
<div align="center">
<img src="review_file.png" alt="drawing" width="600"/>
<a href="https://richionline-portfolio.nw.r.appspot.com"><img src="https://falken-home.herokuapp.com/static/home_project/img/falken_logo.png" width=50 alt="Personal Portfolio web"></a>


![Version](https://img.shields.io/badge/version-1.0.0-blue)
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/rich/10.11.0)](https://www.python.org) 
![GitHub Top languaje](https://img.shields.io/github/languages/top/falken20/review_file) ![GitHub language count](https://img.shields.io/github/languages/count/falken20/review_file) ![Test coverage](https://img.shields.io/badge/test%20coverage-0%25-green)

[![Richi web](https://img.shields.io/badge/web-richionline-blue)](https://richionline-portfolio.nw.r.appspot.com) 
[![Twitter](https://img.shields.io/twitter/follow/richionline?style=social)](https://twitter.com/richionline)
</div>

# review_file
Script to find files in a directory tree and it has to fulfill that it has a determinate extension. The extension set is in a config file. You can configure two environment variables with the path (**PATH_DIR**) and extensions (**EXTENSIONS**) to search. If the variables doesn't exist, the script ask the user for the values.

---
##### Setup

```bash
pip install -r requirements.txt
```

##### Running the app

```bash
python ./src/search_extensions.py
```

##### Setup tests

```bash
pip install -r requirements-tests.txt
```

##### Running the tests with pytest and coverage

```bash
./scripts/coverage.sh
```
or
```bash
coverage run -m pytest -v && coverage html --omit=*/venv/*,*/test/*
```
