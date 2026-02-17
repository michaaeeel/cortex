from celery import Celery

app = Celery("cortex-pipeline")
app.config_from_object("celeryconfig")
app.autodiscover_tasks(["tasks"])
