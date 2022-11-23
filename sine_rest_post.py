import requests
import time
from math import sin, radians
import datetime

def main():
    api_url = "http://localhost:3001/sinewave"
    counter = 0
    while True:
        value = sin(radians(counter))
        counter += 1
        try:
            date_str = datetime.datetime.now()
            data =  {"time": str(date_str), "value": value}
            response = requests.post(api_url, json=data)
            response_text = "None"
            print("response: {}".format(response.status_code))
            time.sleep(1)
        except:
            print("error")


if __name__ == '__main__':
    main()
