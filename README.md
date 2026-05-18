## Contenuto del notebook

Il notebook include:

Data Loading
Data Cleaning
KPI Calculation
Data Visualization
Main Insights
Business Recommendations
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

Questo progetto analizza il dataset **Sample - Superstore**, un dataset retail statunitense di esempio.

L’obiettivo è esplorare vendite, profitto, sconti, categorie prodotto, regioni, segmenti cliente e trend temporali, dimostrando competenze trasferibili di analisi dati, KPI reporting e business-oriented analysis.

Il progetto è stato sviluppato come **progetto portfolio durante il percorso Data & AI Analyst**, con un focus pratico su data cleaning, analisi commerciale, visualizzazioni e costruzione di una dashboard locale con Streamlit.

## Business question

Come variano vendite, profitto e margine in base a categoria, regione, segmento cliente e periodo temporale all’interno di un dataset retail statunitense di esempio?

L’analisi mira a identificare:

- categorie e sottocategorie con performance più forti o critiche;
- differenze tra vendite totali e redditività;
- impatto degli sconti sul profitto;
- trend mensili utili per lettura commerciale e reporting;
- KPI sintetici per supportare decisioni operative.

## Dataset

Dataset utilizzato: **Sample - Superstore.csv**

Il dataset contiene informazioni su ordini, vendite, profitto, sconti, quantità, categorie prodotto, regioni, segmenti cliente e date degli ordini.

Il file si trova nella cartella:

```text
data/Sample - Superstore.csv