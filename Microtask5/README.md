## MICROTASK 5

**AIM:** Execute micro-mordred to collect, enrich and visualize data from Git and GitHub repositories.

**STEPS**

1. After setting up dev environment , Run micro.py with the params :

```Run```->```Edit Configurations ``` -> click the ```+``` icon and create a Python file with Script path = path to utils/micro.py 
and parameters as ```--raw --enrich --panels --cfg ./setup.cfg --backends git cocom```

or 

set pwd=grimoirelab-sirmodred/../utils and 
run 
```python3 micro.py --raw --enrich --panels --cfg ./setup.cfg --backends git cocom```

![Image description](https://github.com/ria18405/Microtasks/blob/master/Microtask4/Output.png)

2. Edit the project.json and add any git repository , In my case, since I did not have any repository with enough number of commits, I am using chaoss data only.

3. Now, visit https://admin:admin@localhost:5601 on the browser

