# simulazione produzione settore primario
# progetto python - azienda agricola con grano, pomodori e allevamento bovino
# autore: [Nome Cognome]
# anno accademico 2024/2025

import random
import time

# parametri configurabili - modificare questi valori per cambiare scenario
# ho messo i valori in un dizionario cosi sono tutti in un posto solo

parametri_grano = {
    "ettari_min": 10,
    "ettari_max": 50,
    "resa_min": 3.0,       # tonnellate per ettaro, annata brutta
    "resa_max": 6.5,       # tonnellate per ettaro, annata buona
    "raccolta_giorno": 8.0,  # quante tonnellate riesce a raccogliere al giorno
    "costo_ettaro": 400,
    "prezzo_ton": 220,
}

parametri_pomodori = {
    "ettari_min": 5,
    "ettari_max": 20,
    "resa_min": 40.0,
    "resa_max": 80.0,
    "raccolta_giorno": 12.0,
    "costo_ettaro": 3500,
    "prezzo_ton": 90,
}

parametri_latte = {
    "capi_min": 20,
    "capi_max": 100,
    "litri_per_capo_min": 15.0,
    "litri_per_capo_max": 28.0,
    "max_stoccaggio": 1000,   # litri al giorno che riesce a conservare
    "costo_capo_giorno": 4.5,
    "prezzo_litro": 0.52,
    "giorni_lattazione": 305,
}

# seme casuale: mettere un numero per avere sempre gli stessi risultati
# oppure lasciare None per risultati diversi ogni volta
SEME = None


# funzione per stampare una linea di separazione
def linea(testo=""):
    if testo != "":
        print("\n--- " + testo + " ---")
    else:
        print("-" * 40)


# piccola pausa per rendere l'output piu leggibile
def attendi():
    time.sleep(0.4)


# -------------------------------------------------------
# SEQUENZA A: simulazione raccolta coltura
# -------------------------------------------------------

def simula_coltura(nome, params):
    # questa funzione simula tutta la sequenza produttiva di una coltura
    # prende il nome e i parametri come input e restituisce i risultati

    linea("SEQUENZA RACCOLTA - " + nome.upper())
    attendi()

    # passo 1: preparazione terreno
    print("Passo 1 - Preparazione del terreno")
    ettari = round(random.uniform(params["ettari_min"], params["ettari_max"]), 1)
    print("  ettari disponibili: " + str(ettari))
    attendi()

    # passo 2: semina
    print("Passo 2 - Semina")
    print("  semina completata su " + str(ettari) + " ettari")
    attendi()

    # passo 3: crescita - la resa dipende dal meteo quindi e casuale
    print("Passo 3 - Crescita")
    resa = round(random.uniform(params["resa_min"], params["resa_max"]), 2)
    produzione = ettari * resa
    produzione = round(produzione, 2)
    print("  resa per ettaro: " + str(resa) + " t/ha")
    print("  produzione totale: " + str(produzione) + " tonnellate")
    attendi()

    # passo 4: raccolta - calcolo quanti giorni ci vogliono
    print("Passo 4 - Raccolta")
    giorni = produzione / params["raccolta_giorno"]
    giorni = round(giorni, 1)
    print("  capacita giornaliera: " + str(params["raccolta_giorno"]) + " t/giorno")
    print("  giorni necessari: " + str(giorni))
    attendi()

    # calcolo economico
    costo = ettari * params["costo_ettaro"]
    costo = round(costo, 2)
    ricavo = produzione * params["prezzo_ton"]
    ricavo = round(ricavo, 2)
    margine = ricavo - costo
    margine = round(margine, 2)

    # metto tutto in un dizionario per poi usarlo nel report
    risultato = {}
    risultato["tipo"] = nome
    risultato["ettari"] = ettari
    risultato["resa"] = resa
    risultato["produzione_ton"] = produzione
    risultato["giorni_raccolta"] = giorni
    risultato["costo"] = costo
    risultato["ricavo"] = ricavo
    risultato["margine"] = margine

    return risultato


# -------------------------------------------------------
# SEQUENZA B: simulazione allevamento bovino da latte
# -------------------------------------------------------

