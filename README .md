# Simulazione della produzione agricola

Questo progetto nasce dal project work sulla digitalizzazione dell'impresa e consiste nella realizzazione di un programma Python che simula, in modo semplificato, alcuni processi produttivi di un'azienda agricola.

Ho scelto di immaginare un'azienda agricola mista, quindi con una parte dedicata alle coltivazioni e una parte dedicata all'allevamento bovino da latte.

Il programma simula tre produzioni:

- grano
- pomodori
- latte bovino

L'idea non è quella di creare un vero gestionale agricolo, ma di utilizzare Python per rappresentare alcune situazioni che possono verificarsi durante la produzione e vedere come cambiano i risultati.

## Come funziona

Le colture seguono una prima sequenza:

**preparazione del terreno → semina → crescita → raccolta**

Per grano e pomodori il programma genera casualmente la superficie coltivata e la resa per ettaro. Da questi valori calcola la produzione totale e, in base alla capacità giornaliera dei macchinari, stima i giorni necessari per la raccolta.

Per il latte la sequenza è diversa:

**alimentazione → mungitura → stoccaggio → distribuzione/vendita**

In questo caso vengono generati casualmente il numero di capi in lattazione e la produzione giornaliera di latte per capo. Il programma controlla poi la capacità del serbatoio: se viene prodotto più latte di quanto sia possibile stoccare, la parte eccedente non viene considerata nella produzione effettivamente vendibile.

Alla fine vengono calcolati costi, ricavi e margine per ciascuna produzione e viene mostrato un riepilogo complessivo dell'azienda.

## Una cosa importante sulla casualità

I risultati non sono sempre uguali, perché alcune quantità vengono generate utilizzando il modulo `random` di Python.

Per esempio, il numero di bovini viene generato come numero intero, mentre la resa per ettaro viene generata come valore compreso in un determinato intervallo.

Se si vuole ottenere sempre lo stesso risultato, nel dizionario `CONFIG` è possibile impostare un valore per il `seme_casuale`.

Per esempio:

```python
"seme_casuale": 42
```

Lasciandolo invece impostato a:

```python
"seme_casuale": None
```

il risultato cambia ad ogni esecuzione.

## Dove si modificano i parametri

Ho cercato di tenere tutti i valori principali concentrati all'inizio del programma, all'interno del dizionario `CONFIG`.

Qui si possono modificare, ad esempio:

- ettari minimi e massimi;
- resa minima e massima;
- capacità di raccolta;
- costi per ettaro;
- prezzi di vendita;
- numero minimo e massimo di bovini;
- produzione di latte per capo;
- capacità di stoccaggio;
- giorni di produzione.

In questo modo è possibile provare scenari diversi senza dover andare a modificare la logica delle funzioni.

## Come eseguire il programma

È sufficiente avere Python 3 installato.

Dal terminale, dopo essersi posizionati nella cartella del progetto:

```bash
python simulazione_agricola.py
```

Il programma utilizza solamente moduli della libreria standard di Python (`random` e `time`), quindi non sono necessarie librerie esterne.

## Struttura del progetto

La repository contiene:

```text
simulazione-agricola/
│
├── simulazione_agricola.py
├── README.md
├── requirements.txt
└── .gitignore
```

La parte principale del programma è contenuta nel file `simulazione_agricola.py`.

Le funzioni principali sono:

- `simula_coltura()` per grano e pomodori;
- `simula_allevamento_latte()` per la produzione di latte;
- `stampa_report()` per il riepilogo finale;
- `main()` per avviare le varie simulazioni.

## Limiti del modello

Il programma è volutamente una semplificazione.

Non vengono, ad esempio, simulati direttamente eventi meteorologici come siccità, grandine o piogge eccessive. La variabilità della resa viene rappresentata attraverso valori casuali.

Anche la parte economica considera principalmente i costi variabili inseriti nel modello e non comprende tutti i costi che avrebbe una vera azienda agricola, come ammortamenti, affitti, costi amministrativi e altri costi fissi.

Inoltre, ogni esecuzione rappresenta una singola simulazione. Per ottenere un'analisi statistica più completa sarebbe interessante automatizzare molte esecuzioni e confrontare la distribuzione dei risultati.

## Perché ho scelto questo approccio

Ho preferito mantenere il programma abbastanza semplice da poter essere letto e modificato facilmente, invece di cercare di costruire un simulatore troppo complesso.

L'obiettivo principale del progetto era infatti mostrare come alcuni concetti di programmazione, probabilità e gestione dei processi possano essere applicati a un problema concreto del settore primario.

## Repository

Il codice completo del progetto è disponibile su GitHub:

https://github.com/angelomaffettone/simulazione-agricola