from app import app
from flaskext.mysql import MySQL

'''
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '@@991674124'
app.config['MYSQL_DATABASE_DB'] = 'cc1'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

Flask
Gunicorn
flask-cors
flask-mysql
'''

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'u731954907_python_flask'
app.config['MYSQL_DATABASE_PASSWORD'] = '__Python_flask01'
app.config['MYSQL_DATABASE_DB'] = 'u731954907_python_flask'
app.config['MYSQL_DATABASE_HOST'] = '212.1.211.201'
mysql.init_app(app)


