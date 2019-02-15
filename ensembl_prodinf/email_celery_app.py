import logging

from celery import Celery

from .utils.app_logging import add_app_handler

app = Celery('ensembl_prodinf', include=['ensembl_prodinf.email_tasks'])

# Load the externalised config module from PYTHONPATH
try:
    import email_celery_app_config

    app.config_from_object('email_celery_app_config')
    add_app_handler(app.log, __name__)
except StandardError as e:
    logging.exception("Error loading email_celery_app_config app config %s", e)
    logging.warning('Celery email requires email_celery_app_config module')

if __name__ == '__main__':
    app.start()
