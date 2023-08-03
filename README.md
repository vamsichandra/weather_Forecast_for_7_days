# weather_Forecast_for_7_days
Weather forecast for the next 7 days for a location, it asks for user's location(done using navigation.geolocation) or the user can enter a city name then the javascript fuction
fetches the latitude and longitude of the place using google maps API and sends it to backend; in the same way the if user gives permission to the location of the latitude and longitude
and longitudes are sent to backend;
In the backend, the opi weather API is called with the latitude and longitude and converted JSON to string using json.dumps() and filters the necessary information and
sends the data in JSON format;
In the front end, the information is presented using Bootstrap the current and the next 7 days.
