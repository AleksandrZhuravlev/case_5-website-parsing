"""Case-study #5 Парсинг web-страниц
Developers:   Zhuravlev A. (60%),
              Kremlin V. (40%)

"""
import urllib.request as u  # Импорт модуля urllib для работы с URL.

with open('input.txt') as infile:  # Создание файлового объекта при помощи функции open.
    for line in infile:  # Цикл для последовательного вывода информации об игроках.
        text = str(u.urlopen(line).read())  # Считываем содержимое web-страницы с помощью функции urlopen.

        name = text.find("nfl-c-player-header__title")  # Анализ HTML-разметки страницы для получения имени игрока.
        name = text[text.find('>', name) + 1:text.find('</h1', name)]
        ATT = text.find("passingAttempts")  # Анализ HTML-разметки страницы для получения параметров игрока (1).
        ATT = text[text.find('>', ATT) + 3:text.find('</th>', ATT)].replace('\\n', '').strip()
        COMP = text.find("passingCompletions") # Анализ HTML-разметки страницы для (1).
        COMP = text[text.find('>', COMP) + 3:text.find('</th>', COMP)].replace('\\n', '').strip()
        YDS = text.find("passingYards")  # Анализ HTML-разметки страницы для (1).
        YDS = text[text.find('>', YDS) + 3:text.find('</th>', YDS)].replace('\\n', '').strip()
        TD = text.find("passingTouchdowns")  # Анализ HTML-разметки страницы для (1).
        TD = text[text.find('>', TD) + 3:text.find('</th>', TD)].replace('\\n', '').strip()
        INT = text.find("passingInterceptions")  # Анализ HTML-разметки страницы для (1).
        INT = text[text.find('>', INT) + 3:text.find('</th>', INT)].replace('\\n', '').strip()
        RATE = text.find("passingPasserRating")  # Анализ HTML-разметки страницы для получения квотербек-рейтинга.
        RATE = float(text[text.find('>', RATE) + 3:text.find('</th>', RATE)].replace('\\n', '').strip())

        with open('output.txt', 'w') as outfile:  # Оформление полученных данных в виде таблицы, используя метод format.
            print('{:<20}{:<7}{:<7}{:<7}{:<7}{:<7}{:.2f}'.format(name, COMP, ATT, YDS, TD, INT, RATE))
