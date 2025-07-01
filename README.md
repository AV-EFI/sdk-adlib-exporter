# collections2efi

## Installation

```console
$ poetry --version                     # check for poetry existence
Poetry (version 1.8.2)                
$ poetry install                       # install dependencies
```

## Running the project

Ensure that you have a network connection to Axiell Collections.

```console
$ export SDK_AXIELL_COLLECTIONS_URL=http://...      # set required env variable
$ echo $SDK_AXIELL_COLLECTIONS_URL                  # check env variable
http://...
$ poetry run python main.py            # run script
```
