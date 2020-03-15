## MICROTASK 5

**AIM:** Execute micro-mordred to collect, enrich and visualize data from Git and GitHub repositories.

**STEPS**

1. After setting up dev environment , Run micro.py with the params :

```Run```->```Edit Configurations ``` -> click the ```+``` icon and create a Python file with Script path = path to utils/micro.py 
and parameters as ```--raw --enrich --panels --cfg ./setup.cfg --backends git github cocom```

or 

set pwd=grimoirelab-sirmodred/../utils and 
run 
```python3 micro.py --raw --enrich --panels --cfg ./setup.cfg --backends git github cocom```

![Image description](https://github.com/ria18405/Microtasks/blob/master/Microtask4/Output.png)


2. Edit the project.json and add any git repository with enough data to visualise. Also, edit setup.cfg according to the docker-compose version(with/without SecurityGuard)


3. Now, visit https://admin:admin@localhost:5601 on the browser

![Image description](https://github.com/ria18405/Microtasks/blob/master/Microtask5/Overview.png)

![Image description](https://github.com/ria18405/Microtasks/blob/master/Microtask5/git.png)

Project.json and setup.cfg have been attached .