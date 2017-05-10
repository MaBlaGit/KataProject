================
Weather App v1.0
================

Description:
============

Weather App - https://simplebottleapp.herokuapp.com/ is a simple weather service, where user can check weather conditions of desired city. Application is written in Python and use Bottle Framework (WSGI micro web-service) for creating web applications (more about Bottle - https://bottlepy.org/docs/dev/)

Development process is supported by **Continuous Integration** (testing application on Travis CI platform) / **Continuous Delivery** (application deployment on Docker and Heroku services). Condition monitoring is provided by StatusCake.

 - **Travis CI** - https://travis-ci.org/MaBlaGit/KataProject
 - **Docker** - https://hub.docker.com/r/dockermariusz/kata-project-new/
 - **Heroku** - https://simplebottleapp.herokuapp.com/

Application is tested by several unit tests, (unittest framework), and GUI tests, (Selenium Framework). More unit/GUI tests will be added soon.

Results of Selenium tests are generated as html document (HTMLTestRunner package was used). Screencast recording of Selenium tests is supported by Castro screencast package.

More about used packages:

 - **HTMLTestRunner** - http://tungwaiyip.info/software/HTMLTestRunner.html
 - **Castro screencast** - https://github.com/hugs/castro
 
Weather App use OpenWeatherMap api https://openweathermap.org/api and google maps api: https://developers.google.com/maps/documentation/javascript/get-api-key

You have to generate your own api keys and paste it into code / shell **docker run** command in order to start application from the script or Docker container.


**Run application from Docker image:**

To run app as docker container (Docker have to be installed on the local machine):
::
 - Pull docker image from https://hub.docker.com/r/dockermariusz/kata-project-new/

 - $ docker run -e GOOGLE_API_KEY=your_google_api_key -e OWM_API_KEY=your_owm_api_key --name 
     weather-app -p 8000:8080 dockermariusz/kata-project-new:latest

 - Type in browser: http://localhost:8080
          

**Preparing environment to run code - steps tested on Linux CentOS 7**

1. Clone/Download project from GitHub: https://github.com/MaBlaGit/KataProject
2. Install pip, virtualenv and virtualenvwrapper:
::
    - # yum install  python-pip
    - $ pip install virtualenv
    - $ pip install virtualenvwrapper
3. Run virtualenvwrapper and create hermetic virtualenv for the project:
::
    - $ source /usr/bin/virtualenvwrapper.sh
    - $ mkvirtualenv <name-of-your-virtualenv>
    - $ workon <name-of-your-virtualenv> 	
	
4. Go to KataProject folder and add project to the virtualenv PYTHONPATH:
::
    - $ add2virtualenv . (resolves problems with module imports)
5. Install required modules:
::
    - $ make deps
    - # yum install tkinter (required for recording screencast)
6. Install **x11vnc Server** (required for recording screencast)
::
	- # yum install x11vnc
	
7. Install Chrome browser

8. Download chromedriver
    - https://sites.google.com/a/chromium.org/chromedriver/

9. In project folder (KataProject) go to **selenium_tests/selenium_test_weather.py**
::
    - Add chromedriver to executable_path:
    - cls.driver = webdriver.Chrome(executable_path='path-to-chromedriver') or add chromedriver path to Environment Variables.
    - set name of the host cls.castro_recorder = Castro(host=name_of_your_host, port=...)

**RUNNING APPLICATION**

1. To run and check how application works, in KataProject folder:
::
    - $ gunicron simple_bottle_app:app
    - go to browser, type: http://127.0.0.1:8000

2. To run unittest, in KataProject folder
::
	- $ make test

3. To run Selenium tests:
   Test app on localhost:

**KataProject/weather_api_script.py** paste **openweathermap** api key and **google api key**:
::
   # api key for openweathermap
   # owm_api_key = os.environ.get('OWM_API_KEY') hash this line
   owm = pyowm.OWM(owm_api_key) paste it here!!!   
   # api key google maps    
   # google_api_key = os.environ.get('GOOGLE_API_KEY') / hash this line
   google_map_api_key = google_api_key paste it here!!!
   in the KataProject folder open shell(virtualenv must be activated)
   $ make run
   open another shell to run **x11vnc server**
   $ x11vnc -display :0
   Check in logs if **display** and **PORT** are the same as we defined in **selenium_tests/selenium_test_weather.py** (see step 8 of preparing environment). If not,  **stop server**, **change code** and run it again!
   open another terminal, go to KataProject/selenium_tests, activate virtualenv:
   $ python smoke_test.py

After test check html_raport folder (**html_test_raport**) and **test_screencast** folder (screencast video from the test).



