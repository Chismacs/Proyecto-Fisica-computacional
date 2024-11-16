{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "f8e6ab28-cc53-4913-85c1-e8a515c001cb",
   "metadata": {},
   "source": [
    "# **PROYECTO**
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
   "id": "07d2e763-d4d8-4ebf-8171-39b77ca4aa6c",
   "metadata": {},
   "outputs": [],
   "source": [
    "anchoPantalla=800 #Se crea una variable con el ancho de pantalla.\n",
    "altoPantalla=600 #Se crea una variable con el ancho de pantalla.\n",
    "\n",
    "#Se crea la pantalla del juego.\n",
    "pantalla=pygame.display.set_mode((anchoPantalla,altoPantalla))\n",
    "pygame.display.set_caption(\"Cosmic Defenders\")\n",
    "\n",
    "#Se ingresa la imagen de inicio en la pantalla.\n",
    "pantallaDeInicio=pygame.image.load(\"Inicio-PrimerNivel.png\").convert()\n",
    "pantallaDeInicio=pygame.transform.scale(pantallaDeInicio,(800,600))\n",
    "\n",
    "#Se ingresa el nombre del juego para mostrar en pantalla.\n",
    "fuenteTitulo=pygame.font.Font(\"Silkscreen-Bold.ttf\",50) \n",
    "textoTitulo=fuenteTitulo.render(\"Cosmic Defenders\",True,(0,0,0))\n",
    "textoRect1=textoTitulo.get_rect(center=(anchoPantalla // 2, altoPantalla // 6))\n",
    "\n",
    "#Se crea el botón de inicio del juego.\n",
    "fuenteBotones=pygame.font.Font(\"Silkscreen-Bold.ttf\",40)\n",
    "textoInicio=fuenteBotones.render(\"INICIO\", True, (255, 255, 255))\n",
    "textoRect2=textoInicio.get_rect(center=(anchoPantalla // 2, altoPantalla // 1.5))\n",
    "inicio=pygame.Rect(textoRect2.left-1,textoRect2.top-1,textoRect2.width+1,textoRect2.height+1)\n",
    "\n",
    "#Se crea el botón de ajustes del juego.\n",
    "textoAjustes=fuenteBotones.render(\"AJUSTES\", True, (255, 255, 255))\n",
    "textoRect3=textoAjustes.get_rect(center=(anchoPantalla // 2, altoPantalla // 1.3))\n",
    "ajustes=pygame.Rect(textoRect3.left-1,textoRect3.top-1,textoRect3.width+1,textoRect3.height+1)\n",
    "\n",
    "#Se hace un ciclo para ejecutar el juego.\n",
    "ejecucion = True #Variable para terminar la ejecución.\n",
    "while ejecucion:\n",
    "    for cerrarJuego in pygame.event.get():\n",
    "        if cerrarJuego.type == pygame.QUIT: #Si se presiona la salida de la pestaña de juego, se termina la ejecución.\n",
    "            ejecucion = False\n",
    "\n",
    "    #Se muestra la pantalla con la imagen de inicio, el nombre del juego y el botón de inicio y ajustes.\n",
    "    pantalla.blit(pantallaDeInicio, [0, 0])\n",
    "    pantalla.blit(textoTitulo,textoRect1)\n",
    "    \n",
    "    pygame.draw.rect(pantalla,(160,32,240),inicio)\n",
    "    pantalla.blit(textoInicio,textoRect2)\n",
    "    \n",
    "    pygame.draw.rect(pantalla,(160,32,240),ajustes)\n",
    "    pantalla.blit(textoAjustes,textoRect3)\n",
    "\n",
    "    pygame.display.flip()\n",
    "\n",
    "\n",
    "pygame.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dc796e9f-34b7-4229-95c3-fcedfa2ff6e2",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
