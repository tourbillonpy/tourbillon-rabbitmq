import logging
import urlparse

import requests
import trollius as asyncio
from trollius import From


logger = logging.getLogger(__name__)


@asyncio.coroutine
def get_rmq_global_stats(agent):
    yield From(agent.run_event.wait())
    logger.debug('starting get_rmq_global_stats')
    config = agent.config['rabbitmq']
    logger.debug('get_rmq_global_stats config retrieved')
    db_config = config['database']
    yield From(agent.async_create_database(**db_config))
    base_url = config['base_url']
    loop = asyncio.get_event_loop()
    while agent.run_event.is_set():
        logger.debug('in while loop')
        try:
            yield From(asyncio.sleep(config['frequency']))
            points = [{
                'measurement': 'rmq_global_stats',
                'tags': {
                    'hostname': config['host'],
                },
                'fields': {
                }
            }]
            global_stats_url = urlparse.urljoin(base_url,
                                                'api/overview')
            res = yield From(loop.run_in_executor(
                None, requests.get, global_stats_url))
            fields = points[0]['fields']
            if res.status_code == 200:
                info = res.json()
                for k, v in info['object_totals'].items():
                    field_name = 'object_totals_{}'.format(k)
                    fields[field_name] = v
                qt = info['queue_totals']
                fields['queue_totals_messages'] = qt['messages']
                fields['queue_totals_messages_rate'] =\
                    qt['messages_details']['rate']
                fields['queue_totals_messages_ready'] = qt['messages_ready']
                fields['queue_totals_messages_ready_rate'] =\
                    qt['messages_ready_details']['rate']
                fields['queue_totals_messages_unacknowledged'] =\
                    qt['messages_unacknowledged']
                fields['queue_totals_messages_unacknowledged_rate'] =\
                    qt['messages_unacknowledged_details']['rate']

                mst = info['message_stats']
                fields['message_stats_ack'] = mst['ack']
                fields['message_stats_ack_rate'] =\
                    mst['ack_details']['rate']
                fields['message_stats_deliver'] = mst['deliver']
                fields['message_stats_deliver_rate'] =\
                    mst['deliver_details']['rate']
                fields['message_stats_deliver_get'] = mst['deliver_get']
                fields['message_stats_deliver_get_rate'] =\
                    mst['deliver_get_details']['rate']
                fields['message_stats_deliver_no_ack'] = mst['deliver_no_ack']
                fields['message_stats_deliver_no_ack_rate'] =\
                    mst['deliver_no_ack_details']['rate']
                fields['message_stats_publish'] = mst['publish']
                fields['message_stats_publish_rate'] =\
                    mst['publish_details']['rate']
                fields['message_stats_redeliver'] = mst['redeliver']
                fields['message_stats_redeliver_rate'] =\
                    mst['redeliver_details']['rate']

                logger.debug('es data: {}'.format(points))
                yield From(agent.async_push(points, db_config['name']))
            else:
                logger.warning('cannot get rabbitmq stats: status={}'
                               .format(res.status_code))
        except:
            logger.exception('cannot get rabbitmq stats')
    logger.info('get_rmq_global_stats terminated')


