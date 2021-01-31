from django.db.models import Manager
from django.utils import timezone


class PromoCodesManager(Manager):
    def get_queryset(self):
        return super().get_queryset().all()
    
    def validate(self, code):
        now = timezone.now()
        queryset = self.get_queryset().filter(code = code).filter(used=False).filter(valid_from__lte=now).filter(valid_to__gte=now).first()
        return queryset