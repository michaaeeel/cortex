from django.db import models


class MetricSnapshot(models.Model):
    campaign = models.ForeignKey(
        "campaigns.Campaign",
        on_delete=models.CASCADE,
        related_name="metrics",
    )
    date = models.DateField()
    impressions = models.BigIntegerField(default=0)
    clicks = models.BigIntegerField(default=0)
    conversions = models.IntegerField(default=0)
    spend = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    revenue = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    ctr = models.FloatField(null=True, blank=True)
    roas = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("campaign", "date")
        ordering = ["-date"]

    def __str__(self):
        return f"{self.campaign.name} - {self.date}"

    def save(self, *args, **kwargs):
        if self.impressions:
            self.ctr = (self.clicks / self.impressions) * 100
        if self.spend:
            self.roas = float(self.revenue) / float(self.spend)
        super().save(*args, **kwargs)
