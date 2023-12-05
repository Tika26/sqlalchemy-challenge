# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
import datetime as dt

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route('/')
def home():
    return '''
    <h2>Path routes:</h2>
    <li>/api/v1.0/precipitation</li>
    <li>/api/v1.0/stations</li>
    <li>/api/v1.0/tobs</li>
    <li>/api/v1.0/[start]</li>
    <li>/api/v1.0/[start]/[end]</li>
    '''

@app.route('/api/v1.0/precipitation')
def precipitation():  
    session = Session(engine)

    return { d:p for d,p in session.query(Measurement.date, Measurement.prcp).filter(Measurement.date>='2016-08-23').all()}

@app.route('/api/v1.0/stations')
def station():
    session = Session(engine)
    
    return { id:loc for id,loc in session.query(Station.station, Station.name).all()}

@app.route('/api/v1.0/tobs')
def tobs():
    session = Session(engine)

    results = session.query(Measurement.date, Measurement.tobs).\
         filter(Measurement.date >= '2016-08-23').\
         filter(Measurement.station=='USC00519281').\
         order_by(Measurement.date).all()
        
    return {d:t for d,t in results}


@app.route('/api/v1.0/<start>')
@app.route('/api/v1.0/<start>/<end>')
def startEnd_dates(start, end='2017-08-23'):
    session = Session(engine)

    sel = [func.min(Measurement.tobs),
           func.avg(Measurement.tobs),
           func.max(Measurement.tobs)
    ]
    
    date_range = session.query(*sel).filter((Measurement.date >= start)&(Measurement.date <= end)).all()

    result = [
        {"TMIN": date_range[0][0]},
        {"TAVG": date_range[0][1]},
        {"TMAX": date_range[0][2]}
    ]
    
    if (start <= '2017-08-23') and (end >='2010-01-01') :
        return jsonify(result)
    else:
        return jsonify("Error: start and end date not within time horzion, please enter a start and end date between 2010-01-01 : 2017-08-23")
    
if __name__ == '__main__':
    app.run(debug=True)





