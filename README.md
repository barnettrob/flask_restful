# RESTful API creation using Flask.
### Based off of the below tutorial but with changes to use MySQL
### https://codeburst.io/this-is-how-easy-it-is-to-create-a-rest-api-8a25122ab1f3
### For MySQL changes, see https://codehandbook.org/python-web-application-flask-mysql/

Instructions:
1. Install Flask
```
pip install flask-restful
```

2. Install Flask-MySQL connector
```
pip install flask-mysql
```

3. Run script
```
python restful_mysql.py
```

4. Use a program like Postman to perform GET, POST, PUT, and DELETE operations.
#### GET
http://127.0.0.1:5000/user/<NAME>
http://127.0.0.1:5000/users/list

#### POST, PUT
http://127.0.0.1:5000/user/<NAME>
key: age
key: occupation

#### Delete
http://127.0.0.1:5000/user/<NAME>
   
