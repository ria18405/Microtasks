"""
Then, write a script to read the enriched index and import the attributes uuid, project, project_1, origin, grimoirelab_creation_date, body and subject_analyzed to a CSV file. 

Import the obtained file to an excel sheet (in a manual or automatic way).
"""
from elasticsearch import Elasticsearch
import csv
import pandas as pd

"""es = Elasticsearch()

file=open("output.csv","w")
writer=csv.writer(file,delimiter=',')
writer.writerow(["uuid","project","project_1","origin","grimoirelab_creation_date","body"])

res = es.search(index="groupsio_enriched", body={"query": {"match_all": {}}})
for i in range(10):
	uuid=(res['hits']['hits'][i]['_source']['uuid'])
	origin=(res['hits']['hits'][i]['_source']['origin'])
	grimoirelab_creation_date=(res['hits']['hits'][i]['_source']['grimoire_creation_date'])
	body=(res['hits']['hits'][i]['_source']['body_extract'])
	subject_analyzed=(res['hits']['hits'][i]['_source']['Subject_analyzed'])
	project=(res['hits']['hits'][i]['_source']['project'])
	project_1=(res['hits']['hits'][i]['_source']['project_1'])

	writer.writerow([uuid,project,project_1,origin,grimoirelab_creation_date,body])"""

read_file = pd.read_csv(r'/home/ria/Desktop/Microtasks/Microtask8/output.csv',delimiter=',',delim_whitespace=True,header=None,encoding='utf-8')
print(read_file)
read_file.to_excel (r'/home/ria/Desktop/Microtasks/Microtask8/output.xlsx',na_rep=",",header=None,index=None,merge_cells=True,engine='openpyxl' )
"""Ref:
https://elasticsearch-py.readthedocs.io/en/master/
"""