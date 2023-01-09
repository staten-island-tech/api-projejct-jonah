import requests
import json
def request1(param):   
    r=requests.get("https://gateway.marvel.com/v1/public"+param+"?ts=1&apikey=b197a361786c4e16a2c6038c26a5f287&hash=c07b7613c9f07a24f7164e8edfa53104").json()
    return r

