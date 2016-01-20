Measurements
************

tourbillon-elasticsearch collects metrics about an Elasticsearch cluster and its nodes.

Please refers to  `https://www.elastic.co/guide/en/elasticsearch/guide/current/_cluster_health.html <https://www.elastic.co/guide/en/elasticsearch/guide/current/_cluster_health.html>`_ and `https://www.elastic.co/guide/en/elasticsearch/guide/current/_monitoring_individual_nodes.html <https://www.elastic.co/guide/en/elasticsearch/guide/current/_monitoring_individual_nodes.html>`_ for more information.


Elasticsearch stats
===================

tourbillon-elasticsearch store metrics in the ``es_cluster_stats`` and ``es_nodes_stats`` series.
Each datapoint is tagged with the elasticsearch instance hostname and the values collected are:


Tags
----
	* **host**: elasticsearch instance hostname

Fields
------
.. note::
	Please refers to the Elasticsearch monitoring documentation to check the list of metrics collected both for cluster and nodes.


