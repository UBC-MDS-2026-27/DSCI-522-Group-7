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

Follow the [README setup instructions](README.md#usage) to clone the repository, set up your SSH key, and download the Docker image using `docker compose pull`. You do not need to install Python packages or Quarto on your own computer.

### Working inside Docker with Positron

1. Install [Positron](https://positron.posit.co/) and the Remote SSH extension.
2. Follow the README instructions to start the Docker container using `docker compose up -d`.
3. Open Positron and press `Cmd + Shift + P` (Mac) or `Ctrl + Shift + P` (Windows/Linux).
4. Select `Remote-SSH: Connect to Host` and connect to your configured Docker SSH host.
5. Open `/workspace` in Positron and trust the folder.
6. Open a terminal in Positron and check your Git identity:

   ```bash
   git config user.name
   git config user.email
   ```

   If either is missing, configure it using your own name and email:

   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your-email@example.com"
   ```

7. Select `/opt/venv/bin/python` as the Python interpreter.
8. You can now edit and run the project inside the Docker container.

**Troubleshooting:**

- **Connection refused:** Check that Docker Desktop is running and the container has started with `docker compose up -d`.
- **Permission denied (publickey):** Check your SSH key and confirm that its public key is authorized in the container.
- **Python interpreter unavailable:** Select `/opt/venv/bin/python` manually.
- **Files missing:** Open `/workspace` instead of a folder on your local computer.
- **Positron features disabled:** Trust the workspace and install the Python extension in the remote environment if needed.

### Adding or updating Python packages

1. Create a new Git branch for your changes.
2. Add or update the package using `uv add --bounds exact <package-name>`.
3. Confirm that `pyproject.toml` and `uv.lock` have been updated.
4. Commit and push the changes, then open a pull request for review.
5. After the PR is merged, wait for GitHub Actions to publish the updated Docker image.
6. Update the image tag in `docker-compose.yml` to the newly published SHA tag and merge that change.
7. Run `git pull` and `docker compose pull` to download the updated environment.

### Publishing the report

After updating the analysis, render the report inside the container:

```bash
docker compose run --rm analysis-env uv run quarto render src/bridge_health_report.qmd
```

Copy the rendered HTML report to the GitHub Pages location:

```bash
cp src/bridge_health_report.html docs/index.html
```

Commit and push the updated report through a pull request. Once merged, GitHub Pages will publish the new version.

For the full setup and rendering instructions, see the [README](README.md#usage).



### Pull request process

* Create a Git branch for each pull request (PR). Do not commit directly to `main`.
* Give a descriptive branch name like `fix-contributing.md` or `add-new-eda`
* Keep each branch small and independent
* Before opening the PR, render the report (`uv run quarto render src/bridge_health_report.qmd`)
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

## AI Policy

AI assistance is welcome, and so is needing help; submitting code you haven't read
is not.

Disclose your AI use, understand and be able to explain anything you
submit, stay in the conversation after you open a pull request, and don't let an AI
agent open one on its own.

### Scope

"AI" herein refers to generative AI tools like large language models (LLMs)
that can generate, edit, and review software code, create and manipulate
images, or generate human-like communication.

### Responsibility
You are responsible for any code you submit to this repository, regardless
of whether it was manually written or generated by AI. You must understand and be able
to explain both the code you submit and the existing related code; submitting a patch
you cannot explain yourself is not acceptable.
The explanation must be yours, though you may use AI to translate or copy-edit it.

### No autonomous AI agent contributions

The use of an AI agent that writes code and then submits a pull request
autonomously is not permitted. A human must check any generated code and open
the pull request themselves.

### Disclosure

You must disclose whether AI was used in developing in your pull request description. If AI was used, 
document which tool(s) and version(s), how they were used, and what code or text is 
AI generated. We will ask you to complete the disclosure before review.

Disclosure helps reviewers give your contribution appropriate attention, and keeps
review transparent.

### Engagement

Our [code of conduct](CODE_OF_CONDUCT.md) guarantees you a respectful review whatever
you submit. Depth of engagement (mentoring, design discussion, patient iteration) is
reciprocal, and we will politely decline it when a pull request's author doesn't
respond to questions about their change. Failing CI, missing tests, and asking for help are never reasons
to close a pull request; an unanswered "can you explain this change?" is.

### Copyright

All code in this repository is released under the MIT license.
Contributors to this repository license their code under the same license when it is
included into Bridge Health Predictor's version control repository. That means contributors must
own the copyright of any code submitted to this repository or must include the
MIT-compatible open source license(s) associated with the submitted code
in the patch. Code generated by AI may infringe on copyright and it is the
submitter's responsibility to not infringe. We reserve the right to reject any pull
requests, AI generated or not, where the copyright is in question.

### Communication

When interacting with developers (forum, discussions,
issues, pull requests, etc.) do not use AI to speak for you, except for
translation or grammar editing. The conversation is where understanding and
relationships come from.

### Attribution

These contributing guidelines were adapted from the [Breast Cancer Predictor contributing guidelines](https://github.com/UBC-MDS/DSCI_522_project-template-breast-cancer-predictor/blob/main/CONTRIBUTING.md).

These AI policy guidelines were adapted from [earthaccess](https://earthaccess.readthedocs.io/en/latest/contributor/ai-policy/).
