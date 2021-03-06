# django_geojson
A django application showing the use of GeoJson data with django from scratch without the use of any third party geojson-libraries. This app has API endpoints for users and API endpoints for the regions/ polygons created by users. User API endpoints let's you create a user(Http-POST-Request), retrieve user details(Http-GET-Request), update/modify user details(Http-PUT-Request), delete user data along with the geojson regions/polygons which they created(Http-DELETE-Request). Region/Polygon API endpoints let's you create a GeoJson polygon region(POST request), retrieve those regions/polygons which contains the specified/provided Coordinates/LatLng, update the region/polygon data, delete the regions/polygons.


## HOW TO RUN

NOTE: For Linux(ubuntu distros only)-- Tested on ElementaryOS

1. Download the zip & extract OR clone the repository.

2. Install Python version 2.7.x.

3. Install pip.

4. Install Virtual Environment( For your own benefit -- to prevent installing python packages globally )

		$ pip install virtualenv

5. Create a virtual environment( Make it somewhere near the downloaded folder for your own benefit)

		$ virtualenv myvenv

		--The above Terminal command initializes a virtual environment( Folder ) with name 'myvenv'
		--You can give any name

6. Enter virtual environment

		$ source PATH-TO-VIRTUAL-ENVIRONMENT/myvenv/bin/activate

		--Now the command shell would look like
			(myvenv) $

7. Install all the Project Dependencies inside virtual environment

		(myvenv) $ pip install -r requirements.txt

		--This file is inside the downloaded Project folder so either get inside the Downloaded project folder or
		  use "pip install -r PATH-TO-requirements.txt-Folder/requirements.txt"

8. Get inside the Extracted Folder(Where "manage.py" is located)

9. Setup a postgreSQL database and a postgreSQL user. You can follow the link:-

		https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04

10. Add Database connection parameters created above in settings.py file and then run the follwing command to migrate the      models to the database:-
 
		(myvenv) $ ./manage.py migrate

11. Start Django project by firing up the Django Server

		(myvenv) $ ./manage.py runserver 0.0.0.0:8000

		--Now Django app is running on http://localhost:8000
		--You can also access this server from any other system on the same Network


## HOW TO USE/ API Docs

NOTE: Sessions have not been implemented so APIs(wherever required) would use hardcoded login details i.e. User-email and Password for Authentication and Authorization purposes. 

**A. APIs for User/Service-Provider**

1. Creating a User/Service-Provider

		FOR LOCALHOST cURL -- curl -H "Content-Type: application/json" -X POST -d '{"name":"alex","email":"alex@xyz.com","phone":"23134355","lang":"FR","curr":"EUR","pass":"test123"}' http://localhost:8000/provider/create/


		--This creates a user/service-provider alex with email: alex@xyz.com, password: test123 and other details as specified.

2. Getting the user data by passing user email and password.

		FOR LOCALHOST cURL -- curl -X "GET" "http://localhost:8000/provider/get/?email=alex@xyz.com&pass=test123"


3. Updating user data by passing user email and password along with the data changes.

		FOR LOCALHOST cURL -- curl -H "Content-Type: application/json" -X PUT -d '{"name":"alex mercer","email":"alex@xyz.com","phone":"11111111","lang":"US","pass":"test123"}' http://localhost:8000/provider/update/


4. Deleting user data along with user created regions/ polygons by passing user email and password.

		FOR LOCALHOST cURL -- curl -X "DELETE" "http://localhost:8000/provider/delete/?email=alex@xyz.com&pass=test123"	





**B. APIs for Region/ GeoJson-Polygons**

1. Creating a Polygon for a given user by passing user email and password.

		FOR LOCALHOST cURL -- curl -X POST  -H "Content-Type: application/json" -d '  {
  		"email": "alex@xyz.com",
  		"pass": "test123",
  		"price": "100",
  		"geodata":{
  		"type": "Feature",
  		"geometry": {
           "type": "Polygon",
           "coordinates": [
             [ [100.0, 0.0], [101.0, 0.0], [101.0, 1.0],
               [100.0, 1.0], [100.0, 0.0] ]
             ]
         },
    		"properties": {
           "name": "California"
           }
           }
           }' "http://localhost:8000/region/add/"





		--This creates a region/geoJson-polygon California with the provided coordinates for user with email: alex@xyz.com, password: test123.

2. Getting all regions/polygons which contains the specified Coordinates/LatLng.

		FOR LOCALHOST cURL -- curl -X "GET" "http://localhost:8000/region/get/?lat=100.5&lng=0.5"


3. Updating a polygon for the provided user email, password and unique ID for that polygon. The unique ID can be found out    by running the get command as specified in point "2." above.

		FOR LOCALHOST cURL -- curl -X PUT  -H "Content-Type: application/json" -d '  {
  		"id":5,
  		"email": "alex@xyz.com",
  		"pass": "test123",
  		"price": "120",
  		"geodata":{
  		"type": "Feature",
  		"geometry": {
           "type": "Polygon",
           "coordinates": [
             [ [100.0, 0.0], [102.0, 0.0], [101.0, 1.0],
               [100.0, 1.0], [100.0, 0.0] ]
             ]
         },
    		"properties": {
           "name": "West California"
           }
           }
           }' "http://localhost:8000/region/update/"





4. Deleting a polygon passing user email, password and Unique ID for the polygon.

		FOR LOCALHOST cURL -- curl -X "DELETE" "http://localhost:8000/region/delete/?email=alex@xyz.com&pass=test123&id=5"	


	
