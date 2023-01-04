from django.contrib import admin

from .models import MasterParameter, MasterBarang, TransaksiPenyesuaianStok

# Register your models here.
admin.site.register(MasterParameter)
admin.site.register(MasterBarang)
admin.site.register(TransaksiPenyesuaianStok)
