## MICROTASK 9

**AIM:** Build a Data Table visualization in Kibiter (you can use the CHAOSS community dashboard) that shows for emails (mbox index) the text of emails (split row by Termbody_extract field).

**STEPS:**

1. Go to Visualisations on Kibiter (Top Left of the Browser window ).

2. Add a new Visualisation of `Data Table`. You can chose any, but for this task, use a Data Table as instructed.

3. Select index as `mbox`.

4. Split row with:
``` 
Aggregation = Terms
Field = body_extract
Order By = metric:Count 
Order = Descending
Size = 100 
```
(Size refers to the number of data entries in the output data table)

![Image description](https://github.com/ria18405/Microtasks/blob/master/Microtask9/assets/task.png)

Some Other visualisations are :

![Image description](https://github.com/ria18405/Microtasks/blob/master/Microtask9/assets/visualisation1.png)
![Image description](https://github.com/ria18405/Microtasks/blob/master/Microtask9/assets/visualisation2.png)