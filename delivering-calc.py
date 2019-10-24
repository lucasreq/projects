import math
import json
import time

with open("cities.json", "r") as read_file:
    data = json.load(read_file)

    ville1 = input('Ville de départ (attention si vous voulez entrer marseille ou paris entrez egalement l\'arrondissement ex: PARIS 01)').upper()
    ville2 = input('Ville d\'arrivé ').upper()


    def search1(city1):
        i = 0
        for p in data:
            if (data[i]['Nom_commune'] == city1):
                return p['coordonnees_gps']

            else:
                i += 1
    
    coordcity1 = search1(ville1)

    def search2(city):
        i = 0
        for p in data:
            if (data[i]['Nom_commune'] == city):
                return p['coordonnees_gps']

            else:
                i += 1

    coordcity2 = search2(ville2)

    tabcoordcity1 = coordcity1.split(", ")
    tabcoordcity2 = coordcity2.split(", ")

    coordcity1a = float(tabcoordcity1[0])
    coordcity1b = float(tabcoordcity1[1])
    coordcity2a = float(tabcoordcity2[0])
    coordcity2b = float(tabcoordcity2[1])

    def convert(lat1, lon1, lat2, lon2):
        R = 6372800  # Earth radius(m)
        
        phi1, phi2 = math.radians(lat1), math.radians(lat2) 
        dphi       = math.radians(lat2 - lat1)
        dlambda    = math.radians(lon2 - lon1)
        
        a = math.sin(dphi/2)**2 + \
            math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
        
        return 2*R*math.atan2(math.sqrt(a), math.sqrt(1 - a))

    kilometers = (convert(coordcity1a,coordcity1b,coordcity2a,coordcity2b)/1000)

    def travel(kilometer):
        t = 0 #in seconds
        v = 0
        kmp = 0
        lpause = 0
        nbpause = 0
        inpause = False

        while(kmp < (kilometer * 1000)):
            if(t != 0 and (t-lpause) % (60*60*2) == 0):
                inpause = True
            if(v < 90 and inpause == False):
                if(v + 10/60 <= 90):
                    v += 10/60
                else:
                    v = 90
            if(inpause and v > 0):
                if(v - 10/60 >= 0):
                    v -= 10/60
                else:
                    v = 0
            elif(inpause == True and v == 0):
                nbpause += 1
                t += 60*15
                lpause = t
                inpause = False
            kmp += (v/3.6)
            t += 1
        hours = 0
        minutes = 0
        if(t/60 > 0):
            if(t/3600 > 0):
                hours = math.floor(t/3600)
            minutes = math.ceil((t % 3600)/60)
        print('--------------------------------------------------------------------------------------------------------------------')
        print('ville de départ : ' + ville1 + ' | ' 'ville d\'arrivée : ' + ville2 + ' | ' + str(kilometers) +  ' km | ' "{}:{}".format(hours, minutes), "(dont {} minutes de pause)".format(nbpause * 15))
        print('--------------------------------------------------------------------------------------------------------------------')

travel(kilometers)


