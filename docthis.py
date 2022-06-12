from time import sleep
import click, sys, subprocess, os, yaml
from os.path import abspath
import requests


SCRIPT_PATH=os.path.dirname(os.path.realpath(__file__))

# Utillities function.

def executeProcess(command=None):
    try:
        return subprocess.run(command, shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8').rstrip()
    except Exception as err:
        sys.exit()

def loadValues(values_from='github'):
    with open(f"{SCRIPT_PATH}/values/{values_from}.yml", 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

def getHtmlFromUrl(url=f""):
    content = ""
    try:
        content = requests.get(url).text
        print(content)
    except:
        pass
    return content

def writeYaml(data, outputfile):
    with open(outputfile, 'w') as file:
        documents = yaml.dump(data, file)

@click.group()
def cli():
    pass

class githubRepo():
    def __init__(self, repo_yaml={}) -> None:
        self.repo_name = repo_yaml['name']
        self.description = executeProcess(f"curl -L --silent https://github.com/{self.repo_name} | grep '<title>' | xargs | sed 's/<[^>]*>//g'")
        src_readme = getHtmlFromUrl(f"https://raw.githubusercontent.com/{self.repo_name}/main/README.md")
        self.readme = src_readme if "404 not found" not in src_readme else ''
        self.installer = repo_yaml['install'] if repo_yaml['install'] else ''

class github():
    def __init__(self, outputdir) -> None:
        self.githubRepos = {"github_repositories": []}
        yaml_data=loadValues('github')
        cnt = 1
        for repo in yaml_data['github_repositories']:
            gitrepo = githubRepo(repo)
            self.githubRepos['github_repositories'] += [{"url": f"https://github.com/{gitrepo.repo_name}",
                                                "description": f"{gitrepo.description.strip()}", 
                                                "repo": gitrepo.repo_name,
                                                "install": f"{gitrepo.installer}",
                                                "readme": f"{gitrepo.readme}",
                                                }]
            print(f"{gitrepo.repo_name} generated succesfully.. {len(self.githubRepos['github_repositories'])} / {len(yaml_data['github_repositories'])}")
            sleep(1)
        # Write the final value file.
        writeYaml(self.githubRepos, f"{outputdir}/github-values.yaml")
        # Render the templates against the value file.
        if os.path.exists(f"{outputdir}/README.md"): os.remove(f"{outputdir}/README.md")
        executeProcess(f"jinja2 {SCRIPT_PATH}/templates/github.tmpl {outputdir}/github-values.yaml --format=yaml > {outputdir}/README.md")
        # Remove temporary generated values files.
        if os.path.exists(f"{outputdir}/github-values.yaml"): os.remove(f"{outputdir}/github-values.yaml")
        # Return
        self.outputFile = f"{outputdir}/README.md"

# Command

@click.command()
@click.argument('outputdir')
def generate(outputdir=os.getcwd()):
    lst_gen_files=[]
    # Get the absolute path of the outputdir parameter value.
    abs_outputDir=abspath(outputdir)
    # Create the outputDir if it doesnt exists yet.
    os.makedirs(abs_outputDir, exist_ok=True)
    # Generate the Github markdown page.
    gfile = github(outputdir)
    lst_gen_files.append(gfile.outputFile)
    # Print the list of generated output files.
    click.echo(lst_gen_files)

cli.add_command(generate)
if __name__ == '__main__':    
    cli()
