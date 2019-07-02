# flask_mail_example

This is a simple Flask app to show working config of Flask-Mail for smtp.gmail.com.

## Easy Setup

Go along the provided steps. Initial config done on `Ubuntu 18.04`

1. create a virtualenv

```
python3.6 -m venv .venv
```

2. start virtualenviroment

```
source .venv/bin/activate
```

3. install requirements

```
pip install -r app/requirements.txt
```

4. fill enviromental variables `.env` file according to pattern in `_env` file

5. export enviromental variables into venv

```
export $(cat .env)
```
