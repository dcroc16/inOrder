from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from in_order.models import OrderListItem
from in_order.models import OrderTitle
from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.

def index(request):
	strTitle = request.GET.get('q',"nevergirls books")
	currTitle = OrderTitle.objects.get(title=strTitle)
	payload = OrderListItem.objects.filter(oID=currTitle).extra(order_by = ['position'])
	allTitles = OrderTitle.objects.all()
	template = loader.get_template('home.html')
	context = RequestContext(request, {'payload': payload, 'allTitles': allTitles,})
	return HttpResponse(template.render(context))


class OrderItemListView(ListView):
	model = OrderListItem
