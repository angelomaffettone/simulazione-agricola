"""
Simulazione della Produzione nel Settore Primario

Scenario: Azienda agricola mista con colture e allevamento.

Output simulati:
  1. Grano          (coltura - sequenza raccolta)
  2. Pomodori        (coltura - sequenza raccolta)
  3. Latte bovino    (allevamento - sequenza allevamento)

Sequenze produttive:
  A. Raccolta colture  → preparazione → semina → crescita → raccolta
  B. Produzione latte  → alimentazione → mungitura → stoccaggio → distribuzione

Autore: Angelo Maffettone
Anno accademico: 2025/2026
"""

import random
import time

# ──────────────────────────────────────────────────────────────────────────────
# 1. CONFIGURAZIONE PARAMETRI (modificabili per scenari diversi)
# ──────────────────────────────────────────────────────────────────────────────

CONFIG = {
    # --- COLTURE ---
    "grano": {
        "ettari_min": 10,
        "ettari_max": 50,
        "resa_per_ettaro_min": 3.0,      # tonnellate/ettaro (annata scarsa)
        "resa_per_ettaro_max": 6.5,      # tonnellate/ettaro (annata buona)
        "capacita_raccolta_giornaliera": 8.0,  # tonnellate/giorno
        "costo_per_ettaro": 400,         # euro/ettaro
        "prezzo_vendita_per_ton": 220,   # euro/tonnellata
    },
    "pomodori": {
        "ettari_min": 5,
        "ettari_max": 20,
        "resa_per_ettaro_min": 40.0,     # tonnellate/ettaro
        "resa_per_ettaro_max": 80.0,
        "capacita_raccolta_giornaliera": 12.0,
        "costo_per_ettaro": 3500,
        "prezzo_vendita_per_ton": 90,
    },
    # --- ALLEVAMENTO ---
    "latte": {
        "capi_min": 20,
        "capi_max": 100,
        "produzione_per_capo_min": 15.0, # litri/capo/giorno (mucca in buona forma)
        "produzione_per_capo_max": 28.0,
        "capacita_stoccaggio_giornaliera": 1000,  # litri/giorno
        "costo_per_capo_giornaliero": 4.5,  # euro/capo/giorno (mangime + cure)
        "prezzo_vendita_per_litro": 0.52,   # euro/litro
        "giorni_produzione": 305,           # giorni lattazione annua
    },
    # --- GLOBALE ---
    "seme_casuale": None,  # Impostare un numero intero per risultati riproducibili
                           # Esempio: 42 → stesso risultato ad ogni esecuzione
                           # None → completamente casuale
}

# ──────────────────────────────────────────────────────────────────────────────
# 2. FUNZIONI DI UTILITÀ
# ──────────────────────────────────────────────────────────────────────────────

def separatore(titolo=""):
    """Stampa una riga separatrice con titolo opzionale."""
    if titolo:
        print(f"\n{'─' * 20} {titolo} {'─' * 20}")
    else:
        print("─" * 55)


def pausa_simulazione(secondi=0.3):
    """Piccola pausa per rendere la simulazione più leggibile."""
    time.sleep(secondi)


# ──────────────────────────────────────────────────────────────────────────────
# 3. SEQUENZA A – RACCOLTA COLTURE
# ──────────────────────────────────────────────────────────────────────────────

