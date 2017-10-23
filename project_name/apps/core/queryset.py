from django.db import models


class AuditableQueryset(models.query.QuerySet):
    def active(self):
        return self.filter(isDeleted=True)


class AuditableManager(models.Manager):
    def get_queryset(self):
        return AuditableQueryset(
            model=self.model, using=self._db,
            hints=self._hints).filter(isDeleted=False)

    def active(self):
        return self.get_queryset()
