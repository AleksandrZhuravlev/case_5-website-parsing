"""Case-study #5 Парсинг web-страниц
Developers:   Zhuravlev A. (60%),
              Kremlin V. (40%)

"""
import urllib.request as u

with open('input.txt') as infile:
    for line in infile:
        text = str(u.urlopen(line).read())

        part_name = text.find("nfl-c-player-header__title")
        name = text[text.find('>', part_name) + 1:text.find('</h1', part_name)]
        attrate = text.find("passingAttempts")
        att = text[text.find('>', attrate) + 3:text.find('</th>', attrate)].replace('\\n', '').strip()
        comprate = text.find("passingCompletions")
        comp = text[text.find('>', comprate) + 3:text.find('</th>', comprate)].replace('\\n', '').strip()
        ydsrate = text.find("passingYards")
        yds = text[text.find('>', ydsrate) + 3:text.find('</th>', ydsrate)].replace('\\n', '').strip()
        tdrate = text.find("passingTouchdowns")
        td = text[text.find('>', tdrate) + 3:text.find('</th>', tdrate)].replace('\\n', '').strip()
        intrate = text.find("passingInterceptions")
        intr = text[text.find('>', intrate) + 3:text.find('</th>', intrate)].replace('\\n', '').strip()
        finrate = text.find("passingPasserRating")
        fin = float(text[text.find('>', finrate) + 3:text.find('</th>', finrate)].replace('\\n', '').strip())

        with open('output.txt', 'w') as out:
            print('{:<20}{:<7}{:<7}{:<7}{:<7}{:<7}{:.2f}'.format(name, comp, att, yds, td, intr, fin))
