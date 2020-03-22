"""
Then, write a script to read the enriched index and import the attributes uuid, project, project_1, origin, grimoirelab_creation_date, body and subject_analyzed to a CSV file. 

Import the obtained file to an excel sheet (in a manual or automatic way).
"""
from elasticsearch import Elasticsearch
import csv
import pandas as pd

es = Elasticsearch()

arr_uuid=[]
arr_origin=[]
arr_body=[]
arr_project=[]
arr_project_1=[]
arr_subject_analysed=[]
arr_grimoirelab_creation_date=[]

res = es.search(index="groupsio_enriched", body={"query": {"match_all": {}}})
for i in range(10):
	uuid=(res['hits']['hits'][i]['_source']['uuid'])
	origin=(res['hits']['hits'][i]['_source']['origin'])
	grimoirelab_creation_date=(res['hits']['hits'][i]['_source']['grimoire_creation_date'])
	body=(res['hits']['hits'][i]['_source']['body_extract'])
	subject_analyzed=(res['hits']['hits'][i]['_source']['Subject_analyzed'])
	project=(res['hits']['hits'][i]['_source']['project'])
	project_1=(res['hits']['hits'][i]['_source']['project_1'])

	arr_uuid.append(uuid)
	arr_origin.append(origin)
	arr_grimoirelab_creation_date.append(grimoirelab_creation_date)
	arr_body.append(body)
	arr_subject_analysed.append(subject_analyzed)
	arr_project.append(project)
	arr_project_1.append(project_1)


df=pd.DataFrame({'uuid':arr_uuid,'origin':arr_origin,'project':arr_project,'project_1':arr_project,'grimoirelab_creation_date':arr_grimoirelab_creation_date,'subject_analyzed':arr_subject_analysed,'body':arr_body})
print(df)
df.to_csv("output.csv")
df.to_excel("output.xlsx", index=None)



"""Ref:
https://elasticsearch-py.readthedocs.io/en/master/
"""