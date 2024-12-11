from typing import Tuple, List, Union
from django.contrib import admin
from django.db import models
from django.db.models import QuerySet
from django.utils.html import format_html

from e_n_n.models import ElectronicNetworkNode
from contacts.models import Contacts


class ContactInline(admin.TabularInline):
    model: models.Model = Contacts


class ENNAdmin(admin.ModelAdmin):

    inlines: List[admin.TabularInline] = [ContactInline,]
    list_display: Tuple[str, ...] = ("id", "name", "node_type", "to_supplier", "debt")
    list_display_links: Tuple[str, ...] = ('name', 'to_supplier')
    list_filter: Tuple[str, ...] = ('contacts__city', )
    fields: List[Union[Tuple[str, ...], str]] = [("id", "name"),
                                                 ("node_type", "supplier"),
                                                 "debt",
                                                 "date"]
    readonly_fields: Tuple[str, ...] = ("id", "date",)
    search_fields: Tuple[str, ...] = ("name",)
    save_on_top: bool = True
    actions: List[str] = ['clear_dept']

    def to_supplier(self, obj: ElectronicNetworkNode):

        if obj.supplier is not None:
            return format_html(
                '<a href="/admin/e_n_n/enn/{id}">{name}</a>',
                id=obj.supplier.id,
                name=obj.supplier
            )


    @admin.action(description='clear debt')
    def clear_dept(self, request, queryset: QuerySet) -> None:
        queryset.update(debt=0)




admin.site.register(ElectronicNetworkNode, ENNAdmin)

