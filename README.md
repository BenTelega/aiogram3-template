# Template Aiogram 3 with SQLAlchemy

### Quickly start:
#### You need to create ```.env``` file in ```./settings``` folder and add there these values:

```
BOT_TOKEN=
DB_CONN_STRING=postgresql+asyncpg://{username}:{password}@{host}:{port}/{database}

```

#### Also you need to replace ```username``` and *others* values in the ```DB_CONN_STRING```

### That`s It! Run this commands in the root directory 

```console
$ > pip install poetry
$ > poetry install
& > poetry run app.py
```

### There are also Others Opportunities here: 
- APScheduler
- Logger
- JSONConfig -> [docs here](https://github.com/enveloss/py_json_config)
- Made Middlewares 
- Simple admin-section (you need to setting it)
- Tools to use db