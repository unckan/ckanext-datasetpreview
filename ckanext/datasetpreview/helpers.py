import csv
import json
import logging
import requests


log = logging.getLogger(__name__)


def get_preview_chart_data(pkg_dict):
    """
    Check if this dataset use preview and in this case return data to preview
    """
    for extra in pkg_dict['extras']:
        if extra['key'] == 'dataset_preview':
            dp = extra['value']
            log.info('Dataset preview found for{}: {}'.format(pkg_dict['name'], dp))
            # defaul values
            data = {
                'name': unicode(pkg_dict['name']).encode("utf-8"),
                'height': 450,
                'chart_title': 'Titulo del grafico',
                'url': 'http://ckan:5000/dataset/23149dfc-45af-43d2-b8b4-9093a3224043/resource/f47bc588-1782-4d4f-9349-3c8d564db127/download/altas-patrimoniales-por-partida-parcial-2014.csv'
            }
            cfg_data = json.loads(dp)
            new_data = {unicode(k).encode("utf-8"): unicode(v).encode("utf-8") for k, v in cfg_data.iteritems()}
            data.update(new_data)

            return data

    log.debug('No dataset preview for {}'.format(pkg_dict['name']))
    return False

def csv_as_data(url):
    response = requests.get(url)
    
