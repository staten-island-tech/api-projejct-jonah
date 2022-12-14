import requests
response=requests.get("https://gateway.marvel.com/v1/public/characters",headers={"apikey": "b197a361786c4e16a2c6038c26a5f287",
  "ts": "a timestamp",
  "hash": "4eea7e12e3483c6df37b420b6e096b3c"})
print(response.status_code)