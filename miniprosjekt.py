from random import randint
def main():
    meny()

def meny():
    print('Valgalternativ:\n'
          '[1] intro\n'
          '[2] ikke uniform\n'
          '[3] gunstig / mulig\n'
          '[4] uavhengighet\n'
          '[5] simulering\n'
          '[6] avslutt\n')

    alternativ=int(input('Hvilket program vil du kjøre?'))
    if alternativ==1:
        intro()
    if alternativ==2:
        ikke_uniform()
    if alternativ == 3:
        gunstig_mulig()
    if alternativ == 4:
        uavhengighet()
    if alternativ == 5:
        simuleringsprogram()
    if alternativ == 6:
        print('Takk for ingenting...')
def spacer():
    print('\n------------------------------------\n')
def intro():
    print('Du har sikkert ofte tenkt på hva som kan komme til å skje.\nDet finnes flere eksempler på at det vil være viktig å kunne forutsi hva som kommer til å skje.\nEt eksempel på dette kan være flomvarsling.\n\n'
          'For å kunne forutsi det som kan komme til å skje, kan man benytte seg av\033[1;32m sannsynlighetsmodeller\033[1;0m og \033[1;32msimuleringer\033[1;0m. \n'
          'I dette programmet skal du få en forklaring for hvordan du kan regne ut sannsynlighet. Til slutt får du muligheten til å kjøre en simulering\n'  )
    input('Trykk \033[1;32mENTER\033[1;0m for å forsette') #I utgangspunktet tenkte vi at vi skulle bruke en tilfeldig tast for å fortsette. Det viste seg å være litt mer komplisert enn tiltenkt, så vi valgte en enklere variant.
    spacer()
    meny()

def ikke_uniform():
    print('Innen sannsynlighetsregning snakker man gjerne om \033[1;32muniform\033[1;0m og \033[1;32mikke-uniform\033[1;0m sannsynlighetsmodell.\n\n'
          'Vi bruker en uniform sannsynlighetsmodell når alle utfall av en hendelse har like stor sannsynlighet for å skje.\nEt eksempel på en slik situasjon er terningkast.\n\n')
    svar1=input('Hva er sannsynligheten for at du skal få en femmer på en terning (skriv tallet som en brøk)? ')
    teller1=1
    while teller1 <3:
        if svar1=='1/6':
            print(f'Du svarte {svar1}. Det er korrekt')
            teller1=3
        else:
            print(f'Du svarte {svar1}. Svaret er ikke rett.\nPå en terning er det 6 utfall. Det er like stor sannsynlihget for alle utfall\n')
            teller1 +=1
            svar1 = input('Hva er sannsynligheten for at du skal få en femmer på en terning (skriv tallet som en brøk)? ')
    print('Siden en terning har seks utfall, og alle utfall har like stor sannsynlighet vil sannsynligheten være 1/6 for å få en femmer.\n')
    input('Trykk \033[1;32mENTER\033[1;0m for å forsette')
    print('Men det er ikke alle hendelser som har like stor sannsynlighet. Slike sannsynlighetsmodeller kaller vi ikke-uniform sannsynlighetsmodell.\n'
          'Et eksempel på en slik situasjon er hvilken blodtype en tilfeldig valgt person har.\n'
          'Selv om det er fire blodtyper, er det ca. halvparten av norges befolkning som har den ene blodtypen.\n'
          'Du vil altså større sannsynlighet for å treffe på en person med blodtype A.\n')
    svar2=input('En håndballspiller skal ta straffekast. Hun har truffet på 150 av 200 straffekast. Hva er sannsynligheten for at spilleren treffer neste kast (skriv svaret som prosent)?')
    teller2 = 1
    while teller2 < 3:
        if svar2 == '75%' or svar2=='75':
            print(f'Du svarte {svar2}. Det er korrekt')
            teller2 = 3
        else:
            print(
                f'Du svarte {svar2}. Svaret er ikke rett.\nHvis jeg treffer på 1 av 4 skudd, er sannsynligheten for å treffe lik 25%.\n')
            teller2 += 1
            svar2=input('En håndballspiller skal ta straffekast. Hun har truffet på 150 av 200 straffekast. Hva er sannsynligheten for at spilleren treffer neste kast (skriv svaret som prosent)?')
    print('Siden spilleren har treffet på 150 av 200 skudd, vil sannsynligheten være 150/200 for å treffe, som er lik 75%.\n')
    input('Trykk \033[1;32mENTER\033[1;0m for å forsette')
    spacer()
    meny()

