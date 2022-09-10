from random import randrange

import pygame.sprite

movimiento = 0

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


def initPhantomMovement(phantoms):
    phantomA = phantoms[0][0]
    if phantomA.rect.left == 385 and 325 < phantomA.rect.top == 365:
        phantomA.rect.top -= movimiento
        phantoms[0][1] = 1  # phantom A Random Direction
    phantomB = phantoms[1][0]
    if phantomB.rect.left == 385 and 325 < phantomB.rect.top == 365:
        phantomB.rect.top -= movimiento
        phantoms[1][1] = 1  # phantom B Random Direction
    phantomC = phantoms[2][0]
    if phantomC.rect.left == 385 and 325 < phantomC.rect.top == 365:
        phantomC.rect.top -= movimiento
        phantoms[2][1] = 1  # phantom C Random Direction
    phantomD = phantoms[3][0]
    if phantomD.rect.left == 385 and 325 < phantomD.rect.top == 365:
        phantomD.rect.top -= movimiento
        phantoms[3][1] = 1  # phantom D Random Direction
    phantoms[0][0] = phantomA
    phantoms[1][0] = phantomB
    phantoms[2][0] = phantomC
    phantoms[3][0] = phantomD


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
        phantoms[index][0] = phantom
