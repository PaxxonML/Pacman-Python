import pygame
from random import randrange

PACMAN_EXTRAPAC_WAV_FILEPATH = "resources/sound/pacman_extrapac.wav"

PACMAN_DEATH_WAV_FILEPATH = "resources/sound/pacman_death.wav"

PACMAN_CHOMP_WAV_FILEPATH = "resources/sound/pacman_chomp.wav"

PACMAN_BEGINNING_WAV_FILEPATH = "resources/sound/pacman_beginning.wav"

FONT_BIT_WONDER_TTF_FILEPATH = "resources/font/8-BIT WONDER.TTF"

# --- CONSTS
# -- Files
# - Pacman
# IMGS
PACMAN_1_IMG_FILEPATH = "resources/img/pacman/Pacman1.png"
PACMAN_2_IMG_FILEPATH = "resources/img/pacman/Pacman2.png"
PACMAN_3_IMG_FILEPATH = "resources/img/pacman/Pacman3.png"
PACMAN_4_IMG_FILEPATH = "resources/img/pacman/Pacman4.png"
PACMAN_5_IMG_FILEPATH = "resources/img/pacman/Pacman5.png"
# - Dot
# IMGS
DOT_IMG_FILEPATH = "resources/img/general/Dot.png"
# TXT
DOT_COORDS_FILEPATH = "resources/txt/dotcoords.txt"
# - Phantom
# IMGS
PHANTOM_A_IMG_FILEPATH = "resources/img/fantasmas/Fantasma1.png"
PHANTOM_B_IMG_FILEPATH = "resources/img/fantasmas/Fantasma2.png"
PHANTOM_C_IMG_FILEPATH = "resources/img/fantasmas/Fantasma3.png"
PHANTOM_D_IMG_FILEPATH = "resources/img/fantasmas/Fantasma4.png"
# -- Game
# - Display
DISPLAY_CAPTION = "'パックマン' by: Paco Murillo"
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
# - Colors
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
NEGRO = (0, 0, 0)
# - Gameplay
# Object Movement
movimiento = 2

# Pacman Imgs
imgsPacman = []  # Will hold Pacman Imgs resources
animationCounterPacman = 0  # Pacman animation special counter


def animationCounterPacmanTick(counter: int) -> int:
    """
    Counts 0 to 9 to change the image on the pacman Sprite object to simulate movement
    :param counter: iterates from [0,9]
    :return: counter+1 except when counter is 9 in this case returns 0
    """
    if counter == 9:
        return 0
    return counter + 1


def loadPacmanImgs():
    """
    Loads Pacman images into imgsPacman (list[pygame.Surface])
    """
    imgsPacman.append(pygame.image.load(PACMAN_1_IMG_FILEPATH))
    imgsPacman.append(pygame.image.load(PACMAN_2_IMG_FILEPATH))
    imgsPacman.append(pygame.image.load(PACMAN_3_IMG_FILEPATH))
    imgsPacman.append(pygame.image.load(PACMAN_4_IMG_FILEPATH))
    imgsPacman.append(pygame.image.load(PACMAN_5_IMG_FILEPATH))


