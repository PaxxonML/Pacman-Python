def main():
    dotArray = []
    for x in range(21, 778, 21):  # Cada 35 px una columna nueva. Separación de dots = 15 px
        for y in range(141, 582, 20):
            if not ((y == 161 and (21 < x < 399 or 399 < x < 777)) or (y == 561 and (21 < x < 777)) or (
                    y == 481 and (105 < x < 399 or 399 < x < 693)) or (
                            y == 241 and (105 < x < 399 or 399 < x < 693)) or (
                            y == 321 and (189 < x < 399 or 399 < x < 609)) or (y == 361 and (189 < x < 609))):
                if not ((y == 201 and (63 < x < 735)) or (y == 281 and (167 < x < 631)) or (
                        y == 401 and (209 < x < 589)) or (y == 441 and (167 < x < 631)) or (
                                y == 521 and (63 < x < 735)) or (y == 381 and 189 < x < 609)):
                    if not ((161 < y < 560 and x == 42) or (161 < y < 560 and x == 756) or (
                            241 < y < 480 and x == 126) or (
                                    241 < y < 480 and x == 672)):
                        if not (((201 < y < 322 or 360 < y < 540) and x == 84) or (
                                (281 < y < 322 or 360 < y < 441) and x == 168) or (
                                        (281 < y < 322 or 360 < y < 441) and x == 630) or (
                                        (201 < y < 322 or 360 < y < 540) and x == 714)):
                            dotArray.append([str(x), str(y)])

    file = open("../txt/dotcoords.txt", "w", encoding="UTF-8")
    for coords in dotArray:
        file.write(",".join(coords) + "\n")
    file.close()

main()