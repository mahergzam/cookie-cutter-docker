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

repo_url = language_repos.get(language_template)
if repo_url:
    print(f"Cloning {language_template} template from {repo_url}...")
    run_command(f'git clone {repo_url} temp_language')

    # Step 2: Run Cookiecutter inside the cloned language repository using its own cookiecutter.json
    os.chdir('temp_language')

    # Run cookiecutter inside the cloned template (using the language-specific cookiecutter.json)
    run_command('cookiecutter . --no-input')

    # Step 3: Identify the rendered project folder (based on rendered project_slug)
    rendered_folder_name = '{{ cookiecutter.project_slug }}'

    # Ensure we navigate back to the parent directory after cookiecutter runs
    os.chdir('..')

    # Step 4: Copy the rendered files to the main project directory
    run_command(f'cp -r temp_language/{rendered_folder_name}/. {{ cookiecutter.project_slug }}/')

    # Step 5: Cleanup
    run_command('rm -rf temp_language')
    print(f"{language_template.capitalize()} template files have been added to your project.")
else:
    print(f"Error: Invalid language template '{language_template}' selected.")

