# Import the dependencies.
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

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


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    return '''
        <h2>Path routes:</h2>
        <li>/api/v1.0/precipitation</li>"
        <li>/api/v1.0/stations</li>"
        <li>/api/v1.0/tobs</li>"
        <li>/api/v1.0/start</li>"
        <li>/api/v1.0/start/end</li>"
    '''


#Convert the query results from your precipitation analysis
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    prcp_results = session.query(Measurement.prcp, Measurement.date).\
        filter(Measurement.date >= "2016-08-23").all()

    session.close() 

    prcp_values = []
    for prcp, date in prcp_results:
        prcp_dict = {}
        prcp_dict["prcp"] = prcp
        prcp_dict["date"] = date
        prcp_values.append(prcp_dict)
    return jsonify(prcp_values)    









