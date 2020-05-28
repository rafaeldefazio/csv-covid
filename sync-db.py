#!/usr/bin/env python3

import csv
import pymongo
import datetime

myclient = pymongo.MongoClient("mongodb://")
mydb = myclient["covid19"]
mycol = mydb["cidades"]
cidade = "Catanduva"


with open('/home/rafaeldefazio/csv-covid/dados.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
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

                        if v:
                                d[k] = int(v)
                        else:
                                d[k] = None



        mycol.insert(d)
