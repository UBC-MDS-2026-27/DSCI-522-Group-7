# [Ontario Bridge Rehabilitation Predictor]

**Authors:** [Jaeda Yurkiw], [Catriona McIntosh], [Jared Chuang] & [Rshan Hluf]

Data analysis project for DSCI 522 (Reproducible and Trustworthy Data Science Workflows); a course in the Master of Data Science program at the University of British Columbia.

## About
Here we attempt to build a classification model that predicts whether an Ontario bridge needs rehabilitation soon, defined as having a Bridge Condition Index (BCI) below 70, the threshold of “good” condition, below which maintenance is usually scheduled within five years. We compared a baseline model, logistic regression and a radial basis function support vector classifier (RBF SVC) using cross-validation. On unseen test data, our final classifier, weighted RBF SVC, correctly identified 80 of the 98 bridges needing rehabilitation (recall of 0.82). However, only 38% of the bridges it flagged actually needed rehabilitation, giving an F1 score of 0.52. This means the model catches most bridges at risk but produces many false alarms, which would cost inspection time and money. Given these results, the model could help prioritize bridges for inspection, but should not replace inspections. Further work with more recent data and additional factors, such as traffic and climate, is needed before it could be used in practice.

The dataset used for this project comes from the Government of Ontario. It was sourced from the Data Catologue and can be found [here](https://data.ontario.ca/dataset/bridge-conditions). The data set contains 5,053 structures: 2,993 bridges and 2,060 culverts. Each row represents a bridge or culvert and includes its structure name and important attributes such as material, structure type, year built, years of its last major and minor rehabilitation, length, width, region, last inspection date, current Bridge Condition Index (BCI), and the BCI from each year between 2000 and 2020. Ontario bridges are inspected every two years following the Ontario Structure Inspection Manual (OSIM). The results of each inspection are combined into the Bridge Condition Index (BCI), a single score that summarizes the condition of the bridge’s elements. A bridge that is brand new, or that has only recently become the Ministry of Transportation’s responsibility, may not have been inspected yet, so it may not have a BCI (Government of Ontario 2020). Because our target variable is defined using each bridge’s current BCI, the BCI is the key variable in this analysis.

We downloaded the data using the code below. The code downloads the Bridge Conditions data from the Ontario Data Catalogue as a CSV file and saves it as `bridge_data_raw.csv` in `data/raw/`. We kept only bridges, removing culverts, and removed 31 bridges with no recorded current BCI, leaving 2,962 bridges.

## Report 
The final report can be found [here]([GitHub Pages link]) (HTML), or as a PDF ([GitHub Pages link]).

## Usage 
First time running the project, install [uv](https://docs.astral.sh/uv/getting-started/installation/) and [Quarto](https://quarto.org/docs/get-started/), then clone this repository and move into it:

```bash
git clone https://github.com/UBC-MDS-2026-27/DSCI-522-Group-7.git
cd DSCI-522-Group-7
```

Then run the following from the root of this repository to create the virtual environment:
```bash
uv sync
```

To run the analysis and render the report, run the following from the root of this repository:
```bash
uv run quarto render
```

Rendering runs the whole analysis from scratch: it downloads the data again from the Ontario Data Catalogue (so you need an internet connection), and overwrites the files in `data/raw/` and `data/processed/`. The rendered report is written to `src/bridge_health_report.html` and `src/bridge_health_report.pdf`, replacing the versions in this repository.

## Dependencies
- [uv] (version 0.12 or higher)
- [Quarto] (version 1.10 or higher)



