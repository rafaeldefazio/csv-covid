import csv
import pymongo
import datetime

myclient = pymongo.MongoClient("mongodb://")
mydb = myclient["database"]
mycol = mydb["collection"]

cidade = "Catanduva"


with open('dados.csv') as f:
    reader = csv.DictReader(f, delimiter=';')
    data = list(reader)
   

for index, d in enumerate(data):


	if index == len(data)-1:
		d['lastUpdate'] = True
	else:
		d['lastUpdate'] = False

	d['city'] = cidade

	d['isoDate'] = d['date']
	d['date'] = datetime.datetime.strptime(d['date'], "%Y-%m-%d")

	for k, v in d.items():
		if k not in ('city', 'isoDate', 'date', 'lastUpdate'):
			d[k] = int(v)

	mycol.insert(d)