def simula_coltura(nome_coltura: str) -> dict:
    """
    Simula la sequenza produttiva di una coltura.

    Sequenza:
        Passo 1 - Preparazione terreno
        Passo 2 - Semina
        Passo 3 - Crescita (variabile casuale)
        Passo 4 - Raccolta
        Passo 5 - Calcolo risultati economici

    Parametri configurabili: ettari, resa, capacità di raccolta,
                             costo per ettaro, prezzo di vendita.

    Args:
        nome_coltura: chiave nel dizionario CONFIG (es. "grano")

    Returns:
        dict con i risultati della simulazione
    """
    cfg = CONFIG[nome_coltura]

    separatore(f"SEQUENZA RACCOLTA – {nome_coltura.upper()}")
    print(f"Avvio simulazione per la coltura: {nome_coltura.capitalize()}\n")
    pausa_simulazione()

    # PASSO 1 – Preparazione terreno
    print("► Passo 1/4 – Preparazione del terreno")
    ettari = round(random.uniform(cfg["ettari_min"], cfg["ettari_max"]), 1)
    print(f"  Superficie disponibile generata casualmente: {ettari} ettari")
    pausa_simulazione()

    # PASSO 2 – Semina
    print("► Passo 2/4 – Semina / Trapianto")
    print(f"  Semina completata su {ettari} ettari.")
    pausa_simulazione()

    # PASSO 3 – Crescita (resa generata casualmente)
    print("► Passo 3/4 – Fase di crescita")
    resa = round(random.uniform(
        cfg["resa_per_ettaro_min"],
        cfg["resa_per_ettaro_max"]
    ), 2)
    produzione_totale = round(ettari * resa, 2)
    print(f"  Resa per ettaro (variabile meteo/clima): {resa} t/ha")
    print(f"  Produzione totale stimata: {produzione_totale} tonnellate")
    pausa_simulazione()

    # PASSO 4 – Raccolta
    print("► Passo 4/4 – Raccolta")
    capacita = cfg["capacita_raccolta_giornaliera"]
    giorni_raccolta = round(produzione_totale / capacita, 1)
    print(f"  Capacità giornaliera macchinari: {capacita} t/giorno")
    print(f"  Giorni necessari per la raccolta: {giorni_raccolta} giorni")
    pausa_simulazione()

    # Calcolo economico
    costo_totale = round(ettari * cfg["costo_per_ettaro"], 2)
    ricavo_totale = round(produzione_totale * cfg["prezzo_vendita_per_ton"], 2)
    margine = round(ricavo_totale - costo_totale, 2)

    risultato = {
        "coltura": nome_coltura,
        "ettari": ettari,
        "resa_per_ettaro": resa,
        "produzione_tonnellate": produzione_totale,
        "giorni_raccolta": giorni_raccolta,
        "costo_totale_eur": costo_totale,
        "ricavo_totale_eur": ricavo_totale,
        "margine_eur": margine,
    }
    return risultato


# ──────────────────────────────────────────────────────────────────────────────
# 4. SEQUENZA B – PRODUZIONE LATTE (ALLEVAMENTO)
# ──────────────────────────────────────────────────────────────────────────────

def simula_allevamento_latte() -> dict:
    """
    Simula la sequenza produttiva di un allevamento bovino da latte.

    Sequenza:
        Passo 1 - Alimentazione capi
        Passo 2 - Mungitura giornaliera
        Passo 3 - Stoccaggio e controllo capacità
        Passo 4 - Distribuzione / vendita
        Passo 5 - Calcolo risultati economici annuali

    Parametri configurabili: numero capi, produzione per capo,
                             costo gestione, prezzo latte, giorni lattazione.

    Returns:
        dict con i risultati della simulazione
    """
    cfg = CONFIG["latte"]

    separatore("SEQUENZA ALLEVAMENTO – PRODUZIONE LATTE BOVINO")
    print("Avvio simulazione per l'allevamento bovino da latte\n")
    pausa_simulazione()

    # PASSO 1 – Alimentazione
    print("► Passo 1/4 – Alimentazione capi")
    n_capi = random.randint(cfg["capi_min"], cfg["capi_max"])
    print(f"  Numero capi in lattazione (casuale): {n_capi} mucche")
    print(f"  Razione giornaliera e integratori somministrati.")
    pausa_simulazione()

    # PASSO 2 – Mungitura
    print("► Passo 2/4 – Mungitura giornaliera")
    prod_per_capo = round(random.uniform(
        cfg["produzione_per_capo_min"],
        cfg["produzione_per_capo_max"]
    ), 1)
    produzione_giornaliera = round(n_capi * prod_per_capo, 1)
    print(f"  Produzione media per capo: {prod_per_capo} litri/giorno")
    print(f"  Produzione totale giornaliera: {produzione_giornaliera} litri")
    pausa_simulazione()

    # PASSO 3 – Stoccaggio
    print("► Passo 3/4 – Stoccaggio e controllo capacità")
    capacita = cfg["capacita_stoccaggio_giornaliera"]
    if produzione_giornaliera > capacita:
        eccedenza = round(produzione_giornaliera - capacita, 1)
        print(f"  ⚠️  Attenzione: capacità stoccaggio superata!")
        print(f"  Stoccato: {capacita} litri | Eccedenza non stoccabile: {eccedenza} litri")
        produzione_effettiva_giornaliera = capacita
    else:
        print(f"  Tutto il latte stoccato correttamente ({produzione_giornaliera} litri)")
        produzione_effettiva_giornaliera = produzione_giornaliera
    pausa_simulazione()

    # PASSO 4 – Distribuzione
    print("► Passo 4/4 – Distribuzione / Vendita")
    giorni = cfg["giorni_produzione"]
    produzione_annuale = round(produzione_effettiva_giornaliera * giorni, 0)
    print(f"  Giorni di lattazione annui: {giorni}")
    print(f"  Produzione annuale effettiva: {produzione_annuale:,.0f} litri")
    pausa_simulazione()

    # Calcolo economico
    costo_annuale = round(n_capi * cfg["costo_per_capo_giornaliero"] * giorni, 2)
    ricavo_annuale = round(produzione_annuale * cfg["prezzo_vendita_per_litro"], 2)
    margine = round(ricavo_annuale - costo_annuale, 2)

    risultato = {
        "prodotto": "latte",
        "n_capi": n_capi,
        "produzione_per_capo_litri_giorno": prod_per_capo,
        "produzione_giornaliera_litri": produzione_giornaliera,
        "produzione_annuale_litri": produzione_annuale,
        "giorni_lattazione": giorni,
        "costo_totale_eur": costo_annuale,
        "ricavo_totale_eur": ricavo_annuale,
        "margine_eur": margine,
    }
    return risultato


