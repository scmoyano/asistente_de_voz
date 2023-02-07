

import pywhatkit
import pyjokes
import webbrowser
import datetime
import wikipedia
import yfinance as yf
import pyttsx3
import speech_recognition as sr

#variables
id_v1 = "KEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0"
#escucha de microfono y comprender texto

def mostrar_audio_en_texto():
    r = sr.Recogniczer()


    #configuracion de microfono

    with sr.Microphone() as origen:

        #tiempo de espera
        r.pause_threshold = 0.8

        # informa comienzo
        print( "ya puedes hablar")

        #guardar el audio

        audio = r.listen(origen)

        try:
            #buscar en google

            pedido = r.recognize.google(audio, language = "es-ar")

            print("dijiste" + pedido)
        except sr.UnknownValueError:

            #prueba de que no comprendio lo que se requirio
            print("lo que dijo es incomprensible")

            # devolver error para reentrada de audo
            return "vuelva a intentarlo"

        except sr.RequestError: 

            #prueba de que no comprendio lo que se requirio
            print("imposible hacer lo que pide")

            # devolver error para reentrada de audo
            return "vuelva a intentarlo"
        
        except:

            #prueba de que no comprendio lo que se requirio
            print("algo salio mal")
            
            # devolver error para reentrada de audo
            return "vuelva a intentarlo"

# da voz al asistente
def hablar(mensaje):

    #iniciar engine pyttsx3

    engine = pyttsx3.init()
    engine.setProperty('voice', id_v1)

    #pronunciar mensaje


    engine.say(mensaje)

    engine.runAndWait()

def pedir_dia( ):

    #variable del dia hoy.
    dia_semanal = datetime.datetime.today()


    # dia actual  de la semana
    nombre_dia = dia_semanal.weekday()

    # generacion de un diccionario para el calendario
    calendario= {0: "lunes",
                 1: "martes",
                 2: "miercoles",                   
                 3: "jueves",
                 4 :"viernes",
                 5: "sabado",
                 6: "domingo"}
    
    # instrucciones para decir el dia
    hablar(f"hoy es el dia {calendario[nombre_dia]}" )

#lector de hora actual
def pedir_hora():
    #creacion de la variable tiempo y generacion del texto para lectura
    hora= datetime.datetime.now()
    hora_actual = f"Son las {hora.hour}horas  con {hora.minute} minutos y {hora.second} segundos"

    hablar(hora_actual)


def saludo_inicial():

    # crear variable condatos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'
    elif 6 <= hora.hour < 13:
        momento = 'Buen día'
    else:
        momento = 'Buenas tardes'

    # decir el saludo
    hablar(f'{momento}, dime en qué te puedo ayudar')

#funcion central

def responder_pedidos():

    #saludos
    saludo_inicial()

    #variable
    comenzar=True

    # loop de inicializacion
    while comenzar:

        #establecimiento de pedido

        pedido = mostrar_audio_en_texto().lower()
        #abrir youtube
        if "abrir youtube"  in pedido:
            hablar("abriendo su youtube")
            webbrowser.open('https://www.youtube.com/')
            continue
        #abrir navegador
        elif "abrir navegador" in pedido:
            hablar('abriendo su navegador predeterminado')
            webbrowser.open('https://www.google.com/')
            continue
        #responder el dia
        elif "que dia es hoy" in pedido:
            pedir_dia()
            continue
        #responder hora
        elif "que hora es" in pedido:
            pedir_hora()
            continue
        
        elif "busca en wikipedia" in pedido:
            hablar("estoy buscando")
            pedido = pedido.replace("busca en wikipedi", " ")
            wikipedia.set_lang("es")
            resultado = wikipedia.summary(pedido, sentenses=1)
            hablar("en wikipedia encontre la siguiente informacion")
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar('Ya mismo estoy en eso')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar('Esto es lo que he encontrado')
            continue
        elif 'reproducir' in pedido:
            hablar('Buena idea, ya comienzo a reproducirlo')
            pedido = pedido.replace('reproducir', '')
            pywhatkit.playonyt(pedido)
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple':'APPL',
                       'amazon':'AMZN',
                       'google':'GOOGL'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'La encontré, el precio de {accion} es {precio_actual}')
                continue
            except:
                hablar("Perdón pero no la he encontrado")
                continue
        #cerrar programa
        elif "cerrar asistente" or "cerrar programa" or "adios" or "chau" in pedido:
           hablar("adios me voy a dormir")
           break







    




