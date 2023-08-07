# SQL Alchemy challenge: climate analysis

## Overview
This project looked at the rain and temperature data in Hawaii focusing the latest one-year data. Original data consisted of data from 2010-01-01 to 2017-08-23.

### Visualization
| Rain | Temperature |
|---------|---------|
| ![12 month precipitation](/images/12monthPrcp.png) | ![12 month temperature](/images/12monthTemp.png)

### API
To run the API, clone the repo and run [app.py](app.py).

Access the server, which should look something like http://127.0.0.1:5000.

Routes:
- /api/v1.0/precipitation

- /api/v1.0/stations

- /api/v1.0/tobs

- /api/v1.0/<StartDate>

- /api/v1.0/[StartDate]/[EndDate]


* input date format:YYYYMMDD
** date range: 2010/01/01 - 2017/08/23