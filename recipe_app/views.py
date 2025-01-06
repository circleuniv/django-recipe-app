from collections import defaultdict

from django.views import  generic

from .models import MenuItems, MEAL_TYPE


class Master(generic.ListView):
    queryset = MenuItems.objects.order_by('-date_created')
    template_name = 'master.html'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["mealtype"]=MEAL_TYPE
        return context


class Detail(generic.DetailView):
    model = MenuItems
    template_name = 'detail.html'



