from django.contrib import admin
from .models import Ingreso, Cuenta, Movimiento

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    list_display= ('title', 'author', 'published', 'post_categories')
    ordering = ('author', 'published')
    search_fields = ('title', 'content', 'author__username', 'categories__name')
    date_hierarchy = 'published'
    list_filter = ('author__username', 'categories__name')

    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    post_categories.short_description = "Categorias"

class IngresoAdmin(admin.ModelAdmin):
    readonly_fields=('monto','descripcion','fecha')


class CuentaAdmin(admin.ModelAdmin):
    readonly_fields=('cuenta','categoria','signo')


class MovimientoAdmin(admin.ModelAdmin):
    readonly_fields=('cuenta','cantidad','signo','detalle','fecha')

    
    


admin.site.register(Ingreso)
admin.site.register(Cuenta)
admin.site.register(Movimiento)

 





