# David Crespo, 2017
import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
import socket
class Manejador:
	def on_boton_buscar_clicked(self, *args):
		try:
			insertar_direccion(obtener_direccion(obtener_nombre()))
		except:
			insertar_direccion("Nombre no válido")
	def on_boton_salir_clicked(self, *args):
		Gtk.main_quit(*args)
def obtener_direccion(nombre_maquina):
	direccion = socket.gethostbyname(nombre_maquina)
	return direccion
def obtener_nombre():
	nombre = constructor.get_object("entrada_nombre")
	nombre = nombre.get_text()
	return nombre
def insertar_direccion(direccion):
	texto = constructor.get_object("entrada_ip")
	texto = texto.set_text(direccion)
constructor=Gtk.Builder()
constructor.add_from_file("hostbyname.glade")
constructor.connect_signals(Manejador())
ventana = constructor.get_object("ventana")
ventana.show_all()
Gtk.main()
