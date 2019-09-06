# STG Python Certification Training
This is the certification given as part of the STG Training we do weekly in the **Autobots** group at **QA at the Point**.
This repo is meant to be an example and reference.

View the certification and challenges:
https://bitly.com/STGpythonwebdriver

## Setup

1. Install chromedriver

    * with brew (recommended)
        * `$ brew cask install chromedriver`
        
    * without brew
        * download chromedriver executable and put its filepath into driver factory
    
2. Install packages and dependencies

    * with pipenv (recommended)
        * `$ pipenv install`
        * This will install all required packages and dependencies in the `Pipfile`

    * without pipenv
        * `$ pip install <package-name>` for each package in `Pipfile`

## pytest Test Framework

We are using **pytest** to run our tests. For example, to run tests in challenge 1 via the CLI:

`$ pytest tests/test_ch1.py`

## PyCharm

We are doing the training with the PyCharm IDE, but you are welcome to use any editor.
