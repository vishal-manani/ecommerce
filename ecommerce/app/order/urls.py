from django.conf.urls import url
from .views import OrderView, OrderUpdateView

urlpatterns = [
    url(r'^order/$', OrderView.as_view(), name='order_list'),
    # url(r'^product/(?P<pk>[0-9]+)/$', ProductUpdateView.as_view(), name='product_detail'),
    url(r'^order/(?P<pk>[0-9]+)/$', OrderUpdateView.as_view(), name='order_update'),
]