def animarPacman(animationCounter):
    imgPacman = imgsPacman[animationCounter // 2]

    return imgPacman


def movimientoPacman(pacman, direccion):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:  # and pacman.rect.left+30 < 795:
        direccion = 4

    elif keys[pygame.K_LEFT]:  # and 5 < pacman.rect.left:
        direccion = 2

    elif keys[pygame.K_DOWN]:  # and 595 > pacman.rect.top+30:
        direccion = 3

    elif keys[pygame.K_UP]:  # and 105 < pacman.rect.top:
        direccion = 1

    elif keys[pygame.K_SPACE]:
        direccion = 0

    if direccion == 4 and pacman.rect.left + pacman.rect.width < 795:  # Derecha
        if (not (130 < pacman.rect.top < 562)) or (162 < pacman.rect.top < 171 and (44 <= pacman.rect.left < 724)) or (
                524 < pacman.rect.top < 532 and (44 <= pacman.rect.left < 724)) or (
                202 < pacman.rect.top < 211 and (86 <= pacman.rect.left < 683)) or (
                482 < pacman.rect.top < 491 and (86 <= pacman.rect.left < 683)) or (
                242 < pacman.rect.top < 251 and (129 <= pacman.rect.left < 641)) or (
                442 < pacman.rect.top < 451 and (129 <= pacman.rect.left < 641)) or (
                402 < pacman.rect.top < 411 and (170 <= pacman.rect.left < 599)) or (
                282 < pacman.rect.top < 291 and (170 <= pacman.rect.left < 599)) or (
                322 < pacman.rect.top < 331 and (129 <= pacman.rect.left < 641)) or ((
                                                                                             131 < pacman.rect.top < 163 or 212 < pacman.rect.top < 244 or 292 < pacman.rect.top < 324 or 452 < pacman.rect.top < 484 or 532 < pacman.rect.top < 564) and (
                                                                                             379 <= pacman.rect.left < 388)):
            pacman.rect.left += movimiento
        elif (127 <= pacman.rect.top <= 130 or 562 <= pacman.rect.top <= 565) and (6 <= pacman.rect.left < 764):
            pacman.rect.left += movimiento
        elif 322 < pacman.rect.top < 331 and (
                44 <= pacman.rect.left < 95 or 128 <= pacman.rect.left < 641 or 675 <= pacman.rect.left < 724):
            pacman.rect.left += movimiento

    elif direccion == 2:  # Izquierda
        pacman.image = pygame.transform.flip(pacman.image, True, False)
        if (162 < pacman.rect.top < 171 and (45 < pacman.rect.left <= 725)) or (
                524 < pacman.rect.top < 532 and (45 < pacman.rect.left <= 725)) or (
                202 < pacman.rect.top < 211 and (87 < pacman.rect.left <= 684)) or (
                482 < pacman.rect.top < 491 and (87 < pacman.rect.left <= 684)) or (
                242 < pacman.rect.top < 251 and (130 < pacman.rect.left <= 642)) or (
                442 < pacman.rect.top < 451 and (130 < pacman.rect.left <= 642)) or (
                402 < pacman.rect.top < 411 and (171 < pacman.rect.left <= 600)) or (
                282 < pacman.rect.top < 291 and (171 < pacman.rect.left <= 600)) or (
                322 < pacman.rect.top < 331 and (130 < pacman.rect.left <= 642)) or ((
                                                                                             131 < pacman.rect.top < 163 or 212 < pacman.rect.top < 244 or 292 < pacman.rect.top < 324 or 452 < pacman.rect.top < 484 or 532 < pacman.rect.top < 564) and (
                                                                                             380 < pacman.rect.left <= 389)):
            pacman.rect.left -= movimiento
        elif (127 <= pacman.rect.top <= 130 or 562 <= pacman.rect.top <= 565) and (7 < pacman.rect.left <= 765):
            pacman.rect.left -= movimiento
        elif 322 < pacman.rect.top < 331 and (
                45 < pacman.rect.left <= 96 or 129 < pacman.rect.left <= 642 or 676 < pacman.rect.left <= 725):
            pacman.rect.left -= movimiento

    elif direccion == 3:  # Abajo
        pacman.image = pygame.transform.rotate(pacman.image, -90)
        if (126 <= pacman.rect.top < 564 and (759 <= pacman.rect.left <= 765 or 6 <= pacman.rect.left <= 12)) or (
                164 <= pacman.rect.top < 530 and (45 <= pacman.rect.left <= 53 or 717 <= pacman.rect.left <= 725)) or (
                204 <= pacman.rect.top < 488 and (87 <= pacman.rect.left <= 95 or 675 <= pacman.rect.left <= 683)) or (
                244 <= pacman.rect.top < 448 and (
                129 <= pacman.rect.left <= 137 or 633 <= pacman.rect.left <= 641)) or (
                284 <= pacman.rect.top < 408 and (
                171 <= pacman.rect.left <= 179 or 591 <= pacman.rect.left <= 599)) or (
                379 <= pacman.rect.left <= 389 and (
                525 <= pacman.rect.top < 564 or 126 <= pacman.rect.top < 168 or 205 <= pacman.rect.top < 247 or 284 <= pacman.rect.top < 326 or 444 <= pacman.rect.top < 488)):
            pacman.rect.top += movimiento

    elif direccion == 1:  # Arriba
        pacman.image = pygame.transform.rotate(pacman.image, 90)
        if (128 < pacman.rect.top <= 565 and (759 <= pacman.rect.left <= 765 or 6 <= pacman.rect.left <= 12)) or (
                165 < pacman.rect.top <= 531 and (45 <= pacman.rect.left <= 53 or 717 <= pacman.rect.left <= 725)) or (
                205 < pacman.rect.top <= 489 and (87 <= pacman.rect.left <= 95 or 675 <= pacman.rect.left <= 683)) or (
                245 < pacman.rect.top <= 449 and (
                129 <= pacman.rect.left <= 137 or 633 <= pacman.rect.left <= 641)) or (
                285 < pacman.rect.top <= 409 and (
                171 <= pacman.rect.left <= 179 or 591 <= pacman.rect.left <= 599)) or (
                379 <= pacman.rect.left <= 389 and (
                526 < pacman.rect.top <= 565 or 127 < pacman.rect.top <= 169 or 206 < pacman.rect.top <= 248 or 285 < pacman.rect.top <= 327 or 445 < pacman.rect.top <= 489)):
            pacman.rect.top -= movimiento

    elif direccion == 0:
        pacman.rect.left += 0
        pacman.rect.top += 0

    return pacman, direccion


def mapa(ventana):
    randBlue = randrange(100, 255)
    # Lineas Externas
    # Horizontales
    pygame.draw.line(ventana, (0, 0, randBlue), (0, 120), (799, 120), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (799, 599), (0, 599), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (3, 123), (796, 123), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (796, 596), (3, 596), 2)
    # Verticales
    # Derecha
    pygame.draw.line(ventana, (0, 0, randBlue), (798, 120), (798, 599), 2)
    # pygame.draw.line(ventana, (0, 0, 0), (798, 325), (798, 375), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (795, 123), (795, 596), 2)
    # pygame.draw.line(ventana, (0, 0, 0), (795, 325), (795, 375), 2)
    # Izquierda
    pygame.draw.line(ventana, (0, 0, randBlue), (0, 120), (0, 599), 2)
    # pygame.draw.line(ventana, (0, 0, 0), (0, 325), (0, 375), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (3, 123), (3, 596), 2)
    # pygame.draw.line(ventana, (0, 0, 0), (3, 325), (3, 375), 2)

    # Líneas internas
    # pygame.draw.line(ventana, (0, 0, randBlue), (,), (,), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (42, 161), (42, 561), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (756, 161), (756, 561), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (42, 161), (378, 161), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (420, 161), (756, 161), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (42, 561), (378, 561), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (420, 561), (756, 561), 2)

    pygame.draw.line(ventana, (0, 0, randBlue), (84, 201), (84, 321), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (84, 361), (84, 521), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (714, 201), (714, 321), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (714, 361), (714, 521), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (84, 201), (714, 201), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (84, 521), (714, 521), 2)

    pygame.draw.line(ventana, (0, 0, randBlue), (126, 241), (126, 481), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (672, 241), (672, 481), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (126, 241), (378, 241), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (420, 241), (672, 241), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (126, 481), (378, 481), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (420, 481), (672, 481), 2)

    pygame.draw.line(ventana, (0, 0, randBlue), (168, 281), (168, 321), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (168, 361), (168, 441), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (630, 281), (630, 321), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (630, 361), (630, 441), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (168, 281), (630, 281), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (168, 441), (630, 441), 2)

    pygame.draw.line(ventana, (0, 0, randBlue), (210, 321), (378, 321), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (420, 321), (588, 321), 2)

    # Caja de fantasmas

    pygame.draw.line(ventana, (0, 0, randBlue), (210, 361), (588, 361), 2)
    pygame.draw.line(ventana, (randBlue, randBlue, randBlue), (378, 361), (420, 361), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (210, 401), (588, 401), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (210, 361), (210, 401), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (588, 361), (588, 401), 2)


def renderScoreTitle(Font):
    return Font.render("SCORE", False, BLANCO)


def renderScore(Font, score):
    return Font.render("%04d" % score, False, BLANCO)


def loadDotCoords(filePath: str) -> list[list[int]]:
    """

    :param filePath: string filepath that states the coords having a coord per line separated by ',' (single comma)
    :return:
    :rtype: list[list[int]]
    """
    dotCoords = []
    file = open(filePath, "r", encoding="UTF-8")
    line = file.readline()
    while line != "":
        strCoords = line.split(",")
        dotCoords.append([int(strCoords[0]), int(strCoords[1])])
        line = file.readline()
    return dotCoords


def crearDots(listaDots, imgDot, dotCoordList: list[list[int]]):
    for [x, y] in dotCoordList:
        dot = pygame.sprite.Sprite()
        dot.image = imgDot
        dot.rect = imgDot.get_rect()
        dot.rect.left = x
        dot.rect.top = y
        listaDots.append(dot)


def dibujarDots(ventana, listaDots):
    for dot in listaDots:
        ventana.blit(dot.image, dot.rect)


def checaPuntaje(pacman, listaDots, copiaLista):
    copiaLista = listaDots[:]
    xPac = pacman.rect.left
    yPac = pacman.rect.top
    x2Pac = pacman.rect.left + pacman.rect.width
    y2Pac = pacman.rect.top + pacman.rect.height
    for dot in range(-1, -len(listaDots) - 1, -1):
        xDot = listaDots[dot].rect.left
        yDot = listaDots[dot].rect.top
        if xPac < xDot < x2Pac and yPac < yDot < y2Pac:
            listaDots.remove(listaDots[dot])
            return 10
    return 0


def movimientoFantasmas(phantoms, ticks) -> list[list[pygame.sprite.Sprite, int]]:
    fanA = phantoms[0][0]
    fanB = phantoms[1][0]
    fanC = phantoms[2][0]
    fanD = phantoms[3][0]
    if fanA.rect.left < 385:
        fanA.rect.left += movimiento
    if ticks >= 180:
        if fanB.rect.left > 385:
            fanB.rect.left -= movimiento
    if ticks >= 360:
        if fanC.rect.left < 385:
            fanC.rect.left += movimiento
    if ticks >= 540:
        if fanD.rect.left > 385:
            fanD.rect.left -= movimiento
    ticks += 1
    return [[fanA, phantoms[0][1]], [fanB, phantoms[1][1]], [fanC, phantoms[2][1]], [fanD, phantoms[3][1]]]


def selectPhantomRandomDirection(phantoms: list[tuple[pygame.sprite.Sprite, int]]):
    for index in range(len(phantoms)):
        phantom = phantoms[index][0]
        selectedPhantomRandomDirection = phantoms[index][1]
        if phantom.rect.left == 385 and phantom.rect.top == 325:
            selectedPhantomRandomDirection = randrange(1, 5)
        elif phantom.rect.left == 385 and phantom.rect.top == 285:
            selectedPhantomRandomDirection = randrange(1, 5)
        elif phantom.rect.left == 385 and phantom.rect.top == 245:
            selectedPhantomRandomDirection = randrange(1, 5)
        elif phantom.rect.left == 385 and phantom.rect.top == 205:
            selectedPhantomRandomDirection = randrange(1, 5)
        elif phantom.rect.left == 385 and phantom.rect.top == 165:
            selectedPhantomRandomDirection = randrange(1, 5)
        elif phantom.rect.left == 385 and phantom.rect.top == 125:
            selectedPhantomRandomDirection = randrange(1, 5)
        elif phantom.rect.left == 385 and phantom.rect.top == 445:
            selectedPhantomRandomDirection = randrange(1, 5)
        elif phantom.rect.left == 385 and phantom.rect.top == 485:
            selectedPhantomRandomDirection = randrange(1, 5)
        elif phantom.rect.left == 385 and phantom.rect.top == 525:
            selectedPhantomRandomDirection = randrange(1, 5)
        elif phantom.rect.left == 385 and phantom.rect.top == 565:
            selectedPhantomRandomDirection = randrange(1, 5)
        elif phantom.rect.left == 3 and phantom.rect.top == 125:
            selectedPhantomRandomDirection = randrange(1, 5)
        elif phantom.rect.left == 3 and phantom.rect.top == 565:
            selectedPhantomRandomDirection = randrange(1, 5)
        elif phantom.rect.left == 767 and phantom.rect.top == 125:
            selectedPhantomRandomDirection = randrange(1, 5)
        elif phantom.rect.left == 767 and phantom.rect.top == 565:
            selectedPhantomRandomDirection = randrange(1, 5)
        elif phantom.rect.left == 45 and phantom.rect.top == 165:
            selectedPhantomRandomDirection = randrange(1, 5)
        elif phantom.rect.left == 45 and phantom.rect.top == 325:
            selectedPhantomRandomDirection = randrange(1, 5)
        elif phantom.rect.left == 45 and phantom.rect.top == 525:
            selectedPhantomRandomDirection = randrange(1, 5)
        elif phantom.rect.left == 725 and phantom.rect.top == 165:
            selectedPhantomRandomDirection = randrange(1, 5)
        elif phantom.rect.left == 725 and phantom.rect.top == 325:
            selectedPhantomRandomDirection = randrange(1, 5)
        elif phantom.rect.left == 725 and phantom.rect.top == 525:
            selectedPhantomRandomDirection = randrange(1, 5)
        elif phantom.rect.left == 87 and phantom.rect.top == 205:
            selectedPhantomRandomDirection = randrange(1, 5)
        elif phantom.rect.left == 87 and phantom.rect.top == 325:
            selectedPhantomRandomDirection = randrange(1, 5)
        elif phantom.rect.left == 87 and phantom.rect.top == 485:
            selectedPhantomRandomDirection = randrange(1, 5)
        elif phantom.rect.left == 683 and phantom.rect.top == 205:
            selectedPhantomRandomDirection = randrange(1, 5)
        elif phantom.rect.left == 683 and phantom.rect.top == 325:
            selectedPhantomRandomDirection = randrange(1, 5)
        elif phantom.rect.left == 683 and phantom.rect.top == 485:
            selectedPhantomRandomDirection = randrange(1, 5)
        elif phantom.rect.left == 129 and phantom.rect.top == 245:
            selectedPhantomRandomDirection = randrange(1, 5)
        elif phantom.rect.left == 129 and phantom.rect.top == 325:
            selectedPhantomRandomDirection = randrange(1, 5)
        elif phantom.rect.left == 129 and phantom.rect.top == 445:
            selectedPhantomRandomDirection = randrange(1, 5)
        elif phantom.rect.left == 641 and phantom.rect.top == 245:
            selectedPhantomRandomDirection = randrange(1, 5)
        elif phantom.rect.left == 641 and phantom.rect.top == 325:
            selectedPhantomRandomDirection = randrange(1, 5)
        elif phantom.rect.left == 641 and phantom.rect.top == 445:
            selectedPhantomRandomDirection = randrange(1, 5)
        elif phantom.rect.left == 171 and phantom.rect.top == 285:
            selectedPhantomRandomDirection = randrange(1, 5)
        elif phantom.rect.left == 171 and phantom.rect.top == 325:
            selectedPhantomRandomDirection = randrange(1, 5)
        elif phantom.rect.left == 171 and phantom.rect.top == 405:
            selectedPhantomRandomDirection = randrange(1, 5)
        elif phantom.rect.left == 599 and phantom.rect.top == 285:
            selectedPhantomRandomDirection = randrange(1, 5)
        elif phantom.rect.left == 599 and phantom.rect.top == 325:
            selectedPhantomRandomDirection = randrange(1, 5)
        elif phantom.rect.left == 599 and phantom.rect.top == 405:
            selectedPhantomRandomDirection = randrange(1, 5)
        phantoms[index] = (phantom, selectedPhantomRandomDirection)


def initPhantomMovement(phantoms: list[tuple[pygame.sprite.Sprite, int]]):
    phantomA = phantoms[0][0]
    phantomARandomDirection = phantoms[0][1]
    if phantomA.rect.left == 385 and 325 < phantomA.rect.top == 365:
        phantomA.rect.top -= movimiento
        phantomARandomDirection = 1  # phantom A Random Direction
    phantomB = phantoms[1][0]
    phantomBRandomDirection = phantoms[1][1]
    if phantomB.rect.left == 385 and 325 < phantomB.rect.top == 365:
        phantomB.rect.top -= movimiento
        phantomBRandomDirection = 1  # phantom B Random Direction
    phantomC = phantoms[2][0]
    phantomCRandomDirection = phantoms[2][1]
    if phantomC.rect.left == 385 and 325 < phantomC.rect.top == 365:
        phantomC.rect.top -= movimiento
        phantomCRandomDirection = 1  # phantom C Random Direction
    phantomD = phantoms[3][0]
    phantomDRandomDirection = phantoms[3][1]
    if phantomD.rect.left == 385 and 325 < phantomD.rect.top == 365:
        phantomD.rect.top -= movimiento
        phantomDRandomDirection = 1  # phantom D Random Direction
    phantoms[0] = (phantomA, phantomARandomDirection)
    phantoms[1] = (phantomB, phantomBRandomDirection)
    phantoms[2] = (phantomC, phantomCRandomDirection)
    phantoms[3] = (phantomD, phantomDRandomDirection)


def movePhantoms(phantoms):
    for index in range(len(phantoms)):
        phantom = phantoms[index][0]
        phantomRandomDirection = phantoms[index][1]
        if 129 < phantom.rect.left < 385 and 285 < phantom.rect.top < 405:
            if phantomRandomDirection == 1:
                phantom.rect.top -= movimiento
            elif phantomRandomDirection == 2:
                phantom.rect.left -= movimiento
            elif phantomRandomDirection == 3:
                phantom.rect.top += movimiento
            elif phantomRandomDirection == 4:
                phantom.rect.left += movimiento
        elif 385 < phantom.rect.left < 641 and 285 < phantom.rect.top < 405:
            if phantomRandomDirection == 1:
                phantom.rect.top -= movimiento
            elif phantomRandomDirection == 2:
                phantom.rect.left -= movimiento
            elif phantomRandomDirection == 3:
                phantom.rect.top += movimiento
            elif phantomRandomDirection == 4:
                phantom.rect.left += movimiento
        elif 171 < phantom.rect.left < 599 and 285 < phantom.rect.top <= 365:
            if phantomRandomDirection == 1:
                phantom.rect.top -= movimiento
            elif phantomRandomDirection == 2:
                phantom.rect.left -= movimiento
            elif phantomRandomDirection == 4:
                phantom.rect.left += movimiento
            if phantom.rect.left != 325:
                if phantomRandomDirection == 3:
                    phantom.rect.top += movimiento
        elif 171 < phantom.rect.left < 599 and 285 <= phantom.rect.top < 325:
            if phantomRandomDirection == 2:
                phantom.rect.left -= movimiento
            elif phantomRandomDirection == 3:
                phantom.rect.top += movimiento
            elif phantomRandomDirection == 4:
                phantom.rect.left += movimiento
            elif phantom.rect.left != 385 and phantom.rect.top != 285:
                if phantomRandomDirection == 1:
                    phantom.rect.top -= movimiento
        elif 171 <= phantom.rect.left < 385 and 285 <= phantom.rect.top < 325:
            if phantomRandomDirection == 3:
                phantom.rect.top += movimiento
            elif phantomRandomDirection == 4:
                phantom.rect.left += movimiento
            elif phantom.rect.left != 171 and phantom.rect.top != 285:
                if phantomRandomDirection == 1:
                    phantom.rect.top -= movimiento
                elif phantomRandomDirection == 2:
                    phantom.rect.left -= movimiento
        elif 171 < phantom.rect.left <= 599 and 325 < phantom.rect.top <= 405:
            if phantomRandomDirection == 1:
                phantom.rect.top -= movimiento
            elif phantomRandomDirection == 2:
                phantom.rect.left -= movimiento
            elif phantom.rect.left != 599 and phantom.rect.top != 405:
                if phantomRandomDirection == 3:
                    phantom.rect.top += movimiento
                elif phantomRandomDirection == 4:
                    phantom.rect.left += movimiento
        elif 171 <= phantom.rect.left < 599 and 325 < phantom.rect.top <= 405:
            if phantomRandomDirection == 1:
                phantom.rect.top -= movimiento
            elif phantomRandomDirection == 4:
                phantom.rect.left += movimiento
            elif phantom.rect.left != 171 and phantom.rect.top != 405:
                if phantomRandomDirection == 3:
                    phantom.rect.top += movimiento
                elif phantomRandomDirection == 2:
                    phantom.rect.left -= movimiento
        elif 129 <= phantom.rect.left < 385 and 285 <= phantom.rect.top < 325:
            if phantomRandomDirection == 3:
                phantom.rect.top += movimiento
            elif phantomRandomDirection == 4:
                phantom.rect.left += movimiento
            elif phantom.rect.left != 129 and phantom.rect.top != 285:
                if phantomRandomDirection == 1:
                    phantom.rect.top -= movimiento
                elif phantomRandomDirection == 2:
                    phantom.rect.left -= movimiento
        elif 87 <= phantom.rect.left < 385 and 205 <= phantom.rect.top < 325:
            if phantomRandomDirection == 3:
                phantom.rect.top += movimiento
            elif phantomRandomDirection == 4:
                phantom.rect.left += movimiento
            elif phantom.rect.left != 87 and phantom.rect.top != 205:
                if phantomRandomDirection == 1:
                    phantom.rect.top -= movimiento
                elif phantomRandomDirection == 2:
                    phantom.rect.left -= movimiento
        elif 45 <= phantom.rect.left < 385 and 165 <= phantom.rect.top < 325:
            if phantomRandomDirection == 3:
                phantom.rect.top += movimiento
            elif phantomRandomDirection == 4:
                phantom.rect.left += movimiento
            elif phantom.rect.left != 45 and phantom.rect.top != 165:
                if phantomRandomDirection == 1:
                    phantom.rect.top -= movimiento
                elif phantomRandomDirection == 2:
                    phantom.rect.left -= movimiento
        elif 3 <= phantom.rect.left < 385 and 125 <= phantom.rect.top < 325:
            if phantomRandomDirection == 3:
                phantom.rect.top += movimiento
            elif phantomRandomDirection == 4:
                phantom.rect.left += movimiento
            elif phantom.rect.left != 3 and phantom.rect.top != 125:
                if phantomRandomDirection == 1:
                    phantom.rect.top -= movimiento
                elif phantomRandomDirection == 2:
                    phantom.rect.left -= movimiento
        elif 129 <= phantom.rect.left < 385 and 325 < phantom.rect.top <= 445:
            if phantomRandomDirection == 1:
                phantom.rect.top -= movimiento
            elif phantomRandomDirection == 4:
                phantom.rect.left += movimiento
            elif phantom.rect.left != 129 and phantom.rect.top != 445:
                if phantomRandomDirection == 3:
                    phantom.rect.top += movimiento
                elif phantomRandomDirection == 2:
                    phantom.rect.left -= movimiento
        elif 87 <= phantom.rect.left < 385 and 325 < phantom.rect.top <= 485:
            if phantomRandomDirection == 1:
                phantom.rect.top -= movimiento
            elif phantomRandomDirection == 4:
                phantom.rect.left += movimiento
            elif phantom.rect.left != 87 and phantom.rect.top != 485:
                if phantomRandomDirection == 3:
                    phantom.rect.top += movimiento
                elif phantomRandomDirection == 2:
                    phantom.rect.left -= movimiento
        elif 45 <= phantom.rect.left < 385 and 325 < phantom.rect.top <= 525:
            if phantomRandomDirection == 1:
                phantom.rect.top -= movimiento
            elif phantomRandomDirection == 4:
                phantom.rect.left += movimiento
            elif phantom.rect.left != 45 and phantom.rect.top != 525:
                if phantomRandomDirection == 3:
                    phantom.rect.top += movimiento
                elif phantomRandomDirection == 2:
                    phantom.rect.left -= movimiento
        elif 3 <= phantom.rect.left < 385 and 325 < phantom.rect.top <= 565:
            if phantomRandomDirection == 1:
                phantom.rect.top -= movimiento
            elif phantomRandomDirection == 4:
                phantom.rect.left += movimiento
            elif phantom.rect.left != 3 and phantom.rect.top != 565:
                if phantomRandomDirection == 3:
                    phantom.rect.top += movimiento
                elif phantomRandomDirection == 2:
                    phantom.rect.left -= movimiento
        elif 385 < phantom.rect.left <= 641 and 325 < phantom.rect.top <= 445:
            if phantomRandomDirection == 1:
                phantom.rect.top -= movimiento
            elif phantomRandomDirection == 2:
                phantom.rect.left -= movimiento
            elif phantom.rect.left != 641 and phantom.rect.top != 445:
                if phantomRandomDirection == 3:
                    phantom.rect.top += movimiento
                elif phantomRandomDirection == 4:
                    phantom.rect.left += movimiento
        elif 385 < phantom.rect.left <= 683 and 325 < phantom.rect.top <= 485:
            if phantomRandomDirection == 1:
                phantom.rect.top -= movimiento
            elif phantomRandomDirection == 2:
                phantom.rect.left -= movimiento
            elif phantom.rect.left != 683 and phantom.rect.top != 485:
                if phantomRandomDirection == 3:
                    phantom.rect.top += movimiento
                elif phantomRandomDirection == 4:
                    phantom.rect.left += movimiento
        elif 385 < phantom.rect.left <= 725 and 325 < phantom.rect.top <= 525:
            if phantomRandomDirection == 1:
                phantom.rect.top -= movimiento
            elif phantomRandomDirection == 2:
                phantom.rect.left -= movimiento
            elif phantom.rect.left != 725 and phantom.rect.top != 525:
                if phantomRandomDirection == 3:
                    phantom.rect.top += movimiento
                elif phantomRandomDirection == 4:
                    phantom.rect.left += movimiento
        elif 385 < phantom.rect.left <= 767 and 325 < phantom.rect.top <= 565:
            if phantomRandomDirection == 1:
                phantom.rect.top -= movimiento
            elif phantomRandomDirection == 2:
                phantom.rect.left -= movimiento
            elif phantom.rect.left != 767 and phantom.rect.top != 565:
                if phantomRandomDirection == 3:
                    phantom.rect.top += movimiento
                elif phantomRandomDirection == 4:
                    phantom.rect.left += movimiento
        elif 385 < phantom.rect.left <= 599 and 285 <= phantom.rect.top < 325:
            if phantomRandomDirection == 2:
                phantom.rect.left -= movimiento
            elif phantomRandomDirection == 3:
                phantom.rect.top += movimiento
            elif phantom.rect.left != 599 and phantom.rect.top != 285:
                if phantomRandomDirection == 1:
                    phantom.rect.top -= movimiento
                elif phantomRandomDirection == 4:
                    phantom.rect.left += movimiento
        elif 385 < phantom.rect.left <= 641 and 245 <= phantom.rect.top < 325:
            if phantomRandomDirection == 2:
                phantom.rect.left -= movimiento
            elif phantomRandomDirection == 3:
                phantom.rect.top += movimiento
            elif phantom.rect.left != 641 and phantom.rect.top != 245:
                if phantomRandomDirection == 1:
                    phantom.rect.top -= movimiento
                elif phantomRandomDirection == 4:
                    phantom.rect.left += movimiento
        elif 385 < phantom.rect.left <= 683 and 205 <= phantom.rect.top < 325:
            if phantomRandomDirection == 2:
                phantom.rect.left -= movimiento
            elif phantomRandomDirection == 3:
                phantom.rect.top += movimiento
            elif phantom.rect.left != 683 and phantom.rect.top != 205:
                if phantomRandomDirection == 1:
                    phantom.rect.top -= movimiento
                elif phantomRandomDirection == 4:
                    phantom.rect.left += movimiento
        elif 385 < phantom.rect.left <= 725 and 165 <= phantom.rect.top < 325:
            if phantomRandomDirection == 2:
                phantom.rect.left -= movimiento
            elif phantomRandomDirection == 3:
                phantom.rect.top += movimiento
            elif phantom.rect.left != 725 and phantom.rect.top != 165:
                if phantomRandomDirection == 1:
                    phantom.rect.top -= movimiento
                elif phantomRandomDirection == 4:
                    phantom.rect.left += movimiento
        elif 385 < phantom.rect.left <= 767 and 125 <= phantom.rect.top < 325:
            if phantomRandomDirection == 2:
                phantom.rect.left -= movimiento
            elif phantomRandomDirection == 3:
                phantom.rect.top += movimiento
            elif phantom.rect.left != 767 and phantom.rect.top != 125:
                if phantomRandomDirection == 1:
                    phantom.rect.top -= movimiento
                elif phantomRandomDirection == 4:
                    phantom.rect.left += movimiento
        elif 45 <= phantom.rect.left < 87 and 165 < phantom.rect.top < 525:
            if phantomRandomDirection == 1:
                phantom.rect.top -= movimiento
            elif phantomRandomDirection == 3:
                phantom.rect.top += movimiento
            elif phantomRandomDirection == 4:
                phantom.rect.left += movimiento
            elif phantom.rect.left != 45:
                if phantomRandomDirection == 2:
                    phantom.rect.left -= movimiento
        elif 129 <= phantom.rect.left < 171 and 245 < phantom.rect.top < 445:
            if phantomRandomDirection == 1:
                phantom.rect.top -= movimiento
            elif phantomRandomDirection == 3:
                phantom.rect.top += movimiento
            elif phantomRandomDirection == 4:
                phantom.rect.left += movimiento
            elif phantom.rect.left != 129:
                if phantomRandomDirection == 2:
                    phantom.rect.left -= movimiento
        elif 683 <= phantom.rect.left < 725 and 205 < phantom.rect.top < 485:
            if phantomRandomDirection == 1:
                phantom.rect.top -= movimiento
            elif phantomRandomDirection == 3:
                phantom.rect.top += movimiento
            elif phantomRandomDirection == 4:
                phantom.rect.left += movimiento
            elif phantom.rect.left != 683:
                if phantomRandomDirection == 2:
                    phantom.rect.left -= movimiento
        elif 45 < phantom.rect.left <= 87 and 165 < phantom.rect.top < 525:
            if phantomRandomDirection == 1:
                phantom.rect.top -= movimiento
            elif phantomRandomDirection == 3:
                phantom.rect.top += movimiento
            elif phantomRandomDirection == 2:
                phantom.rect.left -= movimiento
            elif phantom.rect.left != 87:
                if phantomRandomDirection == 4:
                    phantom.rect.left += movimiento
        elif 599 < phantom.rect.left <= 641 and 245 < phantom.rect.top < 445:
            if phantomRandomDirection == 1:
                phantom.rect.top -= movimiento
            elif phantomRandomDirection == 3:
                phantom.rect.top += movimiento
            elif phantomRandomDirection == 2:
                phantom.rect.left -= movimiento
            elif phantom.rect.left != 641:
                if phantomRandomDirection == 4:
                    phantom.rect.left += movimiento
        elif 683 < phantom.rect.left <= 725 and 165 < phantom.rect.top < 525:
            if phantomRandomDirection == 1:
                phantom.rect.top -= movimiento
            elif phantomRandomDirection == 3:
                phantom.rect.top += movimiento
            elif phantomRandomDirection == 2:
                phantom.rect.left -= movimiento
            elif phantom.rect.left != 725:
                if phantomRandomDirection == 4:
                    phantom.rect.left += movimiento
        elif 3 < phantom.rect.left < 767 and 125 <= phantom.rect.top < 165:
            if phantomRandomDirection == 4:
                phantom.rect.left += movimiento
            elif phantomRandomDirection == 3:
                phantom.rect.top += movimiento
            elif phantomRandomDirection == 2:
                phantom.rect.left -= movimiento
            elif phantom.rect.top != 125:
                if phantomRandomDirection == 1:
                    phantom.rect.top -= movimiento
        elif 87 < phantom.rect.left < 683 and 205 <= phantom.rect.top < 245:
            if phantomRandomDirection == 4:
                phantom.rect.left += movimiento
            elif phantomRandomDirection == 3:
                phantom.rect.top += movimiento
            elif phantomRandomDirection == 2:
                phantom.rect.left -= movimiento
            elif phantom.rect.top != 205:
                if phantomRandomDirection == 1:
                    phantom.rect.top -= movimiento
        elif 3 < phantom.rect.left < 767 and 125 <= phantom.rect.top < 165:
            if phantomRandomDirection == 4:
                phantom.rect.left += movimiento
            elif phantomRandomDirection == 3:
                phantom.rect.top += movimiento
            elif phantomRandomDirection == 2:
                phantom.rect.left -= movimiento
            elif phantom.rect.top != 125:
                if phantomRandomDirection == 1:
                    phantom.rect.top -= movimiento
        elif 129 < phantom.rect.left < 641 and 445 <= phantom.rect.top < 485:
            if phantomRandomDirection == 4:
                phantom.rect.left += movimiento
            elif phantomRandomDirection == 3:
                phantom.rect.top += movimiento
            elif phantomRandomDirection == 2:
                phantom.rect.left -= movimiento
            elif phantom.rect.top != 445:
                if phantomRandomDirection == 1:
                    phantom.rect.top -= movimiento
        elif 45 < phantom.rect.left < 725 and 525 <= phantom.rect.top < 565:
            if phantomRandomDirection == 4:
                phantom.rect.left += movimiento
            elif phantomRandomDirection == 3:
                phantom.rect.top += movimiento
            elif phantomRandomDirection == 2:
                phantom.rect.left -= movimiento
            elif phantom.rect.top != 525:
                if phantomRandomDirection == 1:
                    phantom.rect.top -= movimiento
        elif 3 < phantom.rect.left < 767 and 525 < phantom.rect.top <= 565:
            if phantomRandomDirection == 4:
                phantom.rect.left += movimiento
            elif phantomRandomDirection == 1:
                phantom.rect.top -= movimiento
            elif phantomRandomDirection == 2:
                phantom.rect.left -= movimiento
            elif phantom.rect.top != 565:
                if phantomRandomDirection == 3:
                    phantom.rect.top += movimiento
        elif 87 < phantom.rect.left < 683 and 445 < phantom.rect.top <= 485:
            if phantomRandomDirection == 4:
                phantom.rect.left += movimiento
            elif phantomRandomDirection == 1:
                phantom.rect.top -= movimiento
            elif phantomRandomDirection == 2:
                phantom.rect.left -= movimiento
            elif phantom.rect.top != 485:
                if phantomRandomDirection == 3:
                    phantom.rect.top += movimiento
        elif 129 < phantom.rect.left < 641 and 205 < phantom.rect.top <= 245:
            if phantomRandomDirection == 4:
                phantom.rect.left += movimiento
            elif phantomRandomDirection == 1:
                phantom.rect.top -= movimiento
            elif phantomRandomDirection == 2:
                phantom.rect.left -= movimiento
            elif phantom.rect.top != 245:
                if phantomRandomDirection == 3:
                    phantom.rect.top += movimiento
        elif 45 < phantom.rect.left < 725 and 125 < phantom.rect.top <= 165:
            if phantomRandomDirection == 4:
                phantom.rect.left += movimiento
            elif phantomRandomDirection == 1:
                phantom.rect.top -= movimiento
            elif phantomRandomDirection == 2:
                phantom.rect.left -= movimiento
            elif phantom.rect.top != 165:
                if phantomRandomDirection == 3:
                    phantom.rect.top += movimiento
        phantoms[index] = (phantom, phantomRandomDirection)


def checaChoque(listaFan, pacman):
    ModoDeJuego = 2
    xPac, yPac, wPac, hPac = pacman.rect
    for fan, _ in listaFan:
        if ((fan.rect.left < xPac < fan.rect.left + fan.rect.width) or (
                fan.rect.left < xPac + wPac < fan.rect.left + fan.rect.width)) and (
                (fan.rect.top < yPac < fan.rect.top + fan.rect.height) or (
                fan.rect.top < yPac + hPac < fan.rect.top + fan.rect.height)):
            ModoDeJuego = 3
    return ModoDeJuego


def dibujar():
    # Inicializa el motor de pygame
    pygame.init()
    pygame.display.set_caption(DISPLAY_CAPTION)
    ventana = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución

    # Personaje Pacman inicialización
    imgPacman = pygame.image.load(PACMAN_1_IMG_FILEPATH)
    pacman = pygame.sprite.Sprite()
    pacman.rect = imgPacman.get_rect()

    # Posición inicial Pacman
    pacman.rect.left = 400 - pacman.rect.width // 2
    pacman.rect.top = 562 - pacman.rect.height // 2

    # Inicialización de Fantasmas
    fantasmaAImg = pygame.image.load(PHANTOM_A_IMG_FILEPATH)
    fantasmaA = pygame.sprite.Sprite()
    fantasmaA.rect = fantasmaAImg.get_rect()
    fantasmaA.rect.left = 343
    fantasmaA.rect.top = 365
    fantasmaA.image = fantasmaAImg
    fanARanMov = 0

    fantasmaBImg = pygame.image.load(PHANTOM_B_IMG_FILEPATH)
    fantasmaB = pygame.sprite.Sprite()
    fantasmaB.rect = fantasmaBImg.get_rect()
    fantasmaB.rect.left = 427
    fantasmaB.rect.top = 365
    fantasmaB.image = fantasmaBImg
    fanBRanMov = 0

    fantasmaCImg = pygame.image.load(PHANTOM_C_IMG_FILEPATH)
    fantasmaC = pygame.sprite.Sprite()
    fantasmaC.rect = fantasmaCImg.get_rect()
    fantasmaC.rect.left = 301
    fantasmaC.rect.top = 365
    fantasmaC.image = fantasmaCImg
    fanCRanMov = 0

    fantasmaDImg = pygame.image.load(PHANTOM_D_IMG_FILEPATH)
    fantasmaD = pygame.sprite.Sprite()
    fantasmaD.rect = fantasmaDImg.get_rect()
    fantasmaD.rect.left = 469
    fantasmaD.rect.top = 365
    fantasmaD.image = fantasmaDImg
    fanDRanMov = 0

    # Inicialización de Dots
    listaDots = []
    copiaLista = []
    imgDot = pygame.image.load(DOT_IMG_FILEPATH)
    crearDots(listaDots, imgDot, loadDotCoords(DOT_COORDS_FILEPATH))
    ticksFan = 0

    # Animación
    animationCounterPacman = 0
    ticks = 0

    # Movimiento
    direccion = 0

    # Puntaje
    Font = pygame.font.Font(FONT_BIT_WONDER_TTF_FILEPATH, 30)
    score = 0

    # Modos de Juego
    ModoDeJuego = 1

    Menu = 1
    Juego = 2
    GameOver = 3
    Gano = 4

    # Inicializacion Fondo y Boton
    fondo = pygame.sprite.Sprite()
    fondoImg = pygame.image.load("resources/img/general/menu/Fondo_Pacman.jpg")
    fondo.image = fondoImg
    fondo.rect = fondoImg.get_rect()
    fondo.rect.left = 0
    fondo.rect.top = 0

    boton = pygame.sprite.Sprite()
    botonImg = pygame.image.load("resources/img/general/menu/Boton_Play.png")
    boton.image = botonImg
    boton.rect = botonImg.get_rect()
    boton.rect.left = DISPLAY_WIDTH // 2 - boton.rect.width // 2
    boton.rect.top = 3 * (DISPLAY_HEIGHT // 4) - boton.rect.height // 2

    # Inicializacion Sonidos
    pygame.mixer.init()
    musicaInicio = pygame.mixer.Sound(PACMAN_BEGINNING_WAV_FILEPATH)
    musicaJuego = pygame.mixer.Sound(PACMAN_CHOMP_WAV_FILEPATH)
    efectoMuerte = pygame.mixer.Sound(PACMAN_DEATH_WAV_FILEPATH)
    musicaVictoria = pygame.mixer.Sound(PACMAN_EXTRAPAC_WAV_FILEPATH)
    pygame.mixer.set_num_channels(1)

    # DEBUGGING
    deathSoundPlayed_Flag = False

    while not termina:  # Ciclo principal

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
            if ModoDeJuego == Menu:
                if evento.type == pygame.MOUSEBUTTONUP:
                    xM, yM = pygame.mouse.get_pos()
                    if boton.rect.left <= xM <= boton.rect.left + boton.rect.width:
                        if boton.rect.top <= yM <= boton.rect.top + boton.rect.height:
                            ModoDeJuego = Juego

        # Borrar pantalla
        ventana.fill(NEGRO)

        if ModoDeJuego == Menu:
            if pygame.mixer.Sound.get_num_channels(musicaInicio) < 5:
                pygame.mixer.Sound.play(musicaInicio, loops=0)
            ventana.blit(fondo.image, fondo.rect)
            ventana.blit(boton.image, boton.rect)
            ### Loading screen to be added
            loadPacmanImgs()
        elif ModoDeJuego == Juego:
            pygame.mixer.Sound.stop(musicaInicio)
            pygame.mixer.Sound.play(musicaJuego)
            phantoms_List = [(fantasmaA, 0), (fantasmaB, 0), (fantasmaC, 0), (fantasmaD, 0)]
            animationCounterPacman = animationCounterPacmanTick(animationCounterPacman)
            pacman.image = animarPacman(animationCounterPacman)
            pacman, direccion = movimientoPacman(pacman, direccion)
            if ticks <= 650:
                phantoms_List = movimientoFantasmas(phantoms_List, ticks)

            selectPhantomRandomDirection(phantoms_List)
            initPhantomMovement(phantoms_List)
            movePhantoms(phantoms_List)


            ventana.blit(Font.render("Pacman", False, BLANCO), (5, 10))
            # ventana.blit(Font.render("%03d, %03d" % (pacman.rect.left, pacman.rect.top), False, BLANCO), (5, 10))
            mapa(ventana)
            dibujarDots(ventana, listaDots)
            ventana.blit(fantasmaB.image, fantasmaB.rect)
            ventana.blit(fantasmaC.image, fantasmaC.rect)
            ventana.blit(fantasmaD.image, fantasmaD.rect)
            ventana.blit(fantasmaA.image, fantasmaA.rect)
            ventana.blit(pacman.image, pacman.rect)

            ModoDeJuego = checaChoque(phantoms_List, pacman)

            scoreTitulo = renderScoreTitle(Font)
            scoreNum = renderScore(Font, score)
            score += checaPuntaje(pacman, listaDots, copiaLista)

            ventana.blit(scoreTitulo, (3, 60))
            ventana.blit(scoreNum, (163, 60))

            if len(listaDots) == 0:
                ModoDeJuego = Gano
            ticks += 1
        elif ModoDeJuego == GameOver:
            pygame.mixer.Sound.stop(musicaJuego)
            if not deathSoundPlayed_Flag and pygame.mixer.Sound.get_num_channels(efectoMuerte) < 5:
                pygame.mixer.Sound.play(efectoMuerte)
                deathSoundPlayed_Flag = True
            ventana.blit(fondo.image, fondo.rect)
            ventana.blit(Font.render("Perdiste", False, BLANCO),
                         (DISPLAY_WIDTH // 2 - 105, 3 * (DISPLAY_HEIGHT // 4) - 15))
        elif ModoDeJuego == Gano:
            pygame.mixer.Sound.stop(musicaJuego)
            if pygame.mixer.Sound.get_num_channels(musicaVictoria) < 5:
                pygame.mixer.Sound.play(musicaVictoria, loops=0)
            ventana.blit(fondo.image, fondo.rect)
            ventana.blit(Font.render("Ganaste", False, BLANCO),
                         (DISPLAY_WIDTH // 2 - 100, 3 * (DISPLAY_HEIGHT // 4) - 15))

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(60)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def main():
    dibujar()


main()
