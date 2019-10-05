import django_tables2 as tables
from .models import equipment

class equipmentTable(tables.Table):

    T_read =('<button type=\"button\" class=\"read-book btn btn-sm btn-primary\"  data-id="{% url \'read_book\' record.pk %}\"><span class=\"fa fa-eye\"></span> </button>')
    read = tables.TemplateColumn(T_read); read.verbose_name=''

    T_edit =('<button type=\"button\" class=\"update-book btn btn-sm btn-primary\"  data-id="{% url \'update_book\' record.pk %}\"><span class=\"fa fa-pencil\"></span> </button>')
    edit = tables.TemplateColumn(T_edit); edit.verbose_name=''

    T_del =('<button type=\"button\" class=\"delete-book btn btn-sm btn-danger\"  data-id="{% url \'delete_book\' record.pk %}\"><span class=\"fa fa-trash\"></span> </button>')
    delele = tables.TemplateColumn(T_del); delele.verbose_name=''

    #delete2 = tables.TemplateColumn('<a href="{% url "delete_division" record.pk %}"> width="25"></a>',verbose_name=u'Delete',)
    class Meta:
        model = equipment
        template_name = "django_tables2/bootstrap.html"
