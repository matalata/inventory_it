from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import (BSModalLoginView,
                                           BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)

from .forms import BookForm, CustomUserCreationForm, CustomAuthenticationForm
from .models import equipment
import django_tables2 as tables
from .tables import equipmentTable
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django_tables2.export.views import ExportMixin
from django_tables2 import MultiTableMixin, RequestConfig, SingleTableMixin, SingleTableView
from django_filters.views import FilterView
from .filters import EqFilter
from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)


# @method_decorator(login_required, name='dispatch')
class FilteredEqListView(ExportMixin, SingleTableMixin, FilterView):
    table_class = equipmentTable
    filterset_class = EqFilter
    table_pagination = {"per_page": 20}
    queryset = equipment.objects.all()
    show_header = True
    export_formats = ("csv", "xls")
    model = equipment
    template_name = "index.html"
    #template_name = "bootstrap_template.html"


class BookCreateView(BSModalCreateView):
    template_name = 'examples/create_book.html'
    form_class = BookForm
    success_message = 'Добавлено.'
    success_url = reverse_lazy('index')


class BookUpdateView(BSModalUpdateView):
    model = equipment
    template_name = 'examples/update_book.html'
    form_class = BookForm
    success_message = 'Success: Book was updated.'
    success_url = reverse_lazy('index')


class BookReadView(BSModalReadView):
    model = equipment
    template_name = 'examples/read_book.html'


class BookDeleteView(BSModalDeleteView):
    model = equipment
    template_name = 'examples/delete_book.html'
    success_message = 'Success: Book was deleted.'
    success_url = reverse_lazy('index')


class SignUpView(BSModalCreateView):
    form_class = CustomUserCreationForm
    template_name = 'examples/signup.html'
    success_message = 'Success: Sign up succeeded. You can now Log in.'
    success_url = reverse_lazy('index')


class CustomLoginView(BSModalLoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'examples/login.html'
    success_message = 'Success: You were successfully logged in.'
    success_url = reverse_lazy('index')
