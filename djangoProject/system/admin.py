import time
from django.contrib import admin
from django.http import HttpResponse
from openpyxl import Workbook
from .models import Prescript,OriginPrice,HistoryPrice,OriginStatistics,Info

class ExportExcelMixin(object):
    def export_as_excel(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields][1:]
        field_verbose_names = [field.verbose_name for field in meta.fields][1:]
        response = HttpResponse(content_type='application/msexcel')
        filename = (time.strftime("%m月%d日", time.localtime())) + self.model._meta.verbose_name
        response['Content-Disposition'] = f'attachment; filename={filename.encode("utf-8").decode("ISO-8859-1")}.xlsx'
        wb = Workbook()
        ws = wb.active
        ws.append(field_verbose_names)
        for obj in queryset:
            data = []
            for field in field_names:
                if hasattr(obj, f'get_{field}_display'):
                    value = getattr(obj, f'get_{field}_display')()
                else:
                    value = getattr(obj, field)
                data.append(f'{value}')
            ws.append(data)
        wb.save(response)
        return response

    export_as_excel.short_description = '导出Excel'
    export_as_excel.type = 'success'

class ControlPrescript(admin.ModelAdmin, ExportExcelMixin):
    list_display = ['name', 'recipe', 'dosage' ,'excerpt', 'indications','note','processing','tcmName','recipe_pz']
    ordering = ['name']
    list_filter = ['name']
    list_per_page = 20
    actions = ['export_as_excel']

class ControlOriginPrice(admin.ModelAdmin, ExportExcelMixin):
    list_display = ['keyword','origin','price']
    ordering = ['keyword']
    list_filter = ['keyword']
    list_per_page = 20
    actions = ['export_as_excel']

class ControlHistoryPrice(admin.ModelAdmin, ExportExcelMixin):
    list_display = ['keyword','updateTime','price']
    ordering = ['keyword']
    list_filter = ['keyword']
    list_per_page = 20
    actions = ['export_as_excel']

class ControlOriginStatistics(admin.ModelAdmin, ExportExcelMixin):
    list_display = ['keyword','origin','count']
    ordering = ['keyword']
    list_filter = ['keyword']
    list_per_page = 20
    actions = ['export_as_excel']

class ControlInfo(admin.ModelAdmin, ExportExcelMixin):
    list_display = ['keyword','title','content']
    ordering = ['keyword']
    list_filter = ['keyword']
    list_per_page = 20
    actions = ['export_as_excel']

admin.site.register(Prescript,ControlPrescript)
admin.site.register(OriginPrice,ControlOriginPrice)
admin.site.register(HistoryPrice,ControlHistoryPrice)
admin.site.register(OriginStatistics,ControlOriginStatistics)
admin.site.register(Info,ControlInfo)

admin.site.site_header = '中药数据分析与可视化'
admin.site.site_title = '中药数据分析与可视化'
admin.site.index_title = '中药数据分析与可视化'
