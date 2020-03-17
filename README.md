


Setup virtual env:

```sh
pipevn --python 3.7
pipenv install python-dotenv psycopg2-binary
pipenv shell
```

Setup env vars in a ".env" file (using creds form ElephantSQL):

```sh
DB_NAME="__________"
DB_USER="__________"
DB_PASSWORD="__________"
DB_HOST="__________"
```

Run:

```sh
python app/pg_quries.py
```
