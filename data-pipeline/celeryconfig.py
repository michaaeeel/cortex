from decouple import config

broker_url = config("REDIS_URL", default="redis://redis:6379/0")
result_backend = broker_url
accept_content = ["json"]
task_serializer = "json"
result_serializer = "json"
timezone = "UTC"

task_routes = {
    "tasks.google_ads.*": {"queue": "google_ads"},
    "tasks.meta_ads.*": {"queue": "meta_ads"},
    "tasks.google_analytics.*": {"queue": "google_analytics"},
}
