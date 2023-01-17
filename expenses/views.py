from django.views.generic.list import ListView
from django.http import HttpResponse
from django.template import loader

from .forms import ExpenseSearchForm
from .models import Expense, Category
from .reports import summary_per_category


class ExpenseListView(ListView):
    model = Expense
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = object_list if object_list is not None else self.object_list

        form = ExpenseSearchForm(self.request.GET)
        if form.is_valid():
            name = form.cleaned_data.get('name', '').strip()
            if name:
                queryset = queryset.filter(name__icontains=name)

        return super().get_context_data(
            form=form,
            object_list=queryset,
            summary_per_category=summary_per_category(queryset),
            **kwargs)


class CategoryListView(ListView):
    model = Category
    paginate_by = 5

#functions for sorting
class Sort(ListView):
    model = Expense
    paginate_by = 5

    def sort_date_to(request):
        mydata = Expense.objects.all().order_by('-date').values()
        template = loader.get_template('expense_list.html')
        context = {
            'sort': mydata,
        }
        return HttpResponse(template.render(context, request))

    def sort_date_from(request):
        data = Expense.objects.all().order_by('date').values()
        template = loader.get_template('expense_list.html')
        context = {
            'sorting': data,
            }
        return HttpResponse(template.render(context, request))

    def sort_name(request):
        name = Expense.objects.all().order_by('name').values()
        template = loader.get_template('expense_list.html')
        context = {
            'sorted': name,
            }
        return HttpResponse(template.render(context, request))

    def sort_amount(request):
        amo = Expense.objects.all().order_by('amount').values()
        template = loader.get_template('expense_list.html')
        context = {
            'sorter': amo,
            }
        return HttpResponse(template.render(context, request))

    def sort_category(request):
        cat = Expense.objects.all().order_by('category').values()
        template = loader.get_template('expense_list.html')
        context = {
            'sorters': cat,
            }
        return HttpResponse(template.render(context, request))

#funtions for searching
class Search(ListView):
    model = Expense
    paginate_by = 5

    def search_date_to(request):
        mydata = Expense.objects.all().filters('-date').values()
        template = loader.get_template('expense_list.html')
        context = {
            'search': mydata,
        }
        return HttpResponse(template.render(context, request))

    def search_date_from(request):
        data = Expense.objects.all().filters('date').values()
        template=loader.get_template('expense_list.html')
        context = {
                'searching': data,
        }
        return HttpResponse(template.render(context, request))

    def search_name(request):
        name = Expense.objects.all().filters('name').values()
        template=loader.get_template('expense_list.html')
        context = {
                'searcher': name,
        }
        return HttpResponse(template.render(context, request))

    def search_amount(request):
        amount = Expense.objects.all().filters('-date').values()
        template = loader.get_template('expense_list.html')
        context = {
            'searchers': amount,
        }
        return HttpResponse(template.render(context, request))

    def search_category(request):
        category = Expense.objects.all().filters('-date').values()
        template=loader.get_template('expense_list.html')
        context = {
                'searcherss': category,
        }
        return HttpResponse(template.render(context, request))







