from operator import attrgetter
from django.urls import reverse
from django.utils.safestring import mark_safe


class NotAddMixin:
    def has_add_permission(self, request):
        return False


class NotDeleteMixin:
    def has_delete_permission(self, request, obj=None):
        return False


class NotChangeMixin:
    def has_change_permission(self, request, obj=None):
        return False


class NotModifyMixin(NotChangeMixin, NotAddMixin, NotDeleteMixin):
    ...


def get_objects_change_links(obj, set_name, lookup_field=None):
    set_objects = getattr(obj, set_name).all()
    links = []
    for set_object in set_objects:
        links.append(get_change_link_by_object(set_object, lookup_field))
    return mark_safe(", ".join(links)) if links else None


def get_object_change_link(obj, fk_name, lookup_field=None):
    if '.' in fk_name:
        fk_obj = attrgetter(fk_name)(obj)
    else:
        fk_obj = getattr(obj, fk_name)
    if not fk_obj:
        return None
    link = get_change_link_by_object(fk_obj, lookup_field)
    return mark_safe(link) if link else None


def get_change_link_by_object(obj, lookup_field=None):
    url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=(obj.id,))
    link = f'<a href="{url}">{obj.name if not lookup_field else getattr(obj, lookup_field)}</a>'
    return link
