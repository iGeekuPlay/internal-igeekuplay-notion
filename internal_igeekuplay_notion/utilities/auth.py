from flask_httpauth import HTTPBasicAuth
import os 

# import credentials from env (suggested)
API_UNAME = os.getenv("API_UNAME")
API_PASS = os.getenv("API_PASS")

USER_DATA = {API_UNAME: API_PASS}

auth = HTTPBasicAuth()

# verify API authentication
@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return USER_DATA.get(username) == password
