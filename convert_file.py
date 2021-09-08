import json

with open("firstnames.csv", "r") as source_file:
    data = source_file.read().split('\n')

firstnames = list({line.split(";")[0].split('(')[0] for line in data if line})
with open("firstnames.py", "w") as dest_file:
    dest_file.write("FIRSTNAMES = %s" % str(firstnames))
