from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^paciente/nuevo','CentroAsist.views.registro_paciente', name='registro_paciente'),

    url(r'^paciente/(?P<id_paciente>\d+)','CentroAsist.views.registro_hc', name='registro_hc'),

    url(r'^login/','CentroAsist.views.login_view', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name="auth_logout"),
    url( regex=r'^login/$', view=login, kwargs={'template_name': 'login.html'}, name='login' ), url( regex=r'^logout/$', view=logout, kwargs={'next_page': '/'}, name='logout' ),

]