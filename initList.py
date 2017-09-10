import urllib2
import json

baselink1 = "http://loremricksum.com/api/?paragraphs=1&quotes=1"
paragraphs = 1
quotes = 0
map = {}
for i in range (1,2500):
    link = baselink1
    result = urllib2.urlopen(link).read()
    if result not in map:
        with open('quotes.txt', 'a') as the_file:
            quote = json.loads(result)
            line = yourstring = quote["data"][0].encode('ascii', 'ignore').decode('ascii')
            the_file.write(line)
            the_file.write("\n")
    map[result] = "1"

print len(map)
