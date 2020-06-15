import requests
import time
from util import GetDBConnection

statsDB = GetDBConnection.getDBConnection()

while (True):
    time.sleep(60);
    response = requests.get("http://web:5000/sortBazaar")
    print("UPDATED")