# ──────────────────────────────────────────────────────────────────────────────
# 5. REPORT FINALE
# ──────────────────────────────────────────────────────────────────────────────

def stampa_report(risultati: list):
    """
    Stampa il riepilogo finale con tutti i risultati della simulazione.

    Args:
        risultati: lista di dict restituiti dalle funzioni di simulazione
    """
    separatore("REPORT FINALE – RIEPILOGO PRODUZIONE")

    totale_costi = 0
    totale_ricavi = 0
    totale_margine = 0

    for r in risultati:
        nome = r.get("coltura") or r.get("prodotto")
        print(f"\n  [{nome.upper()}]")

        if nome in ("grano", "pomodori"):
            print(f"    Ettari coltivati:    {r['ettari']} ha")
            print(f"    Produzione totale:   {r['produzione_tonnellate']} t")
            print(f"    Giorni di raccolta:  {r['giorni_raccolta']}")
        else:
            print(f"    Capi in lattazione:  {r['n_capi']}")
            print(f"    Prod. annuale:       {r['produzione_annuale_litri']:,.0f} litri")

        print(f"    Costi totali:        € {r['costo_totale_eur']:>10,.2f}")
        print(f"    Ricavi totali:       € {r['ricavo_totale_eur']:>10,.2f}")
        margine = r['margine_eur']
        simbolo = "✓" if margine >= 0 else "✗"
        print(f"    Margine:             € {margine:>10,.2f}  {simbolo}")

        totale_costi += r['costo_totale_eur']
        totale_ricavi += r['ricavo_totale_eur']
        totale_margine += r['margine_eur']

    separatore()
    print(f"  TOTALE COSTI AZIENDA:   € {totale_costi:>12,.2f}")
    print(f"  TOTALE RICAVI AZIENDA:  € {totale_ricavi:>12,.2f}")
    print(f"  MARGINE COMPLESSIVO:    € {totale_margine:>12,.2f}", end="")
    print("  ✓ UTILE" if totale_margine >= 0 else "  ✗ PERDITA")
    separatore()


# ──────────────────────────────────────────────────────────────────────────────
# 6. MAIN – PUNTO DI INGRESSO
# ──────────────────────────────────────────────────────────────────────────────

def main():
    print("=" * 55)
    print("  SIMULAZIONE PRODUZIONE – SETTORE PRIMARIO")
    print("  Azienda Agricola Mista (colture + allevamento)")
    print("=" * 55)

    # Imposta il seme casuale (riproducibilità opzionale)
    if CONFIG["seme_casuale"] is not None:
        random.seed(CONFIG["seme_casuale"])
        print(f"\n[INFO] Seme casuale impostato: {CONFIG['seme_casuale']}")
    else:
        print("\n[INFO] Seme casuale: non impostato (risultati variabili)")

    risultati = []

    # ── SEQUENZA A: Colture ─────────────────────────────────────────
    # Output 1: Grano
    res_grano = simula_coltura("grano")
    risultati.append(res_grano)

    # Output 2: Pomodori
    res_pomodori = simula_coltura("pomodori")
    risultati.append(res_pomodori)

    # ── SEQUENZA B: Allevamento ─────────────────────────────────────
    # Output 3: Latte bovino
    res_latte = simula_allevamento_latte()
    risultati.append(res_latte)

    # ── Report finale ───────────────────────────────────────────────
    stampa_report(risultati)


if __name__ == "__main__":
    main()