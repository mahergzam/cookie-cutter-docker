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
    'java': 'https://github.com/user/java-template',
    'cpp': 'https://github.com/user/cpp-template'
}

# Clone the selected language template
repo_url = language_repos.get(language_template)
if repo_url:
    print(f"Cloning {language_template} template from {repo_url}...")
    run_command(f'git clone {repo_url} temp_language')

    # Verify that the repository was cloned correctly
    run_command('ls temp_language')

    # Find the actual folder inside temp_language (without assuming project_slug is expanded)
    folder_name = next(os.walk('temp_language'))[1][0]  # Gets the first directory inside temp_language
    source_dir = os.path.join('temp_language', folder_name)

    # Ensure the target directory exists
    if not os.path.exists(project_slug):
        os.makedirs(project_slug)  # Create the target directory if it doesn't exist
        print(f"Created directory {project_slug}")

    if os.path.exists(source_dir):
        # Copy files from the cloned template directory to the project directory
        run_command(f'cp -r {source_dir}/. {project_slug}/')
        print(f"Copied files from {source_dir} to {project_slug}")
    else:
        print(f"Error: Directory {source_dir} not found in the cloned template")

    # Clean up the temporary directory
    run_command('rm -rf temp_language')
    print(f"{language_template.capitalize()} template files have been added to your project.")
else:
    print(f"Error: Invalid language template '{language_template}' selected.")

