# pandemonium
Find inspiration for your next meme creation!


## Installing the dependencies
Make sure [Python](https://www.python.org/downloads/) `3.x` is installed on your system. This can be validated by running the following command: `python --version`.  

It is recommended to use a virtual enviroment to minimise the risk of dependency clashes with other projects. For this, first install `virtualenv` through any of [these methods](https://virtualenv.pypa.io/en/stable/installation.html). Then, run the following commands to activate the virtual environment.  

```
virtualenv venv
source venv/bin/activate
```

Then, install the dependencies by running
```
pip install -r REQUIREMENTS.txt
```

## Running the application
```python app.py``` will run the application locally, it can be accessed by navigating to `http://127.0.0.1:5000`.