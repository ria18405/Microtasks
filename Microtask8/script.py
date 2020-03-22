from elasticsearch import Elasticsearch
import csv
import pandas as pd
def search():
	"""
	Search all data with the index: groupsio_enriched for the attributes like uuid, origin, creation date, body text, subject and projects.
	"""
	#making an elasticsearch object
	es = Elasticsearch()

	#arrays of attributes to be represented in a dataframe.
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


	df=pd.DataFrame({'uuid':arr_uuid,'origin':arr_origin,'project':arr_project,'project_1':arr_project_1,'grimoirelab_creation_date':arr_grimoirelab_creation_date,'subject_analyzed':arr_subject_analysed,'body':arr_body})

	convert_csv(df)
	convert_xlsx(df)

def convert_csv(df):
	df.to_csv("output.csv",index=None)
def convert_xlsx(df):
	df.to_excel("output.xlsx", index=None)

def main():
	search()
	print("Output files are output.csv and output.xlsx")

if __name__ == "__main__":
    main()
