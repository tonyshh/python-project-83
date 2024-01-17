### Hexlet tests and linter status:

[![Actions Status](https://github.com/tonyshh/python-project-83/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/tonyshh/python-project-83/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/f2135ccff4ea992980bc/maintainability)](https://codeclimate.com/github/tonyshh/python-project-83/maintainability)

# [Page Analyzer](https://hexlet-code-jwtk.onrender.com)

это сайт, который анализирует указанные страницы на SEO-пригодность

![](https://cdn2.hexlet.io/store/derivatives/original/5b424cba5ea10b7cfef0bd51ab74d4c6.png)

![](https://cdn2.hexlet.io/derivations/image/original/eyJpZCI6ImI4OTljYTRmNDMyMTVmZWViMTk4MzIxOGYyNzhkNDdjLnBuZyIsInN0b3JhZ2UiOiJjYWNoZSJ9?signature=49835a58ff26000ab22fa23ee14f0c9530b2a066e5ac6db361a3d9575d2756b8)

![](https://cdn2.hexlet.io/derivations/image/original/eyJpZCI6ImM1MDI2MzNmZTBjODUxYTJjMzIxYWI5MWFkNWJhY2Q0LnBuZyIsInN0b3JhZ2UiOiJjYWNoZSJ9?signature=c1d7f4ae3d6f19a532f91a1d558f49f9ed4994c89fbaf5ffc2a5e626db9aa7b8)


## Getting Started

#### Clone the current repository via command:
```git clone https://github.com/tonyshh/python-project-83```

***

## Requirements
* python >= 3.10
* Poetry >= 1.5.1
***

## Required packages
* Flask ^3.0.0
* Python-dotenv  ^1.0.1
* to avoid psycopg problems with different OS, install psycopg2-binary ^2.9.4
* Every other packages are shown inside pyproject.toml

#### Check your pip version with the following command:
```python -m pip --version```

#### Make sure that pip is always up-to-date. If not, use the following:
```python -m pip install --upgrade pip```

#### Next install poetry on your OS. (the link is below)
[Poetry installation](https://python-poetry.org/docs/)
##### don't forget to init poetry packages with command ```poetry init```


## Makefile 
#### For every project should be configured a Makefile to initiate the project without requiring manual commands
#### Current project starts after typing ```make setup```
#### Inside our ```make setup``` we have 2 commands hidden:
* ``` make install```, which makes poetry install packages from pyproject.toml
* ```make lock```, which locks poetry packages inside poetry.lock
***

#### After configuration, you should use ```make dev``` to start your flask app








