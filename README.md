# Google Map Street View Postcards

## Requirements

Python 3

If there is any blank column in the origin data, that row will be flagged as Blank Row.

## Installation

```bash
pip install requests
```

## Usage

Please take a look at [src/constants.py](src/constants.py).

Please define your key at src/API_KEY.py, like following


```
GEOCODE_API_KEY = '*******************'

STREET_IAMGE_KEY = '*******************'
```


The default location of testing input and output CSV files are as follows.

```
"assets/csv/src.csv"

  and

"assets/csv/des.csv"
```

Able to change [assets/default_image.png](assets/default_image.png).

Currently using the same google account as Github.
If there is an urgent question, please contact me directly for a fast answer.

## Run

```bash
python src/main.py
```
