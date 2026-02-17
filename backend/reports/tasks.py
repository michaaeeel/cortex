from celery import shared_task


@shared_task
def generate_report(report_id):
    from .models import Report

    report = Report.objects.get(id=report_id)
    report.status = "processing"
    report.save()

    # TODO: Call ML service, aggregate data, generate insights
    report.status = "completed"
    report.content = {"summary": "Placeholder report content"}
    report.save()
