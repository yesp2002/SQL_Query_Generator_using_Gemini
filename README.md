# SQL Query Generator using Google Gemini

An AI tool which generates and runs SQL queries on a database when given english input of what you want from the database.

## Setup Instructions
### 1) First, create a python virtual environment

i) Open terminal and go to your desired location for project
ii) Create a virtual environment 
```
>>> python -m venv <env_name>
```
iii) activate your virtual environment
```
>>> cd <env_name>
>>> cd Scripts
>>> activate
>>> cd ..
```
iv) Your virtual environment is activated, and you are in your virtual environment directory

### 2) Get project files and install dependencies in the environment
i) Download the project files and paste it in your folder, or open terminal and run the following
```
>>> git clone yesp2002/SQL_Query_Generator_using_Gemini.git
```
ii) Then, install the dependencies required by running the following command
```
>>> pip install -r requirements.txt
```
iii) All the python packages required will be installed for running our application

### 3) Set your Google Gemini API Key
Google Gemini API is free to use and you can access the following website to create your API key
https://aistudio.google.com/app/apikey

Once, you get your API key, create a .env file in your directory and paste the following in the file
```
GOOGLE_API_KEY = "<your-api-key>"
```

### 4) Run the Application

i) All the setup work is done, and you can run the app by running the following in terminal
```
streamlit run app.py
```

ii) This will open the application in localhost:8501 in browser, where the application is running.
iii) Give your english prompts for querying, and the app will give you SQL queries along with the output.

![image](https://github.com/yesp2002/SQL_Query_Generator_using_Gemini/assets/81530631/1f438ef9-834d-4e1e-99fc-9938c4c4aa52)

> Enjoy the application !!!



