import subprocess

def run_command(cmd):
    subprocess.call(cmd, shell=True)

# Docker is always included, now decide which language template to use
language_template = '{{ cookiecutter.language_template }}'

# Map the language selection to repository URLs
language_repos = {
    'python': 'https://github.com/mahergzam/cookie-cutter-python',
    'java': 'https://github.com/mahergzam/cookie-cutter-java',
    'go': 'https://github.com/mahergzam/cookie-cutter-go'
}

# Clone the selected language template
repo_url = language_repos.get(language_template)
if repo_url:
    print(f"Cloning {language_template} template from {repo_url}...")
    run_command(f'git clone {repo_url} temp_language')

    # Copy files from the language template to the current project
    run_command(f'cp -r temp_language/{{ cookiecutter.project_slug }}/. {{ cookiecutter.project_slug }}/')
    
    # Cleanup
    run_command('rm -rf temp_language')
    print(f"{language_template.capitalize()} template files have been added to your project.")
else:
    print(f"Error: Invalid language template '{language_template}' selected.")
