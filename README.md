# Project name
News

# General info
API for news management

# Routes to implement
| METHOD   | ROUTE                                   | FUNCTIONALITY           |
|----------|-----------------------------------------|-------------------------|
| *POST*   | ```/api/v1/jwt/signup```                | register new user       |
| *POST*   | ```/api/v1/jwt/login```                 | login user              |
| *GET*    | ```/api/v1/news/```                     | details of all news     |
| *POST*   | ```/api/v1/news/```                     | create a news           |
| *GET*    | ```/api/v1/news/{pk}```                 | details of news         |
| *PUT*    | ```/api/v1/news/{pk}```                 | update news             |
| *DELETE* | ```/api/v1/news/{pk}```                 | delete news             |
| *GET*    | ```/api/v1/news_by_user/{user_id}```    | get news by user        |
| *GET*    | ```/api/v1/news_by_category/{cat_id}``` | get news by category    |
| *GET*    | ```/api/v1/category/```                 | details of all category |
| *POST*   | ```/api/v1/category/```                 | create a category       |
| *GET*    | ```/api/v1/category/{pk}```             | details of category     |
| *PUT*    | ```/api/v1/category/{pk}```             | update category         |
| *DELETE* | ```/api/v1/category/{pk}```             | delete category         |

# Technologies
* Python 3
* Django
* Django REST Framework
* PostgreSQL
* JWT
* UnitTest

# Setup

Clone the project Repository
```
git clone https://github.com/SergiiPachkovskyi/News
```

Enter the project folder and create a virtual environment
``` 
$ cd https://github.com/SergiiPachkovskyi/News 

$ python -m venv venv 

```

Activate the virtual environment
``` 
$ source env/bin/activate #On linux Or Unix

$ source env/Scripts/activate #On Windows  
```

Install all requirements

```
$ pip install -r requirements.txt
```

Run the project in development 
``` 
$ cd proj_news
$ python manage.py runserver
```

# Status
Project is: in progress
