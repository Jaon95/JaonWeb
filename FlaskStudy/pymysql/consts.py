HOSTNAME = 'localhost'
DATABASE = 'db'
USERNAME = 'web'
PASSWORD = 'web'
DB_URI = 'mysql+pymysql://{}:{}@{}/{}?charset=utf8'.format(
    USERNAME, PASSWORD, HOSTNAME, DATABASE
)