#!/usr/bin/env python3

import requests

import json
import yaml

response = requests.get('https://api.spotify.com/v1/search?type=artist&q=snoop')

print(yaml.dumps(response.json()))

