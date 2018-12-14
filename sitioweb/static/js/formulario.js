var opt_1 = new Array("Iquique","Taramugal")
var opt_2 = new Array("Antofagasta","El Loa", "Tocopilla")
var opt_3 = new Array("Chañaral","Copiapo", "Huasco")
var opt_4 = new Array("Choapa","Elqui", "Limarí")
var opt_5 = new Array("Los Andes","Loa", "Marga","Petorca","Quillota","San Antonio","San Felipe","Valparaíso")
var opt_6 = new Array("Cachapoal","Cardenal caro", "Colchagua")
var opt_7 = new Array("Cauquenes","Curicó","Linares", "Talca")
var opt_8 = new Array("Arauco","Biobío", "Concepción", "Ñuble")
var opt_9 = new Array("Cautín","Malleco")
var opt_10 = new Array("Chiloé","Llanquihue", "Osorno", "Palena")
var opt_11 = new Array("Aysén","Capitán Prat", "Coyhaique","General Carrera")
var opt_12 = new Array("Antártica Chilena","Magallanes", "Tierra del Fuego","Última Esperanza")
var opt_13 = new Array("Chacabuco","Cordillera", "Maipo","Melipilla","Santiago","Talagante")
var opt_14 = new Array("Ranco","Valdivia")
var opt_15 = new Array("Arica","Parinacota")

function cambia()
{
	var cosa;
	cosa=document.formulario.cosa[document.formulario.cosa.selectedIndex].value;

	if (cosa!=0) 
	{
		mis_opts=eval("opt_"+cosa)
		num_opts=mis_opts.length;
		document.formulario.opt.length=num_opts;

		for (i = 0; i < num_opts; i++) {
			document.formulario.opt.options[i].value=mis_opts[i];
			document.formulario.opt.options[i].text=mis_opts[i];
		}
	}
	else{
		document.formulario.opt.length=1;
		document.formulario.opt.options[0].value="-";
		document.formulario.opt.options[0].text="-";
	}
	document.formulario.opt.options[0].selected=true;

}


function validar(){		
			var correo=document.formulario.correo.value;
			if(/^[A-Z-a-z-0-9]+@+[A-Z-a-z-0-9]+.+[a-z]/.test(correo)){				
			}
			else{
				alert("correo incorrecto");
				document.formulario.correo.focus();
				return 0;
			}

			var rut;
			rut=document.formulario.run.value.length;
			if(rut==0){
				alert("Campo run es obligatorio");
				document.formulario.run.focus();
				return	0;	
			}
			else
			{
				if(rut!=12 && rut!=11){
					alert("Ingrese correctamente rut");
					document.formulario.run.focus();
					return	0;
				}			
			}

			if(document.formulario.nombre.value.length==0){
				alert("Campo de Nombre es obligatorio");
				document.formulario.nombre.focus();
				return 0;
			}
			else{
				if (document.formulario.nombre.value.split(" ").length>=2)
				{					
				}
				else
				{
					alert("Debe a lo menos ingresar nombre y apellido");
					document.formulario.nombre.focus();
					return 0;
				}
			}

			var cosa;
				cosa=document.formulario.cosa[document.formulario.cosa.selectedIndex].value;
			if(cosa==0){
				alert("seleccione region");
				document.formulario.cosa.focus();
				return	0;
			}

			if(isNaN(document.formulario.telefono.value)){
				alert("El telefono ingresado no es un número");
				document.formulario.telefono.focus();
				return false;
			}
				
			var nom=document.formulario.nombre.value.split(" ").length;
			var cor=document.formulario.correo.value.length;
			
			alert("Guardando");

			document.formulario.submit();
}

