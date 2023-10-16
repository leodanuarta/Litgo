from django.contrib import admin
from . import models


# Register your models here.

class YourModelAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Menonaktifkan operasi penambahan
        return False

    def has_delete_permission(self, request, obj=None):
        # Menonaktifkan operasi penghapusan
        return False

class Halaman_AwalAdminArea(admin.AdminSite) :
    site_header = 'LitGo Admin Site'
    index_title = "LitGo Admin Dashboard"
    site_title =  "Admin"

halaman_awal_site = Halaman_AwalAdminArea(name = 'Halaman_awalAdmin')

models = (models.aboutus, models.sliders, models.footers)
for m in models:
    admin.site.register(m)
    halaman_awal_site.register(m)
# halaman_awal_site.register(models.aboutus)
# admin.site.register(models)