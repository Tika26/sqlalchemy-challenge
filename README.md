# sqlalchemy-challenge
# Precipitation Analysis:
   # Find the most recent date in the dataset.
   # Get the previous 12 months of precipitation data by querying the previous 12 months of data.
   # Select only the "date" and "prcp" values.
   # Load the query results into a Pandas DataFrame. Explicitly set the column names.
   # Sort the DataFrame values by "date".
   # Plot the results by using the DataFrame plot method.
   # Use Pandas to print the summary statistics for the precipitation data.
# Station Analysis:
   # Query to calculate the total number of stations in the dataset.
   # query to find the most-active stations.
       # List the stations and observation counts in descending order.
       # Station id that has the greatest number of observations.
   # Query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.
   # query to get the previous 12 months of temperature observation (TOBS) data.
       # Filter by the station that has the greatest number of observations.
       # Query the previous 12 months of TOBS data for that station.
       # Plot the results as a histogram with bins=12.


# Climate App:
   # Started at the homepage.
   # List all the available routes.
      # /api/v1.0/precipitation
         # Convert the query results from your precipitation analysis to a dictionary using date as the key and prcp as the value.
         # Return the JSON representation of your dictionary.
      # /api/v1.0/stations
         # Return a JSON list of stations from the dataset.
      # /api/v1.0/tobs
         # Query the dates and temperature observations of the most-active station for the previous year of data.
         # Return a JSON list of temperature observations for the previous year.
      # /api/v1.0/<start> and /api/v1.0/<start>/<end>
         # Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
         # calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
         # calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.
