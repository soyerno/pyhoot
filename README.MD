# Install
    
### Install python 3.12.2
https://www.python.org/downloads/

```
    cd flask
    py -3 -m venv .venv
    .venv\Scripts\activate
    pip install -r requirements.txt
    flask --app project --debug run
```

# Installing dependencies

after install python dependencies run to save all in requirements file.
```
pip freeze > requirements.txt
```


# Run instructions for development
### Open a terminal and run

```
    cd flask
    env\Scripts\activate
    flask --app project --debug run
```


# Run for production instructions
```
    .venv\Scripts\activate
     flask --app project run
```