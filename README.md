
# Quiz Complementi di Biometria

App web basata su **Flask** per la gestione di un quiz sui complementi di biometria. Permette di rispondere a domande randomizzate con feedback immediato.

## Requisiti

- Python 3.6+
- pip

## Installazione

1. **Clona il repository:**

   ```bash
   git clone https://github.com/vitalelele/quiz_complementi_di_biometria.git
   cd quiz_complementi_di_biometria
   ```

2. **Crea e attiva un ambiente virtuale:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Su Windows: venv\Scripts\activate
   ```

3. **Installa le dipendenze:**

   ```bash
   pip install flask
   ```

4. **Aggiungi il file `domande.json`:**

   Assicurati di avere il file `domande.json` con le domande del quiz nella stessa directory.

5. **Avvia il server:**

   ```bash
   python main_quiz.py
   ```

6. **Visita l'app:**

   Vai su `http://127.0.0.1:5000` nel tuo browser.

## Struttura del Progetto

- `app.py`: Logica dell'applicazione Flask.
- `domande.json`: Domande del quiz.
- `templates/`: Template HTML.
- `static/`: Risorse statiche (CSS, JS).
- `requirements.txt`: Dipendenze Python.

## Funzionamento

1. **Inizio del quiz**: Le domande vengono caricate in ordine casuale.
2. **Risposta**: Dopo ogni risposta, viene mostrato un feedback.
3. **Salta domanda**: Le domande saltate vengono registrate.
4. **Mostra risposta**: Mostra la risposta corretta senza avanzare al prossimo step.

## Deploy su Heroku

1. **Crea un'app su Heroku:**

   ```bash
   heroku create nome-della-tua-app
   ```

2. **Push del codice su Heroku:**

   ```bash
   git push heroku master
   ```

3. **Apri l'app:**

   ```bash
   heroku open
   ```

## Licenza

MIT
```

### Modifiche:
- Ho aggiunto gli spazi giusti per la chiarezza della formattazione.
- Ho separato in modo visibile ogni passaggio per facilitarne la lettura e l'uso.
****
