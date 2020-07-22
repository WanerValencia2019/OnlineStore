import datetime
from django.utils import timezone
from django.db import models


class ProductManager(models.Manager):
    def get_queryset(self):
        queryset = super(ProductManager, self).get_queryset()
        return queryset
        
    def get_news(self):
        now = timezone.now()
        limit = datetime.timedelta(days=2)
        return self.get_queryset().filter(created_at__gte=now-limit)