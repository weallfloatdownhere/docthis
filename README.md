

## Refresh markdown files content.

```bash
cd $(mktemp -d) && git clone https://github.com/weallfloatdownhere/docthis.git .&& python3 docthis.py generate . && git add . && git commit -m "Regen README" && git push
```



---



[***GitHub - helm/helm: The Kubernetes Package Manager***](https://github.com/helm/helm)

![GitHub last commit](https://img.shields.io/github/last-commit/helm/helm) ![GitHub Repo stars](https://img.shields.io/github/stars/helm/helm?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/helm/helm)



</br>


<details>

<summary>README</summary> 

# Helm

[![CircleCI](https://circleci.com/gh/helm/helm.svg?style=shield)](https://circleci.com/gh/helm/helm)
[![Go Report Card](https://goreportcard.com/badge/github.com/helm/helm)](https://goreportcard.com/report/github.com/helm/helm)
[![GoDoc](https://img.shields.io/static/v1?label=godoc&message=reference&color=blue)](https://pkg.go.dev/helm.sh/helm/v3)
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/3131/badge)](https://bestpractices.coreinfrastructure.org/projects/3131)

Helm is a tool for managing Charts. Charts are packages of pre-configured Kubernetes resources.

Use Helm to:

- Find and use [popular software packaged as Helm Charts](https://artifacthub.io/packages/search?kind=0) to run in Kubernetes
- Share your own applications as Helm Charts
- Create reproducible builds of your Kubernetes applications
- Intelligently manage your Kubernetes manifest files
- Manage releases of Helm packages

## Helm in a Handbasket

Helm is a tool that streamlines installing and managing Kubernetes applications.
Think of it like apt/yum/homebrew for Kubernetes.

- Helm renders your templates and communicates with the Kubernetes API
- Helm runs on your laptop, CI/CD, or wherever you want it to run.
- Charts are Helm packages that contain at least two things:
  - A description of the package (`Chart.yaml`)
  - One or more templates, which contain Kubernetes manifest files
- Charts can be stored on disk, or fetched from remote chart repositories
  (like Debian or RedHat packages)

## Install


Binary downloads of the Helm client can be found on [the Releases page](https://github.com/helm/helm/releases/latest).

Unpack the `helm` binary and add it to your PATH and you are good to go!

If you want to use a package manager:

- [Homebrew](https://brew.sh/) users can use `brew install helm`.
- [Chocolatey](https://chocolatey.org/) users can use `choco install kubernetes-helm`.
- [Scoop](https://scoop.sh/) users can use `scoop install helm`.
- [GoFish](https://gofi.sh/) users can use `gofish install helm`.
- [Snapcraft](https://snapcraft.io/) users can use `snap install helm --classic`

To rapidly get Helm up and running, start with the [Quick Start Guide](https://helm.sh/docs/intro/quickstart/).

See the [installation guide](https://helm.sh/docs/intro/install/) for more options,
including installing pre-releases.

## Docs

Get started with the [Quick Start guide](https://helm.sh/docs/intro/quickstart/) or plunge into the [complete documentation](https://helm.sh/docs)

## Roadmap

The [Helm roadmap uses GitHub milestones](https://github.com/helm/helm/milestones) to track the progress of the project.

## Community, discussion, contribution, and support

You can reach the Helm community and developers via the following channels:

- [Kubernetes Slack](https://kubernetes.slack.com):
  - [#helm-users](https://kubernetes.slack.com/messages/helm-users)
  - [#helm-dev](https://kubernetes.slack.com/messages/helm-dev)
  - [#charts](https://kubernetes.slack.com/messages/charts)
- Mailing List:
  - [Helm Mailing List](https://lists.cncf.io/g/cncf-helm)
- Developer Call: Thursdays at 9:30-10:00 Pacific ([meeting details](https://github.com/helm/community/blob/master/communication.md#meetings))

### Code of conduct

Participation in the Helm community is governed by the [Code of Conduct](code-of-conduct.md).


</details>



</br>



[***GitHub - redhat-cop/gitops-catalog: Tools and technologies that are hosted on an OpenShift cluster***](https://github.com/redhat-cop/gitops-catalog)

![GitHub last commit](https://img.shields.io/github/last-commit/redhat-cop/gitops-catalog) ![GitHub Repo stars](https://img.shields.io/github/stars/redhat-cop/gitops-catalog?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/redhat-cop/gitops-catalog)



</br>


<details>

<summary>README</summary> 

# GitOps Catalog

[![Build Status](https://github.com/redhat-cop/gitops-catalog/workflows/Lint/badge.svg?branch=main)](https://github.com/redhat-cop/gitops-catalog/actions?workflow=Lint)

The GitOps Catalog includes kustomize bases and overlays for a number of OpenShift operators and applications.

This catalog is not officially supported by Red Hat and customers are discouraged from referencing this repo directly as a remote repo in kustomize as future changes may break these references. Instead customers are encouraged to take individual items of interest into their own curated catalog and maintain it as their own.

## Catalog Refactoring for Consistency

Now that this catalog is part of the Red Hat Community of Practice, there will be some structural refactoring to improve consistency.  If you have been using this catalog since before it was part of the `redhat-cop` organization, or at least before any refactoring has begun, be sure to include a `ref` in your `oc/kubectl` commands or `kustomization.yaml` files to avoid any negative side effects.  The last tag before the repository was migrated is `v0.3`.  Simply include `?ref=v0.3` at the end of the repository reference.  For example:

```
oc apply -k https://github.com/redhat-cop/gitops-catalog/jenkins2/overlays/default?ref=v0.3
```

Or

```
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

resources:
- github.com/redhat-cop/gitops-catalog/jenkins2/bases/?ref=v0.3
```


## Usage

Each catalog item has (or will have) its own README in its directory root with instructions.  Generally speaking, you can usually just apply a "base" or "overlay" directly in your cluster by cloning this repostitory and using the `-k` flag (for Kustomize) built into `oc` and `kubectl`:

```
git clone https://github.com/redhat-cop/gitops-catalog
oc apply -k catalog/jenkins2/overlays/default
```

Or to skip the cloning step:

```
oc apply -k https://github.com/redhat-cop/gitops-catalog/jenkins2/overlays/default
```

## Kustomize

You can reference bases for the various tools here in your own kustomize overlay without explicitly cloning this repo, for example:

```
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

namespace: product-catalog-cicd

resources:
- github.com/redhat-cop/gitops-catalog/jenkins2/bases/?ref=main
```

This enables you to patch these resources for your specific environments. Note that none of these bases specify a namespace, in your kustomization
overlay you can include the specific namespace you want to install the tool into.


</details>



</br>



[***GitHub - rht-labs/ubiquitous-journey: 🧰 Open Innovation Labs Developer Experience - all the tooling for starting a residency***](https://github.com/rht-labs/ubiquitous-journey)

![GitHub last commit](https://img.shields.io/github/last-commit/rht-labs/ubiquitous-journey) ![GitHub Repo stars](https://img.shields.io/github/stars/rht-labs/ubiquitous-journey?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/rht-labs/ubiquitous-journey)



</br>


<details>

<summary>README</summary> 

# 🦄 Ubiquitous Journey 🔥

🧰 This repo embodies a GitOps approach to deploying application code, middleware infrastructure and supporting CI/CD tools. 🧰

At its simplest, the repo is an [ArgoCD Application](https://argo-cd.readthedocs.io/en/stable/core_concepts/) which references [other helm charts](https://github.com/redhat-cop/helm-charts.git) and [other kustomize definitions](https://github.com/rht-labs/refactored-adventure) to deploy applications.

The idea is to reference other Charts, Kustomize, YAML snippets from within this framework. This keeps things `pluggable` to suit the needs of your team.

🎨 We have evolved the design from the original [Labs CI / CD](https://github.com/rht-labs/labs-ci-cd.git) project. The  Ubiquitous Journey (`UJ`) represents a major milestone in moving to a GitOps approach to tooling, application management and configuration drift using [ArgoCD](https://argoproj.github.io/argo-cd/).

## Table of Contents

- [Contributor Covenant Code of Conduct](./code-of-conduct.html#contributor-covenant-code-of-conduct)
  * [Our Pledge](./code-of-conduct.html#our-pledge)
  * [Our Standards](./code-of-conduct.html#our-standards)
  * [Our Responsibilities](./code-of-conduct.html#our-responsibilities)
  * [Scope](./code-of-conduct.html#scope)
  * [Enforcement](./code-of-conduct.html#enforcement)
  * [Attribution](./code-of-conduct.html#attribution)
- [🦄 Ubiquitous Journey 🔥](./index.html#%F0%9F%A6%84-ubiquitous-journey-)
  * [Components](./index.html#components)
  * [How do I run it? 🏃‍♀️](./index.html#how-do-i-run-it-)
    + [Prerequisites](./index.html#prerequisites)
    + [Let's go, installing ArgoCD 🏃🏻](./index.html#lets-go-installing-argocd-)
    + [🤠 Deploying the Ubiquitous Journey](./index.html#%F0%9F%A4%A0-deploying-the-ubiquitous-journey)
    + [Cleanup 🧤](./index.html#cleanup-)
    + [Debugging 🤺](./index.html#debugging-)
- [Common Errors when installing ArgoCD](./docs%2Fargocd-install.html#common-errors-when-installing-argocd)
- [ArgoCD Master and Child 👩‍👦](./docs%2Fargocd-master-child.html#argocd-master-and-child-)
- [Restricted Children](./docs%2Fargocd-master-child.html#restricted-children)
- [Bootstrap projects and ArgoCD 🍻](./docs%2Fbootstrap-argocd.html#bootstrap-projects-and-argocd-)
  * [Tooling for Application Development 🦅](./docs%2Fbootstrap-argocd.html#tooling-for-application-development-)
      - [(A) Deploy using argo app of apps ...](./docs%2Fbootstrap-argocd.html#a-deploy-using-argo-app-of-apps-)
      - [(B) Deploy using helm ...](./docs%2Fbootstrap-argocd.html#b-deploy-using-helm-)
- [Example Application Deploy 🌮](./docs%2Fbootstrap-argocd.html#example-application-deploy-)
- [Cleaning up ArgoCD Apps 🧹](./docs%2Fbootstrap-argocd.html#cleaning-up-argocd-apps-)
- [Metrics 📉](./docs%2Fbootstrap-argocd.html#metrics-)
- [Deploy to a custom namespace 🦴](./docs%2Fdeploy-custom-namespace.html#deploy-to-a-custom-namespace-)
- [Help me](./docs%2Fhelp.html#help-me)
  * [Not automated yet ...](./docs%2Fhelp.html#not-automated-yet-)
- [Sealed Secrets Help](./docs%2Fsealed-secrets.html#sealed-secrets-help)
  * [🕵️‍♀️ Generate Sealed Secrets:](./docs%2Fsealed-secrets.html#%F0%9F%95%B5%EF%B8%8F%E2%80%8D%E2%99%80%EF%B8%8F-generate-sealed-secrets)
  * [📝 Bring your own certs](./docs%2Fsealed-secrets.html#%F0%9F%93%9D-bring-your-own-certs)
- [What's in the box? 👨](./docs%2Fwhats-in-the-box.html#whats-in-the-box-)
- [What it's not...🤷🏻‍♀️](./docs%2Fwhats-in-the-box.html#what-its-not)
- [Dashboard 📃](./docs%2Fwhats-in-the-box.html#dashboard-)

## Components

The folder structure of this repo is split as follows:

```bash
├── archive                            <===  💀 where the skeletons live. archived material.
├── docs                               <===  📖 supporting documentation for UJ.
├── pet-battle                         <===  📖 the example application `pet-battle`
├── templates                          <===  📖 helm templates to create ArgoCD Applications and Projects for UJ
├── ubiquitous-journey                 <===  📖 helm values files containing applications we wish to deploy
├── Chart.yaml                         <===  📖 we deploy UJ using a helm chart
└── values.yaml                        <===  📖 UJ's helm chart values
```

There are two main components to this repository:

1. `Ubiquitous Journey` - Contains all the tools, collaboration software and day2ops to be deployed on Red Hat OpenShift. This includes chat applications, task management apps and tools to support CI/CD workflows and testing. For the complete list and details: [What's in the box?👨](docs/whats-in-the-box.md)
2. An demo application called [`pet-battle`](https://github.com/petbattle) that shows you how to use the UJ structure with a three tiered application stack.

Each part can be used independently of each other but sequentially they create a full stack.

## How do I run it? 🏃‍♀️

If you already have an ArgoCD instance running and you want just want to add the tooling to it, [move to part 2](docs/bootstrap-argocd.md#tooling-for-application-development-🦅) in the docs.

### Prerequisites

You will need:

- OpenShift 4.6+ or greater (cluster admin user required) - [Try OpenShift](https://try.openshift.com)
- Install helm v3+ (cli) or greater - [Helm Quickstart](https://helm.sh/docs/intro/quickstart)

### Let's go, installing ArgoCD 🏃🏻

Install an instance of ArgoCD. There are several methods to install ArgoCD in OpenShift. Pick your favorite flavour 🍦

Use the Red Hat supported GitOps Operator (configured by default as cluster wide and to deploy the operator and an instance in `labs-ci-cd`)

```bash
helm repo add redhat-cop https://redhat-cop.github.io/helm-charts
helm upgrade --install argocd \
  --create-namespace \
  --namespace labs-ci-cd \
  redhat-cop/gitops-operator
```

⛷️ We **strongly** recommend that you make a copy of the `values.yaml` file and make edits that way. This values file can be checked in to this repo and be kept if further changes are needed such as adding in private `repositoryCredentials` or other handy stuff such as `secrets` and `namespaces` etc. For example, you have `argocd-values.yaml` file with your changes:

```bash
helm upgrade --install argocd \
  --create-namespace \
  --namespace labs-ci-cd \
  -f argocd-values.yaml \
  redhat-cop/gitops-operator
```

If you have trouble 😵‍💫 - we have documented some common errors [when installing ArgoCD](docs/argocd-install.md) which may help.

### 🤠 Deploying the Ubiquitous Journey

A handy one liner to deploy all the default software artifacts in this project using their default values. Just make sure the namespace you set below is the same as your ArgoCD namespace from the previous step.

```bash
helm upgrade --install uj --namespace labs-ci-cd .
```

If you login to ArgoCD using the UI here:

```bash
echo https://$(oc get route argocd-server --template='{{ .spec.host }}' -n labs-ci-cd)
```

you should see lots of things spinning up

![argocd-ui](docs/images/argocd-uj.png)

You can set `enabled: true` on all of the application definitions in the `values-*.yaml` files if you want to deploy everything 🧨 .... 💥

Fork the repo and make your changes in the fork if you wish to GitOp enable things. Update the `source` in values.yaml to make sure ArgoCD is pulling from the correct source repo (your fork). If you've already forked the repo and want to deploy quickly you can also run:

```bash
helm upgrade --install uj \
  --set source=https://github.com/<YOUR_FORK>/ubiquitous-journey.git \
  --namespace labs-ci-cd .
```

### Cleanup 🧤

Uninstall and delete all resources in the various projects
```bash
# This may take a while:
helm delete uj --namespace labs-ci-cd

# Then remove your ArgoCD instance
helm delete argocd --namespace labs-ci-cd
```

### Debugging 🤺

Run the following command to debug one of the UJ values files to see which values are being passed:

```bash
# example debugging the ArgoCD `Application` manifests from the example deployment 
helm install debug --dry-run -f pet-battle/test/values.yaml . 
```


</details>



</br>



[***GitHub - slok/agebox: Age based repository file encryption gitops tool***](https://github.com/slok/agebox)

![GitHub last commit](https://img.shields.io/github/last-commit/slok/agebox) ![GitHub Repo stars](https://img.shields.io/github/stars/slok/agebox?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/slok/agebox)



</br>


<details>

<summary>README</summary> 

<p align="center">
    <img src="img/logo.png" width="50%" align="center" alt="agebox">
</p>

# agebox

[![CI](https://github.com/slok/agebox/actions/workflows/ci.yaml/badge.svg?branch=main)](https://github.com/slok/agebox/actions/workflows/ci.yaml)
[![Go Report Card](https://goreportcard.com/badge/github.com/slok/agebox)](https://goreportcard.com/report/github.com/slok/agebox)
[![Apache 2 licensed](https://img.shields.io/badge/license-Apache2-blue.svg)](https://raw.githubusercontent.com/slok/agebox/master/LICENSE)
[![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/slok/agebox)](https://github.com/slok/agebox/releases/latest)

Easy and simple file repository encryption tool based on [Age].

Have you ever thought _"this should be simple"_ while you were using tools like [Blackbox] , [Git-crypt] or [Sops]? This is what agebox is. A tool on top of [Age]'s security system that encrypts/decrypts your repository files, focused on simplicity and gitops.

## Features

- Secure (Agebox delegates security to [Age]).
- Tracks encrypted files in repository.
- No PGP and no agents, just simple SSH and [Age] key files.
- File flexibility (encrypts/decrypts recursive paths, multiple/single files, all tracked files...).
- Reencrypts all tracked files with a single command.
- Focused on Gitops, CI flows and simplicity.
- Works with any file (doesn't understand formats like JSON, YAML...).
- Single binary/executable.
- No side effects like VCS commands (e.g: doesn't execute Git commands for you).

## Get agebox

- [Releases](https://github.com/slok/agebox/releases)
- [Docker images](https://github.com/users/slok/packages/container/package/agebox)
- `git clone git@github.com:slok/agebox.git && cd ./agebox && make build && ls -la ./bin`

## Getting started

Initialize agebox tracking file.

```bash
agebox init
```

Encrypt (and track) multiple files.

```bash
agebox encrypt ./app1/secret1.yaml ./app2/secret1.yaml
```

Encrypt (and track) a directory in dry-run to see what would be encrypted before doing it.

```bash
agebox encrypt ./secrets --dry-run
```

Encrypt (and track) a directory and only (filter regex used) the `secret` named yaml files.

```bash
agebox encrypt ./manifests --filter ".*secret(\.yaml|\.yml)$"
```

Decrypt a subset of tracked secrets and a file.

```bash
agebox decrypt ./secrets/team-1 ./secrets/secret1.yaml
```

Decrypt only (filter regex used) `team-a` tracked files.

```bash
agebox decrypt ./secrets --filter ".*team-a.*"
```

Force decryption of all tracked files.

```bash
agebox decrypt --all --force
```

Validate tracked secrets are encrypted and not decrypted (without decrypt validation).

```bash
agebox validate --no-decrypt
```

Cat multiple encrypted files and print them to stdout.

```bash
agebox cat ./secrets/secret1.yaml.agebox ./secrets/secret2.json.agebox --no-log
```

Reencrypt all files.

```bash
agebox reencrypt
```

Untrack multiple files.

```bash
agebox untrack ./secrets/secret1.yaml ./secrets/secret2.yaml
```

Untrack and delete file.

```bash
agebox untrack ./secrets/secret1.yaml --delete
```

## How does it work

When you initialize agebox on a repository it will create a file (`.ageboxreg.yml`) that will track all the encrypted
files in the repository.

From now on if you encrypt files with agebox from the root of the repository it will:

- Track the files if not already tracked.
- Encrypt the files with the public keys in `./keys` or `--public-keys` as recipients.
- If is a directory it will expand to all the files in the directory and subdirectories.

As a regular flow of agebox usage examples, you can:

- Decrypt tracked files as a single file, multiple files, a directory and its subdirectories...
- Decrypt all tracked files (`--all`).
- Reencrypt all tracked files with the public key recipients.
- Encrypt all tracked files (`--all`) that are decrypted in the repository.
- Untrack a file (and optionally delete from the file system).
- Encrypt/decrypt in dry-run to validate (handy en CI for checking).
- Cat encrypted files to stdout.
- Validate tracked files are encrypted and not decrypted (useful on CI, git hooks...).

Check the **Getting started** section for specific commands.

## Keys

Agebox supports the same asymmetric keys [Age] does:

- X25519 (Age).
- RSA SSH.
- Ed25519 SSH.

**Agebox knows how to discover keys in directories (recursively).**

### Public keys

The public keys are the recipients of the encrypted files. With their respective private keys, users will be able to decrypt the files.

Public keys should be on a directory relative to the root of the repository (by default `./keys`) at the moment of invoking encryption commands, this simplifies the usage of keys by not requiring pgp keys or agents.

Agebox will encrypt with the loaded public keys, this means that when we add or remove any public key we should `reencrypt` the tracked files.

In case you don't want to have all the public keys in all the repositories that are managed by agebox, you could centralize these keys in another repository andgetting them before invoking agebox. Some usage examples:

- Git submodule `git pull --recurse-submodules`.
- Git repo and previous agebox command invoke `git clone/pull`.
- Download public keys from S3.

You can configure this with `--public-keys` flag or `AGEBOX_PUBLIC_KEYS` env var.

You can have multiple public keys in a file (one per line), like [Age recipients file](https://github.com/FiloSottile/age/#recipient-files).

### Private keys

By default Agebox will try loading all the valid private keys from `HOME/.ssh`, however you can configure this with `--private-keys` flag or `AGEBOX_PRIVATE_KEYS` env var to point to specific directory with the keys (or a path to a single key).

## Alternatives

- [Blackbox]: Uses PGP (requires an agent), complex and sometimes has undesired side effects (e.g git commands execution).
- [Sops]: Lots of features and very complex for simple use cases.
- [Git-crypt]: Uses PGP (requires an agent), complex, 100% tied to Git.

## Kudos

Thanks to [@FiloSottile](https://twitter.com/FiloSottile), [@Benjojo12](https://twitter.com/Benjojo12) and all the other [contributors](https://github.com/FiloSottile/age/graphs/contributors) of [Age].

Without [Age], [Agebox] would not exist.

[agebox]: https://github.com/slok/agebox
[age]: https://github.com/FiloSottile/age
[blackbox]: https://github.com/StackExchange/blackbox
[sops]: https://github.com/mozilla/sops
[git-crypt]: https://github.com/AGWA/git-crypt


</details>



</br>



[***GitHub - Azure/AzOps: AzOps is a PowerShell module which deploys (Push) Resource Templates &amp; Bicep files at all Azure scope levels and exports (Pull) ARM resource hierarchy.***](https://github.com/Azure/AzOps)

![GitHub last commit](https://img.shields.io/github/last-commit/Azure/AzOps) ![GitHub Repo stars](https://img.shields.io/github/stars/Azure/AzOps?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/Azure/AzOps)



</br>


<details>

<summary>README</summary> 

# AzOps

![GitHub issues by-label](https://img.shields.io/github/issues/azure/azops/enhancement?label=enhancement%20issues)
![GitHub issues by-label](https://img.shields.io/github/issues/azure/azops/bug?label=bug%20issues)
![PowerShell Gallery](https://img.shields.io/powershellgallery/dt/azops)
![GitHub Super-Linter](https://github.com/Azure/AzOps/workflows/AzOps%20-%20Tests/badge.svg)
![GitHub Super-Linter](https://github.com/Azure/AzOps/workflows/Lint%20Code%20Base/badge.svg)

This repository is for active development of the AzOps PowerShell cmdlets.

## Getting started

For tutorials, samples and quick starts, visit the [AzOps Accelerator](https://github.com/azure/azops-accelerator) template repository.

## Dependencies

- [Az.Accounts](https://github.com/azure/azure-powershell)
- [Az.Billing](https://github.com/azure/azure-powershell)
- [Az.Resources](https://github.com/azure/azure-powershell)
- [PSFramework](https://github.com/PowershellFrameworkCollective/psframework)

## Need help?

For introduction guidance visit the [GitHub Wiki](https://github.com/azure/azops/wiki)  
For reference documentation visit the [Enterprise-Scale](https://github.com/azure/enterprise-scale)  
For tutorials, samples and quick starts, go to [AzOps Accelerator](https://github.com/azure/azops-accelerator)  
For information on contributing to the module, visit the [Contributing Guide](https://github.com/Azure/azops/wiki/debug)  
For information on migrating to the new version, visit the [Migration Guide](https://github.com/azure/azops/wiki/migration)  
File an issue via [GitHub Issues](https://github.com/azure/azops/issues/new/choose)  

## Output

AzOps is rooted in the principle that everything in Azure is a resource and to operate at-scale, it should be managed declaratively to determine target goal state of the overall platform.

This PowerShell module provides the ability to deploy Resource Templates & Bicep files at all Azure [scope](https://docs.microsoft.com/azure/role-based-access-control/scope-overview) levels. To provide this functionality the multiple scopes within Azure Resource Manager are represented (example below) within Git. Using directories and files, templates can be deployed (Push) at various scopes whilst also exporting (Pull) composite templates from ARM and placing them within the repository.

```bash
root
└── tenant root group (e42bc18f)
    ├── applications (73fded8a)
    │   ├── development (204bf7a2)
    │   │   ├── microsoft.authorization_roleassignments-4f687d42.json
    │   │   ├── microsoft.management_managementgroups-204bf7a2.json
    │   │   └── subscription-1 (fdfda291)
    │   │       ├── microsoft.authorization_policyassignments-securitycenterbuiltin.json
    │   │       └── microsoft.subscription_subscriptions-fdfda291.json
    │   ├── microsoft.authorization_roleassignments-219d3675.json
    │   ├── microsoft.management_managementgroups-73fded8a.json
    │   └── production (75718043)
    │       ├── microsoft.authorization_roleassignments-5bf6a637.json
    │       ├── microsoft.management_managementgroups-75718043.json
    │       └── subscription-2 (ad32efed)
    │           ├── microsoft.authorization_policyassignments-dataprotectionsecuritycenter.json
    │           ├── microsoft.authorization_policyassignments-securitycenterbuiltin.json
    │           └── microsoft.subscription_subscriptions-ad32efed.json
    ├── microsoft.authorization_roleassignments-d18adbf0.json
    ├── microsoft.authorization_roledefinitions-40db802e.json
    ├── microsoft.management_managementgroups-e42bc18f.json
    └── platform (4dc7bd90)
        ├── microsoft.authorization_policydefinitions-3029d7f6.parameters.json
        ├── microsoft.authorization_roleassignments-92ebbfe0.json
        ├── microsoft.management_managementgroups-4dc7bd90.json
        └── subscription-0 (1e045925)
            ├── microsoft.authorization_policyassignments-dataprotectionsecuritycenter.json
            ├── microsoft.authorization_policyassignments-securitycenterbuiltin.json
            ├── microsoft.authorization_roleassignments-3d8b69be.json
            ├── microsoft.subscription_subscriptions-1e045925.json
            └── networks
                └── microsoft.resources_resourcegroups-networks.json
```

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit <https://cla.opensource.microsoft.com>.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft
trademarks or logos is subject to and must follow
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.

</details>



</br>



[***GitHub - onedr0p/home-ops: A mono repository for my home infrastructure and Kubernetes cluster which adheres to Infrastructure as Code (IaC) and GitOps practices where possible***](https://github.com/onedr0p/home-ops)

![GitHub last commit](https://img.shields.io/github/last-commit/onedr0p/home-ops) ![GitHub Repo stars](https://img.shields.io/github/stars/onedr0p/home-ops?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/onedr0p/home-ops)



</br>



</br>



[***GitHub - kubernetes/git-sync: A sidecar app which clones a git repo and keeps it in sync with the upstream.***](https://github.com/kubernetes/git-sync)

![GitHub last commit](https://img.shields.io/github/last-commit/kubernetes/git-sync) ![GitHub Repo stars](https://img.shields.io/github/stars/kubernetes/git-sync?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/kubernetes/git-sync)



</br>



</br>



[***GitHub - bjw-s/home-ops: My home or for-home infrastructure written as code, adhering to GitOps practices***](https://github.com/bjw-s/home-ops)

![GitHub last commit](https://img.shields.io/github/last-commit/bjw-s/home-ops) ![GitHub Repo stars](https://img.shields.io/github/stars/bjw-s/home-ops?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/bjw-s/home-ops)



</br>


<details>

<summary>README</summary> 

<!-- markdownlint-disable MD041 -->
<img src="https://camo.githubusercontent.com/5b298bf6b0596795602bd771c5bddbb963e83e0f/68747470733a2f2f692e696d6775722e636f6d2f7031527a586a512e706e67" align="left" width="144px" height="144px"/>

# My home Kubernetes cluster managed by GitOps

_... managed by Flux and serviced with RenovateBot_ :robot:

<br/>
<br/>
<br/>

<div align="center">

[![Discord](https://img.shields.io/discord/673534664354430999?style=for-the-badge&label=discord&logo=discord&logoColor=white&color=teal)](https://discord.gg/k8s-at-home)
[![k3s](https://img.shields.io/badge/k3s-v1.21.3-blue?style=for-the-badge&logo=kubernetes&logoColor=white)](https://k3s.io/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled?logo=pre-commit&logoColor=white&style=for-the-badge&color=brightgreen)](https://github.com/pre-commit/pre-commit)
[![renovate](https://img.shields.io/badge/renovate-enabled?style=for-the-badge&logo=renovatebot&logoColor=white&color=brightgreen)](https://github.com/renovatebot/renovate)

</div>

---

## :wave: Overview

Welcome to my home operations repository.

Lots of fun (to me at least :wink:) stuff can be found, poke around my [Kubernetes clusters](./kubernetes/clusters) directory to see what they are running. Feel free to open a [GitHub Issue](https://github.com/bjw-s/home-ops/issues/new).

For more information, head on over to my [docs](https://bjw-s.github.io/home-ops/).

---

## :handshake:&nbsp; Thanks

A lot of inspiration for my cluster came from the people that have shared their clusters over at [awesome-home-kubernetes](https://github.com/k8s-at-home/awesome-home-kubernetes)


</details>



</br>



[***GitHub - argoproj/gitops-engine: Democratizing GitOps***](https://github.com/argoproj/gitops-engine)

![GitHub last commit](https://img.shields.io/github/last-commit/argoproj/gitops-engine) ![GitHub Repo stars](https://img.shields.io/github/stars/argoproj/gitops-engine?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/argoproj/gitops-engine)



</br>



</br>



[***GitHub - mogensen/kubernetes-split-yaml: Split the &#39;giant yaml file&#39; into one file pr kubernetes resource***](https://github.com/mogensen/kubernetes-split-yaml)

![GitHub last commit](https://img.shields.io/github/last-commit/mogensen/kubernetes-split-yaml) ![GitHub Repo stars](https://img.shields.io/github/stars/mogensen/kubernetes-split-yaml?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/mogensen/kubernetes-split-yaml)



</br>



</br>



[***GitHub - mikefarah/yq: yq is a portable command-line YAML, JSON and XML processor***](https://github.com/mikefarah/yq)

![GitHub last commit](https://img.shields.io/github/last-commit/mikefarah/yq) ![GitHub Repo stars](https://img.shields.io/github/stars/mikefarah/yq?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/mikefarah/yq)


***QUICK INSTALL***

```bash
curl -L --silent "https://github.com/mikefarah/yq/releases/download/$(curl -L -s "https://api.github.com/repos/mikefarah/yq/releases/latest" | grep -Poe '"tag_name": "\K.*?(?=")')/yq_linux_amd64" -o /bin/yq && chmod +x /bin/yq
```


</br>



</br>



[***GitHub - cookiecutter/cookiecutter: A cross-platform command-line utility that creates projects from cookiecutters (project templates), e.g. Python package projects, C projects.***](https://github.com/cookiecutter/cookiecutter)

![GitHub last commit](https://img.shields.io/github/last-commit/cookiecutter/cookiecutter) ![GitHub Repo stars](https://img.shields.io/github/stars/cookiecutter/cookiecutter?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/cookiecutter/cookiecutter)


***QUICK INSTALL***

```bash
python3 -m pip install --user cookiecutter
```


</br>



</br>



[***GitHub - google/python-fire: Python Fire is a library for automatically generating command line interfaces (CLIs) from absolutely any Python object.***](https://github.com/google/python-fire)

![GitHub last commit](https://img.shields.io/github/last-commit/google/python-fire) ![GitHub Repo stars](https://img.shields.io/github/stars/google/python-fire?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/google/python-fire)



</br>



</br>



[***GitHub - nektos/act: Run your GitHub Actions locally 🚀***](https://github.com/nektos/act)

![GitHub last commit](https://img.shields.io/github/last-commit/nektos/act) ![GitHub Repo stars](https://img.shields.io/github/stars/nektos/act?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/nektos/act)


***QUICK INSTALL***

```bash
curl -L "https://github.com/nektos/act/releases/download/$(curl -L -s "https://api.github.com/repos/nektos/act/releases/latest" | grep -Poe '"tag_name": "\K.*?(?=")')/act_Linux_x86_64.tar.gz" | tar --extract -C ~/.local/bin -zxvf -
```


</br>



</br>



[***GitHub - k8s-at-home/flux-cluster-template: Highly opinionated template for deploying a single Kubernetes (k3s) cluster with Ansible and Terraform backed by Flux, SOPS, GitHub Actions, Renovate and more!***](https://github.com/k8s-at-home/flux-cluster-template)

![GitHub last commit](https://img.shields.io/github/last-commit/k8s-at-home/flux-cluster-template) ![GitHub Repo stars](https://img.shields.io/github/stars/k8s-at-home/flux-cluster-template?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/k8s-at-home/flux-cluster-template)



</br>


<details>

<summary>README</summary> 

# Template for deploying k3s backed by Flux

Highly opinionated template for deploying a single [k3s](https://k3s.io) cluster with [Ansible](https://www.ansible.com) and [Terraform](https://www.terraform.io) backed by [Flux](https://toolkit.fluxcd.io/) and [SOPS](https://toolkit.fluxcd.io/guides/mozilla-sops/).

The purpose here is to showcase how you can deploy an entire Kubernetes cluster and show it off to the world using the [GitOps](https://www.weave.works/blog/what-is-gitops-really) tool [Flux](https://toolkit.fluxcd.io/). When completed, your Git repository will be driving the state of your Kubernetes cluster. In addition with the help of the [Ansible](https://github.com/ansible-collections/community.sops), [Terraform](https://github.com/carlpett/terraform-provider-sops) and [Flux](https://toolkit.fluxcd.io/guides/mozilla-sops/) SOPS integrations you'll be able to commit [Age](https://github.com/FiloSottile/age) encrypted secrets to your public repo.

## Overview

- [Introduction](https://github.com/k8s-at-home/flux-cluster-template#-introduction)
- [Prerequisites](https://github.com/k8s-at-home/flux-cluster-template#-prerequisites)
- [Repository structure](https://github.com/k8s-at-home/flux-cluster-template#-repository-structure)
- [Lets go!](https://github.com/k8s-at-home/flux-cluster-template#-lets-go)
- [Post installation](https://github.com/k8s-at-home/flux-cluster-template#-post-installation)
- [Troubleshooting](https://github.com/k8s-at-home/flux-cluster-template#-troubleshooting)
- [What's next](https://github.com/k8s-at-home/flux-cluster-template#-whats-next)
- [Thanks](https://github.com/k8s-at-home/flux-cluster-template#-thanks)

## 👋 Introduction

The following components will be installed in your [k3s](https://k3s.io/) cluster by default. Most are only included to get a minimum viable cluster up and running.

- [flux](https://toolkit.fluxcd.io/) - GitOps operator for managing Kubernetes clusters from a Git repository
- [kube-vip](https://kube-vip.io/) - Load balancer for the Kubernetes control plane nodes
- [metallb](https://metallb.universe.tf/) - Load balancer for Kubernetes services
- [cert-manager](https://cert-manager.io/) - Operator to request SSL certificates and store them as Kubernetes resources
- [calico](https://www.tigera.io/project-calico/) - Container networking interface for inter pod and service networking
- [external-dns](https://github.com/kubernetes-sigs/external-dns) - Operator to publish DNS records to Cloudflare (and other providers) based on Kubernetes ingresses
- [k8s_gateway](https://github.com/ori-edge/k8s_gateway) - DNS resolver that provides local DNS to your Kubernetes ingresses
- [traefik](https://traefik.io) - Kubernetes ingress controller used for a HTTP reverse proxy of Kubernetes ingresses
- [local-path-provisioner](https://github.com/rancher/local-path-provisioner) - provision persistent local storage with Kubernetes

_Additional applications include [hajimari](https://github.com/toboshii/hajimari), [error-pages](https://github.com/tarampampam/error-pages), [echo-server](https://github.com/Ealenn/Echo-Server), [system-upgrade-controller](https://github.com/rancher/system-upgrade-controller), [reflector](https://github.com/emberstack/kubernetes-reflector), [reloader](https://github.com/stakater/Reloader), and [kured](https://github.com/weaveworks/kured)_

For provisioning the following tools will be used:

- [Ubuntu](https://ubuntu.com/download/server) - Universal operating system that supports running all kinds of home related workloads in Kubernetes
- [Ansible](https://www.ansible.com) - Provision the Ubuntu OS and install k3s
- [Terraform](https://www.terraform.io) - Provision an already existing Cloudflare domain and certain DNS records to be used with your k3s cluster

## 📝 Prerequisites

**Note:** _This template has not been tested on cloud providers like AWS EC2, Hetzner, Scaleway etc... Those cloud offerings probably have a better way of provsioning a Kubernetes cluster and it's advisable to use those instead of the Ansible playbooks included here. This repository can still be used for the GitOps/Flux portion if there's a cluster working in one those environments._

### 💻 Systems

- One or more nodes with a fresh install of [Ubuntu Server 22.04](https://ubuntu.com/download/server).
  - These nodes can be ARM64/AMD64 bare metal or VMs.
  - An odd number of control plane nodes, greater than or equal to 3 is required if deploying more than one control plane node.
- A [Cloudflare](https://www.cloudflare.com/) account with a domain, this will be managed by Terraform and external-dns. You can [register new domains](https://www.cloudflare.com/products/registrar/) directly thru Cloudflare.
- Some experience in debugging problems and a positive attitude ;)

📍 It is recommended to have 3 master nodes for a highly available control plane.

### 🔧 Workstation Tools

1. Install the **most recent versions** of the following CLI tools on your workstation, if you are using [Homebrew](https://brew.sh/) on MacOS or Linux skip to steps 3 and 4.

    * Required: [age](https://github.com/FiloSottile/age), [ansible](https://www.ansible.com), [flux](https://toolkit.fluxcd.io/), [gitleaks](https://github.com/zricethezav/gitleaks), [go-task](https://github.com/go-task/task), [ipcalc](http://jodies.de/ipcalc), [jq](https://stedolan.github.io/jq/), [kubectl](https://kubernetes.io/docs/tasks/tools/), [pre-commit](https://github.com/pre-commit/pre-commit), [sops](https://github.com/mozilla/sops), [terraform](https://www.terraform.io), [yq](https://github.com/mikefarah/yq)

    * Recommended: [direnv](https://github.com/direnv/direnv), [helm](https://helm.sh/), [kustomize](https://github.com/kubernetes-sigs/kustomize), [prettier](https://github.com/prettier/prettier), [stern](https://github.com/stern/stern), [yamllint](https://github.com/adrienverge/yamllint)

2. This guide heavily relies on [go-task](https://github.com/go-task/task) as a framework for setting things up. It is advised to learn and understand the commands it is running under the hood.

3. Install [go-task](https://github.com/go-task/task) via Brew

    ```sh
    brew install go-task/tap/go-task
    ```

4. Install workstation dependencies via Brew

    ```sh
    task init
    ```

### ⚠️ pre-commit

It is advisable to install [pre-commit](https://pre-commit.com/) and the pre-commit hooks that come with this repository.
[sops-pre-commit](https://github.com/k8s-at-home/sops-pre-commit) will check to make sure you are not committing non-encrypted Kubernetes secrets to your repository.

1. Enable Pre-Commit

    ```sh
    task precommit:init
    ```

2. Update Pre-Commit, though it will occasionally make mistakes, so verify its results.

    ```sh
    task precommit:update
    ```

## 📂 Repository structure

The Git repository contains the following directories under `cluster` and are ordered below by how Flux will apply them.

```sh
📁 cluster      # k8s cluster defined as code
├─📁 flux       # flux, gitops operator, loaded before everything
├─📁 crds       # custom resources, loaded before 📁 core and 📁 apps
├─📁 charts     # helm repos, loaded before 📁 core and 📁 apps
├─📁 config     # cluster config, loaded before 📁 core and 📁 apps
├─📁 core       # crucial apps, namespaced dir tree, loaded before 📁 apps
└─📁 apps       # regular apps, namespaced dir tree, loaded last
```

## 🚀 Lets go

Very first step will be to create a new repository by clicking the **Use this template** button on this page.

Clone the repo to you local workstation and `cd` into it.

📍 **All of the below commands** are run on your **local** workstation, **not** on any of your cluster nodes.

### 🔐 Setting up Age

📍 Here we will create a Age Private and Public key. Using [SOPS](https://github.com/mozilla/sops) with [Age](https://github.com/FiloSottile/age) allows us to encrypt secrets and use them in Ansible, Terraform and Flux.

1. Create a Age Private / Public Key

    ```sh
    age-keygen -o age.agekey
    ```

2. Set up the directory for the Age key and move the Age file to it

    ```sh
    mkdir -p ~/.config/sops/age
    mv age.agekey ~/.config/sops/age/keys.txt
    ```

3. Export the `SOPS_AGE_KEY_FILE` variable in your `bashrc`, `zshrc` or `config.fish` and source it, e.g.

    ```sh
    export SOPS_AGE_KEY_FILE=~/.config/sops/age/keys.txt
    source ~/.bashrc
    ```

4. Fill out the Age public key in the `.config.env` under `BOOTSTRAP_AGE_PUBLIC_KEY`, **note** the public key should start with `age`...

### ☁️ Global Cloudflare API Key

In order to use Terraform and `cert-manager` with the Cloudflare DNS challenge you will need to create a API key.

1. Head over to Cloudflare and create a API key by going [here](https://dash.cloudflare.com/profile/api-tokens).

2. Under the `API Keys` section, create a global API Key.

3. Use the API Key in the configuration section below.

📍 You may wish to update this later on to a Cloudflare **API Token** which can be scoped to certain resources. I do not recommend using a Cloudflare **API Key**, however for the purposes of this template it is easier getting started without having to define which scopes and resources are needed. For more information see the [Cloudflare docs on API Keys and Tokens](https://developers.cloudflare.com/api/).

### 📄 Configuration

📍 The `.config.env` file contains necessary configuration that is needed by Ansible, Terraform and Flux.

1. Copy the `.config.sample.env` to `.config.env` and start filling out all the environment variables.

    **All are required** unless otherwise noted in the comments.

    ```sh
    cp .config.sample.env .config.env
    ```

2. Once that is done, verify the configuration is correct by running:

    ```sh
    task verify
    ```

3. If you do not encounter any errors run start having the script wire up the templated files and place them where they need to be.

    ```sh
    task configure
    ```

### ⚡ Preparing Ubuntu with Ansible

📍 Here we will be running a Ansible Playbook to prepare Ubuntu for running a Kubernetes cluster.

📍 Nodes are not security hardened by default, you can do this with [dev-sec/ansible-collection-hardening](https://github.com/dev-sec/ansible-collection-hardening) or similar if it supports Ubuntu 22.04.

1. Ensure you are able to SSH into your nodes from your workstation using a private SSH key **without a passphrase**. This is how Ansible is able to connect to your remote nodes.

   [How to configure SSH key-based authentication](https://www.digitalocean.com/community/tutorials/how-to-configure-ssh-key-based-authentication-on-a-linux-server)

2. Install the Ansible deps

    ```sh
    task ansible:init
    ```

3. Verify Ansible can view your config

    ```sh
    task ansible:list
    ```

4. Verify Ansible can ping your nodes

    ```sh
    task ansible:ping
    ```

5. Run the Ubuntu Prepare Ansible playbook

    ```sh
    task ansible:prepare
    ```

6. Reboot the nodes

    ```sh
    task ansible:reboot
    ```

### ⛵ Installing k3s with Ansible

📍 Here we will be running a Ansible Playbook to install [k3s](https://k3s.io/) with [this](https://galaxy.ansible.com/xanmanning/k3s) wonderful k3s Ansible galaxy role. After completion, Ansible will drop a `kubeconfig` in `./provision/kubeconfig` for use with interacting with your cluster with `kubectl`.

☢️ If you run into problems, you can run `task ansible:nuke` to destroy the k3s cluster and start over.

1. Verify Ansible can view your config

    ```sh
    task ansible:list
    ```

2. Verify Ansible can ping your nodes

    ```sh
    task ansible:ping
    ```

3. Install k3s with Ansible

    ```sh
    task ansible:install
    ```

4. Verify the nodes are online

    ```sh
    task cluster:nodes
    # NAME           STATUS   ROLES                       AGE     VERSION
    # k8s-0          Ready    control-plane,master      4d20h   v1.21.5+k3s1
    # k8s-1          Ready    worker                    4d20h   v1.21.5+k3s1
    ```

### ☁️ Configuring Cloudflare DNS with Terraform

📍 Review the Terraform scripts under `./provision/terraform/cloudflare/` and make sure you understand what it's doing (no really review it).

If your domain already has existing DNS records **be sure to export those DNS settings before you continue**.

1. Pull in the Terraform deps

    ```sh
    task terraform:init
    ```

2. Review the changes Terraform will make to your Cloudflare domain

    ```sh
    task terraform:plan
    ```

3. Have Terraform apply your Cloudflare settings

    ```sh
    task terraform:apply
    ```

If Terraform was ran successfully you can log into Cloudflare and validate the DNS records are present.

The cluster application [external-dns](https://github.com/kubernetes-sigs/external-dns) will be managing the rest of the DNS records you will need.

### 🔹 GitOps with Flux

📍 Here we will be installing [flux](https://toolkit.fluxcd.io/) after some quick bootstrap steps.

1. Verify Flux can be installed

    ```sh
    task cluster:verify
    # ► checking prerequisites
    # ✔ kubectl 1.21.5 >=1.18.0-0
    # ✔ Kubernetes 1.21.5+k3s1 >=1.16.0-0
    # ✔ prerequisites checks passed
    ```

2. Push you changes to git

    📍 **Verify** all the `*.sops.yaml` and `*.sops.yml` files under the `./cluster` and `./provision` folders are **encrypted** with SOPS

    ```sh
    git add -A
    git commit -m "Initial commit :rocket:"
    git push
    ```

3. Install Flux and sync the cluster to the Git repository

    ```sh
    task cluster:install
    # namespace/flux-system configured
    # customresourcedefinition.apiextensions.k8s.io/alerts.notification.toolkit.fluxcd.io created
    ```

4. Verify Flux components are running in the cluster

    ```sh
    task cluster:pods -- -n flux-system
    # NAME                                       READY   STATUS    RESTARTS   AGE
    # helm-controller-5bbd94c75-89sb4            1/1     Running   0          1h
    # kustomize-controller-7b67b6b77d-nqc67      1/1     Running   0          1h
    # notification-controller-7c46575844-k4bvr   1/1     Running   0          1h
    # source-controller-7d6875bcb4-zqw9f         1/1     Running   0          1h
    ```

### 🎤 Verification Steps

_Mic check, 1, 2_ - In a few moments applications should be lighting up like a Christmas tree 🎄

You are able to run all the commands below with one task

```sh
task cluster:resources
```

1. View the Flux Git Repositories

    ```sh
    task cluster:gitrepositories
    ```

2. View the Flux kustomizations

    ```sh
    task cluster:kustomizations
    ```

3. View all the Flux Helm Releases

    ```sh
    task cluster:helmreleases
    ```

4. View all the Flux Helm Repositories

    ```sh
    task cluster:helmrepositories
    ```

5. View all the Pods

    ```sh
    task cluster:pods
    ```

6. View all the certificates and certificate requests

    ```sh
    task cluster:certificates
    ```

7. View all the ingresses

    ```sh
    task cluster:ingresses
    ```

🏆 **Congratulations** if all goes smooth you'll have a Kubernetes cluster managed by Flux, your Git repository is driving the state of your cluster.

☢️ If you run into problems, you can run `task ansible:nuke` to destroy the k3s cluster and start over.

🧠 Now it's time to pause and go get some coffee ☕ because next is describing how DNS is handled.

## 📣 Post installation

### 🌐 DNS

📍 The [external-dns](https://github.com/kubernetes-sigs/external-dns) application created in the `networking` namespace will handle creating public DNS records. By default, `echo-server` is the only public domain exposed on your Cloudflare domain. In order to make additional applications public you must set an ingress annotation like in the `HelmRelease` for `echo-server`. You do not need to use Terraform to create additional DNS records unless you need a record outside the purposes of your Kubernetes cluster (e.g. setting up MX records).

[k8s_gateway](https://github.com/ori-edge/k8s_gateway) is deployed on the IP choosen for `${BOOTSTRAP_METALLB_K8S_GATEWAY_ADDR}`. Inorder to test DNS you can point your clients DNS to the `${BOOTSTRAP_METALLB_K8S_GATEWAY_ADDR}` IP address and load `https://hajimari.${BOOTSTRAP_CLOUDFLARE_DOMAIN}` in your browser.

You can also try debugging with the command `dig`, e.g. `dig @${BOOTSTRAP_METALLB_K8S_GATEWAY_ADDR} hajimari.${BOOTSTRAP_CLOUDFLARE_DOMAIN}` and you should get a valid answer containing your `${BOOTSTRAP_METALLB_TRAEFIK_ADDR}` IP address.

If your router (or Pi-Hole, Adguard Home or whatever) supports conditional DNS forwarding (also know as split-horizon DNS) you may have DNS requests for `${SECRET_DOMAIN}` only point to the  `${BOOTSTRAP_METALLB_K8S_GATEWAY_ADDR}` IP address. This will ensure only DNS requests for `${SECRET_DOMAIN}` will only get routed to your [k8s_gateway](https://github.com/ori-edge/k8s_gateway) service thus providing DNS resolution to your cluster applications/ingresses.

To access services from the outside world port forwarded `80` and `443` in your router to the `${BOOTSTRAP_METALLB_TRAEFIK_ADDR}` IP, in a few moments head over to your browser and you _should_ be able to access `https://echo-server.${BOOTSTRAP_CLOUDFLARE_DOMAIN}` from a device outside your LAN.

Now if nothing is working, that is expected. This is DNS after all!

### 🔐 SSL

By default in this template Kubernetes ingresses are set to use the [Let's Encrypt Staging Environment](https://letsencrypt.org/docs/staging-environment/). This will hopefully reduce issues from ACME on requesting certificates until you are ready to use this in "Production".

Once you have confirmed there are no issues requesting your certificates replace `letsencrypt-staging` with `letsencrypt-production` in your ingress annotations for `cert-manager.io/cluster-issuer`

### 🤖 Renovatebot

[Renovatebot](https://www.mend.io/free-developer-tools/renovate/) will scan your repository and offer PRs when it finds dependencies out of date. Common dependencies it will discover and update are Flux, Ansible Galaxy Roles, Terraform Providers, Kubernetes Helm Charts, Kubernetes Container Images, Pre-commit hooks updates, and more!

The base Renovate configuration provided in your repository can be view at [.github/renovate.json5](https://github.com/k8s-at-home/flux-cluster-template/blob/main/.github/renovate.json5). If you notice this only runs on weekends and you can [change the schedule to anything you want](https://docs.renovatebot.com/presets-schedule/) or simply remove it.

To enable Renovate on your repository, click the 'Configure' button over at their [Github app page](https://github.com/apps/renovate) and choose your repository. Over time Renovate will create PRs for out-of-date dependencies it finds. Any merged PRs that are in the cluster directory Flux will deploy.

### 🪝 Github Webhook

Flux is pull-based by design meaning it will periodically check your git repository for changes, using a webhook you can enable Flux to update your cluster on `git push`. In order to configure Github to send `push` events from your repository to the Flux webhook receiver you will need two things:

1. Webhook URL - Your webhook receiver will be deployed on `https://flux-receiver.${BOOTSTRAP_CLOUDFLARE_DOMAIN}/hook/:hookId`. In order to find out your hook id you can run the following command:

    ```sh
    kubectl -n flux-system get receiver/github-receiver --kubeconfig=./provision/kubeconfig
    # NAME              AGE    READY   STATUS
    # github-receiver   6h8m   True    Receiver initialized with URL: /hook/12ebd1e363c641dc3c2e430ecf3cee2b3c7a5ac9e1234506f6f5f3ce1230e123
    ```

    So if my domain was `k8s-at-home.com` the full url would look like this:

    ```text
    https://flux-receiver.k8s-at-home.com/hook/12ebd1e363c641dc3c2e430ecf3cee2b3c7a5ac9e1234506f6f5f3ce1230e123
    ```

2. Webhook secret - Your webhook secret can be found by decrypting the `secret.sops.yaml` using the following command:

    ```sh
    sops -d ./cluster/apps/flux-system/webhooks/github/secret.sops.yaml | yq .stringData.token
    ```

    **Note:** Don't forget to update the `BOOTSTRAP_FLUX_GITHUB_WEBHOOK_SECRET` variable in your `.config.env` file so it matches the generated secret if applicable

Now that you have the webhook url and secret, it's time to set everything up on the Github repository side. Navigate to the settings of your repository on Github, under "Settings/Webhooks" press the "Add webhook" button. Fill in the webhook url and your secret.

### 💾 Storage

Rancher's `local-path-provisioner` is a great start for storage but soon you might find you need more features like replicated block storage, or to connect to a NFS/SMB/iSCSI server. Check out the projects below to read up more on some storage solutions that might work for you.

- [rook-ceph](https://github.com/rook/rook)
- [longhorn](https://github.com/longhorn/longhorn)
- [openebs](https://github.com/openebs/openebs)
- [nfs-subdir-external-provisioner](https://github.com/kubernetes-sigs/nfs-subdir-external-provisioner)
- [democratic-csi](https://github.com/democratic-csi/democratic-csi)
- [csi-driver-nfs](https://github.com/kubernetes-csi/csi-driver-nfs)
- [synology-csi](https://github.com/SynologyOpenSource/synology-csi)

### 🔏 Authenticate Flux over SSH

Authenticating Flux to your git repository has a couple benefits like using a private git repository and/or using the Flux [Image Automation Controllers](https://fluxcd.io/docs/components/image/).

By default this template only works on a public GitHub repository, it is advised to keep your repository public.

The benefits of a public repository include:

* Debugging or asking for help, you can provide a link to a resource you are having issues with.
* Adding a topic to your repository of `k8s-at-home` to be included in the [k8s-at-home-search](https://whazor.github.io/k8s-at-home-search/). This search helps people discover different configurations of Helm charts across others Flux based repositories.

<details>
  <summary>Expand to read guide on adding Flux SSH authentication</summary>

  1. Generate new SSH key:
      ```sh
      ssh-keygen -t ecdsa -b 521 -C "github-deploy-key" -f ./cluster/github-deploy-key -q -P ""
      ```
  2. Paste public key in the deploy keys section of your repository settings
  3. Create sops secret in `cluster/flux/flux-system/github-deploy-key.sops.yaml` with the contents of:
      ```yaml
      # yamllint disable
      apiVersion: v1
      kind: Secret
      metadata:
          name: github-deploy-key
          namespace: flux-system
      stringData:
          # 3a. Contents of github-deploy-key
          identity: |
              -----BEGIN OPENSSH PRIVATE KEY-----
                  ...
              -----END OPENSSH PRIVATE KEY-----
          # 3b. Output of curl --silent https://api.github.com/meta | jq --raw-output '"github.com "+.ssh_keys[]'
          known_hosts: |
              github.com ssh-ed25519 ...
              github.com ecdsa-sha2-nistp256 ...
              github.com ssh-rsa ...
      ```
  4. Encrypt secret:
      ```sh
      sops --encrypt --in-place ./cluster/flux/flux-system/github-deploy-key.sops.yaml
      ```
  5. Apply secret to cluster:
      ```sh
      sops --decrypt cluster/flux/flux-system/github-deploy-key.sops.yaml | kubectl apply -f -
      ```
  6.  Update `cluster/flux/flux-system/flux-cluster.yaml`:
      ```yaml
      ---
      apiVersion: source.toolkit.fluxcd.io/v1beta2
      kind: GitRepository
      metadata:
        name: flux-cluster
        namespace: flux-system
      spec:
        interval: 10m
        # 6a: Change this to your user and repo names
        url: ssh://git@github.com/$user/$repo
        ref:
          branch: main
        secretRef:
          name: github-deploy-key
      ```
  7. Commit and push changes
  8. Force flux to reconcile your changes
     ```sh
     task cluster:reconcile
     ```
  9. Verify git repository is now using SSH:
      ```sh
      task cluster:gitrepositories
      ```
  10. Optionally set your repository to Private in your repository settings.
</details>

## 👉 Troubleshooting

Our [wiki](https://github.com/k8s-at-home/flux-cluster-template/wiki) (WIP, contributions welcome) is a good place to start troubleshooting issues. If that doesn't cover your issue, come join and say Hi in our [Discord](https://discord.gg/k8s-at-home) server by starting a new thread in the #kubernetes support channel.

You may also open a issue on this GitHub repo or open a [discussion on GitHub](https://github.com/k8s-at-home/organization/discussions).

## ❔ What's next

The world is your cluster, see below for important things you could work on adding.

Our Check out our [wiki](https://github.com/k8s-at-home/flux-cluster-template/wiki) (WIP, contributions welcome) for more integrations!

## 🤝 Thanks

Big shout out to all the authors and contributors to the projects that we are using in this repository.

Community member @Whazor created [this website](https://whazor.github.io/k8s-at-home-search/) as a creative way to search Helm Releases across GitHub. You may use it as a means to get ideas on how to configure an applications' Helm values.

Many people have shared their awesome repositories over at [awesome-home-kubernetes](https://github.com/k8s-at-home/awesome-home-kubernetes).


</details>



</br>



[***GitHub - FiloSottile/age: A simple, modern and secure encryption tool (and Go library) with small explicit keys, no config options, and UNIX-style composability.***](https://github.com/FiloSottile/age)

![GitHub last commit](https://img.shields.io/github/last-commit/FiloSottile/age) ![GitHub Repo stars](https://img.shields.io/github/stars/FiloSottile/age?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/FiloSottile/age)


***QUICK INSTALL***

```bash
curl -L "https://github.com/FiloSottile/age/releases/download/$(curl -L -s "https://api.github.com/repos/FiloSottile/age/releases/latest" | grep -Poe '"tag_name": "\K.*?(?=")')/age-$(curl -L -s "https://api.github.com/repos/FiloSottile/age/releases/latest" | grep -Poe '"tag_name": "\K.*?(?=")')-linux-amd64.tar.gz" | tar --extract -C ~/.local/bin --strip=1 -zxvf -
```


</br>


<details>

<summary>README</summary> 

<p align="center"><img alt="The age logo, an wireframe of St. Peters dome in Rome, with the text: age, file encryption" width="600" src="https://user-images.githubusercontent.com/1225294/132245842-fda4da6a-1cea-4738-a3da-2dc860861c98.png"></p>

[![Go Reference](https://pkg.go.dev/badge/filippo.io/age.svg)](https://pkg.go.dev/filippo.io/age)
[![man page](https://img.shields.io/badge/age(1)-man%20page-lightgrey)](https://filippo.io/age/age.1)
[![C2SP specification](https://img.shields.io/badge/%C2%A7%23-specification-blueviolet)](https://age-encryption.org/v1)

age is a simple, modern and secure file encryption tool, format, and Go library.

It features small explicit keys, no config options, and UNIX-style composability.

```
$ age-keygen -o key.txt
Public key: age1ql3z7hjy54pw3hyww5ayyfg7zqgvc7w3j2elw8zmrj2kg5sfn9aqmcac8p
$ tar cvz ~/data | age -r age1ql3z7hjy54pw3hyww5ayyfg7zqgvc7w3j2elw8zmrj2kg5sfn9aqmcac8p > data.tar.gz.age
$ age --decrypt -i key.txt data.tar.gz.age > data.tar.gz
```

The format specification is at [age-encryption.org/v1](https://age-encryption.org/v1). age was designed by [@Benjojo12](https://twitter.com/Benjojo12) and [@FiloSottile](https://twitter.com/FiloSottile).

An alternative interoperable Rust implementation is available at [github.com/str4d/rage](https://github.com/str4d/rage).

The author pronounces it `[aɡe̞]`, like the Italian [“aghe”](https://translate.google.com/?sl=it&text=aghe).

## Usage

For the full documentation, read [the age(1) man page](https://filippo.io/age/age.1).

```
Usage:
    age [--encrypt] (-r RECIPIENT | -R PATH)... [--armor] [-o OUTPUT] [INPUT]
    age [--encrypt] --passphrase [--armor] [-o OUTPUT] [INPUT]
    age --decrypt [-i PATH]... [-o OUTPUT] [INPUT]

Options:
    -e, --encrypt               Encrypt the input to the output. Default if omitted.
    -d, --decrypt               Decrypt the input to the output.
    -o, --output OUTPUT         Write the result to the file at path OUTPUT.
    -a, --armor                 Encrypt to a PEM encoded format.
    -p, --passphrase            Encrypt with a passphrase.
    -r, --recipient RECIPIENT   Encrypt to the specified RECIPIENT. Can be repeated.
    -R, --recipients-file PATH  Encrypt to recipients listed at PATH. Can be repeated.
    -i, --identity PATH         Use the identity file at PATH. Can be repeated.

INPUT defaults to standard input, and OUTPUT defaults to standard output.
If OUTPUT exists, it will be overwritten.

RECIPIENT can be an age public key generated by age-keygen ("age1...")
or an SSH public key ("ssh-ed25519 AAAA...", "ssh-rsa AAAA...").

Recipient files contain one or more recipients, one per line. Empty lines
and lines starting with "#" are ignored as comments. "-" may be used to
read recipients from standard input.

Identity files contain one or more secret keys ("AGE-SECRET-KEY-1..."),
one per line, or an SSH key. Empty lines and lines starting with "#" are
ignored as comments. Passphrase encrypted age files can be used as
identity files. Multiple key files can be provided, and any unused ones
will be ignored. "-" may be used to read identities from standard input.

When --encrypt is specified explicitly, -i can also be used to encrypt to an
identity file symmetrically, instead or in addition to normal recipients.
```

### Multiple recipients

Files can be encrypted to multiple recipients by repeating `-r/--recipient`. Every recipient will be able to decrypt the file.

```
$ age -o example.jpg.age -r age1ql3z7hjy54pw3hyww5ayyfg7zqgvc7w3j2elw8zmrj2kg5sfn9aqmcac8p \
    -r age1lggyhqrw2nlhcxprm67z43rta597azn8gknawjehu9d9dl0jq3yqqvfafg example.jpg
```

#### Recipient files

Multiple recipients can also be listed one per line in one or more files passed with the `-R/--recipients-file` flag.

```
$ cat recipients.txt
# Alice
age1ql3z7hjy54pw3hyww5ayyfg7zqgvc7w3j2elw8zmrj2kg5sfn9aqmcac8p
# Bob
age1lggyhqrw2nlhcxprm67z43rta597azn8gknawjehu9d9dl0jq3yqqvfafg
$ age -R recipients.txt example.jpg > example.jpg.age
```

If the argument to `-R` (or `-i`) is `-`, the file is read from standard input.

### Passphrases

Files can be encrypted with a passphrase by using `-p/--passphrase`. By default age will automatically generate a secure passphrase. Passphrase protected files are automatically detected at decrypt time.

```
$ age -p secrets.txt > secrets.txt.age
Enter passphrase (leave empty to autogenerate a secure one):
Using the autogenerated passphrase "release-response-step-brand-wrap-ankle-pair-unusual-sword-train".
$ age -d secrets.txt.age > secrets.txt
Enter passphrase:
```

### Passphrase-protected key files

If an identity file passed to `-i` is a passphrase encrypted age file, it will be automatically decrypted.

```
$ age-keygen | age -p > key.age
Public key: age1yhm4gctwfmrpz87tdslm550wrx6m79y9f2hdzt0lndjnehwj0ukqrjpyx5
Enter passphrase (leave empty to autogenerate a secure one):
Using the autogenerated passphrase "hip-roast-boring-snake-mention-east-wasp-honey-input-actress".
$ age -r age1yhm4gctwfmrpz87tdslm550wrx6m79y9f2hdzt0lndjnehwj0ukqrjpyx5 secrets.txt > secrets.txt.age
$ age -d -i key.age secrets.txt.age > secrets.txt
Enter passphrase for identity file "key.age":
```

Passphrase-protected identity files are not necessary for most use cases, where access to the encrypted identity file implies access to the whole system. However, they can be useful if the identity file is stored remotely.

### SSH keys

As a convenience feature, age also supports encrypting to `ssh-rsa` and `ssh-ed25519` SSH public keys, and decrypting with the respective private key file. (`ssh-agent` is not supported.)

```
$ age -R ~/.ssh/id_ed25519.pub example.jpg > example.jpg.age
$ age -d -i ~/.ssh/id_ed25519 example.jpg.age > example.jpg
```

Note that SSH key support employs more complex cryptography, and embeds a public key tag in the encrypted file, making it possible to track files that are encrypted to a specific public key.

#### Encrypting to a GitHub user

Combining SSH key support and `-R`, you can easily encrypt a file to the SSH keys listed on a GitHub profile.

```
$ curl https://github.com/benjojo.keys | age -R - example.jpg > example.jpg.age
```

Keep in mind that people might not protect SSH keys long-term, since they are revokable when used only for authentication, and that SSH keys held on YubiKeys can't be used to decrypt files.

## Installation

<table>
    <tr>
        <td>Homebrew (macOS or Linux)</td>
        <td>
            <code>brew install age</code>
        </td>
    </tr>
    <tr>
        <td>MacPorts</td>
        <td>
            <code>port install age</code>
        </td>
    </tr>
    <tr>
        <td>Alpine Linux v3.15+</td>
        <td>
            <code>apk add age</code>
        </td>
    </tr>
    <tr>
        <td>Arch Linux</td>
        <td>
            <code>pacman -S age</code>
        </td>
    </tr>
    <tr>
        <td>Debian 11+ (Bullseye)</td>
        <td>
            <code>apt install age</code>
        </td>
    </tr>
    <tr>
        <td>Fedora 33+</td>
        <td>
            <code>dnf install age</code>
        </td>
    </tr>
    <tr>
        <td>Gentoo Linux</td>
        <td>
            <code>emerge app-crypt/age</code>
        </td>
    </tr>
    <tr>
        <td>NixOS / Nix</td>
        <td>
            <code>nix-env -i age</code>
        </td>
    </tr>
    <tr>
        <td>openSUSE Tumbleweed</td>
        <td>
            <code>zypper install age</code>
        </td>
    </tr>
    <tr>
        <td>Ubuntu 21.04+</td>
        <td>
            <code>apt install age</code>
        </td>
    </tr>
    <tr>
        <td>Void Linux</td>
        <td>
            <code>xbps-install age</code>
        </td>
    </tr>
    <tr>
        <td>FreeBSD</td>
        <td>
            <code>pkg install age</code> (security/age)
        </td>
    </tr>
    <tr>
        <td>OpenBSD 6.7+</td>
        <td>
            <code>pkg_add age</code> (security/age)
        </td>
    </tr>
    <tr>
        <td>Chocolatey (Windows)</td>
        <td>
            <code>choco install age.portable</code>
        </td>
    </tr>
    <tr>
        <td>Scoop (Windows)</td>
        <td>
            <code>scoop bucket add extras; scoop install age</code>
        </td>
    </tr>
</table>

On Windows, Linux, macOS, and FreeBSD you can use the pre-built binaries.

```
https://dl.filippo.io/age/latest?for=linux/amd64
https://dl.filippo.io/age/v1.0.0-rc.1?for=darwin/arm64
...
```

If your system has [a supported version of Go](https://go.dev/dl/), you can build from source.

```
go install filippo.io/age/cmd/...@latest
```

Help from new packagers is very welcome.


</details>



</br>



[***GitHub - xUnholy/k8s-gitops: Kubernetes cluster managed by GitOps - Git as a single source of truth, automated pipelines, declarative everything, next-generation DevOps***](https://github.com/xUnholy/k8s-gitops)

![GitHub last commit](https://img.shields.io/github/last-commit/xUnholy/k8s-gitops) ![GitHub Repo stars](https://img.shields.io/github/stars/xUnholy/k8s-gitops?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/xUnholy/k8s-gitops)



</br>



</br>



[***GitHub - gnunn-gitops/standards: GitOps standards used in my other repos***](https://github.com/gnunn-gitops/standards)

![GitHub last commit](https://img.shields.io/github/last-commit/gnunn-gitops/standards) ![GitHub Repo stars](https://img.shields.io/github/stars/gnunn-gitops/standards?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/gnunn-gitops/standards)



</br>



</br>



[***GitHub - lepture/mistune: A fast yet powerful Python Markdown parser with renderers and plugins.***](https://github.com/lepture/mistune)

![GitHub last commit](https://img.shields.io/github/last-commit/lepture/mistune) ![GitHub Repo stars](https://img.shields.io/github/stars/lepture/mistune?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/lepture/mistune)



</br>



</br>



[***GitHub - ovity/octotree: GitHub on steroids***](https://github.com/ovity/octotree)

![GitHub last commit](https://img.shields.io/github/last-commit/ovity/octotree) ![GitHub Repo stars](https://img.shields.io/github/stars/ovity/octotree?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/ovity/octotree)



</br>



</br>



[***GitHub - helm/charts: ⚠️(OBSOLETE) Curated applications for Kubernetes***](https://github.com/helm/charts)

![GitHub last commit](https://img.shields.io/github/last-commit/helm/charts) ![GitHub Repo stars](https://img.shields.io/github/stars/helm/charts?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/helm/charts)



</br>



</br>



[***GitHub - xwmx/nb: CLI and local web plain text note‑taking, bookmarking, and archiving with linking, tagging, filtering, search, Git versioning &amp; syncing, Pandoc conversion, + more, in a single portable script.***](https://github.com/xwmx/nb)

![GitHub last commit](https://img.shields.io/github/last-commit/xwmx/nb) ![GitHub Repo stars](https://img.shields.io/github/stars/xwmx/nb?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/xwmx/nb)



</br>


<details>

<summary>README</summary> 

<p align="center">
  <img  src="https://raw.githubusercontent.com/xwmx/nb/master/docs/assets/images/nb.png"
        alt="nb"
        width="200">
</p>

<p align="center">
  <a href="https://github.com/xwmx/nb/actions" rel="nofollow">
    <img  src="https://img.shields.io/github/workflow/status/xwmx/nb/nb%20%C2%B7%20Test%20Suite"
          alt="Build Status"
          style="max-width:100%;">
  </a>
</p>

<br>

`nb` is a command line and local web
note‑taking, bookmarking, archiving,
and knowledge base application
with:

- plain text data storage,
- [encryption](#password-protected-encrypted-notes-and-bookmarks),
- [filtering](#listing--filtering), [pinning](#-pinning), [#tagging](#-tagging), and [search](#-search),
- [Git](https://git-scm.com/)-backed [versioning](#-revision-history) and [syncing](#-git-sync),
- [Pandoc](https://pandoc.org/)-backed [conversion](#%EF%B8%8F-import--export),
- <a href="#-linking">[[wiki-style linking]]</a>,
- terminal and GUI web [browsing](#-browsing),
- inline [images](#-images),
- [todos](#-todos) with [tasks](#%EF%B8%8F-tasks),
- global and local [notebooks](#-notebooks),
- organization with [folders](#-folders),
- customizable [color themes](#-color-themes),
- extensibility through [plugins](#-plugins),

and more, in a single portable script.

`nb` creates notes in text-based formats like
[Markdown](https://en.wikipedia.org/wiki/Markdown),
[Org](https://orgmode.org/),
and [LaTeX](https://www.latex-project.org/),
can work with files in any format,
can import and export notes to many document formats,
and can create private, password-protected encrypted notes and bookmarks.
With `nb`, you can write notes using
Vim,
Emacs,
VS Code,
Sublime Text,
and any other text editor you like,
as well as terminal and GUI web browsers.
`nb` works in any standard Linux / Unix environment,
including macOS and Windows via WSL.
[Optional dependencies](#optional) can be installed to enhance functionality,
but `nb` works great without them.

<p align="center">
  <img  src="https://xwmx.github.io/misc/nb/images/nb-theme-nb-home.png"
        alt="home"
        width="450">
</p>

`nb` is also a powerful [bookmarking](#-bookmarks) system featuring:

- locally-served, text-centric, distraction-free bookmark [browsing](#-browsing)
  in terminal and GUI web browsers,
- local full-text search of cached page content with regular expression support,
- convenient filtering and listing,
- [Internet Archive Wayback Machine](https://archive.org/web/) snapshot lookup
  for broken links,
- tagging, pinning, linking, and full integration with other `nb` features.

Page information is
downloaded,
cleaned up,
structured,
and saved
into normal Markdown documents made for humans,
so bookmarks are easy to view and edit just like any other note.

<p align="center">
  <img  src="https://xwmx.github.io/misc/nb/images/gui-terminal-browse.png"
        alt="nb browse"
        width="500">
</p>

`nb` uses [Git](https://git-scm.com/) in the background to
automatically record changes and sync notebooks with remote repositories.
`nb` can also be configured to
sync notebooks using a general purpose syncing utility like Dropbox
so notes can be edited in other apps on any device.

<p align="center">
  <img  src="https://xwmx.github.io/misc/nb/images/terminal-empty.png"
        alt="nb list empty"
        width="450">
</p>

`nb` is designed to be portable, future-focused, and vendor independent,
providing a full-featured and intuitive experience within
a highly composable multimodal user-centric text interface.
The entire program is contained within
a single [well-tested](#tests) shell script
that can be
installed, copied, or `curl`ed almost anywhere and just work,
using a strategy inspired by
[progressive enhancement](https://en.wikipedia.org/wiki/Progressive_enhancement)
for various experience improvements in more capable environments.
`nb` works great whether you have one notebook with just a few notes
or dozens of notebooks containing thousands of notes, bookmarks, and other items.
`nb` makes it easy to incorporate other tools, writing apps, and workflows.
`nb` can be used a little, a lot, once in a while, or for just a subset of features.
`nb` is flexible.

<p align="center">
  📝
  🔖
  🔒
  🔍
  📔
</p>

<br/>

<h1 align="center" id="nb"><code>nb</code></h1>

<p align="center">
  <a href="#installation">Installation</a>&nbsp;·
  <a href="#overview">Overview</a>&nbsp;&nbsp;
</p>

<p align="center">
  <a href="#help">Help</a>
</p>

<p align="center">
  <a href="#top">&nbsp;↑&nbsp;</a>
</p>

### Installation

#### Dependencies

##### Required

- [Bash](https://en.wikipedia.org/wiki/Bash_(Unix_shell))
  - `nb` works perfectly with Zsh, fish, and any other shell
    set as your primary login shell,
    the system just needs to have Bash available on it.
- [Git](https://git-scm.com/)
- A text editor with command line support, such as:
  - [Vim](https://en.wikipedia.org/wiki/Vim_\(text_editor\)),
  - [Emacs](https://en.wikipedia.org/wiki/Emacs),
  - [Visual Studio Code](https://code.visualstudio.com/),
  - [Sublime Text](https://www.sublimetext.com/),
  - [micro](https://github.com/zyedidia/micro),
  - [nano](https://en.wikipedia.org/wiki/GNU_nano),
  - [Atom](https://atom.io/),
  - [TextMate](https://macromates.com/),
  - [MacDown](https://macdown.uranusjr.com/),
  - [some of these](https://github.com/topics/text-editor),
  - [and many of these.](https://en.wikipedia.org/wiki/List_of_text_editors)

##### Optional

`nb` leverages standard command line tools
and works in standard Linux / Unix environments.
`nb` also checks the environment for some additional optional tools and
uses them to enhance the experience whenever they are available.

Recommended:

- [`bat`](https://github.com/sharkdp/bat)
- [`ncat`](https://nmap.org/ncat/)
- [`pandoc`](https://pandoc.org/)
- [`rg`](https://github.com/BurntSushi/ripgrep)
- [`tig`](https://github.com/jonas/tig)
- [`w3m`](https://en.wikipedia.org/wiki/W3m)

Also supported for various enhancements:

[Ack](https://beyondgrep.com/),
[`afplay`](https://ss64.com/osx/afplay.html),
[Ag - The Silver Searcher](https://github.com/ggreer/the_silver_searcher),
[`catimg`](https://github.com/posva/catimg),
[`exa`](https://github.com/ogham/exa),
[`ffplay`](https://ffmpeg.org/ffplay.html),
[ImageMagick](https://imagemagick.org/),
[GnuPG](https://en.wikipedia.org/wiki/GNU_Privacy_Guard),
[`highlight`](http://www.andre-simon.de/doku/highlight/en/highlight.php),
[`imgcat`](https://www.iterm2.com/documentation-images.html),
[kitty's `icat` kitten](https://sw.kovidgoyal.net/kitty/kittens/icat.html),
[Links](https://en.wikipedia.org/wiki/Links_(web_browser)),
[Lynx](https://en.wikipedia.org/wiki/Lynx_(web_browser)),
[Midnight Commander](https://en.wikipedia.org/wiki/Midnight_Commander),
[`mpg123`](https://en.wikipedia.org/wiki/Mpg123),
[MPlayer](https://en.wikipedia.org/wiki/MPlayer),
[ncat](https://nmap.org/ncat/),
[note-link-janitor](https://github.com/andymatuschak/note-link-janitor)
(via [plugin](https://github.com/xwmx/nb/blob/master/plugins/backlink.nb-plugin)),
[`pdftotext`](https://en.wikipedia.org/wiki/Pdftotext),
[Pygments](https://pygments.org/),
[Ranger](https://ranger.github.io/),
[readability-cli](https://gitlab.com/gardenappl/readability-cli),
[`rga` / ripgrep-all](https://github.com/phiresky/ripgrep-all),
[`termpdf.py`](https://github.com/dsanson/termpdf.py),
[vifm](https://vifm.info/)

#### macOS / Homebrew

```bash
brew tap xwmx/taps
brew install nb
```

Installing `nb` with Homebrew also installs
the recommended dependencies above
and completion scripts for Bash and Zsh.

#### Ubuntu, Windows WSL, and others

##### npm

```bash
npm install -g nb.sh
```

After `npm` installation completes, run
`sudo "$(which nb)" completions install`
to install Bash and Zsh completion scripts (recommended).

On Ubuntu and WSL, you can
run [`sudo "$(which nb)" env install`](#env)
to install the optional dependencies.

*`nb` is also available under its original package name,
[notes.sh](https://www.npmjs.com/package/notes.sh),
which comes with an extra `notes` executable wrapping `nb`.*

##### Download and Install

To install as an administrator,
copy and paste one of the following multi-line commands:

```bash
# install using wget
sudo wget https://raw.github.com/xwmx/nb/master/nb -O /usr/local/bin/nb &&
  sudo chmod +x /usr/local/bin/nb &&
  sudo nb completions install

# install using curl
sudo curl -L https://raw.github.com/xwmx/nb/master/nb -o /usr/local/bin/nb &&
  sudo chmod +x /usr/local/bin/nb &&
  sudo nb completions install
```

On Ubuntu and WSL, you can
run [`sudo nb env install`](#env) to install the optional dependencies.

###### User-only Installation

To install with just user permissions, simply
add the `nb` script to your `$PATH`.
If you already have a `~/bin` directory, for example, you can
use one of the following commands:

```bash
# download with wget
wget https://raw.github.com/xwmx/nb/master/nb -O ~/bin/nb && chmod +x ~/bin/nb

# download with curl
curl -L https://raw.github.com/xwmx/nb/master/nb -o ~/bin/nb && chmod +x ~/bin/nb
```

Installing with just user permissions doesn't include
the optional dependencies or completions,
but `nb` core functionality works without them.
If you have `sudo` access and want
to install the completion scripts and dependencies, run the following command:

```bash
sudo nb env install
```

##### Make

To install with [Make](https://en.wikipedia.org/wiki/Make_(software)),
clone this repository, navigate to the clone's root directory, and run:

```bash
sudo make install
```

This will also install the completion scripts on all systems and
the recommended dependencies on Ubuntu and WSL.

##### bpkg

To install with [bpkg](https://github.com/bpkg/bpkg):

```bash
bpkg install xwmx/nb
```

#### Tab Completion

Bash, Fish, and Zsh tab completion should be enabled
when `nb` is installed using the methods above,
assuming you have the appropriate system permissions or installed with `sudo`.
If completion isn't working after installing `nb`, see the
[completion installation instructions](https://github.com/xwmx/nb/tree/master/etc).

#### Updating

When `nb` is installed using a package manager like npm or Homebrew,
use the package manager's upgrade functionality to update `nb` to
the latest version.
When installed via other methods,
`nb` can be updated to the latest version using
the [`nb update`](#update) subcommand.

## Overview

<p align="center">
  <a href="#-notes"><code>📝</code>&nbsp;Notes</a>&nbsp;·
  <a href="#adding">Adding</a>&nbsp;·
  <a href="#listing--filtering">Listing</a>&nbsp;·
  <a href="#editing">Editing</a>&nbsp;·
  <a href="#viewing">Viewing</a>&nbsp;·
  <a href="#deleting">Deleting</a>&nbsp;·
  <a href="#-bookmarks"><code>🔖</code>&nbsp;Bookmarks</a>&nbsp;·
  <a href="#-todos"><code>✅</code>&nbsp;Todos</a>&nbsp;·
  <a href="#%EF%B8%8F-tasks"><code>✔️</code>&nbsp;Tasks</a>&nbsp;·
  <a href="#-tagging"><code>🏷</code>&nbsp;Tagging</a>&nbsp;·
  <a href="#-linking"><code>🔗</code>&nbsp;Linking</a>&nbsp;·
  <a href="#-browsing"><code>🌍</code>&nbsp;Browsing</a>&nbsp;·
  <a href="#-images"><code>🌄</code>&nbsp;Images</a>&nbsp;·
  <a href="#-zettelkasten"><code>🗂</code>&nbsp;Zettelkasten</a>&nbsp;·
  <a href="#-folders"><code>📂</code>&nbsp;Folders</a>&nbsp;·
  <a href="#-pinning"><code>📌</code>&nbsp;Pinning</a>&nbsp;·
  <a href="#-search"><code>🔍</code>&nbsp;Search</a>&nbsp;·
  <a href="#-moving--renaming"><code>↔</code>&nbsp;Moving&nbsp;&&nbsp;Renaming</a>&nbsp;·
  <a href="#-revision-history"><code>🗒</code>&nbsp;History</a>&nbsp;·
  <a href="#-notebooks"><code>📚</code>&nbsp;Notebooks</a>&nbsp;·
  <a href="#-git-sync"><code>🔄</code>&nbsp;Git&nbsp;Sync</a>&nbsp;·
  <a href="#%EF%B8%8F-import--export"><code>↕️</code>&nbsp;Import&nbsp;/&nbsp;Export</a>&nbsp;·
  <a href="#%EF%B8%8F-set--settings"><code>⚙️</code><code>set</code>&<code>settings</code></a>&nbsp;·
  <a href="#-color-themes"><code>🎨</code>&nbsp;Color&nbsp;Themes</a>&nbsp;·
  <a href="#-plugins"><code>🔌</code>&nbsp;Plugins</a>&nbsp;·
  <a href="#-selectors"><code>:/</code>&nbsp;Selectors</a>&nbsp;·
  <a href="#01-metadata"><code>01</code>&nbsp;Metadata</a>&nbsp;·
  <a href="#-interactive-shell"><code>❯</code>&nbsp;Shell</a>&nbsp;·
  <a href="#shortcut-aliases">Shortcuts</a>&nbsp;·
  <a href="#help">Help</a>&nbsp;·
  <a href="#specifications">Specifications</a>&nbsp;·
  <a href="#tests">Tests</a>
</p>

<p align="center">
  <a href="#nb">&nbsp;↑&nbsp;</a>
</p>

To get started, simply run:

```bash
nb
```

`nb` sets up your initial `home` notebook the first time it runs.

By default, notebooks and notes are global (at `~/.nb`),
so they are always available to `nb`
regardless of the current working directory.
`nb` also supports [local notebooks](#global-and-local-notebooks).

### 📝 Notes

#### Adding

<p>
  <sup>
    <a href="#overview">↑</a> ·
    <a href="#add"><code>nb add</code></a>,
    <a href="#browse"><code>nb browse add</code></a>
  </sup>
</p>

Use [`nb add`](#add) (shortcuts: [`nb a`](#add), [`nb +`](#add))
to create new notes:

```bash
# create a new note in your text editor
nb add

# create a new note with the filename "example.md"
nb add example.md

# create a new note containing "This is a note."
nb add "This is a note."

# create a new note with piped content
echo "Note content." | nb add

# create a new password-protected, encrypted note titled "Secret Document"
nb add --title "Secret Document" --encrypt

# create a new note in the notebook named "example"
nb example:add "This is a note."

# create a new note in the folder named "sample"
nb add sample/
```

[`nb add`](#add) with no arguments or input will open the new, blank note
in your environment's preferred text editor.
You can change your editor using
the `$EDITOR` environment variable
or [`nb set editor`](#editor).

`nb` files are [Markdown](https://daringfireball.net/projects/markdown/)
files by default. The default file type can be changed to
whatever you like
using [`nb set default_extension`](#default_extension).

[`nb add`](#add) has intelligent argument parsing
and behaves differently depending on the types of arguments it receives.
When a filename with extension is specified,
a new note with that filename is opened in the editor:

```bash
nb add example.md
```

When a string is specified, a new note is immediately created
with that string as the content and without opening the editor:

```bash
❯ nb add "This is a note."
Added: [1] 20200101000000.md
```

[`nb add <string>`](#add) is useful for quickly jotting down notes directly
via the command line. Quoting content is optional, but recommended.

When no filename is specified, [`nb add`](#add) uses the current datetime as
the filename.

[`nb add`](#add) can also receive piped content, which behaves the same as
[`nb add <string>`](#add):

```bash
# create a new note containing "Note content."
❯ echo "Note content." | nb add
Added: [6] 20200101000100.md

# create a new note containing the clipboard contents on macOS
❯ pbpaste | nb add
Added: [7] 20200101000200.md

# create a new note containing the clipboard contents using xclip
❯ xclip -o | nb add
Added: [8] 20200101000300.md
```

Content can be passed with the [`--content <content>`](#add) option,
which also creates a new note without opening the editor:

```bash
nb add --content "Note content."
```

When content is piped,
specified with [`--content <content>`](#add),
or passed as a string argument,
use the [`--edit`](#add) flag to open the file in the editor
before the change is committed.

The title, filename, and content can also be specified with long and
short options:

```bash
❯ nb add --filename "example.md" -t "Example Title" -c "Example content."
Added: [9] example.md "Example Title"
```

The [`-t <title>`](#add) / [`--title <title>`](#add) option also
sets the filename to the title,
lowercased with spaces and non-filename characters replaced with underscores:

```bash
❯ nb add --title "Example Title" "Example content."
Added: [10] example_title.md "Example Title"
```

Tags can be added with the [`--tags <tag1>,<tag2>...`](#add) option, which
takes a comma separated list of tags,
converts them to [#hashtags](#-tagging),
and inserts them between the title and content:

```bash
❯ nb add "Example content." --title "Tagged Example" --tags tag1,tag2
Added: [11] tagged_example.md "Tagged Example"

❯ nb show 11 --print
# Tagged Example

#tag1 #tag2

Example content.
```

[Search](#-search) for tagged items with
[`nb search`](#search) / [`nb q`](#search):

```bash
# search for items tagged with "#tag1"
nb search --tag tag1

# search for items tagged with "#tag1" AND "#tag2", short options
nb q -t tag1 -t tag2

# search for items tagged with "#tag1" OR "#tag2", arguments
nb q \#tag1 --or \#tag2
```

Files can be created with any file type by specifying the extension either
in the filename (`example.md`),
the extension by itself (`.md`),
or via the [`--type <type>`](#add) option (`--type md`):

```bash
# open a new Org file in the editor
nb add example.org

# open a new reStructuredText file in the editor
nb add --type rst

# open a new JavaScript file in the editor
nb add .js
```

Combining a type argument with piped clipboard content provides
a very convenient way to save code snippets using a clipboard utility such as
`pbpaste`,
`xclip`,
or [`pb`](https://github.com/xwmx/pb):

```bash
# save the clipboard contents as a JavaScript file in the current notebook
pb | nb add .js

# save the clipboard contents as a Rust file in the "rust" notebook
# using the shortcut alias `nb a`
pb | nb a rust: .rs

# save the clipboard contents as a Haskell file named "example.hs" in the
# "snippets" notebook using the shortcut alias `nb +`
pb | nb + snippets: example.hs
```

Use [`nb show`](#show) and [`nb browse`](#browse) to view code snippets
with automatic syntax highlighting and
use [`nb edit`](#edit) to open in your editor.

The [`clip` plugin](#clip) can also be used to
create notes from clipboard content.

Piping,
[`--title <title>`](#add),
[`--tags <tag-list>`](#add),
[`--content <content>`](#add),
and content passed in an argument
can be combined as needed
to create notes with content from multiple input methods and sources
using a single command:

```bash
❯ pb | nb add "Argument content." \
    --title   "Sample Title"      \
    --tags    tag1,tag2           \
    --content "Option content."
Added: [12] sample_title.md "Sample Title"

❯ nb show 12 --print
# Sample Title

#tag1 #tag2

Argument content.

Option content.

Clipboard content.
```

For a full list of options available for [`nb add`](#add), run
[`nb help add`](#add).

##### Password-Protected Encrypted Notes and Bookmarks

Password-protected notes and [bookmarks](#-bookmarks) are
created with the [`-e`](#add) / [`--encrypt`](#add) flag and
encrypted with AES-256 using OpenSSL by default.
GPG is also supported and can be configured with
[`nb set encryption_tool`](#encryption_tool).

Each protected note and bookmark is
encrypted individually with its own password.
When an encrypted item is viewed, edited, or opened,
`nb` will simply prompt for the item's password before proceeding.
After an item is edited,
`nb` automatically re-encrypts it and saves the new version.

Encrypted notes can be decrypted
using the OpenSSL and GPG command line tools directly, so
you aren't dependent on `nb` to decrypt your files.

##### Shortcut Aliases: `nb a`, `nb +`

`nb` includes shortcuts for many commands, including
[`nb a`](#add) and [`nb +`](#add) for [`nb add`](#add):

```bash
# create a new note in your text editor
nb a

# create a new note with the filename "example.md"
nb a example.md

# create a new note containing "This is a note."
nb + "This is a note."

# create a new note containing the clipboard contents with xclip
xclip -o | nb +

# create a new note in the notebook named "example"
nb example:a
```

##### Other Aliases: `nb create`, `nb new`

[`nb add`](#add) can also be invoked with
[`nb create`](#add) and [`nb new`](#add) for convenience:

```bash
# create a new note containing "Example note content."
nb new "Example note content."

# create a new note with the title "Example Note Title"
nb create --title "Example Note Title"
```

##### Adding with `nb browse`

Items can also be added within terminal and GUI web browsers using
[`nb browse add`](#browse) / [`nb b a`](#browse):

```bash
❯ nb browse add
❯nb · home : +

[                                                     ]
[                                                     ]
[                                                     ]
[                                                     ]
[                                                     ]
[                                                     ]
[                                                     ]
[                                                     ]
[                                                     ]
[                                                     ]

[add]
```

Pass a filename, relative path, and / or notebook name to
create a new note at that location:

```bash
# open the add form in the browser to create the file "file.md" in the folder "example"
nb browse add "example/file.md"
```

[`nb browse add`](#browse) includes options for quickly
pre-populating new notes with content:

```bash
❯ nb browse add --title "Example Title" --content "Example content." --tags tag1,tag2
❯nb · home : +

[# Example Title                                      ]
[                                                     ]
[#tag1 #tag2                                          ]
[                                                     ]
[Example content.                                     ]
[                                                     ]
[                                                     ]
[                                                     ]
[                                                     ]
[                                                     ]

[add]
```

[`nb browse add`](#browse) can also be opened with
[`nb add --browse`](#add) / [`nb a -b`](#add).

For more information, see [Browsing](#-browsing).

#### Listing & Filtering

<p>
  <sup>
    <a href="#overview">↑</a> ·
    <a href="#ls"><code>nb ls</code></a>,
    <a href="#list"><code>nb list</code></a>,
    <a href="#browse"><code>nb browse</code></a>
  </sup>
</p>

To list notes and notebooks, run [`nb ls`](#ls) (shortcut alias: `nb`):

<p align="center">
  <img  src="https://xwmx.github.io/misc/nb/images/nb-theme-utility-home.png"
        alt="nb ls"
        width="450">
</p>

Notebooks are listed above the line,
with the current notebook highlighted and/or underlined,
depending on terminal capabilities.
[`nb ls`](#ls) also includes a footer with example commands for easy reference.
The notebook header and command footer can be configured or hidden with
[`nb set header`](#header) and
[`nb set footer`](#footer).

```bash
❯ nb ls
home
----
[3] example.md · "Example content."
[2] sample.md · "Sample content."
[1] demo.md · "- Demo list item one."
```

Notes from the current notebook are listed in the order they were last modified.
By default, each note is listed with its
id, filename, and an excerpt from the first line of the note.
When a note has a title, the title is displayed
instead of the filename and first line.

Markdown titles can be defined within a note using
[either Markdown `h1` style](https://daringfireball.net/projects/markdown/syntax#header)
or [YAML front matter](#front-matter):

```markdown
# Example Title
```

```markdown
Sample Title
============
```

```markdown
---
title: Demo Title
---
```

[Org](https://orgmode.org/) and [LaTeX](https://www.latex-project.org/)
titles are recognized in `.org` and `.latex` files:

```text
#+TITLE: Example Org Title
```

```latex
\title{Example LaTeX Title}
```

Once defined, titles are displayed in place of the filename and first line
in the output of [`nb ls`](#ls):

```bash
❯ nb ls
home
----
[3] Example Title
[2] Sample Title
[1] Demo Title
```

Pass an id, filename, or title to view the listing for that note:

```bash
❯ nb ls Sample\ Title
[2] Sample Title

❯ nb ls 3
[3] Example Title
```

If there is no exact match, `nb` will list items with
titles and filenames that fuzzy match the query:

```bash
❯ nb ls exa
[3] Example Title

❯ nb ls ample
[3] Example Title
[2] Sample Title
```

Multiple words act like an `OR` filter, listing any
titles or filenames that match any of the words:

```bash
❯ nb ls example demo
[3] Example Title
[1] Demo Title
```

When multiple words are quoted, filter titles and filenames for that phrase:

```bash
❯ nb ls "example title"
[3] Example Title
```

For full text search, see [Search](#-search).

To view excerpts of notes, use the [`--excerpt`](#ls) or [`-e`](#ls) option,
which optionally accepts a length:

```bash
❯ nb ls 3 --excerpt
[3] Example Title
-----------------
# Example Title

This is an example excerpt.

❯ nb ls 3 -e 8
[3] Example Title
-----------------
# Example Title

This is an example excerpt.

More example content:
- one
- two
- three
```

Several classes of file types are represented with emoji
[indicators](#indicators) to make them easily identifiable in lists.
For example, bookmarks and encrypted notes are listed with `🔖` and `🔒`:

```bash
❯ nb ls
home
----
[4] Example Note
[3] 🔒 encrypted-note.md.enc
[2] 🔖 Example Bookmark (example.com)
[1] 🔖 🔒 encrypted.bookmark.md.enc
```

File types include:

```text
 🔉  Audio
 📖  Book
 🔖  Bookmark
 🔒  Encrypted
 📂  Folder
 🌄  Image
 📄  PDF, Word, or Open Office document
 📹  Video
```

By default, items are listed starting with the most recently modified.
To reverse the order, use the [`-r`](#ls) or [`--reverse`](#ls) flag:

```bash
❯ nb ls
home
----
[2] Todos
[3] Example Title
[1] Ideas

❯ nb ls --reverse
[1] Ideas
[3] Example Title
[2] Todos
```

Notes can be sorted with the [`-s`](#ls) / [`--sort`](#ls) flag,
which can be combined with [`-r`](#ls) / [`--reverse`](#ls):

```bash
❯ nb ls
home
----
[2] Sample Title
[3] Example Title
[1] Demo Title

❯ nb ls --sort
[1] Demo Title
[2] Sample Title
[3] Example Title

❯ nb ls --sort --reverse
[3] Example Title
[2] Sample Title
[1] Demo Title
```

`nb` with no subcommand behaves like an alias for [`nb ls`](#ls),
so the examples above can be run without the `ls`:

```bash
❯ nb
home
----
[2] Sample Title
[3] Example Title
[1] Demo Title

❯ nb example
[3] Example Title

❯ nb 3 --excerpt
[3] Example Title
-----------------
# Example Title

This is an example excerpt.

❯ nb 3 -e 8
[3] Example Title
-----------------
# Example Title

This is an example excerpt.

More example content:
- one
- two
- three

❯ nb --sort
[1] Demo Title
[2] Sample Title
[3] Example Title

❯ nb --sort --reverse
[3] Example Title
[2] Sample Title
[1] Demo Title
```

Short options can be combined for brevity:

```bash
# equivalent to `nb --sort --reverse --excerpt 2` and `nb -s -r -e 2`:
❯ nb -sre 2
[3] Example Title
-----------------
# Example Title

[2] Sample Title
----------------
Sample Title
============
[1] Demo Title
--------------
---
title: Demo Title
```

`nb` and [`nb ls`](#ls) display the 15 most recently modified items.
The default limit can be changed with [`nb set limit <number>`](#limit).
To list a different number of items on a per-command basis, use the
[`-n <limit>`](#ls),
[`--limit <limit>`](#ls),
[`--<limit>`](#ls),
[`-a`](#ls),
and [`--all`](#ls)
flags:

```bash
❯ nb -n 1
home
----
[5] Example Five
4 omitted. 5 total.

❯ nb --limit 2
home
----
[5] Example Five
[4] Example Four
3 omitted. 5 total.

❯ nb --3
home
----
[5] Example Five
[4] Example Four
[3] Example Three
2 omitted. 5 total.

❯ nb --all
home
----
[5] Example Five
[4] Example Four
[3] Example Three
[2] Example Two
[1] Example One
```

Lists can be paginated with
[`-p <number>`](#ls) / [`--page <number>`](#ls),
which paginates by the value of [`nb set limit`](#limit) by
default, or the value of
[`-n <limit>`](#ls),
[`--limit <limit>`](#ls),
or [`--<limit>`](#ls)
when present:

```bash
❯ nb
home
----
[6] Example Six
[5] Example Five
[4] Example Four
[3] Example Three
[2] Example Two
[1] Example One

❯ nb set limit 3
NB_LIMIT set to 3

❯ nb --page 1
[6] Example Six
[5] Example Five
[4] Example Four

❯ nb -p 2
[3] Example Three
[2] Example Two
[1] Example One

❯ nb -p 2 --limit 2
[4] Example Four
[3] Example Three

❯ nb -p 3 --2
[2] Example Two
[1] Example One
```

[`nb ls`](#ls) is a combination of
[`nb notebooks`](#notebooks) and [`nb list`](#list)
in one view and accepts the same arguments as [`nb list`](#list),
which lists only notes without the notebook list and with no limit by default:

```bash
❯ nb list
[100] Example One Hundred
[99]  Example Ninety-Nine
[98]  Example Ninety-Eight
... lists all notes ...
[2]   Example Two
[1]   Example One
```

For more information about options for listing notes, run
[`nb help ls`](#ls)
and
[`nb help list`](#list).

##### Listing with `browse`

Items can be listed within terminal and GUI web browsers using
[`nb browse`](#browse) / [`nb b`](#browse):

```bash
❯ nb browse example:sample/demo/
❯nb · example : sample / demo / +

search: [                    ]

[example:sample/demo/7] Title Seven
[example:sample/demo/6] Title Six
[example:sample/demo/5] Title Five
[example:sample/demo/4] Title Four
[example:sample/demo/3] Title Three

next ❯
```

For more information, see [Browsing](#-browsing).

#### Editing

<p>
  <sup>
    <a href="#overview">↑</a> ·
    <a href="#edit"><code>nb edit</code></a>,
    <a href="#browse"><code>nb browse edit</code></a>
  </sup>
</p>

You can edit an item in your editor with
[`nb edit`](#edit) (shortcut: [`nb e`](#edit)):

```bash
# edit note by id
nb edit 3

# edit note by filename
nb edit example.md

# edit note by title
nb edit "A Document Title"

# edit note 12 in the notebook named "example"
nb edit example:12

# edit note 12 in the notebook named "example", alternative
nb example:12 edit

# edit note 12 in the notebook named "example", alternative
nb example:edit 12
```

[`edit`](#edit) and other subcommands that take an identifier
can be called with the identifier and subcommand name reversed:

```bash
# edit note by id
nb 3 edit
```

[`nb edit`](#edit) can also receive piped content, which it
appends to the specified note without opening the editor:

```bash
echo "Content to append." | nb edit 1
```

Content can be passed with the [`--content <content>`](#edit) option,
which also appends the content without opening the editor:

```bash
nb edit 1 --content "Content to append."
```

Use the [`--overwrite`](#edit) option to overwrite existing file content
and the [`--prepend`](#edit) option to prepend the new content before existing content.

When content is piped or specified with [`--content <content>`](#edit),
use the [`--edit`](#edit) flag to open the file in the editor
before the change is committed.

##### Editing Encrypted Notes

When a note is encrypted,
[`nb edit`](#edit) prompts you for the note password,
opens the unencrypted content in your editor,
and then automatically reencrypts the note when you are done editing.

##### Shortcut Alias: `nb e`

[`nb edit`](#edit) can be called by the shortcut alias, [`nb e`](#edit):

```bash
# edit note by id
nb e 3

# edit note by filename
nb e example.md

# edit note by title
nb e "A Document Title"

# edit note by id, alternative
nb 3 e

# edit note 12 in the notebook named "example"
nb e example:12

# edit note 12 in the notebook named "example", alternative
nb example:12 e

# edit note 12 in the notebook named "example", alternative
nb example:e 12
```

For [`nb edit`](#edit) help information, run [`nb help edit`](#edit).

##### Editing with `browse`

Items can be edited within terminal and GUI web browsers using
[`nb browse edit`](#browse) / [`nb b e`](#browse):

```bash
❯ nb browse edit text:formats/markdown/123
❯nb · text : formats / markdown / 123 · ↓ · editing · - | +

[# Daring Fireball: Markdown (daringfireball.net)         ]
[                                                         ]
[<https://daringfireball.net/projects/markdown/>          ]
[                                                         ]
[## Related                                               ]
[                                                         ]
[- <https://en.wikipedia.org/wiki/Markdown>               ]
[                                                         ]
[## Comments                                              ]
[                                                         ]
[See also:                                                ]
[                                                         ]
[- [[text:formats/org]]                                   ]
[- [[cli:apps/nb]]                                        ]
[                                                         ]
[## Tags                                                  ]
[                                                         ]

[save] · last: 2021-01-01 01:00:00
```

For more information, see
[`browse edit`](#browse-edit) and [Browsing](#-browsing).

#### Viewing

<p>
  <sup>
    <a href="#overview">↑</a> ·
    <a href="#show"><code>nb show</code></a>,
    <a href="#browse"><code>nb browse</code></a>,
    <a href="#open"><code>nb open</code></a>,
    <a href="#peek"><code>nb peek</code></a>
  </sup>
</p>

Notes and other items can be viewed using
[`nb show`](#show) (shortcut: [`nb s`](#show)):

```bash
# show note by id
nb show 3

# show note by filename
nb show example.md

# show note by title
nb show "A Document Title"

# show note by id, alternative
nb 3 show

# show note 12 in the notebook named "example"
nb show example:12

# show note 12 in the notebook named "example", alternative
nb example:12 show

# show note 12 in the notebook named "example", alternative
nb example:show 12
```

By default, [`nb show`](#show) opens notes in
[`less`](https://linux.die.net/man/1/less),
with syntax highlighting if
[`bat`](https://github.com/sharkdp/bat),
[`highlight`](http://www.andre-simon.de/doku/highlight/en/highlight.php),
or
[Pygments](https://pygments.org/)
is installed.
You can navigate in `less` using the following keys:

```text
Key               Function
---               --------
mouse scroll      Scroll up or down
arrow up or down  Scroll one line up or down
f                 Jump forward one window
b                 Jump back one window
d                 Jump down one half window
u                 Jump up one half window
/<query>          Search for <query>
n                 Jump to next <query> match
q                 Quit
```

*If `less` scrolling isn't working in [iTerm2](https://www.iterm2.com/),
go to*
"Settings"
-> "Advanced"
-> "Scroll wheel sends arrow keys when in alternate screen mode"
*and change it to* "Yes".
*[More Info](https://stackoverflow.com/a/37610820)*

Use the [`-p`](#show) / [`--print`](#show) option
to print to standard output with syntax highlighting:

```bash
❯ nb show 123 --print
# Example Title

Example content:

- one
- two
- three
```

Use [`nb show --print --no-color`](#show) to print without syntax highlighting.

When [Pandoc](https://pandoc.org/) is available,
use the [`-r`](#show) / [`--render`](#show) option to
render the note to HTML and open it in your terminal browser:

```bash
nb show example.md --render
# opens example.md as an HTML page in w3m, links, or lynx
```

[`nb show`](#show) also supports previewing other file types in the terminal,
depending on the tools available in the environment.
Supported file types and tools include:

- PDF files:
  - [`termpdf.py`](https://github.com/dsanson/termpdf.py)
    with [kitty](https://sw.kovidgoyal.net/kitty/)
  - [`pdftotext`](https://en.wikipedia.org/wiki/Pdftotext)
- Audio files:
  - [`mplayer`](https://en.wikipedia.org/wiki/MPlayer)
  - [`afplay`](https://ss64.com/osx/afplay.html)
  - [`mpg123`](https://en.wikipedia.org/wiki/Mpg123)
  - [`ffplay`](https://ffmpeg.org/ffplay.html)
- [Images](#-images):
  - [ImageMagick](https://imagemagick.org/) with a terminal that
    supports [sixels](https://en.wikipedia.org/wiki/Sixel)
  - [`imgcat`](https://www.iterm2.com/documentation-images.html) with
    [iTerm2](https://www.iterm2.com/)
  - [kitty's `icat` kitten](https://sw.kovidgoyal.net/kitty/kittens/icat.html)
  - [`catimg`](https://github.com/posva/catimg)
- Folders / Directories:
  - [`ranger`](https://ranger.github.io/)
  - [Midnight Commander (`mc`)](https://en.wikipedia.org/wiki/Midnight_Commander)
- Word Documents:
  - [Pandoc](https://pandoc.org/) with
    [`w3m`](https://en.wikipedia.org/wiki/W3m) or
    [`links`](https://en.wikipedia.org/wiki/Links_(web_browser))
- EPUB ebooks:
  - [Pandoc](https://pandoc.org/) with
    [`w3m`](https://en.wikipedia.org/wiki/W3m) or
    [`links`](https://en.wikipedia.org/wiki/Links_(web_browser))

When using [`nb show`](#show) with other file types or
if the above tools are not available,
[`nb show`](#show) opens files in
your system's preferred application for each type.

[`nb show`](#show) also provides [options](#show) for
querying information about an item. For example, use the
[`--added`](#show) / [`-a`](#show) and [`--updated`](#show) / [`-u`](#show)
flags to print the date and time that an item was added or updated:

```bash
❯ nb show 2 --added
2020-01-01 01:01:00 -0700

❯ nb show 2 --updated
2020-02-02 02:02:00 -0700
```

[`nb show`](#show) is primarily intended for viewing items within the terminal.
To view a file in the system's preferred GUI application, use
[`nb open`](#open).
To [browse](#-browsing) rendered items in terminal and GUI web browsers, use
[`nb browse`](#browse).

For full [`nb show`](#show) usage information, run [`nb help show`](#show).

##### Shortcut Alias: `nb s`

[`nb show`](#show) can be called using the shortcut alias [`nb s`](#show):

```bash
# show note by id
nb s 3

# show note by filename
nb s example.md

# show note by title
nb s "A Document Title"

# show note by id, alternative
nb 3 s

# show note 12 in the notebook named "example"
nb s example:12

# show note 12 in the notebook named "example", alternative
nb example:12 s

# show note 12 in the notebook named "example", alternative
nb example:s 12
```

##### Alias: `nb view`

[`nb show`](#show) can also be invoked with [`nb view`](#show) for convenience:

```bash
# show note by id
nb view 3

# show note by filename
nb view example.md

# show note by title
nb view "A Document Title"

# show note by id, alternative
nb 3 view
```

##### Viewing with `browse`

Items can be viewed within terminal and GUI web browsers using
[`nb browse`](#browse) / [`nb b`](#browse):

```bash
❯ nb browse text:formats/markdown/123
❯nb · text : formats / markdown / 123 · ↓ · edit | +
Daring Fireball: Markdown (daringfireball.net)

https://daringfireball.net/projects/markdown/

Related

  • https://en.wikipedia.org/wiki/Markdown

Comments

See also:

  • [[text:formats/org]]
  • [[cli:apps/nb]]

Tags

#markup #plain-text

Content

Daring Fireball: Markdown

Download

Markdown 1.0.1 (18 KB) — 17 Dec 2004

Introduction

Markdown is a text-to-HTML conversion tool for web writers. Markdown allows
you to write using an easy-to-read, easy-to-write plain text format, then
convert it to structurally valid XHTML (or HTML).
```

For more information, see [Browsing](#-browsing).

#### Deleting

<p>
  <sup>
    <a href="#overview">↑</a> ·
    <a href="#delete"><code>nb delete</code></a>,
    <a href="#browse"><code>nb browse delete</code></a>
  </sup>
</p>

To delete one or more notes, pass any number of
ids, filenames, titles, and other [selectors](#-selectors)
to [`nb delete`](#delete) (shortcuts: [`nb d`](#delete), [`nb -`](#delete)):

```bash
# delete item by id
nb delete 3

# delete item by filename
nb delete example.md

# delete item by title
nb delete "A Document Title"

# delete item by id, alternative
nb 3 delete

# delete item 12 in the notebook named "example"
nb delete example:12

# delete item 12 in the notebook named "example", alternative
nb example:12 delete

# delete item 12 in the notebook named "example", alternative
nb example:delete 12

# delete item 345 in the folder named "example"
nb delete example/345

# delete items with the ids 89, 56, and 21
nb delete 89 56 21
```

By default, [`nb delete`](#delete) will display a confirmation prompt.
To skip, use the [`--force`](#delete) / [`-f`](#delete) option:

```bash
nb delete 3 --force
```

##### Shortcut Aliases: `nb d`, `nb -`

[`nb delete`](#delete) has the aliases [`nb d`](#delete) and [`nb -`](#delete):

```bash
# delete note by id
nb d 3

# delete note by filename
nb d example.md

# delete note by title
nb - "A Document Title"

# delete note by id, alternative
nb 3 d

# delete note 12 in the notebook named "example"
nb - example:12

# delete note 12 in the notebook named "example", alternative
nb example:12 d

# delete note 12 in the notebook named "example", alternative
nb example:d 12
```

For [`nb delete`](#delete) help information, run [`nb help delete`](#delete).

##### Deleting with `nb browse`

Items can be deleted within terminal and GUI web browsers using
[`nb browse delete`](#browse) / [`nb b d`](#browse):

```bash
❯ nb browse delete example:4
❯nb · example : 4 · ↓ · edit · - | +

              deleting

[4] example_file.md "Example Title"

              [delete]
 
```

For more information, see [Browsing](#-browsing).

### 🔖 Bookmarks

<p>
  <sup>
    <a href="#overview">↑</a> ·
    <a href="#nb-help"><code>nb&nbsp;&lt;url&gt;</code></a>,
    <a href="#browse"><code>nb&nbsp;browse</code></a>,
    <a href="#bookmark"><code>nb&nbsp;bookmark</code></a>,
    <a href="#open"><code>nb&nbsp;open</code></a>,
    <a href="#peek"><code>nb&nbsp;peek</code></a>,
    <a href="#show"><code>nb&nbsp;show</code></a>
  </sup>
</p>

`nb` includes a bookmarking system to conveniently
create, annotate, view, search, [browse](#-browsing), and manage
collections of bookmarks.

<p align="center">
  <img  src="https://xwmx.github.io/misc/nb/images/nb-bookmarks-gui-gui-terminal.png"
        alt="nb bookmarks"
        width="450">
</p>

Bookmarks in `nb` are stored as
[simple structured Markdown files](#nb-markdown-bookmark-file-format)
containing information extracted from the bookmarked pages.

To create a new bookmark, pass a URL as the first argument to `nb`:

```bash
nb https://example.com
```

`nb` automatically generates a bookmark using information from the page:

```markdown
# Example Title (example.com)

<https://example.com>

## Description

Example description.

## Content

Example Title
=============

This domain is for use in illustrative examples in documents. You may
use this domain in literature without prior coordination or asking for
permission.

[More information\...](https://www.iana.org/domains/example)
```

`nb` embeds the page content in the bookmark, making it available for
[full text search](#-search) with [`nb search`](#search) and
locally-served, distraction-free [reading and browsing](#-browsing)
with [`nb browse`](#browse).
When [Pandoc](https://pandoc.org/) is installed,
the HTML page content is converted to Markdown.
When [readability-cli](https://gitlab.com/gardenappl/readability-cli)
is installed, markup is cleaned up to focus on content.

In addition to caching the page content,
you can also include a quote from the page in a
[`## Quote`](#-quote) section
using the
[`-q <quote>`](#bookmark) / [`--quote <quote>`](#bookmark) option:

```bash
nb https://example.com --quote "Example quote line one.

Example quote line two."
```
```markdown
# Example Title (example.com)

<https://example.com>

## Description

Example description.

## Quote

> Example quote line one.
>
> Example quote line two.

## Content

Example Title
=============

This domain is for use in illustrative examples in documents. You may
use this domain in literature without prior coordination or asking for
permission.

[More information\...](https://www.iana.org/domains/example)
```

Add a comment in a [`## Comment`](#-comment) section using the
[`-c <comment>`](#bookmark) / [`--comment <comment>`](#bookmark) option:

```bash
nb https://example.com --comment "Example comment."
```
```markdown
# Example Title (example.com)

<https://example.com>

## Description

Example description.

## Comment

Example comment.

## Content

Example Title
=============

This domain is for use in illustrative examples in documents. You may
use this domain in literature without prior coordination or asking for
permission.

[More information\...](https://www.iana.org/domains/example)
```

Add related URLs and [linked](#-linking) [selectors](#-selectors)
to a [`## Related`](#-related) section using the
[`-r (<url> | <selector>)`](#bookmark) /
[`--related (<url> | <selector>)`](#bookmark)
option:

```bash
nb https://example.com --related example:123 -r https://example.com
```
```markdown
# Example Title (example.com)

<https://example.com>

## Description

Example description.

## Related

- [[sample:123]]
- <https://example.net>

## Content

Example Title
=============

This domain is for use in illustrative examples in documents. You may
use this domain in literature without prior coordination or asking for
permission.

[More information\...](https://www.iana.org/domains/example)
```

Bookmarks can be tagged using the
[`-t <tag1>,<tag2>...`](#bookmark) /
[`--tags <tag1>,<tag2>...`](#bookmark) option.
Tags are converted into [#hashtags](#-tagging) and
added to a [`## Tags`](#-tags) section:

```bash
nb https://example.com --tags tag1,tag2
```
```markdown
# Example Title (example.com)

<https://example.com>

## Description

Example description.

## Tags

#tag1 #tag2

## Content

Example Title
=============

This domain is for use in illustrative examples in documents. You may
use this domain in literature without prior coordination or asking for
permission.

[More information\...](https://www.iana.org/domains/example)
```

[Search](#-search) for tagged bookmarks with
[`nb search`](#search) / [`nb q`](#search):

```bash
nb search --tag tag1

nb q -t tag1

nb q \#tag1
```

[`nb search`](#search) / [`nb q`](#search)
automatically searches archived page content:

```bash
❯ nb q "example query"
[10] 🔖 example.bookmark.md "Example Bookmark (example.com)"
------------------------------------------------------------
5:Lorem ipsum example query.
```

Bookmarks can also be encrypted:

```bash
# create a new password-protected, encrypted bookmark
nb https://example.com --encrypt
```

Encrypted bookmarks require a password before they can be viewed or
opened.

#### Listing and Filtering Bookmarks

<p align="center">
  <img  src="https://xwmx.github.io/misc/nb/images/nb-bookmarks-gui-terminal-terminal.png"
        alt="nb bookmark lists"
        width="500">
</p>

Bookmarks are included in
`nb`,
[`nb ls`](#ls),
[`nb list`](#list),
and [`nb browse`](#browse)
along with items of other types.
[`nb bookmark`](#bookmark) and [`nb bookmark list`](#bookmark) can be used to
list and filter only bookmarks:

```bash
❯ nb bookmark
Add: nb <url> Help: nb help bookmark
------------------------------------
[3] 🔖 🔒 example.bookmark.md.enc
[2] 🔖 Bookmark Two (example.com)
[1] 🔖 Bookmark One (example.com)

❯ nb bookmark list two
[2] 🔖 Bookmark Two (example.com)
```

Bookmarks are also included in `nb`, [`nb ls`](#ls), and [`nb list`](#list):

```bash
❯ nb
home
----
[7] 🔖 Bookmark Three (example.com)
[6] Example Note
[5] 🔖 Bookmark Two (example.net)
[4] Sample Note
[3] 🔖 🔒 example-encrypted.bookmark.md.enc
[2] Demo Note
[1] 🔖 Bookmark One (example.com)
```

Use the [`--type <type>`](#ls) / [`--<type>`](#ls)
option as a filter to display only bookmarks:

```bash
❯ nb --type bookmark
[7] 🔖 Bookmark Three (example.com)
[5] 🔖 Bookmark Two (example.net)
[3] 🔖 🔒 example-encrypted.bookmark.md.enc
[1] 🔖 Bookmark One (example.com)

❯ nb --bookmark
[7] 🔖 Bookmark Three (example.com)
[5] 🔖 Bookmark Two (example.net)
[3] 🔖 🔒 example-encrypted.bookmark.md.enc
[1] 🔖 Bookmark One (example.com)
```

`nb` saves the domain in the title, making it easy to filter by domain
using any list subcommands:

```bash
❯ nb example.com
[7] 🔖 Bookmark Three (example.com)
[1] 🔖 Bookmark One (example.com)
```

For more listing options, see
[`nb help ls`](#ls),
[`nb help list`](#list),
and [`nb help bookmark`](#bookmark).

##### Shortcut Aliases: `nb bk`, `nb bm`

[`nb bookmark`](#bookmark) can also be used with the aliases
[`nb bk`](#bookmark) and [`nb bm`](#bookmark):

```bash
❯ nb bk
Add: nb <url> Help: nb help bookmark
------------------------------------
[7] 🔖 Bookmark Three (example.com)
[5] 🔖 Bookmark Two (example.net)
[3] 🔖 🔒 example-encrypted.bookmark.md.enc
[1] 🔖 Bookmark One (example.com)

❯ nb bm example.net
[5] 🔖 Bookmark Two (example.net)
```

#### Viewing Bookmarks

<p>
  <sup>
    <a href="#overview">↑</a> ·
    <a href="#browse"><code>nb&nbsp;browse</code></a>,
    <a href="#open"><code>nb&nbsp;open</code></a>,
    <a href="#peek"><code>nb&nbsp;peek</code></a>,
    <a href="#show"><code>nb&nbsp;show</code></a>
  </sup>
</p>

`nb` provides multiple ways to view bookmark files, bookmarked content,
and bookmarked URLs.

Use [`nb browse`](#browse) (shortcut: [`nb b`](#browse))
to [browse](#-browsing) bookmarks with cached content,
<a href="#-linking">[[wiki-style links]]</a>,
linked [#tags](#-tagging), and external links:

```bash
❯ nb browse text:formats/markdown/123
❯nb · text : formats / markdown / 123 · ↓ · edit | +
Daring Fireball: Markdown (daringfireball.net)

https://daringfireball.net/projects/markdown/

Related

  • https://en.wikipedia.org/wiki/Markdown

Comments

See also:

  • [[text:formats/org]]
  • [[cli:apps/nb]]

Tags

#markup #plain-text

Content

Daring Fireball: Markdown

Download

Markdown 1.0.1 (18 KB) — 17 Dec 2004

Introduction

Markdown is a text-to-HTML conversion tool for web writers. Markdown allows
you to write using an easy-to-read, easy-to-write plain text format, then
convert it to structurally valid XHTML (or HTML).
```

For more information, see [Browsing](#-browsing).

[`nb open`](#open) (shortcut: [`nb o`](#open)) opens the bookmarked URL in
your system's primary web browser:

```bash
# open bookmark by id
nb open 3

# open bookmark 12 in the notebook named "example"
nb open example:12

# open bookmark 12 in the notebook named "example", alternative
nb example:12 open

# open bookmark 12 in the notebook named "example", alternative
nb example:open 12
```

*N.B. To use [`nb open`](#open) with
[WSL](https://docs.microsoft.com/en-us/windows/wsl/install),
install [wslu](https://github.com/wslutilities/wslu).*

[`nb peek`](#peek) (shortcut: [`nb p`](#peek), alias: [`nb preview`](#peek))
opens the bookmarked URL in your terminal web browser,
such as
[w3m](https://en.wikipedia.org/wiki/W3m),
[Links](https://en.wikipedia.org/wiki/Links_(web_browser)), or
[Lynx](https://en.wikipedia.org/wiki/Lynx_(web_browser)):

```bash
# peek bookmark by id
nb peek 3

# peek bookmark 12 in the notebook named "example"
nb peek example:12

# peek bookmark 12 in the notebook named "example", alternative
nb example:12 peek

# peek bookmark 12 in the notebook named "example", alternative
nb example:peek 12
```

[`nb open`](#open) and [`nb peek`](#peek)
work seamlessly with encrypted bookmarks.
`nb` simply prompts you for the bookmark's password.

[`nb open`](#open) and [`nb peek`](#peek)
automatically check whether the URL is still valid.
If the page has been removed, `nb` can check
the [Internet Archive Wayback Machine](https://archive.org/web/)
for an archived copy.

The preferred terminal web browser can be set using
the `$BROWSER` environment variable,
assigned in `~/.bashrc`, `~/.zshrc`, or similar:

```bash
export BROWSER=lynx
```

When `$BROWSER` is not set, `nb` looks for
[`w3m`](https://en.wikipedia.org/wiki/W3m),
[`links`](https://en.wikipedia.org/wiki/Links_(web_browser)), and
[`lynx`](https://en.wikipedia.org/wiki/Lynx_(web_browser))
and uses the first one it finds.

`$BROWSER` can also be used to easy specify the terminal browser for
an individual command:

```bash
❯ BROWSER=links nb 12 peek
# opens the URL from bookmark 12 in links

❯ BROWSER=w3m nb 12 peek
# opens the URL from bookmark 12 in w3m
```

[`nb show`](#show) and [`nb edit`](#edit)
can also be used to view and edit bookmark files,
which include the cached page converted to Markdown.

[`nb show <id> --render`](#show) / [`nb show <id> -r`](#show)
displays the bookmark file converted to HTML in the terminal web browser,
including all bookmark fields and the cached page content,
providing a cleaned-up, distraction-free, locally-served view of
the page content along with all of your notes.

##### Shortcut Aliases: `nb o` and `nb p`

[`nb open`](#open) and [`nb peek`](#peek)
can also be used with the shortcut aliases
[`nb o`](#open) and [`nb p`](#peek):

```bash
# open bookmark by id
nb o 3

# open bookmark 12 in the notebook named "example"
nb o example:12

# open bookmark 12 in the notebook named "example", alternative
nb example:12 o

# peek bookmark by id
nb p 3

# peek bookmark 12 in the notebook named "example"
nb p example:12

# peek bookmark 12 in the notebook named "example", alternative
nb example:12 p
```

#### Bookmark File Format

Bookmarks are identified by a `.bookmark.md` file extension.
The bookmark URL is the first URL in the file within `<` and `>` characters.
To create a minimally valid bookmark file with [`nb add`](#add):

```bash
nb add example.bookmark.md --content "<https://example.com>"
```

For a full overview, see
[`nb` Markdown Bookmark File Format](#nb-markdown-bookmark-file-format).

#### `bookmark` -- A command line tool for managing bookmarks.

`nb` includes [`bookmark`](#bookmark-help), a full-featured
command line interface for creating, viewing, searching, and editing bookmarks.

[`bookmark`](#bookmark-help) is a shortcut for the
[`nb bookmark`](#bookmark) subcommand,
accepting all of the same subcommands and options with identical behavior.

Bookmark a page:

```bash
❯ bookmark https://example.com --tags tag1,tag2
Added: [3] 🔖 20200101000000.bookmark.md "Example Title (example.com)"
```
List and filter bookmarks with
[`bookmark`](#bookmark) and [`bookmark list`](#bookmark):

```bash
❯ bookmark
Add: bookmark <url> Help: bookmark help
---------------------------------------
[3] 🔖 🔒 example.bookmark.md.enc
[2] 🔖 Example Two (example.com)
[1] 🔖 Example One (example.com)

❯ bookmark list two
[2] 🔖 Example Two (example.com)
```

View a bookmark in your terminal web browser:

```bash
bookmark peek 2
```

Open a bookmark in your system's primary web browser:

```bash
bookmark open 2
```

Perform a full text search of bookmarks and archived page content:

```bash
❯ bookmark search "example query"
[10] 🔖 example.bookmark.md "Example Bookmark (example.com)"
------------------------------------------------------------
5:Lorem ipsum example query.
```

See [`bookmark help`](#bookmark-help) for more information.

### ✅ Todos

<p>
  <sup>
    <a href="#overview">↑</a> ·
    <a href="#do"><code>nb do</code></a>,
    <a href="#tasks"><code>nb tasks</code></a>,
    <a href="#todo"><code>nb todo</code></a>,
    <a href="#undo"><code>nb undo</code></a>
  </sup>
</p>

Use [`nb todo`](#todo) (shortcut: [`nb t`](#todo))
to create, list, and update todos.
`nb` todos are [structured Markdown documents](#nb-markdown-todo-file-format)
referencing a single primary todo,
with optional [tasks](#%EF%B8%8F-tasks).

Use [`nb todo add`](#todo) to create a new todo:

```bash
# create a new todo titled "Example todo one."
❯ nb todo add "Example todo one."
Added: [1] ✔️ [ ] Example todo one.

❯ nb show 1 --print
# [ ] Example todo one.
```

Use the [`--due <date>`](#todo) option to add an optional due date in a
[`## Due`](#-due) section:

```bash
# create a new todo titled "Example todo two." with a due date of "2100-01-01"
❯ nb todo add "Example todo two." --due "2100-01-01"
Added: [2] ✔️ [ ] Example todo two.

❯ nb show 2 --print
# [ ] Example todo two.

## Due

2100-01-01
```

Add an optional [description](#-description-1) with the
[`--description <description>`](#todo)
option:

```bash
❯ nb todo add "Example todo three." --description "Example description."
Added: [3] ✔️ [ ] Example todo three.

❯ nb show 3 --print
# [ ] Example todo three.

## Description

Example description.
```

Todos can have [tasks](#%EF%B8%8F-tasks).
Tasks added with one or more [`--task <task>`](#todo) options
are represented as a markdown task list and placed in a
[`## Tasks`](#-tasks) section:

```bash
❯ nb todo add "Example todo seven." --task "Task one." --task "Task two." --task "Task three."
Added: [7] ✔️ [ ] Example todo seven.

❯ nb show 7 --print
# [ ] Example todo seven.

## Tasks

- [ ] Task one.
- [ ] Task two.
- [ ] Task three.
```

Related URLs and [linked](#-linking) [selectors](#-selectors)
can be added to a [`## Related`](#-related-1) field using the
[`-r (<url> | <selector>)`](#todo) / [`--related (<url> | <selector>)`](#todo)
option:

```bash
❯ nb todo add "Example todo four." --related example:123 -r https://example.com
Added: [4] ✔️ [ ] Example todo four.

❯ nb show 4 --print
# [ ] Example todo four.

## Related

- [[example:123]]
- <https://example.com>
```

[Tags](#-tagging) can be added to todos with the
[`--tags <tag1>,<tag2>...`](#todo) option:

```bash
❯ nb todo add "Example todo five." --tags tag1,tag2
Added: [5] ✔️ [ ] Example todo five.

❯ nb show 5 --print
# [ ] Example todo five.

## Tags

#tag1 #tag2
```

[Tags](#-tagging), [links](#-linking), and URLs can be
[browsed](#-browsing)
in terminal and GUI web browers with [`nb browse`](#browse).

#### Listing Todos

List todos in with [`nb todos`](#todo):

```bash
# list todos in the current notebook
❯ nb todos
[6] ✔️ [ ] Example todo six.
[5] ✅ [x] Example todo five.
[4] ✔️ [ ] Example todo four.
[3] ✅ [x] Example todo three.
[2] ✅ [x] Example todo two.
[1] ✔️ [ ] Example todo one.

# list todos in the notebook named "sample"
❯ nb todos sample:
[sample:4] ✅ [x] Sample todo four.
[sample:3] ✔️ [ ] Sample todo three.
[sample:2] ✔️ [ ] Sample todo two.
[sample:1] ✅ [x] Sample todo one.

```

Open / undone todos can be listed with [`nb todos open`](#todo):

```bash
# list open todos in the current notebook
❯ nb todos open
[6] ✔️ [ ] Example todo six.
[4] ✔️ [ ] Example todo four.
[1] ✔️ [ ] Example todo one.

# list open todos in the notebook named "sample"
❯ nb tasks open sample:
[sample:3] ✔️ [ ] Sample todo three.
[sample:2] ✔️ [ ] Sample todo two.
```

Closed / done todos can be listed with [`nb todos closed`](#todo):

```bash
# list closed todos in the current notebook
❯ nb todos closed
[5] ✅ [x] Example todo five.
[3] ✅ [x] Example todo three.
[2] ✅ [x] Example todo two.

# list closed todos in the notebook named "sample"
❯ nb tasks closed sample:
[sample:4] ✅ [x] Sample todo four.
[sample:1] ✅ [x] Sample todo one.
```

See
[`nb help todo`](#todo)
for more information.

#### `do` / `undo`

Mark a todo as done or closed with [`nb do`](#do):

```bash
# add a new todo titled "Example todo six."
❯ nb todo add "Example todo six."
Added: [6] ✔️ [ ] Example todo six.

# mark todo 6 as done / closed
❯ nb do 6
Done: [6] ✅ [x] Example todo six.
```

Re-open a closed todo with [`nb undo`](#undo):

```bash
# mark todo 6 as undone / open
❯ nb undo 6
Undone: [6] ✔️ [ ] Example todo six.
```

See
[`nb help do`](#do)
and
[`nb help undo`](#undo)
for more information.

### ✔️ Tasks

<p>
  <sup>
    <a href="#overview">↑</a> ·
    <a href="#do"><code>nb do</code></a>,
    <a href="#tasks"><code>nb tasks</code></a>,
    <a href="#todo"><code>nb todo</code></a>,
    <a href="#undo"><code>nb undo</code></a>
  </sup>
</p>

`nb` can list and update tasks in [todos](#-todos) and other Markdown documents.

Tasks are defined as one or more Markdown list items starting with
`- [ ]` to indicate an open task or `- [x]` to indicate a done / closed task:

```markdown
- [ ] Example open task.
- [x] Example closed task.
```

List tasks in items, folders, and notebooks with
[`nb tasks`](#tasks) (shortcut: [`nb t`](#tasks)),
which lists both tasks and todos:

```bash
# list tasks in item 7
❯ nb tasks 7
[7] ✔️ [ ] Example todo seven.
------------------------------
[7 1] [x] Task one.
[7 2] [x] Task two.
[7 3] [ ] Task three.

# list tasks and todos in the notebook named "example"
❯ nb tasks example:
[example:9] ✔️ [ ] Example todo nine.
[example:8] ✅ [x] Example todo eight.
--------------------------------------
[example:8 1] [x] Task one.
[example:8 2] [x] Task two.

[example:6] ✔️ [ ] Example todo six.
[example:4] Example Note Title
------------------------------
[example:4 1] [ ] Task one.
[example:4 2] [x] Task two.
[example:4 3] [ ] Task three.

[example:3] ✔️ [ ] Example todo three.
```

Open / undone tasks can be listed with [`nb tasks open`](#tasks):

```bash
# list open tasks in item 7
❯ nb tasks open 7
[7] ✔️ [ ] Example todo seven.
------------------------------
[7 3] [ ] Task three.

# list open tasks and todos in the notebook named "example"
❯ nb tasks open example:
[example:9] ✔️ [ ] Example todo nine.
[example:6] ✔️ [ ] Example todo six.
[example:4] Example Note Title
------------------------------
[example:4 1] [ ] Task one.
[example:4 3] [ ] Task three.

[example:3] ✔️ [ ] Example todo three.
```

Closed / done tasks can be listed with [`nb tasks closed`](#tasks):

```bash
# list closed tasks in item 7
❯ nb tasks closed 7
[7] ✔️ [ ] Example todo seven.
------------------------------
[7 1] [x] Task one.
[7 2] [x] Task two.

# list closed tasks and todos in the notebook named "example"
❯ nb tasks closed example:
[example:8] ✅ [x] Example todo eight.
--------------------------------------
[example:8 1] [x] Task one.
[example:8 2] [x] Task two.

[example:4] Example Note Title
------------------------------
[example:4 2] [x] Task two.
```

Tasks are identified by the item [selector](#-selectors), followed by
a space, then followed by the sequential number of the task in the file.

Use [`nb do`](#do) to mark tasks as done / closed:

```bash
# list tasks in item 9
❯ nb tasks 9
[9] ✔️ [ ] Eample todo nine.
----------------------------
[9 1] [ ] Task one.
[9 2] [ ] Task two.
[9 3] [ ] Task three.

# mark task 2 in item 9 as done / closed
❯ nb do 9 2
[9] ✔️ [ ] Eample todo nine.
----------------------------
Done: [9 2] [x] Task two.

# list tasks in item 9
❯ nb tasks 9
[9] ✔️ [ ] Eample todo nine.
----------------------------
[9 1] [ ] Task one.
[9 2] [x] Task two.
[9 3] [ ] Task three.
```

Undo a done / closed task with [`nb undo`](#undo):

```bash
# mark task 2 in item 9 as undone / open
❯ nb undo 9 2
[9] ✔️ [ ] Example todo nine.
-----------------------------
Undone: [9 2] [ ] Task two.

# list tasks in item 9
❯ nb tasks 9
[9] ✔️ [ ] Example todo nine.
-----------------------------
[9 1] [ ] Task one.
[9 2] [ ] Task two.
[9 3] [ ] Task three.
```

See
[`nb help tasks`](#tasks)
for more information.

### 🏷 #tagging

<p>
  <sup>
    <a href="#overview">↑</a> ·
    <a href="#add"><code>nb add</code></a>,
    <a href="#bookmark"><code>nb bookmark</code></a>,
    <a href="#browse"><code>nb browse</code></a>,
    <a href="#list"><code>nb list</code></a>,
    <a href="#ls"><code>nb ls</code></a>,
    <a href="#search"><code>nb search</code></a>
  </sup>
</p>

`nb` recognizes `#hashtags` defined anywhere within a document.
A hashtag is defined in `nb` as a `#` character followed by any number of
letters, numbers, underscores, and dashes.

Notes and bookmarks can be tagged when they are created using the
`--tags <tag1>,<tag2>...` option,
which is available with
[`nb add`](#add),
[`nb <url>`](#nb-help),
[`nb browse add`](#browse),
[`nb bookmark`](#bookmark),
and
[`nb todo`](#todo).
`--tags` takes a comma-separated list of tags, converts them to
`#hashtags`,
and adds them to the document.

Tags added to notes with [`nb add --tags`](#add) are placed between the title
and body text:

```bash
❯ nb add --title "Example Title" "Example note content." --tags tag1,tag2
```

```markdown
# Example Title

#tag1 #tag2

Example note content.
```

Tags added to [bookmarks](#bookmarks) with
[`nb <url> --tags`](#nb-help) and [`nb bookmark <url> --tags`](#bookmark)
are placed in a [`## Tags`](#-tags) section:

```bash
❯ nb https://example.com --tags tag1,tag2
```

```markdown
# Example Title (example.com)

<https://example.com>

## Description

Example description.

## Tags

#tag1 #tag2

## Content

Example Title
=============

This domain is for use in illustrative examples in documents. You may
use this domain in literature without prior coordination or asking for
permission.

[More information\...](https://www.iana.org/domains/example)
```

Tags added to [todos](#-todos) with
[`nb todo add --tags`](#todo)
are placed in a [`## Tags`](#-tags-1) section:

```bash
❯ nb todo add --tags tag1,tag2 "Example todo."
```

```markdown
# [ ] Example todo.

## Tags

#tag1 #tag2
```

Use [`nb --tags`](#nb-help), [`nb ls --tags`](#ls),
and [`nb list --tags`](#list)
to list the tags present in a notebook, folder, or item:

```bash
# list all tags found in items in the current notebook
nb --tags

# list all tags found in the folder named "example"
nb example/ --tags

# list all tags in the item with id 123 in the notebook named "sample"
nb sample:123 --tags
```

Tagged items can be [searched](#-search) with
[`nb search`](#search) / [`nb q`](#search):

```bash
# search for items tagged with "#tag1"
nb search --tag tag1

# search for items tagged with "#tag1", shortcut and short option
nb q -t tag1

# search for items tagged with "#tag1", shortcut and argument
nb q \#tag1

# search for items tagged with "#tag1", shortcut and argument, alternative
nb q "#tag1"

# search for items tagged with "#tag1" AND "#tag2"
nb q --tag tag1 --tag tag2

# search for items tagged with "#tag1" AND "#tag2", short options
nb q -t tag1 -t tag2

# search for items tagged with "#tag1" AND "#tag2", arguments
nb q \#tag1 \#tag2

# search for items tagged with "#tag1" AND "#tag2", tag list
nb q --tags tag1,tag2

# search for items tagged with either "#tag1" OR "#tag2", options
nb q -t tag1 --or -t tag2

# search for items tagged with either "#tag1" OR "#tag2", arguments
nb q \#tag1 --or \#tag2

# search for items tagged with either "#tag1" OR "#tag2", single argument
nb q "#tag1|#tag2"

# search for items tagged with "#tag1" AND "#tag2" AND "#tag3"
nb q -t tag1 --tags tag2,tag3

# search for items tagged with "#tag1" OR "#tag2" OR "#tag3"
nb q -t tag1 --or --tags tag2,tag3

# search for items tagged with "#tag1" OR "#tag2" OR "#tag3"
nb q \#tag1 --or -t tag2 --or "#tag3"
```

Linked tags can be [browsed](#-browsing) with [`nb browse`](#browse),
providing another dimension of browsability in terminal and GUI web browsers,
complimenting <a href="#-linking">[[wiki-style linking]]</a>.

Tags in notes,
bookmarks,
files in text-based formats,
Word `.docx` documents,
and [Open Document](https://en.wikipedia.org/wiki/OpenDocument) `.odt` files
are rendered as links to the list of items in the notebook sharing that tag:

```bash
❯nb · example : 321

Example Title

#tag1 #tag2

Example content with link to [[Sample Title]].

More example content:
- one
- two
- three
```

Use the [`-t <tag>`](#browse) / [`--tag <tag>`](#browse) option
to open [`nb browse`](#browse) to the list of
all items in the current notebook or a specified notebook or folder that
share a tag:

```bash
# open to a list of items tagged with "#tag2" in the "example" notebook
❯ nb browse example: --tag tag2
❯nb · example

search: [#tag2               ]

[example:321] Example Title
[example:654] Sample Title
[example:789] Demo Title

# shortcut alias and short option
❯ nb b example: -t tag2
❯nb · example

search: [#tag2               ]

[example:321] Example Title
[example:654] Sample Title
[example:789] Demo Title
```

For more information about full-text search, see
[Search](#-search) and [`nb search`](#search).
For more information about browsing, see
[Browsing](#-browsing) and [`nb browse`](#browse).

### 🔗 Linking

<p>
  <sup>
    <a href="#overview">↑</a> ·
    <a href="#browse"><code>nb browse</code></a>
  </sup>
</p>

Notes,
bookmarks,
files in text-based formats,
Word `.docx` documents,
and [Open Document](https://en.wikipedia.org/wiki/OpenDocument) `.odt` files
can reference other items using
<a href="#-linking">[[wiki-style links]]</a>,
making `nb` a powerful terminal-first platform for
[Zettelkasten](#-zettelkasten),
wiki-style knowledge mapping,
and other link-based note-taking methods.

To add a link from a note or bookmark to another in the same notebook,
include the id, title, or relative path for the target item
within double square brackets anywhere in the linking document:

```bash
# link to the item with id 123 in the root level of current notebook
[[123]]

# link to the item titled "Example Title" in the root level of the current notebook
[[Example Title]]

# link to the item with id 456 in the folder named "Sample Folder"
[[Sample Folder/456]]

# link to the item titled "Demo Title" in the folder named "Sample Folder"
[[Sample Folder/Demo Title]]
```

To link to an item in another notebook,
add the notebook name with a colon before the identifier:

```bash
# link to the item with id 123 in the "sample" folder in the "example" notebook
[[example:sample/123]]

# link to the item titled "Example Title" in the "demo" notebook
[[demo:Example Title]]

# link to the item with filename "Example File.md" in the "sample" notebook
[[sample:Example File.md]]
```

The text for a link can be specified after a pipe `|` character:

```bash
# render link to item 123 in the "example" notebook as [[Example Link Text]]
[[example:123|Example Link Text]]
```

<a href="#-linking">[[wiki-style links]]</a> cooperate well with
[Org links](https://orgmode.org/guide/Hyperlinks.html),
which have a similar syntax,
providing a convenient option for linking collections of Org files.

Linked items can be [browsed](#-browsing) with [`nb browse`](#browse).

For more information about identifying items, see [Selectors](#-selectors).

### 🌍 Browsing

<p>
  <sup>
    <a href="#overview">↑</a> ·
    <a href="#browse"><code>nb browse</code></a>
  </sup>
</p>

Use [`nb browse`](#browse) (shortcut: [`nb b`](#browse)) to
browse, view, edit, and search linked notes, bookmarks, notebooks, folders,
and other items using terminal and GUI web browsers.

<p align="center">
  <img  src="https://xwmx.github.io/misc/nb/images/gui-gui-terminal-browse.png"
        alt="nb browse"
        width="500">
</p>

[`nb browse`](#browse) includes an embedded, terminal-first web application
that renders
<a href="#-linking">[[wiki-style links]]</a>
and
[#hashtags](#-tagging)
as internal links, enabling you to browse your notes and notebooks in web
browsers, including seamlessly browsing to and from the offsite links in
bookmarks and notes.

```bash
❯ nb browse
❯nb · home : +

search: [                    ]

[home:6]  📌 Example Markdown Title
[home:12] 🔒 example-encrypted.md.enc
[home:11] 🔖 Example Bookmark (example.com)
[home:10] 🔖 🔒 example-encrypted.bookmark.md.enc
[home:9]  Example .org Title
[home:8]  🌄 example-image.png
[home:7]  📄 example.pdf
[home:5]  🔉 example-audio.mp3
[home:4]  Example LaTeX Title
[home:3]  📹 example-video.mp4
[home:2]  example.md
[home:1]  📂 Example Folder
```

Lists are displayed using the same format as `nb` and [`nb ls`](#ls),
including [pinned](#-pinning) items, with each list item linked.
Lists are automatically paginated to fit the height of the terminal window.

```bash
❯ nb browse example:sample/demo/
❯nb · example : sample / demo / +

search: [                    ]

[example:sample/demo/7] Title Seven
[example:sample/demo/6] Title Six
[example:sample/demo/5] Title Five
[example:sample/demo/4] Title Four
[example:sample/demo/3] Title Three

next ❯
```

[`nb browse`](#browse) is designed to make it easy to navigate within
terminal web browsers using only keyboard commands,
while also supporting mouse interactions.
The [`nb browse`](#browse) interface includes links
to quickly jump to parent folders,
the current notebook,
and other notebooks.

[`nb browse`](#browse) opens in
[w3m](https://en.wikipedia.org/wiki/W3m),
[Links](https://en.wikipedia.org/wiki/Links_\(web_browser\)),
or in the browser set in the `$BROWSER` environment variable.
Use [`nb browse --gui`](#browse) / [`nb b -g`](#browse) to
open in the system's primary [GUI web browser](#browse---gui).

To open a specific item in [`nb browse`](#browse),
pass the [selector](#-selectors) for the item, folder, or notebook
to [`nb browse`](#browse):

```bash
# open the item with id 42 in the folder named "sample" in the "example" notebook
❯ nb browse example:sample/42
❯nb · example : sample / 42 · ↓ · edit | +

Example Title

#tag1 #tag2

Example content with link to [[Demo Title]].

More example content:

  • one
  • two
  • three
```

Items can also be browsed with
[`nb show --browse`](#show) / [`nb s -b`](#show),
which behaves identically.

[`nb browse`](#browse) is particularly useful for [bookmarks](#-bookmarks).
Cached content is rendered in the web browser along with comments and notes.
Internal and external links are easily accessible directly in the terminal,
providing a convenient, distraction-free approach for browsing collections
of bookmarks.

```bash
❯ nb browse text:formats/markdown/123
❯nb · text : formats / markdown / 123 · ↓ · edit | +
Daring Fireball: Markdown (daringfireball.net)

https://daringfireball.net/projects/markdown/

Related

  • https://en.wikipedia.org/wiki/Markdown

Comments

See also:

  • [[text:formats/org]]
  • [[cli:apps/nb]]

Tags

#markup #plain-text

Content

Daring Fireball: Markdown

Download

Markdown 1.0.1 (18 KB) — 17 Dec 2004

Introduction

Markdown is a text-to-HTML conversion tool for web writers. Markdown allows
you to write using an easy-to-read, easy-to-write plain text format, then
convert it to structurally valid XHTML (or HTML).
```

Notes, bookmarks, files in text-based formats, source code,
Word `.docx` documents, and
[Open Document](https://en.wikipedia.org/wiki/OpenDocument) `.odt`
files are converted into HTML and rendered in the browser. Use the down
arrow (`↓`) link to view or download the original file.

#### `browse edit`

<p align="center">
  <img  src="https://xwmx.github.io/misc/nb/images/gui-terminal-browse-edit.png"
        alt="nb browse edit"
        width="500">
</p>

Items in text formats can be edited within terminal and GUI web browsers using
the `edit` link on the item page or by opening the item with
[`nb browse edit`](#browse) / [`nb b e`](#browse),
which automatically resizes the form to fit the current terminal window:

```bash
❯ nb browse edit text:formats/markdown/123
❯nb · text : formats / markdown / 123 · ↓ · editing · - | +

[# Daring Fireball: Markdown (daringfireball.net)         ]
[                                                         ]
[<https://daringfireball.net/projects/markdown/>          ]
[                                                         ]
[## Related                                               ]
[                                                         ]
[- <https://en.wikipedia.org/wiki/Markdown>               ]
[                                                         ]
[## Comments                                              ]
[                                                         ]
[See also:                                                ]
[                                                         ]
[- [[text:formats/org]]                                   ]
[- [[cli:apps/nb]]                                        ]
[                                                         ]
[## Tags                                                  ]
[                                                         ]

[save] · last: 2021-01-01 01:00:00
```

Terminal web browsers provide different editing workflows.
[`w3m`](https://en.wikipedia.org/wiki/W3m) opens items in your `$EDITOR`,
then returns you back to the browser to save changes and continue browsing.
Edits in [`links`](https://en.wikipedia.org/wiki/Links_(web_browser))
are performed directly in the browser.

Syntax highlighting, block selection, and other
[advanced editor features](#browse---gui-editing)
are available with [`nb browse --gui`](#browse).

#### `browse add`

Add an item within the browser using the `+` link or
[`nb browse add`](#browse) / [`nb b a`](#browse).
Pass a notebook, folder, and / or filename selector to create a new note
in that location:

```bash
❯ nb browse add text:formats/
❯nb · text : formats / +

[                                                   ]
[                                                   ]
[                                                   ]
[                                                   ]
[                                                   ]
[                                                   ]
[                                                   ]
[                                                   ]
[                                                   ]
[                                                   ]

[add]
```

[`nb browse add`](#browse) includes options for quickly pre-populating
new notes with content:

```bash
❯ nb browse add --title "Example Title" --content "Example content." --tags tag1,tag2
❯nb · home : +

[# Example Title                                    ]
[                                                   ]
[#tag1 #tag2                                        ]
[                                                   ]
[Example content.                                   ]
[                                                   ]
[                                                   ]
[                                                   ]
[                                                   ]
[                                                   ]

[add]
```

#### `browse delete`

Use the `-` link on the [`nb browse edit`](#browse) page or
[`nb browse delete`](#browse) / [`nb b d`](#browse)
to delete an item:

```bash
❯ nb browse delete example:4
❯nb · example : 4 · ↓ · edit · - | +

              deleting

[4] example_file.md "Example Title"

              [delete]
 
```

#### `browse` Search

[`nb browse`](#browse) includes a search field powered by
[`nb search`](#search)
that can be used to search the current notebook or folder.
Search queries are treated as command line arguments for
[`nb search`](#search),
providing the ability to perform `AND` and `OR` queries.
Use the
[`-q <query>`](#browse) / [`--query <query>`](#browse)
option to open [`nb browse`](#browse) to
the results page for a search:

```bash
# open to a list of items containing "example" in the current notebook
❯ nb browse --query "example"
❯nb · home

search: [example             ]

[home:321] Test Title
[home:654] Sample Title
[home:789] Demo Title

# using shortcut alias and short option
❯ nb b -q "example"
❯nb · home

search: [example             ]

[home:321] Test Title
[home:654] Sample Title
[home:789] Demo Title
```

Search for [#tags](#-tagging) with the
[`-t`](#browse) / [`--tag`](#browse) / [`--tags`](#browse) options:

```bash
# open to a list of items tagged with "#tag2" in the current notebook
❯ nb browse --tag tag2
❯nb · home

search: [#tag2               ]

[home:654] Sample Title
[home:789] Demo Title

# using shortcut alias and short option
❯ nb b -t tag2
❯nb · home

search: [#tag2               ]

[home:654] Sample Title
[home:789] Demo Title
```

For more information about search options, see [Search](#-search) and
[`nb search`](#search).

#### `browse --gui`

To open any [`nb browse`](#browse) view in
the system's primary GUI web browser,
add the [`nb browse --gui`](#browse) / [`nb b -g`](#browse) option:

```bash
# open the item with id 123 in the "sample" notebook in the system's primary GUI browser
nb browse sample:123 --gui

# open the folder named "example" in the system's primary GUI browser,
# short option
nb browse example/ -g

# open the current notebook in the system's primary GUI browser,
# shortcut alias and short option
nb b -g
```

##### `browse --gui` Editing

By default,
[`nb browse --gui`](#browse)
uses the browser's default `<textarea>` for editing items.

[Ace](https://ace.c9.io/) is a text editor for GUI web browsers
that provides advanced text editing functionality,
including block selection and
[syntax highlighting](#gui-web-syntax-highlighting).

To use Ace as the editor for [`nb browse --gui`](#browse),
add the following line to your `~/.nbrc` file:

```bash
export NB_ACE_ENABLED=1
```

The next time a form is loaded in [`nb browse`](#browse),
`nb` will automatically download
(from [GitHub](https://github.com/ajaxorg/ace-builds/)),
install,
and enable the Ace editor in
[`nb browse edit --gui`](#browse) and [`nb browse add --gui`](#browse).

#### `browse` Portability

[`nb browse`](#browse) depends on
[`ncat`](https://nmap.org/ncat/), which is available as part of
the `ncat` or `nmap` package in most package managers, and
[`pandoc`](https://pandoc.org/).
When only `pandoc` is available, the current note is rendered and
<a href="#-linking">[[wiki-style links]]</a>
go to unrendered, original files.
If only `ncat` is available,
files in plain text formats are rendered with the original markup unconverted.
If neither `ncat` nor `pandoc` is available,
[`nb browse`](#browse) falls back to the default behavior of [`nb show`](#show).

#### `browse` Privacy

[`nb browse`](#browse) is completely local and self-contained within `nb`,
from the CSS and JavaScript
all the way down through the HTTP request parsing and response building,
with no imports, libraries, frameworks, or third-party code
outside of the few binary dependencies (`bash`, `git`, `ncat`, `pandoc`),
the Linux / Unix environment,
and the optional [Ace editor](#ace-editor).

Terminal web browsers don't use JavaScript, so visits from them are not
visible to some web analytics tools.
[`nb browse`](#browse) includes a number of additional features
to enhance privacy and avoid leaking information:

- Page content is cached locally within each bookmark file,
  making it readable in terminal and GUI web browsers
  without requesting the page again or needing to be connected to the internet.
- `<img>` tags in bookmarked content are removed to avoid requests.
- Outbound links are automatically rewritten to use an
  [exit page redirect](https://geekthis.net/post/hide-http-referer-headers/#exit-page-redirect)
  to mitigate leaking information via the
  [referer header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referer).
- All pages include the `<meta name="referrer" content="no-referrer" />` tag.
- Links include a `rel="noopener noreferrer"` attribute.
- `lynx` is opened with the `-noreferer` option.

#### Shortcut Alias: `nb b`

[`nb browse`](#browse) can also be used with the alias [`nb b`](#browse):

```bash
# open the current notebook in the terminal web browser
nb b

# open the item with id 123 in the "example" notebook using the terminal web browser
nb b example:123

# open the notebook named "sample" in the GUI web browser
nb b sample: -g
```

For more information, see [`nb browse`](#browse).

### 🌄 Images

<p>
  <sup>
    <a href="#overview">↑</a> ·
    <a href="#browse"><code>nb browse</code></a>,
    <a href="#import"><code>nb import</code></a>,
    <a href="#open"><code>nb open</code></a>,
    <a href="#show"><code>nb show</code></a>
  </sup>
</p>

`nb` can be used to view, organize, browse, reference, and work with images in
terminals,
web browsers,
and GUI applications.

#### Image Items

[Import](#%EF%B8%8F-import--export) images with [`nb import`](#import):

```bash
# import the image file "example.png" into the current notebook
nb import example.png

# import an image file from a URL into the current notebook
nb import https://raw.githubusercontent.com/xwmx/nb/master/docs/images/nb.png

# nb import "sample.jpg" into the "demo" folder in the "example" notebook
nb import sample.jpg example:demo/
```

Imported images are displayed with [`🌄` indicators](#indicators) in
[lists](#listing--filtering):

```bash
❯ nb
home
----
[5] Example Five
[4] 🌄 example-image.png
[3] Example Three
[2] Example Two
[1] Example One
```

Imported image items can be opened in the system GUI application for
the item's file type using [`nb open`](#open):

```bash
# open the image "example-image.png" in the system GUI photo viewer
nb open example-image.png

# open the image with id "4" in the system GUI photo viewer
nb 4 o
```

Image items can be viewed in web browsers with [`nb browse`](#browse),
providing a convenient mechanism for
[browsing](#-browsing) notebooks and folders containing image collections.

[`nb browse`](#browse) renders image items within in an `<img>` tag
on the item page. Open the item page for an image item by passing a
[selector](#-selectors) to [`nb browse`](#browse), optionally including the
[`-g`](#browse) / [`--gui`](#browse) option
to open the page in the system GUI web browser:

```bash
# open item with id "123" in the terminal web browser
nb browse 123

# open item with id "456" in the "example" notebook in the GUI web browser
nb browse example:456 --gui

# open item "example:456" in the GUI web browser, alternative
nb example:456 b -g
```

The original file can be viewed or downloaded from the item page
by either clicking the image item or using the down arrow (`↓`) link.

[`nb browse --gui`](#browse---gui) displays images in any GUI web browser.
Some terminal web browsers, such as [`w3m`](http://w3m.sourceforge.net/),
can be configured to display images.

[`nb show`](#show) can display images directly in the terminal with
supported tools and configurations, including:

- [ImageMagick](https://imagemagick.org/) with a terminal that
  supports [sixels](https://en.wikipedia.org/wiki/Sixel)
- [`imgcat`](https://www.iterm2.com/documentation-images.html) with
  [iTerm2](https://www.iterm2.com/)
- [kitty's `icat` kitten](https://sw.kovidgoyal.net/kitty/kittens/icat.html)
- [`catimg`](https://github.com/posva/catimg)

#### Inline Images

Images can be referenced and rendered inline within
notes, bookmarks, and other items.

To reference an image in the same notebook,
specify the image's relative path within the notebook:

```markdown
# reference "example.jpg" from markdown
![](example.jpg)

# reference "demo.png" in the "sample" folder from markdown
![](sample/demo.png)
```

Images in any notebook can be referenced using the `--original` URL,
obtainable from the image's [`nb browse`](#browse) item page
by either clicking the image item or using the down arrow (`↓`) link.

```markdown
# reference "example.jpg" in the "home" notebook with the --original URL
![](http://localhost:6789/--original/home/example.jpg)
```

Image references in content are rendered inline within web browsers with
[`nb browse`](#browse) and [`nb show --render`](#show).

`<img>` tags are stripped from bookmarked content when rendering to HTML.
Inline images can still be used in other bookmark sections like
[`## Comment`](#-comment).

### 🗂 Zettelkasten

<p>
  <sup>
    <a href="#overview">↑</a>
  </sup>
</p>

Zettelkasten (German: "slip box") is a method of note-taking and
personal knowledge management modeled around a few key features:

- Notes are taken liberally on index cards.
- Each note is numbered for easy reference.
- Index cards are organized into boxes.
- Index cards can reference other index cards.
- Cards can include tags and other metadata.

Since `nb` works directly on plain text files
organized in normal system directories in normal git repositories,
`nb` is a very close digital analogue to physical zettelkasten note-taking.

|    Zettelkasten   |                       `nb`                      |
|:-----------------:|:-----------------------------------------------:|
| index cards       | [notes](#-notes) & [bookmarks](#-bookmarks)     |
| numbering         | ids & [selectors](#-selectors)                  |
| slip boxes        | [notebooks](#-notebooks)                        |
| tags              | [#tags](#-tagging)                              |
| metadata          | [front matter](#front-matter)                   |
| cross-references  |  <a href="#-linking">[[wiki-style links]]</a>   |
| fast note-taking  | [`nb add`](#adding) / [`nb <url>`](#-bookmarks) |

For more information about Zettelkasten, see
[Wikipedia](https://en.wikipedia.org/wiki/Zettelkasten).

### 📂 Folders

<p>
  <sup>
    <a href="#overview">↑</a> ·
    <a href="#add"><code>nb add</code></a>,
    <a href="#browse"><code>nb browse</code></a>,
    <a href="#folders"><code>nb folders</code></a>,
    <a href="#list"><code>nb list</code></a>,
    <a href="#ls"><code>nb ls</code></a>
  </sup>
</p>

Items can be organized in folders.
To add a note to a folder,
call [`nb add`](#add) with the folder's relative path within the notebook
followed by a slash:

```bash
# add a new note in the folder named "example"
nb add example/

# add a new note in the folder named "demo" in "example"
nb add example/demo/
```

`nb` automatically creates any intermediate folders as needed.

Folders can be created directly using [`nb add folder`](#add),
[`nb folders add`](#folders), and [`nb add --type folder`](#add):

```bash
# create a new folder named "sample"
nb add folder sample

# create a new folder named "sample", alternative
nb folders add sample

# create a new folder named "demo"
nb add demo --type folder

# create a folder named "example" containing a folder named "test"
nb add example/test --type folder
```

To list the items in a folder, pass the folder relative path to
`nb`,
[`nb ls`](#ls),
[`nb list`](#list),
or [`nb browse`](#browse)
with a trailing slash:

```bash
❯ nb example/demo/
home
----
[example/demo/3] Title Three
[example/demo/2] Title Two
[example/demo/1] Title One
```

Folders can also be identified by the folder's id
and listed with a trailing slash:

```bash
❯ nb list
[1] 📂 example

❯ nb list 1/
[example/2] 📂 demo
[example/1] document.md

❯ nb list 1/2/
[example/demo/3] Title Three
[example/demo/2] Title Two
[example/demo/1] Title One
```

Items in folders can be idenitified with
the folder's relative path using either folder ids or names,
followed by the id, title, or filename of the item:

```bash
# list item 1 ("Title One", one.md) in the example/demo/ folder
nb list example/demo/1

# edit item 1 ("Title One", one.md) in the example/demo/ folder
nb edit example/2/one.md

# show item 1 ("Title One", one.md) in the example/demo/ folder
nb show 1/2/Title\ One

# delete item 1 ("Title One", one.md) in the example/demo/ folder
nb delete 1/demo/1
```

For folders and items in other notebooks,
combine the relative path with the notebook name, separated by a colon:

```bash
# list the contents of the "sample" folder in the "example" notebook
nb example:sample/

# add an item to the "sample/demo" folder in the "example" notebook
nb add example:sample/demo/

# edit item 3 in the "sample/demo" folder in the "example" notebook
nb edit example:sample/demo/3
```

[Browse](#-browsing) starting at any folder with [`nb browse`](#browse):

```bash
❯ nb browse example:sample/demo/
❯nb · example : sample / demo /

search: [                    ]

[example:sample/demo/5] Title Five
[example:sample/demo/4] Title Four
[example:sample/demo/3] Title Three
[example:sample/demo/2] Title Two
[example:sample/demo/1] Title One
```

For more information about identifying folders, see [Selectors](#-selectors).

### 📌 Pinning

<p>
  <sup>
    <a href="#overview">↑</a> ·
    <a href="#pin"><code>nb pin</code></a>,
    <a href="#unpin"><code>nb unpin</code></a>,
    <a href="#ls"><code>nb ls</code></a>,
    <a href="#browse"><code>nb browse</code></a>
  </sup>
</p>

Items can be pinned so they appear first in
`nb`, [`nb ls`](#ls), and [`nb browse`](#browse):

```bash
❯ nb
home
----
[2] 📌 Title Two
[5] Title Five
[4] Title Four
[3] Title Three
[1] Title One
```

Use [`nb pin`](#pin) and [`nb unpin`](#unpin) to pin and unpin items:

```bash
❯ nb
home
----
[5] Title Five
[4] Title Four
[3] Title Three
[2] Title Two
[1] Title One

❯ nb pin 4
Pinned: [4] four.md "Title Four"

❯ nb pin 1
Pinned: [1] one.md "Title One"

❯ nb
home
----
[4] 📌 Title Four
[1] 📌 Title One
[5] Title Five
[3] Title Three
[2] Title Two

❯ nb unpin 4
Unpinned: [4] four.md "Title Four"

❯ nb
home
----
[1] 📌 Title One
[5] Title Five
[4] Title Four
[3] Title Three
[2] Title Two
```

`nb` can also be configured to pin notes that contain
a specified [#hashtag](#-tagging) or other search pattern.
To enable tag / search-based pinning,
set the `$NB_PINNED_PATTERN` environment variable to
the desired [#tag](#-tagging) or pattern.

For example, to treat all items tagged with `#pinned` as pinned items,
add the following line to your `~/.nbrc` file,
which can be opened in your editor with [`nb settings edit`](#settings):

```bash
export NB_PINNED_PATTERN="#pinned"
```

All [indicator icons](#indicators) in `nb` can be customized, so
to use a different character as the pindicator,
simply add a line like the following to your `~/.nbrc` file:

```bash
export NB_INDICATOR_PINNED="💖"
```

```bash
❯ nb
home
----
[1] 💖 Title One
[5] Title Five
[4] Title Four
[3] Title Three
[2] Title Two
```

To bump an item to the top of the list without pinning, use the
[`bump` plugin](#bump).

### 🔍 Search

<p>
  <sup>
    <a href="#overview">↑</a> ·
    <a href="#search"><code>nb search</code></a>
  </sup>
</p>

Use [`nb search`](#search) (shortcut: [`nb q`](#search)) to
perform full text searches, with support for regular expressions,
[#tags](#-tagging), and both `AND` and `OR` queries:

```bash
# search current notebook for "example query"
nb search "example query"

# search the notebook "example" for "example query"
nb search example: "example query"

# search the folder named "demo" for "example query"
nb search demo/ "example query"

# search all unarchived notebooks for "example query" and list matching items
nb search "example query" --all --list

# search for "example" AND "demo" with multiple arguments
nb search "example" "demo"

# search for "example" AND "demo" with option
nb search "example" --and "demo"

# search for "example" OR "sample" with argument
nb search "example|sample"

# search for "example" OR "sample" with option
nb search "example" --or "sample"

# search items containing the hashtag "#example"
nb search "#example"

# search with a regular expression
nb search "\d\d\d-\d\d\d\d"

# search bookmarks for "example"
nb search "example" --type bookmark

# search bookmarks for "example", alternative
nb bk q "example"

# search the current notebook for "example query"
nb q "example query"

# search the notebook named "example" for "example query"
nb q example: "example query"

# search all unarchived notebooks for "example query" and list matching items
nb q -la "example query"
```

[`nb search`](#search) prints the id number, filename,
and title of each matched file,
followed by each search query match and its line number,
with color highlighting:

```bash
❯ nb search "example"
[314]  🔖 example.bookmark.md "Example Bookmark (example.com)"
--------------------------------------------------------------
1:# Example Bookmark (example.com)

3:<https://example.com>

[2718] example.md "Example Note"
--------------------------------
1:# Example Note
```

To just print the note information line without the content matches,
use the [`-l`](#search) or [`--list`](#search) option:

```bash
❯ nb search "example" --list
[314]  🔖 example.bookmark.md "Example Bookmark (example.com)"
[2718] example.md "Example Note"
```

Multiple query arguments are treated as `AND` queries,
returning items that match all queries.
`AND` queries can also be specified with the
[`--and <query>`](#search) option:

```bash
# search for items tagged with "#example" AND "#demo" AND "#sample" using
# multiple arguments
nb q "#example" "#demo" "#sample"

# options
nb q "#example" --and "#demo" --and "#sample"
```

`nb` matches `AND` query terms regardless of where they appear in a document,
an improvement over most approaches for performing `AND` queries
with command line tools,
which typically only match terms appearing on the same line.

`OR` queries return items that match at least one of the queries
and can be created by separating terms in a single argument
with a pipe character `|` or with the [`--or <query>`](#search) option:

```bash
# search for "example" OR "sample" with argument
nb q "example|sample"

# search for "example" OR "sample" with option
nb q "example" --or "sample"
```

[`--or`](#search) and [`--and`](#search) queries can be used together:

```bash
nb q "example" --or "sample" --and "demo"
# equivalent: example|sample AND demo|sample
```

Search for [#tags](#-tagging) with flexible
[`nb search --tags [<tags>]`](#search) / [`nb q -t [<tags>]`](#search) options:

```bash
# search for tags in the current notebook
nb search --tags

# search for tags in the "sample" notebook, shortcut alias
nb sample:q --tags

# search for items tagged with "#tag1"
nb search --tag tag1

# search for items tagged with "#tag1", shortcut alias and short option
nb q -t tag1

# search for items tagged with "#tag1", shortcut alias and argument
nb q \#tag1

# search for items tagged with "#tag1", shortcut alias and argument, alternative
nb q "#tag1"

# search for items in the "sample" notebook tagged with "#tag1" AND "#tag2"
nb sample:search --tag tag1 --tag tag2

# search for items in the "sample" notebook tagged with "#tag1" AND "#tag2"
nb sample:q --tags tag1,tag2

# search for items in the current notebook tagged with "#tag1" AND "#tag2"
nb q --tag tag1 --tag tag2

# search for items in the current notebook tagged with "#tag1" OR "#tag2"
nb q -t tag1 --or -t tag2

# search for items tagged with "#tag1" AND "#tag2" AND "#tag3"
nb q -t tag1 --tags tag2,tag3

# search for items tagged with "#tag1" OR "#tag2" OR "#tag3"
nb q -t tag1 --or --tags tag2,tag3

# search for items tagged with "#tag1" OR "#tag2" OR "#tag3"
nb q \#tag1 --or -t tag2 --or "#tag3"
```

[`nb search`](#search) leverages Git's powerful built-in
[`git grep`](https://git-scm.com/docs/git-grep).
`nb` also supports performing searches with alternative search tools
using the [`--utility <name>`](#search) option.

Supported alternative search tools:
- [`rga`](https://github.com/phiresky/ripgrep-all)
- [`rg`](https://github.com/BurntSushi/ripgrep)
- [`ag`](https://github.com/ggreer/the_silver_searcher)
- [`ack`](https://beyondgrep.com/)
- [`grep`](https://en.wikipedia.org/wiki/Grep)

##### Shortcut Alias: `nb q`

[`nb search`](#search) can also be used with the alias
[`nb q`](#search) (for "query"):

```bash
# search for "example" and print matching excerpts
nb q "example"

# search for "example" and list each matching file
nb q -l "example"

# search for "example" in all unarchived notebooks
nb q -a "example"

# search for "example" in the notbook named "sample"
nb sample:q "example"
```

For more information about search, see [`nb help search`](#search).

##### Searching with `browse`

Searches can be performed within terminal and GUI web browsers using
[`nb browse --query`](#browse) / [`nb b -q`](#browse):

```bash
❯ nb browse --query "#example"
❯nb · home : +

search: [#example             ]

[home:7]   Title Seven
[home:32]  Title Thirty-Two
[home:56]  Title Fifty-Six
[home:135] Title One Hundred and Thirty-Five
```

For more information, see [Browsing](#-browsing).

### ↔ Moving & Renaming

<p>
  <sup>
    <a href="#overview">↑</a> ·
    <a href="#move"><code>nb move</code></a>,
    <a href="#copy"><code>nb copy</code></a>
  </sup>
</p>

Use [`nb move`](#move) (alias: [`nb rename`](#move), shortcut: [`nb mv`](#move))
to move and rename items:

```bash
# move "example.md" to "sample.org"
nb move example.md sample.org

# rename note 2 ("example.md") to "New Name.md"
nb rename 2 "New Name"
```

Items can be moved between notebooks and folders:

```bash
# move note 12 from the "example" notebook into "Sample Folder" in the "demo" notebook
nb move example:12 demo:Sample\ Folder/
```

When the file extension is omitted, the existing extension is used:

```bash
# rename "example.bookmark.md" to "New Name.bookmark.md"
nb move example.bookmark.md "New Name"
```

When only a file extension is specified, only the extension is updated:

```bash
# change the file extension of note 5 ("demo file.md") to .org ("demo file.org")
nb rename 5 .org
```

Use [`nb rename --to-bookmark`](#move) to change the extension of a note
to `.bookmark.md`,
[`nb rename --to-todo`](#move) to change the extension to `.todo.md`,
and [`nb rename --to-note`](#move) to change the extension
of a bookmark or todo to either `.md` or the extension set with
[`nb set default_extension`](#default_extension):

```bash
# rename note 3 ("example.md") to a bookmark named "example.bookmark.md"
nb rename 3 --to-bookmark

# rename bookmark 6 ("sample.bookmark.md") to a note named "sample.md"
nb rename 6 --to-note

# rename note 7 ("demo.md") to a todo named "demo.todo.md"
nb rename 7 --to-todo
```

Use [`nb rename --to-title`](#move) to set the filename to the note title,
lowercased with spaces and disallowed filename characters replaced
with underscores:

```bash
❯ nb rename 12 --to-title
Moving:   [12] 20210101010000.md "Example Title"
To:       example_title.md
Proceed?  [y/N]
```

Copy an item to a destination notebook, folder path, or filename
with [`nb copy`](#copy) (alias: [`nb duplicate`](#copy)):

```bash
# copy item 456 to "sample.md"
nb copy 456 sample.md

# copy item 678 to the "example" notebook
nb copy 678 example:

# copy item 789 to the "demo" folder
nb copy 789 demo/

# copy item 543 to test.md in the "sample" folder in the "example" notebook
nb copy 543 example:sample/test.md
```

Omit a destination to copy the item in place:

```bash
# copy item 123 ("example.md") to example-1.md
❯ nb copy 123
Added: [124] example-1.md

# copy item 123 ("example.md") to example-2.md, alias
❯ nb duplicate 123
Added: [125] example-2.md
```

For more information about moving, renaming, and copying items, see
[`nb help move`](#move) and [`nb help copy`](#copy).

### 🗒 Revision History

<p>
  <sup>
    <a href="#overview">↑</a> ·
    <a href="#history"><code>nb history</code></a>,
    <a href="#notebooks"><code>nb notebooks</code></a>
  </sup>
</p>

Whenever a note is added, modified, or deleted,
`nb` automatically commits the change to git transparently in the background.

Use [`nb history`](#history) to view the revision history of
any notebook, folder, or item:

```bash
# show history for current notebook
nb history

# show history for note number 4
nb history 4

# show history for note with filename example.md
nb history example.md

# show history for note titled "Example"
nb history Example

# show history for the notebook named "example"
nb example:history

# show history for the notebook named "example", alternative
nb history example:

# show the history for note 12 in the notebook named "example"
nb history example:12
```

[`nb history`](#history) uses `git log` by default and prefers
[`tig`](https://github.com/jonas/tig) when available.

#### Authorship

By default, git commits are attributed to the email and name configured in your
[global `git` configuration](https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration).

Change the email and name used for a notebook with
[`nb notebooks author`](#notebooks):

```bash
# edit the commit author email and name for the current notebook
❯ nb notebooks author
Current configuration for: home
--------------------------
email (global): example@example.test
name  (global): Example Name

Update?  [y/N]

# edit the commit author email and name for the notebook named "example"
❯ nb notebooks author example
Current configuration for: example
--------------------------
email (global): example@example.test
name  (global): Example Name

Update?  [y/N]
```

The updated author email and name applies to subsequent commits.

To use a different email and name from the beginning of a notebook's
history, create the new notebook using
[`nb notebooks add --author`](#notebooks) or
[`nb notebooks init --author`](#notebooks).

### 📚 Notebooks

<p>
  <sup>
    <a href="#overview">↑</a> ·
    <a href="#notebooks"><code>nb&nbsp;notebooks</code></a>,
    <a href="#archive"><code>nb&nbsp;archive</code></a>,
    <a href="#unarchive"><code>nb&nbsp;unarchive</code></a>,
    <a href="#use"><code>nb&nbsp;use</code></a>
  </sup>
</p>

You can create additional notebooks, each of which has its own version history.

Create a new notebook with [`nb notebooks add`](#notebooks):

```bash
# add a notebook named example
nb notebooks add example
```

`nb` and [`nb ls`](#ls) list the available notebooks above the list of notes:

```bash
❯ nb
example · home
--------------
[3] Title Three
[2] Title Two
[1] Title One
```

Commands in `nb` run within the current notebook, and identifiers
such as ids, filenames, and titles refer to notes within the current notebook.
`nb edit 3`, for example, tells `nb` to
[`edit`](#edit) note with id `3` within the current notebook.

To switch to a different notebook, use [`nb use`](#use):

```bash
# switch to the notebook named "example"
nb use example
```

If you are in one notebook and you want
to perform a command in a different notebook without switching to it,
add the notebook name with a colon before the command name:

```bash
# add a new note in the notebook "example"
nb example:add

# add a new note in the notebook "example", shortcut alias
nb example:a

# show note 5 in the notebook "example"
nb example:show 5

# show note 5 in the notebook "example", shortcut alias
nb example:s 5

# edit note 12 in the notebook "example"
nb example:edit 12

# edit note 12 in the notebook "example", shortcut alias
nb example:e 12

# search for "example query" in the notebook "example"
nb example:search "example query"

# search for "example query" in the notebook "example", shortcut alias
nb example:q "example query"

# show the revision history of the notebook "example"
nb example:history
```

The notebook name with colon can also be used as a modifier to
the id, filename, or title:

```bash
# edit note 12 in the notebook "example"
nb edit example:12

# edit note 12 in the notebook "example", shortcut alias
nb e example:12

# edit note 12 in the notebook "example", alternative
nb example:12 edit

# edit note 12 in the notebook "example", alternative, shortcut alias
nb example:12 e

# show note titled "misc" in the notebook "example"
nb show example:misc

# show note titled "misc" in the notebook "example", shortcut alias
nb s example:misc

# delete note with filename "todos.md" in the notebook "example", alternative
nb example:todos.md delete

# delete note with filename "todos.md" in the notebook "example", alternative,
# shortcut alias
nb example:todos.md d
```

When a notebook name with colon is called without a subcommand,
`nb` runs [`nb ls`](#ls) in the specified notebook:

```bash
❯ nb example:
example · home
--------------
[example:3] Title Three
[example:2] Title Two
[example:1] Title One
```

A bookmark can be created in another notebook by specifying
the notebook name with colon, then a space, then the URL and bookmark options:

```bash
# create a new bookmark in a notebook named "sample"
❯ nb sample: https://example.com --tags tag1,tag2
```

Notes can also be moved between notebooks:

```bash
# move note 3 from the current notebook to "example"
nb move 3 example:

# move note 5 in the notebook "example" to the notebook "sample"
nb move example:5 sample:
```

##### Example Workflow

The flexibility of `nb`'s argument handling makes it easy to
build commands step by step as items are listed, filtered, viewed, and edited,
particularly in combination with shell history:

```bash
# list items in the "example" notebook
❯ nb example:
example · home
--------------
[example:3] Title Three
[example:2] Title Two
[example:1] Title One

# filter list
❯ nb example: three
[example:3] Title Three

# view item
❯ nb example:3 show
# opens item in `less`

# edit item
❯ nb example:3 edit
# opens item in $EDITOR
```

##### Notebooks and Tab Completion

[`nb` tab completion](#tab-completion) is optimized for
frequently running commands in various notebooks using the colon syntax,
so installing the completion scripts is recommended
and makes working with notebooks easy, fluid, and fun.

For example, listing the contents of a notebook is usually as simple as typing
the first two or three characters of the name,
then pressing the `<tab>` key,
then pressing `<enter>` / `<return>`:

```bash
❯ nb exa<tab>
# completes to "example:"
❯ nb example:
example · home
--------------
[example:3] Title Three
[example:2] Title Two
[example:1] Title One
```

Scoped notebook commands are also available in tab completion:

```bash
❯ nb exa<tab>
# completes to "example:"
❯ nb example:hi<tab>
# completes to "example:history"
```

#### Notebooks, Tags, and Taxonomy

`nb` is optimized to work well with a collection of notebooks, so
notebooks are a good way to organize notes and bookmarks by top-level topic.

[#tags](#-tagging) are searchable across notebooks and can be created ad hoc,
making notebooks and tags distinct and complementary organizational systems
in `nb`.

Search for a tag in or across notebooks with
[`nb search`](#search) / [`nb q`](#search):

```bash
# search for #tag in the current notebook
nb q --tag tag

# search for #tag in all notebooks, short options
nb q -t tag -a

# search for #tag in the "example" notebook, argument
nb q example: "#tag"
```

#### Global and Local Notebooks

##### Global Notebooks

By default, all `nb` notebooks are global, making them
always accessible in the terminal regardless of the current working directory.
Global notebooks are stored in the directory configured in
[`nb set nb_dir`](#nb_dir),
which is `~/.nb` by default.

##### Local Notebooks

`nb` also supports creating and working with local notebooks.
Local notebooks are notebooks that are
anywhere on the system outside of `NB_DIR`.
Any folder can be an `nb` local notebook, which is just a normal folder
that has been initialized as a git repository and contains an `nb` .index file.
Initializing a folder as an `nb` local notebook is a very easy way to
add structured git versioning to any folder of documents and other files.

When `nb` runs within a local notebook,
the local notebook is set as the current notebook:

```bash
❯ nb
local · example · home
----------------------
[3] Title Three
[2] Title Two
[1] Title One
```

A local notebook is always referred to by the name `local`
and otherwise behaves just like a global notebook
whenever a command is run from within it:

```bash
# add a new note in the local notebook
nb add

# edit note 15 in the local notebook
nb edit 15

# move note titled "Todos" from the home notebook to the local notebook
nb move home:Todos local:

# move note 1 from the local notebook to the home notebook
nb move 1 home:

# search the local notebook for <query string>
nb search "query string"

# search the local notebook and all unarchived global notebooks for <query string>
nb search "query string" --all
```

Local notebooks can be created with [`nb notebooks init`](#notebooks):

```bash
# initialize the current directory as a notebook
nb notebooks init

# create a new notebook at ~/example
nb notebooks init ~/example

# clone an existing notebook to ~/example
nb notebooks init ~/example https://github.com/example/example.git
```

Local notebooks can also be created by exporting a global notebook:

```bash
# export global notebook named "example" to "../path/to/destination"
nb notebooks export example ../path/to/destination

# alternative
nb export example ../path/to/destination
```

Local notebooks can also be imported, making them global:

```bash
# import notebook or folder at "../path/to/notebook"
nb notebooks import ../path/to/notebook

# alternative
nb import ../path/to/notebook
```

[`nb notebooks init`](#notebooks) and [`nb notebooks import`](#notebooks)
can be used together to easily turn any directory of existing files
into a global `nb` notebook:

```bash
❯ ls
example-directory

❯ nb notebooks init example-directory
Initialized local notebook: /home/username/example-directory

❯ nb notebooks import example-directory
Imported notebook: example-directory

❯ nb notebooks
example-directory
home
```

#### Archiving Notebooks

<p>
  <sup>
    <a href="#-notebooks">↑</a> ·
    <a href="#archive"><code>nb&nbsp;archive</code></a>,
    <a href="#status"><code>nb&nbsp;status</code></a>,
    <a href="#unarchive"><code>nb&nbsp;unarchive</code></a>
  </sup>
</p>

Notebooks can be archived using
[`nb archive`](#archive) (shortcut: [`nb ar`](#archive)):

```bash
# archive the current notebook
nb archive

# archive the notebook named "example"
nb archive example

# archive the current notebook, shortcut alias
nb ar

# archive the notebook named "example", shortcut alias
nb ar example
```

When a notebook is archived it is not included in
[`nb`](#ls) / [`nb ls`](#ls) output,
[`nb search --all`](#search),
or tab completion,
nor synced automatically with [`nb sync --all`](#sync).

```bash
❯ nb
example1 · example2 · example3 · [1 archived]
---------------------------------------------
[3] Title Three
[2] Title Two
[1] Title One
```

Archived notebooks can still be used individually
using normal notebook commands:

```bash
# switch the current notebook to the archived notebook "example"
nb use example

# run the `list` subcommand in the archived notebook "example"
nb example:list
```

Check a notebook's archival status with
[`nb status`](#status) (shortcut: [`nb st`](#status)) and
[`nb notebooks status`](#notebooks):

```bash
# print status information, including archival status, for the current notebook
nb status

# print status information, including archival status, for the notebook named "example"
nb status example

# print status information, including archival status, for the current notebook,
# shortcut alias
nb st

# print status information, including archival status, for the notebook named "example",
# shortcut alias
nb st example

# print the archival status of the current notebook
nb notebooks status

# print the archival status of the notebook named "example"
nb notebooks status example
```

Use [`nb unarchive`](#unarchive) (shortcut: [`nb unar`](#unarchive))
to unarchive a notebook:

```bash
# unarchive the current notebook
nb unarchive

# unarchive the notebook named "example"
nb unarchive example
```

For more information about working with notebooks, see
[`nb help notebooks`](#notebooks),
[`nb help archive`](#archive),
and [`nb help unarchive`](#unarchive).

For technical details about notebooks, see
[`nb` Notebook Specification](#nb-notebook-specification).

### 🔄 Git Sync

<p>
  <sup>
    <a href="#overview">↑</a> ·
    <a href="#remote"><code>nb remote</code></a>,
    <a href="#sync"><code>nb sync</code></a>
  </sup>
</p>

Each notebook can be synced with a remote git repository by
setting the remote URL using [`nb remote`](#remote):

```bash
# set the current notebook's remote to a private GitHub repository
nb remote set https://github.com/example/example

# set the remote for the notebook named "example"
nb example:remote set https://github.com/example/example
```

Any notebook with a remote URL will sync automatically
every time a command is run in that notebook.

When you use `nb` on multiple systems, you can
set a notebook on each system to the same remote
and `nb` will keep everything in sync in the background
every time there's a change in that notebook.

Since each notebook has its own git history,
you can have some notebooks syncing with remotes
while other notebooks are only available locally on that system.

Many services provide free private git repositories, so
git syncing with `nb` is easy, free, and vendor-independent.
You can also sync your notes using
Dropbox, Drive, Box, Syncthing, or another syncing tool
by changing your `nb` directory with
[`nb set nb_dir <path>`](#nb_dir),
and git syncing will still work simultaneously.

Clone an existing notebook by passing the URL to
[`nb notebooks add`](#notebooks):

```bash
# create a new notebook named "example" cloned from a private GitLab repository
nb notebooks add example https://gitlab.com/example/example.git
```

Turn off syncing for a notebook by removing the remote:

```bash
# remove the remote from the current notebook
nb remote remove

# remove the remote from the notebook named "example"
nb example:remote remove
```

Automatic git syncing can be turned on or off with
[`nb set auto_sync`](#auto_sync).

To sync manually, use [`nb sync`](#sync):

```bash
# manually sync the current notebook
nb sync

# manually sync the notebook named "example"
nb example:sync
```

To bypass `nb` syncing and run `git` commands directly within a
notebook, use [`nb git`](#git):

```bash
# run `git fetch` in the current notebook
nb git fetch origin

# run `git status` in the notebook named "example"
nb example:git status
```

#### Syncing Multiple Notebooks with One Remote

Multiple notebooks can be synced to one remote using orphan branches.
An
[orphan branch](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt---orphanltnewbranchgt)
is a branch with a history that is independent
from the repository's `main`, `master`,
or equivalent primary branch history.
To sync a notebook with a new orphan branch,
add the remote using [`nb remote set`](#remote)
and select the option to create a new orphan branch.
The name of orphan branch is derived from notebook name
and can alternatively be specified as an argument to
[`nb remote set`](#remote):

```bash
# set the remote for the current notebook to a remote URL and branch
nb remote set https://github.com/xwmx/example demo-branch
```

To create a notebook using an existing orphan branch on a remote,
pass the branch name to
[`nb init`](#init),
[`nb notebooks add`](#notebooks), or
[`nb notebooks init`](#notebooks) after the URL:

```bash
# initialize new "home" notebook with the branch "sample-branch" on the remote
nb init https://github.com/xwmx/example sample-branch

# add a new "example" notebook from the branch "example-branch" on the remote
nb notebooks add example https://github.com/xwmx/example example-branch
```

To list all branches on a remote, use [`nb remote branches`](#remote):

```bash
# list all branches on the current remote
nb remote branches

# list all branches on a remote repository identified by a URL
nb remote branches "https://github.com/xwmx/example"
```

For information about assigning remotes, see [`nb help remote`](#remote).

#### Private Repositories and Git Credentials

Syncing with private repositories requires
configuring git to not prompt for credentials.
For repositories cloned over HTTPS,
[credentials can be cached with git
](https://docs.github.com/en/free-pro-team@latest/github/using-git/caching-your-github-credentials-in-git).
For repositories cloned over SSH,
[keys can be added to the ssh-agent
](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).

Use [`nb sync`](#sync) within a notebook to determine
whether your configuration is working.
If `nb sync` displays a password prompt,
then follow the instructions above to configure your credentials.
The password prompt can be used to authenticate, but
`nb` does not cache or otherwise handle git credentials in any way,
so there will likely be multiple password prompts during each sync
if credentials are not configured.

#### Sync Conflict Resolution

`nb` handles git operations automatically, so
you shouldn't ever need to use the `git` command line tool directly.
`nb` merges changes when syncing
and handles conflicts using a couple different strategies.

When [`nb sync`](#sync) encounters a conflict in a text file
and can't cleanly merge overlapping local and remote changes,
`nb` saves both versions within the file separated by git conflict markers
and prints a message indicating which files contain conflicting text.
Use [`nb edit`](#edit) to remove the conflict markers
and delete any unwanted text.

For example, in the following file, the second list item was changed
on two systems, and git has no way to determine which one we want to keep:

```
# Example Title

- List Item apple
<<<<<<< HEAD
- List Item apricot
=======
- List Item pluot
>>>>>>> 719od01... [nb] Commit
- List Item plum
```

The local change is between the lines starting with
`<<<<<<<` and `=======`,
while the remote change is between the
`=======` and `>>>>>>>`
lines.

To resolve this conflict by keeping both items, simply
edit the file with [`nb edit`](#edit) and
remove the lines starting with `<<<<<<<`, `=======`, and `>>>>>>>`:

```
# Example Title

- List Item apple
- List Item apricot
- List Item pluot
- List Item plum
```

When `nb` encounters a conflict in a binary file,
such as an encrypted note,
both versions of the file are saved in the notebook as individual files,
with `--conflicted-copy` appended to the filename
of the version from the remote.
To resolve a conflicted copy of a binary file,
compare both versions and merge them manually,
then delete the `--conflicted-copy`.

If you do encounter a conflict that `nb` says it can't merge at all,
[`nb git`](#git) and [`nb run`](#run) can be used to
perform git and shell operations within the notebook
to resolve the conflict manually.
Please also
[open an issue](https://github.com/xwmx/nb/issues/new)
with any relevant details
that could inform a strategy for handling any such cases automatically.

### ↕️ Import / Export

<p>
  <sup>
    <a href="#overview">↑</a> ·
    <a href="#import"><code>nb import</code></a>,
    <a href="#export"><code>nb export</code></a>,
    <a href="#browse"><code>nb browse</code></a>
  </sup>
</p>

Files of any type can be imported into a notebook using
[`nb import`](#import) (shortcut: [`nb i`](#import)).
[`nb edit`](#edit) and [`nb open`](#open) open files in
your system's default application for that file type.

```bash
# import an image file
nb import ~/Pictures/example.png

# open image in your default image viewer
nb open example.png

# import a .docx file
nb import ~/Documents/example.docx

# open .docx file in Word or your system's .docx viewer
nb open example.docx
```

Multiple filenames and globbing are supported:

```bash
# import all files and directories in the current directory
nb import ./*

# import all markdown files in the current directory
nb import ./*.md

# import example.md and sample.md in the current directory
nb import example.md sample.md
```

[`nb import`](#import) can also download and import files directly from the web:

```bash
# import a PDF file from the web
nb import https://example.com/example.pdf
# Imported "https://example.com/example.pdf" to "example.pdf"

# open example.pdf in your system's PDF viewer
nb open example.pdf
```

Some imported file types have [indicators](#indicators) to make them
easier to identify in lists:

```bash
❯ nb
home
----
[6] 📖 example-ebook.epub
[5] 🌄 example-picture.png
[4] 📄 example-document.docx
[3] 📹 example-video.mp4
[2] 🔉 example-audio.mp3
[1] 📂 Example Folder
```

Notes, bookmarks, and other files can be exported using [`nb export`](#export).
If [Pandoc](https://pandoc.org/) is installed,
notes can be automatically converted to any of the
[formats supported by Pandoc](https://pandoc.org/MANUAL.html#option--to).
By default, the output format is determined by the file extension:

```bash
# export a Markdown note to a .docx Microsoft Office Word document
nb export example.md /path/to/example.docx

# export a note titled "Movies" to an HTML web page.
nb export Movies /path/to/example.html
```

For more control over the `pandoc` options, use the
[`nb export pandoc`](#export) subcommand:

```bash
# export note 42 as an epub with pandoc options
nb export pandoc 42 --from markdown_strict --to epub -o path/to/example.epub
```

[`nb export notebook`](#export) and [`nb import notebook`](#import) can be
used to export and import notebooks:

```bash
# export global notebook named "example" to "../path/to/destination"
nb export notebook example ../path/to/destination

# import notebook or folder at "../path/to/notebook"
nb import notebook ../path/to/notebook
```

[`nb export notebook`](#export) and [`nb import notebook`](#import)
behave like aliases for
[`nb notebooks export`](#notebooks) and [`nb notebooks import`](#notebooks),
and the subcommands can be used interchangeably.

For more information about imported and exported notebooks, see
[Global and Local Notebooks](#global-and-local-notebooks).

For [`nb import`](#import) and [`nb export`](#export) help information, see
[`nb help import`](#import) and [`nb help export`](#export).

#### Exporting with `browse`

Items can be exported using terminal and GUI [web browsers](#-browsing).
Use the down arrow (`↓`) link
on the [`nb browse`](#browse) item page
to download the original file:

```bash
❯ nb browse 123
❯nb · home : 123 · ↓ | +

    example.pdf
 
```

### ⚙️ `set` & `settings`

<p>
  <sup>
    <a href="#overview">↑</a> ·
    <a href="#settings"><code>nb settings</code></a>,
    <a href="#unset"><code>nb unset</code></a>
  </sup>
</p>

[`nb set`](#settings) and [`nb settings`](#settings)
open the settings prompt,
which provides an easy way to change your `nb` settings.

```bash
nb set
```

To update a setting in the prompt,
enter the setting name or number and then enter the new value.
`nb` will add the setting to your `~/.nbrc` configuration file.

#### Example: editor

`nb` can be configured to use a specific command line editor
using the `editor` setting.

The settings prompt for a setting can be started by passing
the setting name or number to [`nb set`](#settings):

```bash
❯ nb set editor
[6]  editor
     ------
     The command line text editor used by `nb`.

     • Example Values:

         atom
         code
         emacs
         macdown
         mate
         micro
         nano
         pico
         subl
         vi
         vim

EDITOR is currently set to vim

Enter a new value, unset to set to the default value, or q to quit.
Value:
```

A setting can also be updated without the prompt by
passing both the name and value to [`nb set`](#settings):

```bash
# set editor with setting name
❯ nb set editor code
EDITOR set to code

# set editor with setting number (6)
❯ nb set 6 code
EDITOR set to code

# set the color theme to blacklight
❯ nb set color_theme blacklight
NB_COLOR_THEME set to blacklight

# set the default `ls` limit to 10
❯ nb set limit 10
NB_LIMIT set to 10
```

Use [`nb settings get`](#settings) to print the value of a setting:

```bash
❯ nb settings get editor
code

❯ nb settings get 6
code
```

Use
[`nb unset`](#unset) or
[`nb settings unset`](#settings)
to unset a setting and revert to the default:

```bash
❯ nb unset editor
EDITOR restored to the default: vim

❯ nb settings get editor
vim
```

[`nb set`](#settings) and [`nb settings`](#settings)
are aliases that refer to the same subcommand,
so the two subcommand names can be used interchangeably.

For more information about [`set`](#settings) and [`settings`](#settings), see
[`nb help settings`](#settings).

### 🎨 Color Themes

<p>
  <sup>
    <a href="#overview">↑</a> ·
    <a href="#color_theme"><code>nb&nbsp;set&nbsp;color_theme</code></a>,
    <a href="#syntax_theme"><code>nb&nbsp;set&nbsp;syntax_theme</code></a>,
    <a href="#color_primary"><code>nb&nbsp;set&nbsp;color_primary</code></a>,
    <a href="#color_secondary"><code>nb&nbsp;set&nbsp;color_secondary</code></a>
  </sup>
</p>

`nb` uses color to highlight various interface elements, including
ids and [selectors](#-selectors),
the current notebook name,
the shell prompt,
divider lines,
[syntax elements](#terminal-syntax-highlighting-theme),
and links.

`nb` includes several built-in color themes
and also supports user-defined themes.
The current color theme can be set using [`nb set color_theme`](#color_theme):

```bash
nb set color_theme
```

#### Built-in Color Themes

##### `blacklight`

| ![blacklight](https://xwmx.github.io/misc/nb/images/nb-theme-blacklight-home.png) | ![blacklight](https://xwmx.github.io/misc/nb/images/nb-theme-blacklight-web.png)  |
|:--:|:--:|
|    |    |

##### `console`

| ![console](https://xwmx.github.io/misc/nb/images/nb-theme-console-home.png)       | ![console](https://xwmx.github.io/misc/nb/images/nb-theme-console-web.png)        |
|:--:|:--:|
|    |    |

##### `desert`

| ![desert](https://xwmx.github.io/misc/nb/images/nb-theme-desert-home.png)         | ![desert](https://xwmx.github.io/misc/nb/images/nb-theme-desert-web.png)          |
|:--:|:--:|
|    |    |

##### `electro`

| ![electro](https://xwmx.github.io/misc/nb/images/nb-theme-electro-home.png)       | ![electro](https://xwmx.github.io/misc/nb/images/nb-theme-electro-web.png)        |
|:--:|:--:|
|    |    |

##### `forest`

| ![forest](https://xwmx.github.io/misc/nb/images/nb-theme-forest-home.png)         | ![forest](https://xwmx.github.io/misc/nb/images/nb-theme-forest-web.png)          |
|:--:|:--:|
|    |    |

##### `nb` (default)

| ![nb](https://xwmx.github.io/misc/nb/images/nb-theme-nb-home.png)                 | ![nb](https://xwmx.github.io/misc/nb/images/nb-theme-nb-web.png)                  |
|:--:|:--:|
|    |    |

##### `ocean`

| ![ocean](https://xwmx.github.io/misc/nb/images/nb-theme-ocean-home.png)           | ![ocean](https://xwmx.github.io/misc/nb/images/nb-theme-ocean-web.png)            |
|:--:|:--:|
|    |    |

##### `raspberry`

| ![raspberry](https://xwmx.github.io/misc/nb/images/nb-theme-raspberry-home.png)   | ![raspberry](https://xwmx.github.io/misc/nb/images/nb-theme-raspberry-web.png)    |
|:--:|:--:|
|    |    |

##### `smoke`

| ![smoke](https://xwmx.github.io/misc/nb/images/nb-theme-monochrome-home.png)      | ![smoke](https://xwmx.github.io/misc/nb/images/nb-theme-smoke-web.png)            |
|:--:|:--:|
|    |    |

##### `unicorn`

| ![unicorn](https://xwmx.github.io/misc/nb/images/nb-theme-unicorn-home.png)       | ![unicorn](https://xwmx.github.io/misc/nb/images/nb-theme-unicorn-web.png)        |
|:--:|:--:|
|    |    |

##### `utility`

| ![utility](https://xwmx.github.io/misc/nb/images/nb-theme-utility-home.png)       | ![utility](https://xwmx.github.io/misc/nb/images/nb-theme-utility-web.png)        |
|:--:|:--:|
|    |    |

#### Custom Color Themes

Color themes are
[`nb` plugins](#-plugins) with a `.nb-theme` file extension.
`.nb-theme` files are expected to contain one `if` statement
testing for the theme name
and setting the color environment variables to `tput` ANSI color numbers:

```bash
# turquoise.nb-theme
if [[ "${NB_COLOR_THEME}" == "turquoise" ]]
then
  export NB_COLOR_PRIMARY=43
  export NB_COLOR_SECONDARY=38
fi
```

View this theme as a complete file:
[`plugins/turquoise.nb-theme`](https://github.com/xwmx/nb/blob/master/plugins/turquoise.nb-theme)

Themes can be installed using [`nb plugins`](#plugins):

```bash
❯ nb plugins install https://github.com/xwmx/nb/blob/master/plugins/turquoise.nb-theme
Plugin installed:
/home/example/.nb/.plugins/turquoise.nb-theme
```

Once a theme is installed,
use [`nb set color_theme`](#color_theme) to set it as the current theme:

```bash
❯ nb set color_theme turquoise
NB_COLOR_THEME set to turquoise
```

The primary and secondary colors can also be overridden individually,
making color themes easily customizable:

```bash
# open the settings prompt for the primary color
nb set color_primary

# open the settings prompt for the secondary color
nb set color_secondary
```

To view a table of available colors and numbers, run:

```bash
nb set colors
```

#### Terminal Syntax Highlighting Theme

`nb` displays files with syntax highlighting when
[`bat`](https://github.com/sharkdp/bat),
[`highlight`](http://www.andre-simon.de/doku/highlight/en/highlight.php),
or
[Pygments](https://pygments.org/)
is installed.

When `bat` is installed, syntax highlighting
color themes are available for both light and dark terminal backgrounds.
To view a list of available themes
and set the syntax highlighting color theme,
use [`nb set syntax_theme`](#syntax_theme).

#### GUI Web Syntax Highlighting

Syntax highlighting is also available when
viewing and editing items in text formats with
[`nb browse --gui`](#browse---gui),
which incorporates the color theme's primary color into the syntax theme:

<p align="center">
  <img  src="https://xwmx.github.io/misc/nb/images/nb-web-pandoc-ruby-utility.png"
        alt="nb syntax highlighting"
        width="500">
</p>

#### Indicators

`nb` uses emoji characters to represent information about files in lists.
These characters are referred to internally as "indicators"
and can be customized by assigning a different character to
the indicator's environment variable in your `~/.nbrc` file,
which can be opened with [`nb settings edit`](#settings).

For example, to use a different indicator for pinned items,
add a line like the following to your `~/.nbrc` file:

```bash
export NB_INDICATOR_PINNED="✨"
```

To turn off an indicator, assign the variable to an empty string:

```bash
export NB_INDICATOR_PINNED=""
```

Available indicator variables with default values:

```bash
export  NB_INDICATOR_AUDIO="🔉"
export  NB_INDICATOR_BOOKMARK="🔖"
export  NB_INDICATOR_DOCUMENT="📄"
export  NB_INDICATOR_EBOOK="📖"
export  NB_INDICATOR_ENCRYPTED="🔒"
export  NB_INDICATOR_FOLDER="📂"
export  NB_INDICATOR_IMAGE="🌄"
export  NB_INDICATOR_PINNED="📌"
export  NB_INDICATOR_TODO="✔️ "
export  NB_INDICATOR_TODO_DONE="✅"
export  NB_INDICATOR_VIDEO="📹"
```

### $ Shell Theme Support

- [`astral` Zsh Theme](https://github.com/xwmx/astral) - Displays the
    current notebook name in the context line of the prompt.

### 🔌 Plugins

<p>
  <sup>
    <a href="#overview">↑</a> ·
    <a href="#plugin-help">Plugin Help</a>,
    <a href="#plugins"><code>nb plugins</code></a>
  </sup>
</p>

`nb` includes support for plugins, which can be used to create new
subcommands, design themes, and otherwise extend the functionality of `nb`.

`nb` supports two types of plugins, identified by their file extensions:

<dl>
  <dt><code>.nb-theme</code></dt>
  <dd>Plugins defining <a href="#custom-color-themes">color themes</a>.</dd>
  <dt><code>.nb-plugin</code></dt>
  <dd>Plugins defining new subcommands and adding functionality.</dd>
</dl>

Plugins are managed with the [`nb plugins`](#plugins) subcommand and
are installed in the `${NB_DIR}/.plugins` directory.

Plugins can be installed from either a URL or a path using the
[`nb plugins install`](#plugins) subcommand.

```bash
# install a plugin from a URL
nb plugins install https://raw.githubusercontent.com/xwmx/nb/master/plugins/clip.nb-plugin

# install a plugin from a standard GitHub URL
nb plugins install https://github.com/xwmx/nb/blob/master/plugins/example.nb-plugin

# install a theme from a standard GitHub URL
nb plugins install https://github.com/xwmx/nb/blob/master/plugins/turquoise.nb-theme

# install a plugin from a path
nb plugins install plugins/example.nb-plugin
```

The `<url>` should be the full URL to the plugin file.
`nb` also recognizes regular GitHub URLs,
which can be used interchangeably with raw GitHub URLs.

Installed plugins can be listed with [`nb plugins`](#plugins),
which optionally takes a name and prints full paths:

```bash
❯ nb plugins
clip.nb-plugin
example.nb-plugin
turquoise.nb-theme

❯ nb plugins clip.nb-plugin
clip.nb-plugin

❯ nb plugins --paths
/home/example/.nb/.plugins/clip.nb-plugin
/home/example/.nb/.plugins/example.nb-plugin
/home/example/.nb/.plugins/turquoise.nb-theme

❯ nb plugins turquoise.nb-theme --paths
/home/example/.nb/.plugins/turquoise.nb-theme
```

Use [`nb plugins uninstall`](#plugins) to uninstall a plugin:

```bash
❯ nb plugins uninstall example.nb-plugin
Plugin successfully uninstalled:
/home/example/.nb/.plugins/example.nb-plugin
```

#### Creating Plugins

Plugins are written in a Bash-compatible shell scripting language
and have an `.nb-plugin` extension.

`nb` includes a few example plugins:

- [`example.nb-plugin`](https://github.com/xwmx/nb/blob/master/plugins/example.nb-plugin)
- [`clip.nb-plugin`](https://github.com/xwmx/nb/blob/master/plugins/clip.nb-plugin)
- [`ebook.nb-plugin`](https://github.com/xwmx/nb/blob/master/plugins/ebook.nb-plugin)

Create a new subcommand in three easy steps:

##### 1. Add the new subcommand name with `_subcommands add <name>`:

```bash
_subcommands add "example"
```

##### 2. Define help and usage text with `_subcommands describe <subcommand> <usage>`:

```bash
_subcommands describe "example" <<HEREDOC
Usage:
  nb example

Description:
  Print "Hello, World!"
HEREDOC
```

##### 3. Define the subcommand as a function, named with a leading underscore:

```bash
_example() {
  printf "Hello, World!\\n"
}
```

That's it! 🎉

View the complete plugin:
[`plugins/example.nb-plugin`](https://github.com/xwmx/nb/blob/master/plugins/example.nb-plugin)

With `example.nb-plugin` installed, `nb` includes an `nb example` subcommand
that prints "Hello, World!"

For a full example,
[`clip.nb-plugin`](https://github.com/xwmx/nb/blob/master/plugins/clip.nb-plugin)
add clipboard functionality to `nb` and demonstrates how to create a
plugin using `nb` subcommands and simple shell scripting.

You can install any plugin you create locally with
[`nb plugins install <path>`](#plugins),
and you can publish it on GitHub, GitLab,
or anywhere else online and install it with
[`nb plugins install <url>`](#plugins).

#### API

The `nb` API is the [command line interface](#nb-help), which is designed for
composability and provides a variety of powerful options for interacting with
notes, bookmarks, notebooks, and `nb` functionality. Within plugins,
subcommands can be called using their function names, which are named with
leading underscores. Options can be used to output information in formats
suitable for parsing and processing:

```bash
# print the content of note 3 to standard output with no color
_show 3 --print --no-color

# list all unarchived global notebook names
_notebooks --names --no-color --unarchived --global

# list all filenames in the current notebook
_list --filenames --no-id --no-indicator

# print the path to the current notebook
_notebooks current --path
```

`nb` automatically scans arguments for
[selectors](#-selectors) with notebook names
and updates the current notebook if a valid one is found.

Identifier selectors are passed to subcommands as arguments along with
any subcommand options. Use [`show <selector>`](#show) to query
information about the file specified in the selector. For example, to
obtain the filename of a selector-specified file, use
[`show <selector> --filename`](#show):

```bash
_example() {
  local _selector="${1:-}"
  [[ -z "${_selector:-}" ]] && printf "Usage: example <selector>\\n" && exit 1

  # Get the filename using the selector.
  local _filename=
  _filename="$(_show "${_selector}" --filename)"

  # Rest of subcommand function...
}
```

[`notebooks current --path`](#notebooks) returns the path to the current
notebook:

```bash
# _example() continued:

# get the notebook path
local _notebook_path=
_notebook_path="$(_notebooks current --path)"

# print the file at "${_notebook_path}/${_filename}" to standard output
cat "${_notebook_path}/${_filename}"
```

See
[`clip.nb-plugin`](https://github.com/xwmx/nb/blob/master/plugins/clip.nb-plugin)
for a practical example using both [`show <selector>`](#show) and
[`notebooks current --path`](#notebooks) along with other
subcommands called using their underscore-prefixed function names.

### `:/` Selectors

<p>
  <sup>
    <a href="#overview">↑</a>
  </sup>
</p>

Items in `nb` are primarily identified using structured arguments called
"selectors." Selectors are like addresses for notebooks, folders, and items.
A selector can be as simple as an id like `123` or folder path like `example/`,
or it can combine multiple elements to identify
an item in a nested folder within a particular notebook, such as:

```bash
cli:tools/shellcheck/home-page.bookmark.md
```

An item, folder, or notebook selector is constructed by specifying the
notebook name, folder path, and / or item identifier
in the following pattern:

```text
notebook:folder/path/item-idenitifer
```

Represented in a [docopt](http://docopt.org/)-like format:

```text
[<notebook>:][<folder-path>/][<id> | <filename> | <title>]
```

Notebooks are identified by the notebook name followed by a colon.
Folder and item identifiers without a notebook name refer to
items within the current notebook.
When a selector consists of notebook name and colon
with no folder path or item identifer,
the command runs in the root folder of the notebook:

```bash
# list items in the "example" notebook
nb example:

# add a new note named "Example Title" to the "example" notebook
nb add example: --title "Example Title"

# edit item with id "123" in the notebook "example"
nb edit example:123
```

A notebook selector can be combined with a subcommand name to
run the command within the notebook:

```bash
# list all items in the "example" notebook and display excerpts
nb example:list -e

# edit item with id "123" in the "example" notebook
nb example:edit 123

# show the git history for the notebook named "example"
nb example:history
```

Folders are identified by relative path from the notebook root.
Folders can be referenced by either id or name, and segments
in nested paths can mix and match names and ids:

```bash
# list items in the folder named "sample" in the folder named demo"
nb sample/demo/

# add a new item to the folder named "demo" in the folder with id "3"
nb add 3/demo/

# show the history of the folder with id "4" in the folder named
# "sample" in the notebook named "example"
nb history example:sample/4/
```

A trailing slash indicates that the command is expected to operate on
the contents of the folder. When a trailing slash is omitted, the
selector refers to the folder itself:

```bash
❯ nb list sample
[1] 📂 sample

❯ nb list sample/
[sample/3] Title Three
[sample/2] Title Two
[sample/1] Title One
```

For more information about folders, see [Folders](#-folders).

An item is identified by id, filename, or title, optionally preceeded by
notebook name or folder path:

```bash
# edit item with id "123"
nb edit 123

# open the item titled "demo title" in the folder with id "3"
nb open 3/demo\ title

# show "file.md" in the "sample" folder in the "example" notebook
nb show example:sample/file.md
```

Items can also be specified using the full path:

```bash
# edit "demo.md" in the "sample" folder in the "home" notebook
nb edit /home/example/.nb/home/sample/demo.md
```

##### Examples

*Idenitifer Selectors*

```text
123
example.md
title
relative/path/to/123
relative/path/to/demo.md
relative/path/to/title
/full/path/to/sample.md
notebook:123
notebook:example.md
notebook:title
notebook:relative/path/to/123
notebook:relative/path/to/demo.md
notebook:relative/path/to/title
```

*Subcommand Selectors*

```text
notebook:
notebook:show
notebook:history
notebook:a
notebook:q
```

### `01` Metadata

<p>
  <sup>
    <a href="#overview">↑</a> ·
    <a href="#show"><code>nb show</code></a>
  </sup>
</p>

Metadata in `nb` is primarily derived from git, the filesystem, and file
content. For example, displayed timestamps are derived from
[`git log`](https://git-scm.com/docs/git-log), with [`nb show --added`](#show)
displaying the datetime of the first commit containing the file and
[`nb show --updated`](#show) displaying the datetime of the last commit in
which the file was modified. Meanwhile, the file system's modified
timestamp is used for sorting.

`nb` also uses plain text files to store ids and state information in
git, including
[`.index` files](https://github.com/xwmx/nb#index-files),
[`.pindex` files](https://github.com/xwmx/nb#pindex-files),
and [`.archived` files](https://github.com/xwmx/nb#archived-notebooks).

#### Front Matter

User-defined metadata can be added to notes in `nb` using [front
matter](https://jekyllrb.com/docs/front-matter/). Front matter is a
simple, human accessible, and future-friendly method for defining metadata
fields in plain text and is well supported in tools for working with
Markdown.

Front matter is defined within a Markdown file with triple-dashed lines
(`---`) indicating the start and end of the block, with each field represented
by a key name with a colon followed by the value:

```markdown
---
title:  Example Title
author: xwmx
year:   2021
---

Example content.

More example content:

- one
- two
- three
```

Any metadata can be placed in the front matter block. `nb` uses the
`title:` field for listing, filtering, and selecting items, if one is
present, and ignores any other fields.

The simple `key: value` syntax is suitable for many metadata fields.
More complex data can be defined using additional
[YAML](https://en.wikipedia.org/wiki/YAML)
capabilities.

### `❯` Interactive Shell

<p>
  <sup>
    <a href="#overview">↑</a> ·
    <a href="#shell"><code>nb shell</code></a>
  </sup>
</p>

`nb` has an interactive shell that can be started with
[`nb shell`](#shell), [`nb -i`](#nb-help), or [`nb --interactive`](#nb-help):

```bash
$ nb shell
__          _
\ \   _ __ | |__
 \ \ | '_ \| '_ \
 / / | | | | |_) |
/_/  |_| |_|_.__/
------------------
nb shell started. Enter ls to list notes and notebooks.
Enter help for usage information. Enter exit to exit.
nb❯ ls
home
----
[3] Example
[2] Sample
[1] Demo

nb❯ edit 3 --content "New content."
Updated: [3] Example

nb❯ bookmark https://example.com
Added: [4] 🔖 example.bookmark.md "Example Title (example.com)"

nb❯ ls
home
----
[4] 🔖 Example Title (example.com)
[3] Example
[2] Sample
[1] Demo

nb❯ bookmark url 4
https://example.com

nb❯ search "example"
[4] example.bookmark.md "Example (example.com)"
-----------------------------------------------
1:# Example (example.com)

3:<https://example.com>

[3] example.md "Example"
------------------------
1:# Example

nb❯ exit
$
```

The `nb` shell recognizes all `nb` subcommands and options,
providing a streamlined, distraction-free approach for working with `nb`.

### Shortcut Aliases

<p>
  <sup>
    <a href="#overview">↑</a>
  </sup>
</p>

Several core `nb` subcommands have shortcut aliases to make
them faster to work with:

```bash
# `a` (add): add a new note named "example.md"
nb a example.md

# `+` (add): add a new note titled "Example Title"
nb + --title "Example Title"

# `b` (browse): open the folder named "sample" in the web browser
nb b sample/

# `o` (open): open the URL from bookmark 12 in your web browser
nb o 12

# `p` (peek): open the URL from bookmark 6 in your terminal browser
nb p 6

# `e` (edit): edit note 5
nb e 5

# `d` (delete): delete note 19
nb d 19

# `d` (delete): delete note 123 in the notebook named "example:"
nb - example:123

# `s` (show): show note 27
nb s 27

# `q` (search): search notes for "example query"
nb q "example query"

# `h` (help): display the help information for the `add` subcommand
nb h add

# `u` (use): switch to example-notebook
nb u example-notebook
```

For more commands and options, run
[`nb help`](#nb-help) or
[`nb help <subcommand>`](#subcommands)

<p align="center">
  <img  src="https://xwmx.github.io/misc/nb/images/gui-browse-themes.png"
        alt="nb browse themes"
        width="700">
</p>

### Help

<p align="center">
  <a href="#nb-help">nb</a>&nbsp;·
  <a href="#bookmark-help">bookmark</a>&nbsp;·
  <a href="#subcommands">subcommands</a>&nbsp;·
  <a href="#plugin-help">plugins</a>
</p>

<p align="center">
  <a href="#add">add</a>&nbsp;·
  <a href="#archive">archive</a>&nbsp;·
  <a href="#bookmark">bookmark</a>&nbsp;·
  <a href="#browse">browse</a>&nbsp;·
  <a href="#completions">completions</a>&nbsp;·
  <a href="#copy">copy</a>&nbsp;·
  <a href="#count">count</a>&nbsp;·
  <a href="#delete">delete</a>&nbsp;·
  <a href="#do">do</a>&nbsp;·
  <a href="#edit">edit</a>&nbsp;·
  <a href="#env">env</a>&nbsp;·
  <a href="#export">export</a>&nbsp;·
  <a href="#folders">folders</a>&nbsp;·
  <a href="#git">git</a>&nbsp;·
  <a href="#help-1">help</a>&nbsp;·
  <a href="#history">history</a>&nbsp;·
  <a href="#import">import</a>&nbsp;·
  <a href="#init">init</a>&nbsp;·
  <a href="#list">list</a>&nbsp;·
  <a href="#ls">ls</a>&nbsp;·
  <a href="#move">move</a>&nbsp;·
  <a href="#notebooks">notebooks</a>&nbsp;·
  <a href="#open">open</a>&nbsp;·
  <a href="#peek">peek</a>&nbsp;·
  <a href="#pin">pin</a>&nbsp;·
  <a href="#plugins">plugins</a>&nbsp;·
  <a href="#remote">remote</a>&nbsp;·
  <a href="#run">run</a>&nbsp;·
  <a href="#search">search</a>&nbsp;·
  <a href="#settings">settings</a>&nbsp;·
  <a href="#shell">shell</a>&nbsp;·
  <a href="#show">show</a>&nbsp;·
  <a href="#status">status</a>&nbsp;·
  <a href="#subcommands-1">subcommands</a>&nbsp;·
  <a href="#sync">sync</a>&nbsp;·
  <a href="#tasks">tasks</a>&nbsp;·
  <a href="#todo">todo</a>&nbsp;·
  <a href="#unarchive">unarchive</a>&nbsp;·
  <a href="#undo">undo</a>&nbsp;·
  <a href="#unpin">unpin</a>&nbsp;·
  <a href="#unset">unset</a>&nbsp;·
  <a href="#update">update</a>&nbsp;·
  <a href="#use">use</a>&nbsp;·
  <a href="#version">version</a>
</p>

<p align="center">
  <a href="#overview">&nbsp;↑&nbsp;</a>
</p>

#### `nb help`

[↑](#help) · See also:
[`help`](#help-1)

```text
__          _
\ \   _ __ | |__
 \ \ | '_ \| '_ \
 / / | | | | |_) |
/_/  |_| |_|_.__/

[nb] Command line and local web note-taking, bookmarking, and archiving with
plain text data storage, encryption, filtering and search, pinning, #tagging,
Git-backed versioning and syncing, Pandoc-backed conversion, global and local
notebooks, customizable color themes, [[wiki-style linking]], plugins, and more
in a single portable, user-friendly script.

Help:
  nb help               Display this help information.
  nb help <subcommand>  View help information for <subcommand>.
  nb help --colors      View information about color settings.
  nb help --readme      View the `nb` README file.

Usage:
  nb
  nb [<ls-options>...] [<id> | <filename> | <path> | <title> | <notebook>]
  nb [<url>] [<bookmark options>...]
  nb add [<notebook>:][<folder-path>/][<filename>] [<content>]
         [-b | --browse] [-c <content> | --content <content>] [--edit]
         [-e | --encrypt] [-f <filename> | --filename <filename>]
         [--folder <folder-path>] [--tags <tag1>,<tag2>...]
         [-t <title> | --title <title>] [--type <type>]
  nb add bookmark [<bookmark-options>...]
  nb add folder [<name>]
  nb add todo [<todo-options>...]
  nb archive [<notebook>]
  nb bookmark [<ls-options>...]
  nb bookmark [<notebook>:][<folder-path>/] <url>
              [-c <comment> | --comment <comment>] [--edit] [-e | --encrypt]
              [-f <filename> | --filename <filename>] [--no-request]
              [-q <quote> | --quote <quote>] [--save-source]
              [-r (<url> | <selector>) | --related (<url> | <selector>)]...
              [-t <tag1>,<tag2>... | --tags <tag1>,<tag2>...] [--title <title>]
  nb bookmark [list [<list-options>...]]
  nb bookmark (open | peek | url) (<id> | <filename> | <path> | <title>)
  nb bookmark (edit | delete) (<id> | <filename> | <path> | <title>)
  nb bookmark search <query>
  nb browse [<notebook>:][<folder-path>/][<id> | <filename> | <title>]
            [-g | --gui] [-n | --notebooks] [-p | --print] [-q | --query <query>]
            [-s | --serve] [-t <tag> | --tag <tag> | --tags <tag1>,<tag2>...]
  nb browse add [<notebook>:][<folder-path>/][<filename>]
            [-c <content> | --content <content>] [--tags <tag1>,<tag2>...]
            [-t <title> | --title <title>]
  nb browse delete ([<notebook>:][<folder-path>/][<id> | <filename> | <title>])
  nb browse edit ([<notebook>:][<folder-path>/][<id> | <filename> | <title>])
  nb completions (check | install [-d | --download] | uninstall)
  nb copy ([<notebook>:][<folder-path>/][<id> | <filename> | <title>])
          [[<notebook>:][<folder-path>/]<filename>]
  nb count [<notebook>:][<folder-path>/]
  nb delete ([<notebook>:][<folder-path>/][<id> | <filename> | <title>])...
            [-f | --force]
  nb do ([<notebook>:][<folder-path>/][<id> | <filename> | <title>])
        [<task-number>]
  nb edit ([<notebook>:][<folder-path>/][<id> | <filename> | <title>])
          [-c <content> | --content <content>] [--edit]
          [-e <editor> | --editor <editor>] [--overwrite] [--prepend]
  nb export ([<notebook>:][<folder-path>/][<id> | <filename> | <title>])
            <path> [-f | --force] [<pandoc options>...]
  nb export notebook <name> [<path>]
  nb export pandoc ([<notebook>:][<folder-path>/][<id> | <filename> | <title>])
            [<pandoc options>...]
  nb folders (add | delete) [<notebook>:][<folder-path>/]<folder-name>
  nb folders <list-options>...
  nb git [checkpoint [<message>] | dirty]
  nb git <git-options>...
  nb help [<subcommand>] [-p | --print]
  nb help [-c | --colors] | [-r | --readme] | [-s | --short] [-p | --print]
  nb history [<notebook>:][<folder-path>/][<id> | <filename> | <title>]
  nb import [copy | download | move] (<path>... | <url>) [--convert]
            [<notebook>:][<folder-path>/][<filename>]
  nb import notebook <path> [<name>]
  nb init [<remote-url> [<branch>]] [--author] [--email <email>]
          [--name <name>]
  nb list [-e [<length>] | --excerpt [<length>]] [--filenames]
          [-n <limit> | --limit <limit> | --<limit>] [--no-id]
          [--no-indicator] [-p <number> | --page <number>] [--pager]
          [--paths] [-s | --sort] [-r | --reverse] [--tags]
          [-t <type> | --type <type> | --<type>]
          [<notebook>:][<folder-path>/][<id> | <filename> | <path> | <query>]
  nb ls [-a | --all] [-b | --browse] [-e [<length>] | --excerpt [<length>]]
        [--filenames] [-g | --gui] [-n <limit> | --limit <limit> | --<limit>]
        [--no-footer] [--no-header] [--no-id] [--no-indicator]
        [-p <number> | --page <number>] [--pager] [--paths] [-s | --sort]
        [-r | --reverse] [--tags] [-t <type> | --type <type> | --<type>]
        [<notebook>:][<folder-path>/][<id> | <filename> | <path> | <query>]
  nb move ([<notebook>:][<folder-path>/][<id> | <filename> | <title>])
          ([<notebook>:][<path>] | --reset | --to-bookmark | --to-note |
          --to-title | --to-todo) [-f | --force]
  nb notebooks [<name> | <query>] [--ar | --archived] [--global] [--local]
               [--names] [--paths] [--unar | --unarchived]
  nb notebooks add ([<name>] [<remote-url> [<branch>... | --all]]) [--author]
                   [--email <email>] [--name <name>]
  nb notebooks (archive | open | peek | status | unarchive) [<name>]
  nb notebooks author [<name> | <path>] [--email <email>] [--name <name>]
  nb notebooks current [--path | --selected | --filename [<filename>]]
                       [--global | --local]
  nb notebooks delete <name> [-f | --force]
  nb notebooks (export <name> [<path>] | import <path>)
  nb notebooks init [<path> [<remote-url> [<branch>]]] [--author]
                    [--email <email>] [--name <name>]
  nb notebooks rename <old-name> <new-name>
  nb notebooks select <selector>
  nb notebooks show (<name> | <path> | <selector>) [--ar | --archived]
                    [--escaped | --name | --path | --filename [<filename>]]
  nb notebooks use <name>
  nb open ([<notebook>:][<folder-path>/][<id> | <filename> | <title>])
  nb peek ([<notebook>:][<folder-path>/][<id> | <filename> | <title>])
  nb pin  ([<notebook>:][<folder-path>/][<id> | <filename> | <title>])
  nb plugins [<name>] [--paths]
  nb plugins install [<path> | <url>] [--force]
  nb plugins uninstall <name> [--force]
  nb remote [branches [<url>] | remove | rename [<branch-name>] <name>]
  nb remote [delete <branch-name> | reset <branch-name>]
  nb remote set <url> [<branch-name>]
  nb run <command> [<arguments>...]
  nb search ([<notebook>:][<folder-path>/][<id> | <filename> | <title>])
            <query>... [-a | --all] [--and <query>] [--or <query>]
            [-l | --list] [--path] [-t <tag1>,<tag2>... | --tag <tag1>,<tag2>...]
            [-t | --tags] [--type <type> | --<type>] [--utility <name>]
  nb set [<name> [<value>] | <number> [<value>]]
  nb settings [colors [<number> | themes] | edit | list [--long]]
  nb settings (get | show | unset) (<name> | <number>)
  nb settings set (<name> | <number>) <value>
  nb shell [<subcommand> [<options>...] | --clear-history]
  nb show ([<notebook>:][<folder-path>/][<id> | <filename> | <title>])
          [[-a | --added] | [--authors] | [-b | --browse] | --filename | --id |
          --info-line | --path | [-p | --print] | --relative-path | [-r |
          --render] | --title | --type [<type>] | [-u | --updated]] [--no-color]
  nb show <notebook>
  nb status [<notebook>]
  nb subcommands [add <name>...] [alias <name> <alias>]
                 [describe <name> <usage>]
  nb sync [-a | --all]
  nb tasks ([<notebook>:][<folder-path>/][<id> | <filename> | <description>])
           [open | closed]
  nb todo add [<notebook>:][<folder-path>/][<filename>] <title>
              [--description <description>] [--due <date>]
              [-r (<url> | <selector>) | --related (<url> | <selector>)]
              [--tags <tag1>,<tag2>...] [--task <title>]...
  nb todo do   ([<notebook>:][<folder-path>/][<id> | <filename> | <description>])
               [<task-number>]
  nb todo undo ([<notebook>:][<folder-path>/][<id> | <filename> | <description>])
               [<task-number>]
  nb todos [<notebook>:][<folder-path>/] [open | closed]
  nb todos tasks ([<notebook>:][<folder-path>/][<id> | <filename> | <description>])
                 [open | closed]
  nb unarchive [<notebook>]
  nb undo ([<notebook>:][<folder-path>/][<id> | <filename> | <title>])
          [<task-number>]
  nb unpin ([<notebook>:][<folder-path>/][<id> | <filename> | <title>])
  nb unset (<name> | <number>)
  nb update
  nb use <notebook>
  nb -h | --help | help [<subcommand> | --readme]
  nb -i | --interactive [<subcommand> [<options>...]]
  nb --no-color
  nb --version | version

Subcommands:
  (default)    List notes and notebooks. This is an alias for `nb ls`.
               When a <url> is provided, create a new bookmark.
  add          Add a note, folder, or file.
  archive      Archive the current or specified notebook.
  bookmark     Add, open, list, and search bookmarks.
  browse       Browse and manage linked items in terminal and GUI web browsers.
  completions  Install and uninstall completion scripts.
  copy         Copy or duplicate an item.
  count        Print the number of items in a notebook or folder.
  delete       Delete a note.
  do           Mark a todo or task as done.
  edit         Edit a note.
  export       Export a note to a variety of different formats.
  folders      Add, delete, and list folders.
  git          Run `git` commands within the current notebook.
  help         View help information for the program or a subcommand.
  history      View git history for the current notebook or a note.
  import       Import a file into the current notebook.
  init         Initialize the first notebook.
  list         List notes in the current notebook.
  ls           List notebooks and notes in the current notebook.
  move         Move or rename a note.
  notebooks    Manage notebooks.
  open         Open a bookmarked web page or notebook folder, or edit a note.
  peek         View a note, bookmarked web page, or notebook in the terminal.
  pin          Pin an item so it appears first in lists.
  plugins      Install and uninstall plugins and themes.
  remote       Configure the remote URL and branch for the notebook.
  run          Run shell commands within the current notebook.
  search       Search notes.
  settings     Edit configuration settings.
  shell        Start the `nb` interactive shell.
  show         Show a note or notebook.
  status       Run `git status` in the current notebook.
  subcommands  List, add, alias, and describe subcommands.
  status       Print notebook status information.
  sync         Sync local notebook with the remote repository.
  tasks        List tasks in todos, notebooks, folders, and other items.
  todo         Manage todos and tasks.
  unarchive    Unarchive the current or specified notebook.
  undo         Mark a todo or task as not done.
  unpin        Unpin a pinned item.
  unset        Return a setting to its default value.
  update       Update `nb` to the latest version.
  use          Switch to a notebook.
  version      Display version information.

Notebook Usage:
  nb <notebook>:[<subcommand>] [<identifier>] [<options>...]
  nb <subcommand> <notebook>:<identifier> [<options>...]

Program Options:
  -h, --help          Display this help information.
  -i, --interactive   Start the `nb` interactive shell.
  --no-color          Print without color highlighting.
  --version           Display version information.

More Information:
  https://github.com/xwmx/nb
```

#### `bookmark help`

[↑](#help) · See also:
[Bookmarks](#-bookmarks),
[`bookmark`](#bookmark),
[`browse`](#browse)

```text
    __                __                        __
   / /_  ____  ____  / /______ ___  ____ ______/ /__
  / __ \/ __ \/ __ \/ //_/ __ `__ \/ __ `/ ___/ //_/
 / /_/ / /_/ / /_/ / ,< / / / / / / /_/ / /  / ,<
/_.___/\____/\____/_/|_/_/ /_/ /_/\__,_/_/  /_/|_|

bookmark -- Command line bookmarking with tagging, encryption,
full-text page content search with regular expression support,
GUI and terminal browser support, and data stored in plain text
Markdown files with Git-backed versioning and syncing.

Usage:
  bookmark [<ls-options>...]
  bookmark [<notebook>:][<folder-path>] <url>
              [-c <comment> | --comment <comment>] [--edit] [-e | --encrypt]
              [-f <filename> | --filename <filename>] [--no-request]
              [-q <quote> | --quote <quote>] [--save-source]
              [-r (<url> | <selector>) | --related (<url> | <selector>)]...
              [-t <tag1>,<tag2>... | --tags <tag1>,<tag2>...] [--title <title>]
  bookmark (edit | delete | open | peek | url)
              ([<notebook>:][<folder-path>/][<id> | <filename> | <title>])
  bookmark search <query>

Options:
  -c, --comment <comment>      A comment or description for this bookmark.
  --edit                       Open the bookmark in your editor before saving.
  -e, --encrypt                Encrypt the bookmark with a password.
  -f, --filename <filename>    The filename for the bookmark. It is
                               recommended to omit the extension so the
                               default bookmark extension is used.
  --no-request                 Don't request or download the target page.
  -q, --quote <quote>          A quote or excerpt from the saved page.
                               Alias: `--excerpt`
  -r, --related <selector>     A selector for an item related to the
                               bookmarked page.
  -r, --related <url>          A URL for a page related to the bookmarked page.
                               Multiple `--related` flags can be used in a
                               command to save multiple related URLs.
  --save-source                Save the page source as HTML.
  -t, --tags <tag1>,<tag2>...  A comma-separated list of tags.
  --title <title>              The bookmark title. When not specified,
                               `nb` will use the html <title> tag.

Subcommands:
  (default)  Add a new bookmark for <url>, or list bookmarks.
             Bookmarks can also be added with `nb <url>`
  delete     Delete a bookmark.
  edit       Edit a bookmark.
  list       List bookmarks in the current notebook.
             Shortcut Alias: `ls`
  open       Open the bookmarked page in your system's primary web browser.
             Shortcut Alias: `o`
  peek       Open the bookmarked page in your terminal web browser.
             Alias: `preview`
             Shortcut Alias: `p`
  search     Search bookmarks for <query>.
             Shortcut Alias: `q`
  url        Print the URL for the specified bookmark.

Description:
  Create, view, search, edit, and delete bookmarks.

  By default, the html page content is saved within the bookmark, making the
  bookmarked page available for full-text search. When Pandoc [1] is
  installed, the HTML content is converted to Markdown before saving.
  When readability-cli [2] is install, markup is cleaned up to focus on
  content.

  `peek` opens the page in `w3m` [3] or `links` [4] when available.
  To specify a preferred browser, set the `$BROWSER` environment variable
  in your .bashrc, .zshrc, or equivalent, e.g.: export BROWSER="lynx"

  Bookmarks are identified by the `.bookmark.md` file extension. The
  bookmark URL is the first URL in the file within "<" and ">" characters:

    <https://www.example.com>

    1. https://pandoc.org/
    2. https://gitlab.com/gardenappl/readability-cli
    3. https://en.wikipedia.org/wiki/W3m
    4. https://en.wikipedia.org/wiki/Links_(web_browser)

Read More:
  https://github.com/xwmx/nb#-bookmarks

See Also:
  nb help browse
  nb help open
  nb help peek
  nb help show

Examples:
  bookmark https://example.com
  bookmark https://example.com --encrypt
  bookmark https://example.com --tags example,sample,demo
  bookmark https://example.com/about -c "Example comment."
  bookmark https://example.com/faqs -f example-filename
  bookmark https://example.com --quote "Example quote or excerpt."
  bookmark list
  bookmark search "example query"
  bookmark open 5

------------------------------------------
Part of `nb` (https://github.com/xwmx/nb).
For more information, see: `nb help`.
```

### Subcommands

<p align="center">
  <a href="#add">add</a>&nbsp;·
  <a href="#archive">archive</a>&nbsp;·
  <a href="#bookmark">bookmark</a>&nbsp;·
  <a href="#browse">browse</a>&nbsp;·
  <a href="#completions">completions</a>&nbsp;·
  <a href="#copy">copy</a>&nbsp;·
  <a href="#count">count</a>&nbsp;·
  <a href="#delete">delete</a>&nbsp;·
  <a href="#do">do</a>&nbsp;·
  <a href="#edit">edit</a>&nbsp;·
  <a href="#env">env</a>&nbsp;·
  <a href="#folders">folders</a>&nbsp;·
  <a href="#export">export</a>&nbsp;·
  <a href="#git">git</a>&nbsp;·
  <a href="#help-1">help</a>&nbsp;·
  <a href="#history">history</a>&nbsp;·
  <a href="#import">import</a>&nbsp;·
  <a href="#init">init</a>&nbsp;·
  <a href="#list">list</a>&nbsp;·
  <a href="#ls">ls</a>&nbsp;·
  <a href="#move">move</a>&nbsp;·
  <a href="#notebooks">notebooks</a>&nbsp;·
  <a href="#open">open</a>&nbsp;·
  <a href="#peek">peek</a>&nbsp;·
  <a href="#pin">pin</a>&nbsp;·
  <a href="#plugins">plugins</a>&nbsp;·
  <a href="#remote">remote</a>&nbsp;·
  <a href="#run">run</a>&nbsp;·
  <a href="#search">search</a>&nbsp;·
  <a href="#settings">settings</a>&nbsp;·
  <a href="#shell">shell</a>&nbsp;·
  <a href="#show">show</a>&nbsp;·
  <a href="#status">status</a>&nbsp;·
  <a href="#subcommands-1">subcommands</a>&nbsp;·
  <a href="#sync">sync</a>&nbsp;·
  <a href="#tasks">tasks</a>&nbsp;·
  <a href="#todo">todo</a>&nbsp;·
  <a href="#unarchive">unarchive</a>&nbsp;·
  <a href="#undo">undo</a>&nbsp;·
  <a href="#unpin">unpin</a>&nbsp;·
  <a href="#unset">unset</a>&nbsp;·
  <a href="#update">update</a>&nbsp;·
  <a href="#use">use</a>&nbsp;·
  <a href="#version">version</a>
</p>

<p align="center">
  <a href="#overview">&nbsp;↑&nbsp;</a>
</p>

#### `add`

[↑](#help) · See also:
[Adding](#adding),
[`bookmark`](#bookmark),
[`browse`](#browse),
[`delete`](#delete),
[`edit`](#edit),
[`folders`](#folders),
[`import`](#import),
[`show`](#show),
[`todo`](#todo)

```text
Usage:
  nb add [<notebook>:][<folder-path>/][<filename>] [<content>]
         [-b | --browse] [-c <content> | --content <content>] [--edit]
         [-e | --encrypt] [-f <filename> | --filename <filename>]
         [--folder <folder-path>] [--tags <tag1>,<tag2>...]
         [-t <title> | --title <title>] [--type <type>]
  nb add bookmark [<bookmark-options>...]
  nb add folder [<name>]
  nb add todo [<todo-options>...]

Options:
  -b, --browse                Add using a terminal or GUI web browser.
  -c, --content <content>     The content for the new note.
  --edit                      Open the note in the editor before saving when
                              content is piped or passed as an argument.
  -e, --encrypt               Encrypt the note with a password.
  -f, --filename <filename>   The filename for the new note.
  --folder <folder-path>      Add within the folder located at <folder-path>.
  --tags <tag1>,<tag2>...     A comma-separated list of tags.
  -t, --title <title>         The title for a new note. If `--title` is
                              present, the filename is derived from the
                              title, unless `--filename` is specified.
  --type <type>               The file type for the new note, as a file
                              extension.

Description:
  Create a new note or folder.

  If no arguments are passed, a new blank note file is opened with `$EDITOR`,
  currently set to: example

  If a non-option argument is passed, `nb` will treat it as a <filename≥
  if a file extension is found. If no file extension is found,  `nb` will
  treat the string as <content> and will create a new note without opening the
  editor. `nb add` can also create a new note with piped content.

  `nb` creates Markdown files by default. To create a note with a
  different file type, use the extension in the filename or use the `--type`
  option. To change the default file type, use `nb set default_extension`.

  When the `-e` / `--encrypt` option is used, `nb` will encrypt the
  note with AES-256 using OpenSSL by default, or GPG, if configured in
  `nb set encryption_tool`.

Read More:
  https://github.com/xwmx/nb#adding

See Also:
  nb help bookmark
  nb help browse
  nb help delete
  nb help edit
  nb help folders
  nb help import
  nb help show
  nb help todo

Examples:
  nb add
  nb add example.md
  nb add "Note content."
  nb add example.md --title "Example Title" --content "Example content."
  echo "Note content." | nb add
  nb add -t "Secret Document" --encrypt
  nb add example/document.md
  nb add folder sample/demo
  nb example:add
  nb example:add -t "Title"
  nb a
  nb a "Note content."
  nb example:a
  nb example:a -t "Title"

Aliases:
  nb create
  nb new

Shortcut Aliases:
  nb a
  nb +
```

#### `archive`

[↑](#help) · See also:
[Archiving Notebooks](#archiving-notebooks),
[`notebooks`](#notebooks),
[`status`](#status),
[`unarchive`](#unarchive)

```text
Usage:
  nb archive [<name>]

Description:
  Set the current notebook or notebook <name> to "archived" status.

  This is an alias for `nb notebooks archive`.

Read More:
  https://github.com/xwmx/nb#archiving-notebooks

See Also:
  nb help notebooks
  nb help status
  nb help unarchive

Examples:
  nb archive
  nb archive example

Shortcut Alias:
  nb ar
```

#### `bookmark`

[↑](#help) · See also:
[Bookmarks](#-bookmarks),
[`browse`](#browse),
[`open`](#open),
[`peek`](#peek),
[`show`](#show)

```text
Usage:
  nb bookmark [<ls-options>...]
  nb bookmark [<notebook>:][<folder-path>/] <url>
              [-c <comment> | --comment <comment>] [--edit] [-e | --encrypt]
              [-f <filename> | --filename <filename>] [--no-request]
              [-q <quote> | --quote <quote>] [--save-source]
              [-r (<url> | <selector>) | --related (<url> | <selector>)]...
              [-t <tag1>,<tag2>... | --tags <tag1>,<tag2>...] [--title <title>]
  nb bookmark list [<list-options>...]
  nb bookmark (edit | delete | open | peek | url)
              ([<notebook>:][<folder-path>/][<id> | <filename> | <title>])
  nb bookmark search <query>

Options:
  -c, --comment <comment>      A comment or description for this bookmark.
  --edit                       Open the bookmark in your editor before saving.
  -e, --encrypt                Encrypt the bookmark with a password.
  -f, --filename <filename>    The filename for the bookmark. It is
                               recommended to omit the extension so the
                               default bookmark extension is used.
  --no-request                 Don't request or download the target page.
  -q, --quote <quote>          A quote or excerpt from the saved page.
                               Alias: `--excerpt`
  -r, --related <selector>     A selector for an item related to the
                               bookmarked page.
  -r, --related <url>          A URL for a page related to the bookmarked page.
                               Multiple `--related` flags can be used in a
                               command to save multiple related URLs.
  --save-source                Save the page source as HTML.
  -t, --tags <tag1>,<tag2>...  A comma-separated list of tags.
  --title <title>              The bookmark title. When not specified,
                               `nb` will use the html <title> tag.

Subcommands:
  (default)  Add a new bookmark for <url>, or list bookmarks.
             Bookmarks can also be added with `nb <url>`
  delete     Delete a bookmark.
  edit       Edit a bookmark.
  list       List bookmarks in the current notebook.
             Shortcut Alias: `ls`
  open       Open the bookmarked page in your system's primary web browser.
             Shortcut Alias: `o`
  peek       Open the bookmarked page in your terminal web browser.
             Alias: `preview`
             Shortcut Alias: `p`
  search     Search bookmarks for <query>.
             Shortcut Alias: `q`
  url        Print the URL for the specified bookmark.

Description:
  Create, view, search, edit, and delete bookmarks.

  By default, the html page content is saved within the bookmark, making the
  bookmarked page available for full-text search. When Pandoc [1] is
  installed, the HTML content is converted to Markdown before saving.
  When readability-cli [2] is install, markup is cleaned up to focus on
  content.

  `peek` opens the page in `w3m` [3] or `links` [4] when available.
  To specify a preferred browser, set the `$BROWSER` environment variable
  in your .bashrc, .zshrc, or equivalent, e.g.: export BROWSER="lynx"

  Bookmarks are identified by the `.bookmark.md` file extension. The
  bookmark URL is the first URL in the file within "<" and ">" characters:

    <https://www.example.com>

    1. https://pandoc.org/
    2. https://gitlab.com/gardenappl/readability-cli
    3. https://en.wikipedia.org/wiki/W3m
    4. https://en.wikipedia.org/wiki/Links_(web_browser)

Read More:
  https://github.com/xwmx/nb#-bookmarks

See Also:
  nb help browse
  nb help open
  nb help peek
  nb help show

Examples:
  nb https://example.com
  nb example: https://example.com
  nb https://example.com --encrypt
  nb https://example.com --tags example,sample,demo
  nb https://example.com/about -c "Example comment."
  nb https://example.com/faqs -f example-filename
  nb https://example.com --quote "Example quote or excerpt."
  nb bookmark list
  nb bookmark search "example query"
  nb bookmark open 5
  nb bk

Shortcut Aliases:
  nb bk
  nb bm
```

#### `browse`

[↑](#help) · See also:
[Browsing](#-browsing),
[Images](#-images),
[Linking](#-linking),
[`add`](#add),
[`delete`](#delete),
[`edit`](#edit),
[`list`](#list),
[`ls`](#ls),
[`open`](#open),
[`peek`](#peek),
[`pin`](#pin),
[`search`](#search),
[`show`](#show)

```text
Usage:
  nb browse [<notebook>:][<folder-path>/][<id> | <filename> | <title>]
            [-g | --gui] [-n | --notebooks] [-p | --print] [-q | --query <query>]
            [-s | --serve] [-t <tag> | --tag <tag> | --tags <tag1>,<tag2>...]
  nb browse add [<notebook>:][<folder-path>/][<filename>]
            [-c <content> | --content <content>] [--tags <tag1>,<tag2>...]
            [-t <title> | --title <title>]
  nb browse delete ([<notebook>:][<folder-path>/][<id> | <filename> | <title>])
  nb browse edit ([<notebook>:][<folder-path>/][<id> | <filename> | <title>])

Subcommands:
  (default)  Open a notebook, folder, or item in the terminal or GUI web browser.
  add        Open the add view in the browser.
             Shortcut Aliases: `a`, `+`
  delete     Open the delete view in the browser.
             Shortcut Aliases: `d`, `-`
  edit       Open the edit view in the browser.
             Shortcut Alias:   `e`

Options:
  -c, --content <content>      Add content to the new note.
  -g, --gui                    Open in the system's primary GUI web browser.
  -n, --notebooks              Browse notebooks.
  -p, --print                  Print to standard output.
  -q, --query <query>          Open to the search results for <query>.
  -s, --serve                  Start the web application server.
  -t, --tag <tag>              Search for a tag.
  --tags <tag1>,<tag2>...      A comma-separated list of tags.
  -t, --title <title>          Add a title to the new note.

Description:
  Browse, view, and edit linked notes, bookmarks, notebooks, folders, and
  other items using terminal and GUI web browsers.

  `browse` includes an embedded web application designed for terminal
  and GUI web browsers that renders [[wiki-style links]] and #tags as
  internal links, providing the ability to browse notes and notebooks,
  as well as seamlessly browse to and from the offsite links in
  bookmarks and notes.

  To link to a note or bookmark from another, include the selector for the
  target item within double square brackets anywhere in the linking document:

    # link to item 123 in the "sample" folder in the "example" notebook
    [[example:sample/123]]

    # link to the item titled "Example Title" in the "demo" notebook
    [[demo:Example Title]]

  `browse` supports `w3m` [1] and `links` [2], and depends on
  `ncat` [3] and `pandoc` [4]:

    1. https://en.wikipedia.org/wiki/W3m
    2. https://en.wikipedia.org/wiki/Links_(web_browser)
    3. https://nmap.org/ncat/
    4. https://pandoc.org/

Read More:
  https://github.com/xwmx/nb#-browsing

See Also:
  nb help add
  nb help delete
  nb help edit
  nb help list
  nb help ls
  nb help open
  nb help peek
  nb help pin
  nb help search
  nb help show
  nb help unpin

Examples:
  nb browse
  nb browse example:
  nb browse Example\ Folder/
  nb browse 123
  nb browse demo:456
  nb br

Shortcut Alias:
  nb b
```

#### `completions`

[↑](#help) · See also:
[Tab Completion](https://github.com/xwmx/nb/tree/master/etc),
[`env`](#env)

```text
Usage:
  nb completions (check | install [-d | --download] | uninstall)

Options:
  -d, --download  Download the completion scripts and install.

Description:
  Manage completion scripts.

Read More:
  https://github.com/xwmx/nb/blob/master/etc/README.md

See Also:
  nb help env
```

#### `copy`

[↑](#help) · See also:
[Moving & Renaming](#-moving--renaming),
[`move`](#move)

```text
Usage:
  nb copy ([<notebook>:][<folder-path>/][<id> | <filename> | <title>])
          [[<notebook>:][<folder-path>/]<filename>]

Description:
  Copy or duplicate an item.

Read More:
  https://github.com/xwmx/nb#-moving--renaming

See Also:
  nb help move

Examples:
  nb copy 321
  nb copy 456 example:
  nb copy sample/demo.md

Alias:
  nb duplicate
```

#### `count`

[↑&nbsp;](#help)

```text
Usage:
  nb count [<notebook>:][<folder-path>/]

Description:
  Print the number of items in the first level of the current notebook,
  <notebook>, or the folder at <folder-path>.
```

#### `delete`

[↑](#help) · See also:
[Deleting](#deleting),
[`add`](#add),
[`browse`](#browse),
[`edit`](#edit),
[`move`](#move),
[`show`](#show)

```text
Usage:
  nb delete ([<notebook>:][<folder-path>/][<id> | <filename> | <title>])...
            [-f | --force]

Options:
  -f, --force   Skip the confirmation prompt.

Description:
  Delete one or more items.

Read More:
  https://github.com/xwmx/nb#deleting

See Also:
  nb help add
  nb help browse
  nb help edit
  nb help move
  nb help show

Examples:
  nb delete 3
  nb delete example.md
  nb delete "A Document Title"
  nb 3 delete --force
  nb example:delete 12
  nb delete example:12
  nb example:12 delete
  nb d 3
  nb 3 d
  nb d example:12
  nb example:12 d

Shortcut Aliases:
  nb d
  nb -
```

#### `do`

[↑](#help) · See also:
[Todos](#-todos),
[Tasks](#%EF%B8%8F-tasks),
[`tasks`](#tasks),
[`todo`](#todo),
[`undo`](#undo)

```text
Usage:
  nb do ([<notebook>:][<folder-path>/][<id> | <filename> | <title>])
        [<task-number>]

Description:
  Mark a todo or task as done.

Read More:
  https://github.com/xwmx/nb#-todos

See Also:
  nb help tasks
  nb help todo
  nb help undo

Examples:
  nb do 123
  nb do example:sample/321
  nb do 543 7
```

#### `edit`

[↑](#help) · See also:
[Editing](#editing),
[`add`](#add),
[`browse`](#browse),
[`delete`](#delete),
[`move`](#move),
[`show`](#show)

```text
Usage:
  nb edit ([<notebook>:][<folder-path>/][<id> | <filename> | <title>])
          [-c <content> | --content <content>] [--edit]
          [-e <editor> | --editor <editor>] [--overwrite] [--prepend]

Options:
  -c, --content <content>  Content to add to the item.
  --edit                   Open the note in the editor before saving when
                           content is piped or passed as an argument.
  -e, --editor <editor>    Edit the note with <editor>, overriding the editor
                           specified in the `$EDITOR` environment variable.
  --overwrite              Overwrite existing content with <content> and
                           standard input.
  --prepend                Prepend <content> and standard input before
                           existing content.

Description:
  Open the specified note in `$EDITOR` or <editor> if specified.
  Content piped to `nb edit` or passed using the `--content` option
  is appended to the file without opening it in the editor,
  unless the `--edit` flag is specified.

  Non-text files are opened in your system's preferred app or program for
  that file type.

Read More:
  https://github.com/xwmx/nb#editing

See Also:
  nb help add
  nb help browse
  nb help delete
  nb help move
  nb help show

Examples:
  nb edit 3
  nb edit example.md
  nb edit "A Document Title"
  echo "Content to append." | nb edit 1
  nb 3 edit
  nb example:edit 12
  nb edit example:12
  nb example:12 edit
  nb e 3
  nb 3 e
  nb e example:12
  nb example:12 e

Shortcut Alias:
  nb e
```

#### `env`

[↑](#help) · See also:
[Installation](#installation),
[`completions`](#completions),
[`init`](#init),
[`update`](#update),
[`version`](#version)

```text
Usage:
  nb env [install]

Subcommands:
  install  Install dependencies on supported systems.

Description:
  Print program environment and configuration information, or install
  dependencies.

Read More:
  https://github.com/xwmx/nb#installation

See Also:
  nb help completions
  nb help init
  nb help update
  nb help version
```

#### `export`

[↑](#help) · See also:
[Import / Export](#%EF%B8%8F-import--export),
[`browse`](#browse),
[`import`](#import)

```text
Usage:
  nb export ([<notebook>:][<folder-path>/][<id> | <filename> | <title>])
            <path> [-f | --force] [<pandoc options>...]
  nb export notebook <name> [<path>]
  nb export pandoc ([<notebook>:][<folder-path>/][<id> | <filename> | <title>])
            [<pandoc options>...]

Options:
  -f, --force   Skip the confirmation prompt when overwriting an existing file.

Subcommands:
  (default)     Export a file to <path>. If <path> has a different extension
                than the source note, convert the note using `pandoc`.
  notebook      Export the notebook <name> to the current directory or <path>.
                Alias for `nb notebooks export`.
  pandoc        Export the file to standard output or a file using `pandoc`.
                `export pandoc` prints to standard output by default.

Description:
  Export a file or notebook.

  If Pandoc [1] is available, convert the note from its current format
  to the format of the output file as indicated by the file extension
  in <path>. Any additional arguments are passed directly to Pandoc.
  See the Pandoc help information for available options.

    1. https://pandoc.org/

Read More:
  https://github.com/xwmx/nb#%EF%B8%8F-import--export

See Also:
  nb help browse
  nb help import

Examples:
  # Export an Org note
  nb export example.org /path/to/example.org

  # Export a Markdown note to HTML and print to standard output
  nb export pandoc example.md --from=markdown_strict --to=html

  # Export a Markdown note to a .docx Microsoft Office Word document
  nb export example.md /path/to/example.docx

  # Export note 12 in the "sample" notebook to HTML
  nb export sample:12 /path/to/example.html
```

#### `folders`

[↑](#help) · See also:
[Folders](#-folders),
[`add`](#add),
[`delete`](#delete),
[`list`](#list),
[`ls`](#ls)

```text
Usage:
  nb folders add [<notebook>:][<folder-path>/]<folder-name>
  nb folders delete [<notebook>:][<folder-path>/]<folder-name>
  nb folders <list-options>...

Subcommands:
  (default)  List folders.
  add        Add a new folder.
  delete     Delete a folder.

Description:
  Add, delete, and list folders.

Read More:
  https://github.com/xwmx/nb#-folders

See Also:
  nb help add
  nb help delete
  nb help list
  nb help ls

Examples:
  nb folders
  nb folders add example
  nb folders delete example:sample

Alias:
  nb folder

Shortcut Alias:
  nb f
```

#### `git`

[↑](#help) · See also:
[Git Sync](#-git-sync),
[History](#-revision-history),
[`history`](#history),
[`remote`](#remote),
[`run`](#run),
[`status`](#status),
[`sync`](#sync)

```text
Usage:
  nb git [checkpoint [<message>] | dirty]
  nb git <git-options>...

Subcommands:
  checkpoint    Create a new git commit in the current notebook and sync with
                the remote if `nb set auto_sync` is enabled.
  dirty         0 (success, true) if there are uncommitted changes in the
                current notebook. 1 (error, false) if the notebook is clean.

Description:
  Run `git` commands within the current notebook directory.

Read More:
  https://github.com/xwmx/nb#-git-sync
  https://github.com/xwmx/nb#-revision-history

See Also:
  nb help history
  nb help remote
  nb help run
  nb help status
  nb help sync

Examples:
  nb git status
  nb git diff
  nb git log
  nb example:git status
```

#### `help`

[↑](#help) · See also:
[`nb help`](#nb-help)

```text
Usage:
  nb help [<subcommand>] [-p | --print]
  nb help [-c | --colors] | [-r | --readme] | [-s | --short] [-p | --print]

Options:
  -c, --colors  View information about color themes and color settings.
  -p, --print   Print to standard output / terminal.
  -r, --readme  View the `nb` README file.
  -s, --short   Print shorter help without subcommand descriptions.

Description:
  Print the program help information. When a subcommand name is passed, print
  the help information for the subcommand.

Examples:
  nb help
  nb help add
  nb help import
  nb h notebooks
  nb h e

Shortcut Alias:
  nb h
```

#### `history`

[↑](#help) · See also:
[History](#-revision-history),
[Git Sync](#-git-sync),
[`git`](#git),
[`remote`](#remote),
[`status`](#status),
[`sync`](#sync)

```text
Usage:
  nb history [<notebook>:][<folder-path>/][<id> | <filename> | <title>]

Description:
  Display notebook history using `tig` [1] (if available) or `git log`.
  When a note is specified, the history for that note is displayed.

    1. https://github.com/jonas/tig

Read More:
  https://github.com/xwmx/nb#-revision-history
  https://github.com/xwmx/nb#-git-sync

See Also:
  nb help git
  nb help remote
  nb help status
  nb help sync

Examples:
  nb history
  nb history example.md
  nb 3 history
  nb history example:
  nb example:history
  nb example:history 12
  nb history example:12
  nb example:12 history
```

#### `import`

[↑](#help) · See also:
[Import / Export](#%EF%B8%8F-import--export),
[Images](#-images),
[`add`](#add),
[`export`](#export)

```text
Usage:
  nb import [copy | download | move] (<path>... | <url>) [--convert]
            [<notebook>:][<folder-path>/][<filename>]
  nb import notebook <path> [<name>]

Options:
  --convert  Convert HTML content to Markdown.

Subcommands:
  (default) Copy or download the file(s) at <path> or <url>.
  copy      Copy the file(s) at <path> into the current notebook.
  download  Download the file at <url> into the current notebook.
  move      Move the file(s) at <path> into the current notebook.
  notebook  Import the local notebook at <path> to make it global.

Description:
  Copy, move, or download files into the current notebook or import
  a local notebook to make it global.

Read More:
  https://github.com/xwmx/nb#%EF%B8%8F-import--export

See Also:
  nb help add
  nb help export

Examples:
  nb import ~/Pictures/example.png
  nb import ~/Documents/example.docx
  nb import https://example.com/example.pdf
  nb example:import https://example.com/example.jpg
  nb import ./*
  nb import ./*.md
  nb import ~/Pictures/example.png example-notebook:
  nb import ~/Documents/example.docx example-folder/

Shortcut Alias:
  nb i
```

#### `init`

[↑](#help) · See also: [`notebooks`](#notebooks)

```text
Usage:
  nb init [<remote-url> [<branch>]] [--author] [--email <email>]
          [--name <name>]

Options:
  --author         Display the local email and name config prompt.
  --email <email>  Set the local commit author email address to <email>.
  --name  <name>   Set the local commit author name to <name>.

Description:
  Initialize the initial "home" notebook and generate a configuration file at:

      ~/.nbrc

  Pass optional <remote-url> and <branch> arguments to create the initial
  "home" notebook using a clone of an existing notebook.

See Also:
  nb help notebooks

Examples:
  nb init
  nb init https://github.com/example/example.git
  nb init https://github.com/example/example.git example-branch
```

#### `list`

[↑](#help) · See also:
[Listing & Filtering](#listing--filtering),
[`browse`](#browse),
[`ls`](#ls),
[`pin`](#pin),
[`search`](#search),
[`unpin`](#unpin)

```text
Usage:
  nb list [-e [<length>] | --excerpt [<length>]] [--filenames]
          [-n <limit> | --limit <limit> | --<limit>] [--no-id]
          [--no-indicator] [-p <number> | --page <number>] [--pager]
          [--paths] [-s | --sort] [-r | --reverse] [--tags]
          [-t <type> | --type <type> | --<type>]
          [<notebook>:][<folder-path>/][<id> | <filename> | <path> | <query>]

Options:
  -e, --excerpt [<length>]        Print an excerpt <length> lines long under
                                  each note's filename [default: 3].
  --filenames                     Print the filename for each note.
  -n, --limit <limit>, --<limit>  The maximum number of notes to list.
  --no-id                         Don't include the id in list items.
  --no-indicator                  Don't include the indicator in list items.
  -p, --page <number>             The page to view in the list paginated by
                                  a <limit> option or `nb set limit`.
  --pager                         Display output in the pager.
  --paths                         Print the full path to each item.
  -s, --sort                      Order notes by id.
  -r, --reverse                   List items in reverse order.
  --tags                          List tags in the notebook or folder.
  -t, --type <type>, --<type>     List items of <type>. <type> can be a file
                                  extension or one of the following types:
                                  archive, audio, book, bookmark, document,
                                  folder, image, note, text, video

Description:
  List notes in the current notebook.

  When <id>, <filename>, <path>, or <title> are present, the listing for the
  matching note is displayed. When no match is found, titles and filenames
  are searched for any that match <query> as a case-insensitive regular
  expression.

Read More:
  https://github.com/xwmx/nb#listing--filtering

Indicators:
  🔉  Audio
  📖  Book
  🔖  Bookmark
  🔒  Encrypted
  📂  Folder
  🌄  Image
  📄  PDF, Word, or Open Office document
  📹  Video

See Also:
  nb help browse
  nb help ls
  nb help pin
  nb help search
  nb help unpin

Examples:
  nb list
  nb list example.md -e 10
  nb list --excerpt --no-id
  nb list --filenames --reverse
  nb list "^Example.*"
  nb list --10
  nb list --type document
  nb example:list
```

#### `ls`

[↑](#help) · See also:
[Listing & Filtering](#listing--filtering),
[`browse`](#browse),
[`list`](#list),
[`pin`](#pin),
[`search`](#search),
[`unpin`](#unpin)

```text
Usage:
  nb ls [-a | --all] [-b | --browse] [-e [<length>] | --excerpt [<length>]]
        [--filenames] [-g | --gui] [-n <limit> | --limit <limit> | --<limit>]
        [--no-footer] [--no-header] [--no-id] [--no-indicator]
        [-p <number> | --page <number>] [--pager] [--paths] [-s | --sort]
        [-r | --reverse] [--tags] [-t <type> | --type <type> | --<type>]
        [<notebook>:][<folder-path>/][<id> | <filename> | <path> | <query>]

Options:
  -a, --all                       Print all items in the notebook. Equivalent
                                  to no limit.
  -b, --browse                    Open the specified item or current notebook
                                  with `browse` in a terminal web browser.
  -e, --excerpt [<length>]        Print an excerpt <length> lines long under
                                  each note's filename [default: 3].
  --filenames                     Print the filename for each note.
  -g, --gui                       Open the specified item or current notebook
                                  with `browse` in a GUI web browser.
  -n, --limit <limit>, --<limit>  The maximum number of listed items.
                                  [default: 15]
  --no-footer                     Print without footer.
  --no-header                     Print without header.
  --no-id                         Don't include the id in list items.
  --no-indicator                  Don't include the indicator in list items.
  -p, --page <number>             The page to view in the list paginated by
                                  a <limit> option or `nb set limit`.
  --pager                         Display output in the pager.
  --paths                         Print the full path to each item.
  -s, --sort                      Order notes by id.
  -r, --reverse                   List items in reverse order.
  --tags                          List tags in the notebook or folder.
  -t, --type <type>, --<type>     List items of <type>. <type> can be a file
                                  extension or one of the following types:
                                  archive, audio, book, bookmark, document,
                                  folder, image, note, text, video

Description:
  List notebooks and notes in the current notebook, displaying note titles
  when available. `nb ls` is a combination of `nb notebooks` and
  `nb list` in one view.

  When <id>, <filename>, <path>, or <title> are present, the listing for the
  matching note is displayed. When no match is found, titles and filenames
  are searched for any that match <query> as a case-insensitive regular
  expression.

  Options are passed through to `list`. For more information, see
  `nb help list`.

Read More:
  https://github.com/xwmx/nb#listing--filtering

Indicators:
  🔉  Audio
  📖  Book
  🔖  Bookmark
  🔒  Encrypted
  📂  Folder
  🌄  Image
  📄  PDF, Word, or Open Office document
  📹  Video

See Also:
  nb help browse
  nb help list
  nb help pin
  nb help search
  nb help unpin

Examples:
  nb
  nb --all
  nb ls
  nb ls example.md -e 10
  nb ls --excerpt --no-id
  nb ls --reverse
  nb ls "^Example.*"
  nb ls --10
  nb ls --type document
  nb example:
  nb example: -ae
  nb example:ls
```

#### `move`

[↑](#help) · See also:
[Moving & Renaming](#-moving--renaming),
[`copy`](#copy),
[`delete`](#delete),
[`edit`](#edit)

```text
Usage:
  nb move ([<notebook>:][<folder-path>/][<id> | <filename> | <title>])
          ([<notebook>:][<path>] | --reset | --to-bookmark | --to-note |
          --to-title | --to-todo) [-f | --force]

Options:
  -f, --force     Skip the confirmation prompt.
  --reset         Reset the filename to the last modified timestamp.
  --to-bookmark   Preserve the existing filename and replace the extension
                  with ".bookmark.md" to convert the note to a bookmark.
  --to-note       Preserve the existing filename and replace the bookmark's
                  ".bookmark.md" extension with ".md" to convert the bookmark
                  to a Markdown note.
  --to-title      Set the filename to the note title, lowercased with spaces
                  and disallowed filename characters replaced with underscores.
  --to-todo       Preserve the existing filename and replace the extension
                  with ".todo.md" to convert the note to a todo.

Description:
  Move or rename a note. Move the note to <path> or change the file type.
  When the file extension is omitted, the existing extension is used.
  When only a file extension is specified, only the extension will be updated.

  `nb move` and `nb rename` are aliases and can be used interchangeably.

Read More:
  https://github.com/xwmx/nb#-moving--renaming

See Also:
  nb help copy
  nb help delete
  nb help edit

Examples:
  # move "example.md" to "sample.org"
  nb move example.md sample.org

  # rename note 3 ("example.md") to "New Name.md"
  nb rename 3 "New Name"

  # rename "example.bookmark.md" to "New Name.bookmark.md"
  nb move example.bookmark.md "New Name"

  # rename note 3 ("example.md") to a bookmark named "example.bookmark.md"
  nb rename 3 --to-bookmark

  # move note 12 into "Sample Folder" in the "demo" notebook
  nb move example:12 demo:Sample\ Folder/

  # rename note 12 in the "example" notebook to "sample.md"
  nb rename example:12 "sample.md"

  # change the file extension of note 5 to .org
  nb rename 5 .org

Alias:
  nb rename

Shortcut Alias:
  nb mv
```

#### `notebooks`

[↑](#help) · See also:
[Notebooks](#-notebooks),
[`archive`](#archive),
[`history`](#history),
[`move`](#move),
[`remote`](#remote),
[`status`](#status),
[`sync`](#sync),
[`unarchive`](#unarchive),
[`use`](#use)

```text
Usage:
  nb notebooks [<name> | <query>] [--ar | --archived] [--global] [--local]
               [--names] [--paths] [--unar | --unarchived]
  nb notebooks add ([<name>] [<remote-url> [<branch>... | --all]]) [--author]
                   [--email <email>] [--name <name>]
  nb notebooks (archive | open | peek | status | unarchive) [<name>]
  nb notebooks author [<name> | <path>] [--email <email>] [--name <name>]
  nb notebooks current [--path | --selected | --filename [<filename>]]
                       [--global | --local]
  nb notebooks delete <name> [-f | --force]
  nb notebooks (export <name> [<path>] | import <path>)
  nb notebooks init [<path> [<remote-url> [<branch>]]] [--author]
                    [--email <email>] [--name <name>]
  nb notebooks rename <old-name> <new-name>
  nb notebooks select <selector>
  nb notebooks show (<name> | <path> | <selector>) [--ar | --archived]
                    [--escaped | --name | --path | --filename [<filename>]]
  nb notebooks use <name>

Options:
  --all                    Add notebooks from all remote branches.
  --ar, --archived         List archived notebooks, or return archival status
                           with `show`.
  --author                 Set the notebook's commit author email and name.
  --email <email>          Set the notebook's commit author email to <email>.
  --escaped                Print the notebook name with spaces escaped.
  --filename [<filename>]  Print an available filename for the notebooks. When
                           <filename> is provided, check for an existing file
                           and provide a filename with an appended sequence
                           number for uniqueness.
  -f, --force              Skip the confirmation prompt.
  --global                 List global notebooks or the notebook set globally
                           with `use`.
  --local                  Exit with 0 if current within a local notebook,
                           otherwise exit with 1.
  --name, --names          Print the notebook name.
  --name <name>            Set the notebook's commit author name to <name>.
  --path, --paths          Print the notebook path.
  --selected               Exit with 0 if the current notebook differs from
                           the current global notebook, otherwise exit with 1.
  --unar, --unarchived     Only list unarchived notebooks.

Subcommands:
  (default)  List notebooks.
  add        Create a new global notebook. When <remote-url> is specified,
             create one ore more new global notebook by cloning selected
             or specified <branch>es from <remote-url>.
             Aliases: `nb notebooks create`, `nb notebooks new`
  archive    Set the current notebook or notebook <name> to "archived" status.
  author     Configure the commit author email and name for the notebook.
  current    Print the current notebook name or path.
  delete     Delete a notebook.
  export     Export the notebook <name> to the current directory or <path>,
             making it usable as a local notebook.
  import     Import the local notebook at <path> to make it global.
  init       Create a new local notebook. Specify a <path> or omit to
             initialize the current working directory as a local notebook.
             Specify <remote-url> to clone an existing notebook.
  open       Open the current notebook directory or notebook <name> in the
             file browser, explorer, or finder.
             Shortcut Alias: `o`
  peek       Open the current notebook directory or notebook <name> in the
             first tool found in the following list:
             `ranger` [1], `mc` [2], `vifm` [3], `exa` [4], or `ls`.
             Shortcut Alias: `p`
  rename     Rename a notebook. Aliases: `move`, `mv`
  select     Set the current notebook from a colon-prefixed selector.
             Not persisted. Selection format: <notebook>:<identifier>
  status     Print the archival status of the current notebook or
             notebook <name>.
  show       Show and return information about a specified notebook.
  unarchive  Remove "archived" status from the current notebook or notebook <name>.
  use        Switch to a notebook.

    1. https://ranger.github.io/
    2. https://en.wikipedia.org/wiki/Midnight_Commander
    3. https://vifm.info/
    4. https://github.com/ogham/exa

Description:
  Manage notebooks.

Read More:
  https://github.com/xwmx/nb#-notebooks

See Also:
  nb help archive
  nb help history
  nb help move
  nb help remote
  nb help status
  nb help sync
  nb help unarchive
  nb help use

Examples:
  nb notebooks --names
  nb notebooks add sample
  nb notebooks add example https://github.com/example/example.git
  nb nb current --path
  nb nb archive example

Shortcut Aliases:
  nb n
  nb nb
```

#### `open`

[↑](#help) · See also:
[Viewing Bookmarks](#viewing-bookmarks),
[Images](#-images),
[`bookmark`](#bookmark),
[`browse`](#browse),
[`peek`](#peek),
[`show`](#show)

```text
Usage:
  nb open ([<notebook>:][<folder-path>/][<id> | <filename> | <title>])

Description:
  Open an item or notebook. When the item is a bookmark, open the bookmarked
  page in your system's primary web browser. When the item is in a text format
  or any other file type, `open` is the equivalent of `edit`. `open`
  with a notebook opens the notebook folder in the system's file browser.

Read More:
  https://github.com/xwmx/nb#viewing-bookmarks

See also:
  nb help bookmark
  nb help browse
  nb help peek
  nb help show

Examples:
  nb open 3
  nb open example.bookmark.md
  nb 3 open
  nb example:open 12
  nb open example:12
  nb example:12 open
  nb o 3
  nb 3 o
  nb o example:12
  nb example:12 o

Shortcut Alias:
  nb o
```

#### `peek`

[↑](#help) · See also:
[Viewing Bookmarks](#viewing-bookmarks),
[`bookmark`](#bookmark),
[`browse`](#browse),
[`open`](#open),
[`show`](#show)

```text
Usage:
  nb peek ([<notebook>:][<folder-path>/][<id> | <filename> | <title>])

Description:
  View an item or notebook in the terminal. When the item is a bookmark, view
  the bookmarked page in your terminal web browser. When the note is in a text
  format or any other file type, `peek` is the equivalent of `show`. When
  used with a notebook, `peek` opens the notebook folder first tool found in
  the following list: `ranger` [1], `mc` [2], `exa` [3], or `ls`.

    1. https://ranger.github.io/
    2. https://en.wikipedia.org/wiki/Midnight_Commander
    3. https://github.com/ogham/exa

Read More:
  https://github.com/xwmx/nb#viewing-bookmarks

See also:
  nb help bookmark
  nb help browse
  nb help open
  nb help show

Examples:
  nb peek 3
  nb peek example.bookmark.md
  nb 3 peek
  nb example:peek 12
  nb peek example:12
  nb example:12 peek
  nb p 3
  nb 3 p
  nb p example:12
  nb example:12 p

Alias:
  nb preview

Shortcut Alias:
  nb p
```

#### `pin`

[↑](#help) · See also:
[Pinning](#-pinning),
[`browse`](#browse),
[`list`](#list),
[`ls`](#ls),
[`unpin`](#unpin)

```text
Usage:
  nb pin ([<notebook>:][<folder-path>/][<id> | <filename> | <title>])

Description:
  Pin an item so it appears first in lists.

Read More:
  https://github.com/xwmx/nb#-pinning

See Also:
  nb help browse
  nb help list
  nb help ls
  nb help unpin

Examples:
  nb pin 123
  nb pin example:sample/321
```

#### `plugins`

[↑](#help) · See also:
[Plugins](#-plugins),
[Plugin Help](#plugin-help),
[`subcommands`](#subcommands-1)

```text
Usage:
  nb plugins [<name>] [--paths] [--force]
  nb plugins install [<path> | <url>] [--force]
  nb plugins uninstall <name>

Options:
  --paths  Print the full path to each plugin.

Subcommands:
  (default)  List plugins.
  install    Install a plugin from a <path> or <url>.
  uninstall  Uninstall the specified plugin.

Description:
  Manage plugins and themes.

Read More:
  https://github.com/xwmx/nb#-plugins

Plugin Extensions:
  .nb-theme   Plugins defining color themes.
  .nb-plugin  Plugins defining new subcommands and functionality.

See Also:
  nb help subcommands

Alias:
  nb plugin
```

#### `remote`

[↑](#help) · See also:
[Git Sync](#-git-sync),
[History](#-revision-history),
[`history`](#history),
[`notebooks`](#notebooks),
[`status`](#status),
[`sync`](#sync)

```text
Usage:
  nb remote
  nb remote branches [<url>]
  nb remote delete <branch-name>
  nb remote remove
  nb remote rename [<branch-name>] <name>
  nb remote reset <branch-name>
  nb remote set <url> [<branch-name>]

Subcommands:
  (default)  Print the remote URL and branch for the notebook.
  branches   List branches on the current or given remote.
  delete     Delete <branch-name> from the remote.
             Caveat: only orphan branches can be deleted.
  remove     Remove the remote URL from the notebook.
             Alias: `unset`
  rename     Rename the current orphan branch or <branch-name> to <name>.
             Caveat: only orphan branches can be renamed.
  reset      Reset <branch-name> on the remote to a blank initial state.
  set        Set the remote URL and branch for the notebook.

Description:
  Configure the remote repository URL and branch for the current notebook.

Read More:
  https://github.com/xwmx/nb#-git-sync
  https://github.com/xwmx/nb#-revision-history

See Also:
  nb help history
  nb help notebooks
  nb help status
  nb help sync

Examples:
  nb remote set https://github.com/example/example.git
  nb remote remove
  nb example-notebook:remote set https://github.com/example/example.git
```

#### `run`

[↑](#help) · See also: [`git`](#git), [`shell`](#shell)

```text
Usage:
  nb run <command> [<arguments>...]

Description:
  Run shell commands within the current notebook directory.

See Also:
  nb help git
  nb help shell

Examples:
  nb run ls -la
  nb run find . -name 'example*'
  nb run rg example
```

#### `search`

[↑](#help) · See also:
[Search](#-search),
[`browse`](#browse),
[`list`](#list),
[`ls`](#ls)

```text
Usage:
  nb search ([<notebook>:][<folder-path>/][<id> | <filename> | <title>])
            <query>... [-a | --all] [--and <query>] [--or <query>]
            [-l | --list] [--path] [-t <tag1>,<tag2>... | --tag <tag1>,<tag2>...]
            [-t | --tags] [--type <type> | --<type>] [--utility <name>]

Options:
  -a, --all                     Search all unarchived notebooks.
  --and <query>                 Add a AND query.
  -l, --list                    Print the id, filename, and title listing for
                                each matching file, without the excerpt.
  --or <query>                  Add an OR query.
  --path                        Print the full path for each matching file.
  -t, --tag <tag1>,<tag2>...    A comma-separated list of tags.
  -t, --tags                    List all tags found in the notebook.
  --type <type>, --<type>       Search items of <type>. <type> can be a file
                                extension or one of the following types:
                                note, bookmark, document, archive, image,
                                video, audio, folder, text
  --utility <name>              The name of the search utility to search with.

Description:
  Perform a full text search.

  Multiple query arguments are treated as AND queries, returning items that
  match all queries. AND queries can also be specified with the --and <query>
  option. The --or <query> option can be used to specify an OR query,
  returning items that match at least one of the queries.

  `nb search` is powered by Git's built-in `git grep` tool. `nb` also
  supports performing searches with alternative search tools using the
  --utility <name> option.

  Supported alternative search tools:
    1. `rga`   https://github.com/phiresky/ripgrep-all
    2. `rg`    https://github.com/BurntSushi/ripgrep
    3. `ag`    https://github.com/ggreer/the_silver_searcher
    4. `ack`   https://beyondgrep.com/
    5. `grep`  https://en.wikipedia.org/wiki/Grep

Read More:
  https://github.com/xwmx/nb#-search

See Also:
  nb help browse
  nb help list
  nb help ls

Examples:
  # search current notebook for "example query"
  nb search "example query"

  # search the notebook "example" for "example query"
  nb search example: "example query"

  # search all notebooks for "example query" and list matching items
  nb search "example query" --all --list

  # search for items matching "Example" AND "Demo"
  nb search "Example" "Demo"
  nb search "Example" --and "Demo"

  # search for items matching "Example" OR "Sample"
  nb search "Example|Sample"
  nb search "Example" --or "Sample"

  # search with a regular expression
  nb search "\d\d\d-\d\d\d\d"

  # search for tags
  nb search --tag tag1 -t tag2

  # search the current notebook for "example query"
  nb q "example query"

  # search all notebooks for "example query" and list matching items
  nb q -la "example query"

Shortcut Alias:
  nb q
```

#### `settings`

[↑](#help) · See also:
[`set` & `settings`](#%EF%B8%8F-set--settings),
[`unset`](#unset)

```text
Usage:
  nb set [<name> [<value>] | <number> [<value>]]
  nb settings colors [<number> | themes]
  nb settings edit
  nb settings get   (<name> | <number>)
  nb settings list  [--long]
  nb settings set   (<name> | <number>) <value>
  nb settings show  (<name> | <number>)
  nb settings unset (<name> | <number>)

Subcommands:
  (default)  Open the settings prompt, to <name> or <number>, if present.
             When <value> is also present, assign <value> to the setting.
  colors     Print a table of available colors and their xterm color numbers.
             When <number> is provided, print the number in its color.
             `settings colors themes` prints a list of installed themes.
  edit       Open the `nb` configuration file in `$EDITOR`.
  get        Print the value of a setting.
  list       List information about available settings.
  set        Assign <value> to a setting.
  show       Print the help information and current value of a setting.
  unset      Unset a setting, returning it to the default value.

Description:
  Configure `nb`. Use `nb settings set` to customize a setting and
  `nb settings unset` to restore the default for a setting.

  Use the `nb set` alias to quickly assign values to settings:

    nb set color_theme blacklight
    nb set limit 40

Read More:
  https://github.com/xwmx/nb#%EF%B8%8F-set--settings

See Also:
  nb help unset

Examples:
  nb settings
  nb set 5 "org"
  nb set color_primary 105
  nb set unset color_primary
  nb set color_secondary unset
  nb settings colors
  nb settings colors 105
  nb set limit 15

Alias:
  nb set
```

##### `auto_sync`

[↑](#help) · See also: [Git Sync](#-git-sync)

```text
[1]  auto_sync
     ---------
     By default, operations that trigger a git commit like `add`, `edit`,
     and `delete` will sync notebook changes to the remote repository, if
     one is set. To disable this behavior, set this to "0".

     • Default Value: 1
```

##### `color_primary`

[↑](#help) · See also: [Color Themes](#-color-themes), [Custom Color Themes](#custom-color-themes)

```text
[2]  color_primary
     -------------
     The primary color used to highlight identifiers and messages.

     • Supported Values: xterm color numbers 0 through 255.
     • Default Value:    68 (blue) for 256 color terminals,
                         4  (blue) for  8  color terminals.
```

##### `color_secondary`

[↑](#help) · See also: [Color Themes](#-color-themes), [Custom Color Themes](#custom-color-themes)

```text
[3]  color_secondary
     ---------------
     The color used for lines and footer elements.

     • Supported Values: xterm color numbers 0 through 255.
     • Default Value:    8
```

##### `color_theme`

[↑](#help) · See also: [Color Themes](#-color-themes)

```text
[4]  color_theme
     -----------
     The color theme.

     To view screenshots of the built-in themes, visit:

         https://git.io/nb-docs-color-themes

     `nb` supports custom, user-defined themes. To learn more, run:

         nb help --colors

     To change the syntax highlighting theme, use:

         nb set syntax_theme

     • Available themes:

         blacklight
         console
         desert
         electro
         forest
         nb
         ocean
         raspberry
         smoke
         unicorn
         utility

     • Default Value: nb
```

##### `default_extension`

[↑](#help) · See also: [Adding](#adding)

```text
[5]  default_extension
     -----------------
     The default extension to use for note files. Change to "org" for
     Org files, "rst" for reStructuredText, "txt" for plain text, or
     whatever you prefer.

     • Default Value: md
```

##### `editor`

[↑](#help) · See also: [Editing](#editing), [Adding](#adding)

```text
[6]  editor
     ------
     The command line text editor used by `nb`.

     • Example Values:

         atom
         code
         emacs
         macdown
         mate
         micro
         nano
         pico
         subl
         vi
         vim
```

##### `encryption_tool`

[↑](#help) · See also: [Password-Protected Encrypted Notes and Bookmarks](#password-protected-encrypted-notes-and-bookmarks)

```text
[7]  encryption_tool
     ---------------
     The tool used for encrypting notes.

     • Supported Values: openssl, gpg
     • Default Value:    openssl
```

##### `footer`

[↑](#help) · See also: [Listing & Filtering](#listing--filtering)

```text
[8]  footer
     ------
     By default, `nb` and `nb ls` include a footer with example commands.
     To hide this footer, set this to "0".

     • Default Value: 1
```

##### `header`

[↑](#help) · See also: [Listing & Filtering](#listing--filtering)

```text
[9]  header
     ------
     By default, `nb` and `nb ls` include a header listing available notebooks.
     Set the alignment, or hide the header with "0".

     • Supported Values:

         0  Hide Header
         1  Dynamic Alignment
              - Left justified when list is shorter than terminal width.
              - Center aligned when list is longer than terminal width.
         2  Center Aligned (default)
         3  Left Justified

     • Default Value: 1
```

##### `limit`

[↑](#help) · See also: [Listing & Filtering](#listing--filtering)

```text
[10] limit
     -----
     The maximum number of items included in the `nb` and `nb ls` lists.
     Set to `auto` to automatically limit output to the current terminal height.
     Add an auto limit offset for multiline prompts with `auto-<number>`.

     • Example Values:

       15
       auto
       auto-2

     • Default Value: 15
```

##### `nb_dir`

[↑&nbsp;](#help)

```text
[11] nb_dir
     ------
     The location of the directory that contains the notebooks.

     For example, to sync all notebooks with Dropbox, create a folder at
     `~/Dropbox/Notes` and run: `nb settings set nb_dir ~/Dropbox/Notes`

     • Default Value: ~/.nb
```

##### `syntax_theme`

[↑](#help) · See also: [Terminal Syntax Highlighting](#terminal-syntax-highlighting-theme)

```text
[12] syntax_theme
     ------------
     The syntax highlighting theme. View examples with:

         bat --list-themes

     • Available themes:

         1337
         DarkNeon
         Dracula
         GitHub
         Monokai Extended
         Monokai Extended Bright
         Monokai Extended Light
         Monokai Extended Origin
         Nord
         OneHalfDark
         OneHalfLight
         Solarized (dark)
         Solarized (light)
         Sublime Snazzy
         TwoDark
         ansi-dark
         ansi-light
         base16
         base16-256
         gruvbox
         gruvbox-light
         gruvbox-white
         zenburn

     • Default Value: base16
```

#### `shell`

[↑](#help) · See also:
[Interactive Shell](#-interactive-shell),
[`run`](#run)

```text
Usage:
  nb shell [<subcommand> [<options>...] | --clear-history]

Options:
  --clear-history  Clear the `nb` shell history.

Description:
  Start the `nb` interactive shell. Type "exit" to exit.

  `nb shell` recognizes all `nb` subcommands and options, providing
  a streamlined, distraction-free approach for working with `nb`.

  When <subcommand> is present, the command will run as the shell is opened.

Read More:
  https://github.com/xwmx/nb#-interactive-shell

See Also:
  nb help run

Example:
  $ nb shell
  nb> ls 3
  [3] Example

  nb> edit 3 --content "New content."
  Updated: [3] Example

  nb> notebook
  home

  nb> exit
  $
```

#### `show`

[↑](#help) · See also:
[Viewing](#viewing),
[Images](#-images),
[`browse`](#browse),
[`open`](#open),
[`peek`](#peek)

```text
Usage:
  nb show ([<notebook>:][<folder-path>/][<id> | <filename> | <title>])
          [[-a | --added] | [--authors] | [-b | --browse] | --filename | --id |
          --info-line | --path | [-p | --print] | --relative-path | [-r |
          --render] | --title | --type [<type>] | [-u | --updated]] [--no-color]
  nb show <notebook>

Options:
  -a, --added      Print the date and time when the item was added.
  --authors        List the git commit authors of an item.
  -b, --browse     Open the item with `nb browse`.
  --filename       Print the filename of the item.
  --id             Print the id number of the item.
  --info-line      Print the id, filename, and title of the item.
  --no-color       Show without syntax highlighting.
  --path           Print the full path of the item.
  -p, --print      Print to standard output / terminal.
  --relative-path  Print the item's path relative within the notebook.
  -r, --render     Use `pandoc` [1] to render the file to HTML and display
                   in the terminal web browser. If either `pandoc` or a
                   browser are unavailable, `-r` / `--render` is ignored.
  --title          Print the title of the note.
  --type [<type>]  Print the file extension or, when <type> is specified,
                   return true if the item matches <type>. <type> can be a
                   file extension or one of the following types:
                   archive, audio, bookmark, document, folder, image,
                   text, video
  -u, --updated    Print the date and time of the last recorded change.

Description:
  Show an item or notebook. Notes in text file formats can be rendered or
  printed to standard output. Non-text files are opened in your system's
  preferred app or program for that file type.

  By default, the item is opened using `less` or the program configured
  in the `$PAGER` environment variable. Use the following keys to navigate
  in `less` (see `man less` for more information):

    Key               Function
    ---               --------
    mouse scroll      Scroll up or down
    arrow up or down  Scroll one line up or down
    f                 Jump forward one window
    b                 Jump back one window
    d                 Jump down one half window
    u                 Jump up one half window
    /<query>          Search for <query>
    n                 Jump to next <query> match
    q                 Quit

  To skip the pager and print to standard output, use the `-p` / `--print`
  option.

  `-r` / `--render` automatically uses either `w3m` [2] or `links` [3].
  To specify a preferred browser, set the `$BROWSER` environment variable
  in your .bashrc, .zshrc, or equivalent, e.g.: export BROWSER="links"

  If `bat` [4], `highlight` [5], or Pygments [6] is installed, notes are
  printed with syntax highlighting.

    1. https://pandoc.org/
    2. https://en.wikipedia.org/wiki/W3m
    3. https://en.wikipedia.org/wiki/Links_(web_browser)
    4. https://github.com/sharkdp/bat
    5. http://www.andre-simon.de/doku/highlight/en/highlight.php
    6. https://pygments.org/

Read More:
  https://github.com/xwmx/nb#viewing

See Also:
  nb help browse
  nb help open
  nb help peek

Examples:
  nb show 1
  nb show example.md --render
  nb show "A Document Title" --print --no-color
  nb 1 show
  nb example:show 12
  nb show example:12
  nb example:12 show
  nb s 1
  nb 1 s
  nb s example:12
  nb example:12 s

Alias:
  nb view

Shortcut Alias:
  nb s
```

#### `status`

[↑](#help) · See also:
[Git Sync](#-git-sync),
[History](#-revision-history),
[`archive`](#archive),
[`history`](#history),
[`notebooks`](#notebooks),
[`remote`](#remote),
[`sync`](#sync),
[`unarchive`](#unarchive)

```text
Usage:
  nb status [<notebook>]

Description:
  Print archival, git, and remote status for the current notebook or <notebook>.

Read More:
  https://github.com/xwmx/nb#-git-sync
  https://github.com/xwmx/nb#-revision-history

See Also:
  nb help archive
  nb help history
  nb help notebooks
  nb help remote
  nb help sync
  nb help unarchive

Examples:
  nb status
  nb status example

Shortcut Alias:
  nb st
```

#### `subcommands`

[↑](#help) · See also:
[Plugins](#-plugins),
[`plugins`](#plugins)

```text
Usage:
  nb subcommands [add <name>...] [alias <name> <alias>]
                 [describe <name> <usage>]

Subcommands:
  add       Add a new subcommand.
  alias     Create an <alias> of a given subcommand <name>, with linked help.
            Note that aliases must also be added with `subcommands add`.
  describe  Set the usage text displayed with `nb help <subcommand>`.
            This can be assigned as a heredoc, which is recommended, or
            as a string argument.

Description:
  List, add, alias, and describe subcommands. New subcommands, aliases, and
  descriptions are not persisted, so `add`, `alias`, `describe` are
  primarily for plugins.

Read More:
  https://github.com/xwmx/nb#-plugins

See Also:
  nb help plugins
```

#### `sync`

[↑](#help) · See also:
[Git Sync](#-git-sync),
[History](#-revision-history),
[`history`](#history),
[`notebooks`](#notebooks),
[`remote`](#remote),
[`status`](#status)

```text
Usage:
  nb sync [-a | --all]

Options:
  -a, --all   Sync all unarchived notebooks.

Description:
  Sync the current notebook with its remote.

Private Repositories and Git Credentials:
  Syncing with private repositories requires configuring git to not prompt
  for credentials.

  For repositories cloned over HTTPS, credentials can be cached with git.
  For repositories cloned over SSH, keys can be added to the ssh-agent.

  More Information:
    https://github.com/xwmx/nb#private-repositories-and-git-credentials

Sync Conflict Resolution:
  When `nb sync` encounters a conflict in a text file and can't merge
  overlapping local and remote changes, both versions are saved in the
  file, separated by git conflict markers. Use `nb edit` to remove the
  conflict markers and delete any unwanted text.

  When `nb sync` encounters a conflict in a binary file, such as an
  encrypted note or bookmark, both versions of the file are saved in the
  notebook as individual files, one with `--conflicted-copy` appended to
  the filename.

  More Information:
    https://github.com/xwmx/nb#sync-conflict-resolution

Read More:
  https://github.com/xwmx/nb#-git-sync
  https://github.com/xwmx/nb#-revision-history

See Also:
  nb help history
  nb help notebooks
  nb help remote
  nb help status

Examples:
  nb sync
  nb sync --all
```

#### `tasks`

[↑](#help) · See also:
[Tasks](#%EF%B8%8F-tasks),
[Todos](#-todos),
[`do`](#do),
[`todo`](#todo),
[`undo`](#undo)

```text
Usage:
  nb tasks ([<notebook>:][<folder-path>/][<id> | <filename> | <description>])
           [open | closed]

Description:
  List tasks in todos, notebooks, folders, and other items.

Read More:
  https://github.com/xwmx/nb#%EF%B8%8F-tasks
  https://github.com/xwmx/nb#-todos

See Also:
  nb help do
  nb help todo
  nb help undo

Examples:
  nb tasks
  nb tasks open
  nb tasks closed
  nb tasks 123
  nb example:tasks open
  nb tasks closed sample/
  nb tasks closed demo:456

Shortcut Alias:
  nb t
```

#### `todo`

[↑](#help) · See also:
[Todos](#-todos),
[`do`](#do),
[`tasks`](#tasks),
[`undo`](#undo)

```text
Usage:
  nb todo add [<notebook>:][<folder-path>/][<filename>] <title>
              [--description <description>] [--due <date>]
              [-r (<url> | <selector>) | --related (<url> | <selector>)]
              [--tags <tag1>,<tag2>...] [--task <title>]...
  nb todo do   ([<notebook>:][<folder-path>/][<id> | <filename> | <description>])
               [<task-number>]
  nb todo undo ([<notebook>:][<folder-path>/][<id> | <filename> | <description>])
               [<task-number>]
  nb todos [<notebook>:][<folder-path>/] [open | closed]
  nb todos tasks ([<notebook>:][<folder-path>/][<id> | <filename> | <description>])
                 [open | closed]

Options:
  --description <description>         Description for the todo.
  --due <date>                        Due date and / or time for the todo.
  -r, --related (<url> | <selector>)  Related URL or selector.
  --tags <tag1>,<tag2>...             Comma-separated list of tags.
  --task <title>                      Task to add to the tasklist.

Subcommands:
  (default)   List todos.
  add         Add a new todo.
              Shortcut Aliases: `nb todo a`, `nb todo +`
  do          Mark a todo or task as done.
  tasks       List tasks in todos, notebooks, folders, and other item.
  undo        Unmark a todo or task as done.

Description:
  Manage todos and tasks.

Read More::
  https://github.com/xwmx/nb#-todos

See Also:
  nb help do
  nb help tasks
  nb help undo

Examples:
  nb todo add "Example todo title."
  nb todo add Example todo title.
  nb todo add "Sample title." --tags tag1,tag2 --related demo:567
  nb todos
  nb todos open
  nb todos closed
  nb example:todos open
  nb todos closed sample/

Alias:
  nb todos

Shortcut Alias:
  nb t
```

#### `unarchive`

[↑](#help) · See also:
[Archiving Notebooks](#archiving-notebooks),
[`archive`](#archive),
[`notebooks`](#notebooks),
[`status`](#status)

```text
Usage:
  nb unarchive [<name>]

Description:
  Remove "archived" status from the current notebook or notebook <name>.

  This is an alias for `nb notebooks unarchive`.

Read More:
  https://github.com/xwmx/nb#archiving-notebooks

See Also:
  nb help archive
  nb help notebooks
  nb help status

Examples:
  nb unarchive
  nb unarchive example

Shortcut Alias:
  nb unar
```

#### `undo`

[↑](#help) · See also:
[Todos](#-todos),
[Tasks](#%EF%B8%8F-tasks),
[`do`](#do),
[`tasks`](#tasks),
[`todo`](#todo)

```text
Usage:
  nb undo ([<notebook>:][<folder-path>/][<id> | <filename> | <title>])
          [<task-number>]

Description:
  Mark a todo or task as not done.

Read More:
  https://github.com/xwmx/nb#-todos

See Also:
  nb help do
  nb help tasks
  nb help todo

Examples:
  nb undo 123
  nb undo example:sample/321
  nb undo 543 7
```

#### `unpin`

[↑](#help) · See also:
[Pinning](#-pinning),
[`browse`](#browse),
[`list`](#list),
[`ls`](#ls),
[`pin`](#pin)

```text
Usage:
  nb unpin ([<notebook>:][<folder-path>/][<id> | <filename> | <title>])

Description:
  Unpin a pinned item.

Read More:
  https://github.com/xwmx/nb#-pinning

See Also:
  nb help browse
  nb help list
  nb help ls
  nb help pin

Examples:
  nb unpin 123
  nb unpin example:sample/321
```

#### `unset`

[↑](#help) · See also:
[`set` & `settings`](#%EF%B8%8F-set--settings),
[`settings`](#settings)

```text
Usage:
  nb unset (<name> | <number>)

Description:
  Unset a setting, returning it to the default value.

  This is an alias for `nb settings unset`.

Read More:
  https://github.com/xwmx/nb#%EF%B8%8F-set--settings

See Also:
  nb help settings

Examples:
  nb unset color_primary
  nb unset 2

Alias:
  nb reset
```

#### `update`

[↑](#help) · See also:
[Installation](#installation),
[`env`](#env),
[`version`](#version)

```text
Usage:
  nb update

Description:
  Update `nb` to the latest version. You will be prompted for
  your password if administrator privileges are required.

  If `nb` was installed using a package manager like npm or
  Homebrew, use the package manager's upgrade functionality instead
  of this command.

Read More:
  https://github.com/xwmx/nb#installation

See Also:
  nb help env
  nb help version
```

#### `use`

[↑](#help) · See also:
[Notebooks](#-notebooks),
[`notebooks`](#notebooks)

```text
Usage:
  nb use <notebook>

Description:
  Switch to the specified notebook. Shortcut for `nb notebooks use`.

Read More:
  https://github.com/xwmx/nb#-notebooks

See Also:
  nb help notebooks

Example:
  nb use example

Shortcut Alias:
  nb u
```

#### `version`

[↑](#help) · See also:
[Installation](#installation),
[`env`](#env),
[`update`](#update)

```text
Usage:
  nb version

Description:
  Display version information.

See Also:
  nb help env
  nb help update
```

### Plugin Help

<p>
  <sup>
    <a href="#help">↑</a> ·
    <a href="#-plugins">Plugins</a>,
    <a href="#plugins"><code>nb plugins</code></a>
  </sup>
</p>

<p align="center">
  <a href="#backlink">backlink</a>&nbsp;·
  <a href="#bump">bump</a>&nbsp;·
  <a href="#clip">clip</a>&nbsp;·
  <a href="#ebook">ebook</a>&nbsp;·
  <a href="#example">example</a>&nbsp;·
  <a href="#weather">weather</a>
</p>

<p align="center">
  <a href="#help">&nbsp;↑&nbsp;</a>
</p>

#### `backlink`

[↑&nbsp;](#plugin-help)

##### Install

```bash
nb plugins install https://github.com/xwmx/nb/blob/master/plugins/backlink.nb-plugin
```

##### Help

```text
Usage:
  nb backlink [--force]

Description:
  Add backlinks to notes. Crawl notes in a notebook for [[wiki-style links]]
  and append a "Backlinks" section to each linked file that lists passages
  referencing the note.

  To link to a note from within another note, surround the title of the
  target note in double square brackets:

      Example with link to [[Target Note Title]] in content.

  Depends on note-link-janitor:
    https://github.com/andymatuschak/note-link-janitor

    Requirement: every note in the notebook must have a title.
```

#### `bump`

[↑&nbsp;](#plugin-help)

##### Install

```bash
nb plugins install https://github.com/xwmx/nb/blob/master/plugins/bump.nb-plugin
```

##### Help

```text
Usage:
  nb bump [<notebook>:][<folder-path>/][<id>][<filename>][<title>]

Description:
  Bump an item to the top of the list.

  `bump` updates the item's modification timestamp without editing the item
  or creating a new commit.

Examples:
  nb bump 123
  nb bump example:sample/456

Alias:
  nb touch
```

#### `clip`

[↑&nbsp;](#plugin-help)

##### Install

```bash
nb plugins install https://github.com/xwmx/nb/blob/master/plugins/clip.nb-plugin
```

##### Help

```text
Usage:
  nb clip [<notebook>:][<id> | <filename> | <path> | <title> | <extension>]

Description:
  Save the clipboard contents and copy contents of text or markdown items to
  the clipboard.

  When called with no arguments or when no matching file is found, the text
  content on the clipboard is saved to a new file, pending a prompt.

Examples:
  # copy the content of item 123 to the clipboard
  nb clip 123

  # save the clipboard contents to a new file with a `.js` file extension
  nb clip .js

  # save the clipboard contents as a new `.cr` file in the "snippets" notebook
  nb snippets:clip .cr
```

#### `ebook`

[↑&nbsp;](#plugin-help)

##### Install

```bash
nb plugins install https://github.com/xwmx/nb/blob/master/plugins/ebook.nb-plugin
```

##### Help

```text
Usage:
  nb ebook new <name>
  nb ebook publish

Subcommands:
  ebook new      Create a new notebook initialized with placeholder files for
                 authoring an ebook.
  ebook publish  Generate a .epub file using the current notebook contents.

Description:
  Ebook authoring with `nb`.

  `nb ebook new` creates a notebook populated with initial placeholder files
  for creating an ebook. Edit the title page and chapters using normal `nb`
  commands, then use `nb ebook publish` to generate an epub file.

  Chapters are expected to be markdown files with sequential numeric
  filename prefixes for ordering:

    01-example.md
    02-sample.md
    03-demo.md

  Create new chapters with `nb add`:

    nb add --filename "04-chapter4.md"

  title.txt contains the book metadata in a YAML block. For more information
  about the fields for this file, visit:

    https://pandoc.org/MANUAL.html#epub-metadata

  stylesheet.css contains base styling for the generated ebook. It can be used
  as it is and can also be edited using `nb edit`.

  As with all `nb` notebooks, changes are recorded automatically in git,
  providing automatic version control for all ebook content, source, and
  metadata files.

  Generated epub files are saved in the notebook and can be previewed in the
  terminal with `nb show`. Export a generated epub file with `nb export`:

    nb export 12 .

More info:
  https://pandoc.org/epub.html
```

#### `example`

[↑&nbsp;](#plugin-help)

##### Install

```bash
nb plugins install https://github.com/xwmx/nb/blob/master/plugins/example.nb-plugin
```

##### Help

```text
Usage:
  nb example

Description:
  Print "Hello, World!"
```

#### `weather`

[↑&nbsp;](#plugin-help)

##### Install

```bash
nb plugins install https://github.com/xwmx/nb/blob/master/plugins/weather.nb-plugin
```

##### Help

```text
Usage:
  nb weather [<option>...]

Description:
  Display weather information from wttr.in.

More Info:
  https://github.com/chubin/wttr.in
  https://wttr.in

Examples:
  nb weather
  nb weather Tokyo
  nb weather lax

Shortcut Alias:
  nb w
```

## Specifications

<p align="center">
  <a href="#nb-markdown-bookmark-file-format">Bookmark File Format</a>&nbsp;·
  <a href="#nb-markdown-todo-file-format">Todo File Format</a>&nbsp;·
  <a href="#nb-notebook-specification">Notebook Specification</a>
</p>

<p align="center">
  <a href="#help">&nbsp;↑&nbsp;</a>
</p>

### `nb` Markdown Bookmark File Format

<p>
  <sup>
    <a href="#specifications">↑</a> ·
    <a href="#-bookmarks">Bookmarks</a>,
    <a href="#bookmark"><code>nb bookmark</code></a>
  </sup>
</p>

#### Extension

`.bookmark.md`

#### Description

`nb` bookmarks are Markdown documents created using a combination of
user input and data from the bookmarked page. The `nb` bookmark format
is intended to be readable, editable, convertible, renderable, and
clearly organized for greatest accessibility.

Bookmarks are identified by a `.bookmark.md` file extension. The
bookmark URL is the first URL in the file within `<` and `>` characters.
To create a minimally valid bookmark file with [`nb add`](#add):

```bash
nb add example.bookmark.md --content "<https://example.com>"
```

This creates a file with the name `example.bookmark.md` containing:

```markdown
<https://example.com>
```

In a full bookmark, information is separated into sections,
with each bookmark section indicated by a Markdown `h2` heading.

#### Example

````markdown
# Example Title (example.com)

<https://example.com>

## Description

Example description.

## Quote

> Example quote line one.
>
> Example quote line two.

## Comment

Example comment.

## Related

- <https://example.net>
- <https://example.org>
- [[example:123]]

## Tags

#tag1 #tag2

## Content

Example Title
=============

This domain is for use in illustrative examples in documents. You may
use this domain in literature without prior coordination or asking for
permission.

[More information\...](https://www.iana.org/domains/example)

## Source

```html
<!doctype html>
<html>
  <head>
    <title>Example Title</title>
    <meta name="description" content="Example description." />
  </head>

  <body>
    <h1>Example Title</h1>
    <p>
      This domain is for use in illustrative examples in documents. You may
      use this domain in literature without prior coordination or asking for
      permission.
    </p>
    <p>
      <a href="https://www.iana.org/domains/example">More information...</a>
    </p>
  </body>
</html>
```
````

#### Elements

##### Title

`Optional`

A [Markdown atx-style `h1` heading
](https://daringfireball.net/projects/markdown/syntax#header)
containing the content of the bookmarked page's
HTML `<title>` or [`og:title`](https://ogp.me/) tag, if present, followed by
the domain within parentheses.

###### Examples

```markdown
# Example Title (example.com)
```
```markdown
# (example.com)
```

<p>
  <sup>
    <a href="#nb-markdown-bookmark-file-format">↑</a>
  </sup>
</p>

##### URL

`Required`

The URL of the bookmarked resource, with surrounding angle brackets
(`<`, `>`).

This is the only required element.

<p>
  <sup>
    <a href="#nb-markdown-bookmark-file-format">↑</a>
  </sup>
</p>

##### `## Description`

`Optional`

A text element containing the content of the bookmarked page's meta description
or [`og:description`](https://ogp.me/) tag, if present.

<p>
  <sup>
    <a href="#nb-markdown-bookmark-file-format">↑</a>
  </sup>
</p>

##### `## Quote`

`Optional`

A markdown quote block containing a user-specified excerpt from the bookmarked
resource.

<p>
  <sup>
    <a href="#nb-markdown-bookmark-file-format">↑</a>
  </sup>
</p>

##### `## Comment`

`Optional`

A text element containing a comment written by the user.

<p>
  <sup>
    <a href="#nb-markdown-bookmark-file-format">↑</a>
  </sup>
</p>

##### `## Related`

`Optional`

A Markdown list of
angle bracketed (`<`, `>`) URLs and
[[[wiki-style links]]](#-linking)
that are related to the bookmarked resource.

<p>
  <sup>
    <a href="#nb-markdown-bookmark-file-format">↑</a>
  </sup>
</p>

##### `## Tags`

`Optional`

A list of [#tags](#-tagging)
represented as `#hashtags`
separated by individual spaces.

<p>
  <sup>
    <a href="#nb-markdown-bookmark-file-format">↑</a>
  </sup>
</p>

##### `## Content`

`Optional`

The full content of the bookmarked page, converted to Markdown.

The `## Content` section makes the page content available locally for
full-text search and viewing of page content. The source HTML is converted
to inline Markdown to reduce the amount of markup, make it more readable,
and make page content easily viewable in the terminal as markdown and
streamlined HTML in web browsers.

<p>
  <sup>
    <a href="#nb-markdown-bookmark-file-format">↑</a>
  </sup>
</p>

##### `## Source`

`Optional`

A fenced code block with `html` language identifier containing the source HTML
from the bookmarked page.

`nb` does not save the page source by default. `nb` uses this section to save
the source HTML page content when `pandoc` is not available to convert it to
Markdown.

<p>
  <sup>
    <a href="#nb-markdown-bookmark-file-format">↑</a>
  </sup>
</p>

### `nb` Markdown Todo File Format

<p>
  <sup>
    <a href="#specifications">↑</a> ·
    <a href="#-todos">Todos</a>,
    <a href="#todo"><code>nb todo</code></a>
  </sup>
</p>

#### Extension

`.todo.md`

#### Description

`nb` todos are Markdown documents identified by a `.todo.md` file extension.
Todos contain a Markdown `h1` heading
starting with a Markdown checkbox (`[ ]` / `[x]`) indicating
the todo completion state, followed by the todo title.

#### Example

```markdown
# [x] Example todo title.

## Due

2100-01-01

## Description

Example description.

## Tasks

- [ ] One
- [x] Two
- [ ] Three

## Related

- [[example:123]]
- <https://example.org>

## Tags

#tag1 #tag2
```

#### Elements

##### Title

`Required`

A [Markdown atx-style `h1` heading
](https://daringfireball.net/projects/markdown/syntax#header)
containing a Markdown checkbox followed by the todo title.
An `x` within the checkbox (`[ ]`) indicates that the todo is done.

###### Examples

```markdown
# [ ] Example undone / open todo title.
```
```markdown
# [x] Example done / closed todo title.
```

<p>
  <sup>
    <a href="#nb-markdown-todo-file-format">↑</a>
  </sup>
</p>

##### `## Due`

`Optional`

A text element containing a value referencing
a due date and / or time for the todo.

<p>
  <sup>
    <a href="#nb-markdown-todo-file-format">↑</a>
  </sup>
</p>

##### `## Description`

`Optional`

A text element containing a description for the todo.

<p>
  <sup>
    <a href="#nb-markdown-todo-file-format">↑</a>
  </sup>
</p>

##### `## Tasks`

`Optional`

A markdown tasklist containing sub-tasks for the todo.

<p>
  <sup>
    <a href="#nb-markdown-todo-file-format">↑</a>
  </sup>
</p>

##### `## Related`

`Optional`

A Markdown list of
angle bracketed (`<`, `>`) URLs and
[[[wiki-style links]]](#-linking)
that are related to the todo.

<p>
  <sup>
    <a href="#nb-markdown-todo-file-format">↑</a>
  </sup>
</p>

##### `## Tags`

`Optional`

A list of [#tags](#-tagging)
represented as `#hashtags`
separated by individual spaces.

<p>
  <sup>
    <a href="#nb-markdown-todo-file-format">↑</a>
  </sup>
</p>

### `nb` Notebook Specification

<p>
  <sup>
    <a href="#specifications">↑</a> ·
    <a href="#-notebooks">Notebooks</a>,
    <a href="#notebooks"><code>nb notebooks</code></a>
  </sup>
</p>

An `nb` notebook is a directory that contains a valid `.git` directory,
indicating that it has been initialized as a git repository, and a `.index`
file in the root directory.

#### `.index` Files

A notebook folder index is a text file named `.index` in any folder
within the notebook directory. `.index` contains a list of visible
filenames within the folder, one per line, and the line number of each
filename represents the id. `.index` files are included in the git repository
so ids are preserved across systems.

##### Operations

<dl>
  <dt><code>add</code></dt>
  <dd>Append a new line containing the filename to <code>.index</code>.</dd>
  <dt><code>update</code></dt>
  <dd>Overwrite the existing filename in <code>.index</code> with the new filename.</dd>
  <dt><code>delete</code></dt>
  <dd>Delete the filename, preserving the newline, leaving the line blank.</dd>
  <dt><code>reconcile</code></dt>
  <dd>Remove duplicate lines, preserving existing blank lines, <code>add</code> entries for new files, and <code>delete</code> entries for deleted files.</dd>
  <dt><code>rebuild</code></dt>
  <dd>Delete and rebuild <code>.index</code>, listing files by most recently modified, reversed.</dd>
</dl>

##### `index` Subcommand

`nb` manages the `.index` of each folder within a notebook using an internal
`index` subcommand.

###### `nb help index`

```text
Usage:
  nb index add <filename>
  nb index delete <filename>
  nb index get_basename <id>
  nb index get_id <filename>
  nb index get_max_id
  nb index rebuild [--ancestors]
  nb index reconcile [--ancestors] [--commit]
  nb index show
  nb index update <existing-filename> <new-filename>
  nb index verify
  nb index <subcommand> <options>... [<folder-path>]

Options:
  --ancestors   Perform the action on all folders within the notebook that
                are ancestors of the current folder.
  --commit      Commit changes to git.

Subcommands:
  add           Add <filename> to the index.
  delete        Delete <filename> from the index.
  get_basename  Print the filename / basename at the specified <id>.
  get_id        Get the id for <filename>.
  get_max_id    Get the maximum id for the folder.
  rebuild       Rebuild the index, listing files by last modified, reversed.
                Some ids will change. Prefer `nb index reconcile`.
  reconcile     Remove duplicates and update index for added and deleted files.
  show          Print the index.
  update        Overwrite the <existing-filename> entry with <new-filename>.
  verify        Verify that the index matches the folder contents.

Description:
  Manage the index for the current folder or the folder at <folder-path>,
  which can be passed as the final argument to any `index` subcommand.

  `index` is used internally by `nb` and using it manually will
  probably corrupt the index. If something goes wrong with an index,
  fix it with `nb index reconcile`.

  An index is a text file named '.index' in any folder within a notebook.
  .index contains a list of filenames and the line number of each filename
  represents the id. .index files are included in the git repository so
  ids are preserved across systems.
```

#### `.pindex` Files

Any folder may contain an optional plain text file named `.pindex`
containing a list of basenames from that folder, one per line, that should
be treated as [pinned](#-pinning), meaning they appear first in some
list operations, including `nb` and [`nb ls`](#ls). Entries are added to a
`.pindex` file with [`nb pin`](#pin) and removed with [`nb unpin`](#unpin).

#### Archived Notebooks

A notebook is considered [archived](#archiving-notebooks)
when it contains a file named `.archived`
at the root level of the notebook directory.

## Tests

With more than 2,000 tests spanning tens of thousands of lines,
`nb` is really mostly a
[test suite](https://github.com/xwmx/nb/tree/master/test).
Tests run continuously [via GitHub Actions](https://github.com/xwmx/nb/actions)
on recent versions of both Ubuntu and macOS to account for differences between
BSD and GNU tools and Bash versions.
To run the tests locally, install
[Bats](https://github.com/bats-core/bats-core)
and the [recommended dependencies](#optional),
then run `bats test` within the project root directory. Run groups of
tests with globbing, e.g., `bats test/browse*` and `bats test/folders*`.

<p align="center">
  <a href="#overview">&nbsp;↑&nbsp;</a>
</p>

---

<p align="center">
  Copyright (c) 2015-present ·
  <a href="https://www.williammelody.com/">William Melody</a> ·
  <a href="https://github.com/xwmx/nb/blob/master/LICENSE">AGPLv3</a>
</p>

<p align="center">
  <a href="https://xwmx.github.io/nb">xwmx.github.io/nb</a>&nbsp;·
  <a href="https://github.com/xwmx/nb">github.com/xwmx/nb</a>
</p>

<p align="center">
  📝🔖🔒🔍📔
</p>

<p align="center">
  <a href="#top">&nbsp;↑&nbsp;</a>
</p>


</details>



</br>



[***GitHub - smallstep/cli: 🧰 A zero trust swiss army knife for working with X509, OAuth, JWT, OATH OTP, etc.***](https://github.com/smallstep/cli)

![GitHub last commit](https://img.shields.io/github/last-commit/smallstep/cli) ![GitHub Repo stars](https://img.shields.io/github/stars/smallstep/cli?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/smallstep/cli)



</br>



</br>



[***GitHub - loft-sh/vcluster: vcluster - Create fully functional virtual Kubernetes clusters - Each vcluster runs inside a namespace of the underlying k8s cluster. It&#39;s cheaper than creating separate full-blown clusters and it offers better multi-tenancy and isolation than regular namespaces.***](https://github.com/loft-sh/vcluster)

![GitHub last commit](https://img.shields.io/github/last-commit/loft-sh/vcluster) ![GitHub Repo stars](https://img.shields.io/github/stars/loft-sh/vcluster?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/loft-sh/vcluster)


***QUICK INSTALL***

```bash
curl -s -L "https://github.com/loft-sh/vcluster/releases/latest" | sed -nE 's!.*"([^"]*vcluster-linux-amd64)".*!https://github.com\1!p' | xargs -n 1 curl -L -o vcluster && chmod +x vcluster;
sudo mv vcluster /usr/local/bin;
```


</br>


<details>

<summary>README</summary> 

<br>
<a href="https://www.vcluster.com"><img src="docs/static/media/vcluster-logo-dark.svg"></a>

### **[Website](https://www.vcluster.com)** • **[Quickstart](https://www.vcluster.com/docs/getting-started/setup)** • **[Documentation](https://www.vcluster.com/docs/what-are-virtual-clusters)** • **[Blog](https://loft.sh/blog)** • **[Twitter](https://twitter.com/loft_sh)** • **[Slack](https://slack.loft.sh/)**

![Latest Release](https://img.shields.io/github/v/release/loft-sh/vcluster?style=for-the-badge&label=Latest%20Release&color=%23007ec6)
![License: Apache-2.0](https://img.shields.io/github/license/loft-sh/vcluster?style=for-the-badge&color=%23007ec6)

[![Join us on Slack!](docs/static/media/slack.svg)](https://slack.loft.sh/)

Create fully functional virtual Kubernetes clusters - Each vcluster runs inside a namespace of the underlying k8s cluster. It's cheaper than creating separate full-blown clusters and it offers better multi-tenancy and isolation than regular namespaces.

### Why Virtual Kubernetes Clusters?

- **Cluster Scoped Resources**: much more powerful than simple namespaces (virtual clusters allow users to use CRDs, namespaces, cluster roles etc.)
- **Ease of Use**: usable in any Kubernetes cluster and created in seconds either via a single command or [cluster-api](https://github.com/loft-sh/cluster-api-provider-vcluster)
- **Cost Efficient**: much cheaper and efficient than "real" clusters (single pod and shared resources just like for namespaces)
- **Lightweight**: built upon the ultra-fast k3s distribution with minimal overhead per virtual cluster (other distributions work as well)
- **Strict isolation**: complete separate Kubernetes control plane and access point for each vcluster while still being able to share certain services of the underlying host cluster
- **Cluster Wide Permissions**: allow users to install apps which require cluster-wide permissions while being limited to actually just one namespace within the host cluster
- **Great for Testing**: allow you to test different Kubernetes versions inside a single host cluster which may have a different version than the virtual clusters

Learn more on [www.vcluster.com](https://vcluster.com).

<br>

![vcluster Intro](docs/static/media/vcluster-comparison.png)

![vcluster Compatibility](docs/static/media/cluster-compatibility.png)


Learn more in the [documentation](https://vcluster.com/docs/what-are-virtual-clusters).

<br>

<p align="center">
⭐️ <strong>Do you like vcluster? Support the project with a star</strong> ⭐️
</p>

<br>

### Features

- **Certified Kubernetes Distribution** - vcluster itself is a [certified Kubernetes distribution](https://www.cncf.io/certification/software-conformance/) and is 100% Kubernetes API conform. Everything that works in a regular Kubernetes cluster works in vcluster
- **Lightweight & Low-Overhead** - Based on k3s, bundled in a single pod and with super-low resource consumption. Other distributions such as k0s or vanilla k8s are also supported
- **No Performance Degradation** - Pods are scheduled in the underlying host cluster, so they get no performance hit at all while running
- **Reduced Overhead On Host Cluster** - Split up large multi-tenant clusters into smaller vclusters to reduce complexity and increase scalability. Since most vcluster api requests and objects will not reach the host cluster at all, vcluster can greatly decrease pressure on the underlying Kubernetes cluster
- **Easy Provisioning** - Create via vcluster CLI, helm, kubectl, [cluster api](https://github.com/loft-sh/cluster-api-provider-vcluster), Argo CD or any of your favorite tools (it is basically just a StatefulSet)
- **No Admin Privileges Required** - If you can deploy a web app to a Kubernetes namespace, you will be able to deploy a vcluster as well
- **Single Namespace Encapsulation** - Every vcluster and all of its workloads are inside a single namespace of the underlying host cluster
- **Easy Cleanup** - Delete the host namespace and the vcluster plus all of its workloads will be gone immediately
- **Flexible & Versatile** - vcluster supports different storage backends (such as sqlite, mysql, postgresql & etcd), plugins, customizable sync behaviour, vcluster within vcluster setups and has many more additional configuration options to fit a multitude of different use cases

<br>

## Quick Start (~ 1 minute)
To learn more about vcluster, [**open the full getting started guide**](https://www.vcluster.com/docs/getting-started/setup).

### 1. Download vcluster CLI
Use one of the following commands to download the vcluster CLI binary from GitHub:

<details>
<summary>Mac (Intel/AMD)</summary>

```bash
curl -s -L "https://github.com/loft-sh/vcluster/releases/latest" | sed -nE 's!.*"([^"]*vcluster-darwin-amd64)".*!https://github.com\1!p' | xargs -n 1 curl -L -o vcluster && chmod +x vcluster;
sudo mv vcluster /usr/local/bin;
```

</details>

<details>
<summary>Mac (Silicon/ARM)</summary>

```bash
curl -s -L "https://github.com/loft-sh/vcluster/releases/latest" | sed -nE 's!.*"([^"]*vcluster-darwin-arm64)".*!https://github.com\1!p' | xargs -n 1 curl -L -o vcluster && chmod +x vcluster;
sudo mv vcluster /usr/local/bin;
```

</details>

<details>
<summary>Linux (AMD)</summary>

```bash
curl -s -L "https://github.com/loft-sh/vcluster/releases/latest" | sed -nE 's!.*"([^"]*vcluster-linux-amd64)".*!https://github.com\1!p' | xargs -n 1 curl -L -o vcluster && chmod +x vcluster;
sudo mv vcluster /usr/local/bin;
```

</details>

<details>
<summary>Linux (ARM)</summary>

```bash
curl -s -L "https://github.com/loft-sh/vcluster/releases/latest" | sed -nE 's!.*"([^"]*vcluster-linux-arm64)".*!https://github.com\1!p' | xargs -n 1 curl -L -o vcluster && chmod +x vcluster;
sudo mv vcluster /usr/local/bin;
```

</details>

<details>
<summary>Windows (Powershell)</summary>

```bash
md -Force "$Env:APPDATA\vcluster"; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]'Tls,Tls11,Tls12';
Invoke-WebRequest -UseBasicParsing ((Invoke-WebRequest -URI "https://github.com/loft-sh/vcluster/releases/latest" -UseBasicParsing).Content -replace "(?ms).*`"([^`"]*vcluster-windows-amd64.exe)`".*","https://github.com/`$1") -o $Env:APPDATA\vcluster\vcluster.exe;
$env:Path += ";" + $Env:APPDATA + "\vcluster";
[Environment]::SetEnvironmentVariable("Path", $env:Path, [System.EnvironmentVariableTarget]::User);
```

> If you get the error that Windows cannot find vcluster after installing it, you will need to restart your computer, so that the changes to the `PATH` variable will be applied.

</details>

<br>

Alternatively, you can download the binary for your platform from the [GitHub Releases](https://github.com/loft-sh/vcluster/releases) page and add this binary to your PATH.

<br>


### 2. Create a vcluster
```vash
vcluster create my-vcluster

# OR: Use --expose to create a vcluster with an externally accessible LoadBalancer
vcluster create my-vcluster --expose 

# OR: Use --isolate to create an isolated environment for the vcluster workloads
vcluster create my-vcluster --isolate
```

Take a look at the [vcluster docs](https://www.vcluster.com/docs/getting-started/deployment) to see how to deploy a vcluster using Helm or Kubectl instead.

### 3. Use the vcluster

Run in a terminal:
```bash
# Run any kubectl, helm, etc. command in your vcluster
kubectl get namespace
kubectl get pods -n kube-system
kubectl create namespace demo-nginx
kubectl create deployment nginx-deployment -n demo-nginx --image=nginx
kubectl get pods -n demo-nginx
```

### 4. Cleanup
```bash
vcluster delete my-vcluster
```

Alternatively, you could also delete the host-namespace using kubectl.

## Architecture
[![vcluster Intro](docs/static/media/diagrams/vcluster-architecture.svg)](https://www.vcluster.com)

## Contributing

Thank you for your interest in contributing! Please refer to
[CONTRIBUTING.md](https://github.com/loft-sh/vcluster/blob/main/CONTRIBUTING.md) for guidance.

<br>

---

This project is open-source and licensed under Apache 2.0, so you can use it in any private or commercial projects.


</details>



</br>



[***GitHub - rosineygp/mkdkr: mkdkr = Makefile + Docker***](https://github.com/rosineygp/mkdkr)

![GitHub last commit](https://img.shields.io/github/last-commit/rosineygp/mkdkr) ![GitHub Repo stars](https://img.shields.io/github/stars/rosineygp/mkdkr?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/rosineygp/mkdkr)



</br>



</br>



[***GitHub - mkdocs/mkdocs: Project documentation with Markdown.***](https://github.com/mkdocs/mkdocs)

![GitHub last commit](https://img.shields.io/github/last-commit/mkdocs/mkdocs) ![GitHub Repo stars](https://img.shields.io/github/stars/mkdocs/mkdocs?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/mkdocs/mkdocs)



</br>



</br>



[***GitHub - helm/chart-releaser: Hosting Helm Charts via GitHub Pages and Releases***](https://github.com/helm/chart-releaser)

![GitHub last commit](https://img.shields.io/github/last-commit/helm/chart-releaser) ![GitHub Repo stars](https://img.shields.io/github/stars/helm/chart-releaser?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/helm/chart-releaser)


***QUICK INSTALL***

```bash
curl -L "https://github.com/helm/chart-releaser/releases/download/$(curl -L -s "https://api.github.com/repos/helm/chart-releaser/releases/latest" | grep -Poe '"tag_name": "\K.*?(?=")' | head -n 1)/chart-releaser_$(curl -L -s "https://api.github.com/repos/helm/chart-releaser/releases/latest" | grep -Poe '"tag_name": "\K.*?(?=")' | head -n 1 | cut -c2- )_linux_amd64.tar.gz" | sudo tar -C /usr/bin -xzv
```


</br>


<details>

<summary>README</summary> 

# Chart Releaser

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
![CI](https://github.com/helm/chart-releaser/workflows/CI/badge.svg?branch=main&event=push)

**Helps Turn GitHub Repositories into Helm Chart Repositories**

`cr` is a tool designed to help GitHub repos self-host their own chart repos by adding Helm chart artifacts to GitHub Releases named for the chart version and then creating an `index.yaml` file for those releases that can be hosted on GitHub Pages (or elsewhere!).

## Installation

### Binaries (recommended)

Download your preferred asset from the [releases page](https://github.com/helm/chart-releaser/releases) and install manually.

### Homebrew

```console
$ brew tap helm/tap
$ brew install chart-releaser
```

### Go get (for contributing)

```console
$ # clone repo to some directory outside GOPATH
$ git clone https://github.com/helm/chart-releaser
$ cd chart-releaser
$ go mod download
$ go install ./...
```

### Docker (for Continuous Integration)

Docker images are pushed to the [helmpack/chart-releaser](https://quay.io/repository/helmpack/chart-releaser?tab=tags) Quay container registry. The Docker image is built on top of Alpine and its default entry-point is `cr`. See the [Dockerfile](./Dockerfile) for more details.

## Usage

Currently, `cr` can create GitHub Releases from a set of charts packaged up into a directory and create an `index.yaml` file for the chart repository from GitHub Releases.

```console
$ cr --help
Create Helm chart repositories on GitHub Pages by uploading Chart packages
and Chart metadata to GitHub Releases and creating a suitable index file

Usage:
  cr [command]

Available Commands:
  completion  generate the autocompletion script for the specified shell
  help        Help about any command
  index       Update Helm repo index.yaml for the given GitHub repo
  package     Package Helm charts
  upload      Upload Helm chart packages to GitHub Releases
  version     Print version information

Flags:
      --config string   Config file (default is $HOME/.cr.yaml)
  -h, --help            help for cr

Use "cr [command] --help" for more information about a command.
```

### Create GitHub Releases from Helm Chart Packages

Scans a path for Helm chart packages and creates releases in the specified GitHub repo uploading the packages.

```console
$ cr upload --help
Upload Helm chart packages to GitHub Releases

Usage:
  cr upload [flags]

Flags:
  -c, --commit string                  Target commit for release
  -b, --git-base-url string            GitHub Base URL (only needed for private GitHub) (default "https://api.github.com/")
  -r, --git-repo string                GitHub repository
  -u, --git-upload-url string          GitHub Upload URL (only needed for private GitHub) (default "https://uploads.github.com/")
  -h, --help                           help for upload
  -o, --owner string                   GitHub username or organization
  -p, --package-path string            Path to directory with chart packages (default ".cr-release-packages")
      --release-name-template string   Go template for computing release names, using chart metadata (default "{{ .Name }}-{{ .Version }}")
      --release-notes-file string      Markdown file with chart release notes. If it is set to empty string, or the file is not found, the chart description will be used instead
      --skip-existing                  Skip upload if release exists
  -t, --token string                   GitHub Auth Token

Global Flags:
      --config string   Config file (default is $HOME/.cr.yaml)
```

### Create the Repository Index from GitHub Releases

Once uploaded you can create an `index.yaml` file that can be hosted on GitHub Pages (or elsewhere).

```console
$ cr index --help
Update a Helm chart repository index.yaml file based on a the
given GitHub repository's releases.

Usage:
  cr index [flags]

Flags:
  -b, --git-base-url string            GitHub Base URL (only needed for private GitHub) (default "https://api.github.com/")
  -r, --git-repo string                GitHub repository
  -u, --git-upload-url string          GitHub Upload URL (only needed for private GitHub) (default "https://uploads.github.com/")
  -h, --help                           help for index
  -i, --index-path string              Path to index file (default ".cr-index/index.yaml")
  -o, --owner string                   GitHub username or organization
  -p, --package-path string            Path to directory with chart packages (default ".cr-release-packages")
      --pages-branch string            The GitHub pages branch (default "gh-pages")
      --pages-index-path string        The GitHub pages index path (default "index.yaml")
      --pr                             Create a pull request for index.yaml against the GitHub Pages branch (must not be set if --push is set)
      --push                           Push index.yaml to the GitHub Pages branch (must not be set if --pr is set)
      --release-name-template string   Go template for computing release names, using chart metadata (default "{{ .Name }}-{{ .Version }}")
      --remote string                  The Git remote used when creating a local worktree for the GitHub Pages branch (default "origin")
  -t, --token string                   GitHub Auth Token (only needed for private repos)

Global Flags:
      --config string   Config file (default is $HOME/.cr.yaml)
```

## Configuration

`cr` is a command-line application.
All command-line flags can also be set via environment variables or config file.
Environment variables must be prefixed with `CR_`.
Underscores must be used instead of hyphens.

CLI flags, environment variables, and a config file can be mixed.
The following order of precedence applies:

1. CLI flags
1. Environment variables
1. Config file

### Examples

The following example show various ways of configuring the same thing:

#### CLI

    cr upload --owner myaccount --git-repo helm-charts --package-path .deploy --token 123456789

#### Environment Variables

    export CR_OWNER=myaccount
    export CR_GIT_REPO=helm-charts
    export CR_PACKAGE_PATH=.deploy
    export CR_TOKEN="123456789"
    export CR_GIT_BASE_URL="https://api.github.com/"
    export CR_GIT_UPLOAD_URL="https://uploads.github.com/"
    export CR_SKIP_EXISTING=true

    cr upload

#### Config File

`config.yaml`:

```yaml
owner: myaccount
git-repo: helm-charts
package-path: .deploy
token: 123456789
git-base-url: https://api.github.com/
git-upload-url: https://uploads.github.com/
```

#### Config Usage

    cr upload --config config.yaml


`cr` supports any format [Viper](https://github.com/spf13/viper) can read, i. e. JSON, TOML, YAML, HCL, and Java properties files.

Notice that if no config file is specified, `cr.yaml` (or any of the supported formats) is loaded from the current directory, `$HOME/.cr`, or `/etc/cr`, in that order, if found.

#### Notes for Github Enterprise Users

For Github Enterprise, `chart-releaser` users need to set `git-base-url` and `git-upload-url` correctly, but the correct values are not always obvious to endusers.

By default they are often along these lines:

```
https://ghe.example.com/api/v3/
https://ghe.example.com/api/uploads/
```

If you are trying to figure out what your `upload_url` is try to use a curl command like this:
`curl -u username:token https://example.com/api/v3/repos/org/repo/releases`
and then look for `upload_url`. You need the part of the URL that appears before `repos/` in the path.

##### Known Bug

Currently, if you set the upload URL incorrectly, let's say to something like `https://example.com/uploads/`, then `cr upload` will appear to work, but the release will not be complete. When everything is working there should be 3 assets in each release, but instead there will only be the 2 source code assets. The third asset, which is what helm actually uses, is missing. This issue will become apparent when you run `cr index` and it always claims that nothing has changed, because it can't find the asset it expects for the release.

It appears like the [go-github Do call](https://github.com/google/go-github/blob/master/github/github.go#L520) does not catch the fact that the upload URL is incorrect and pass back the expected error. If the asset upload fails, it would be better if the release was rolled back (deleted) and an appropriate log message is be displayed to the user.

The `cr index` command should also generate a warning when a release has no assets attached to it, to help people detect and troubleshoot this type of problem.


</details>



</br>



[***GitHub - vidispine/hull: The incredible HULL - Helm Uniform Layer Library - is a Helm library chart to improve Helm chart based workflows***](https://github.com/vidispine/hull)

![GitHub last commit](https://img.shields.io/github/last-commit/vidispine/hull) ![GitHub Repo stars](https://img.shields.io/github/stars/vidispine/hull?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/vidispine/hull)



</br>


<details>

<summary>README</summary> 

# HULL - Helm Uniform Layer Library

This repository contains the HULL Helm library chart. It is designed to ease building, maintaining and configuring Kubernetes objects in Helm charts and can be added to any Helm chart as an addon to enhance functionality without any risk of breaking existing Helm chart configurations.

The chart itself and all documentation related to it can be found in the [`hull`](hull) folder which is the root folder of the HULL library helm chart. 

The Kubernetes API JSON Schemas are stored in the [`kubernetes-json-schema`](kubernetes-json-schema) folder. 

[![Build Status](https://dev.azure.com/arvato-systems-dmm/VPMS3%20CrossCutting/_apis/build/status/HULL/vidispine.hull.release?branchName=release-1.23)](https://dev.azure.com/arvato-systems-dmm/VPMS3%20CrossCutting/_build/latest?definitionId=589&branchName=release-1.23)

---

Below is the HULL charts [`README.md`](/hull/README.md):

---

> Abstractions need to be maintained - Kelsey Hightower

## Introduction

One major design aspect of [Helm](https://helm.sh) is that it forces the user to create individual abstractions of the Kubernetes configuration of applications. For each individual Helm Chart that is realized in form of YAML templates in a [Helm charts](https://helm.sh/docs/topics/charts/) `/templates` folder. These template files, containing boilerplate Kubernetes YAML code blocks on the one hand and custom configuration mappings utilizing Go Templating expressions on the other hand, provide the glue between the configuration of the application via the central `values.yaml` configuration file and the desired Kubernetes YAML output. Arguably this approach of per-application abstraction is suited well to create tailormade configuration packages for even the most specialized applications but comes at a cost of having a large overhead for simpler, recurring and off-the-shelf application packaging use cases. Creating, maintaining and (often) understanding the abstractions introduced by Helm Charts - especially when facing a high number of individual Helm charts from various sources - can become tedious and challenging.

The primary feature of the HULL library is the ability to remove customized YAML template files entirely from Helm chart workflows and thereby allowing to remove a level of abstraction. Using the HULL library chart, Kubernetes objects including all their properties can be completely and transparently specified in the `values.yaml`. The HULL library chart itself provides the uniform layer to streamline specification, configuration and rendering of Helm charts to achieve this. You can also think of it as a thin layer on top of the Kubernetes API to avoid the middleman between Helm Chart and Kubernetes API object configuration, yet providing flexibility when it is required to customize individual configuration options instead of requiring you to add each configuration switch manually to the templates. JSON schema validation based on the [Helm JSON validation feature](https://helm.sh/docs/topics/charts/#schema-files) (via `values.schema.json`) aids in writing Kubernetes API conforming objects right from the beginning when [using an IDE that supports live JSON schema validation](./hull/doc/json_schema_validation.md). Additional benefits (uniform inheritable object metadata, simplified inclusion of ConfigMaps/Secrets, cross-referencing values within the `values.yaml`, ...) are available with HULL which you can read about below in the **Key Features Overview**. But maybe most importantly, the HULL library can be added as a dependency to any existing Helm chart and be used side-by-side without breaking any existing Helm charts functionalities, see [adding the HULL library chart to a Helm chart](./hull/doc/setup.md) for more information. And lastly, by being a library chart itself, everything works 100% within the functionality that plain Helm offers - no additional tooling is introduced or involved.

**Your feedback on this project is valued, hence please comment or start a discussion in the `Issues` section or create feature wishes and bug reports. Thank you!**

The HULL library chart idea is partly inspired by the [common](
https://github.com/helm/charts/tree/master/incubator/common) Helm chart concept and for testing 

[![Gauge Badge](https://gauge.org/Gauge_Badge.svg)](https://gauge.org).

[![Build Status](https://dev.azure.com/arvato-systems-dmm/VPMS3%20CrossCutting/_apis/build/status/vidispine.hull?branchName=main)](https://dev.azure.com/arvato-systems-dmm/VPMS3%20CrossCutting/_build/latest?definitionId=589&branchName=main)

## Key Features Overview

As highlighted above, when included in a Helm chart the HULL library chart can take over the job of dynamically rendering Kubernetes objects from their given specifications from the `values.yaml` file alone. With YAML object construction deferred to the HULL library's Go Templating functions instead of custom YAML templates in the `/templates` folder you can centrally enforce best practices:

- Concentrate on what is needed to specify Kubernetes objects without having to add individual boilerplate YAML templates to your chart. This removes a common source of errors and maintenance from the regular Helm workflow. **To have the HULL rendered output conform to the Kubernetes API specification, a large number of unit tests validate the HULL rendered output against the Kubernetes API JSON schema.**

  For more details refer to the documentation on [JSON Schema Validation](./hull/doc/json_schema_validation.md).

- For all Kubernetes object types supported by HULL, **full configurational access to the Kubernetes object types properties is directly available**. This relieves chart maintainers from having to add missing configuration options one by one and the Helm chart users from forking the Helm chart to add just the properties they need for their configuration. Only updating the HULL chart to a newer version with matching Kubernetes API version is required to enable configuration of properties added to Kubernetes objects meanwhile in newer API versions. The HULL charts are versioned to reflect the minimal Kubernetes API versions supported by them. 

   For more details refer to the documentation on [Architecture Overview](./hull/doc/architecture.md).

- The single interface of the HULL library is used to both create and configure objects in charts for deployment. This fosters the mutual understanding of chart creators/maintainers and consumers of how the chart actually works and what it contains. Digging into the `/templates` folder to understand the Helm charts implications is not required anymore. To avoid any misconfiguration, the interface to the library - the `values.yaml` of the HULL library - is fully JSON validated. **When using an IDE supporting live JSON schema validation (e.g. VSCode) you can get IDE guidance when creating the HULL objects.  Before rendering, JSON schema conformance is validated by the HULL library.**

  For more details refer to the documentation on [JSON Schema Validation](./hull/doc/json_schema_validation.md).

- **Uniform and rich metadata is automatically attached to all objects created by the HULL library.** 
  - Kubernetes standard labels as defined for [Kubernetes](https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/) and [Helm](https://helm.sh/docs/chart_best_practices/labels/#standard-labels) are added to all objects metadata automatically. 
  - Additional custom labels and annotations metadata can be set hierarchically for:
    - all created Kubernetes objects or 
    - all created Kubernetes objects of a given type or 
    - any individual Kubernetes object. 

  For more details on metadata overwriting refer to the advanced example below.

- Flexible handling of ConfigMap and Secret input by choosing between inline specification of contents in `values.yaml` or import from external files for contents of larger sizes. When importing data from files the data can be either run through the templating engine or imported un-templated 'as is' if it already contains templating expressions that shall be passed on to the consuming application. **Adding ConfigMaps or Secrets to your deployment requires only a few lines of code.**

  For more details refer to the documentation on [ConfigMaps and Secrets](./hull/doc/configmaps_secrets.md).

- For more complex scenarios where actual values in the target YAML are subject to configurations in the `values.yaml`, there is **support to dynamically populate values by injecting Go Templating expressions defined in place of the value in the `values.yaml`**. For example, if your concrete container arguments depend on various other settings in `values.yaml` you can inject the conditions into the calculation of the arguments.

  For more details refer to the documentation on [Transformations](./hull/doc/transformations.md).

- Enable automatic hashing of referenced ConfigMaps and Secrets to facilitate pod restarts on changes of configuration (work in progress)

To learn more about the general architecture and features of the HULL library see the [Architecture Overview](./hull/doc/architecture.md)

## Important information

Some important things to mention first before looking at the library in more detail:

⚠️ **While there may be several benefits to rendering YAML via the HULL library please take note that it is a non-breaking addition to your Helm charts. The regular Helm workflow involving rendering of YAML templates in the `/templates` folder is completely unaffected by integration of the HULL library chart. Sometimes you might have very specific requirements on your configuration or object specification which the HULL library does not meet so you can use the regular Helm workflow for them and the HULL library for your more standard needs - easily in parallel in the same Helm chart.** ⚠️

⚠️ **Note that a single static file, the `hull.yaml`, must be copied 'as-is' without any modification from an embedded HULL charts root folder to the parent charts `/templates` folder to be able to render any YAML via HULL. It contains the code that initiates the HULL rendering pipeline, see [adding the HULL library chart to a Helm chart](./hull/doc/setup.md) for more details!** ⚠️

⚠️ **At this time HULL releases are tested against all existing non-beta and non-alpha Helm 3 CLI versions. Note that Helm CLI versions `3.0.x` are not compatible with HULL, all other currently existing non-beta and non-alpha versions are compatible.** ⚠️

⚠️ **It is intended to support the latest 3 major Kubernetes releases with corresponding HULL releases. At this time Kubernetes versions `1.22` and `1.23` and `1.24` have a matching and maintained HULL release.** ⚠️

## NEW! The HULL Tutorials

If you like a hands on approach you are invited to take a look at the [new HULL tutorials series at dev.to](https://dev.to/gre9ory/series/18319)! The eigth part tutorial will start from the very beginning of setting up Helm and creating a HULL based chart to finalizing a real life HULL based Helm Chart step by step. To highlight the differences to the regular Helm chart workflow the tutorials take the popular [`kubernetes-dashboard`](https://artifacthub.io/packages/helm/k8s-dashboard/kubernetes-dashboard) Helm chart as a source and transport it to a functionally equivalent HULL based Helm chart. In the end it shows that reducing the lines of configuration to create and maintain can be reduced by more than 50% when using a HULL based approach instead of the regular Helm style of writing charts!

## Creating and configuring a HULL based chart

The tasks of creating and configuring a HULL based helm chart can be considered as two sides of the same coin. Both sides interact with the same interface (the HULL library) to specify the objects that should be created. The task from a creators/maintainers perspective is foremost to provide the ground structure for the objects that make up the particular application which is to be wrapped in a Helm chart. The consumer of the chart is tasked with appropriately adding his system specific context to the ground structure wherein he has the freedom to change and even add or delete objects as needed to achieve his goals. At deploy time the creators base structure is merged with the consumers system-specific yaml file to build the complete configuration. Interacting via the same library interface fosters common understanding of how to work with the library on both sides and can eliminate most of the tedious copy&paste creation and examination heavy configuration processes.

So all that is needed to create a helm chart based on HULL is a standard scaffolded helm chart directory structure. Add the HULL library chart as a sub-chart, copy the `hull.yaml` from the HULL library chart to your parent Helm charts `/templates` folder. Then just configure the default objects to deploy via the `values.yaml` and you are done. There is no limit as to how many objects of which type you create for your deployment package.

But besides allowing to define more complex applications with HULL you could also use it to wrap simple Kubernetes Objects you would otherwise either deploy via kubectl (being out-of-line from the management perspective with helm releases) or have to write a significant amount of Helm boilerplate templates to achieve this. 

The base structure of the `values.yaml` understood by HULL is given here in the next section. This essentially forms the single interface for producing and consuming HULL based charts. Any object is only created in case it is defined and enabled in the `values.yaml`, this means you might want to pre-configure objects for consumers that would just need to enable them if they want to use them.

At the top level of the YAML structure, HULL distinguishes between `config` and `objects`. While the `config` sub-configuration is intended to deal with chart specific settings such as metadata and product settings, the concrete Kubernetes objects to be rendered are specified under the `objects` key.
An additional third top level key named `version` is allowed as well, when this is being set to the HULL charts version for example during the parent Helm Charts release pipeline it will automatically populate the label `vidispine.hull/version`on all objects indicating the HULL version that was used to render the objects.

### _The `config` section_

Within the `config` section you can configure general settings for your Helm chart.

| Parameter                       | Description                                                     | Default                      |                  Example |
| ------------------------------- | ----------------------------------------------------------------| -----------------------------| -----------------------------------------|
| `config` | Specification of configuration options for this chart. <br><br>Has only the following sub-fields: <br><br>`specific`<br>`general` | |
| `config.general` | In this section you might define everything that is not particular to a unique product but to a range of products you want to deploy via helm. See the subfields descriptions for their intended usage. <br><br>Has only the following sub-fields: <br><br>`nameOverride`<br>`fullnameOverride`<br>`createImagePullSecretsFromRegistries`<br>`globalImageRegistryServer`<br>`globalImageRegistryToFirstRegistrySecretServer`<br>`rbac`<br>`data`<br>`metadata` | |
| `config.general.nameOverride` | The name override is applied to values of metadata label `app.kubernetes.io/name`. If set this effectively replaces the chart name here.
| `config.general.fullnameOverride` | If set to a value, the fullname override is applied as a prefix to all object names and replaces the standard `<release>-<chart>` prefix pattern in object names. |  | `myapp` |
| `config.general.noObjectNamePrefixes` | If set, the object instance keys directly serve as the names for the Kubernetes objects created and are never prefixed. This is technically equivalent to setting `staticName` true on each object. Note that by setting this to `true` the value of `config.general.fullnameOverride` becomes irrelevant. | `false` | `true` |
| `config.general.createImagePullSecretsFromRegistries` | If true, image pull secrets are created from all registries defined in this Helm chart and are added to all pods. | `true` | `false` |
| `config.general.globalImageRegistryServer` | If not empty the `registry` field of all container `image` fields is set to the value given here. The setting of `config.general.globalImageRegistryToFirstRegistrySecretServer` is ignored if this field is non-empty. All defined explicit `registry` settings for an `image` are overwritten with this value.<br><br>Intended usage of this is to conveniently have all images pulled from a central docker registry in case of air-gap like deployment scenarios. <br><br>Contrary to setting `config.general.globalImageRegistryToFirstRegistrySecretServer` to `true` in this case the registry secret is typically defined outside of this helm chart and the registry secret's server is referenced by its name directly. If you use this feature and define the Docker registry secret outside of this Helm chart you may additionally need to add `imagePullSecrets` to your pods in case the referenced Docker registry is not insecure. | `""` | `mycompany.docker-registry.io`
| `config.general.globalImageRegistryToFirstRegistrySecretServer` | If true and `config.general.globalImageRegistryServer` is empty, the `registry` field of all container `image` fields is set to the `server` field of the first found `registry` object. Note that this is the registry with the lowest alphanumeric key name if you provide multiple `registry` obejcts. Should normally be used together with setting `config.general.createImagePullSecretsFromRegistries` to `true` to benefit from autopopulated `imagePullSecrets` and accordingly set `registry`. Explicit `registry` settings for an `image` are overwritten with this value.<br><br>Intended usage of this setting is to conveniently have all images pulled from a central docker registry in case of air-gap like deployment scenarios.  | `false` | `true`
| `config.general.rbac` | Global switch which enables RBAC objects for installation. <br><br> If `true` all enabled RBAC objects are deployed to the cluster, if `false` no RBAC objects are created at all.<br><br> RBAC objects that are deployable are:<br>`roles`<br>`rolebindings`<br>`clusterroles`<br>`clusterrolebindings`  | `true` | `false` |
| `config.general.data` | Free form field whereas subfields of this field should have a clearly defined meaning in the context of your product suite. <br><br>For example, assume all of your products or microservices (each coming as a separate helm chart) depends on the same given endpoints (authentication, configuration, ...). You might have a shared Kubernetes job executed by each helm chart which targets those endpoints. Now you could specify an external HULL `values.yaml` containing the job specification and the endpoint definition here in a way you see fit and construct an overlay `values.yaml` rendered on top of each deployment and have a unified mechanism in place.  | `{}` |
| `config.general.metadata` | Defined metadata fields here will be automatically added to all objects metadata. <br><br>Has only the following sub-fields: <br><br>`labels`<br>`annotations`| | 
| `config.general.metadata.labels` | Labels that are added to all objects. The `common` labels refer to the Kubernetes and Helm common labels and `custom` labels can be freely specified. <br><br>Has only the following sub-fields: <br><br>`common`<br>`custom`| | 
| `config.general.metadata.labels.common` | Common labels specification as defined in https://helm.sh/docs/chart_best_practices/labels/ and https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/. <br><br>Unless specifically overwritten with empty values (`''`) all metadata labels are automatically added to all objects according to their default definition. It should be considered to set a value for `config.general.metadata.labels.common.'app.kubernetes.io/part-of'` if the helm chart is part-of a product suite. | | 
| `config.general.metadata.labels.common.'app.kubernetes.io/managed-by'` | Managed by metadata. | `{{ .Release.Service }}` |
| `config.general.metadata.labels.common.'app.kubernetes.io/version'` | Version metadata. | `{{ .Chart.AppVersion }}` |
| `config.general.metadata.labels.common.'app.kubernetes.io/part-of'` | Part-of metadata. | `"unspecified"` |
| `config.general.metadata.labels.common.'app.kubernetes.io/name'` | Name metadata. | `{{ printf "%s-%s" .ChartName <hullObjectKey> }}`
| `config.general.metadata.labels.common.'app.kubernetes.io/instance'` | Instance metadata. | `{{ .Release.Name }}`
| `config.general.metadata.labels.common.'app.kubernetes.io/component'` | Component metadata. | `<hullObjectKey>`
| `config.general.metadata.labels.common.'helm.sh/chart'` | Helm metadata. | `{{ (printf "%s-%s" .Chart.Name .Chart.Version) | replace "+" "_" }}`
| `config.general.metadata.labels.custom` | All specified custom labels are automatically added to all objects of this helm chart. | `{}`| 
| `config.general.metadata.annotations` | Annotations that are added to all objects. The `custom` labels can be freely specified. <br><br>Has only the following sub-fields: <br><br>`custom`. | 
| `config.general.metadata.annotations.custom` | All specified custom annotations are automatically added to all objects of this helm chart. | `{}`| 
| `config.specific` | Free form field that holds configuration options that are specific to the specific product contained in the helm chart. Typically the values specified here ought to be used to populate the contents of configuration files that a particular applications read their configuration from at startup. Hence the `config.specific` fields are typically being consumed in ConfigMaps or Secrets. | `{}` | `maxDatepickerRange:`&#160;`50`<br>`defaultPoolColor:`&#160;`"#FB6350"`<br>`updateInterval:`&#160;`60000`

### _The `objects` section_

The top-level object types beneath `hull.objects` represent the supported Kubernetes object types you might want to create instances from. Each object type is a dictionary where the entries values are the objects properties and each object has it's own key which is unique to the object type it belongs to. Further K8S object types can be added as needed to the library so it can easily be extended. 

#### _Keys of object instances_

One important aspect is that for all top-level object types, instances of a particular type are always identified by a key which is unique to the instance and object type combination. The same key can however be used for instances of different object types.

By having keys that identify instances you can:

- do multi-layered merging of object properties by stacking `values.yaml` files on top of each other. You might start with defining the default object structure of the application or micro service defined in the given helm chart. Then you might add a `values.yaml` layer for a particular environment like staging or production. Then you might add a `values.yaml` layer for credentials. And so on. By uniquely identifying the instances of a particular K8s object type it becomes easy to adjust the objects properties through a multitude of layers.
- use the key of an instance for naming the instance. All instance names are constructed by the following ground rule: `{{ printf "%s-%s-%s" .Release.Name .Chart.Name key }}`. This generates unique, dynamic names per object type and release + instance key combination. 

  For example, assuming the parent Helm chart is named `my_webservice` and the release named `staging` and given this specification in `values.yaml`:

  ```yaml
  hull:
    objects:
      deployment:
        nginx:
          pod:
            containers:
              nginx:
                repository: nginx
                tag: 1.14.2
  ```

  a Kubernetes deployment object with the following `metadata.name` is created:

  `my_webservice-staging-nginx`

  > Note that you can opt to define a static name for instances you create by adding a property `staticName: true` to your objects definition. If you do so the objects name will exactly match the key name you chose.

- each particular instance can have an `enabled` sub-field set to `true` or `false`. This way you can predefine instances of object types in your helm charts `values.yaml` but not deploy them in a default scenario. Or enable them by default and refrain from deploying them in a particular environment by disabling them in an superimposed system specific `values.yaml`. Note that unless you explicitly specify `enabled: false` each instance you define will be created by default, a missing `enabled` key is equivalent to `enabled: true`.

- cross-referencing objects within a helm chart by the instance key is a useful feature of the HULL library. This is possible in these contexts:
  -  when a reference to a ConfigMap or Secret comes into play you can just use the key of the targeted instance and the dynamic name will be rendered in the output. This is possible for referencing 
    - a ConfigMap or Secret behind a Volume or 
    - a Secret behind an Ingress' TLS specification or
    - a ConfigMap or Secret behind an environment value added to a container spec.
  - when referencing Services in the backend of an ingress' host you can specify the key to reference the backend service.
  
  > Note that you can in these cases opt to refer to a static name instead too. Adding a property `staticName: true` to the dictionary with your reference will force the referenced objects name to exactly match the name you entered.

#### _Values of object instances_

The values of object instance keys reflects the Kubernetes objects to create for the chart. To specify these objects efficiently, the available properties for configuration can be split into three groups:

1. Basic HULL object configuration with [hull.ObjectBase.v1](doc/object_base.md) whose properties are available for all object types and instances. These are `enabled`, `staticName`, `annotations` and `labels`. 

    Given the example of a `deployment` named `nginx` you can add the following properties of [hull.ObjectBase.v1](doc/object_base.md) to the object instance:

    ```yaml
    hull:
      objects:
        deployment:
          nginx: # unique key/identifier of the deployment to create
            staticName: true # property of hull.ObjectBase.v1
                             # forces the metadata.name to be just the <KEY> 'nginx' 
                             # and not a dynamic name '<CHART>-<RELEASE>-<KEY>' which 
                             # would be the better default behavior of creating 
                             # unique object names for all objects.
            enabled: true    # property of hull.ObjectBase.v1
                             # this deployment will be rendered to a YAML object if enabled
            labels:
              demo_label: "demo" # property of hull.ObjectBase.v1
                                 # add all labels here that shall be added 
                                 # to the object instance metadata section
            annotations:
              demo_annotation: "demo" # property of hull.ObjectBase.v1
                                      # add all annotations here that shall be added 
                                      # to the object instance metadata section
            pod: 
              ... # Here would come the hull.PodTemplate.v1 definition
                  # see below for details

    ```

2. Specialized HULL object properties for some object types. Below is a reference of which object type supports which special properties in addition to the basic object configuration. 

    Again given the example of a `deployment` named `nginx` you would want to add properties of the HULL [**hull.PodTemplate.v1**](doc/objects_pod.md) to the instance. With them you set the `pod` property to define the pod template (initContainers, containers, volumes, ...) and can add `templateLabels` and `templateAnnotations` just to the pods created `metadata` and not the deployment objects `metadata` section:

    ```yaml
    hull:
      objects:
        deployment:
          nginx: 
            staticName: true 
            enabled: true 
            labels: 
              demo_label: "demo" 
            annotations: 
              demo_annotation: "demo" 
            templateLabels: # property of hull.PodTemplate.v1 to define 
                            # labels only added to the pod
              demo_pod_label: "demo pod" 
            templateAnnotations: # property of hull.PodTemplate.v1 to define 
                            # annotations only added to the pod
              demo_pod_annotation: "demo pod"
            pod: # property of hull.PodTemplate.v1 to define the pod template
              containers:
                nginx: # all containers of a pod template are also referenced by a 
                      # unique key to make manipulating them easy.
                  image:
                    repository: nginx # specify repository and tag
                                      # separately with HULL for easier composability
                    tag: 1.14.2
                  ... # further properties (volumeMounts, affinities, ...)

    ```
3. Kubernetes object properties. For each object type it is basically possible to specify all existing Kubernetes properties. In case a HULL property overwrites a identically named Kubernetes property the HULL property has precedence. Even if a HULL property overrides a Kubernetes property it is intended to provide the same complete configuration options, even if sometimes handled differently by HULL. 

    Some of the typical top-level Kubernetes object properties and fields don't require setting them with HULL based objects because they can be deducted automatically:
    - the `apiVersion` and `kind` are determined by the HULL object type and Kubernetes API version and don't require to be explicitly set (except for objects of type `customresource`).
    - the top-level `metadata` dictionary on objects is handled by HULL via the `annotations` and `labels` fields and the naming rules explained above. So the `metadata` field does not require configuration and is hence not configurable for any object. 

    Some lower level structures are also converted from the Kubernetes API array form to a dictionary form or are modified to improve working with them. This also enables more sophisticated merging of layers since arrays don't merge well, they only can be overwritten completely. Overwriting arrays however can make it hard to forget about elements that are contained in the default form of the array (you would need to know that they existed in the first place). In short, for a layered configuration approach without an endless amount of elements the dictionary is preferable for representing data since it offers a much better merging support.

    So again using the example of a `deployment` named `nginx` you can add the remaining available Kubernetes properties to the object instance which are not handled by HULL as shown below. For a `deployment` specifically you can add all the remaining properties defined in the `deploymentspec` API schema from [**deploymentspec-v1-apps**](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#deploymentspec-v1-apps) which are `minReadySeconds`, `paused`, `progressDeadlineSeconds`, `replicas`, `revisionHistoryLimit` and `strategy`. If properties are marked as mandatory in the Kubernetes JSON schema you must provide them otherwise the rendering process will fail:

    ```yaml
    hull:
      objects:
        deployment:
          nginx: 
            staticName: true 
            enabled: true 
            labels: 
              demo_label: "demo" 
            annotations: 
              demo_annotation: "demo" 
            pod:
              ... # Here would come the hull.PodTemplate.v1 definition
                  # see above for details 
            replicas: 3 # property from the Kubernetes API deploymentspec
            strategy: # property from the Kubernetes API deploymentspec
              type: Recreate
            ... # further Kubernetes API deploymentspec options

    ```

#### _Composing objects with HULL_

Here is an overview of which top level properties are available for which object type in HULL. The HULL properties are grouped by the respective HULL JSON schema group they belong to. A detailed description of these groups and their properties is found in the documentation of this helm chart and the respective linked documents.

**[Workloads APIs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#-strong-workloads-apis-strong-)**

HULL<br> Object Type<br>&#160; | HULL <br>Properties | Kubernetes/External<br> Properties
------------------------------ | --------------------| ----------------------------------
`deployment` | [**hull.ObjectBase.v1**](doc/objects_base.md)<br>`enabled`<br>`annotations`<br>`labels`<br>`staticName`<br><br>[**hull.PodTemplate.v1**](doc/objects_pod.md)<br>`templateAnnotations`<br>`templateLabels`<br>`pod` | [**deploymentspec-v1-apps**](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#deploymentspec-v1-apps)<br>`minReadySeconds`<br>`paused`<br>`progressDeadlineSeconds`<br>`replicas`<br>`revisionHistoryLimit`<br>`strategy` 
`job` | [**hull.ObjectBase.v1**](doc/objects_base.md)<br>`enabled`<br>`annotations`<br>`labels`<br>`staticName`<br><br>[**hull.PodTemplate.v1**](doc/objects_pod.md)<br>`templateAnnotations`<br>`templateLabels`<br>`pod` | [**jobspec-v1-batch**](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#jobspec-v1-batch)<br>`activeDeadlineSeconds`<br>`backoffLimit`<br>`completionMode`<br>`completions`<br>`manualSelector`<br>`parallelism`<br>`selector`<br>`suspend`<br>`ttlSecondsAfterFinished` 
`daemonset` | [**hull.ObjectBase.v1**](doc/objects_base.md)<br>`enabled`<br>`annotations`<br>`labels`<br>`staticName`<br><br>[**hull.PodTemplate.v1**](doc/objects_pod.md)<br>`templateAnnotations`<br>`templateLabels`<br>`pod` | [**daemonsetspec-v1-apps**](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#daemonsetspec-v1-apps)<br>`minReadySeconds`<br>`revisionHistoryLimit`<br>`updateStrategy` 
`statefulset` | [**hull.ObjectBase.v1**](doc/objects_base.md)<br>`enabled`<br>`annotations`<br>`labels`<br>`staticName`<br><br>[**hull.PodTemplate.v1**](doc/objects_pod.md)<br>`templateAnnotations`<br>`templateLabels`<br>`pod` | [**statefulsetspec-v1-apps**](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#statefulsetspec-v1-apps)<br>`podManagementPolicy`<br>`replicas`<br>`revisionHistoryLimit`<br>`serviceName`<br>`updateStrategy`<br>`serviceName`<br>`volumeClaimTemplates` 
`cronjob` | [**hull.ObjectBase.v1**](doc/objects_base.md)<br>`enabled`<br>`annotations`<br>`labels`<br>`staticName`<br><br>[**hull.Job.v1**](./hull/README.md)<br>`job` | [**cronjobspec-v1-batch**](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#cronjobspec-v1-batch)<br>`concurrencyPolicy`<br>`failedJobsHistoryLimit`<br>`schedule`<br>`startingDeadlineSeconds`<br>`successfulJobsHistoryLimit`<br>`suspend` 

**[Service APIs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#-strong-service-apis-strong-)**
HULL<br> Object Type<br>&#160; | HULL <br>Properties | Kubernetes/External<br> Properties
------------------------------ | --------------------| ----------------------------------
`endpoints` | [**hull.ObjectBase.v1**](doc/objects_base.md)<br>`enabled`<br>`annotations`<br>`labels`<br>`staticName` | [**endpoints-v1-core**](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#endpoints-v1-core)<br>`subsets`
`endpointslice` | [**hull.ObjectBase.v1**](doc/objects_base.md)<br>`enabled`<br>`annotations`<br>`labels`<br>`staticName` | [**endpointslice-v1-discovery-k8s-io**](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#endpointslice-v1-discovery-k8s-io)<br>`addressType`<br>`endpoints`<br>`ports`
`service` | [**hull.ObjectBase.v1**](doc/objects_base.md)<br>`enabled`<br>`annotations`<br>`labels`<br>`staticName`<br><br>[**hull.Service.v1**](doc/objects_service.md)<br>`ports` | [**servicespec-v1-core**](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#servicespec-v1-core)<br>`allocateLoadBalancerNodePorts`<br>`clusterIP`<br>`clusterIPs`<br>`externalIPs`<br>`externalName`<br>`externalTrafficPolicy`<br>`healthCheckNodePort`<br>`internalTrafficPolicy`<br>`ipFamilies`<br>`ipFamilyPolicy`<br>`loadBalancerClass`<br>`loadBalancerIP`<br>`loadBalancerSourceRanges`<br>`publishNotReadyAddresses`<br>`selector`<br>`sessionAffinity`<br>`sessionAffinityConfig`<br>`topologyKeys`<br>`type`
`ingress` | [**hull.ObjectBase.v1**](doc/objects_base.md)<br>`enabled`<br>`annotations`<br>`labels`<br>`staticName`<br><br>[**hull.Ingress.v1**](doc/objects_ingress.md)<br>`tls`<br>`rules` | [**ingressspec-v1-networking-k8s-io**](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#ingressspec-v1-networking-k8s-io)<br>`defaultBackend`<br>`ingressClassName`
`ingressclass` | [**hull.ObjectBase.v1**](doc/objects_base.md)<br>`enabled`<br>`annotations`<br>`labels`<br>`staticName` | [**ingressclassspec-v1-networking-k8s-io**](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#ingressclassspec-v1-networking-k8s-io)<br>`controller`<br>`parameters`

**[Config and Storage APIs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#-strong-config-and-storage-apis-strong-)**
HULL<br> Object Type<br>&#160; | HULL <br>Properties | Kubernetes/External<br> Properties
------------------------------ | --------------------| ----------------------------------
`configmap` | [**hull.ObjectBase.v1**](doc/objects_base.md)<br>`enabled`<br>`annotations`<br>`labels`<br>`staticName`<br><br>[**hull.VirtualFolder.v1**](doc/objects_configmaps_secrets.md)<br>`data` |  [**configmap-v1-core**](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#configmap-v1-core)<br>`binaryData`<br>`immutable`
`secret` | [**hull.ObjectBase.v1**](doc/objects_base.md)<br>`enabled`<br>`annotations`<br>`labels`<br>`staticName`<br><br>[**hull.VirtualFolder.v1**](doc/objects_configmaps_secrets.md)<br>`data` |  [**secret-v1-core**](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#secret-v1-core)<br>`immutable`<br>`stringData`<br>`type` 
`registry` | [**hull.ObjectBase.v1**](doc/objects_base.md)<br>`enabled`<br>`annotations`<br>`labels`<br>`staticName`<br><br>[**hull.Registry.v1**](doc/objects_registry.md)<br>`server`<br>`username`<br>`password` | [**secret-v1-core**](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#secret-v1-core)
`persistentvolumeclaim` | [**hull.ObjectBase.v1**](doc/objects_base.md)<br>`enabled`<br>`annotations`<br>`labels`<br>`staticName` |  [**persistentvolumeclaimspec-v1-core**](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#persistentvolumeclaimspec-v1-core)<br>`accessModes`<br>`dataSource`<br>`resources`<br>`selector`<br>`storageClassName`<br>`volumeMode`<br>`volumeName`
`storageclass` | [**hull.ObjectBase.v1**](doc/objects_base.md)<br>`enabled`<br>`annotations`<br>`labels`<br>`staticName` |  [**storageclass-v1-storage-k8s-io**](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#storageclass-v1-storage-k8s-io)<br>`allowVolumeExpansion`<br>`allowedTopologies`<br>`mountOptions`<br>`parameters`<br>`provisioner`<br>`reclaimPolicy`<br>`volumeBindingMode`

**[Metadata APIs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#-strong-metadata-apis-strong-)**
HULL<br> Object Type<br>&#160; | HULL <br>Properties | Kubernetes/External<br> Properties
------------------------------ | --------------------| ----------------------------------
`customresource` | [**hull.ObjectBase.v1**](doc/objects_base.md)<br>`enabled`<br>`annotations`<br>`labels`<br>`staticName`<br><br>[**hull.CustomResource.v1**](doc/objects_customresource.md)<br>`apiVersion`<br>`kind`<br>`spec`
`limitrange` | [**hull.ObjectBase.v1**](doc/objects_base.md)<br>`enabled`<br>`annotations`<br>`labels`<br>`staticName` | [**limitrange-v1-core**](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#limitrange-v1-core)<br>`limits`
`horizontalpodautoscaler` | [**hull.ObjectBase.v1**](doc/objects_base.md)<br>`enabled`<br>`annotations`<br>`labels`<br>`staticName`<br><br>[**hull.HorizontalPodAutoscaler.v1**](doc/objects_horizontalpodautoscaler.md)<br>`scaleTargetRef` | [**horizontalpodautoscalerspec-v2-autoscaling**](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#horizontalpodautoscalerspec-v2-autoscaling)<br>`behavior`<br>`maxReplicas`<br>`metrics`<br>`minReplicas`
`mutatingwebhookconfiguration` | [**hull.ObjectBase.v1**](doc/objects_base.md)<br>`enabled`<br>`annotations`<br>`labels`<br>`staticName`<br><br>[**hull.MutatingWebhook.v1**](doc/objects_base_webhook.md)<br>`webhooks`
`poddisruptionbudget` | [**hull.ObjectBase.v1**](doc/objects_base.md)<br>`enabled`<br>`annotations`<br>`labels`<br>`staticName` | [**poddisruptionbudgetspec-v1-policy**](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#poddisruptionbudgetspec-v1-policy)<br>`maxUnavailable`<br>`minAvailable`<br>`selector`
`validatingwebhookconfiguration` | [**hull.ObjectBase.v1**](doc/objects_base.md)<br>`enabled`<br>`annotations`<br>`labels`<br>`staticName`<br><br>[**hull.ValidatingWebhook.v1**](doc/objects_base_webhook.md)<br>`webhooks` 
`priorityclass` | [**hull.ObjectBase.v1**](doc/objects_base.md)<br>`enabled`<br>`annotations`<br>`labels`<br>`staticName` | [**priorityclass-v1-scheduling-k8s-io**](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#priorityclass-v1-scheduling-k8s-io)<br>`description`<br>`globalDefault`<br>`preemptionPolicy`<br>`value`
`podsecuritypolicy` | [**hull.ObjectBase.v1**](doc/objects_base.md)<br>`enabled`<br>`annotations`<br>`labels`<br>`staticName` | [**podsecuritypolicyspec-v1beta1-policy**](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#podsecuritypolicyspec-v1beta1-policy)<br>`allowPrivilegeEscalation`<br>`allowedCSIDrivers`<br>`allowedCapabilities`<br>`allowedFlexVolumes`<br>`allowedHostPaths`<br>`allowedProcMountTypes`<br>`allowedUnsafeSysctls`<br>`defaultAddCapabilities`<br>`defaultAllowPrivilegeEscalation`<br>`forbiddenSysctls`<br>`fsGroup`<br>`hostIPC`<br>`hostNetwork`<br>`hostPID`<br>`hostPorts`<br>`privileged`<br>`readOnlyRootFilesystem`<br>`requiredDropCapabilities`<br>`runAsGroup`<br>`runAsUser`<br>`runtimeClass`<br>`seLinux`<br>`supplementalGroups`<br>`volumes`

**[Cluster APIs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#-strong-cluster-apis-strong-)**
HULL<br> Object Type<br>&#160; | HULL <br>Properties | Kubernetes/External<br> Properties
------------------------------ | --------------------| ----------------------------------
`clusterrole` | [**hull.ObjectBase.v1**](doc/objects_base.md)<br>`enabled`<br>`annotations`<br>`labels`<br>`staticName`<br><br>[**hull.Rule.v1**](doc/objects_role.md)<br>`rules` |  [**clusterrole-v1-rbac-authorization-k8s-io**](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#clusterrole-v1-rbac-authorization-k8s-io)<br>`aggregationRule`
`clusterrolebinding` | [**hull.ObjectBase.v1**](doc/objects_base.md)<br>`enabled`<br>`annotations`<br>`labels`<br>`staticName` |  [**clusterrolebinding-v1-rbac-authorization-k8s-io**](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#clusterrolebinding-v1-rbac-authorization-k8s-io)<br>`roleRef`<br>`subjects`
`namespace` | [**hull.ObjectBase.v1**](doc/objects_base.md)<br>`enabled`<br>`annotations`<br>`labels`<br>`staticName` |  [**namespace-v1-core**](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#namespace-v1-core)<br>`spec`<br>`status`
`persistentvolume` | [**hull.ObjectBase.v1**](doc/objects_base.md)<br>`enabled`<br>`annotations`<br>`labels`<br>`staticName` |  [**persistentvolumespec-v1-core**](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#persistentvolumespec-v1-core)<br>`accessModes`<br>`awsElasticBlockStore`<br>`azureDisk`<br>`azureFile`<br>`capacity`<br>`cephfs`<br>`cinder`<br>`claimRef`<br>`csi`<br>`fc`<br>`flexVolume`<br>`flocker`<br>`gcePersistentDisk`<br>`glusterfs`<br>`hostPath`<br>`iscsi`<br>`local`<br>`mountOptions`<br>`nfs`<br>`nodeAffinity`<br>`persistentVolumeReclaimPolicy`<br>`photonPersistentDisk`<br>`portworxVolume`<br>`quobyte`<br>`rbd`<br>`scaleIO`<br>`storageClassName`<br>`storageos`<br>`volumeMode`<br>`vsphereVolume`
`role` | [**hull.ObjectBase.v1**](doc/objects_base.md)<br>`enabled`<br>`annotations`<br>`labels`<br>`staticName`<br><br>[**hull.Rule.v1**](doc/objects_role.md)<br>`rules` |  [**role-v1-rbac-authorization-k8s-io**](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#role-v1-rbac-authorization-k8s-io)
`rolebinding` | [**hull.ObjectBase.v1**](doc/objects_base.md)<br>`enabled`<br>`annotations`<br>`labels`<br>`staticName` |  [**rolebinding-v1-rbac-authorization-k8s-io**](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#rolebinding-v1-rbac-authorization-k8s-io)<br>`roleRef`<br>`subjects`
`serviceaccount` | [**hull.ObjectBase.v1**](doc/objects_base.md)<br>`enabled`<br>`annotations`<br>`labels`<br>`staticName` |  [**serviceaccount-v1-core**](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#serviceaccount-v1-core)<br>`automountServiceAccountToken`<br>`imagePullSecrets`<br>`secrets`
`resourcequota` | [**hull.ObjectBase.v1**](doc/objects_base.md)<br>`enabled`<br>`annotations`<br>`labels`<br>`staticName` |  [**resourcequotaspec-v1-core**](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#resourcequotaspec-v1-core)<br>`hard`<br>`scopeSelector`<br>`scopes`
`networkpolicy` | [**hull.ObjectBase.v1**](doc/objects_base.md)<br>`enabled`<br>`annotations`<br>`labels`<br>`staticName` |  [**networkpolicyspec-v1-networking-k8s-io**](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#networkpolicyspec-v1-networking-k8s-io)<br>`egress`<br>`ingress`<br>`podSelector`<br>`policyTypes`

**Other APIs**
HULL<br> Object Type<br>&#160; | HULL <br>Properties | Kubernetes/External<br> Properties
------------------------------ | --------------------| ----------------------------------
`servicemonitor` | [**hull.ObjectBase.v1**](doc/objects_base.md)<br>`enabled`<br>`annotations`<br>`labels`<br>`staticName` | [**ServiceMonitor CRD**](https://github.com/prometheus-community/helm-charts/blob/main/charts/kube-prometheus-stack/crds/crd-servicemonitors.yaml)<br>`spec`

## Testing and installing a HULL based chart
To test or install a chart based on HULL the standard Helm v3 tooling is usable. See also the Helm documentation at the [Helm website](https://helm.sh). 

### Testing a HULL based chart

To inspect the outcome of a specific `values.yaml` configuration you can simply render the templates which would be deployed to Kubernetes and inspect them with the below command adapted to your needs:

  `<PATH_TO_HELM_V3_BINARY> template --debug --namespace <CHART_RELEASE_NAMESPACE> --kubeconfig <PATH_TO_K8S_CLUSTER_KUBECONFIG> -f <PATH_TO_SYSTEM_SPECIFIC_VALUES_YAML> --output-dir <PATH_TO_OUTPUT_DIRECTORY> <PATH_TO_CHART_DIRECTORY>`

### Install or upgrade a release: 

Installing or upgrading a chart using HULL follows the standard procedures for every Helm chart:

  `<PATH_TO_HELM_V3_BINARY> upgrade --install --debug --create-namespace --atomic --namespace <CHART_RELEASE_NAMESPACE> --kubeconfig <PATH_TO_K8S_CLUSTER_KUBECONFIG> -f <PATH_TO_SYSTEM_SPECIFIC_VALUES_YAML> <RELEASE_NAME> <PATH_TO_CHART_DIRECTORY>`


## First Examples

Using the nginx deployment example from the Kubernetes documentation https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#creating-a-deployment as something we want to create with our HULL based Helm chart:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
```

To render this analogously using the HULL library your chart needs to be [setup for using HULL](./hull/doc/setup.md). In the following section we assume the parent Helm chart is named `hull-test` and we use the `helm template` command to test render the `values.yaml`'s.

### Minimal Example

A minimal example of creating the expected result from above would be to create a `values.yaml` like below in your parent chart (commented with some explanations). Note that some default features of HULL such as RBAC and dynamic naming are explicitly disabled here to obtain the output matching the above example closely:

```yaml
hull:
  config:
    general:
      rbac: false # Don't render RBAC objects. By default HULL would provide 
                  # a 'default' Role and 'default' RoleBinding associated with 
                  # a 'default' ServiceAccount to use for all pods.
                  # You can modify this as needed. Here we turn it off to not 
                  # render the default RBAC objects.
  objects:
    serviceaccount:
      default:
        enabled: false # The release specific 'default' ServiceAccount created
                       # for a release by default is disabled here. In this case 
                       # it will not be rendered out and automatically used as 
                       # 'serviceAccountName' in the pod templates. 
    deployment:
      nginx: # all object instances have a key used for naming the objects and 
             # allowing to overwrite properties in multiple values.yaml layers
        staticName: true # forces the metadata.name to be just the <KEY> 'nginx' 
                         # and not a dynamic name '<CHART>-<RELEASE>-<KEY>' which 
                         # would be the better default behavior of creating 
                         # unique object names for all objects.
        replicas: 3
        pod:
          containers:
            nginx: # all containers of a pod template are also referenced by a 
                   # unique key to make manipulating them easy.
              image:
                repository: nginx
                tag: 1.14.2
              ports:
                http: # unique key per container here too. All key-value structures
                      # which are finally arrays in the K8S objects are converted to 
                      # arrays on rendering the chart.
                  containerPort: 80
```

This produces the following rendered deployment when running the `helm template` command (commented with some brief explanations):

```yaml
apiVersion: apps/v1 # derived from object type 'deployment'
kind: Deployment # derived from object type 'deployment'
metadata: 
  annotations: {}
  labels: # standard Kubernetes metadata is created always automatically.
    app.kubernetes.io/component: nginx 
    app.kubernetes.io/instance: release-name
    app.kubernetes.io/managed-by: Helm
    app.kubernetes.io/name: hull-test
    app.kubernetes.io/part-of: undefined
    app.kubernetes.io/version: 1.24.0
    helm.sh/chart: hull-test-1.24.1
  name: nginx # default name would be 'release-name-hull-test-nginx' 
              # but with staticName: true in the HULL spec it is just the key name
spec:
  replicas: 3
  selector: # selector is auto-created to match the unique metadata combination 
            # found also in the in the object's metadata labels.
    matchLabels:
      app.kubernetes.io/component: nginx
      app.kubernetes.io/instance: release-name
      app.kubernetes.io/name: hull-test
  template:
    metadata:
      annotations: {}
      labels: # auto-created metadata is added to pod template 
        app.kubernetes.io/component: nginx
        app.kubernetes.io/instance: release-name
        app.kubernetes.io/managed-by: Helm
        app.kubernetes.io/name: hull-test
        app.kubernetes.io/part-of: undefined
        app.kubernetes.io/version: 1.24.0
        helm.sh/chart: hull-test-1.24.1
    spec:
      containers:
      - env: []
        envFrom: []
        image: nginx:1.14.2
        name: nginx
        ports:
        - containerPort: 80
          name: http # name 'http' derived from the key of the port 
                     # object defined in the values.yaml
        volumeMounts: []
      imagePullSecrets: {}
      initContainers: []
      volumes: []
```

### Advanced Example

Now to render the nginx deployment example showcasing extra features of the HULL library you can could create the below `values.yaml` file in your parent chart. Note that this is a very advanced example of what is possible using this library chart. 

This example highlights:

- hierarchical metadata handling
- default RBAC setup of objects
- dynamic naming mechanism
- transformations
- easy inclusion of ConfigMaps and/or Secrets

```yaml
hull:
  config:
    general:  # This time we are not setting rbac: false 
              # so RBAC default objects are created. 
              # If the default objects don't match the use-case
              # you can tweak all aspects individually if needed
      metadata:
        labels:         
          custom: # Additional labels added to all K8S objects
            general_custom_label_1: General Custom Label 1
            general_custom_label_2: General Custom Label 2
            general_custom_label_3: General Custom Label 3
        annotations: 
          custom: # Additional annotations added to all K8S objects
            general_custom_annotation_1: General Custom Annotation 1
            general_custom_annotation_2: General Custom Annotation 2
            general_custom_annotation_3: General Custom Annotation 3
    specific: # Put configuration options specific to this chart here
      nginx_tag: 1.14.2 # You can also use entries here to globally 
                        # define values that are referenced in multiple
                        # places in your chart. See how this field 
                        # is accessed below in the deployment.

  objects:
    deployment:
      _HULL_OBJECT_TYPE_DEFAULT_: # A special object key available for
                                  # all object types allowing defining 
                                  # defaults for properties of all object 
                                  # type instances created.
        annotations:  
          default_annotation_1: Default Annotation 1
          default_annotation_2: Default Annotation 2
          general_custom_annotation_2:  Default Annotation 2  # overwriting this 
                                                              # general annotation for
                                                              # all deployments
          
        labels:
          default_label_1: Default Label 1
          default_label_2: Default Label 2
          general_custom_label_2:  Default Label 2 # overwriting this 
                                                   # general label for
                                                   # all deployments
          
      nginx: # specify the nginx deployment under key 'nginx'
        # This time we're not setting the metadata.name to be static so 
        # name will be created dynamically and will be unique
        annotations:
          general_custom_annotation_3: Specific Object Annotation 3 # overwrite a
                                                                    # general annotation
          default_annotation_2: Specific Object Annotation 2 # overwrite a default annotation
          specific_annotation_1: Specific Object Annotation 1 # add a specific annotation 
                                                              # to the all this object's metadata
        labels: 
          general_custom_label_3: Specific Object Label 3 # overwrite a
                                                          # general label
          default_label_2: Specific Object Label 2 # overwrite a default label
          specific_label_1: Specific Object Label 1 # add a specific label 
                                                    # to the all this object's metadata
        templateAnnotations:
          specific_annotation_2: Specific Template Annotation 2 # this annotation will only appear 
                                                                # in the pod template metadata
        templateLabels:
          specific_label_2: Specific Template Label 2 # this label will only appear 
                                                      # in the pod template metadata
        replicas: 3
        pod:
          containers:
            nginx: # all containers of a pod template are also referenced by a 
                   # unique key to make manipulating them easy.
              image:
                repository: nginx
                tag: _HT!{{ (index . "$").Values.hull.config.specific.nginx_tag }}
                  # Applies a tpl transformation allowing to inject dynamic data based
                  # on values in this values.yaml into the resulting field (here the tag
                  # field of this container).
                  # _HT! is the short form of the transformation that applies tpl to
                  # a given value. This example just references the value of the field 
                  # which is specified further above in the values.yaml and will 
                  # produce 'image: nginx:1.14.2' when rendered in the resulting 
                  # deployment YAML but complex conditional Go templating logic is 
                  # applicable too. 
                  # There are some limitations to using this approach which are 
                  # detailed in the transformation.md in the doc section.
              ports:
                http: # unique key per container here too. All key-value structures
                      # which are array in the K8S objects are converted to arrays
                      # on rendering the chart.
                  containerPort: 80
    configmap: # this is to highlight the secret/configmap inclusion feature
      nginx_configmap: # configmap objects have keys too
        data: # specify for which contents a data entry shall be created
              # within only a few lines of configuration. Contents can come from ...
          an_inline_configmap.txt: # ... an inline specified content or ...
            inline: |- 
              Top secret contents
              spread over 
              multiple lines...
          contents_from_an_external_file.txt: # ... something from an external file.
            path: files/my_secret.txt 

```

This produces the following rendered objects when running the `helm template` command (commented with some brief explanations):

```yaml
---
# Source: hull-test/templates/hull.yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  annotations:
    general_custom_annotation_1: General Custom Annotation 1 # All objects share the general_custom_annotations
    general_custom_annotation_2: General Custom Annotation 2 # if they are not overwritten for the object type's
    general_custom_annotation_3: General Custom Annotation 3 # default or specific instance
  labels:
    app.kubernetes.io/component: default
    app.kubernetes.io/instance: release-name
    app.kubernetes.io/managed-by: Helm
    app.kubernetes.io/name: hull-test
    app.kubernetes.io/part-of: undefined
    app.kubernetes.io/version: 1.24.0
    general_custom_label_1: General Custom Label 1 # All objects share the general_custom_labels
    general_custom_label_2: General Custom Label 2 # if they are not overwritten for the object type's
    general_custom_label_3: General Custom Label 3 # default or specific instance
    helm.sh/chart: hull-test-1.24.1
  name: release-name-hull-test-default # This is the default ServiceAccount created for this chart.
                                       # As all object instances by default it will be assigned a 
                                       # dynamically created unique name in context of this object type.
                                       # In the simple example we disabled this rendering by 
                                       # setting enabled: false for this object's key.
---
# Source: hull-test/templates/hull.yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  annotations:
    general_custom_annotation_1: General Custom Annotation 1
    general_custom_annotation_2: General Custom Annotation 2
    general_custom_annotation_3: General Custom Annotation 3
  labels:
    app.kubernetes.io/component: default
    app.kubernetes.io/instance: release-name
    app.kubernetes.io/managed-by: Helm
    app.kubernetes.io/name: hull-test
    app.kubernetes.io/part-of: undefined
    app.kubernetes.io/version: 1.24.0
    general_custom_label_1: General Custom Label 1
    general_custom_label_2: General Custom Label 2
    general_custom_label_3: General Custom Label 3
    helm.sh/chart: hull-test-1.24.1
  name: release-name-hull-test-default # A default Role for RBAC. 
rules: []
---
# Source: hull-test/templates/hull.yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  annotations:
    general_custom_annotation_1: General Custom Annotation 1
    general_custom_annotation_2: General Custom Annotation 2
    general_custom_annotation_3: General Custom Annotation 3
  labels:
    app.kubernetes.io/component: default
    app.kubernetes.io/instance: release-name
    app.kubernetes.io/managed-by: Helm
    app.kubernetes.io/name: hull-test
    app.kubernetes.io/part-of: undefined
    app.kubernetes.io/version: 1.24.0
    general_custom_label_1: General Custom Label 1
    general_custom_label_2: General Custom Label 2
    general_custom_label_3: General Custom Label 3
    helm.sh/chart: hull-test-1.24.1
  name: release-name-hull-test-default
roleRef:
  apiGroup: rbac.authorization.k8s.io/v1
  kind: Role
  name: release-name-hull-test-default
subjects:
- apiGroup: rbac.authorization.k8s.io/v1
  kind: ServiceAccount
  name: release-name-hull-test-default # A default RoleBinding for RBAC. It connects the 
                                       # default ServiceAccount with the default Role.
                                       # By default RBAC is enabled in charts.
---
# Source: hull-test/templates/hull.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  annotations:
    default_annotation_1: Default Annotation 1 # non-overwritten default_annotation
    default_annotation_2: Specific Object Annotation 2 # overwritten default_annotation by instance
    general_custom_annotation_1: General Custom Annotation 1 # non-overwritten general_custom_annotation
    general_custom_annotation_2: Default Annotation 2 # overwritten general_custom_annotation 
                                                      # by default_annotation
    general_custom_annotation_3: Specific Object Annotation 3 # overwritten general_custom_annotation 
                                                              # by specific_annotation
    specific_annotation_1: Specific Object Annotation 1 # added annotation for instance metadata only
  labels:
    app.kubernetes.io/component: nginx
    app.kubernetes.io/instance: release-name
    app.kubernetes.io/managed-by: Helm
    app.kubernetes.io/name: hull-test
    app.kubernetes.io/part-of: undefined
    app.kubernetes.io/version: 1.24.0
    default_label_1: Default Label 1 # non-overwritten default_label
    default_label_2: Specific Object Label 2 # overwritten default_label by instance
    general_custom_label_1: General Custom Label 1 # non-overwritten general_custom_label
    general_custom_label_2: Default Label 2 # overwritten general_custom_label by default_label
    general_custom_label_3: Specific Object Label 3 # overwritten general_custom_label 
                                                    # by specific_label
    helm.sh/chart: hull-test-1.24.1
    specific_label_1: Specific Object Label 1 # added label for instance metadata only
  name: release-name-hull-test-nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app.kubernetes.io/component: nginx
      app.kubernetes.io/instance: release-name
      app.kubernetes.io/name: hull-test
  template:
    metadata:
      annotations:
        default_annotation_1: Default Annotation 1
        default_annotation_2: Specific Object Annotation 2
        general_custom_annotation_1: General Custom Annotation 1
        general_custom_annotation_2: Default Annotation 2
        general_custom_annotation_3: Specific Object Annotation 3
        specific_annotation_1: Specific Object Annotation 1
        specific_annotation_2: Specific Template Annotation 2 # this annotation was added only 
                                                              # for the pod template's metadata
      labels:
        app.kubernetes.io/component: nginx
        app.kubernetes.io/instance: release-name
        app.kubernetes.io/managed-by: Helm
        app.kubernetes.io/name: hull-test
        app.kubernetes.io/part-of: undefined
        app.kubernetes.io/version: 1.24.0
        default_label_1: Default Label 1
        default_label_2: Specific Object Label 2
        general_custom_label_1: General Custom Label 1
        general_custom_label_2: Default Label 2
        general_custom_label_3: Specific Object Label 3
        helm.sh/chart: hull-test-1.24.1
        specific_label_1: Specific Object Label 1
        specific_label_2: Specific Template Label 2 # this label was added only 
                                                    # for the pod template's metadata
    spec:
      containers:
      - env: []
        envFrom: []
        image: nginx:1.14.2
        name: nginx
        ports:
        - containerPort: 80
          name: http
        volumeMounts: []
      imagePullSecrets: {}
      initContainers: []
      serviceAccountName: release-name-hull-test-default # the dynamically created name
      volumes: []
---
# Source: hull-test/templates/hull.yaml
apiVersion: v1
data:
  an_inline_configmap.txt: "Top secret contents\nspread over \nmultiple lines..."
  contents_from_an_external_file.txt: "Whatever was in this file ..."  
kind: ConfigMap
metadata:
  annotations:
    general_custom_annotation_1: General Custom Annotation 1 # All objects share the general_custom_annotations
    general_custom_annotation_2: General Custom Annotation 2 # if they are not overwritten for the object type's
    general_custom_annotation_3: General Custom Annotation 3 # default or specific instance
  labels:
    app.kubernetes.io/component: nginx_configmap
    app.kubernetes.io/instance: release-name
    app.kubernetes.io/managed-by: Helm
    app.kubernetes.io/name: hull-test
    app.kubernetes.io/part-of: undefined
    app.kubernetes.io/version: 1.24.0
    general_custom_label_1: General Custom Label 1 # All objects share the general_custom_labels
    general_custom_label_2: General Custom Label 2 # if they are not overwritten for the object type's
    general_custom_label_3: General Custom Label 3 # default or specific instance
    helm.sh/chart: hull-test-1.24.1
  name: release-name-hull-test-nginx_configmap
```

Read the additional documentation in the [documentation folder](./hull/doc) on how to utilize the features of the HULL library to the full effect.


</details>



</br>



[***GitHub - helm/chartmuseum: Host your own Helm Chart Repository***](https://github.com/helm/chartmuseum)

![GitHub last commit](https://img.shields.io/github/last-commit/helm/chartmuseum) ![GitHub Repo stars](https://img.shields.io/github/stars/helm/chartmuseum?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/helm/chartmuseum)



</br>


<details>

<summary>README</summary> 

# ChartMuseum

[![GitHub Actions status](https://github.com/helm/chartmuseum/workflows/build/badge.svg)](https://github.com/helm/chartmuseum/actions?query=workflow%3Abuild)
[![Go Report Card](https://goreportcard.com/badge/github.com/helm/chartmuseum)](https://goreportcard.com/report/github.com/helm/chartmuseum)
[![GoDoc](https://godoc.org/github.com/helm/chartmuseum?status.svg)](https://godoc.org/github.com/helm/chartmuseum)

<p align="center"><img align="center" src="logo2.png"></p><br/>

*ChartMuseum* is an open-source **[Helm Chart Repository](https://helm.sh/docs/topics/chart_repository/)** server written in Go (Golang), with support for cloud storage backends, including [Google Cloud Storage](https://cloud.google.com/storage/), [Amazon S3](https://aws.amazon.com/s3/), [Microsoft Azure Blob Storage](https://azure.microsoft.com/en-us/services/storage/blobs/), [Alibaba Cloud OSS Storage](https://www.alibabacloud.com/product/oss), [Openstack Object Storage](https://developer.openstack.org/api-ref/object-store/), [Oracle Cloud Infrastructure Object Storage](https://cloud.oracle.com/storage), [Baidu Cloud BOS Storage](https://cloud.baidu.com/product/bos.html), [Tencent Cloud Object Storage](https://intl.cloud.tencent.com/product/cos), [Netease Cloud NOS Storage](https://www.163yun.com/product/nos), [DigitalOcean Spaces](https://www.digitalocean.com/products/spaces/), [Minio](https://min.io/), and [etcd](https://etcd.io/).

Works as a valid Helm Chart Repository, and also provides an API for uploading charts.

<img width="120" align="right" src="https://github.com/redblue9771/gopher-vector/raw/master/gopher-side_color.png">
<img width="40" align="right" src="https://github.com/redblue9771/gopher-vector/raw/master/gopher-side_color.png">

Powered by some great Go technology:
- [helm/helm](https://github.com/helm/helm) - for working with charts
- [gin-gonic/gin](https://github.com/gin-gonic/gin) - for HTTP routing
- [urfave/cli](https://github.com/urfave/cli) - for command line option parsing
- [spf13/viper](https://github.com/spf13/viper) - for configuration
- [uber-go/zap](https://github.com/uber-go/zap) - for logging
- [chartmuseum/auth](https://github.com/chartmuseum/auth) - for auth
- [chartmuseum/storage](https://github.com/chartmuseum/storage) - for multi-cloud storage

## API

### Helm Chart Repository
- `GET /index.yaml` - retrieved when you run `helm repo add chartmuseum http://localhost:8080/`
- `GET /charts/mychart-0.1.0.tgz` - retrieved when you run `helm install chartmuseum/mychart`
- `GET /charts/mychart-0.1.0.tgz.prov` - retrieved when you run `helm install` with the `--verify` flag

### Chart Manipulation
- `POST /api/charts` - upload a new chart version
- `POST /api/prov` - upload a new provenance file
- `DELETE /api/charts/<name>/<version>` - delete a chart version (and corresponding provenance file)
- `GET /api/charts` - list all charts
- `GET /api/charts/<name>` - list all versions of a chart
- `GET /api/charts/<name>/<version>` - describe a chart version
- `GET /api/charts/<name>/<version>/templates` - get chart template
- `GET /api/charts/<name>/<version>/values` - get chart values
- `HEAD /api/charts/<name>` - check if chart exists (any versions)
- `HEAD /api/charts/<name>/<version>` - check if chart version exists

### Server Info
- `GET /` - HTML welcome page
- `GET /info` - returns current ChartMuseum version
- `GET /health` - returns 200 OK

## Uploading a Chart Package
<sub>*Follow **"How to Run"** section below to get ChartMuseum up and running at ht<span>tp:/</span>/localhost:8080*<sub>

First create `mychart-0.1.0.tgz` using the [Helm CLI](https://docs.helm.sh/using_helm/#installing-helm):
```
cd mychart/
helm package .
```

Upload `mychart-0.1.0.tgz`:
```bash
curl --data-binary "@mychart-0.1.0.tgz" http://localhost:8080/api/charts
```

If you've signed your package and generated a [provenance file](https://github.com/helm/helm-www/blob/master/content/en/docs/topics/provenance.md), upload it with:
```bash
curl --data-binary "@mychart-0.1.0.tgz.prov" http://localhost:8080/api/prov
```

Both files can also be uploaded at once (or one at a time) on the `/api/charts` route using the `multipart/form-data` format:

```bash
curl -F "chart=@mychart-0.1.0.tgz" -F "prov=@mychart-0.1.0.tgz.prov" http://localhost:8080/api/charts
```

You can also use the [helm-push plugin](https://github.com/chartmuseum/helm-push):
```
helm cm-push mychart/ chartmuseum
```

## Installing Charts into Kubernetes
Add the URL to your *ChartMuseum* installation to the local repository list:
```bash
helm repo add chartmuseum http://localhost:8080
```

Search for charts:
```bash
helm search repo chartmuseum/
```

Install chart:
```bash
helm install chartmuseum/mychart --generate-name
```

## How to Run
### CLI
#### Installation
Install binary using [GoFish](https://gofi.sh/):
```
gofish install chartmuseum
==> Installing chartmuseum...
🐠  chartmuseum 0.15.0: installed in 95.431145ms
```

or you can use the installer script:
```
curl https://raw.githubusercontent.com/helm/chartmuseum/main/scripts/get-chartmuseum | bash
```

or download manually from the [releases page](https://github.com/helm/chartmuseum/releases),
which also contains all package checksums and signatures.

Determine your version with `chartmuseum --version`.

#### Configuration
Show all CLI options with `chartmuseum --help`. Common configurations can be seen below.

All command-line options can be specified as environment variables, which are defined by the command-line option, capitalized, with all `-`'s replaced with `_`'s.

For example, the env var `STORAGE_AMAZON_BUCKET` can be used in place of `--storage-amazon-bucket`.

##### Using a configuration file
Use `chartmuseum --config config.yaml` to read configuration from a file.

When using file-based configuration, the corresponding option name can be looked up in [`pkg/config/vars.go`]( https://github.com/helm/chartmuseum/blob/main/pkg/config/vars.go). It would be the key of `configVars` entry corresponding to the command line option / environment variable. For example, `--storage` corresponds to `storage.backend` in the configuration file.

Here's a complete example of a `config.yaml`:

```yaml
debug: true
port: 8080
storage.backend: local
storage.local.rootdir: <storage_path>
bearerauth: 1
authrealm: <authorization server url>
authservice: <authorization server service name>
authcertpath: <path to authorization server public pem file>
authactionssearchpath: <optional: JMESPath to find allowed actions in a jwt token>
depth: 2
```

#### Using with Amazon S3 or Compatible services like Minio or DigitalOcean.
Make sure your environment is properly setup to access `my-s3-bucket`

For Amazon S3, `endpoint` is automatically inferred.
```bash
chartmuseum --debug --port=8080 \
  --storage="amazon" \
  --storage-amazon-bucket="my-s3-bucket" \
  --storage-amazon-prefix="" \
  --storage-amazon-region="us-east-1"
```

For S3 compatible services like Minio, set the credentials using environment variables and pass the `endpoint`.

```bash
export AWS_ACCESS_KEY_ID=""
export AWS_SECRET_ACCESS_KEY=""
chartmuseum --debug --port=8080 \
  --storage="amazon" \
  --storage-amazon-bucket="my-s3-bucket" \
  --storage-amazon-prefix="" \
  --storage-amazon-region="us-east-1" \
  --storage-amazon-endpoint="my-s3-compatible-service-endpoint"
```

You need at least the following permissions inside your IAM Policy
```yaml
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowListObjects",
      "Effect": "Allow",
      "Action": [
        "s3:ListBucket"
      ],
      "Resource": "arn:aws:s3:::my-s3-bucket"
    },
    {
      "Sid": "AllowObjectsCRUD",
      "Effect": "Allow",
      "Action": [
        "s3:DeleteObject",
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": "arn:aws:s3:::my-s3-bucket/*"
    }
  ]
}
```

In order to work with AWS service accounts you may need to set `AWS_SDK_LOAD_CONFIG=1` in your environment.
For more context, please see [here](https://github.com/helm/chartmuseum/issues/280#issuecomment-592292527).

For DigitalOcean, set the credentials using environment variable and pass the `endpoint`.
Note below, that the region `us-east-1` needs to be set, since that is how the DigitalOcean cli implementation functions. The actual region of your spaces location is defined by the endpoint. Below we are using Frankfurt as an example.
```bash
export AWS_ACCESS_KEY_ID="spaces_access_key"
export AWS_SECRET_ACCESS_KEY="spaces_secret_key"
  chartmuseum --debug --port=8080 \
  --storage="amazon" \
  --storage-amazon-bucket="my_spaces_name" \
  --storage-amazon-prefix="my_spaces_name_subfolder" \
  --storage-amazon-region="us-east-1" \
  --storage-amazon-endpoint="https://fra1.digitaloceanspaces.com"
```
The access_key and secret_key can be generated from the DigitalOcean console, under the section API/Spaces_access_keys.

Note: on certain S3-based storage backends, the `LastModified` field on objects
is truncated to the nearest second. For more info, please see issue [#152](https://github.com/helm/chartmuseum/issues/152).

In order to mitigate this, you may use use the `--storage-timestamp-tolerance` option.
For example, to round to the nearest second, you could use `--storage-timestamp-tolerance=1s`.
For acceptable values to use for this field, please see [here](https://golang.org/pkg/time/#ParseDuration).

#### Using with Google Cloud Storage
Make sure your environment is properly setup to access `my-gcs-bucket`.

One way to do so is to set the `GOOGLE_APPLICATION_CREDENTIALS` var in your environment, pointing to the JSON file containing your service account key:
```
export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/[FILE_NAME].json"
```

More info on Google Cloud authentication can be found [here](https://cloud.google.com/docs/authentication/getting-started).

```bash
chartmuseum --debug --port=8080 \
  --storage="google" \
  --storage-google-bucket="my-gcs-bucket" \
  --storage-google-prefix=""
```

#### Using with Microsoft Azure Blob Storage

Make sure your environment is properly setup to access `mycontainer`.

To do so, you must set the following env vars:
- `AZURE_STORAGE_ACCOUNT`
- `AZURE_STORAGE_ACCESS_KEY`

```bash
chartmuseum --debug --port=8080 \
  --storage="microsoft" \
  --storage-microsoft-container="mycontainer" \
  --storage-microsoft-prefix=""
```

#### Using with Alibaba Cloud OSS Storage

Make sure your environment is properly setup to access `my-oss-bucket`.

To do so, you must set the following env vars:
- `ALIBABA_CLOUD_ACCESS_KEY_ID`
- `ALIBABA_CLOUD_ACCESS_KEY_SECRET`

```bash
chartmuseum --debug --port=8080 \
  --storage="alibaba" \
  --storage-alibaba-bucket="my-oss-bucket" \
  --storage-alibaba-prefix="" \
  --storage-alibaba-endpoint="oss-cn-beijing.aliyuncs.com"
```

#### Using with Openstack Object Storage

Make sure your environment is properly setup to access `mycontainer`.

To do so, you must set the following env vars (depending on your openstack version):
- `OS_AUTH_URL`
- either `OS_PROJECT_NAME` or `OS_TENANT_NAME` or `OS_PROJECT_ID` or `OS_TENANT_ID`
- either `OS_DOMAIN_NAME` or `OS_DOMAIN_ID`
- either `OS_USERNAME` or `OS_USERID`
- `OS_PASSWORD`

```bash
chartmuseum --debug --port=8080 \
  --storage="openstack" \
  --storage-openstack-container="mycontainer" \
  --storage-openstack-prefix="" \
  --storage-openstack-region="myregion"
```

For Swift V1 Auth you must set the following env vars:
- `ST_AUTH`
- `ST_USER`
- `ST_KEY`

```bash
chartmuseum --debug --port=8080 \
  --storage="openstack" \
  --storage-openstack-auth="v1" \
  --storage-openstack-container="mycontainer" \
  --storage-openstack-prefix=""
```


#### Using with Oracle Cloud Infrastructure Object Storage

Make sure your environment is properly setup to access `my-ocs-bucket`.

More info on Oracle Cloud Infrastructure authentication can be found [here](https://docs.cloud.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm).

```bash
chartmuseum --debug --port=8080 \
  --storage="oracle" \
  --storage-oracle-bucket="my-ocs-bucket" \
  --storage-oracle-prefix="" \
  --storage-oracle-compartmentid="ocid1.compartment.oc1..1234"
```

#### Using with Baidu Cloud BOS Storage

Make sure your environment is properly setup to access `my-bos-bucket`.

To do so, you must set the following env vars:
- `BAIDU_CLOUD_ACCESS_KEY_ID`
- `BAIDU_CLOUD_ACCESS_KEY_SECRET`

```bash
chartmuseum --debug --port=8080 \
  --storage="baidu" \
  --storage-baidu-bucket="my-bos-bucket" \
  --storage-baidu-prefix="" \
  --storage-baidu-endpoint="bj.bcebos.com"
```

#### Using with Tencent Cloud COS Storage

Make sure your environment is properly setup to access `my-cos-bucket`.

To do so, you must set the following env vars:
- `TENCENT_CLOUD_COS_SECRET_ID`
- `TENCENT_CLOUD_COS_SECRET_KEY`

```bash
chartmuseum --debug --port=8080 \
  --storage="tencent" \
  --storage-tencent-bucket="my-cos-bucket" \
  --storage-tencent-prefix="" \
  --storage-tencent-endpoint="cos.ap-beijing.myqcloud.com"
```

#### Using with Netease Cloud NOS Storage

Make sure your environment is properly setup to access `my-nos-bucket`.

To do so, you must set the following env vars:
- `NETEASE_CLOUD_ACCESS_KEY_ID`
- `NETEASE_CLOUD_ACCESS_KEY_SECRET`

```bash
chartmuseum --debug --port=8080 \
  --storage="netease" \
  --storage-netease-bucket="my-nos-bucket" \
  --storage-netease-prefix="" \
  --storage-netease-endpoint="nos-eastchina1.126.net"
```

#### Using with etcd

To use etcd as backend you need the CA certificate and the signed key pair.
See [here](https://coreos.com/etcd/docs/latest/op-guide/security.html)

```bash
chartmuseum --debug --port=8080 \
  --storage="etcd" \
  --storage-etcd-cafile="/path/to/ca.crt" \
  --storage-etcd-certfile="/path/to/server.crt" \
  --storage-etcd-keyfile="/path/to/server.key" \
  --storage-etcd-prefix="" \
  --storage-etcd-endpoint="http://localhost:2379"
```

#### Using with local filesystem storage
Make sure you have read-write access to `./chartstorage` (will create if doesn't exist on first upload)
```bash
chartmuseum --debug --port=8080 \
  --storage="local" \
  --storage-local-rootdir="./chartstorage"
```

#### Basic Auth
If both of the following options are provided, basic http authentication will protect all routes:
- `--basic-auth-user=<user>` - username for basic http authentication
- `--basic-auth-pass=<pass>` - password for basic http authentication

You may want basic auth to only be applied to operations that can change Charts, i.e. PUT, POST and DELETE.  So to avoid basic auth on GET operations use

- `--auth-anonymous-get` - allow anonymous GET operations

#### Bearer/Token Auth

If all of the following options are provided, bearer auth will protect all routes:
- `--bearer-auth` - enables bearer auth
- `--auth-realm=<realm>` - authorization server url
- `--auth-service=<service>` - authorization server service name
- `--auth-cert-path=<path>` - path to authorization server public pem file
- `--auth-actions-search-path=<JMESPath>` - (optional) JMESPath to find allowed actions in a jwt token

Using options above, *ChartMuseum* is configured with a public key, and will accept RS256 JWT tokens signed by the associated private key, passed in the `Authorization` header. You can use the [chartmuseum/auth](https://github.com/chartmuseum/auth) Go library to generate valid JWT tokens.

##### JWT Token without a custom JMESPath to find actions

In order to gain access to a specific resource, the JWT token must contain an `access` section in the claims. This section indicates which resources the user is able to access. Here is an example token payload:

```json
{
  "exp": 1543995770,
  "iat": 1543995470,
  "access": [
    {
      "type": "artifact-repository",
      "name": "org1/repo1",
      "actions": [
        "pull"
      ]
    }
  ]
}
```

The `type` is always "artifact-repository", the `name` is the namespace/tenant (just use the string "repo" if using single-tenant server), and `actions` is an array of actions the user can perform ("pull" and/or "push).

If your JWT token structure is different, you can configure a [JMESPath string](https://jmespath.org/). So you can define the way to find the allowed actions yourself.
For the `type` and the the `name` you can use following placeholder
* name: `$NAMESPACE`
* type: `$ACCESS_ENTRY_TYPE`

E.g.: If you want to represent the default configuration, the JMESPath looks like: `access[?name=='$NAMESPACE' && type=='$ACCESS_ENTRY_TYPE'].actions[]`.

For more information about how this works, please see [chartmuseum/auth-server-example](https://github.com/chartmuseum/auth-server-example).


#### HTTPS
If both of the following options are provided, the server will listen and serve HTTPS:
- `--tls-cert=<crt>` - path to tls certificate chain file
- `--tls-key=<key>` - path to tls key file

##### HTTPS with Client Certificate Authentication
If the above HTTPS values are provided in addition to below, the server will listen and serve HTTPS and authenticate client requests against the CA certificate:
-  `--tls-ca-cert=<cacert>` - path to tls certificate file

#### Just generating index.yaml
You can specify the `--gen-index` option if you only wish to use _ChartMuseum_ to generate your index.yaml file. Note that this will only work with `--depth=0`.

The contents of index.yaml will be printed to stdout and the program will exit. This is useful if you are satisfied with your current Helm CI/CD process and/or don't want to monitor another webservice.

#### Other CLI options
- `--log-json` - output structured logs as json
- `--log-health` - log incoming /health requests
- `--log-latency-integer` - log latency as an integer (nanoseconds) instead of a string
- `--disable-api` - disable all routes prefixed with /api
- `--disable-delete` - explicitly disable the delete chart route
- `--disable-statefiles` - disable use of index-cache.yaml
- `--allow-overwrite` - allow chart versions to be re-uploaded without ?force querystring
- `--disable-force-overwrite` - do not allow chart versions to be re-uploaded, even with ?force querystring
- `--chart-url=<url>` - absolute url for .tgzs in index.yaml
- `--storage-amazon-endpoint=<endpoint>` - alternative s3 endpoint
- `--storage-amazon-sse=<algorithm>` - s3 server side encryption algorithm
- `--storage-openstack-cacert=<path>` - path to a custom ca certificates bundle for openstack
- `--chart-post-form-field-name=<field>` - form field which will be queried for the chart file content
- `--prov-post-form-field-name=<field>` - form field which will be queried for the provenance file content
- `--index-limit=<number>` - limit the number of parallel indexers
- `--context-path=<path>` - base context path (new root for application routes)
- `--depth=<number>` - levels of nested repos for multitenancy
- `--cors-alloworigin=<value>` - value to set in the Access-Control-Allow-Origin HTTP header
- `--read-timeout=<number>` - socket read timeout for http server
- `--write-timeout=<number>` - socker write timeout for http server

### Docker Image
Available via [GitHub Container Registry (GHCR)](https://github.com/orgs/helm/packages/container/package/chartmuseum).

Example usage (local storage):
```bash
docker run --rm -it \
  -p 8080:8080 \
  -e DEBUG=1 \
  -e STORAGE=local \
  -e STORAGE_LOCAL_ROOTDIR=/charts \
  -v $(pwd)/charts:/charts \
  ghcr.io/helm/chartmuseum:v0.15.0
```

Example usage (S3):
```bash
docker run --rm -it \
  -p 8080:8080 \
  -e DEBUG=1 \
  -e STORAGE="amazon" \
  -e STORAGE_AMAZON_BUCKET="my-s3-bucket" \
  -e STORAGE_AMAZON_PREFIX="" \
  -e STORAGE_AMAZON_REGION="us-east-1" \
  -v ~/.aws:/home/chartmuseum/.aws:ro \
  ghcr.io/helm/chartmuseum:v0.15.0
```

### Helm Chart
There is a [Helm chart for *ChartMuseum*](https://github.com/chartmuseum/charts/tree/main/src/chartmuseum) itself.

You can also view it on [Artifact Hub](https://artifacthub.io/packages/helm/chartmuseum/chartmuseum).

To install:
```bash
helm repo add chartmuseum https://chartmuseum.github.io/charts
helm install chartmuseum/chartmuseum
```

If interested in making changes, please submit a PR to [chartmuseum/charts](https://github.com/chartmuseum/charts). Before doing any work, please check for any [currently open pull requests](https://github.com/chartmuseum/charts/pulls?q=is%3Apr+is%3Aopen). Thanks!

## Multitenancy
Multitenancy is supported with the `--depth` flag.

To begin, start with a directory structure such as
```
charts
├── org1
│   ├── repoa
│   │   └── nginx-ingress-0.9.3.tgz
├── org2
│   ├── repob
│   │   └── chartmuseum-0.4.0.tgz
```

This represents a storage layout appropriate for `--depth=2`. The organization level can be eliminated by using `--depth=1`. The default depth is 0 (singletenant server).

Start the server with `--depth=2`, pointing to the `charts/` directory:
```
chartmuseum --debug --depth=2 --storage="local" --storage-local-rootdir=./charts
```

This example will provide two separate Helm Chart Repositories at the following locations:
- `http://localhost:8080/org1/repoa`
- `http://localhost:8080/org2/repob`

This should work with all supported storage backends.

To use the chart manipulation routes, simply place the name of the repo directly after "/api" in the route:

```bash
curl -F "chart=@mychart-0.1.0.tgz" http://localhost:8080/api/org1/repoa/charts
```

You may also experiment with the `--depth-dynamic` flag, which should allow for dynamic depth levels (i.e. all of `/api/charts`, `/api/myrepo/charts`, `/api/org1/repoa/charts`).

## Pagination

For large chart repositories, you may wish to paginate the results from the `GET /api/charts` route.

To do so, add the `offset` and `limit` query params to the request. For example, to retrieve a list of 5 charts total, skipping the first 5 charts, you could use the following:

```
GET /api/charts?offset=5&limit=5
```

## Cache

By default, the contents of `index.yaml` (per-tenant) will be stored in memory. This means that memory usage will continue to grow indefinitely as more charts are added to storage.

You may wish to offload this to an external cache store, especially for large, multitenant installations.

### Cache Interval

When dealing with thousands of charts, you may experience latency with the default settings. This is because upon each request, the storage backend is scanned for changes compared to the cache.

If you are ok with `index.yaml` being out-of-date for a fixed period of time, you can improve performance by using the `--cache-interval=<interval>` option.
When this setting is enabled, the charts available for each tenant are refreshed on a timer.

For example, to only check storage every 5 minutes, you can use `--cache-interval=5m`.

For valid values to use for this setting, please see [here](https://godoc.org/time#ParseDuration).

### Using Redis

Example of using Redis as an external cache store:
```bash
chartmuseum --debug --port=8080 \
  --storage="local" \
  --storage-local-rootdir="./chartstorage" \
  --cache="redis" \
  --cache-redis-addr="localhost:6379" \
  --cache-redis-password="" \
  --cache-redis-db=0
```


## Prometheus Metrics

ChartMuseum exposes its [Prometheus metrics](https://prometheus.io/docs/concepts/metric_types/) at the `/metrics` route on the main port. This can be enabled with the `--enable-metrics` command-line flag or the `ENABLE_METRICS` environment variable.

> Note that the Kubernetes chart currently disables metrics by default (`ENABLE_METRICS=false` is set in the chart). The `--disable-metrics` command-line flag has be deprecated and will only be available in `v0.14.0` and prior.

Below are the current application metrics exposed. Note that there is a per tenant (repo) label. The repo label corresponds to the depth parameter, so a depth=2 as the example above would
have repo labels named `org1/repoa` and `org2/repob`.

| Metric                                   | Type  | Labels     | Description                              |
| ---------------------------------------- | ----- | ---------- | ---------------------------------------- |
| chartmuseum_charts_served_total          | Gauge | {repo="*"} | Total number of charts                   |
| chartmuseum_chart_versions_served_total | Gauge | {repo="*"} | Total number of chart versions available |

*: see above for repo label

There are other general global metrics harvested (per process, hence for all tenants). You can get the complete list by using the `/metrics` route.

| Metric                                     | Type    | Labels                                                | Description                               |
| ------------------------------------------ | ------- | ----------------------------------------------------- | ----------------------------------------- |
| chartmuseum_request_duration_seconds       | Summary | {quantile="0.5"}, {quantile="0.9"}, {quantile="0.99"} | The HTTP request latencies in seconds     |
| chartmuseum_request_duration_seconds_sum   |         |                                                       |                                           |
| chartmuseum_request_duration_seconds_count |         |                                                       |                                           |
| chartmuseum_request_size_bytes             | Summary | {quantile="0.5"}, {quantile="0.9"}, {quantile="0.99"} | The HTTP request sizes in bytes           |
| chartmuseum_request_size_bytes_sum         |         |                                                       |                                           |
| chartmuseum_request_size_bytes_count       |         |                                                       |                                           |
| chartmuseum_response_size_bytes            | Summary | {quantile="0.5"}, {quantile="0.9"}, {quantile="0.99"} | The HTTP response sizes in bytes          |
| chartmuseum_response_size_bytes_sum        |         |                                                       |                                           |
| chartmuseum_response_size_bytes_count      |         |                                                       |                                           |
| go_goroutines                              | Gauge   |                                                       | Number of goroutines that currently exist |


## Notes on index.yaml
The repository index (index.yaml) is dynamically generated based on packages found in storage. If you store your own version of index.yaml, it will be completely ignored.

`GET /index.yaml` occurs when you run `helm repo add chartmuseum http://localhost:8080` or `helm repo update`.

If you manually add/remove a .tgz package from storage, it will be immediately reflected in `GET /index.yaml`.

You are no longer required to maintain your own version of index.yaml using `helm repo index --merge`.

The `--gen-index` CLI option (described above) can be used to generate and print index.yaml to stdout.

Upon index regeneration, *ChartMuseum* will, however, save a statefile in storage called `index-cache.yaml` used for cache optimization. This file is only meant for internal use, but may be able to be used for migration to simple storage.

## Mirroring the official Kubernetes repositories
Please see `scripts/mirror-k8s-repos.sh` for an example of how to download all .tgz packages from the official Kubernetes repositories (both stable and incubator).

You can then use *ChartMuseum* to serve up an internal mirror:
```
scripts/mirror-k8s-repos.sh
chartmuseum --debug --port=8080 --storage="local" --storage-local-rootdir="./mirror"
 ```

## Custom Welcome Page

With the flag `--web-template-path=<path>`, you can specify the path to your custom welcome page.

The structure of the folder should be like this:

```bash
web/
  index.html
  xyz.html
  static/
      main.css
      main.js
```

> ChartMuseum is using gin-gonic to serve the static files, this means that you can use go-template to render the files.

If you don't specify a custom welcome page, ChartMuseum will serve the default one.

#### Artifact Hub

By setting the flag `--artifact-hub-repo-id <repo id>`, ChartMuseum will serve a `artifacthub-repo.yml` file with the
specified repo ID in the `repositoryID` field of the yaml file.

```yaml
repositoryID: The ID of the Artifact Hub repository where the packages will be published to (optional, but it enables verified publisher)
```

##### Multitenancy

For multitenancy setups, you can provide a key value pair to the flag in the format: `--artifact-hub-repo-id <repo>=<repo id>`

```bash
chartmuseum --storage local --storage-local-rootdir /tmp/ --depth 1 --artifact-hub-repo-id org1=<repo id> --artifact-hub-repo-id org2=<repo2 id>
```

The `artifacthub-repo.yml` file will then be served at `/org1/artifacthub-repo.yml` and `/org2/artifacthub-repo.yml`

## Original Logo

<sub>**_"Preserve your precious artifacts... in the cloud!"_**<sub>

![](./logo.png)

## Subprojects

The following subprojects are maintained by *ChartMuseum*:

- [chartmuseum/helm-push](https://github.com/chartmuseum/helm-push) - Helm plugin to push chart package to ChartMuseum
- [chartmuseum/storage](https://github.com/chartmuseum/storage) - Go library providing common interface for working across multiple cloud storage backends
- [chartmuseum/auth](https://github.com/chartmuseum/auth) - Go library for generating ChartMuseum JWT Tokens, authorizing HTTP requests, etc.
- [chartmuseum/auth-server-example](https://github.com/chartmuseum/auth-server-example) - Example server providing JWT tokens for ChartMuseum auth
- [chartmuseum/testbed](https://github.com/chartmuseum/testbed) - Docker testbed for continuous integration
- [chartmuseum/www](https://github.com/chartmuseum/www) - chartmuseum.com static site source code
- [chartmuseum/ui](https://github.com/chartmuseum/ui) - ChartMuseum frontend UI

## Community
You can reach the *ChartMuseum* community and developers in the [Kubernetes Slack](https://slack.k8s.io) **#chartmuseum** channel.


</details>



</br>



[***GitHub - Datalux/Osintgram: Osintgram is a OSINT tool on Instagram. It offers an interactive shell to perform analysis on Instagram account of any users by its nickname***](https://github.com/Datalux/Osintgram)

![GitHub last commit](https://img.shields.io/github/last-commit/Datalux/Osintgram) ![GitHub Repo stars](https://img.shields.io/github/stars/Datalux/Osintgram?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/Datalux/Osintgram)



</br>



</br>



[***GitHub - bitnami/charts: Bitnami Helm Charts***](https://github.com/bitnami/charts)

![GitHub last commit](https://img.shields.io/github/last-commit/bitnami/charts) ![GitHub Repo stars](https://img.shields.io/github/stars/bitnami/charts?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/bitnami/charts)



</br>



</br>



[***GitHub - kubernetes/autoscaler: Autoscaling components for Kubernetes***](https://github.com/kubernetes/autoscaler)

![GitHub last commit](https://img.shields.io/github/last-commit/kubernetes/autoscaler) ![GitHub Repo stars](https://img.shields.io/github/stars/kubernetes/autoscaler?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/kubernetes/autoscaler)



</br>



</br>



[***GitHub - argoproj/argocd-example-apps: Example Apps to Demonstrate Argo CD***](https://github.com/argoproj/argocd-example-apps)

![GitHub last commit](https://img.shields.io/github/last-commit/argoproj/argocd-example-apps) ![GitHub Repo stars](https://img.shields.io/github/stars/argoproj/argocd-example-apps?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/argoproj/argocd-example-apps)



</br>



</br>



[***GitHub - kubernetes-sigs/kubespray: Deploy a Production Ready Kubernetes Cluster***](https://github.com/kubernetes-sigs/kubespray)

![GitHub last commit](https://img.shields.io/github/last-commit/kubernetes-sigs/kubespray) ![GitHub Repo stars](https://img.shields.io/github/stars/kubernetes-sigs/kubespray?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/kubernetes-sigs/kubespray)



</br>



</br>



[***GitHub - k8s-at-home/flux-cluster-template: Highly opinionated template for deploying a single Kubernetes (k3s) cluster with Ansible and Terraform backed by Flux, SOPS, GitHub Actions, Renovate and more!***](https://github.com/k8s-at-home/template-cluster-k3s)

![GitHub last commit](https://img.shields.io/github/last-commit/k8s-at-home/template-cluster-k3s) ![GitHub Repo stars](https://img.shields.io/github/stars/k8s-at-home/template-cluster-k3s?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/k8s-at-home/template-cluster-k3s)



</br>


<details>

<summary>README</summary> 

# Template for deploying k3s backed by Flux

Highly opinionated template for deploying a single [k3s](https://k3s.io) cluster with [Ansible](https://www.ansible.com) and [Terraform](https://www.terraform.io) backed by [Flux](https://toolkit.fluxcd.io/) and [SOPS](https://toolkit.fluxcd.io/guides/mozilla-sops/).

The purpose here is to showcase how you can deploy an entire Kubernetes cluster and show it off to the world using the [GitOps](https://www.weave.works/blog/what-is-gitops-really) tool [Flux](https://toolkit.fluxcd.io/). When completed, your Git repository will be driving the state of your Kubernetes cluster. In addition with the help of the [Ansible](https://github.com/ansible-collections/community.sops), [Terraform](https://github.com/carlpett/terraform-provider-sops) and [Flux](https://toolkit.fluxcd.io/guides/mozilla-sops/) SOPS integrations you'll be able to commit [Age](https://github.com/FiloSottile/age) encrypted secrets to your public repo.

## Overview

- [Introduction](https://github.com/k8s-at-home/flux-cluster-template#-introduction)
- [Prerequisites](https://github.com/k8s-at-home/flux-cluster-template#-prerequisites)
- [Repository structure](https://github.com/k8s-at-home/flux-cluster-template#-repository-structure)
- [Lets go!](https://github.com/k8s-at-home/flux-cluster-template#-lets-go)
- [Post installation](https://github.com/k8s-at-home/flux-cluster-template#-post-installation)
- [Troubleshooting](https://github.com/k8s-at-home/flux-cluster-template#-troubleshooting)
- [What's next](https://github.com/k8s-at-home/flux-cluster-template#-whats-next)
- [Thanks](https://github.com/k8s-at-home/flux-cluster-template#-thanks)

## 👋 Introduction

The following components will be installed in your [k3s](https://k3s.io/) cluster by default. Most are only included to get a minimum viable cluster up and running.

- [flux](https://toolkit.fluxcd.io/) - GitOps operator for managing Kubernetes clusters from a Git repository
- [kube-vip](https://kube-vip.io/) - Load balancer for the Kubernetes control plane nodes
- [metallb](https://metallb.universe.tf/) - Load balancer for Kubernetes services
- [cert-manager](https://cert-manager.io/) - Operator to request SSL certificates and store them as Kubernetes resources
- [calico](https://www.tigera.io/project-calico/) - Container networking interface for inter pod and service networking
- [external-dns](https://github.com/kubernetes-sigs/external-dns) - Operator to publish DNS records to Cloudflare (and other providers) based on Kubernetes ingresses
- [k8s_gateway](https://github.com/ori-edge/k8s_gateway) - DNS resolver that provides local DNS to your Kubernetes ingresses
- [traefik](https://traefik.io) - Kubernetes ingress controller used for a HTTP reverse proxy of Kubernetes ingresses
- [local-path-provisioner](https://github.com/rancher/local-path-provisioner) - provision persistent local storage with Kubernetes

_Additional applications include [hajimari](https://github.com/toboshii/hajimari), [error-pages](https://github.com/tarampampam/error-pages), [echo-server](https://github.com/Ealenn/Echo-Server), [system-upgrade-controller](https://github.com/rancher/system-upgrade-controller), [reflector](https://github.com/emberstack/kubernetes-reflector), [reloader](https://github.com/stakater/Reloader), and [kured](https://github.com/weaveworks/kured)_

For provisioning the following tools will be used:

- [Ubuntu](https://ubuntu.com/download/server) - Universal operating system that supports running all kinds of home related workloads in Kubernetes
- [Ansible](https://www.ansible.com) - Provision the Ubuntu OS and install k3s
- [Terraform](https://www.terraform.io) - Provision an already existing Cloudflare domain and certain DNS records to be used with your k3s cluster

## 📝 Prerequisites

**Note:** _This template has not been tested on cloud providers like AWS EC2, Hetzner, Scaleway etc... Those cloud offerings probably have a better way of provsioning a Kubernetes cluster and it's advisable to use those instead of the Ansible playbooks included here. This repository can still be used for the GitOps/Flux portion if there's a cluster working in one those environments._

### 💻 Systems

- One or more nodes with a fresh install of [Ubuntu Server 22.04](https://ubuntu.com/download/server).
  - These nodes can be ARM64/AMD64 bare metal or VMs.
  - An odd number of control plane nodes, greater than or equal to 3 is required if deploying more than one control plane node.
- A [Cloudflare](https://www.cloudflare.com/) account with a domain, this will be managed by Terraform and external-dns. You can [register new domains](https://www.cloudflare.com/products/registrar/) directly thru Cloudflare.
- Some experience in debugging problems and a positive attitude ;)

📍 It is recommended to have 3 master nodes for a highly available control plane.

### 🔧 Workstation Tools

1. Install the **most recent versions** of the following CLI tools on your workstation, if you are using [Homebrew](https://brew.sh/) on MacOS or Linux skip to steps 3 and 4.

    * Required: [age](https://github.com/FiloSottile/age), [ansible](https://www.ansible.com), [flux](https://toolkit.fluxcd.io/), [gitleaks](https://github.com/zricethezav/gitleaks), [go-task](https://github.com/go-task/task), [ipcalc](http://jodies.de/ipcalc), [jq](https://stedolan.github.io/jq/), [kubectl](https://kubernetes.io/docs/tasks/tools/), [pre-commit](https://github.com/pre-commit/pre-commit), [sops](https://github.com/mozilla/sops), [terraform](https://www.terraform.io), [yq](https://github.com/mikefarah/yq)

    * Recommended: [direnv](https://github.com/direnv/direnv), [helm](https://helm.sh/), [kustomize](https://github.com/kubernetes-sigs/kustomize), [prettier](https://github.com/prettier/prettier), [stern](https://github.com/stern/stern), [yamllint](https://github.com/adrienverge/yamllint)

2. This guide heavily relies on [go-task](https://github.com/go-task/task) as a framework for setting things up. It is advised to learn and understand the commands it is running under the hood.

3. Install [go-task](https://github.com/go-task/task) via Brew

    ```sh
    brew install go-task/tap/go-task
    ```

4. Install workstation dependencies via Brew

    ```sh
    task init
    ```

### ⚠️ pre-commit

It is advisable to install [pre-commit](https://pre-commit.com/) and the pre-commit hooks that come with this repository.
[sops-pre-commit](https://github.com/k8s-at-home/sops-pre-commit) will check to make sure you are not committing non-encrypted Kubernetes secrets to your repository.

1. Enable Pre-Commit

    ```sh
    task precommit:init
    ```

2. Update Pre-Commit, though it will occasionally make mistakes, so verify its results.

    ```sh
    task precommit:update
    ```

## 📂 Repository structure

The Git repository contains the following directories under `cluster` and are ordered below by how Flux will apply them.

```sh
📁 cluster      # k8s cluster defined as code
├─📁 flux       # flux, gitops operator, loaded before everything
├─📁 crds       # custom resources, loaded before 📁 core and 📁 apps
├─📁 charts     # helm repos, loaded before 📁 core and 📁 apps
├─📁 config     # cluster config, loaded before 📁 core and 📁 apps
├─📁 core       # crucial apps, namespaced dir tree, loaded before 📁 apps
└─📁 apps       # regular apps, namespaced dir tree, loaded last
```

## 🚀 Lets go

Very first step will be to create a new repository by clicking the **Use this template** button on this page.

Clone the repo to you local workstation and `cd` into it.

📍 **All of the below commands** are run on your **local** workstation, **not** on any of your cluster nodes.

### 🔐 Setting up Age

📍 Here we will create a Age Private and Public key. Using [SOPS](https://github.com/mozilla/sops) with [Age](https://github.com/FiloSottile/age) allows us to encrypt secrets and use them in Ansible, Terraform and Flux.

1. Create a Age Private / Public Key

    ```sh
    age-keygen -o age.agekey
    ```

2. Set up the directory for the Age key and move the Age file to it

    ```sh
    mkdir -p ~/.config/sops/age
    mv age.agekey ~/.config/sops/age/keys.txt
    ```

3. Export the `SOPS_AGE_KEY_FILE` variable in your `bashrc`, `zshrc` or `config.fish` and source it, e.g.

    ```sh
    export SOPS_AGE_KEY_FILE=~/.config/sops/age/keys.txt
    source ~/.bashrc
    ```

4. Fill out the Age public key in the `.config.env` under `BOOTSTRAP_AGE_PUBLIC_KEY`, **note** the public key should start with `age`...

### ☁️ Global Cloudflare API Key

In order to use Terraform and `cert-manager` with the Cloudflare DNS challenge you will need to create a API key.

1. Head over to Cloudflare and create a API key by going [here](https://dash.cloudflare.com/profile/api-tokens).

2. Under the `API Keys` section, create a global API Key.

3. Use the API Key in the configuration section below.

📍 You may wish to update this later on to a Cloudflare **API Token** which can be scoped to certain resources. I do not recommend using a Cloudflare **API Key**, however for the purposes of this template it is easier getting started without having to define which scopes and resources are needed. For more information see the [Cloudflare docs on API Keys and Tokens](https://developers.cloudflare.com/api/).

### 📄 Configuration

📍 The `.config.env` file contains necessary configuration that is needed by Ansible, Terraform and Flux.

1. Copy the `.config.sample.env` to `.config.env` and start filling out all the environment variables.

    **All are required** unless otherwise noted in the comments.

    ```sh
    cp .config.sample.env .config.env
    ```

2. Once that is done, verify the configuration is correct by running:

    ```sh
    task verify
    ```

3. If you do not encounter any errors run start having the script wire up the templated files and place them where they need to be.

    ```sh
    task configure
    ```

### ⚡ Preparing Ubuntu with Ansible

📍 Here we will be running a Ansible Playbook to prepare Ubuntu for running a Kubernetes cluster.

📍 Nodes are not security hardened by default, you can do this with [dev-sec/ansible-collection-hardening](https://github.com/dev-sec/ansible-collection-hardening) or similar if it supports Ubuntu 22.04.

1. Ensure you are able to SSH into your nodes from your workstation using a private SSH key **without a passphrase**. This is how Ansible is able to connect to your remote nodes.

   [How to configure SSH key-based authentication](https://www.digitalocean.com/community/tutorials/how-to-configure-ssh-key-based-authentication-on-a-linux-server)

2. Install the Ansible deps

    ```sh
    task ansible:init
    ```

3. Verify Ansible can view your config

    ```sh
    task ansible:list
    ```

4. Verify Ansible can ping your nodes

    ```sh
    task ansible:ping
    ```

5. Run the Ubuntu Prepare Ansible playbook

    ```sh
    task ansible:prepare
    ```

6. Reboot the nodes

    ```sh
    task ansible:reboot
    ```

### ⛵ Installing k3s with Ansible

📍 Here we will be running a Ansible Playbook to install [k3s](https://k3s.io/) with [this](https://galaxy.ansible.com/xanmanning/k3s) wonderful k3s Ansible galaxy role. After completion, Ansible will drop a `kubeconfig` in `./provision/kubeconfig` for use with interacting with your cluster with `kubectl`.

☢️ If you run into problems, you can run `task ansible:nuke` to destroy the k3s cluster and start over.

1. Verify Ansible can view your config

    ```sh
    task ansible:list
    ```

2. Verify Ansible can ping your nodes

    ```sh
    task ansible:ping
    ```

3. Install k3s with Ansible

    ```sh
    task ansible:install
    ```

4. Verify the nodes are online

    ```sh
    task cluster:nodes
    # NAME           STATUS   ROLES                       AGE     VERSION
    # k8s-0          Ready    control-plane,master      4d20h   v1.21.5+k3s1
    # k8s-1          Ready    worker                    4d20h   v1.21.5+k3s1
    ```

### ☁️ Configuring Cloudflare DNS with Terraform

📍 Review the Terraform scripts under `./provision/terraform/cloudflare/` and make sure you understand what it's doing (no really review it).

If your domain already has existing DNS records **be sure to export those DNS settings before you continue**.

1. Pull in the Terraform deps

    ```sh
    task terraform:init
    ```

2. Review the changes Terraform will make to your Cloudflare domain

    ```sh
    task terraform:plan
    ```

3. Have Terraform apply your Cloudflare settings

    ```sh
    task terraform:apply
    ```

If Terraform was ran successfully you can log into Cloudflare and validate the DNS records are present.

The cluster application [external-dns](https://github.com/kubernetes-sigs/external-dns) will be managing the rest of the DNS records you will need.

### 🔹 GitOps with Flux

📍 Here we will be installing [flux](https://toolkit.fluxcd.io/) after some quick bootstrap steps.

1. Verify Flux can be installed

    ```sh
    task cluster:verify
    # ► checking prerequisites
    # ✔ kubectl 1.21.5 >=1.18.0-0
    # ✔ Kubernetes 1.21.5+k3s1 >=1.16.0-0
    # ✔ prerequisites checks passed
    ```

2. Push you changes to git

    📍 **Verify** all the `*.sops.yaml` and `*.sops.yml` files under the `./cluster` and `./provision` folders are **encrypted** with SOPS

    ```sh
    git add -A
    git commit -m "Initial commit :rocket:"
    git push
    ```

3. Install Flux and sync the cluster to the Git repository

    ```sh
    task cluster:install
    # namespace/flux-system configured
    # customresourcedefinition.apiextensions.k8s.io/alerts.notification.toolkit.fluxcd.io created
    ```

4. Verify Flux components are running in the cluster

    ```sh
    task cluster:pods -- -n flux-system
    # NAME                                       READY   STATUS    RESTARTS   AGE
    # helm-controller-5bbd94c75-89sb4            1/1     Running   0          1h
    # kustomize-controller-7b67b6b77d-nqc67      1/1     Running   0          1h
    # notification-controller-7c46575844-k4bvr   1/1     Running   0          1h
    # source-controller-7d6875bcb4-zqw9f         1/1     Running   0          1h
    ```

### 🎤 Verification Steps

_Mic check, 1, 2_ - In a few moments applications should be lighting up like a Christmas tree 🎄

You are able to run all the commands below with one task

```sh
task cluster:resources
```

1. View the Flux Git Repositories

    ```sh
    task cluster:gitrepositories
    ```

2. View the Flux kustomizations

    ```sh
    task cluster:kustomizations
    ```

3. View all the Flux Helm Releases

    ```sh
    task cluster:helmreleases
    ```

4. View all the Flux Helm Repositories

    ```sh
    task cluster:helmrepositories
    ```

5. View all the Pods

    ```sh
    task cluster:pods
    ```

6. View all the certificates and certificate requests

    ```sh
    task cluster:certificates
    ```

7. View all the ingresses

    ```sh
    task cluster:ingresses
    ```

🏆 **Congratulations** if all goes smooth you'll have a Kubernetes cluster managed by Flux, your Git repository is driving the state of your cluster.

☢️ If you run into problems, you can run `task ansible:nuke` to destroy the k3s cluster and start over.

🧠 Now it's time to pause and go get some coffee ☕ because next is describing how DNS is handled.

## 📣 Post installation

### 🌐 DNS

📍 The [external-dns](https://github.com/kubernetes-sigs/external-dns) application created in the `networking` namespace will handle creating public DNS records. By default, `echo-server` is the only public domain exposed on your Cloudflare domain. In order to make additional applications public you must set an ingress annotation like in the `HelmRelease` for `echo-server`. You do not need to use Terraform to create additional DNS records unless you need a record outside the purposes of your Kubernetes cluster (e.g. setting up MX records).

[k8s_gateway](https://github.com/ori-edge/k8s_gateway) is deployed on the IP choosen for `${BOOTSTRAP_METALLB_K8S_GATEWAY_ADDR}`. Inorder to test DNS you can point your clients DNS to the `${BOOTSTRAP_METALLB_K8S_GATEWAY_ADDR}` IP address and load `https://hajimari.${BOOTSTRAP_CLOUDFLARE_DOMAIN}` in your browser.

You can also try debugging with the command `dig`, e.g. `dig @${BOOTSTRAP_METALLB_K8S_GATEWAY_ADDR} hajimari.${BOOTSTRAP_CLOUDFLARE_DOMAIN}` and you should get a valid answer containing your `${BOOTSTRAP_METALLB_TRAEFIK_ADDR}` IP address.

If your router (or Pi-Hole, Adguard Home or whatever) supports conditional DNS forwarding (also know as split-horizon DNS) you may have DNS requests for `${SECRET_DOMAIN}` only point to the  `${BOOTSTRAP_METALLB_K8S_GATEWAY_ADDR}` IP address. This will ensure only DNS requests for `${SECRET_DOMAIN}` will only get routed to your [k8s_gateway](https://github.com/ori-edge/k8s_gateway) service thus providing DNS resolution to your cluster applications/ingresses.

To access services from the outside world port forwarded `80` and `443` in your router to the `${BOOTSTRAP_METALLB_TRAEFIK_ADDR}` IP, in a few moments head over to your browser and you _should_ be able to access `https://echo-server.${BOOTSTRAP_CLOUDFLARE_DOMAIN}` from a device outside your LAN.

Now if nothing is working, that is expected. This is DNS after all!

### 🔐 SSL

By default in this template Kubernetes ingresses are set to use the [Let's Encrypt Staging Environment](https://letsencrypt.org/docs/staging-environment/). This will hopefully reduce issues from ACME on requesting certificates until you are ready to use this in "Production".

Once you have confirmed there are no issues requesting your certificates replace `letsencrypt-staging` with `letsencrypt-production` in your ingress annotations for `cert-manager.io/cluster-issuer`

### 🤖 Renovatebot

[Renovatebot](https://www.mend.io/free-developer-tools/renovate/) will scan your repository and offer PRs when it finds dependencies out of date. Common dependencies it will discover and update are Flux, Ansible Galaxy Roles, Terraform Providers, Kubernetes Helm Charts, Kubernetes Container Images, Pre-commit hooks updates, and more!

The base Renovate configuration provided in your repository can be view at [.github/renovate.json5](https://github.com/k8s-at-home/flux-cluster-template/blob/main/.github/renovate.json5). If you notice this only runs on weekends and you can [change the schedule to anything you want](https://docs.renovatebot.com/presets-schedule/) or simply remove it.

To enable Renovate on your repository, click the 'Configure' button over at their [Github app page](https://github.com/apps/renovate) and choose your repository. Over time Renovate will create PRs for out-of-date dependencies it finds. Any merged PRs that are in the cluster directory Flux will deploy.

### 🪝 Github Webhook

Flux is pull-based by design meaning it will periodically check your git repository for changes, using a webhook you can enable Flux to update your cluster on `git push`. In order to configure Github to send `push` events from your repository to the Flux webhook receiver you will need two things:

1. Webhook URL - Your webhook receiver will be deployed on `https://flux-receiver.${BOOTSTRAP_CLOUDFLARE_DOMAIN}/hook/:hookId`. In order to find out your hook id you can run the following command:

    ```sh
    kubectl -n flux-system get receiver/github-receiver --kubeconfig=./provision/kubeconfig
    # NAME              AGE    READY   STATUS
    # github-receiver   6h8m   True    Receiver initialized with URL: /hook/12ebd1e363c641dc3c2e430ecf3cee2b3c7a5ac9e1234506f6f5f3ce1230e123
    ```

    So if my domain was `k8s-at-home.com` the full url would look like this:

    ```text
    https://flux-receiver.k8s-at-home.com/hook/12ebd1e363c641dc3c2e430ecf3cee2b3c7a5ac9e1234506f6f5f3ce1230e123
    ```

2. Webhook secret - Your webhook secret can be found by decrypting the `secret.sops.yaml` using the following command:

    ```sh
    sops -d ./cluster/apps/flux-system/webhooks/github/secret.sops.yaml | yq .stringData.token
    ```

    **Note:** Don't forget to update the `BOOTSTRAP_FLUX_GITHUB_WEBHOOK_SECRET` variable in your `.config.env` file so it matches the generated secret if applicable

Now that you have the webhook url and secret, it's time to set everything up on the Github repository side. Navigate to the settings of your repository on Github, under "Settings/Webhooks" press the "Add webhook" button. Fill in the webhook url and your secret.

### 💾 Storage

Rancher's `local-path-provisioner` is a great start for storage but soon you might find you need more features like replicated block storage, or to connect to a NFS/SMB/iSCSI server. Check out the projects below to read up more on some storage solutions that might work for you.

- [rook-ceph](https://github.com/rook/rook)
- [longhorn](https://github.com/longhorn/longhorn)
- [openebs](https://github.com/openebs/openebs)
- [nfs-subdir-external-provisioner](https://github.com/kubernetes-sigs/nfs-subdir-external-provisioner)
- [democratic-csi](https://github.com/democratic-csi/democratic-csi)
- [csi-driver-nfs](https://github.com/kubernetes-csi/csi-driver-nfs)
- [synology-csi](https://github.com/SynologyOpenSource/synology-csi)

### 🔏 Authenticate Flux over SSH

Authenticating Flux to your git repository has a couple benefits like using a private git repository and/or using the Flux [Image Automation Controllers](https://fluxcd.io/docs/components/image/).

By default this template only works on a public GitHub repository, it is advised to keep your repository public.

The benefits of a public repository include:

* Debugging or asking for help, you can provide a link to a resource you are having issues with.
* Adding a topic to your repository of `k8s-at-home` to be included in the [k8s-at-home-search](https://whazor.github.io/k8s-at-home-search/). This search helps people discover different configurations of Helm charts across others Flux based repositories.

<details>
  <summary>Expand to read guide on adding Flux SSH authentication</summary>

  1. Generate new SSH key:
      ```sh
      ssh-keygen -t ecdsa -b 521 -C "github-deploy-key" -f ./cluster/github-deploy-key -q -P ""
      ```
  2. Paste public key in the deploy keys section of your repository settings
  3. Create sops secret in `cluster/flux/flux-system/github-deploy-key.sops.yaml` with the contents of:
      ```yaml
      # yamllint disable
      apiVersion: v1
      kind: Secret
      metadata:
          name: github-deploy-key
          namespace: flux-system
      stringData:
          # 3a. Contents of github-deploy-key
          identity: |
              -----BEGIN OPENSSH PRIVATE KEY-----
                  ...
              -----END OPENSSH PRIVATE KEY-----
          # 3b. Output of curl --silent https://api.github.com/meta | jq --raw-output '"github.com "+.ssh_keys[]'
          known_hosts: |
              github.com ssh-ed25519 ...
              github.com ecdsa-sha2-nistp256 ...
              github.com ssh-rsa ...
      ```
  4. Encrypt secret:
      ```sh
      sops --encrypt --in-place ./cluster/flux/flux-system/github-deploy-key.sops.yaml
      ```
  5. Apply secret to cluster:
      ```sh
      sops --decrypt cluster/flux/flux-system/github-deploy-key.sops.yaml | kubectl apply -f -
      ```
  6.  Update `cluster/flux/flux-system/flux-cluster.yaml`:
      ```yaml
      ---
      apiVersion: source.toolkit.fluxcd.io/v1beta2
      kind: GitRepository
      metadata:
        name: flux-cluster
        namespace: flux-system
      spec:
        interval: 10m
        # 6a: Change this to your user and repo names
        url: ssh://git@github.com/$user/$repo
        ref:
          branch: main
        secretRef:
          name: github-deploy-key
      ```
  7. Commit and push changes
  8. Force flux to reconcile your changes
     ```sh
     task cluster:reconcile
     ```
  9. Verify git repository is now using SSH:
      ```sh
      task cluster:gitrepositories
      ```
  10. Optionally set your repository to Private in your repository settings.
</details>

## 👉 Troubleshooting

Our [wiki](https://github.com/k8s-at-home/flux-cluster-template/wiki) (WIP, contributions welcome) is a good place to start troubleshooting issues. If that doesn't cover your issue, come join and say Hi in our [Discord](https://discord.gg/k8s-at-home) server by starting a new thread in the #kubernetes support channel.

You may also open a issue on this GitHub repo or open a [discussion on GitHub](https://github.com/k8s-at-home/organization/discussions).

## ❔ What's next

The world is your cluster, see below for important things you could work on adding.

Our Check out our [wiki](https://github.com/k8s-at-home/flux-cluster-template/wiki) (WIP, contributions welcome) for more integrations!

## 🤝 Thanks

Big shout out to all the authors and contributors to the projects that we are using in this repository.

Community member @Whazor created [this website](https://whazor.github.io/k8s-at-home-search/) as a creative way to search Helm Releases across GitHub. You may use it as a means to get ideas on how to configure an applications' Helm values.

Many people have shared their awesome repositories over at [awesome-home-kubernetes](https://github.com/k8s-at-home/awesome-home-kubernetes).


</details>



</br>



[***GitHub - stakater/Reloader: A Kubernetes controller to watch changes in ConfigMap and Secrets and do rolling upgrades on Pods with their associated Deployment, StatefulSet, DaemonSet and DeploymentConfig – [✩Star] if you&#39;re using it!***](https://github.com/stakater/Reloader)

![GitHub last commit](https://img.shields.io/github/last-commit/stakater/Reloader) ![GitHub Repo stars](https://img.shields.io/github/stars/stakater/Reloader?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/stakater/Reloader)



</br>



</br>



[***GitHub - emberstack/kubernetes-reflector: Custom Kubernetes controller that can be used to replicate secrets, configmaps and certificates.***](https://github.com/emberstack/kubernetes-reflector)

![GitHub last commit](https://img.shields.io/github/last-commit/emberstack/kubernetes-reflector) ![GitHub Repo stars](https://img.shields.io/github/stars/emberstack/kubernetes-reflector?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/emberstack/kubernetes-reflector)



</br>


<details>

<summary>README</summary> 

# Reflector
Reflector is a Kubernetes addon designed to monitor changes to resources (secrets and configmaps) and reflect changes to mirror resources in the same or other namespaces.

[![Pipeline](https://github.com/emberstack/kubernetes-reflector/actions/workflows/pipeline.yaml/badge.svg)](https://github.com/emberstack/kubernetes-reflector/actions/workflows/pipeline.yaml)
[![Release](https://img.shields.io/github/release/emberstack/kubernetes-reflector.svg?style=flat-square)](https://github.com/emberstack/kubernetes-reflector/releases/latest)
[![Docker Image](https://img.shields.io/docker/image-size/emberstack/kubernetes-reflector/latest?style=flat-square)](https://hub.docker.com/r/emberstack/kubernetes-reflector)
[![Docker Pulls](https://img.shields.io/docker/pulls/emberstack/kubernetes-reflector?style=flat-square)](https://hub.docker.com/r/emberstack/kubernetes-reflector)
[![license](https://img.shields.io/github/license/emberstack/kubernetes-reflector.svg?style=flat-square)](LICENSE)


> Supports `amd64`, `arm` and `arm64`

## Support
If you need help or found a bug, please feel free to open an Issue on GitHub (https://github.com/emberstack/kubernetes-reflector/issues).  

## Deployment

Reflector can be deployed either manually or using Helm (recommended).

### Prerequisites
- Kubernetes 1.14+
- Helm 3 (if deployed using Helm)

#### Deployment using Helm

Use Helm to install the latest released chart:
```shellsession
$ helm repo add emberstack https://emberstack.github.io/helm-charts
$ helm repo update
$ helm upgrade --install reflector emberstack/reflector
```

You can customize the values of the helm deployment by using the following Values:

| Parameter                            | Description                                      | Default                                                 |
| ------------------------------------ | ------------------------------------------------ | ------------------------------------------------------- |
| `nameOverride`                       | Overrides release name                           | `""`                                                    |
| `fullnameOverride`                   | Overrides release fullname                       | `""`                                                    |
| `image.repository`                   | Container image repository                       | `emberstack/kubernetes-reflector`                       |
| `image.tag`                          | Container image tag                              | `Same as chart version`                                 |
| `image.pullPolicy`                   | Container image pull policy                      | `IfNotPresent`                                          |
| `configuration.logging.minimumLevel` | Logging minimum level                            | `Information`                                           |
| `configuration.watcher.timeout`      | Maximum watcher lifetime in seconds              | ``                                                      |
| `rbac.enabled`                       | Create and use RBAC resources                    | `true`                                                  |
| `serviceAccount.create`              | Create ServiceAccount                            | `true`                                                  |
| `serviceAccount.name`                | ServiceAccount name                              | _release name_                                          |
| `livenessProbe.initialDelaySeconds`  | `livenessProbe` initial delay                    | `5`                                                     |
| `livenessProbe.periodSeconds`        | `livenessProbe` period                           | `10`                                                    |
| `readinessProbe.initialDelaySeconds` | `readinessProbe` initial delay                   | `5`                                                     |
| `readinessProbe.periodSeconds`       | `readinessProbe` period                          | `10`                                                    |
| `startupProbe.failureThreshold`      | `startupProbe` failure threshold                 | `10`                                                    |
| `startupProbe.periodSeconds`         | `startupProbe` period                            | `5`                                                     |
| `resources`                          | Resource limits                                  | `{}`                                                    |
| `nodeSelector`                       | Node labels for pod assignment                   | `{}`                                                    |
| `tolerations`                        | Toleration labels for pod assignment             | `[]`                                                    |
| `affinity`                           | Node affinity for pod assignment                 | `{}`                                                    |
| `priorityClassName`                  | `priorityClassName` for pods                     | `""`                                                    |

> Find us on [Artifact Hub](https://artifacthub.io/packages/helm/emberstack/reflector)


#### Manual deployment
Each release (found on the [Releases](https://github.com/emberstack/kubernetes-reflector/releases) GitHub page) contains the manual deployment file (`reflector.yaml`).

```shellsession
$ kubectl -n kube-system apply -f https://github.com/emberstack/kubernetes-reflector/releases/latest/download/reflector.yaml
```


## Usage

### 1. Annotate the source `secret` or `configmap`
  
  - Add `reflector.v1.k8s.emberstack.com/reflection-allowed: "true"` to the resource annotations to permit reflection to mirrors.
  - Add `reflector.v1.k8s.emberstack.com/reflection-allowed-namespaces: "<list>"` to the resource annotations to permit reflection from only the list of comma separated namespaces or regular expressions. Note: If this annotation is omitted or is empty, all namespaces are allowed.

  #### Automatic mirror creation:
  Reflector can create mirrors with the same name in other namespaces automatically. The following annotations control if and how the mirrors are created:
  - Add `reflector.v1.k8s.emberstack.com/reflection-auto-enabled: "true"` to the resource annotations to automatically create mirrors in other namespaces. Note: Requires `reflector.v1.k8s.emberstack.com/reflection-allowed` to be `true` since mirrors need to able to reflect the source.
  - Add `reflector.v1.k8s.emberstack.com/reflection-auto-namespaces: "<list>"` to the resource annotations specify in which namespaces to automatically create mirrors. Note: If this annotation is omitted or is empty, all namespaces are allowed. Namespaces in this list will also be checked by `reflector.v1.k8s.emberstack.com/reflection-allowed-namespaces` since mirrors need to be in namespaces from where reflection is permitted.

  > Important: If the `source` is deleted, automatic mirrors are deleted. Also if either reflection or automirroring is turned off or the automatic mirror's namespace is no longer a valid match for the allowed namespaces, the automatic mirror is deleted.

  > Important: Reflector will skip any conflicting resource when creating auto-mirrors. If there is already a resource with the source's name in a namespace where an automatic mirror is to be created, that namespace is skipped and logged as a warning.
  
  Example source secret:
   ```yaml
  apiVersion: v1
  kind: Secret
  metadata:
    name: source-secret
    annotations:
      reflector.v1.k8s.emberstack.com/reflection-allowed: "true"
      reflector.v1.k8s.emberstack.com/reflection-allowed-namespaces: "namespace-1,namespace-2,namespace-[0-9]*"
  data:
    ...
  ```
  
  Example source configmap:
   ```yaml
  apiVersion: v1
  kind: ConfigMap
  metadata:
    name: source-config-map
    annotations:
      reflector.v1.k8s.emberstack.com/reflection-allowed: "true"
      reflector.v1.k8s.emberstack.com/reflection-allowed-namespaces: "namespace-1,namespace-2,namespace-[0-9]*"
  data:
    ...
  ```
  
### 2. Annotate the mirror secret or configmap

  - Add `reflector.v1.k8s.emberstack.com/reflects: "<source namespace>/<source name>"` to the mirror object. The value of the annotation is the full name of the source object in `namespace/name` format.

  > Note: Add `reflector.v1.k8s.emberstack.com/reflected-version: ""` to the resource annotations when doing any manual changes to the mirror (for example when deploying with `helm` or re-applying the deployment script). This will reset the reflected version of the mirror.
  
  Example mirror secret:
   ```yaml
  apiVersion: v1
  kind: Secret
  metadata:
    name: mirror-secret
    annotations:
      reflector.v1.k8s.emberstack.com/reflects: "default/source-secret"
  data:
    ...
  ```
  
  Example mirror configmap:
   ```yaml
  apiVersion: v1
  kind: ConfigMap
  metadata:
    name: mirror-config-map
    annotations:
      reflector.v1.k8s.emberstack.com/reflects: "default/source-config-map"
  data:
    ...
  ```

### 3. Done!
  Reflector will monitor any changes done to the source objects and copy the following fields:
  - `data` for secrets
  - `data` and `binaryData` for configmaps
  Reflector keeps track of what was copied by annotating mirrors with the source object version.

 - - - -



## `cert-manager` support

> Since version 1.5 of cert-manager you can annotate secrets created from certificates for mirroring using `secretTemplate`  (see https://cert-manager.io/docs/usage/certificate/).

```
apiVersion: cert-manager.io/v1
kind: Certificate
...
spec:
  secretTemplate:
    annotations:
      reflector.v1.k8s.emberstack.com/reflection-allowed: "true"
      reflector.v1.k8s.emberstack.com/reflection-allowed-namespaces: ""
  ...
  ```

</details>



</br>



[***GitHub - go-task/task: A task runner / simpler Make alternative written in Go***](https://github.com/go-task/task)

![GitHub last commit](https://img.shields.io/github/last-commit/go-task/task) ![GitHub Repo stars](https://img.shields.io/github/stars/go-task/task?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/go-task/task)


***QUICK INSTALL***

```bash
sh -c "$(curl --location https://taskfile.dev/install.sh)" -- -d -b /usr/local/bin
```


</br>



</br>



[***GitHub - megadose/holehe: holehe allows you to check if the mail is used on different sites like twitter, instagram and will retrieve information on sites with the forgotten password function.***](https://github.com/megadose/holehe)

![GitHub last commit](https://img.shields.io/github/last-commit/megadose/holehe) ![GitHub Repo stars](https://img.shields.io/github/stars/megadose/holehe?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/megadose/holehe)



</br>



</br>



[***GitHub - webtorrent/webtorrent-cli: WebTorrent, the streaming torrent client. For the command line.***](https://github.com/webtorrent/webtorrent-cli)

![GitHub last commit](https://img.shields.io/github/last-commit/webtorrent/webtorrent-cli) ![GitHub Repo stars](https://img.shields.io/github/stars/webtorrent/webtorrent-cli?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/webtorrent/webtorrent-cli)



</br>



</br>



[***GitHub - zakjan/cert-chain-resolver: SSL certificate chain resolver***](https://github.com/zakjan/cert-chain-resolver)

![GitHub last commit](https://img.shields.io/github/last-commit/zakjan/cert-chain-resolver) ![GitHub Repo stars](https://img.shields.io/github/stars/zakjan/cert-chain-resolver?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/zakjan/cert-chain-resolver)



</br>



</br>



[***GitHub - cert-manager/cert-manager: Automatically provision and manage TLS certificates in Kubernetes***](https://github.com/cert-manager/cert-manager)

![GitHub last commit](https://img.shields.io/github/last-commit/cert-manager/cert-manager) ![GitHub Repo stars](https://img.shields.io/github/stars/cert-manager/cert-manager?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/cert-manager/cert-manager)



</br>



</br>



[***GitHub - gravitational/teleport: Certificate authority and access plane for SSH, Kubernetes, web apps, databases and desktops***](https://github.com/gravitational/teleport)

![GitHub last commit](https://img.shields.io/github/last-commit/gravitational/teleport) ![GitHub Repo stars](https://img.shields.io/github/stars/gravitational/teleport?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/gravitational/teleport)



</br>



</br>



[***GitHub - localtunnel/localtunnel: expose yourself***](https://github.com/localtunnel/localtunnel)

![GitHub last commit](https://img.shields.io/github/last-commit/localtunnel/localtunnel) ![GitHub Repo stars](https://img.shields.io/github/stars/localtunnel/localtunnel?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/localtunnel/localtunnel)



</br>



</br>



[***GitHub - argoproj-labs/argocd-image-updater: Automatic container image update for Argo CD***](https://github.com/argoproj-labs/argocd-image-updater)

![GitHub last commit](https://img.shields.io/github/last-commit/argoproj-labs/argocd-image-updater) ![GitHub Repo stars](https://img.shields.io/github/stars/argoproj-labs/argocd-image-updater?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/argoproj-labs/argocd-image-updater)



</br>



</br>



[***GitHub - rancher/system-upgrade-controller: In your Kubernetes, upgrading your nodes***](https://github.com/rancher/system-upgrade-controller)

![GitHub last commit](https://img.shields.io/github/last-commit/rancher/system-upgrade-controller) ![GitHub Repo stars](https://img.shields.io/github/stars/rancher/system-upgrade-controller?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/rancher/system-upgrade-controller)



</br>



</br>



[***GitHub - archlinux/archinstall: Arch Linux installer - guided, templates etc.***](https://github.com/archlinux/archinstall)

![GitHub last commit](https://img.shields.io/github/last-commit/archlinux/archinstall) ![GitHub Repo stars](https://img.shields.io/github/stars/archlinux/archinstall?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/archlinux/archinstall)



</br>



</br>



[***GitHub - sensepost/Frack: Frack - Keep and Maintain your breach data***](https://github.com/sensepost/Frack)

![GitHub last commit](https://img.shields.io/github/last-commit/sensepost/Frack) ![GitHub Repo stars](https://img.shields.io/github/stars/sensepost/Frack?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/sensepost/Frack)



</br>


<details>

<summary>README</summary> 

![Head](/media/Head.png)

[![Twitter](https://img.shields.io/badge/twitter-Stingray__ZA-blue)](https://twitter.com/Stingray_ZA)
[![Defcon](https://img.shields.io/badge/Defcon-29-blue)](https://forum.defcon.org/node/237235)

[![Plugins](/media/plugins.png)](media/Plugins.md)

## What is Frack?

Frack is my attempt at creating an end-to-end solution to store, manage and query your breach data. The tool has got a very basic workflow making it easy to use.

![WF](media/Frack_Workflow.jpg)

[![Youtube video of DefCon 29](https://img.youtube.com/vi/XYR0BCu422w/0.jpg)](https://www.youtube.com/watch?v=XYR0BCu422w "Youtube video of DefCon 29")

## Why Frack?

Well, I wanted something that was easy to use, didn’t cost millions of dollars and was quick. The python is easy to read and understand so hopefully you will get a better understanding of interacting with your database using python while learning about all the awesome cloud stuff that’s available.

## Let’s get into it.
Frack has been updated to use custom plugins to make it easier to parse raw breach data. The SHA-1 hashes of the breach files will be posted on the [Plugins](/media/Plugins.md) page to make it easy to find the correct plugin for your dataset. These plugins will be updated as new breaches are released. If you feel like contributing, you are more than welcome to add your own parsers.

Should you have a breach that is not supported by a plugin, you can still manually parse the file if you can get in one of the following .csv formats.

Frack supports these .csv file formats:

* `<email>,<password>`
* `<email>,<hash>`
* `<email>,<hash>,<salt>`

Unfortunately, the breach data available on the internet is never clean, and has to be extracted manually to ensure quality of the data. An example of extracting the data from a .sql dump can be seen below. I’m using an awk script to break down the .sql file into .csv files for each table and then a .sql file containing the structure of the .csv file. The awk script I use in this video is by: [https://gist.github.com/slawo-ch/894349427655d22398f825dc535a40f0](https://gist.github.com/slawo-ch/894349427655d22398f825dc535a40f0)

![Extracting](media/Extracting_E-Mail_Hash.gif)

Once you’ve got a clean .csv file, you can use the parsing module to add fields to the .csv file to make the data make sense when viewed in the database. The converted format looks like this:

`breach:string,site:string,year:int,domain:string,email:string,password:string,hash:string,salt:string`

Because we’re adding a lot of data to the .csv the file will grow substantially which is why we then convert it to .orc format. To learn more about the .orc format you can visit: [https://orc.apache.org/](https://orc.apache.org/)

As you can see below, the .orc file is super compressed, so it fits in perfectly with the why, to not spend your whole year’s salary on bandwidth.

![Image01](media/Image_001.png)

Here you can see how effective .orc is at compressing data. I threw a kitchen sink at it and it managed to parse it perfectly. Our input file was 29.7GB, then after adding our fields it was 75.7GB then after converting to .orc it’s a mere 12.8GB. That’s smaller than the original, and we’re adding 1 billion lines to our DB.

Now let’s go through the modules. The tool consists of three modules. A query module to query your data, a db module to manage your database and get some pretty cool info from your db and finally the parse module to do the whole conversion process explained above.

## The Parse Module:

This module’s sole purpose is to first clean up the data by performing these checks:

- The fields must equal that of the selected input. This is two fields for `<email>,<password>` and `<email>,<hash>` and then three fields for `<email>,<hash>,<salt>`.
- Validate that the e-mail address is valid by using some RegEx.
- Do some rubbish removal of lines with blank fields and non-ascii characters.
- Check that the hash is longer than 16 chars. If it's shorter it's probably trash.

The parse module now supports plugins. This will allow importing of a raw dump no matter what format it was dumped in to be parsed into Frack format alleviating the pain associated with extracting the data into a clean usable dataset. To see if your breach is supported by a plugin you can search for the SHA-1 of the file on the [Plugins](/media/Plugins.md) page.

The parse module has got several arguments. The default input file format is `<email>,<hash>`. If your file differs, you need to use flags to specify what data your file contains.
|Argument|What it does|
|--|--|
| -i / --inputfile `<file>`| File to import data from. This is your cleaned .csv file.|
| -m / --module `<module name>` | Use a plugin module to import a raw breach. |
| -y / --year `<year>`| The year the breach / combo / collection was released. |
| -n / --name `<name>`| The name of the breach / combo / collection. |
| -w / --website `<website>`| The website address of the site in question. |
| -p / --passwords | Use this flag if the file being imported contains passwords i.e. `<email>,<password>`|
| -s / --salt | Use this flag if the file contains salt values i.e. `<email>,<hash>,<salt>`.|
| -d / --nodel | Don't delete the .error file. During parsing all fields that does not comply with the rules above will be dumped into a .error file for further analysis. |
| -u / --upload | When parsing is done, upload the .orc file to the ingestion bucket. |

## The db module:

The db module is used for managing the data, and includes some cool stats for your dataset.

![Image09](media/Image_009.png)

|Argument|What it does|
|--|--|
| -c / --count | Count the lines in the database. |
| -n / --nomnom | Create and start an ingestion job for all the files in your storage bucket. |
| -d / --delete | Adding this flag, the ingestion bucket will be emptied once everything has been ingested. |
| -t / --top `<n>`| Displays the top `<n>` passwords from the whole dataset. |
| -w / --web | Display all the websites with line counts that's currently in your database. |
| -b / --breach | Display all the breaches with their line counts that's in the current database. |
| -f / --file | Save the output of any of the queries above to an Excel sheet. |

## The query module:

The query module allows you to query the dataset for domains. The output will be in Excel and include a quick password analysis and a list of all the unique passwords for the domain you’ve queried.

![Image10](media/Image_010.png)

|Argument|What it does|
|--|--|
| -i / --inputfile `<filename>`  | Specify a file containing all the domains you wish to query. One domain per line. |
| -d / --singledomain `<domain>` | Specify a single domain to query. |

# Installation
``` bash
    git clone https://github.com/sensepost/Frack
    cd Frack
    pip3 install -r requirements
```

# Quick guided run through
1. [Configuring your local and Cloud infrastructure.](/media/Step1.md)
2. [Converting and Ingesting your first data.](/media/Step2.md)
3. [Converting and Ingesting using a plugin.](/media/Step3.md)

## License
`Frack` is licensed under a [GNU General Public v3 License](https://www.gnu.org/licenses/gpl-3.0.en.html). Permissions beyond the scope of this license may be available at [http://sensepost.com/contact/](http://sensepost.com/contact/).

</details>



</br>



[***GitHub - cloudposse/charts: The &quot;Cloud Posse&quot; Distribution of Kubernetes Applications***](https://github.com/cloudposse/charts)

![GitHub last commit](https://img.shields.io/github/last-commit/cloudposse/charts) ![GitHub Repo stars](https://img.shields.io/github/stars/cloudposse/charts?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/cloudposse/charts)



</br>



</br>



[***GitHub - chr4/shellrc: Shell dotfiles, conf.d stype, for multiple shells (bash, zsh)***](https://github.com/chr4/shellrc)

![GitHub last commit](https://img.shields.io/github/last-commit/chr4/shellrc) ![GitHub Repo stars](https://img.shields.io/github/stars/chr4/shellrc?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/chr4/shellrc)



</br>



</br>



[***GitHub - emirozer/kubectl-doctor: kubectl cluster triage plugin for k8s - 🏥 (brew doctor equivalent)***](https://github.com/emirozer/kubectl-doctor)

![GitHub last commit](https://img.shields.io/github/last-commit/emirozer/kubectl-doctor) ![GitHub Repo stars](https://img.shields.io/github/stars/emirozer/kubectl-doctor?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/emirozer/kubectl-doctor)



</br>



</br>



[***GitHub - willhallonline/docker-ansible: Ansible inside Docker containers: Alpine, Ubuntu, Centos &amp; Debian with Ansible 2.12, 2.11, 2.10 and 2.9 + Mitogen***](https://github.com/willhallonline/docker-ansible)

![GitHub last commit](https://img.shields.io/github/last-commit/willhallonline/docker-ansible) ![GitHub Repo stars](https://img.shields.io/github/stars/willhallonline/docker-ansible?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/willhallonline/docker-ansible)



</br>



</br>



[***GitHub - zricethezav/gitleaks: Protect and discover secrets using Gitleaks 🔑***](https://github.com/zricethezav/gitleaks)

![GitHub last commit](https://img.shields.io/github/last-commit/zricethezav/gitleaks) ![GitHub Repo stars](https://img.shields.io/github/stars/zricethezav/gitleaks?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/zricethezav/gitleaks)


***QUICK INSTALL***

```bash
curl -L "https://github.com/zricethezav/gitleaks/releases/download/$(curl -L -s "https://api.github.com/repos/zricethezav/gitleaks/releases/latest" | grep -Poe '"tag_name": "\K.*?(?=")' | head -n 1)/gitleaks_$(curl -L -s "https://api.github.com/repos/zricethezav/gitleaks/releases/latest" | grep -Poe '"tag_name": "\K.*?(?=")' | head -n 1 | cut -c2- )_linux_x64.tar.gz" | sudo tar -C /usr/bin -xzv
```


</br>



</br>



[***GitHub - Jaydee94/kubeseal-webgui: This is a python based webapp for using Bitnami-Sealed-Secrets in a web-ui.***](https://github.com/Jaydee94/kubeseal-webgui)

![GitHub last commit](https://img.shields.io/github/last-commit/Jaydee94/kubeseal-webgui) ![GitHub Repo stars](https://img.shields.io/github/stars/Jaydee94/kubeseal-webgui?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/Jaydee94/kubeseal-webgui)



</br>



</br>



[***GitHub - bitnami-labs/sealed-secrets: A Kubernetes controller and tool for one-way encrypted Secrets***](https://github.com/bitnami-labs/sealed-secrets)

![GitHub last commit](https://img.shields.io/github/last-commit/bitnami-labs/sealed-secrets) ![GitHub Repo stars](https://img.shields.io/github/stars/bitnami-labs/sealed-secrets?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/bitnami-labs/sealed-secrets)


***QUICK INSTALL***

```bash
curl -L "https://github.com/bitnami-labs/sealed-secrets/releases/download/$(curl -L -s "https://api.github.com/repos/bitnami-labs/sealed-secrets/releases/latest" | grep -Poe '"tag_name": "\K.*?(?=")' | head -n 1)/kubeseal-$(curl -L -s "https://api.github.com/repos/bitnami-labs/sealed-secrets/releases/latest" | grep -Poe '"tag_name": "\K.*?(?=")' | head -n 1 | cut -c2- )-linux-amd64.tar.gz" | sudo tar -C /usr/bin -xzv
```


</br>


<details>

<summary>README</summary> 

# "Sealed Secrets" for Kubernetes

[![](https://img.shields.io/badge/install-docs-brightgreen.svg)](#Installation)
[![](https://img.shields.io/github/release/bitnami-labs/sealed-secrets.svg)](https://github.com/bitnami-labs/sealed-secrets/releases/latest)
[![](https://img.shields.io/homebrew/v/kubeseal)](https://formulae.brew.sh/formula/kubeseal)
[![Build Status](https://github.com/bitnami-labs/sealed-secrets/actions/workflows/ci.yml/badge.svg)](https://github.com/bitnami-labs/sealed-secrets/actions/workflows/ci.yml)
[![](https://img.shields.io/github/v/release/bitnami-labs/sealed-secrets?include_prereleases&label=helm&sort=semver)](https://github.com/bitnami-labs/sealed-secrets/releases)
[![Verification Status](https://github.com/bitnami-labs/sealed-secrets/actions/workflows/helm-vib.yaml/badge.svg)](https://github.com/bitnami-labs/sealed-secrets/actions/workflows/helm-vib.yaml)
[![Go Report Card](https://goreportcard.com/badge/github.com/bitnami-labs/sealed-secrets)](https://goreportcard.com/report/github.com/bitnami-labs/sealed-secrets)
![Downloads](https://img.shields.io/github/downloads/bitnami-labs/sealed-secrets/total.svg)

**Problem:** "I can manage all my K8s config in git, except Secrets."

**Solution:** Encrypt your Secret into a SealedSecret, which *is* safe
to store - even to a public repository.  The SealedSecret can be
decrypted only by the controller running in the target cluster and
nobody else (not even the original author) is able to obtain the
original Secret from the SealedSecret.

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Overview](#overview)
  - [SealedSecrets as templates for secrets](#sealedsecrets-as-templates-for-secrets)
  - [Public key / Certificate](#public-key--certificate)
  - [Scopes](#scopes)
- [Installation](#installation)
  - [Controller](#controller)
    - [Kustomize](#kustomize)
    - [Helm Chart](#helm-chart)
  - [Homebrew](#homebrew)
  - [MacPorts](#macports)
  - [Installation from source](#installation-from-source)
- [Upgrade](#upgrade)
- [Usage](#usage)
  - [Managing existing secrets](#managing-existing-secrets)
  - [Update existing secrets](#update-existing-secrets)
  - [Raw mode (experimental)](#raw-mode-experimental)
- [Secret Rotation](#secret-rotation)
  - [Sealing key renewal](#sealing-key-renewal)
  - [User secret rotation](#user-secret-rotation)
  - [Early key renewal](#early-key-renewal)
  - [Common misconceptions about key renewal](#common-misconceptions-about-key-renewal)
  - [Manual key management (advanced)](#manual-key-management-advanced)
  - [Re-encryption (advanced)](#re-encryption-advanced)
- [Details (advanced)](#details-advanced)
  - [Crypto](#crypto)
- [Developing](#developing)
- [FAQ](#faq)
  - [Will you still be able to decrypt if you no longer have access to your cluster?](#will-you-still-be-able-to-decrypt-if-you-no-longer-have-access-to-your-cluster)
  - [How can I do a backup of my SealedSecrets?](#how-can-i-do-a-backup-of-my-sealedsecrets)
  - [Can I decrypt my secrets offline with a backup key?](#can-i-decrypt-my-secrets-offline-with-a-backup-key)
  - [What flags are available for kubeseal?](#what-flags-are-available-for-kubeseal)
  - [How do I update parts of JSON/YAML/TOML/.. file encrypted with sealed secrets?](#how-do-i-update-parts-of-jsonyamltoml-file-encrypted-with-sealed-secrets)
  - [Can I bring my own (pre-generated) certificates?](#can-i-bring-my-own-pre-generated-certificates)
  - [How to use kubeseal if the controller is not running within the `kube-system` namespace?](#how-to-use-kubeseal-if-the-controller-is-not-running-within-the-kube-system-namespace)
  - [How to verify the images?](#how-to-verify-the-images)
  - [How to use one controller for a subset of namespaces](#How-to-use-one-controller-for-a-subset-of-namespaces)

- [Community](#community)
  - [Related projects](#related-projects)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Overview

Sealed Secrets is composed of two parts:

- A cluster-side controller / operator
- A client-side utility: `kubeseal`

The `kubeseal` utility uses asymmetric crypto to encrypt secrets that only the controller can decrypt.

These encrypted secrets are encoded in a `SealedSecret` resource, which you can see as a recipe for creating
a secret. Here is how it looks:

```yaml
apiVersion: bitnami.com/v1alpha1
kind: SealedSecret
metadata:
  name: mysecret
  namespace: mynamespace
spec:
  encryptedData:
    foo: AgBy3i4OJSWK+PiTySYZZA9rO43cGDEq.....
```

Once unsealed this will produce a secret equivalent to this:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: mysecret
  namespace: mynamespace
data:
  foo: bar  # <- base64 encoded "bar"
```

This normal [kubernetes secret](https://kubernetes.io/docs/concepts/configuration/secret/) will appear in the cluster
after a few seconds you can use it as you would use any secret that you would have created directly (e.g. reference it from a `Pod`).

Jump to the [Installation](#installation) section to get up and running.

The [Usage](#usage) section explores in more detail how you craft `SealedSecret` resources.

### SealedSecrets as templates for secrets

The previous example only focused on the encrypted secret items themselves, but the relationship between a `SealedSecret` custom resource and the `Secret` it unseals into is similar in many ways (but not in all of them) to the familiar `Deployment` vs `Pod`.

In particular, the annotations and labels of a `SealedSecret` resource are not the same as the annotations of the `Secret` that gets generated out of it.

To capture this distinction, the `SealedSecret` object has a `template` section which encodes all the fields you want the controller to put in the unsealed `Secret`.

This includes metadata such as labels or annotations, but also things like the `type` of the secret.

```yaml
apiVersion: bitnami.com/v1alpha1
kind: SealedSecret
metadata:
  name: mysecret
  namespace: mynamespace
  annotations:
    "kubectl.kubernetes.io/last-applied-configuration": ....
spec:
  encryptedData:
    .dockerconfigjson: AgBy3i4OJSWK+PiTySYZZA9rO43cGDEq.....
  template:
    type: kubernetes.io/dockerconfigjson
    # this is an example of labels and annotations that will be added to the output secret
    metadata:
      labels:
        "jenkins.io/credentials-type": usernamePassword
      annotations:
        "jenkins.io/credentials-description": credentials from Kubernetes
```

The controller would unseal that into something like:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: mysecret
  namespace: mynamespace
  labels:
    "jenkins.io/credentials-type": usernamePassword
  annotations:
    "jenkins.io/credentials-description": credentials from Kubernetes
  ownerReferences:
  - apiVersion: bitnami.com/v1alpha1
    controller: true
    kind: SealedSecret
    name: mysecret
    uid: 5caff6a0-c9ac-11e9-881e-42010aac003e
type: kubernetes.io/dockerconfigjson
data:
  .dockerconfigjson: ewogICJjcmVk...
```

As you can see, the generated `Secret` resource is a "dependent object" of the `SealedSecret` and as such
it will be updated and deleted whenever the `SealedSecret` object gets updated or deleted.

### Public key / Certificate

The key certificate (public key portion) is used for sealing secrets,
and needs to be available wherever `kubeseal` is going to be
used. The certificate is not secret information, although you need to
ensure you are using the correct one.

`kubeseal` will fetch the certificate from the controller at runtime
(requires secure access to the Kubernetes API server), which is
convenient for interactive use, but it's known to be brittle when users
have clusters with special configurations such as [private GKE clusters](docs/GKE.md#private-gke-clusters) that have
firewalls between master and nodes.

An alternative workflow
is to store the certificate somewhere (e.g. local disk) with
`kubeseal --fetch-cert >mycert.pem`,
and use it offline with `kubeseal --cert mycert.pem`.
The certificate is also printed to the controller log on startup.

Since v0.9.x certificates get automatically renewed every 30 days. It's good practice that you and your team
update your offline certificate periodically. To help you with that, since v0.9.2 `kubeseal` accepts URLs too. You can set up your internal automation to publish certificates somewhere you trust.

```bash
kubeseal --cert https://your.intranet.company.com/sealed-secrets/your-cluster.cert
```

It also recognizes the `SEALED_SECRETS_CERT` env var. (pro-tip: see also [direnv](https://github.com/direnv/direnv)).

> **NOTE**: we are working on providing key management mechanisms that offload the encryption to HSM based modules or managed cloud crypto solutions such as KMS.

### Scopes

SealedSecrets are from the POV of an end user a "write only" device.

The idea is that the SealedSecret can be decrypted only by the controller running in the target cluster and
nobody else (not even the original author) is able to obtain the original Secret from the SealedSecret.

The user may or may not have direct access to the target cluster.
More specifically, the user might or might not have access to the Secret unsealed by the controller.

There are many ways to configure RBAC on k8s, but it's quite common to forbid low-privilege users
from reading Secrets. It's also common to give users one or more namespaces where they have higher privileges,
which would allow them to create and read secrets (and/or create deployments that can reference those secrets).

Encrypted SealedSecret resources are designed to be safe to be looked at without gaining any knowledge about the secrets it conceals. This implies that we cannot allow users to read a SealedSecret meant for a namespace they wouldn't have access to
and just push a copy of it in a namespace where they can read secrets from.

Sealed-secrets thus behaves *as if* each namespace had its own independent encryption key and thus once you
seal a secret for a namespace, it cannot be moved in another namespace and decrypted there.

We don't technically use an independent private key for each namespace, but instead we *include* the namespace name
during the encryption process, effectively achieving the same result.

Furthermore, namespaces are not the only level at which RBAC configurations can decide who can see which secret. In fact, it's possible that users can access a secret called `foo` in a given namespace but not any other secret in the same namespace. We cannot thus by default let users freely rename SealedSecret resources otherwise a malicious user would be able to decrypt any SealedSecret for that namespace by just renaming it to overwrite the one secret she does have access to. We use the same mechanism used to include the namespace in the encryption key to also include the secret name.

That said, there are many scenarios where you might not care about this level of protection. For example, the only people who have access to your clusters are either admins or they cannot read any secret resource at all. You might have a use case for moving a sealed secret to other namespaces (e.g. you might not know the namespace name upfront), or you might not know the name of the secret (e.g. it could contain a unique suffix based on the hash of the contents etc).

These are the possible scopes:

- `strict` (default): the secret must be sealed with exactly the same *name* and *namespace*. These attributes become *part of the encrypted data* and thus changing name and/or namespace would lead to "decryption error".
- `namespace-wide`: you can freely *rename* the sealed secret within a given namespace.
- `cluster-wide`: the secret can be unsealed in *any* namespace and can be given *any* name.

In contrast to the restrictions of *name* and *namespace*, secret *items* (i.e. JSON object keys like `spec.encryptedData.my-key`) can be renamed at will without losing the ability to decrypt the sealed secret.

The scope is selected with the `--scope` flag:

```bash
kubeseal --scope cluster-wide <secret.yaml >sealed-secret.json
```

It's also possible to request a scope via annotations in the input secret you pass to `kubeseal`:

- `sealedsecrets.bitnami.com/namespace-wide: "true"` -> for `namespace-wide`
- `sealedsecrets.bitnami.com/cluster-wide: "true"` -> for `cluster-wide`

The lack of any of such annotations means `strict` mode. If both are set, `cluster-wide` takes precedence.

> NOTE: next release will consolidate this into a single `sealedsecrets.bitnami.com/scope` annotation.

## Installation

See https://github.com/bitnami-labs/sealed-secrets/releases for the latest release and detailed installation instructions.

Cloud platform specific notes and instructions:

- [GKE](docs/GKE.md)

### Controller

Once you deploy the manifest it will create the `SealedSecret` resource
and install the controller into `kube-system` namespace, create a service
account and necessary RBAC roles.

After a few moments, the controller will start, generate a key pair,
and be ready for operation.  If it does not, check the controller
logs.

#### Kustomize

The official controller manifest installation mechanism is just a YAML file.

In some cases you might need to apply your own customizations, like set a custom namespace or set some env variables.

`kubectl` has native support for that, see [kustomize](https://kustomize.io/).

#### Helm Chart

The Sealed Secrets helm chart is now official supported and hosted in this GitHub repo.

```bash
helm repo add sealed-secrets https://bitnami-labs.github.io/sealed-secrets
```

NOTE: The versioning scheme of the helm chart differs from the versioning scheme of the sealed secrets project itself.

Originally the helm chart was maintained by the community and the first version adopted a major version of 1 while the
sealed secrets project itself is still at major 0.
This is ok because the version of the helm chart itself is not meant to be necessarily the version of the app itself.
However this is confusing, so our current versioning rule is:

1. The sealed secret controller version scheme: 0.X.Y
2. The helm chart version scheme: 1.X.Y-rZ

There can be thus multiple revisions of the helm chart, with fixes that apply only to the helm chart without
affecting the static YAML manifests or the controller image itself.

NOTE: the helm chart readme still contains a deprecation notice, but it's no longer reflects reality
and will be removed upon next release.

NOTE: the helm chart by default installs the controller with the name `sealed-secrets`, while the `kubeseal` command line interface (CLI) tries to access the controller with the name `sealed-secrets-controller`. You can explicitly pass `--controller-name` to the CLI:

```bash
kubeseal --controller-name sealed-secrets <args>
```

Alternatively, you can override `fullnameOverride` on the helm chart install.

### Homebrew

The `kubeseal` client is also available on [homebrew](https://formulae.brew.sh/formula/kubeseal):

```bash
brew install kubeseal
```

### MacPorts

The `kubeseal` client is also available on [MacPorts](https://ports.macports.org/port/kubeseal/summary):

```bash
port install kubeseal
```

### Installation from source

If you just want the latest client tool, it can be installed into
`$GOPATH/bin` with:

```bash
(cd /; GO111MODULE=on go get github.com/bitnami-labs/sealed-secrets/cmd/kubeseal@main)
```

You can specify a release tag or a commit SHA instead of `main`.

## Upgrade

Don't forget to check the [release notes](RELEASE-NOTES.md) for guidance about
possible breaking changes when you upgrade the client tool
and/or the controller.

## Usage

```bash
# Create a json/yaml-encoded Secret somehow:
# (note use of `--dry-run` - this is just a local file!)
echo -n bar | kubectl create secret generic mysecret --dry-run=client --from-file=foo=/dev/stdin -o json >mysecret.json

# This is the important bit:
# (note default format is json!)
kubeseal <mysecret.json >mysealedsecret.json

# mysealedsecret.json is safe to upload to github, post to twitter,
# etc.  Eventually:
kubectl create -f mysealedsecret.json

# Profit!
kubectl get secret mysecret
```

Note the `SealedSecret` and `Secret` must have **the same namespace and
name**. This is a feature to prevent other users on the same cluster
from re-using your sealed secrets. See the [Scopes](#scopes) section for more info.

`kubeseal` reads the namespace from the input secret, accepts an explicit `--namespace` arg, and uses
the `kubectl` default namespace (in that order). Any labels,
annotations, etc on the original `Secret` are preserved, but not
automatically reflected in the `SealedSecret`.

By design, this scheme *does not authenticate the user*.  In other
words, *anyone* can create a `SealedSecret` containing any `Secret`
they like (provided the namespace/name matches).  It is up to your
existing config management workflow, cluster RBAC rules, etc to ensure
that only the intended `SealedSecret` is uploaded to the cluster.  The
only change from existing Kubernetes is that the *contents* of the
`Secret` are now hidden while outside the cluster.

### Managing existing secrets

If you want `SealedSecret` controller to take management of an existing `Secret` (i.e. overwrite it when unsealing a `SealedSecret` with the same name and namespace), then you have to annotate that `Secret` with the annotation `sealedsecrets.bitnami.com/managed: "true"` ahead applying the [Usage](#usage) steps.

### Update existing secrets

If you want to add or update existing sealed secrets without having the cleartext for the other items,
you can just copy&paste the new encrypted data items and merge it into an existing sealed secret.

You must take care of sealing the updated items with a compatible name and namespace (see note about scopes above).

You can use the `--merge-into` command to update an existing sealed secrets if you don't want to copy&paste:

```bash
echo -n bar | kubectl create secret generic mysecret --dry-run=client --from-file=foo=/dev/stdin -o json \
  | kubeseal > mysealedsecret.json
echo -n baz | kubectl create secret generic mysecret --dry-run=client --from-file=bar=/dev/stdin -o json \
  | kubeseal --merge-into mysealedsecret.json
```

### Raw mode (experimental)

Creating temporary Secret with the `kubectl` command, only to throw it away once piped to `kubeseal` can
be a quite unfriendly user experience. We're working on an overhaul of the CLI experience. In the meantime,
we offer an alternative mode where kubeseal only cares about encrypting a value to stdout, and it's your responsibility to put it inside a `SealedSecret` resource (not unlike any of the other k8s resources).

It can also be useful as a building block for editor/IDE integrations.

The downside is that you have to be careful to be consistent with the sealing scope, the namespace and the name.

See [Scopes](#scopes)

`strict` scope (default):

```console
$ echo -n foo | kubeseal --raw --from-file=/dev/stdin --namespace bar --name mysecret
AgBChHUWLMx...
```

`namespace-wide` scope:

```console
$ echo -n foo | kubeseal --raw --from-file=/dev/stdin --namespace bar --scope namespace-wide
AgAbbFNkM54...
```
Include the `sealedsecrets.bitnami.com/namespace-wide` annotation in the `SealedSecret`
```yaml
metadata:
  annotations:
    sealedsecrets.bitnami.com/namespace-wide: "true"
```

`cluster-wide` scope:

```console
$ echo -n foo | kubeseal --raw --from-file=/dev/stdin --scope cluster-wide
AgAjLKpIYV+...
```
Include the `sealedsecrets.bitnami.com/cluster-wide` annotation in the `SealedSecret`
```yaml
metadata:
  annotations:
    sealedsecrets.bitnami.com/cluster-wide: "true"
```

## Secret Rotation

You should always rotate your secrets. But since your secrets are encrypted with another secret,
you need to understand how these two layers relate in order to take the right decisions.

TL;DR:

> If a *sealing* private key is compromised, you need to follow the instructions below in "Early key renewal"
> section before rotating any of your actual secret values.
>
> SealedSecret key renewal and re-encryption features are **not a substitute** for periodical rotation of your actual secret values.

### Sealing key renewal

Sealing keys are automatically renewed every 30 days. Which means a new sealing key is created and appended to the set of active sealing keys the controller can use to unseal Sealed Secret resources.

The most recently created sealing key is the one used to seal new secrets when you use `kubeseal` and it's the one whose certificate is downloaded when you use `kubeseal --fetch-cert`.

The renewal time of 30d is a reasonable default, but it can be tweaked as needed
with the `--key-renew-period=<value>` flag for the command in the pod template of the sealed secret controller. The `value` field can be given as golang
duration flag (eg: `720h30m`).

A value of `0` will disable automatic key renewal. Of course, it's possible you have a valid use case for disabling automatic sealing key renewal; but experience has shown that new users often tend to jump to conclusions that they want control over key renewal, before fully understanding how sealed secrets work. Read more about this in the [common misconceptions](#common-misconceptions-about-key-renewal) section below.

> Unfortunately you cannot use e.g. "d" as a unit for days because that's not supported by the Go stdlib. Instead of hitting your face with a palm, take this as an opportunity to meditate on the [falsehoods programmers believe about time](https://infiniteundo.com/post/25326999628/falsehoods-programmers-believe-about-time).

A common misunderstanding is that key renewal is often thought of as a form of key rotation, where the old key is not only obsolete but actually bad and that you thus want to get rid of it.
It doesn't help that this feature has been historically called "key rotation", which can add to the confusion.

Sealed secrets are not automatically rotated and old keys are not deleted
when new keys are generated. Old sealed secrets resources can be still decrypted (that's because old sealing keys are not deleted).

### User secret rotation

The *sealing key* renewal and SealedSecret rotation are **not a substitute** for rotating your actual secrets.

A core value proposition of this tool is:

> Encrypt your Secret into a SealedSecret, which *is* safe to store - even to a public repository.

If you store anything in a version control storage, and in a public one in particular, you must assume
you cannot ever delete that information.

*If* a sealing key somehow leaks out of the cluster you must consider all your SealedSecret resources
encrypted with that key as compromised. No amount of sealing key rotation in the cluster or even re-encryption of existing SealedSecrets files can change that.

The best practice is to periodically rotate all your actual secrets (e.g. change the password) **and** craft new
SealedSecret resource with those new secrets.

But if the sealed secrets controller were not renewing the *sealing key* that rotation would be moot,
since the attacker could just decrypt the new secrets as well. Thus, you need to do both: periodically renew the sealing key and rotate your actual secrets!

### Early key renewal

If you know or suspect a *sealing key* has been compromised you should renew the key ASAP before you
start sealing your new rotated secrets, otherwise you'll be giving attackers access to your new secrets as well.

A key can be generated early by passing the current timestamp to the controller into a flag called `--key-cutoff-time` or an env var called `SEALED_SECRETS_KEY_CUTOFF_TIME`. Expected format is RFC1123, you can generate it with the `date -R` unix command.

### Common misconceptions about key renewal

Sealed secrets sealing keys are not access control keys (e.g. like a password); they are more like the GPG key you might use to read encrypted mail sent to you. Let's continue with the email analogy for a bit:

Imagine you have reasons to believe your private GPG key might have been compromised. You'd have more to lose than to gain if the first thing you do is to just delete your private key. All the previous emails sent with that key are no longer accessible to you (unless you have a decrypted copy of those emails), nor are new emails sent by your friends whom you have not yet managed to tell to use the new key.

Sure, the content of those encrypted emails is not secure, as an attacker might now be able to decrypt them, but what's done is done. Your sudden loss of ability to read those emails surely doesn't undo the damage; if anything, it's worse because you no longer know for sure what secret the attacker got to know. What you really want to do is to make sure that your friend stops using your old key and that from now on all further communication is encrypted with a new key pair (i.e. your friend must know about that new key).

The same logic applies to SealedSecrets. The ultimate goal is securing your actual "user" secrets. The "sealing" secrets are just a mechanism, an "envelope". If a secret is leaked there is no going back; what's done is done.

You first need to ensure that new secrets don't get encrypted with that old compromised key (in the email analogy above that's: create a new key pair and give all your friends your new public key).

The second logical step is to neutralize the damage, which depends on the nature of the secret. A simple example is a database password: if you accidentally leak your database password, the thing you're supposed to do is simply to change your database password (on the database; and revoke the old one!) *and* update the SealedSecret resource with the new password (i.e. running `kubeseal` again).

Both steps are described in the previous sections, albeit in a less verbose way. There is no shame in reading them again, now that you have a more in-depth grasp of the underlying rationale.

### Manual key management (advanced)

The sealed secrets controller and the associated workflow is designed to keep old sealing keys around and periodically add new ones. You should not delete old keys unless you know what you're doing.

That said, if you want you can manually manage (create, move, delete) *sealing keys*. They are just normal k8s secrets living in the same namespace where the sealed secret controller lives (usually `kube-system`, but it's configurable).

There are advanced use cases that you can address by creative management of the sealing keys.
For example, you can share the same sealing key among a few clusters so that you can apply exactly the same sealed secret in multiple clusters.
Since sealing keys are just normal k8s secrets you can even use sealed secrets itself and use a GitOps workflow to manage your sealing keys (useful when you want to share the same key among different clusters)!

Labelling a *sealing key* secret with anything other than `active` effectively deletes
the key from the sealed secrets controller, but it is still available in k8s for
manual encryption/decryption if need be.

**NOTE** Sealed secrets currently does not automatically pick up manually created, deleted or relabeled sealing keys, an admin must restart the controller before the effect will apply.

### Re-encryption (advanced)

Before you can get rid of some old sealing keys you need to re-encrypt your SealedSecrets with the latest private key.

```bash
kubeseal --re-encrypt <my_sealed_secret.json >tmp.json \
  && mv tmp.json my_sealed_secret.json
```

The invocation above will produce a new sealed secret file freshly encrypted with
the latest key, without making the secrets leave the cluster to the client. You can then save that file
in your version control system (`kubeseal --re-encrypt` doesn't update the in-cluster object).

Currently, old keys are not garbage collected automatically.

It's a good idea to periodically re-encrypt your SealedSecrets. But as mentioned above, don't lull yourself in a false sense of security: you must assume the old version of the SealedSecret (the one encrypted with a key you think of as dead) is still potentially around and accessible to attackers. I.e. re-encryption is not a substitute for periodically rotating your actual secrets.

## Details (advanced)

This controller adds a new `SealedSecret` custom resource. The
interesting part of a `SealedSecret` is a base64-encoded
asymmetrically encrypted `Secret`.

The controller maintains a set of private/public key pairs as kubernetes
secrets. Keys are labelled with `sealedsecrets.bitnami.com/sealed-secrets-key`
and identified in the label as either `active` or `compromised`. On startup,
The sealed secrets controller will...

1. Search for these keys and add them to its local store if they are
labelled as active.
2. Create a new key
3. Start the key rotation cycle

### Crypto

More details about crypto can be found [here](docs/developer/crypto.md).

## Developing

More details about crypto can be found [in the Developer Guide](docs/developer/README.md).

## FAQ

### Will you still be able to decrypt if you no longer have access to your cluster?

No, the private keys are only stored in the Secret managed by the controller (unless you have some other backup of your k8s objects). There are no backdoors - without that private key used  to encrypt a given SealedSecrets, you can't decrypt it. If you can't get to the Secrets with the encryption keys, and you also can't get to the decrypted versions of your Secrets live in the cluster, then you will need to regenerate new passwords for everything, seal them again with a new sealing key, etc.

### How can I do a backup of my SealedSecrets?

If you do want to make a backup of the encryption private keys, it's easy to do from an account with suitable access and:

```bash
kubectl get secret -n kube-system -l sealedsecrets.bitnami.com/sealed-secrets-key -o yaml >master.key
kubectl get secret -n kube-system sealed-secrets-key -o yaml >>master.key
```

NOTE: you need the second statement only if you ever installed sealed-secrets older than version 0.9.x on your cluster.

NOTE: This file will contain the controller's public + private keys and should be kept omg-safe!

To restore from a backup after some disaster, just put that secrets back before starting the controller - or if the controller was already started, replace the newly-created secrets and restart the controller:

```bash
kubectl apply -f master.key
kubectl delete pod -n kube-system -l name=sealed-secrets-controller
```

### Can I decrypt my secrets offline with a backup key?

While treating sealed-secrets as long term storage system for secrets is not the recommended use case, some people
do have a legitimate requirement for being able to recover secrets when the k8s cluster is down and restoring a backup into a new sealed-secrets controller deployment is not practical.

If you have backed up one or more of your private keys (see previous question), you can use the `kubeseal --recovery-unseal --recovery-private-key file1.key,file2.key,...` command to decrypt a sealed secrets file.

### What flags are available for kubeseal?

You can check the flags available using `kubeseal --help`.

### How do I update parts of JSON/YAML/TOML/.. file encrypted with sealed secrets?

A kubernetes secret resource contains multiple items, basically a flat map of key/value pairs.
SealedSecrets operate at that level, and does not care what you put in the values. In other words
it cannot make sense of any structured configuration file you might have put in a secret and thus
cannot help you update individual fields in it.

Since this is a common problem, especially when dealing with legacy applications, we do offer an [example](docs/examples/config-template) of a possible workaround.

### Can I bring my own (pre-generated) certificates?

Yes, you can provide the controller with your own certificates, and it will consume them.
Please check [here](docs/bring-your-own-certificates.md) for a workaround.

### How to use kubeseal if the controller is not running within the `kube-system` namespace?

If you installed the controller in a different namespace than the default `kube-system`, you need to provide this namespace
to the `kubeseal` commandline tool. There are two options: You can specify the namespace via the command line option
`--controller-namespace <namespace>` or via the environment variable `SEALED_SECRETS_CONTROLLER_NAMESPACE`.

Example:

```bash
# Provide the namespace via the command line option
kubeseal --controller-namespace sealed-secrets <mysecret.json >mysealedsecret.json

# Provide the namespace via the environment variable
export SEALED_SECRETS_CONTROLLER_NAMESPACE=sealed-secrets
kubeseal <mysecret.json >mysealedsecret.json
```

### How to verify the images?

Our images are being signed using [cosign](https://github.com/sigstore/cosign). The signatures have been saved in our [GitHub Container Registry](https://github.com/bitnami-labs/sealed-secrets/pkgs/container/sealed-secrets/signs).

It is pretty simple to verify the images:

```bash
# export the COSIGN_VARIABLE setting up the GitHub container registry signs path
export COSIGN_REPOSITORY=ghcr.io/bitnami-labs/sealed-secrets-controller/signs

# verify the image uploaded in GHCR
cosign verify --key .github/workflows/cosign.pub ghcr.io/bitnami-labs/sealed-secrets-controller:latest

# verify the image uploaded in Dockerhub
cosign verify --key .github/workflows/cosign.pub docker.io/bitnami/sealed-secrets-controller:latest
```

### How to use one controller for a subset of namespaces

If you want to use one controller for more than one namespace, but not all namespaces, you can provide additional namespaces using the command line flag `--additional-namespaces=<namespace1>,<namespace2>,<...>`. Make sure you provide appropriate roles and rolebindings in the target namespaces, so the controller can manage the secrets in there.

## Community

- [#sealed-secrets on Kubernetes Slack](https://kubernetes.slack.com/messages/sealed-secrets)

Click [here](http://slack.k8s.io) to sign up to the Kubernetes Slack org.

### Related projects

- Visual Studio Code extension: https://marketplace.visualstudio.com/items?itemName=codecontemplator.kubeseal
- WebSeal: generates secrets in the browser : https://socialgouv.github.io/webseal
- HybridEncrypt TypeScript implementation : https://github.com/SocialGouv/aes-gcm-rsa-oaep
- [DEPRACATED] Sealed Secrets Operator: https://github.com/disposab1e/sealed-secrets-operator-helm


</details>



</br>



[***GitHub - argoproj-labs/argocd-autopilot: Argo-CD Autopilot***](https://github.com/argoproj-labs/argocd-autopilot)

![GitHub last commit](https://img.shields.io/github/last-commit/argoproj-labs/argocd-autopilot) ![GitHub Repo stars](https://img.shields.io/github/stars/argoproj-labs/argocd-autopilot?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/argoproj-labs/argocd-autopilot)


***QUICK INSTALL***

```bash
curl -L --silent https://github.com/argoproj-labs/argocd-autopilot/releases/download/$(curl -L -s "https://api.github.com/repos/argoproj-labs/argocd-autopilot/releases/latest" | grep -Poe '"tag_name": "\K.*?(?=")' | head -n 1)/argocd-autopilot-linux-amd64.tar.gz | tar zx && mv ./argocd-autopilot-* ./argocd-autopilot
```


</br>


<details>

<summary>README</summary> 

<p align="center"><img src="./docs/assets/argo_autopilot.png" alt="Argo Logo"></p>

[![Codefresh build status]( https://g.codefresh.io/api/badges/pipeline/codefresh-inc/argocd-autopilot%2Frelease?type=cf-1)]( https://g.codefresh.io/public/accounts/codefresh-inc/pipelines/new/60881f8199c9564ef31aac61) 
[![codecov](https://codecov.io/gh/argoproj-labs/argocd-autopilot/branch/main/graph/badge.svg?token=IDyZNfRUfY)](https://codecov.io/gh/argoproj-labs/argocd-autopilot) 
[![Documentation Status](https://readthedocs.org/projects/argocd-autopilot/badge/?version=latest)](https://argocd-autopilot.readthedocs.io/en/latest/?badge=latest)
[![slack](https://img.shields.io/badge/slack-argoproj-brightgreen.svg?logo=slack)](https://argoproj.github.io/community/join-slack/)

## Introduction

New users to GitOps and Argo CD are not often sure how they should structure their repos, add applications, promote apps across environments, and manage the Argo CD installation itself using GitOps. 

Argo CD Autopilot saves operators time by:

- Installing and managing the Argo CD application using GitOps.
- Providing a clear structure for how applications are to be added and updated, all from git.
- Creating a simple pattern for making updates to applications and promoting those changes across environments.
- Enabling better disaster recovery by being able to bootstrap new clusters with all the applications previously installed.
- Handles secrets for Argo CD to prevent them from spilling into plaintext git. (Soon to come)

The Argo-CD Autopilot is a tool which offers an opinionated way of installing Argo-CD and managing GitOps repositories.

## Installation
### Using brew:
```bash
# install
brew install argocd-autopilot

# check the installation
argocd-autopilot version
```

### Using scoop:
```bash
# update
scoop update

# install
scoop install argocd-autopilot

# check the installation
argocd-autopilot version
```

### Using chocolatey:
```bash
# install
choco install argocd-autopilot

# check the installation
argocd-autopilot version
```

### Linux AUR:
```bash
# install
yay -S argocd-autopilot-bin
# or
sudo pacman -S argocd-autopilot-bin

# check the installation
argocd-autopilot version
```

### Linux and WSL (using curl):
```bash
# get the latest version or change to a specific version
VERSION=$(curl --silent "https://api.github.com/repos/argoproj-labs/argocd-autopilot/releases/latest" | grep '"tag_name"' | sed -E 's/.*"([^"]+)".*/\1/')

# download and extract the binary
curl -L --output - https://github.com/argoproj-labs/argocd-autopilot/releases/download/$VERSION/argocd-autopilot-linux-amd64.tar.gz | tar zx

# move the binary to your $PATH
mv ./argocd-autopilot-* /usr/local/bin/argocd-autopilot

# check the installation
argocd-autopilot version
```

### Mac (using curl):
```bash
# get the latest version or change to a specific version
VERSION=$(curl --silent "https://api.github.com/repos/argoproj-labs/argocd-autopilot/releases/latest" | grep '"tag_name"' | sed -E 's/.*"([^"]+)".*/\1/')

# download and extract the binary
curl -L --output - https://github.com/argoproj-labs/argocd-autopilot/releases/download/$VERSION/argocd-autopilot-darwin-amd64.tar.gz | tar zx

# move the binary to your $PATH
mv ./argocd-autopilot-* /usr/local/bin/argocd-autopilot

# check the installation
argocd-autopilot version
```

## Docker
When using the Docker image, you have to provide the `.kube` and `.gitconfig` directories as mounts to the running container:
```
docker run \
  -v ~/.kube:/home/autopilot/.kube \
  -v ~/.gitconfig:/home/autopilot/.gitconfig \
  -it quay.io/argoprojlabs/argocd-autopilot <cmd> <flags>
```

## Getting Started
```bash
# All of the commands need your git token with the --git-token flag,
# or the GIT_TOKEN env variable:

    export GIT_TOKEN=<YOUR_TOKEN>

# The commands will also need your repo clone URL with the --repo flag,
# or the GIT_REPO env variable:

    export GIT_REPO=<REPO_URL>

# 1. Run the bootstrap installation on your current kubernetes context.
# This will install argo-cd as well as the application-set controller.

    argocd-autopilot repo bootstrap

# Please note that this will automatically attempt to create a private repository,
# if the clone URL references a non-existing one. If the repository already exists,
# the command will just clone it.

# 2. Create your first project

    argocd-autopilot project create my-project

# 3. Install your first application on your project

    argocd-autopilot app create demoapp --app github.com/argoproj-labs/argocd-autopilot/examples/demo-app/ -p my-project
```

Now, if you go to your Argo-CD UI, you should see something similar to this:

![](./docs/assets/getting_started_apps_1.png)

Head over to our [Getting Started](./docs/Getting-Started.md) guide for further details.

## How it works
The autopilot bootstrap command will deploy an Argo-CD manifest to a target k8s cluster, and will commit an Argo-CD Application manifest under a specific directory in your GitOps repository. This Application will manage the Argo-CD installation itself - so after running this command, you will have an Argo-CD deployment that manages itself through GitOps.

From that point on, the user can create Projects and Applications that belong to them. Autopilot will commit the required manifests to the repository. Once committed, Argo-CD will do its magic and apply the Applications to the cluster.

An application can be added to a project from a public git repo + path, or from a directory in the local filesystem.

## Architecture
![Argo-CD Autopilot Architecture](./docs/assets/architecture.png)

Autopilot communicates with the cluster directly **only** during the bootstrap phase, when it deploys Argo-CD. After that, most commands will only require access to the GitOps repository. When adding a Project or Application to a remote k8s cluster, autopilot will require access to the Argo-CD server.

You can read more about it in the [official proposal doc](https://docs.google.com/document/d/1gxKxaMQzH9nNDWW9mZV5_cS7EO4S-pm1s_u5aMK-PZQ/edit?usp=sharing).

## Features
* Opinionated way to build a multi-project multi-application system, using GitOps principles.
* Create a new GitOps repository, or use an existing one.
* Supports creating the entire directory structure under any path the user requires.
* When adding applications from a public repo, allow committing as either a kustomization that references the public repo, or as a "flat" manifest file containing all the required resources.
* Use a different cluster from the one Argo-CD is running on, as a default cluster for a Project, or a target cluster for a specific Application.

## Development Status
Argo-CD autopilot is currently under active development. Some of the basic commands are not yet implemented, but we hope to complete most of them in the coming weeks.

## Slack Channel
Join us in channel #argo-autopilot in CNCF slack workspace.

Click here to join: https://slack.cncf.io/


</details>



</br>



[***GitHub - redhat-cop/patch-operator: An operator to apply patches to Kubernetes objects in a declarative way.***](https://github.com/redhat-cop/patch-operator)

![GitHub last commit](https://img.shields.io/github/last-commit/redhat-cop/patch-operator) ![GitHub Repo stars](https://img.shields.io/github/stars/redhat-cop/patch-operator?style=social) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/redhat-cop/patch-operator)



</br>



</br>


