## Contenuto del notebook

Il notebook include:

Data Loading
Data Cleaning
KPI Calculation
Data Visualization
Main Insights
Recommendations
Limitations and Conclusion
Principali insight
Le vendite totali non coincidono sempre con la redditività.
Alcune categorie generano vendite elevate ma margini più deboli.
Gli sconti più alti tendono a ridurre il profitto medio.
Alcune sottocategorie mostrano perdite significative o margini negativi.
Le regioni devono essere confrontate non solo per profitto totale, ma anche per margine percentuale.
Il trend mensile delle vendite mostra variazioni utili per pianificazione commerciale e gestione promozionale.
Dashboard

La dashboard Streamlit permette di filtrare i dati per:

anno;
regione;
categoria;
segmento cliente.

Include KPI principali e visualizzazioni semplici per esplorare vendite, profitto e andamento mensile.

## How to Run the Notebook

Clone or download this repository.
Make sure the dataset files are stored inside the data/ folder.
Install the required libraries:
pip install -r requirements.txt

# Superstore Sales Analysis Dashboard

## Descrizione del progetto

Questo progetto analizza il dataset **Sample - Superstore** con l’obiettivo di esplorare vendite, profitto, sconti, categorie, regioni, segmenti cliente e trend temporali.

Il lavoro è stato sviluppato come progetto accademico per dimostrare competenze base di analisi dati con Python e la capacità di costruire una dashboard interattiva con Streamlit.

## Obiettivo dell’analisi

L’obiettivo principale è identificare pattern utili, con particolare attenzione a:

- performance di vendita;
- redditività per categoria e regione;
- impatto degli sconti sul profitto;
- sottocategorie con performance critiche;
- andamento delle vendite nel tempo.

## Dataset utilizzato

Dataset: **Sample - Superstore.csv**

Il dataset contiene informazioni su ordini, vendite, profitto, sconti, quantità, categorie prodotto, regioni, segmenti cliente e date degli ordini.

Il file si trova nella cartella:

```text
data/Sample - Superstore.csv
