MICROTASK 4:
AIM: Set up a dev environment to work on GrimoireLab.
STEPS:
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

3. ```Settings``` -> ```Project```->```Project Settings```-> click the ```+``` icon and add all the folders of cloned repositories.

3. Install all requirements of these cloned repositories.
	```pip install -r requirements.txt```
And go to each folder and run ```python3 setup.py install``` 
