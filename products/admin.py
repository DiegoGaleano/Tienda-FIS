from django.contrib import admin

# Models
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
	readonly_fields = ('created', 'updated')

class ProductAdmin(admin.ModelAdmin):
    #columnas que se verán en la lista de usuarios
    list_display = ('pk', 'name', 'price' )
    # # nos lleva al detalle
    # list_display_links = ('pk', 'user')
    # # campos editable desde las listas
    # list_editable = ('phone_number', 'picture')
    # # elementos de busqueda
    # search_fields = ('user__email', 'user__first_name', 'user__last_name', 'user__phone_number','user_username')
    # # Filtros
    # list_filter = ('created', 'updated', 'user__is_active', 'user__is_staff')

    # fieldsets = (
    #     ('Profile', {
    #         'fields': (('user', 'picture'),),
    #     }),
    #     ('Extra info', {
    #         'fields': (
    #             ('phone_number'),
    #             ('biography')
    #         )
    #     }),
    #     ('Metadata', {
    #         'fields': (('created', 'updated'),),
    #     })
    # )

    # readonly_fields = ('created', 'updated',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
