<!-- Simplified version of https://github.com/othneildrew/Best-README-Template -->

<!-- For "back to top" links -->
<a name="readme-top"></a>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li>
      <a href="#usage">Usage</a>
      <ul>
        <li><a href="#running-locally">Running Locally</a></li>
        <li><a href="#deploying-to-azure">Deploying To Azure</a></li>
      </ul>
    </li>
    <li>
      <a href="#roadmap">Roadmap</a>
      <ul>
        <li><a href="#essential-features">Essential Features</a></li>
        <li><a href="#nonessential-features">Nonessential Features</a></li>
      </ul>
    </li>
    <li>
      <a href="#acknowledgments">Acknowledgments</a>
    </li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project is a simple website that uses object storage and a NoSQL database to store data.
It is meant to practice using multiple cloud services together.
The application was designed to use various Microsoft Azure services,
specifically Blob Storage and Cosmos DB while being hosted using App Service.

I completed this project as an assignment for my Cloud Computing course at the University of Washington Bothell.
The specifications provided can be found at [`specifications.pdf`](specifications.pdf).

### Built With

* [![Python][Python-shield]][Python-url]
* [![Flask][Flask-shield]][Flask-url]
* [![Azure][Azure-shield]][Azure-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

1. [Create][Azure-account] an Azure account.

2. [Create][Azure-cosmos-db] an Azure Cosmos DB account.

3. [Install][Python-download] Python 3.9 or later.

   macOS/Linux: `python3 --version`

   Windows: `py --version`

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE -->
## Usage

### Running Locally

1. Create a virtual environment.

   macOS/Linux: `python3 -m venv .venv`

   Windows: `py -m venv .venv`

2. Activate the virtual environment.

   macOS/Linux: `source .venv/bin/activate`

   Windows: `.venv\Scripts\activate`

3. Install the dependencies.
   ```commandline
   pip install -r requirements.txt
   ```

4. Set the environment variables.
   Follow the instructions in the [`.env`](.env) file.

5. Run the application.
   ```commandline
   flask run
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Deploying To Azure

There are a variety of ways to deploy the application to Azure,
but the following are the instructions for deploying to an Azure Web App using the Azure CLI.

1. [Create][Azure-app-services] an Azure Web App.

2. Set the environment variables.
   Follow the instructions in the [`.env`](.env) file.

3. [Install][Azure-cli] the Azure CLI.
   ```commandline
   az --version
   ```

4. Login to Azure.
   ```commandline
   az login
   ```

5. Deploy the application to the Azure Web App.
   ```commandline
   az webapp up --name [web-app-name]
   ```

The application should now be running at the Azure Web App's domain
(by default `<web-app-name>.azurewebsites.net`).

#### Additional References
* [Azure Quickstart: Deploy A Python Web App][Azure-python-quickstart] was helpful during development.
* The [Azure Tools][Azure-tools] extension for [Visual Studio Code][Visual-studio-code] might simplify deployment.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

### Essential Features

- [X] Set-up the flask framework.
- [X] Implement the back-end API.
  - [X] Add `GET /people`.
  - [X] Add `POST /people`.
  - [X] Add `DELETE /people`.
- [ ] Implement the front-end webpage.
  - [ ] Add the `Load Data` button.
  - [ ] Add the `Clear Data` button.
  - [ ] Add the `Query` button.

### Nonessential Features

- [ ] Allow `POST /people` to accept custom data, including URLs, files, and plain-text.
- [ ] Allow query results to be sorted by the front-end.
- [ ] Allow partial matches when querying.
- [ ] Include entry relevancy in query results.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Azure Quickstart: Deploy A Python Web App][Azure-python-quickstart]
* [Flask Installation][Flask-installation]
* [Flask Quickstart][Flask-quickstart]
* [README Template][Readme-template]
* [Img Shields][Shields-io]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- Azure Links -->
[Azure-account]:           https://azure.microsoft.com/en-us/free
[Azure-cli]:               https://learn.microsoft.com/en-us/cli/azure/install-azure-cli
[Azure-python-quickstart]: https://learn.microsoft.com/en-us/azure/app-service/quickstart-python
[Azure-app-services]:      https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/Microsoft.Web%2Fsites
[Azure-cosmos-db]:         https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/Microsoft.DocumentDb%2FdatabaseAccounts
[Azure-tools]:             https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-node-azure-pack

<!-- Other External Links -->
[Flask-installation]: https://flask.palletsprojects.com/en/3.0.x/installation/
[Flask-quickstart]:   https://flask.palletsprojects.com/en/3.0.x/quickstart/
[Python-download]:    https://www.python.org/downloads/
[Readme-template]:    https://github.com/othneildrew/Best-README-Template
[Shields-io]:         https://shields.io
[Visual-studio-code]: https://code.visualstudio.com/

<!-- Shields and URLs for "Built With" -->
[Azure-shield]:  https://img.shields.io/badge/Azure-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white
[Azure-url]:     https://azure.microsoft.com/en-us
[Flask-shield]:  https://img.shields.io/badge/Flask-3baac3?style=for-the-badge&logo=flask&logoColor=white
[Flask-url]:     https://flask.palletsprojects.com/en/3.0.x/
[Python-shield]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]:    https://www.python.org/
