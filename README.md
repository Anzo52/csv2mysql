<h1 align="center">csv2mysql</h1>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/Anzo52/csv2mysql.svg)](https://github.com/kylelobo/The-Documentation-Compendium/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/Anzo52/csv2mysql.svg)](https://github.com/Anzo52/csv2mysql/pulls)
[![License](https://img.shields.io/badge/license-GPL3-blue.svg)](/LICENSE)

</div>

---

<p align="center"> Python script to convert csv files to mysql database tables.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Built Using](#built_using)

## 🧐 About <a name = "about"></a>

This project is a python script to convert csv files to mysql database tables. Only tested on Linux, LMDE 5, Debian 10.


## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

As stated in [Getting Started](#getting_started), this project was only tested on Linux, LMDE 5, Debian 10, so built-in tools may not be available on other systems. Please create an issue if you have any problems.
Other than that, you'll need to install the following dependencies (you'll find step-by-step instructions for the Python packages in the [Installing](#installing) section below):
- Python 3.7 or higher
- pip (Python package manager) <-- I used debian's package manager to install this
- Python packages:
  - sqlalchemy
  - pandas
  - numpy
- MySQL server (version 8.0.23) <-- I used debian's package manager to install this
- MySQL Workbench (version 8.0.23) <-- I used debian's package manager to install this

It is recommended to use a virtual environment to install the dependencies. The following instructions will install the dependencies in a virtual environment.
You should also have a MySQL server running on your machine. You can download it from [here](https://dev.mysql.com/downloads/mysql/). Instructions for setting up a MySQL server can be found [here](https://dev.mysql.com/doc/mysql-getting-started/en/).

### Installing and Using <a name = "installing"></a>

Here's a list of the installation steps required to get the project up and running, it's assumed that you already have Python 3.7 or higher, pip, and venv installed. If you don't, please refer to the [Prerequisites](#prerequisites) section above or the [Python documentation](https://www.python.org/about/gettingstarted/):

1. Clone the repository and cd into the project directory
2. Create and activate a virtual environment
3. Install the dependencies
4. Create a MySQL database
5. Run the script


1. Clone the repository and cd into the project directory
```bash
git clone https://github.com/Anzo52/csv2mysql.git
cd csv2mysql
```

2. Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install the dependencies
```bash
pip install -r requirements.txt
```

4. Create a MySQL database
```bash
mysql -u root -p
```
```sql
CREATE DATABASE [database_name];
```

5. Run the script (you'll be prompted to enter the database name, username, and password. Make sure to use the same database name you used in step 4)
```bash
python3 csv2mysql.py
```

## ⛏️ Built Using <a name = "built_using"></a>

- [Python](https://www.python.org/) - Programming language
- [pandas](https://pandas.pydata.org/) - Data analysis and manipulation tool
- [numpy](https://numpy.org/) - Scientific computing package
- [sqlalchemy](https://www.sqlalchemy.org/) - SQL toolkit and Object Relational Mapper
