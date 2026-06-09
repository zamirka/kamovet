from django.contrib import admin
from .models import (
    CooperativeInfo, ImportantInfo, Contact,
    Document, News, WorkReport, FinancialReport
)


@admin.register(CooperativeInfo)
class CooperativeInfoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Основное', {'fields': ('name', 'tagline', 'address', 'established_year', 'total_garages', 'working_hours')}),
        ('Описание', {'fields': ('short_description', 'full_description')}),
    )

    def has_add_permission(self, request):
        return not CooperativeInfo.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(ImportantInfo)
class ImportantInfoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Собрания', {'fields': ('meetings_schedule',)}),
        ('Членские взносы', {'fields': ('fee_amount', 'fee_period', 'fee_payment_info')}),
        ('Дополнительно', {'fields': ('extra_info',)}),
    )

    def has_add_permission(self, request):
        return not ImportantInfo.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('role', 'name', 'phone', 'email', 'order')
    list_editable = ('order',)
    ordering = ('order',)


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date', 'is_published')
    list_filter = ('category', 'is_published')
    list_editable = ('is_published',)
    ordering = ('-date',)
    fieldsets = (
        (None, {'fields': ('title', 'category', 'date', 'is_published')}),
        ('Документ', {'fields': ('url', 'description')}),
    )


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'is_published')
    list_editable = ('is_published',)
    ordering = ('-date',)


@admin.register(WorkReport)
class WorkReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'period', 'date')
    ordering = ('-date',)


@admin.register(FinancialReport)
class FinancialReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'period', 'income', 'expenses', 'date')
    ordering = ('-date',)
    fieldsets = (
        (None, {'fields': ('title', 'period', 'date')}),
        ('Суммы', {'fields': ('income', 'expenses')}),
        ('Содержание', {'fields': ('content', 'url')}),
    )
