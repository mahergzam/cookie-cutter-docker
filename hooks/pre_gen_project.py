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
    # Clone the selected language template
    run_command('git clone https://github.com/user/python-template temp_language')

    # Verify the clone was successful
    run_command('ls temp_language')

    # Copy the contents from the project folder in the language template to the target folder
    run_command('cp -r temp_language/{{ cookiecutter.project_slug }}/. {{ cookiecutter.project_slug }}/')

    # Cleanup
    run_command('rm -rf temp_language')
    print("Template files have been added to your project.")

else:
    print(f"Error: Invalid language template '{language_template}' selected.")
