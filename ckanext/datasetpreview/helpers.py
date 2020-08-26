import json
import logging

log = logging.getLogger(__name__)


def get_preview_chart_data(pkg_dict):
    """
    Check if this dataset use preview and in this case return data to preview
    """
    for extra in pkg_dict['extras']:
        if extra['key'] == 'dataset_preview':
            dp = extra['value']
            log.info('Dataset preview found for{}: {}'.format(pkg_dict['name'], dp))
            return json.loads(dp)

    log.info('No dataset preview for {}'.format(pkg_dict['name']))
    return False