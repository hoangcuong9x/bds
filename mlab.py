import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds131296.mlab.com:31296/seconmapp

host = "ds131296.mlab.com"
port = 31296
db_name = "seconmapp"
user_name = "admin2"
password = "admin1"

def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password, email=email)