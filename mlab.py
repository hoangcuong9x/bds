import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds213259.mlab.com:13259/vinhhome

host = "ds213259.mlab.com:13259"
port = 13259
db_name = "vinhhome"
user_name = "admin"
password = "admin1"

def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)