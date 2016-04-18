# -*- coding: utf-8 -*-
 
import telebot # Librería de la API del bot.
from telebot import types # Tipos para la API del bot.
import time # Librería para hacer que el programa que controla el bot no se acabe.
import random
import urllib2
import datetime
import token
import os
import commands
import sched
TOKEN = '' #Nuestro token del bot
s = sched.scheduler(time.time, time.sleep)
bot = telebot.TeleBot(TOKEN) # Creamos el objeto de nuestro bot.
#############################################
#Listener
def listener(messages): # Con esto, estamos definiendo una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'.
    for m in messages: # Por cada dato 'm' en el dato 'messages'
        cid = m.chat.id # Almacenaremos el ID de la conversación.
        if m.content_type == 'text':
            print "[" + str(cid) + "]: " + m.text # Y haremos que imprima algo parecido a esto -> [52033876]: /start
 
bot.set_update_listener(listener) # Así, le decimos al bot que utilice como función escuchadora nuestra función 'listener' declarada arriba.
#############################################
#Funciones
@bot.message_handler(commands=['ayuda']) 
def command_ayuda(m): 
    cid = m.chat.id 
    bot.send_message( cid, "Comandos Disponibles: /ayuda, /informacion, /notadecorte, /grados, /salidas, /menciones, /informatica, /software, /computadores, /salud, /masters, /asignaturas")

@bot.message_handler(commands=['salidas'])
def command_salidas(m):
	cid = m.chat.id
	salidas = 'Con cada grado las salidas son diferentes, si bien es obligatorio para todas saber inglés y muy recomendable saber otro idioma, como el alemán. Para mas información de las salidas laborales usa los comandos de cada grado'
	bot.send_message(cid, salidas)
@bot.message_handler(commands=['informacion'])
def command_informacion(m):
	cid = m.chat.id(m):
	info = 'Bot programado para la Jornada de Puertas Abiertas 2016 por Adrián Marín Portillo (Github: Mangu93)'
	bot.send_message(cid, info)

@bot.message_handler(commands=['asignaturas'])
def command_asignaturas(m):
	cid = m.chat.id
	asignaturas = 'Dudas típicas sobre asignaturas:\n ¿Hay muchas matemáticas? \n Si y no. En Informática/Computadores/Software hay 4 asignaturas obligatorias de matemáticas, pero luego los conceptos matemáticos que se usarán se repetirán y se machacaran en las asignaturas que se usen. En Salud se usarán los correspondientes a los campos de la medicina'
	saludmedicina = '¿Es Ing. de la Salud una alternativa a Medicina? \n No, es una ingeniería, con lo bueno y lo malo que tiene esto. Si deseabas entrar en Medicina, no te escogen, y entras en Salud de rebote, podrías encontrarte algo que no te gusta.'
	videojuegos = '¿Que puedo hacer si yo quiero hacer videojuegos? \n Si bien una ingeniería no es obligatoria, si da muchas bases (programación y matemáticas). Es recomendable que si te matriculas escojas las asignaturas optativas de Inteligencia Artificial para Videojuegos y la de Programación de Videojuegos, y luego entres en el Master Propio de Videojuegos que oferta la UMA (mas información usando el comando /masters)'
	teleco = 'Informática, Teleco...¿no es lo mismo? ¿No es mejor Teleco? \n No son lo mismo y no es mejor, pues los grados que se ofertan en esta Escuela son de distinta orientación que los de la Escuela de Telecomunicaciones, mas enfocados a los sistemas electrónicos, de Telecomunicaciones y ondas'
	programar = 'Yo solo quiero programar a tope, ¿necesito una ingeniería? \n No es necesaria, una FP puede valerte, y luego puedes volver a considerar hacer un grado'
	convalidaciones = 'Si me quiero cambiar de Informática a Software, ¿hay algún problema? \n No suele haberlo, porque las asignaturas de los 2 primeros años de Informática, Computadores y Software son comunes, pero por norma general no suele haber muchos problemas. Otra cosa que se puede hacer es que si no consigues entrar en Software, por ejemplo, que tiene mas nota, es intentar entrar en Informática y hacer los dos años comunes ahí, para luego pedir el cambio a Software'
	bot.send_message(cid, asignaturas)
	bot.send_message(cid, saludmedicina)
	bot.send_message(cid, videojuegos)
	bot.send_message(cid, teleco)
	bot.send_message(cid, programar)
	bot.send_message(cid, convalidaciones)
