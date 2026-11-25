# Ontario Bridge Rehabilitation Predictor

**Authors:** Catriona McIntosh, Jaeda Yurkiw, Jared Chuang & Rshan Hluf

Data analysis project for DSCI 522 (Reproducible and Trustworthy Data Science Workflows); a course in the Master of Data Science program at the University of British Columbia.

## About
Here we attempt to build a classification model that predicts whether an Ontario bridge needs rehabilitation soon, defined as having a Bridge Condition Index (BCI) below 70. We compared a baseline model, logistic regression and a radial basis function support vector classifier (RBF SVC) using cross-validation. On unseen test data, our final classifier, weighted RBF SVC, correctly identified 80 of the 98 bridges needing rehabilitation (recall of 0.82). However, only 38% of the bridges it flagged actually needed rehabilitation, giving an F1 score of 0.52. This means the model catches most bridges at risk but produces many false alarms, which would cost inspection time and money. Given these results, the model could help prioritize bridges for inspection, but should not replace inspections. Further work with more recent data and additional factors, such as traffic and climate, is needed before it could be used in practice.

The dataset used for this project comes from the Government of Ontario. It was sourced from the Data Catalogue and can be found [here](https://data.ontario.ca/dataset/bridge-conditions). The data set contains 5,053 structures: 2,993 bridges and 2,060 culverts. Each row represents a bridge or culvert and includes its structure name and important attributes such as material, structure type, year built, years of its last major and minor rehabilitation, length, width, region, last inspection date, current BCI, and the BCI from each year between 2000 and 2020. Ontario bridges are inspected every two years following the Ontario Structure Inspection Manual (OSIM). The results of each inspection are combined into the BCI, a single score that summarizes the condition of the bridge’s elements. A bridge that is brand new, or that has only recently become the Ministry of Transportation’s responsibility, may not have been inspected yet, so it may not have a BCI (Ontario Ministry of Transportation 2021). Because our target variable is defined using each bridge’s current BCI, the BCI is the key variable in this analysis.

## Report 
The final report can be found [here](https://ubc-mds-2026-27.github.io/DSCI-522-ontario-bridge-rehab-predictor/) (HTML).

## Usage 
We run the analysis in a Docker container, so everyone uses the same software and package versions. The image is published on Docker Hub at [link].

# Setup
First time running the project, install [git](https://git-scm.com/install/) and install and launch [Docker](https://www.docker.com/get-started/), then clone this repository and move into it:
```bash
git clone https://github.com/UBC-MDS-2026-27/DSCI-522-ontario-bridge-rehab-predictor.git
cd DSCI-522-ontario-bridge-rehab-predictor
```
Run all the commands below from the root of this repository.

# 1. Make an ssh key 
If you don't have an ssh key yet, make one and press Enter at each question:
```bash
ssh-keygen -t ed25519
```
The container lets you log in with this key. If you skip this step, Docker makes a folder named `~/.ssh/id_ed25519.pub` instead, and connecting to the container over ssh fails until you delete that folder and make the key.

# 2. Download the image 
```bash
docker compose pull
```

# 3. Run the analysis and render the report
```bash
docker compose run --rm analysis-env uv run quarto render src/bridge_health_report.qmd
```
Rendering runs the whole analysis from scratch: it downloads the data again from the UCI Machine Learning Repository (so you need an internet connection), and overwrites the files in `data/raw/` and `data/processed/`. The rendered report is written to src/bridge_health_report.html, replacing the versions in this repository. Because of `--rm`, the container is removed by itself when the render finishes, so there is nothing to stop afterwards.

## Dependencies
- [uv](https://docs.astral.sh/uv/) (version 0.12 or higher)
- [Quarto](https://quarto.org/) (version 1.10 or higher)
- Python and packages listed in [`pyproject.toml`](pyproject.toml) (exact versions are locked in [`uv.lock`](uv.lock))

## AI use statement
We used Anthropic [Claude Code](https://www.anthropic.com/claude-code) (Opus 5.5), Anthropic [Claude](https://claude.ai) (Opus 5.5), OpenAI [ChatGPT](https://chatgpt.com) (GPT-6), and Google [Gemini](https://gemini.google.com) to help with this project, including debugging code, understanding and improving our data analysis and visualization code, brainstorming our modelling strategy, learning Git and GitHub workflows, generating the column renaming in the data wrangling, formatting Markdown tables, and drafting and revising parts of the report. All AI-generated suggestions and text were reviewed, tested, and edited by the authors, who take full responsibility for the content of this repository.

We did not use an instruction file (such as a `CLAUDE.md`). Some example prompts we used:

- "Should I use grid search or random search for hyperparameter tuning?"
- "Create a python dictionary for the renaming of columns to snake_case."
- "How do I resolve merge conflicts in my Quarto report without losing the EDA visualizations?"
- "Walk me through how to do Table 1 step by step."

## License 
The Ontario Bridge Rehabilitation Predictor report contained herein is licensed under the [Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) License](https://creativecommons.org/licenses/by-nc-sa/4.0/). See [the license file](LICENSE.md) for more information. If re-using/re-mixing please provide attribution and link to this webpage. The software code contained within this repository is licensed under the MIT license. See [the license file](LICENSE.md) for more information.

## References
Ontario Ministry of Transportation. 2021. "Bridge Conditions." Dataset, last updated June 9, 2021. Ontario Data Catalogue. https://data.ontario.ca/dataset/bridge-conditions/resource/703cdf01-ff09-4b86-b017-6e8d87b11fd2.
