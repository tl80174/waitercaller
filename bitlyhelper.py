import urllib2
import json
import requests

TOKEN= 'd9d940b04a30261b823a256257b8461b59b73d59'
ROOT_URL = "https://api-ssl.bitly.com"
SHORTEN = "/v3/shorten?access_token={}&longUrl={}"

class BitlyHelper:

    def shorten_url(self, longurl, proxies="NA"):
        try:
            url = ROOT_URL + SHORTEN.format(TOKEN, longurl)
            if proxies == "NA":
                response = requests.get (url)
            else:
                response = requests.get (url, proxies=proxies)
            
            jr = json.loads(response.text)
            return jr['data']['url']
        except Exception as e:
            print e