@bot.message_handler(commands=['notadecorte'])
def command_temp(m):
	cid = m.chat.id
	corte = 'La nota de corte el curso anterior fue de: 5.132 para 140 plazas en Informática, 5.160 para 65 plazas en Computadores, 7.417 para 65 plazas en Salud y 8.154 para 65 plazas en Software'
	bot.send_message(cid, corte)

@bot.message_handler(commands=['grados'])
def command_camara(m):
	cid = m.chat.id
	grados = 'En la ETSII se ofertan los Grados de Ingeniería Informática, de Computadores, de Software y de la Salud'
	bot.send_message(cid,grados)

@bot.message_handler(commands=['menciones'])
def command_speedtest(m):
	cid = m.chat.id
	menciones = 'En Informática existe las menciones de Computación (mas dedicadas al campo de la teoría informática), de Sistemas de Información (dedicada al diseño e implementación de sistemas robustos y eficaces) y la de Tecnologías de la Información (dedicada mas a la parte del desarrollo)'
	menciones_salud = 'En Salud están las menciones de Bioinformática (orientada al desarrollo de software especifico para temas de salud), de Biomédica (relacionado con el funcionamiento de la maquinaria médica) e Informática Clínica (administración de software e infraestructuras médicas)'
	bot.send_message(cid, menciones)
	bot.send_message(cid, menciones_salud)

@bot.message_handler(commands=['masters'])
def command_ping(m):
	cid = m.chat.id
	masters = 'Masters Oficiales: Master en Ingeniería Informática, para capacitarte como tal, y Master en Ingeniería del Software e Inteligencia Artificial, enfocado a la investigación en estas areas'
	bot.send_message(cid,masters)
	no_oficiales = 'Masters Propios (tienen enfoque en un area pero no son habilitantes de una profesión) ofertados: Master en Diseño/Programación/Diseño y Programación de Videojuegos y Master en Ingeniería Web'
	bot.send_message(cid,no_oficiales)  

@bot.message_handler(commands=['informatica'])
def command_temp(m):
    cid = m.chat.id
    informatica = 'En rasgos generales, el grado está enfocado a prepararte para poder desarrollar sistemas informáticos, gestionar la seguridad de sistemas, aplicaciones de todo tipo y gestionar proyectos de todo tipo. Luego con las menciones te especializas mas en una parte.Mas información sobre las menciones de Informática usando el comando /menciones'
    bot.send_message(cid, informatica)
@bot.message_handler(commands=['software'])
def command_temp(m):
    cid = m.chat.id
	software = 'Este grado está enfocado tanto a la creación como mantenimiento y pruebas de cualquier software. Junto a las bases necesarias para la obtención de requisitos (que quiere y que necesita el cliente), principios de modelado tanto conceptual como prácticos enfocados al software. También se manejan bases de datos, se le da gran importancia a calidad del código y la necesidad de unas interfaces amigables y de calidad. '
    bot.send_message(cid, software)
@bot.message_handler(commands=['computadores'])
def command_nmap(m):
	cid = m.chat.id
	computadores = 'En este grado se consiguen conocimientos más cercanos al nivel del computador, se tocan temas como la programación a bajo nivel, ensamblador en muchas ocasiones, como funciona realmente un computador en su interior y también otros aspectos relacionados con los dispositivos físicos de red, medios y protocolos de transmisión.'
	bot.send_message(cid,computadores)
@bot.message_handler(commands=['salud'])
def command_espacio(m):
    cid = m.chat.id
    salud = 'Este grado está diseñado para que las personas que realicen este grado tengan conocimientos suficientes para poder hacer como una especie de traductores entre los profesionales del mundo de la medicina, biología, etc. y los profesionales del mundo de la tecnología y también para ejercer como estos últimos.'
    bot.send_message(cid, salud)
#############################################
#Peticiones
bot.polling(none_stop=True) # Con esto, le decimos al bot que siga funcionando incluso si encuentra algun fallo.