# Silica
[![Build Status](https://travis-ci.com/leonardt/silica.svg?token=BftLM4kSr1QfgPspi6aF&branch=master)](https://travis-ci.com/leonardt/silica)
[![codecov](https://codecov.io/gh/leonardt/silica/branch/master/graph/badge.svg)](https://codecov.io/gh/leonardt/silica)
[![License](https://img.shields.io/badge/License-BSD%202--Clause-orange.svg)](https://opensource.org/licenses/BSD-2-Clause)

A language embedded in Python for building Finite State Machines in hardware.

Requires Python 3.5+

# Development Setup
Ubuntu
```shell
sudo apt install python3 verilator
```
MacOS/Homebrew
```shell
brew install python3 verilator
```

[virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/index.html)
is useful tool for managing project specific Python environments.
```shell
pip install virtualenvwrapper
mkvirtualenv --python=python3 silica
```
Now you can use `workon silica` to activate the environment and `deactivate` to deactivate.

Install Python dependencies
```shell
pip install -r dev-requirements.txt
```
Install Silica as a local Python package
```shell
pip install -e .
```

Run the Test Suite
```shell
py.test --cov=silica --cov-report term-missing test
```
