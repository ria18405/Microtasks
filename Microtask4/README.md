**MICROTASK 4:**

**AIM: Set up a dev environment to work on GrimoireLab.**

**STEPS:**


1. Clone all these repositories to a local folder with their 2 remotes : ```origin and upstream.``` 
To add upstream of a repo : ```git remote add upstream https://github.com/chaoss/grimoirelab-repo.git ```  (change repo with repo-name)

	-SirModred

	-ELK

	-Graal

	-Perceval

	-Perceval for Mozilla

	-Perceval for OPNFV

	-Perceval for Puppet

	-Perceval for FINOS

	-SortingHat

	-Sigils

	-Kidash

	-Toolkit

	-Cereslib

	-Manuscripts

![Image description](https://github.com/ria18405/Microtasks/blob/master/Microtask4/remotes.png)

2. ```Settings``` -> ```Project```->```Project Interpreter```-> click the ```+``` icon and add install packages like mariadb , elasticsearch and kibiter etc

3. ```Settings``` -> ```Project```->```Project Settings```-> click the ```+ content root ``` icon and add all the folders of cloned repositories.

![Image description](https://github.com/ria18405/Microtasks/blob/master/Microtask4/ProjectStructure.png)


4. Then go to ```Run```->```Edit Configurations ``` -> click the ```+``` icon and create a Python file with Script path = path to utils/micro.py 

and parameters as ```--raw --enrich --panels --cfg ./setup.cfg --backends git cocom```

![Image description](https://github.com/ria18405/Microtasks/blob/master/Microtask4/micro.png)

**Set up finished**
![Image description](https://github.com/ria18405/Microtasks/blob/master/Microtask4/output.png)

