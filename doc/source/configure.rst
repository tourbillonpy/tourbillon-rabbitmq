Configure
*********


Create the tourbillon-elasticsearch configuration file
======================================================

You must create the tourbillon-elasticsearch configuration file in order to use tourbillon-elasticsearch.
By default, the configuration file must be placed in **/etc/tourbillon/conf.d** and its name
must be **elasticsearch.conf**.

The tourbillon-elasticsearch configuration file looks like: ::

	{
		"database": {
			"name": "elasticsearch",
			"duration": "365d",
			"replication": "1"
		},
		"host": "localhost",
		"base_url": "http://localhost:9200",
		"frequency": 1
	}


You can customize the database name, the hostname with which datapoints are tagged,
the frequency at which measures are collected and the Elasticsearch base url.


Enable the tourbillon-linux metrics collectors
==============================================

To enable the tourbillon-elasticsearch metrics collectors types the following command: ::

	$ sudo -i tourbillon enable tourbillon.elasticsearch=<collector_name>

Where <collector_name> can be one of or a comma separated list of the colectors names within:
	
	* get_es_cluster_stats
	* get_es_nodes_stats

