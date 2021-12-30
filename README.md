# Temperature Stick Scraping

## A simple web scraper using selenium for [Temperature Stick](https://tempstick.com)

Currently only gets recent temperature and last read time.

Copy `secrets-demo.json` to `secrets.json` and fill in to get it to run.

## Special Considerations

`requirements-freeze.txt` is automatically generated using `pip freeze > requirements-freeze.txt`, while `requirements.txt` is hand-crafted to avoid including packages that aren't actually required. Got idea from [`$ pip freeze > requirements.txt` considered harmful](https://medium.com/@tomagee/pip-freeze-requirements-txt-considered-harmful-f0bce66cf895).