
**CONNECTION REFUSED**

* Indications:  Cannot connect to locallhost with ```curl -XGET <elasticsearch-url> -k  ``` 

* Diagnosis: 

    - Check docker logs : 
    
	    a. [Low Virtual Memory](https://github.com/chaoss/grimoirelab-sirmordred#low-virtual-memory)
	    
	    b. Low File Descriptors

    - Check with other version of docker-compose (with/without SecurityGuard), and compose the docker again. (https://github.com/chaoss/grimoirelab-sirmordred#source-code-and-docker)

    - Try changing port number to any number say 9300, and try connecting to localhost. 

* Solution :

    Start a fresh environment 

    - Make sure there is no entry in ```docker ps``` output. To do that, run ```docker-compose down --remove-orphans```

    - Make a fresh installation ```docker system prune -a --volume```, This will clear all containers from the system.

    - Now, execute docker-compose up using the source code (https://github.com/chaoss/grimoirelab-sirmordred#source-code-and-docker 

    - Check connection by connecting to the localhost and later try executing micromondred by setup.cfg and project.json. The data should be visible through the dashboard.


**RATE LIMIT EXHAUSTED**

* Indication: While executing perceval, see error message ```RuntimeError: Rate limit exhausted.; 3581.0 seconds to rate reset```

* Solution : Enable the sleep-for-rate parameter. 



**NO SWAP SPACE**

* Indication: While composing docker , NO SWAP SPACE would be displayed.

* Solution:  Edit the ```/etc/default/grub file``` with sudo previleges.
	```
	    GRUB_CMDLINE_LINUX="cgroup_enable=memory swapaccount=1" 
		sudo update-grub
	```
    And restart the system.

