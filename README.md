# pandemonium
**Find inspiration for your next meme creation!**

## Imgflip API
This project uses the [Imgflip API](https://imgflip.com/api) to get meme templates. The raw [API endpoint output](https://api.imgflip.com/get_memes) can be consulted to modity the parsing script in the event of schema updates. 

## Contributing
Contributions welcome!  
Feel free to raise an issue to report a bug and suggest changes, and work on corresponding PRs. 
Please read the [Contributing guidelines](https://github.com/vijay-jaisankar/pandemonium/blob/main/CONTRIBUTING.md) before raising an issue/PR to main consistency with the community guidelines.

---

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
