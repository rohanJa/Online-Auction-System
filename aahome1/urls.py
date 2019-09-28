from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^$', views.home, name='home'),
    url(r'^bid/(?P<product_id>\d+)/$', views.bid, name='bid'),
    url(r'^history/(?P<product_id>\d+)/$', views.history, name='history'),
    url(r'^present/$', views.present, name='present'),
    url(r'^pastt/$', views.past, name='past'),
    url(r'^future/$', views.future, name='future'),
    url(r'^product/(?P<product_id>\d+)/$', views.product_detail, name='product_detail'),
    # url(r'^$',views.main_page,name='main_page'),
    #url(r'^postadv/$', views.post_adv, name='post_adv'),
   # url(r'^hello/', views.hello, name='hello'),
    #url(r'^crudops/', views.crudops, name='crudops'),
    #url(r'^(?P<dreamreal_id>[0-9]+)/$', views.detail, name='detail'),
   # url(r'^home/', views.home, name='home'),
    #url(r'^index', views.sourcingCube, name='sourcingCube'),
    #url(r'^service/(?P<service_title>.+)/$', views.service_detail, name='service_detail'),
    #url(r'^product/(?P<product_title>.+)/$', views.product_detail, name='product_detail'),
    
    

]
