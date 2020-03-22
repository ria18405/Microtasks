## Microtask 6:
**AIM:** Using the dev tools in Kibiter, create a query that counts the number of unique authors on a Git repository from 2018-01-01 until 2019-01-01.

Connect to localhost:5601 after setting up dev environment, click on dev tools.

Use the console for this query.

For the operation from 2018-01-01 to 2019-01-01, use `range` operator on `author_date` where `gte` stands for greater than or equal to and `lte` stamds for less than or equal to.

Now we need to count no of unique authors satisfying the above condition, we use `cardinality` operator on field `author_id` (as it is the only attribute which is unique)

```
GET _search
{"size":0,
  "query": {
    "range": {
      "author_date": {
        "gte": "2018-01-01",
        "lte": "2019-01-01"
      }
    }
    
  },
  "aggs": {
      "unique_author_count": {
        "cardinality": {
          "field": "author_id"
        }
      }
    }
}
```

![Image description](https://github.com/ria18405/Microtasks/blob/master/Microtask6/kibana_console_query.png)

Had we not used the attribute `size`, we would have obtained the output as shown below. Data wuld be displayed intead of counting the number of entries.
![Image description](https://github.com/ria18405/Microtasks/blob/master/Microtask6/withoutsize.png)

Ref: 
https://kb.objectrocket.com/elasticsearch/elasticsearch-how-to-display-query-results-in-a-kibana-console

https://www.elastic.co/guide/en/elasticsearch/reference/current/search-aggregations-metrics-cardinality-aggregation.html

http://man.hubwiz.com/docset/ElasticSearch.docset/Contents/Resources/Documents/www.elastic.co/guide/en/elasticsearch/reference/current/search-aggregations-metrics-valuecount-aggregation.html