def simula_latte(params):
    # questa funzione e diversa dalla precedente perche l'allevamento
    # ha una logica diversa rispetto alla raccolta delle colture

    linea("SEQUENZA ALLEVAMENTO - LATTE BOVINO")
    attendi()

    # passo 1: alimentazione
    print("Passo 1 - Alimentazione")
    n_capi = random.randint(params["capi_min"], params["capi_max"])
    print("  numero mucche: " + str(n_capi))
    attendi()

    # passo 2: mungitura giornaliera
    print("Passo 2 - Mungitura")
    litri_capo = round(random.uniform(params["litri_per_capo_min"], params["litri_per_capo_max"]), 1)
    litri_totali = round(n_capi * litri_capo, 1)
    print("  litri per capo al giorno: " + str(litri_capo))
    print("  totale giornaliero: " + str(litri_totali) + " litri")
    attendi()

    # passo 3: stoccaggio - controllo se supera la capacita del serbatoio
    print("Passo 3 - Stoccaggio")
    if litri_totali > params["max_stoccaggio"]:
        # produzione troppa, non riesce a stoccare tutto
        eccedenza = round(litri_totali - params["max_stoccaggio"], 1)
        print("  ATTENZIONE: capacita serbatoio superata!")
        print("  stoccato: " + str(params["max_stoccaggio"]) + " litri")
        print("  perso: " + str(eccedenza) + " litri")
        litri_effettivi = params["max_stoccaggio"]
    else:
        print("  tutto stoccato: " + str(litri_totali) + " litri")
        litri_effettivi = litri_totali
    attendi()

    # passo 4: distribuzione annuale
    print("Passo 4 - Distribuzione")
    giorni = params["giorni_lattazione"]
    litri_anno = round(litri_effettivi * giorni, 0)
    print("  giorni di lattazione: " + str(giorni))
    print("  produzione annuale: " + str(litri_anno) + " litri")
    attendi()

    # calcolo costi e ricavi annuali
    costo_anno = n_capi * params["costo_capo_giorno"] * giorni
    costo_anno = round(costo_anno, 2)
    ricavo_anno = litri_anno * params["prezzo_litro"]
    ricavo_anno = round(ricavo_anno, 2)
    margine = round(ricavo_anno - costo_anno, 2)

    risultato = {}
    risultato["tipo"] = "latte"
    risultato["n_capi"] = n_capi
    risultato["litri_giorno"] = litri_totali
    risultato["litri_anno"] = litri_anno
    risultato["costo"] = costo_anno
    risultato["ricavo"] = ricavo_anno
    risultato["margine"] = margine

    return risultato


# -------------------------------------------------------
# REPORT FINALE
# -------------------------------------------------------

def stampa_report(lista_risultati):
    linea("REPORT FINALE")

    tot_costi = 0
    tot_ricavi = 0
    tot_margine = 0

    for r in lista_risultati:
        print("\n[" + r["tipo"].upper() + "]")

        # stampo dati diversi a seconda del tipo
        if r["tipo"] == "latte":
            print("  Capi allevati:     " + str(r["n_capi"]))
            print("  Litri/anno:        " + str(r["litri_anno"]))
        else:
            print("  Ettari:            " + str(r["ettari"]))
            print("  Produzione (ton):  " + str(r["produzione_ton"]))
            print("  Giorni raccolta:   " + str(r["giorni_raccolta"]))

        print("  Costo totale:      " + str(r["costo"]) + " euro")
        print("  Ricavo totale:     " + str(r["ricavo"]) + " euro")

        if r["margine"] >= 0:
            print("  Margine:           " + str(r["margine"]) + " euro  (positivo)")
        else:
            print("  Margine:           " + str(r["margine"]) + " euro  (negativo!)")

        tot_costi = tot_costi + r["costo"]
        tot_ricavi = tot_ricavi + r["ricavo"]
        tot_margine = tot_margine + r["margine"]

    linea()
    print("TOTALE COSTI:    " + str(round(tot_costi, 2)) + " euro")
    print("TOTALE RICAVI:   " + str(round(tot_ricavi, 2)) + " euro")
    print("MARGINE TOTALE:  " + str(round(tot_margine, 2)) + " euro")

    if tot_margine >= 0:
        print("=> risultato positivo, l'azienda e in utile")
    else:
        print("=> risultato negativo, l'azienda e in perdita")

    linea()


# -------------------------------------------------------
# PROGRAMMA PRINCIPALE
# -------------------------------------------------------

print("=" * 45)
print("SIMULAZIONE AZIENDA AGRICOLA MISTA")
print("=" * 45)

# imposto il seme se definito
if SEME is not None:
    random.seed(SEME)
    print("seme casuale impostato: " + str(SEME))
else:
    print("nessun seme impostato, risultati casuali")

# lista dove salvo i risultati di ogni simulazione
tutti_i_risultati = []

# sequenza A - colture
ris_grano = simula_coltura("grano", parametri_grano)
tutti_i_risultati.append(ris_grano)

ris_pomodori = simula_coltura("pomodori", parametri_pomodori)
tutti_i_risultati.append(ris_pomodori)

# sequenza B - allevamento
ris_latte = simula_latte(parametri_latte)
tutti_i_risultati.append(ris_latte)

# report finale con tutti i dati
stampa_report(tutti_i_risultati)
