"""Case-study #5 Парсинг web-страниц
Разработчики:

"""
with open('input.txt') as inp:
    for line in inp:
        url = line
        import urllib.request
        f = urllib.request.urlopen(url)
        s = f.read()
        text = str(s)
        part_name = text.find("nfl-c-player-header__title")
        name = text[text.find('>',part_name)+1:text.find('</h1',part_name)]
        attrate = text.find("passingAttempts")
        att = text[text.find('>',attrate)+3:text.find('</th>',attrate)]
        att1=att.replace('\\n','').strip()
        comprate = text.find("passingCompletions")
        comp = text[text.find('>',comprate)+3:text.find('</th>',comprate)]
        comp1=comp.replace('\\n','').strip()
        ydsrate = text.find("passingYards")
        yds = text[text.find('>',ydsrate)+3:text.find('</th>',ydsrate)]
        yds1=yds.replace('\\n','').strip()
        tdrate = text.find("passingTouchdowns")
        td = text[text.find('>',tdrate)+3:text.find('</th>',tdrate)]
        td1=td.replace('\\n','').strip()
        intrate = text.find("passingInterceptions")
        int = text[text.find('>',intrate)+3:text.find('</th>',intrate)]
        int1=int.replace('\\n','').strip()
        finrate = text.find("passingPasserRating")
        fin = text[text.find('>', finrate) + 3:text.find('</th>', finrate)]
        fin1 = fin.replace('\\n', '').strip()
        with open('output.txt','w') as out:
            print('{:<20}{:<7}{:<7}{:<7}{:<7}{:<7}{:.2f}'.format(name,comp1,att1,yds1,td1,int1,float(fin1)))


