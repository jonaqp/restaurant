from django.contrib import admin

from . import models


@admin.register(models.Group)
class TeamAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Role)
class RoleAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Permission)
class PermissionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Types)
class TypesAdmin(admin.ModelAdmin):
    pass
