from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import ListView
from .models import Customer


class CustomerListView(ListView):
    model = Customer
    template_name = 'customers/main.html'


def customer_render_pdf_view(request,*args,**kwargs):


    pk = kwargs.get('pk')
    customer = get_object_or_404(Customer,pk = pk)




    template_path = 'customers/pdf2.html'
    context = {'customer': customer}

    # Create a Django response object, and set content type to PDF
    response = HttpResponse(content_type='application/pdf')

    # for display pdf 
    response['Content-Disposition'] = 'filename="report.pdf"'

    # for download pdf
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html,dest=response)

    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')

    return response



def render_pdf_view(request):
    template_path = 'customers/pdf1.html'
    context = {'myvar': 'this is your template context'}

    # Create a Django response object, and set content type to PDF
    response = HttpResponse(content_type='application/pdf')

    # for display pdf 
    response['Content-Disposition'] = 'filename="report.pdf"'

    # for download pdf
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html,dest=response)

    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')

    return response