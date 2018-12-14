from django.shortcuts import render,redirect
from django.template import RequestContext
from sitioweb.models import Tecnico,add_cli,add_OrdenTrabajo
from django.views.decorators.csrf import csrf_exempt

# usuario
from django.views.generic import CreateView, TemplateView
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.urls import reverse
# fin


# , UserProfileInfoForm

# Create your views here.



	
@csrf_exempt
def pag_cliente(request):
	form= Tecnico.objects.all()
	cli = add_cli()
	if request.method=="POST":
		cli.nombre = request.POST['nombre']
		cli.direccion = request.POST['direccion']
		cli.ciudad = request.POST['opt']
		cli.comuna = request.POST['cosa']
		cli.telefono = request.POST['telefono']
		cli.correo = request.POST['correo']
		cli.tecnico = request.POST['tecnico']
		
		cli.save()
		estado=True

	contex={'formularios':form}
	return render(request,'Clientes.html',contex)

def pag_list(request):
	form= add_cli.objects.all()
	contex={'formularios':form}
	return	render(request,'index.html',contex)

def pag_orden_trabajo(request, id_add_cli):
	clientes=add_cli.objects.get(id=id_add_cli)
	form= Tecnico.objects.all()
	orden=add_OrdenTrabajo()
	if request.method=='POST':

		if request.POST['nombre']!="" and request.POST['fecha']!="" and request.POST['hora_ini']!="" and request.POST['hora_ter']!="" and request.POST['id_asc']!="" and request.POST['modelo']!="" and request.POST.get('tecnico', False)!="":

			orden.cliente=request.POST['nombre']
			orden.fecha=request.POST['fecha']
			orden.hora_ini=request.POST['hora_ini']
			orden.hora_ter=request.POST['hora_ter']
			orden.id_ascen=request.POST['id_asc']
			orden.modelo=request.POST['modelo']
			orden.fallas=request.POST['fallas']
			orden.reparacion=request.POST['reparacion']
			orden.pieza_cam=request.POST['piezas']
			orden.nom_trab=request.POST.get('tecnico', False)

			orden.save()

	return render(request,'ordenTrabajo.html', {'clientes':clientes, 'formularios':form})
	


def pag_list_orden(request):
	form= add_OrdenTrabajo.objects.all()
	contex={'formularios':form}
	return	render(request,'ordenes.html',contex)

def pag_registrar(request):
	
	tec = Tecnico()
	user_form = UserForm()
	if request.method=='POST':		
		user_form = UserForm(data=request.POST)
		if user_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			tec.nombre = request.POST['nombre']		
			tec.save()
			user.save()

	
	return render(request,'RegistrarTecnicos.html',{'user_form':user_form})

# usuario


@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('pag_index'))
            else:
                return HttpResponse("Tu cuenta está inactiva")
        else:
            return HttpResponse("Datos de ingreso incorrectos!")
    else:
        return render(request, 'Login.html', {})

def logOut(request):
	logout(request)
	return redirect('/')

# @login_required
# def special(request):
#     return HttpResponse("Has iniciado sesión correctamente")

# @login_required
# def user_logout(request):
#     logout(request)
#     return HttpResponseRedirect(reverse('register'))




# def mostrar(request):
# 	userito = UserProfileInfo.objects.all()
# 	contexto = {'equisde':userito}
# 	return render(request, 'blog/index.html',contexto)

# def Login(request):  
#     return render(request, 'blog/Login.html', {})


# fin
