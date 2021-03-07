"""Case-study #5 Web-pages parsing
Developers:   Zhuravlev A. (60%),
              Kremlin V. (40%)

"""
import urllib.request as u  # Importing module "urlib" for working with URL.

with open('input.txt') as infile:  # Creating a file object by using "open" function.
    for line in infile:  # Cycle for successive player information output.
        text = str(u.urlopen(line).read())  # Reading the content of a web-page by using function "urlopen".

        NAME = text.find("nfl-c-player-header__title")  # Parsing the page HTML-markup to define player's name.
        NAME = text[text.find('>', NAME) + 1:text.find('</h1', NAME)]
        ATT = text.find("passingAttempts")  # Parsing the page HTML-markup to get player's parameters (1).
        ATT = text[text.find('>', ATT) + 3:text.find('</th>', ATT)].replace('\\n', '').strip()
        COMP = text.find("passingCompletions") # Parsing the page HTML-markup to get (1).
        COMP = text[text.find('>', COMP) + 3:text.find('</th>', COMP)].replace('\\n', '').strip()
        YDS = text.find("passingYards")  # Parsing the page HTML-markup to get (1).
        YDS = text[text.find('>', YDS) + 3:text.find('</th>', YDS)].replace('\\n', '').strip()
        TD = text.find("passingTouchdowns")  # Parsing the page HTML-markup to get (1).
        TD = text[text.find('>', TD) + 3:text.find('</th>', TD)].replace('\\n', '').strip()
        INT = text.find("passingInterceptions")  # Parsing the page HTML-markup to get (1).
        INT = text[text.find('>', INT) + 3:text.find('</th>', INT)].replace('\\n', '').strip()
        RATE = text.find("passingPasserRating")  # Parsing the page HTML-markup to get player's quarterback rating.
        RATE = float(text[text.find('>', RATE) + 3:text.find('</th>', RATE)].replace('\\n', '').strip())

        with open('output.txt', 'w') as outfile:  # Formatting the data we received in a table by using "format" method.
            print('{:<20}{:<7}{:<7}{:<7}{:<7}{:<7}{:.2f}'.format(NAME, COMP, ATT, YDS, TD, INT, RATE))
