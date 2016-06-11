# django_geojson
django_geojson  This is a django application which shows you the use of GeoJson data with django from scratch without the use of any third party geojson-libraries. This app has API endpoints for users and API endpoints for the regions/ polygons created by users. User API endpoints let's you create a user(Http-POST-Request), retrieve user details(Http-GET-Request), update/modify user details(Http-PUT-Request), delete user data along with the geojson regions/polygons which they created. Region/Polygon API endpoints let's you create a GeoJson polygon region(POST request), retrieve those regions/polygons which contains the specified/provided Coordinates/LatLng, update the region/polygon data, delete the regions/polygons.


-----------------------------------------------------HOW TO RUN--------------------------------------------------------------

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

9. Start Django project by firing up the Django Server
		(myvenv) $ ./manage.py runserver 0.0.0.0:8000

		--Now Django app is running on http://localhost:8000
		--You can also access this server from any other system on the same Network


---------------------------------------------------HOW TO USE/ API Docs--------------------------------------------------------------

1. Creating a request
		GO TO URL -- "http://localhost:8000/api/request?connId=YOUR_WISH&timeOut=YOUR_WISH"

		--timeOut is in seconds.
		--The request is running in the background. You can see it executing in the Celery Terminal
		--The request here is doing very basic job. It is only to show that it is working. You can create any desired			   task by changing the task in "tasks.py" file.
		--You can see all the active/running requests by follwing the next step.

2. Getting and checking all running requests
		GO TO URL -- "http://localhost:8000/api/active"

3. To see the Server Status
		GO TO URL -- "http://localhost:8000/api/serverStatus"

4. To kill a request
		GO TO URL -- "http://localhost:8000/api/kill/"
		
		and execute a PUT request on it with a payload/data {"connId" : "YOUR_WISH"}


		--for your own convenience I have given a second option to kill the request
		--You can also simply kill a request by running a GET call on -- http://localhost:8000/api/kill?connId=YOUR_WISH
		so that don't have to use any Third party Software/Plugin/Extension to kill a task. 
