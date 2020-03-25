## MICROTASK 4:

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

![Image description](https://github.com/ria18405/Microtasks/blob/master/Microtask4/assets/remotes.png)

2. ```Settings``` -> ```Project```->```Project Interpreter```-> click the ```+``` icon and add install all requirement packages like mariadb , elasticsearch, dulwich etc (Find all requirements [here](https://github.com/chaoss/grimoirelab-perceval/blob/master/requirements.txt) )

3. ```Settings``` -> ```Project```->```Project Settings```-> click the ```+ content root ``` icon and add all the folders of cloned repositories.

![Image description](https://github.com/ria18405/Microtasks/blob/master/Microtask4/assets/ProjectStructure.png)

4. Set up docker and try connecting to local host (i.e ```curl -XGET https://admin:admin@localhost:9200 -k ```) to check if connection is being set up. 

5. Then go to ```Run```->```Edit Configurations ``` -> click the ```+``` icon and create a Python file with Script path = path to utils/micro.py 

and parameters as ```--raw --enrich --panels --cfg ./setup.cfg --backends git cocom```

![Image description](https://github.com/ria18405/Microtasks/blob/master/Microtask4/assets/Output.png)


**Set up finished**

**STEPS to setup docker :**

1. Make a docker-compose.yml file with contents : (You have 2 options- with SearchGuard or without SearchGuard)
```
elasticsearch:
  restart: on-failure:5
  image: bitergia/elasticsearch:6.1.0-secured
  command: elasticsearch -Enetwork.bind_host=0.0.0.0 -Eexithttp.max_content_length=2000mb
  environment:
    - ES_JAVA_OPTS=-Xms2g -Xmx2g
  ports:
    - 9200:9200

kibiter:
  restart: on-failure:5
  image: bitergia/kibiter:secured-v6.1.4-5
  environment:
    - PROJECT_NAME=Development
    - NODE_OPTIONS=--max-old-space-size=1000
    - ELASTICSEARCH_URL=https://elasticsearch:9200
    - ELASTICSEARCH_USER=kibanaserver
    - ELASTICSEARCH_PASSWORD=kibanaserver
  links:
    - elasticsearch
  ports:
    - 5601:5601

``` 
(I have ignored mariadb portion since I had MySQL running)


3. Run ```docker-compose up -d```. In case of error like 
> ERROR: Couldn't connect to Docker daemon at http+docker://localunixsocket - is it running? 

Do not use sudo for running the command, instead follow step 4.

4. Add user details . See this for adding user details : https://docs.docker.com/install/linux/linux-postinstall/


5. Run ```docker-compose up -d```

![Image description](https://github.com/ria18405/Microtasks/blob/master/Microtask4/assets/dockersetup.png)
(docker setup- complete)


7. run ```systemctl status docker``` to know the status of docker and ```docker ps``` to know the status of the container.

![Image description](https://github.com/ria18405/Microtasks/blob/master/Microtask4/assets/dockeractive.png)  



