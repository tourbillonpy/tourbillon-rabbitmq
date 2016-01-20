Measurements
************

tourbillon-rabbitmq collects metrics about a RabbitMQ cluster and its nodes.

Please refers to  `https://raw.githack.com/rabbitmq/rabbitmq-management/rabbitmq_v3_6_0/priv/www/api/index.html <https://raw.githack.com/rabbitmq/rabbitmq-management/rabbitmq_v3_6_0/priv/www/api/index.html>`_ for more information.


RabbitMQ stats
==============

tourbillon-rabbitmq store metrics in the ``rmq_global_stats``,  ``rmq_nodes_stats`` and ``rmq_queues_stats`` series.

Each datapoint is tagged with the rabbitmq instance hostname and the values collected are:


Tags
----
	* **hostname**: rabbitmq instance hostname (only for rmq_global_stats)
	* **node**: rabbitmq node name (only for rmq_nodes_stats and rmq_queues_stats)
	* **queue_name**: name of the queue (only for rmq_queues_stats)
	* **vhost**: name of the rabbitmq virtualhost (only for rmq_queues_stats)


Fields
------
.. note::
	Please refers to the RabbitMQ documentation to check the list of metrics collected both for cluster, nodes and queues.


