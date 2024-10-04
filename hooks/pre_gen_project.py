import os
import subprocess

def run_command(cmd):
    subprocess.call(cmd, shell=True)

# Docker is always included, now decide which language template to use
language_template = '{{ cookiecutter.language_template }}'
project_slug = '{{ cookiecutter.project_slug }}'  # Get the project_slug from cookiecutter context

# Map the language selection to repository URLs
language_repos = {
    'python': 'https://github.com/mahergzam/cookie-cutter-python',
    'java': 'https://github.com/mahergzam/cookie-cutter-java',
    'go': 'https://github.com/mahergzam/cookie-cutter-go'
}

# Clone the selected language template
import os
import subprocess

def run_command(cmd):
    subprocess.call(cmd, shell=True)

# Docker is always included, now decide which language template to use
language_template = '{{ cookiecutter.language_template }}'
project_slug = '{{ cookiecutter.project_slug }}'  # Get the project_slug from cookiecutter context

# Map the language selection to repository URLs
language_repos = {
    'python': 'https://github.com/mahergzam/cookie-cutter-python',
    'java': 'https://github.com/mahergzam/cookie-cutter-java',
    'go': 'https://github.com/mahergzam/cookie-cutter-go',
}

# Clone the selected language template
repo_url = language_repos.get(language_template)
if repo_url:
    print(f"Cloning {language_template} template from {repo_url}...")
    run_command(f'git clone {repo_url} temp_language')

    # Verify that the repository was cloned correctly
    run_command('ls')

else:
    print(f"Error: Invalid language template '{language_template}' selected.")

