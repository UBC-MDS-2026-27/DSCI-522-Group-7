# Contributing to the Bridge Health Predictor Project

This outlines how to propose a change to Bridge Health Predictor Project.

### Fixing typos

Small typos or grammatical errors in documentation may be edited directly using
the GitHub web interface, so long as the changes are made in the _source_ file.

*  YES: you edit the Quarto source file `src/bridge_health_report.qmd`.
*  NO: you edit the rendered `src/bridge_health_report.html` or `pdf`.

### Prerequisites

Before you make a substantial pull request, you should always file an issue and
make sure someone from the team agrees that it's a problem. If you've found a
bug, create an associated issue and illustrate the bug with a minimal 
[reprex](https://www.tidyverse.org/help/#reprex).

### Setting up the project

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) and
[Quarto](https://quarto.org/docs/get-started/), then clone the repository and
create the virtual environment from the root of the repository:

``` bash
git clone https://github.com/UBC-MDS/DSCI_522_project-template-breast-cancer-predictor.git
cd DSCI_522_project-template-breast-cancer-predictor
uv sync
```

To re-run the analysis and render the report:

``` bash
uv run quarto render
```

If your change needs a new Python package, add it with `uv add <package>`
(this pins an exact version in `pyproject.toml` and updates `uv.lock`),
and commit both files.

### Pull request process

* Create a Git branch for each pull request (PR). Do not commit directly to `main`.
* Give a descriptive branch name like `fix-contributing.md` or `add-new-eda`
* Keep each branch small and independent
* Before opening the PR, render the report (`uv run quarto render`)
   to check that the analysis still runs from start to finish.
* Open a PR into `main` and describe what changed and why.
   Link the related issue (e.g., "Closes #12").
* At least one other team member must review and approve the PR before it is merged.
   The reviewer, not the author, merges it.
* New code should follow the PEP8 [style guide](https://peps.python.org/pep-0008/).

### Code of Conduct

Please note that this project is released with a [Contributor Code of
Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to
abide by its terms.

### Attribution

These contributing guidelines were adapted from the [Breast Cancer Predictor contributing guidelines](https://github.com/UBC-MDS/DSCI_522_project-template-breast-cancer-predictor/blob/main/CONTRIBUTING.md).

