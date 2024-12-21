from flask import Flask, render_template, request, redirect, url_for, session
import random
import json
import os

# File per salvare lo stato del quiz
QUIZ_STATE_FILE = 'quiz_state.json'

# Leggi il file JSON delle domande
with open('pull_finale.json', 'r', encoding='utf-8') as f:
    domande = json.load(f)

# Verifica che domande sia un dizionario
if not isinstance(domande, dict):
    raise ValueError("Il file delle domande non contiene un dizionario valido.")

app = Flask(__name__)
app.secret_key = 'chiave_segreta'

def save_quiz_state(state):
    """Salva lo stato del quiz in un file JSON."""
    with open(QUIZ_STATE_FILE, 'w', encoding='utf-8') as f:
        json.dump(state, f)

def load_quiz_state():
    """Carica lo stato del quiz dal file JSON, se esiste."""
    if os.path.exists(QUIZ_STATE_FILE):
        with open(QUIZ_STATE_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None

@app.route('/')
def index():
    # Carica stato salvato o inizia un nuovo quiz
    quiz_state = load_quiz_state()
    if quiz_state:
        session.update(quiz_state)
    else:
        session['domande'] = random.sample(list(domande.keys()), len(domande))
        session['punti'] = 0
        session['indice'] = 0
        session['saltate'] = []
        session['mostrate'] = []
        session['feedback'] = None
        save_quiz_state(session)

    indice_corrente = session['indice']

    if indice_corrente >= len(session['domande']):
        return redirect(url_for('risultati'))

    # Recupera la domanda corrente
    domanda_id = session['domande'][indice_corrente]

    # Verifica se la domanda esiste nel dizionario
    if str(domanda_id) in domande:
        domanda = domande[str(domanda_id)]  # Usa str per garantire l'accesso corretto
    else:
        # Gestisci l'errore se la domanda non è presente nel dizionario
        domanda = None
        session['feedback'] = 'Errore: domanda non valida.'
    
    # Procedi solo se la domanda è valida
    if domanda:
        # Verifica se la domanda è un dizionario e contiene la chiave 'risposte'
        if isinstance(domanda, dict) and 'risposte' in domanda and isinstance(domanda['risposte'], list):
            risposte = random.sample(domanda['risposte'], len(domanda['risposte']))
        else:
            risposte = ["Errore: risposte non disponibili"]
    else:
        risposte = []

    feedback = session.pop('feedback', None)

    return render_template('quiz.html', domanda=domanda, risposte=risposte, indice=indice_corrente + 1, totale=len(session['domande']), feedback=feedback)

@app.route('/rispondi', methods=['POST'])
def rispondi():
    azione = request.form.get('azione')
    domanda_id = session['domande'][session['indice']]

    # Verifica che la domanda esista
    if str(domanda_id) in domande:
        domanda = domande[str(domanda_id)]
    else:
        session['feedback'] = 'Errore: domanda non valida.'
        return redirect(url_for('index'))

    # Verifica che la domanda contenga la risposta giusta
    if isinstance(domanda, dict) and 'giusta' in domanda:
        if azione == 'salta':
            session['saltate'].append(domanda_id)
            session['feedback'] = 'Domanda saltata!'
            session['indice'] += 1
        elif azione == 'mostra':
            session['feedback'] = f'La risposta corretta è: {domanda["giusta"]}.'
            session['mostrate'].append(domanda_id)
        else:
            risposta = request.form.get('risposta')
            if risposta == domanda['giusta']:
                session['punti'] += 1
                session['feedback'] = 'Corretto! 🎉'
                session['indice'] += 1  # Avanza solo se la risposta è corretta
            else:
                # Se la risposta è sbagliata, non si avanza
                session['feedback'] = f'Sbagliato! La risposta corretta era: {domanda["giusta"]}. Prova ancora.'
    else:
        session['feedback'] = 'Errore: domanda non valida.'
    
    save_quiz_state(session)  # Salva lo stato del quiz
    return redirect(url_for('index'))

@app.route('/risultati')
def risultati():
    punteggio = session.get('punti', 0)
    totale = len(session['domande'])
    saltate = session.get('saltate', [])
    mostrate = session.get('mostrate', [])
    if os.path.exists(QUIZ_STATE_FILE):
        os.remove(QUIZ_STATE_FILE)  
    
    return render_template('risultati.html', punteggio=punteggio, totale=totale, saltate=saltate, mostrate=mostrate, domande=domande)

@app.route('/reset')
def reset():
    """Ricomincia il quiz da capo."""
    if os.path.exists(QUIZ_STATE_FILE):
        os.remove(QUIZ_STATE_FILE)
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)