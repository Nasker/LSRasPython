import http.client, urllib

conn = http.client.HTTPSConnection("api.pushover.net:443")
conn.request("POST", "/1/messages.json",
  urllib.parse.urlencode({
    "token": "awq42rfkakrn9t9v3rak1jc1wg9po8",
    "user": "unzod5y5ynqjrdywft5i1x9bxqtibf",
    "message": "que pasa nen!",
  }), { "Content-type": "application/x-www-form-urlencoded" })
conn.getresponse()