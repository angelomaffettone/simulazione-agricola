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
"grano": {
        "ettari_min": 10,
        "ettari_max": 50,
        "resa_per_ettaro_min": 3.0,      # tonnellate/ettaro (annata scarsa)
        "resa_per_ettaro_max": 6.5,      # tonnellate/ettaro (annata buona)
        "capacita_raccolta_giornaliera": 8.0,  # tonnellate/giorno
        "costo_per_ettaro": 400,         # euro/ettaro
        "prezzo_vendita_per_ton": 220,   # euro/tonnellata
    }
```

Modificando questi valori è possibile simulare scenari diversi, ad esempio:
- **Annata siccitosa**: abbassare `resa_per_ettaro_max` di grano e pomodori
- **Ampliamento allevamento**: aumentare `capi_max` nel dizionario latte
- **Nuovi macchinari**: aumentare `capacita_raccolta_giornaliera`

Per ottenere risultati riproducibili (utile in fase di test o presentazione), impostare la variabile `seme_casuale` con un numero intero:

```python
seme_casuale = 42   # stessi risultati a ogni esecuzione
```

## Sequenze produttive

### Sequenza A – Raccolta colture (grano e pomodori)

1. Preparazione del terreno → generazione casuale degli ettari disponibili
2. Semina
3. Crescita → generazione casuale della resa per ettaro
4. Raccolta → calcolo dei giorni necessari in base alla capacità dei macchinari
5. Calcolo risultati economici → calcolo della produzione e dei ricavi

### Sequenza B – Allevamento bovino da latte

1. Alimentazione capi→ generazione casuale del numero di capi
2. Mungitura giornaliera→ generazione casuale della produzione per capo
3. Stoccaggio e controllo qualità → verifica della capacità del serbatoio, gestione eccedenza
4. Distribuzione / vendita → calcolo della produzione annuale 
5. Calcolo risultati economici annuali → calcolo ricavi

## Esempio di output

```
=======================================================
  SIMULAZIONE PRODUZIONE – SETTORE PRIMARIO
  Azienda Agricola Mista (colture + allevamento)
=======================================================

[INFO] Seme casuale: non impostato (risultati variabili)

──────────────────── SEQUENZA RACCOLTA – GRANO ────────────────────
Avvio simulazione per la coltura: Grano

► Passo 1/4 – Preparazione del terreno
  Superficie disponibile generata casualmente: 23.5 ettari
► Passo 2/4 – Semina / Trapianto
  Semina completata su 23.5 ettari.
► Passo 3/4 – Fase di crescita
  Resa per ettaro (variabile meteo/clima): 5.46 t/ha
  Produzione totale stimata: 128.31 tonnellate
► Passo 4/4 – Raccolta
  Capacità giornaliera macchinari: 8.0 t/giorno
  Giorni necessari per la raccolta: 16.0 giorni
...
──────────────────── REPORT FINALE – RIEPILOGO PRODUZIONE ────────────────────

  [GRANO]
    Ettari coltivati:    23.5 ha
    Produzione totale:   128.31 t
    Giorni di raccolta:  16.0
    Costi totali:        €   9,400.00
    Ricavi totali:       €  28,228.20
    Margine:             €  18,828.20  ✓
...
───────────────────────────────────────────────────────
  TOTALE COSTI AZIENDA:   €    66,250.00
  TOTALE RICAVI AZIENDA:  €   155,760.70
  MARGINE COMPLESSIVO:    €    89,510.70  ✓ UTILE
───────────────────────────────────────────────────────
```

## Autore

**Angelo Maffettone**  
Corso di laurea: Informatica per le Aziende Digitali (L-31)  
Università Telematica Pegaso  
Anno accademico: 2025/2026
