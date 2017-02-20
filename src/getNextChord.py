import json
import urllib2

# with open('search.json', 'w') as outfile:
#     json.dump(search_results["data"]["children"][0], outfile, sort_keys = True, indent = 4, separators=(',', ': '))
with open('credentials.json') as data_file:
   data = json.load(data_file)

req = urllib2.Request("https://api.hooktheory.com/v1/users/auth", json.dumps(data), headers={'Content-type': 'application/json', 'Accept': 'application/json'})
response = urllib2.urlopen(req)
the_page = response.read()
print the_page