def gunstig_mulig():
    print('Når man skal regne ut sannsynligheten for en hendelse, så bruker vi begrepene gunstig og mulig\n'
          '\033[1;32mGunstige utfall\033[1;0m er det vi ønsker skal skje, mens\033[1;32m mulige utfall\033[1;0m er alle hendelser som kan skje.\n'
          'Hvis du kan velge en av fem luker, så vil antall gunstige valg være lik 1 og mulige utfall vil være lik 5\n')
    svar1=input('Hvor mange gunstige utfall er det dersom du skal trekke en spar fra en kortstokk? ')
    teller1 = 1
    while teller1 < 3:
        if svar1 == '13':
            print(f'Du svarte {svar1}. Det er korrekt')
            teller1 = 3
        else:
            print(f'Du svarte {svar1}. Svaret er ikke rett.\nI en kortstokk er det fire typer kort (hjerter, spar, kløver og ruter). Totalt er det 52 kort.\n')
            teller1 += 1
            svar1 = input(
                'Hva er sannsynligheten for at du skal få en femmer på en terning (skriv tallet som en brøk)? ')
    print('En kortstokk har 13 spar, derfor er det 13 mulige utfall.\n')
    input('Trykk \033[1;32mENTER\033[1;0m for å forsette')
    spacer()
    meny()

def uavhengighet():
    print('Det finnes situasjoner der vi ønske å vite hvor stor sannsynligheten er for at flere ting skal skje.\n'
          'Dersom situasjonene ikke påvirker hverandre, kaller vi slike hendelser for \033[1;32uavhengige hendelser\033[1;0m.\n'
          'Et eksempel på en uavhengig hendelse vil være å kaste en terning flere ganger. Du vil ikke ha mindre sannsynlighet for å få en sekser på ditt andre kast dersom du fikk sekser på første kast.\n\n'
          'For å regne sannsynligheten for flere hendelser bruker vi produktregelen. Den sier at for å regne ut sannsynligheten for to påfølgende hendelser (A og B), så kan man multiplisere sannsynligheten for hendelse A og B.\n'
          'Sannsynligheten for å trekke to få to femmere på en terning blir da 1/6 * 1/6 = 1/36.\n')
    svar1=input('Du skal velge mellom fire luker to ganger på rad. Hva er sannsynligheten for å velge rett begge ganger (oppgi svaret som brøk)? ')
    teller1 = 1
    while teller1 < 3:
        if svar1 == '1/16':
            print(f'Du svarte {svar1}. Det er korrekt')
            teller1 = 3
        else:
            print(f'Du svarte {svar1}. Svaret er ikke rett.\nSannsynligheten for å velge rett dør første gang er 1/4. Sannsynligheten for å velge rett dør andre gang er 1/4\n')
            teller1 += 1
            svar1=input('Du skal velge mellom fire luker to ganger på rad. Hva er sannsynligheten for å velge rett begge ganger (oppgi svaret som brøk)? ')
    print('Når du skal velge mellom fire dører to ganger på rad vil sannsynligheten for å velge rett begge ganger være 1/4 * 1/4 = 1/16\n')
    input('Trykk \033[1;32mENTER\033[1;0m for å forsette')
    spacer()
    meny()

