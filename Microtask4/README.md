**MICROTASK 4:**

**AIM: Set up a dev environment to work on GrimoireLab.**

**STEPS:**


1. Clone all these repositories to a local folder with their 2 remotes : origin and upstream.

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

2. ```Settings``` -> ```Project```->```Project Interpreter```-> click the ```+``` icon and add install packages like mariadb , elasticsearch and kibiter.

3. ```Settings``` -> ```Project```->```Project Settings```-> click the ```+ content root ``` icon and add all the folders of cloned repositories.

![Image description](https://github.com/ria18405/Microtasks/blob/master/Microtask4/ProjectStructure.png)

3. Install all requirements of these cloned repositories.


	```pip install -r requirements.txt```

And go to each folder and run ```python3 setup.py install```

4. Then go to ```Run```->```Edit Configurations ``` -> click the ```+``` icon and create a Python file with Script path = path to utils/micro.py 

and parameters as ```--raw --enrich --panels --cfg ./setup.cfg --backends git cocom```

![Image description](https://github.com/ria18405/Microtasks/blob/master/Microtask4/micro.png)

**Set up finished**
![Image description](https://github.com/ria18405/Microtasks/blob/master/Microtask4/output.png)

