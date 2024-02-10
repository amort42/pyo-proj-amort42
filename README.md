# python-template

Template for python-based repositories.

## Usage

1. Use this repository by specifying it as a template for your repository.
2. run `./script/bootstrap`

## Notes for personal setup

(from https://armandsauzay.medium.com/python-project-setup-a-step-by-step-guide-to-industry-best-practices-dbce717b2d12)

1. gh repo create amort42/hello-world-cli --template amort42/python-template --public
2. git clone https://github.com/amort42/hello-world-cli.git
3. cd hello-world-cli
4. ./script/bootstrap
5. Using pyenv and poetry
   1. pyenv install <version> pre 3.12 to prevent dependency error
   2. pyenv global <version>
   3. pip install poetry
   4. poetry add requests mypy
   5. poetry add --group lint flake8 black isort **mypy**
   6. poetry run pytest
   7. poetry run mypy hello_world_cli/main.py
   8. poetry run flake8 hello_world_cli/cli.py
   9. poetry run black hello_world_cli/cli.py
   10. pre-commit run --all-files

When the github action runs, it uses an automatically generated token named GITHUB_TOKEN as the access to run the actions required. In order for it to do so, we need to allow the automatically generated token to have write permission. So, in the Settings, go to Actions > General, and scroll down to the Workflow permissions section, and select the Read and write permissions radio button. Don’t forget to click the save button.
