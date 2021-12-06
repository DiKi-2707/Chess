import logging

logging.basicConfig(filename="logfile.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(funcName)s: "
                                                                       "%(lineno)d - %(message)s")
alha = logging.getLogger()

"""Функция опредения цвета поля"""

def color_vibor(u1, p1, u2, p2):
    if (u1 + p1) % 2 != (u2 + p2) % 2:
        print("Фигуры стоят на полях разного цвета")
        logging.info("Остатки от деления на 2 - %s и %s, они не равны " % ((u1 + p1) % 2, (u2 + p2) % 2))
    else:
        print("Фигуры стоят на полях одинакового цвета")
        logging.info("Остатки от деления на 2 - %s и %s, они равны " % ((u1 + p1) % 2, (u2 + p2) % 2))

try:

    print("Первое число — номер вертикали (при счете слева направо), второе — номер горизонтали (при счете снизу вверх)")
    a, b = map(int, input("Введите через пробел номер вертикали и горизонтали для первой фигуры: ").split())
    if a > 8 or a < 1 or b > 8 or b < 1:
        logging.error("Ошибка! %s или %s вне диапазона от 1 до 8" % (a, b))
        quit("Ошибка! Нужно ввести число от 1 до 8! Перезапустите программу!")
    sarinka = int(
        input("\nВведите номер для определение типа первой фигуры\n1. Ферзь\n2. Ладья\n3. Слон\n4. Конь\n"))
    if sarinka > 4 or sarinka < 1:
        logging.error("Ошибка! %s вне диапазона от 1 до 4" % sarinka)
        quit("Ошибка! Нужно ввести число от 1 до 4! Перезапустите программу!")
    c, d = map(int, input("Введите через пробел номер вертикали и горизонтали для второй фигуры: ").split())
    if c > 8 or c < 1 or d > 8 or d < 1:
        logging.error("Ошибка! %s или %s вне диапазона от 1 до 8" % (c, d))
        quit("Ошибка! Нужно ввести число от 1 до 8! Перезапустите программу!")

        """Массивы координат фигур для второго хода"""

    a_pur = []
    b_pur = []

    """Проверка для ходов ферзя"""

    def dan_kurt(a, b, c, d):
        if a == c or b == d or (abs(a - c) == abs(b - d)):
            print("Ферзь угрожает пешке")
            logging.info("%s = %s или %s = %s или %s = %s" % (a, b, c, d, abs(a - c), abs(b - d)))
            logging.info("Так как ферзь находится на одной диагонали или вертикали или горизонтали - он угрожает пешке")
        else:
            print("Ферзь не угрожает пешке")
            print("Клетки чтобы уничтожить пешку со второго хода")
            logging.info("%s ≠ %s или %s ≠ %s или %s ≠ %s" % (a, b, c, d, abs(a - c), abs(b - d)))
            logging.info("Так как ферзь не находится на одной диагонали или вертикали или горизонтали - он не "
                         "угрожает пешке")
            a_pur.append(a)
            a_pur.append(c)
            b_pur.append(d)
            b_pur.append(b)
            a2 = a3 = a4 = a5 = a
            b2 = b3 = b4 = b5 = b
            while a2 < 8 and b2 < 8:
                a2 += 1
                b2 += 1
                if abs(a2 - c) == abs(b2 - d) or a2 == c or b2 == d:
                    a_pur.append(a2)
                    b_pur.append(b2)
            while a3 < 9 and b3 > 1:
                a3 += 1
                b3 -= 1
                if abs(a3 - c) == abs(b3 - d) or a3 == c or b3 == d:
                    a_pur.append(a3)
                    b_pur.append(b3)
            while a4 > 1 and b4 < 8:
                a4 -= 1
                b4 += 1
                if abs(a4 - c) == abs(b4 - d) or a4 == c or b4 == d:
                    a_pur.append(a4)
                    b_pur.append(b4)
            while a5 > 1 and b5 > 1:
                a5 -= 1
                b5 -= 1
                if abs(a5 - c) == abs(b5 - c) or a5 == c or b5 == d:
                    a_pur.append(a5)
                    b_pur.append(b5)

                """Проверка для ходов ладьи"""

    def lok_tin(a, b, c, d):
        if a == c or b == d:
            print("Ладья угрожает пешке")
            logging.info("%s = %s или %s = %s" % (a, c, b, d))
            logging.info("Так как ладья находится на одной вертикали или горизонтали - она угрожает пешке")
        else:
            print("Ладья не угрожает пешке")
            logging.info("%s ≠ %s или %s ≠ %s" % (a, c, b, d))
            logging.info("Так как ладья не находится на одной вертикали или горизонтали - она не угрожает пешке")
            a_pur.append(a)
            a_pur.append(c)
            b_pur.append(d)
            b_pur.append(b)
            print("Клетки чтобы уничтожить пешку со второго хода")

            """Проверка для ходов слона"""

    def oper_www(a, b, c, d):
        if abs(a - c) == abs(b - d):
            print("Слон угрожает пешке")
            logging.info("%s = %s " % (abs(a - c), abs(b - d)))
            logging.info("Так как слон находится на одной диагонали - он угрожает пешке")
        else:
            print("Слон не угрожает пешке")
            print("Клетки чтобы уничтожить пешку со второго хода")
            logging.info("%s ≠ %s " % (abs(a - c), abs(b - d)))
            logging.info("Так как слон не находится на одной диагонали - он не угрожает пешке")
            a2 = a3 = a4 = a5 = a
            b2 = b3 = b4 = b5 = b
            while a2 < 8 and b2 < 8:
                a2 += 1
                b2 += 1
                if abs(a2 - c) == abs(b2 - d):
                    a_pur.append(a2)
                    b_pur.append(b2)
            while a3 < 9 and b3 > 1:
                a3 += 1
                b3 -= 1
                if abs(a3 - c) == abs(b3 - d):
                    a_pur.append(a3)
                    b_pur.append(b3)
            while a4 > 0 and b4 < 8:
                a4 -= 1
                b4 += 1
                if abs(a4 - c) == abs(b4 - d):
                    a_pur.append(a4)
                    b_pur.append(b4)
            while a5 > 0 and b5 > 1:
                a5 -= 1
                b5 -= 1
                if abs(a5 - c) == abs(b5 - d):
                    a_pur.append(a5)
                    b_pur.append(b5)

                """Проверка для ходов коня"""

    def gogi_bit(a, b, c, d):
        if ((abs(a - c) == 1) and (abs(b - d) == 2)) or ((abs(a - c) == 2) and (abs(b - d) == 1)):
            print("Конь угрожает пешке")
            logging.info("(%s = 1 и %s = 2) или (%s = 2 и %s = 1)" % (abs(a - c), abs(b - d), abs(a - c), abs(b - d)))
            logging.info("Конь угрожает пешке")
        else:
            print("Конь не угрожает пешке")
            logging.info("(%s ≠ 1 и %s ≠ 2) или (%s ≠ 2 и %s ≠ 1)" % (abs(a - c), abs(b - d), abs(a - c), abs(b - d)))
            logging.info("Конь не угрожает пешке")
            a2 = a
            b2 = b
            a_yes = [2, 1, 1, 2, -1, -2, -2, -1]
            b_yes = [-1, -2, 2, 1, 2, 1, -1, -2]
            for i in range(8):
                a2 += a_yes[i]
                b2 += b_yes[i]
                if ((abs(a2 - c) == 1) and (abs(b2 - d) == 2)) or ((abs(a2 - c) == 2) and (abs(b2 - d) == 1)):
                    if a2 < 8 and a2 > 1 and b2 < 8 and b2 > 1:
                        a_pur.append(a2)
                        b_pur.append(b2)
                a2 = a
                b2 = b

        """Тело нашей программы"""

    color_vibor(a, b, c, d)
    if sarinka == 1:
        dan_kurt(a, b, c, d)
        for i in range(len(a_pur)):
            print(a_pur[i], b_pur[i])
    if sarinka == 2:
        lok_tin(a, b, c, d)
        for i in range(len(a_pur)):
            print(a_pur[i], b_pur[i])
    if sarinka == 3:
        oper_www(a, b, c, d)
        for i in range(len(a_pur)):
            print(a_pur[i], b_pur[i])
    if sarinka == 4:
        gogi_bit(a, b, c, d)
        for i in range(len(a_pur)):
            print(a_pur[i], b_pur[i])
except ValueError:
    alha.exception("Ошибка неверного типа данных!")
    quit("Ошибка! Перезапустите программу!")
