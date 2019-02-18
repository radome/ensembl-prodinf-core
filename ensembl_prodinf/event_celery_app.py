import logging

from celery import Celery
from celery.utils.log import get_task_logger

from utils import add_app_handler

app = Celery('ensembl_prodinf', include=['ensembl_prodinf.event_tasks'])

# Load the externalised config module from PYTHONPATH
try:
    import event_celery_app_config

    app.config_from_object('event_celery_app_config')
    add_app_handler(get_task_logger(__name__), __name__)

except StandardError as e:
    logging.exception("Error loading event_celery_app_config app config %s", e)
    logging.warning('Celery email requires event_celery_app_config module')
if __name__ == '__main__':
    app.start()
