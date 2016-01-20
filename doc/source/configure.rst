Configure
*********


Create the tourbillon-rabbitmq configuration file
=================================================

You must create the tourbillon-rabbitmq configuration file in order to use tourbillon-rabbitmq.
By default, the configuration file must be placed in **/etc/tourbillon/conf.d** and its name
must be **rabbitmq.conf**.

The tourbillon-rabbitmq configuration file looks like: ::

	{
		"database": {
			"name": "rabbitmq",
			"duration": "10d",
			"replication": "1"
		},
		"host": "localhost",
		"base_url": "http://guest:guest@localhost:15672",
		"frequency": 1
	}


You can customize the database name, the hostname with which datapoints are tagged,
the frequency at which measures are collected and the Elasticsearch base url.


Enable the tourbillon-rabbitmq metrics collectors
=================================================

To enable the tourbillon-rabbitmq metrics collectors types the following command: ::

	$ sudo -i tourbillon enable tourbillon.rabbitmq=<collector_name>

Where <collector_name> can be one of or a comma separated list of the colectors names within:
	
	* get_rmq_global_stats
	* get_rmq_nodes_stats
	* get_rmq_queues_stats
