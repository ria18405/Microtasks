## MICROTASK 1

**AIM:** Set up Perceval to be executed from PyCharm.

**STEPS** 

1. Create a perceval project on Pycharm.

2. ` pip3 install perceval `

or 

2. Clone repository perceval, and open it in Pycharm New project window. A new virtual environment will be formed. 

Now go to `File->Settings->Project Structure-> Add content Root `. After clicking on `+` icon, add the folder which contains the clone of the perceval repository.

Execute these commands : 

```
$ pip3 install -r requirements.txt
$ pip3 install -r requirements_tests.txt
$ pip3 install -e .

```

Optionally, u can also go to `File->Settings->Project Interpreter->` and enter the name of all reurements that need to be installed.

Now perceval.backends.core can be easily imported.


3. Edit Configuration of perceval.py and set parameters as ``` github elastic logstash --from date '2016-01-01' --sleep-for-rate ```

![Image description](https://github.com/ria18405/Microtasks/blob/master/Microtask1/configuration.png)

4. Run perceval.py and see the output.

![Image description](https://github.com/ria18405/Microtasks/blob/master/Microtask1/output.png)

**Output**

Sir Perceval is on his quest.

(Full output file is [here](https://github.com/ria18405/Microtasks/blob/master/Microtask1/output.txt) )