# Simulazione Azienda Agricola Mista

Progetto Python sviluppato come Project Work per il corso di laurea in Informatica per le Aziende Digitali (L-31) presso l'Università Telematica Pegaso.

## Descrizione

Il programma simula il processo produttivo di un'azienda agricola mista che opera su tre tipologie di output:

- **Grano** – coltura cerealicola (Sequenza A: raccolta colture)
- **Pomodori** – coltura orticola (Sequenza A: raccolta colture)  
- **Latte bovino** – allevamento bovino da latte (Sequenza B: allevamento)

Le quantità produttive vengono generate casualmente a ogni esecuzione, simulando la variabilità naturale del settore primario (meteo, stagionalità, numero di capi). Il programma calcola per ogni output i costi, i ricavi e il margine operativo, restituendo un report finale con il bilancio complessivo dell'azienda.

## Struttura del progetto

```
simulazione-agricola/
│
├── simulazione_agricola.py   # programma principale
├── README.md                 # questo file
├── requirements.txt          # dipendenze (nessuna libreria esterna)
└── .gitignore                # file da escludere dal repository
```

## Come eseguire il programma

### Requisiti

- Python 3.x installato ([scarica da python.org](https://www.python.org/downloads/))
- Nessuna libreria esterna richiesta (solo moduli standard: `random`, `time`)

### Esecuzione

```bash
python simulazione_agricola.py
```

oppure, su alcuni sistemi:

```bash
python3 simulazione_agricola.py
```

## Configurazione degli scenari

All'inizio del file `simulazione_agricola.py` si trovano tre dizionari di parametri configurabili:

```python
parametri_grano = {
    "ettari_min": 10,
    "ettari_max": 50,
    "resa_min": 3.0,        # annata sfavorevole
    "resa_max": 6.5,        # annata ottimale
    "raccolta_giorno": 8.0, # tonnellate/giorno
    "costo_ettaro": 400,
    "prezzo_ton": 220,
}
```

Modificando questi valori è possibile simulare scenari diversi, ad esempio:
- **Annata siccitosa**: abbassare `resa_max` di grano e pomodori
- **Ampliamento allevamento**: aumentare `capi_max` nel dizionario latte
- **Nuovi macchinari**: aumentare `raccolta_giorno`

Per ottenere risultati riproducibili (utile in fase di test o presentazione), impostare la variabile `SEME` con un numero intero:

```python
SEME = 42   # stessi risultati a ogni esecuzione
```

## Sequenze produttive

### Sequenza A – Raccolta colture (grano e pomodori)

1. Preparazione del terreno → generazione casuale degli ettari disponibili
2. Semina
3. Crescita → generazione casuale della resa per ettaro
4. Raccolta → calcolo dei giorni necessari in base alla capacità dei macchinari

### Sequenza B – Allevamento bovino da latte

1. Alimentazione → generazione casuale del numero di capi
2. Mungitura → generazione casuale della produzione per capo
3. Stoccaggio → verifica della capacità del serbatoio, gestione eccedenza
4. Distribuzione → calcolo della produzione annuale e dei ricavi

## Esempio di output

```
=============================================
SIMULAZIONE AZIENDA AGRICOLA MISTA
=============================================
nessun seme impostato, risultati casuali

--- SEQUENZA RACCOLTA - GRANO ---
Passo 1 - Preparazione del terreno
  ettari disponibili: 34.2
Passo 2 - Semina
  semina completata su 34.2 ettari
Passo 3 - Crescita
  resa per ettaro: 5.43 t/ha
  produzione totale: 185.71 tonnellate
Passo 4 - Raccolta
  capacita giornaliera: 8.0 t/giorno
  giorni necessari: 23.2
...
--- REPORT FINALE ---
TOTALE COSTI:    148230.5 euro
TOTALE RICAVI:   261874.3 euro
MARGINE TOTALE:  113643.8 euro
=> risultato positivo, l'azienda e in utile
```

## Autore

**Angelo Maffettone**  
Corso di laurea: Informatica per le Aziende Digitali (L-31)  
Università Telematica Pegaso  
Anno accademico: 2025/2026