@asyncio.coroutine
def get_rmq_nodes_stats(agent):
    yield From(agent.run_event.wait())
    logger.debug('starting get_rmq_global_stats')
    config = agent.config['rabbitmq']
    logger.debug('get_rmq_global_stats config retrieved')
    db_config = config['database']
    yield From(agent.async_create_database(**db_config))
    base_url = config['base_url']
    loop = asyncio.get_event_loop()
    while agent.run_event.is_set():
        logger.debug('in while loop')
        try:
            yield From(asyncio.sleep(config['frequency']))
            points = []
            nodes_stats_url = urlparse.urljoin(base_url,
                                                'api/nodes')
            res = yield From(loop.run_in_executor(
                None, requests.get, nodes_stats_url))

            if res.status_code == 200:
                info = res.json()
                for node in info:
                    p = {
                        'measurement': 'rmq_nodes_stats',
                        'tags': {
                            'node': node['name'],
                        },
                        'fields': {
                        }
                    }
                    fields = p['fields']
                    fields['fd_total'] = node['fd_total']
                    fields['fd_used'] = node['fd_used']
                    fields['mem_limit'] = node['mem_limit']
                    fields['mem_used'] = node['mem_used']
                    fields['proc_total'] = node['proc_total']
                    fields['proc_used'] = node['proc_used']
                    fields['run_queue'] = node['run_queue']
                    fields['sockets_total'] = node['sockets_total']
                    fields['sockets_used'] = node['sockets_used']
                    fields['disk_free'] = node['disk_free']
                    fields['disk_free_limit'] = node['disk_free_limit']
                    points.append(p)

                logger.debug('es data: {}'.format(points))
                yield From(agent.async_push(points, db_config['name']))
            else:
                logger.warning('cannot get rabbitmq stats: status={}'
                               .format(res.status_code))
        except:
            logger.exception('cannot get rabbitmq stats')
    logger.info('get_rmq_nodes_stats terminated')


@asyncio.coroutine
def get_rmq_queues_stats(agent):
    yield From(agent.run_event.wait())
    logger.debug('starting get_rmq_global_stats')
    config = agent.config['rabbitmq']
    logger.debug('get_rmq_queues_stats config retrieved')
    db_config = config['database']
    yield From(agent.async_create_database(**db_config))
    base_url = config['base_url']
    loop = asyncio.get_event_loop()
    while agent.run_event.is_set():
        logger.debug('in while loop')
        try:
            yield From(asyncio.sleep(config['frequency']))
            points = []
            queues_stats_url = urlparse.urljoin(base_url,
                                                'api/queues')
            res = yield From(loop.run_in_executor(
                None, requests.get, queues_stats_url))

            if res.status_code == 200:
                info = res.json()
                for queue in info:
                    p = {
                        'measurement': 'rmq_queues_stats',
                        'tags': {
                            'node': queue['node'],
                            'queue_name': queue['name'],
                            'vhost': queue['vhost']
                        },
                        'fields': {
                        }
                    }

                    fields = p['fields']
                    fields['consumers'] = queue['consumers']
                    fields['memory'] = queue['memory']
                    fields['messages'] = queue['messages']
                    fields['messages_ready'] = queue['messages_ready']
                    fields['messages_unacknowledged'] =\
                        queue['messages_unacknowledged']

                    if 'message_stats' in queue:
                        mst = queue['message_stats']
                        if 'ack' in mst:
                            fields['message_stats_ack'] = mst['ack']
                            fields['message_stats_ack_rate'] =\
                                mst['ack_details']['rate']
                        if 'deliver' in mst:
                            fields['message_stats_deliver'] = mst['deliver']
                            fields['message_stats_deliver_rate'] =\
                                mst['deliver_details']['rate']
                        if 'deliver_get' in mst:
                            fields['message_stats_deliver_get'] =\
                                mst['deliver_get']
                            fields['message_stats_deliver_get_rate'] =\
                                mst['deliver_get_details']['rate']
                        if 'publish' in mst:
                            fields['message_stats_publish'] = mst['publish']
                            fields['message_stats_publish_rate'] =\
                                mst['publish_details']['rate']
                        if 'redeliver' in mst:
                            fields['message_stats_redeliver'] = mst['redeliver']
                            fields['message_stats_redeliver_rate'] =\
                                mst['redeliver_details']['rate']
                        points.append(p)

                logger.debug('es data: {}'.format(points))
                yield From(agent.async_push(points, db_config['name']))
            else:
                logger.warning('cannot get rabbitmq stats: status={}'
                               .format(res.status_code))
        except:
            logger.exception('cannot get rabbitmq stats')
    logger.info('get_rmq_queues_stats terminated')
