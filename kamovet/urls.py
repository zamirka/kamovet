from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'ГСК «Камовец» — Управление сайтом'
admin.site.site_title = 'Камовец'
admin.site.index_title = 'Панель управления'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
