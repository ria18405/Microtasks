## MICROTASK 7

**AIM:** Install and use elasticdump to download the mapping and data of an ElasticSearch index (it can be anyone created in Microtask 5)

**STEPS:**

1. HOW TO DOWNLOAD ELASTICDUMP:

	- `sudo apt-get install nodejs-dev node-gyp libssl1.0-dev`

	- `sudo apt-get install npm`

	- `npm install elasticdump -g`

2. Now, ```curl 'localhost:9200/_cat/indices?v'``` to find the indexes running:

```
health status index                         uuid                   pri rep docs.count docs.deleted store.size pri.store.size
yellow open   git_chaoss_enriched           vD4-Uo6uRw-szWwoOTepxw   5   1       3851          786      8.5mb          8.5mb
yellow open   git-onion_enriched            aIhO7aMuSTCjrI39flYaBw   5   1        568            0      319kb          319kb
yellow open   git-aoc_chaoss_enriched       n6lD3oatQcurzKhnI2VrQw   5   1       8645           93      7.8mb          7.8mb
yellow open   cocom_chaoss_enrich           taDw8LYfR8CALUxnj6H8yg   5   1          0            0      1.2kb          1.2kb
yellow open   .kibana                       FN5ns8dsQwqoCY6dB2OQ3w   1   1        351            3    397.7kb        397.7kb
yellow open   github_issues_chaoss          Xw1xY3FmQEiXBCIF9u3a_A   5   1       1236           10      9.5mb          9.5mb
yellow open   github_issues_chaoss_enriched OHrEGbKHQBaHo7T0bpe_aw   5   1       1236            0      1.8mb          1.8mb
yellow open   git_chaoss                    jCr8xjWnRvOKj9SLpjGfTQ   5   1       3851            9      4.8mb          4.8mb
yellow open   cocom_chaoss_study            ucBiKoP2TIGfaqhNDk6drQ   5   1          0            0      1.2kb          1.2kb
yellow open   cocom_chaoss                  108oMmfzQqKpA9NR4ugZ6A   5   1          0            0      1.2kb          1.2kb


```

3. Now, we can choose any one, and run elastic dump on it:

```
elasticdump --input=http://localhost:9200/git-onion_enriched --output=git-onion_enriched_mapping.json --type=mapping

```

```
elasticdump --input=http://localhost:9200/git-onion_enriched --output=git-onion_enriched_data.json --type=data

```
![Image description](https://github.com/ria18405/Microtasks/blob/master/Microtask7/OutputData/mapping.png)

![Image description](https://github.com/ria18405/Microtasks/blob/master/Microtask7/OutputData/data.png)

OUTPUT:

* [git-onion_enriched_data.json](https://github.com/ria18405/Microtasks/blob/master/Microtask7/OutputData/git-onion_enriched_data.json)

* [git-onion_enriched_mapping.json](https://github.com/ria18405/Microtasks/blob/master/Microtask7/OutputData/git-onion_enriched_mapping.json)

* [git-chaoss_enriched_data.json](https://github.com/ria18405/Microtasks/blob/master/Microtask7/OutputData/git-chaoss_enriched_data.json)

* [git-chaoss_enriched_mapping.json](https://github.com/ria18405/Microtasks/blob/master/Microtask7/OutputData/git-chaoss_enriched_mapping.json)


Ref:
https://www.npmjs.com/package/elasticdump

https://stackoverflow.com/questions/17426521/list-all-indexes-on-elasticsearch-server
