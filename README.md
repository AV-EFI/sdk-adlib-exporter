# av-efi-generator

script for generating av-efi compliant records from adlib records provided by hard-coded pointer files

## Installation

```console
$ poetry --version                     # check for poetry existence
Poetry (version 1.8.2)                
$ poetry install                       # install dependencies
```

## Running the project

Ensure that you have a network connection to adlib.

```console
$ export SDK_ADLIB_URL=http://...      # set required env variable
$ echo $SDK_ADLIB_URL                  # check env variable
http://...
$ poetry run python main.py            # run script
```
