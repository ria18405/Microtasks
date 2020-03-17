## MICROTASK3:


**AIM:** Based on the JSON documents produced by Perceval and its source code, try to answer the following questions:


1. What is the meaning of the JSON attribute `timestamp`?
	
	Timestamp is the current UTC date and time of the item.

2. What is the meaning of the JSON attribute `updated_on`?

	It is a unix date time, and represents the last updated time of a given fetched item.

3. What is the meaning of the JSON attribute ```origin```?

	Origin is the identifier of the repository.It defines which origin repository has to be fetched.

4. What is the meaning of the JSON attribute ```category```?
	
	It represents the category of the items fetched. i.e data type of items fetched by backend 

5. How many categories do the GitHub and GitLab backends have?

	Github has 3 categories namely: 'issue', 'pull_request' and 'repository'.

	GitLab has 2 categories namely: 'issue' and 'merge_request'

6. What is the meaning of the JSON attribute ```uuid```?
	
	UUID stands for a Universal Unique Identifier.
	The UUID will be the SHA1 of the concatenation of the values
    from the list. The separator between these values is ':'.
    Each value must be a non-empty string, otherwise, the function
    will raise an exception.


7. What is the meaning of the JSON attribute ```search_fields```?
	
	By default, search_fields contains the id of the item ('item_id': item_id_value). However, each backend can set extra search fields using the dict EXTRA_SEARCH_FIELDS.

8. What is stored in the attribute ```data``` of each JSON document produced by Perceval?
	`data` attribute represents all the data of the item retrieved/fetched from repositories.The contents from the original item are stored under the 'data' keyword.


