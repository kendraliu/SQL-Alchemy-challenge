# SQL Alchemy challenge: climate analysis

This project looked at the rain and temperature data in Hawaii focusing the latest one-year data. Original data consisted of data from 2010-01-01 to 2017-08-23.

## Visualization
| Rain | Temperature |
|---------|---------|
| ![12 month precipitation](/images/12monthPrcp.png) | ![12 month temperature](/images/12monthTemp.png)

## API
To run the API, clone the repo and run [app.py](app.py).

Access the server, which should look something like `http://127.0.0.1:5000`.

### Availble Routes:
- `/api/v1.0/precipitation`: daily precipitation in Hawaii from 2016/08/24 - 2017/08/23

- `/api/v1.0/tobs`: temperature frequency in Hawaii from 2016/08/24 - 2017/08/23

* for temperature stats for a certain period of time, use:

    * `/api/v1.0/{StartDate}`: from the specified date to the latest date available

    * `/api/v1.0/{StartDate}/{EndDate}`: within the specified period

        * input date format:YYYYMMDD
        * available date range: 2010/01/01 - 2017/08/23

- `/api/v1.0/stations`: all the stations that contribut to the data