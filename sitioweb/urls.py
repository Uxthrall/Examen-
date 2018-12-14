from django.conf.urls import include, url
from .import views

# SignUpView, SignInView

urlpatterns = [
	url(r'^$', views.pag_list, name='pag_index'),
	url(r'^listOrden', views.pag_list_orden, name='pag_listOrden'),
	url(r'^add_cli', views.pag_cliente, name='cliente'),
	url(r'^ordenTrabajo/(?P<id_add_cli>\d+)/$', views.pag_orden_trabajo, name='orden'),
	url(r'^registrar', views.pag_registrar, name='registrar'),
	# usuario
	url(r'^salir/$', views.logOut, name='logOut'),
	url(r'^login', views.user_login, name='pag_login'),
]