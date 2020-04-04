## MICROTASK 8

**AIM:** Execute micro-mordred to collect and enrich data from a groupsio repository. You need to register to a group (e.g., https://lists.onap.org/g/main) and follow the instructions at https://github.com/chaoss/grimoirelab-sirmordred#groupsio. 
Then, write a script to read the enriched index and import the attributes uuid, project, project_1, origin, grimoirelab_creation_date, body and subject_analyzed to a CSV file. Import the obtained file to an excel sheet (in a manual or automatic way).

**STEP 1:** ENRICH DATA

1. Make a groupsio account and register to a group. Make sure that archive download_permissions are enabled for that group. 

2. [Projects.json](https://github.com/ria18405/Microtasks/blob/master/Microtask8/assets/Projects.json)

```
{
    "Chaoss": {
        "groupsio": [
            "onap",
            "onap+onap-arc"
        ]
    }
}
```

3. Add groupsio section in [setup.cfg](https://github.com/ria18405/Microtasks/blob/master/Microtask8/assets/setup.cfg) file.

4. Run micro.py with configuration with backends= groupsio 
	i.e ```--raw --enrich --panels --cfg ./setup.cfg --backends groupsio```

![Image description](https://github.com/ria18405/Microtasks/blob/master/Microtask8/assets/collection.png)
![Image description](https://github.com/ria18405/Microtasks/blob/master/Microtask8/assets/kibana2.png)


**STEP 2:** READ ENRICHED DATA AND IMPORT TO CSV FILES

Run the [script.py](https://github.com/ria18405/Microtasks/blob/master/Microtask8/script.py) as 
	`python3 script.py`

Output : "Output files are output.csv and output.xlsx"

I have only taken 10 data rows for illustration.


A new output.csv and output.xlsx file will be made and all data i.e uuid, project, project_1, origin, grimoirelab_creation_date, body and subject_analyzed will be stored in a output.csv file. 

![Image description](https://github.com/ria18405/Microtasks/blob/master/Microtask8/assets/csv.png)


![Image description](https://github.com/ria18405/Microtasks/blob/master/Microtask8/assets/excel.png)


Ref:
https://elasticsearch-py.readthedocs.io/en/master/



#### ADDITIONAL TASKS:

**Export CSV to Airtable**
Have added the code to export CSV to Airtable code in [script.py](https://github.com/ria18405/Microtasks/blob/master/Microtask8/script.py)

Have used Airtable APIs to export enriched_index data.

![Image description](https://github.com/ria18405/Microtasks/blob/master/Microtask8/assets/Airtable.png)

Important documentations and referances used:
- https://airtable.com/api
- https://community.airtable.com/t/how-to-programatically-import-csv-to-airtable-creating-a-new-table-in-an-existing-base-csv-is-a-file-on-a-cloud-vm/26189/6


