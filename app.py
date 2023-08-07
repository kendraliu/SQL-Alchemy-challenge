import numpy as np
import os
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect, MetaData, Table, select
from flask import Flask, jsonify
from flask_cors import CORS
from datetime import timedelta, datetime as dt

cwd = os.getcwd()
print(cwd)

engine = create_engine("sqlite:///SurfsUp/Resources/hawaii.sqlite")

Base = automap_base()
Base.prepare(autoload_with=engine)
measurement = Base.classes.measurement
station = Base.classes.station

app = Flask(__name__)

@app.route("/")
def home():
    return(
        f"Available Routes:<br/>------------------------------------------<br/>"
        f"/api/v1.0/precipitation<br/><br/>"
        f"/api/v1.0/stations<br/><br/>"
        f"/api/v1.0/tobs<br/><br/>"
        f"/api/v1.0/[StartDate]*<br/><br/>"
        f"/api/v1.0/[StartDate]*/[EndDate]*<br/><br/><br/>* input date format:YYYYMMDD<br/>"
        f"** date range: 2010/01/01 - 2017/08/23"
    )

@app.route("/api/v1.0/precipitation")
def precipitaion():
    session = Session(engine)
    latestDay = session.query(func.max(measurement.date)).scalar()
    oneYearAgo = dt.strptime(latestDay, "%Y-%m-%d") - timedelta(days=365)
    prcpData = session.query(measurement.date, measurement.prcp).filter(measurement.date>=oneYearAgo, measurement.date<=latestDay).all()
    session.close()
    api=[]
    for row in prcpData:
        dict={}
        dict["Date"] = row.date
        dict["Precipitation"] = row.prcp
        api.append(dict)
    return(api)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    stations = session.query(station.station, station.name).all()
    session.close()
    api=[]
    for row in stations:
        dict={}
        dict["Station"] = row.station
        dict["Name"] = row.name
        api.append(dict)
    return(api)

@app.route("/api/v1.0/tobs")
def temp():
    session = Session(engine)
    latestDay = session.query(func.max(measurement.date)).scalar()
    oneYearAgo = dt.strptime(latestDay, "%Y-%m-%d") - timedelta(days=365)
    tempData = session.query(measurement.date, measurement.tobs).filter(measurement.station == "USC00519281").filter(measurement.date>=oneYearAgo, measurement.date<=latestDay).all()
    session.close()
    api=[]
    for row in tempData:
        dict={}
        dict["Date"] = row.date
        dict["Temperature"] = row.tobs
        api.append(dict)
    return(api)

@app.route("/api/v1.0/<start>/<end>")
def timeRange(start, end):
    startDate = dt.strptime(start, "%Y%m%d")
    endDate = dt.strptime(end, "%Y%m%d")

    session = Session(engine)
    tempData = session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)).filter(measurement.station == "USC00519281").filter(measurement.date>=startDate, measurement.date<=endDate).all()
    session.close()
    api=[]
    for row in tempData:
        dict={}
        dict["Lowest Temperature"] = row[0]
        dict["Highes Temperature"] = row[1]
        dict["Avg Temperature"] = row[2]
        api.append(dict)
    return(api)

@app.route("/api/v1.0/<start>")
def timeAfter(start):
    startDate = dt.strptime(start, "%Y%m%d")

    session = Session(engine)
    latestDay = session.query(func.max(measurement.date)).scalar()
    tempData = session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)).filter(measurement.station == "USC00519281").filter(measurement.date>=startDate, measurement.date<=latestDay).all()
    session.close()
    api=[]
    for row in tempData:
        dict={}
        dict["Lowest Temperature"] = row[0]
        dict["Highes Temperature"] = row[1]
        dict["Avg Temperature"] = row[2]
        api.append(dict)
    return(api)

if __name__ == '__main__':
    app.run(debug=True)

