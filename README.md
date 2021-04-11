# A POC for loading 3 csv files into MongoDB

## Testing env
- d1: run jupyter note book
- d2: MongoDB, LDAP, KMIP, PostgreSQL. As I don't install these sofeware on my host machine, the port are mapped as they are, i.e. 27017 to 27017
- d orcl: oracle 12.2 database
- host machine: SqlDeveloper, VS code, Python3 (venv)

```bash
                ┌───────────────────────────────────────────────────┐
                │                                                   │
                │ ┌─────────────┐  ┌─────────────┐  ┌─────────────┐ │
                │ │             │  │             │  │             │ │
                │ │    d1       │  │      d2     │  │    d orcl   │ │
                │ └─────────────┘  └─────────────┘  └─────────────┘ │
                │                                                   │
                │   SqlDeveloper, VS code, Python 3                 │
                │                                 host machine      │
                └───────────────────────────────────────────────────┘
```

## Plan
- design layout
- Read config and parse configure file
- connect to DB
- read file and load into DB with simple json structure
    - prepare client file 1000 records, keep script to prepare it
    - load client file
    - load file with relationship

## Execution
- Create RDBMS table in oracle 
    - scripts/oracle_00010_create_table.sql
- Prepare *customer* data in oracle and load into MongoDB
    - prepare: scripts/oracle_00020_prepare_data_customer.sql
    - load: note/load_customer.ipynb


## Directory layout

```bash
    python_data_load/
    ├── app_config.py       # read and parse app_config.yml
    ├── app_config.yml      # all configuration related to this app, i.e. DB connection
    ├── data_load.py        # read file and load
    ├── database.py         # database related modules
    └── requirements.txt    # python dependency packages.

```

## How to run

To run **data_load**, you need to download the source code. Then open a terminal or command-line window and run the following steps:

1. Create and activate a Python virtual environment

```sh
$ cd python_data_load/
$ python3 -m venv .venv
$ source .venv/bin/activate
(venv) $
```

2. Install the dependencies

```sh
(venv) $ python3 -m pip install -r requirements.txt
```

3. Run the application

```sh
(venv) $ python3 data_load.py
```

## Data model

### ERD

![data model erd view](images/oracle_erd.png)
### tabular view

![data model tabular view](images/data_model_tabular_view.png )

