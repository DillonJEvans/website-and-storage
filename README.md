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
specifically Blob Storage and Cosmos DB while being hosted on App Service.

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
2. [Install][Azure-cli] the Azure CLI.
   ```commandline
   az --version
   ```
3. [Install][Python-download] Python 3.9 or later.

   Windows: `py --version`

   macOS/Linux: `python3 --version`

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE -->
## Usage

### Running Locally

1. Create a virtual environment.

   Windows: `py -m venv .venv`

   macOS/Linux: `python3 -m venv .venv`

2. Activate the virtual environment.

   Windows: `.venv\Scripts\activate`

   macOS/Linux: `source .venv/bin/activate`

3. Install the dependencies.
   ```commandline
   pip install -r requirements.txt
   ```

4. Run the application.
   ```commandline
   flask run
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Deploying To Azure

1. Login to Azure.
   ```commandline
   az login
   ```

2. Deploy the application to Azure.
   ```commandline
   az webapp up --name [web-app-name]
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

### Essential Features

- [X] Set-up the flask framework.
- [ ] Implement the back-end API.
  - [ ] Add the `/people` endpoint.
  - [ ] Add the `/people/<person>` endpoint.
- [ ] Implement the front-end webpage.
  - [ ] Add the `Load Data` button.
  - [ ] Add the `Clear Data` button.
  - [ ] Add the `Query` button.

### Nonessential Features

- [ ] Allow query results to be sorted.
- [ ] Allow partial matches when querying.
- [ ] Include entry relevancy in query results.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Azure Quickstart: Deploy A Python Web App][Azure-python-quickstart]
* [Flask Installation][Flask-installation]
* [Flask Quickstart][Flask-quickstart]
* [README Template](https://github.com/othneildrew/Best-README-Template)
* [Img Shields](https://shields.io)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- External Links -->
[Azure-account]:           https://azure.microsoft.com/en-us/free
[Azure-cli]:               https://learn.microsoft.com/en-us/cli/azure/install-azure-cli
[Azure-python-quickstart]: https://learn.microsoft.com/en-us/azure/app-service/quickstart-python
[Flask-installation]:      https://flask.palletsprojects.com/en/3.0.x/installation/
[Flask-quickstart]:        https://flask.palletsprojects.com/en/3.0.x/quickstart/
[Python-download]:         https://www.python.org/downloads/

<!-- Shields and URLs for "Built With" -->
[Azure-shield]:  https://img.shields.io/badge/Azure-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white
[Azure-url]:     https://azure.microsoft.com/en-us
[Flask-shield]:  https://img.shields.io/badge/Flask-3baac3?style=for-the-badge&logo=flask&logoColor=white
[Flask-url]:     https://flask.palletsprojects.com/en/3.0.x/
[Python-shield]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]:    https://www.python.org/
