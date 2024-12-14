{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "f8e6ab28-cc53-4913-85c1-e8a515c001cb",
   "metadata": {},
   "source": [
    "# **PROYECTO**"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0fc67673-6acf-4e1a-8bf1-9b0a05101576",
   "metadata": {},
   "source": [
    "## COSMIC DEFENDERS"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "98354230-baaf-49ab-bbb7-0e331154686c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "pygame 2.6.1 (SDL 2.28.4, Python 3.12.2)\n",
      "Hello from the pygame community. https://www.pygame.org/contribute.html\n"
     ]
    }
   ],
   "source": [
    "import pygame #Se importa la librería pygame con todas sus funciones.\n",
    "import random #Se importa la librería random para generación de eventos aleatorios.\n",
    "import time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "8a5df25b-1946-41e9-bc3f-9d6ba241cf94",
   "metadata": {},
   "outputs": [],
   "source": [
    "pygame.init() #Se inicia el constructor de pygame\n",
    "pygame.mixer.init() #Se inicia el constructor de sonido de pygame."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "7605d93b-05dd-4960-9f9d-0ad1927a03e6",
   "metadata": {},
   "outputs": [],
   "source": [
    anchoPantalla = 800  # Se crea una variable con el ancho de pantalla.
altoPantalla = 600   # Se crea una variable con el alto de pantalla.

# Se crea la pantalla del juego.
pantalla = pygame.display.set_mode((anchoPantalla, altoPantalla))
pygame.display.set_caption("Cosmic Defenders")

# Se ingresa la imagen de inicio en la pantalla.
pantallaDeInicio = pygame.image.load("Inicio-PrimerNivel.png").convert()
pantallaDeInicio = pygame.transform.scale(pantallaDeInicio, (800, 600))

# Se ingresa el nombre del juego para mostrar en pantalla.
fuenteTitulo = pygame.font.Font("Silkscreen-Bold.ttf", 50)
textoTitulo = fuenteTitulo.render("Cosmic Defenders", True, (0, 0, 0))
textoRect1 = textoTitulo.get_rect(center=(anchoPantalla // 2, altoPantalla // 6))

# Se crea el botón de inicio del juego.
fuenteBotones = pygame.font.Font("Silkscreen-Bold.ttf", 40)
textoInicio = fuenteBotones.render("INICIO", True, (255, 255, 255))
textoRect2 = textoInicio.get_rect(center=(anchoPantalla // 2, altoPantalla // 1.5))
inicio = pygame.Rect(textoRect2.left - 1, textoRect2.top - 1, textoRect2.width + 1, textoRect2.height + 1)

# Se crea el botón de ajustes del juego.
textoAjustes = fuenteBotones.render("AJUSTES", True, (255, 255, 255))
textoRect3 = textoAjustes.get_rect(center=(anchoPantalla // 2, altoPantalla // 1.3))
ajustes = pygame.Rect(textoRect3.left - 1, textoRect3.top - 1, textoRect3.width + 1, textoRect3.height + 1)

# Se crea la variable con el sonido de fondo.
musicaInicio=pygame.mixer.music.load("Himno Universidad de Santiago De Chile.mp3")
reproducirMusica=pygame.mixer.music.play(loops=1)
    
def pantallaAjustes():
    pantalla.fill((0, 0, 0))  # Llenamos la pantalla de negro
    fuenteAjustes = pygame.font.Font("Silkscreen-Bold.ttf", 50)
    textoMusica = fuenteAjustes.render("Musica", True, (255, 255, 255))
    textoRectMusica = textoMusica.get_rect(center=(anchoPantalla // 2, altoPantalla // 5))

    fuenteSonido = pygame.font.Font("Silkscreen-Bold.ttf", 50)
    textoSonido = fuenteSonido.render("Sonidos", True, (255, 255, 255))
    textoRectSonido = textoSonido.get_rect(center=(anchoPantalla // 2, altoPantalla // 2))

    fuenteSalir = pygame.font.Font("Silkscreen-Bold.ttf", 50)
    textoSalir = fuenteSalir.render("Salir", True, (255, 255, 255))
    textoRectSalir = textoSalir.get_rect(center=(anchoPantalla // 2, altoPantalla // 1.3))

    pantalla.blit(textoMusica, textoRectMusica)
    pantalla.blit(textoSonido, textoRectSonido)
    pantalla.blit(textoSalir, textoRectSalir)

    return textoRectSalir

# Se hace un ciclo para ejecutar el juego.
ejecucion = True  # Variable para terminar la ejecución.
ingresarAjustes = False #Variable para entrar a ajustes
while ejecucion:
    for opcionesJuego in pygame.event.get():
        if opcionesJuego.type == pygame.QUIT:  #Si se presiona la salida de la pestaña de juego, se termina la ejecución.
            ejecucion = False
        if opcionesJuego.type == pygame.MOUSEBUTTONDOWN:
            if ajustes.collidepoint(opcionesJuego.pos):  #Si se hace clic en el botón de ajustes
                ingresarAjustes = True  # Cambiamos a pantalla de ajustes

    if ingresarAjustes:
        pantallaAjustes()  #Mostramos la pantalla de ajustes
        pygame.display.update() # Se actualiza la pantalla
        salirAjustes=pantallaAjustes()
        for opcionesAjustes in pygame.event.get():
            if opcionesAjustes.type == pygame.QUIT:  #Si se presiona la salida de la pestaña de juego, se termina la ejecución.
                ejecucion = False
                
            if opcionesAjustes.type == pygame.MOUSEBUTTONDOWN:
                if salirAjustes.collidepoint(opcionesAjustes.pos):
                    ingresarAjustes=False
            
    if ingresarAjustes == False:
        # Si no estamos en ajustes, mostramos la pantalla inicial
        pantalla.blit(pantallaDeInicio, [0, 0])
        pantalla.blit(textoTitulo, textoRect1)

        pygame.draw.rect(pantalla, (160, 32, 240), inicio)  # Botón de INICIO
        pantalla.blit(textoInicio, textoRect2)

        pygame.draw.rect(pantalla, (160, 32, 240), ajustes)  # Botón de AJUSTES
        pantalla.blit(textoAjustes, textoRect3)

    pygame.display.flip()  #Actualizamos la pantalla

pygame.quit()
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
