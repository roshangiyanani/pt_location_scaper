# Physical Therapy Location Scraper

A tool for scraping the website of physical therapy companies to get their locations.

## Documentation

### Supported Physical Therapy Companies

* Athletica
* ATI
* US Physical Therapy (USPh)
* Select Physical Therapy
* Novacare (Part of Select)
* Pivot Physical Therapy
* Professional PT
* Upstream Rehabilitation (URPT)
* CORA Health Services
* Fyzical

### (Hopefully soon to be) supported physical therapy websites


### Output format

The code outputs the data into individual csv files, which can then be opened in excel or your favorite text editor.

### To run

To run the program:

~~~~bash
pipenv run python ptls
~~~~

Pass in the `-h` or `--help` flag to get cli options.

## Development

### Installation

Installation requires pipenv, which you can install by running:

~~~~bash
pip install pipenv
~~~~

To install dependencies:

~~~~bash
# from project root
pipenv sync
pipenv run pip install -e ./
~~~~

### Testing

To test the program:

~~~~bash
# from project root
pipenv run python download.py # downloads test files
pipenv run python -m unittest
~~~~