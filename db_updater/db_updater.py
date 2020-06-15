import requests
import time

while (True):
    time.sleep(60);
    response = requests.get("http://web:5000/sortBazaar")
    print("UPDATED")