def simuleringsprogram():
    def setup():
        print('Dette er en simulering som viser veivalg.')
        str_1 = str("Elven deler seg i tre. Hvor bred er elv")
        elv_a = int(input(f"{str_1} A?"))
        elv_b = int(input(f"{str_1} B?"))
        elv_c = int(input(f"{str_1} C?"))
        print('Elv[A] deler seg i to. Hvor bred er elvene?')
        elv_a_1 = int(input(f"{str_1} A1?"))
        elv_a_2 = int(input(f"{str_1} A2"))
        print('Elv[B] deler seg i to. Hvor bred er elvene?')
        elv_b_1 = int(input(f"{str_1} B1"))
        elv_b_2 = int(input(f"{str_1} B2"))
        print('Elv[C] deler seg i to. Hvor bred er elvene?')
        elv_c_1 = int(input(f"{str_1} C1?"))
        elv_c_2 = int(input(f"{str_1} C2?"))

        return elv_a, elv_b, elv_c, elv_a_1, elv_a_2, elv_b_1, elv_b_2, elv_c_1, elv_c_2

    def databehandling(antall_sim):
        oversikt = {'elv_a': 0, 'elv_b': 0, 'elv_c': 0, 'elv_a_1': 0, 'elv_a_2': 0,
                    'elv_b_1': 0, 'elv_b_2': 0, 'elv_c_1': 0, 'elv_c_2': 0}

        while antall_sim > 0:
            søppel = randint(1, 5)
            elvekryss1 = randint(1, elv_a + elv_b + elv_c)
            if elvekryss1 <= elv_a:
                oversikt['elv_a'] += søppel
                elvekryss2 = randint(1, elv_a_1 + elv_a_2)
                if elvekryss2 <= elv_a_1:
                    oversikt['elv_a_1'] += søppel
                else:
                    oversikt['elv_a_2'] += søppel
            elif elvekryss1 > elv_a and elvekryss1 <= elv_a + elv_b:
                oversikt['elv_b'] += søppel
                elvekryss2 = randint(1, elv_b_1 + elv_b_2)
                if elvekryss2 <= elv_b_1:
                    oversikt['elv_b_1'] += søppel
                else:
                    oversikt['elv_b_2'] += søppel
            elif elvekryss1 > elv_a + elv_b:
                oversikt['elv_c'] += søppel
                elvekryss2 = randint(1, elv_c_1 + elv_c_2)
                if elvekryss2 <= elv_c_1:
                    oversikt['elv_c_1'] += søppel
                else:
                    oversikt['elv_c_2'] += søppel
            else:
                print("error")
            antall_sim -= 1
        return oversikt

    def teoretisk_sannsynlighet():
        sum_elv = elv_a + elv_b + elv_c
        prob_a = elv_a / sum_elv
        prob_b = elv_b / sum_elv
        prob_c = elv_c / sum_elv
        sum1 = elv_a_1 + elv_a_2
        sum2 = elv_b_1 + elv_b_2
        sum3 = elv_c_1 + elv_c_2
        prob_a1 = elv_a_1 / sum1
        prob_a2 = elv_a_2 / sum1
        prob_b1 = elv_b_1 / sum2
        prob_b2 = elv_b_2 / sum2
        prob_c1 = elv_c_1 / sum3
        prob_c2 = elv_c_2 / sum3
        sannsynlighet = {}
        sannsynlighet['Utløp 1'] = format(prob_a*prob_a1, '.2%')
        sannsynlighet['Utløp 2'] = format(prob_a*prob_a2, '.2%')
        sannsynlighet['Utløp 3'] = format(prob_b*prob_b1, '.2%')
        sannsynlighet['Utløp 4'] = format(prob_b*prob_b2, '.2%')
        sannsynlighet['Utløp 5'] = format(prob_c*prob_c1, '.2%')
        sannsynlighet['Utløp 6'] = format(prob_c*prob_c2, '.2%')
        return sannsynlighet

    brukersvar='j'


    elv_a, elv_b, elv_c, elv_a_1, elv_a_2, elv_b_1, elv_b_2, elv_c_1, elv_c_2 = setup()
    teori_sannsyn = teoretisk_sannsynlighet()

    while brukersvar == 'j' or brukersvar == 'J':

        print(teori_sannsyn) # teoretisk sannsynlighet bør pyntes på

        antall_sim = int(input('Hvor mange simuleringer vil du kjøre?'))

        oversikt=databehandling(antall_sim)

        total = sum(oversikt.values()) / 2
        spacer()

        print('\033[1;32mKg søppel:' + '\t\t\t' + 'prosentdel:\033[1;0m')
        print('Utløp 1: ' + str(oversikt['elv_a_1']) + '\t\t' + str(format(oversikt['elv_a_1']/total, '.2%')) + '\n' +
            'Utløp 2: ' + str(oversikt['elv_a_2']) + '\t\t' + str(format(oversikt['elv_a_2']/total, '.2%')) + '\n' +
            'Utløp 3: ' + str(oversikt['elv_b_1']) + '\t\t' + str(format(oversikt['elv_b_1']/total, '.2%')) + '\n' +
            'Utløp 4: ' + str(oversikt['elv_b_2']) + '\t\t' + str(format(oversikt['elv_b_2']/total, '.2%')) + '\n' +
            'Utløp 5: ' + str(oversikt['elv_c_1']) + '\t\t' + str(format(oversikt['elv_c_1']/total, '.2%')) + '\n' +
            'Utløp 6: ' + str(oversikt['elv_c_2']) + '\t\t' + str(format(oversikt['elv_c_2']/total, '.2%')) + '\n'
        )
        print(f' Totalt har det kommet {total} kilo søppel i elva.')

        brukersvar=input('Vil du kjøre en ny simulering med samme data? (j/n) ')

    print(teori_sannsyn)
    print('store talls lov') # fiks bedre tekst

    input('Trykk \033[1;32mENTER\033[1;0m for å gå til menyen')
    spacer()
    meny()

main()

# validering av input
# format print
# linjeskift spacing
# teoretisk sannsynlighet , store talls lov - evt. kommentarsetninger på avvik fra flytskjema

# test daniel