from django.urls import path
from .views import CustomerListView, customer_render_pdf_view, render_pdf_view


app_name = 'customers'


urlpatterns = [
    path('',CustomerListView.as_view(),name='customer-list-view'),
    path('test/',render_pdf_view,name='test-view'),
    path('pdf/<int:pk>/',customer_render_pdf_view,name='customer-pdf-view')
]
