# EduAPI

- This application was created to add payments notifications for customers data.

### Local Install instructions:

Before running please follow this steps:

- 1- Create new folder in your selected path(Desktop, Downloads, Documents, etc..)
- 2- Clone this repository and move the unzipped folder to the new folder created previously
- 3- Open your terminal and move it to the path folder created on step 1
- 4- Create a virtual environment using the next command (MacOS):
```
                            python3 -m venv <yourvenvname>
``` 

## Running local EduAPI  

- 1- Open your cloned repository (located in your new folder created in previous section) using
     your code editor preferred (PyCharm, VisualStudioCode, ...)
- 2- Open your code editor's terminal and use "cd .." command to move one folder back into directory path
- 3- Activate your virtual environment using the next command(MacOS):
```
                            source <yourvenvname>/bin/activate
```
- 4- Once you have activated your virtual environment, return to your cloned repository (this should be one up folder) using "cd <reponame>" command 
- 5- Install all requirements located in requirements.txt file using the next command:
```
                            pip install -r requirements.txt
```

- 6- Done!!! You can run your local server using the nex command (MacOS)
```
                            python3 manage.py runserver
```
- 8- Open your browser at **http://127.0.0.1:8000**

- 9- IMPORTANT: Once your localhost is running, open a new terminal and run tests to check our API rest operation.
                Our local server needs to be running while we run our tests.
```
                            python3 manage.py test
```

# API endpoints

- Once you are logged as Professor(Admin) in the system, you will have access to our APIrest endpoints:
    - Modules endpoints:
        - **http://127.0.0.1:8000/api/v1/customerdata/** 
        - **http://127.0.0.1:8000/payments/paypal/**
        - **http://127.0.0.1:8000/admin/**
        

## Use with Docker 

- This instructions assume that you have already install docker and docker compose. If don't, please do it before continue.

-   1.- Download this repository in your local machine.
    
-   2.- Open it with your code editor (PyCharm, VisualStudioCode, etc...).
    
-   3.- On your terminal execute the  follow command (This command build containers, install requirements and make migrations):
```
                            docker-compose run web python manage.py migrate
```  
-   4.-To run docker compose execute on your terminal the follow command:
```
                            docker-compose up
```  

-   5.-Done!!, now you are ready to use it. Now you can access to  http://0.0.0.0:8000/ for our app. Please read the next section to use it.



## EduApi Circle CI [![NeOneSoft](https://img.shields.io/circleci/build/gh/NeOneSoft/EduApi?token=840c51b266b087c8c9545d3aff59f00248d94e59)](https://circleci.com/gh/NeOneSoft/EduApi)
-  CircleCI keeps running your unit tests automatically for every change that you make on your repository.
