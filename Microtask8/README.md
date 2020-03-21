## MICROTASK 8

**AIM:** Execute micro-mordred to collect and enrich data from a groupsio repository. You need to register to a group (e.g., https://lists.onap.org/g/main) and follow the instructions at https://github.com/chaoss/grimoirelab-sirmordred#groupsio. 
Then, write a script to read the enriched index and import the attributes uuid, project, project_1, origin, grimoirelab_creation_date, body and subject_analyzed to a CSV file. Import the obtained file to an excel sheet (in a manual or automatic way).

STEP 1: ENRICH DATA

Projects.json 

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
You can check permissions via this code :https://gist.github.com/abhiandthetruth/b198e3b965f02f1742f2f7fa9f89df7c


![Image description](https://github.com/ria18405/Microtasks/blob/master/Microtask8/assets/collection.png)
![Image description](https://github.com/ria18405/Microtasks/blob/master/Microtask8/assets/kibana.png)
![Image description](https://github.com/ria18405/Microtasks/blob/master/Microtask8/assets/kibana2.png)

STEP 2: READ ENRICHED DATA AND IMPORT TO CSV FILES
