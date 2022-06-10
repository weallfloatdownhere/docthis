import click, sys, subprocess, os, yaml
from os.path import abspath

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

def writeYaml(data, outputfile):
    with open(outputfile, 'w') as file:
        documents = yaml.dump(data, file)


# Sources classes. 

@click.group()
def cli():
    pass

class github():
    def __init__(self, outputdir) -> None:

        self.outputs = {"github_repositories": []}

        yaml_data=loadValues('github')

        for repo in yaml_data['github_repositories']:
            desc = executeProcess(f"curl -L --silent https://github.com/{repo['name']} | grep '<title>' | xargs | sed 's/<[^>]*>//g'")
            installer = repo['install'] if repo['install'] else ''
            self.outputs['github_repositories'] += [{"url": f"https://github.com/{repo['name']}",
                                                    "description": f"{desc.strip()}", 
                                                    "repo": repo['name'],
                                                    "install": f"{installer}"
                                                    }]

        # Write the final value file.
        writeYaml(self.outputs, f"{outputdir}/github-values.yaml")
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
