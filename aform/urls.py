from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import(signup, login_view, post_adv, view_adv, logout_view, searchl,searchp, searchf,single_adv)
from django.contrib.auth.views import(
    password_reset, password_reset_done, password_reset_confirm, password_reset_complete)
    
urlpatterns = [
    #url(r'^$', views.index, name='index'),
    #url(r'^register_user/$', views.UserFormView.as_view(), name='UserForm'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^login/$', login_view, name='login_view'),
    url(r'^postadv/$', post_adv, name='post_adv'),
    url(r'^viewadv/$', view_adv, name='view_adv'),
    url(r'^searchl/$', searchl, name='searchl'),
    url(r'^searchf/$', searchf, name='searchf'),
    url(r'^searchp/$', searchp, name='searchp'),
    url(r'^logout/$', logout_view, name='logout_view'),
    url(r'^singleadv/(?P<product_id>\d+)/$', single_adv, name='single_adv'),
    # url(r'^singleadv/(?P<product_id>\d+)/$', change_data, name='change_data'),
]   
