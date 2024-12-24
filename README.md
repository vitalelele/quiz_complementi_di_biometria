# Quiz Complementi di Biometria

Quiz a risposta multipla per il corso di Complementi di Biometria.

## Setup

1. Ottieni il codice:
```bash
git clone https://github.com/vitalelele/quiz_complementi_di_biometria.git
```
oppure scarica il .zip dalla pagina del repository

2. Entra nella cartella del progetto:
```bash
cd quiz_complementi_di_biometria
```

## Requisiti
- Python 3.x
- Flask (`pip install flask`)

## Avvio Rapido

1. Installa Flask:
```bash
pip install flask
```

2. Assicurati di avere nella cartella del progetto:
- `main_quiz.py`
- `pull_domande.json` (file con le domande)
- cartella `templates/` con `quiz.html` e `risultati.html`

3. Avvia l'applicazione:
```bash
python main_quiz.py
```

4. Apri nel browser:
```
http://localhost:5000
```

Il quiz presenta domande casuali con possibilità di saltare, vedere la risposta corretta e visualizzare il punteggio finale.
