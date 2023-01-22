from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import *
from random import randint
import time
import sys

"""---------------- TABLEAUx ----------------------- """

limite=sys.getrecursionlimit()
sys.setrecursionlimit(6000)
"""--------------------------------------------------"""
""" --------------------------    FONCTION RETOUR   ------------------------------------"""
def retour(event=""):
    global quitter,enregistrement,butretour
    fond=Canvas(fen,width=1366,height=768,bg="white")
    photo=PhotoImage(file="0.PNG")
    fond.create_image(683,345,image=photo)
    fond.grid(row=0)
    eparains=Button(fen,text="ENTRER NOM DES PARRAINS",font="arial 15",bg="turquoise4",command=parrains)
    eparains.place(x=40,y=700)
    efilleuls=Button(fen,text="ENTRER NOM DES FILLEULS",font="arial 15",bg="turquoise4",command=filleuls)
    efilleuls.place(x=550,y=700)
    aalancement=Button(fen,text="FIN DE L'ENREGISTREMENT",font="arial 15",bg="turquoise4",command=fendelancement)
    aalancement.place(x=1040,y=700)
    bquitter=Button(fen,text="QUITTER",font="arial 15",bg="turquoise4",command=quitter)
    bquitter.place(x=1230,y=10)
    fen.mainloop()
    fen.quit()
def meltab(t):
    b=[]
    verif=[]
    for i in range(len(t)):
        j=randint(0,len(t)-1)
        while j in verif:
            j=randint(0,len(t)-1)
        b.append(t[j])
        verif.append(j)
    return b
"""------------------------------------------------------------------------------------------"""

"""------------------     FENETRE D'ENREGISTREMENRT       -------------------------------------"""
def enregistrement(qui):
    global parcourir,retour,ephoto,enregistrer,butretour,butparcourir,butenregistrer,fermentry,lbp,lbf
    fond=Canvas(fen,width=1366,height=768,bg="white")
    photo=PhotoImage(file="0.PNG")
    fond.create_image(683,345,image=photo)
    fond.grid(row=0)

    if qui=="PARRAINS":
        lbp=Listbox(fond)
        lbp.place(x=100,y=200)
        try:
            for i in range(len(nomP)):
                lbp.insert(0,nomP[i])
        except:
            pass
    else:
        lbf=Listbox(fond)
        lbf.place(x=100,y=200)
        try:
            for i in range(len(nomF)):
                lbf.insert(0,nomF[i])
        except:
            pass       
    ephoto=Canvas(fen, width=380, height=380, bg='red')
    ephoto.place(x=470, y=100)
    reinitialiser=Button(fen,text="REINITIALISER TOUT",font="arial 15",bg="gray")
    reinitialiser.place(x=1040,y=90)
    actionp=Button(fen,text="PRECEDENT",font="arial 15",bg="gray",command=preced)
    actionp.place(x=1040,y=20)
    butenregistrer=Button(fen, text='Enregistrer',font='Callibri 18',bg='gray',relief=FLAT)
    butenregistrer.place(x=600, y=545)
    fermentry= Label(fen,relief=GROOVE, bg='gray', width=54)
    fermentry.place(x=470, y=500)
    np= Label(fen, text='NOM ET PRENOMS :', fg='turquoise4')
    np.place(x=350,y=500)
    lab2 =Label(fen, text='IDENTIFICATION DES '+str(qui), font="Helvetica 11 bold", fg='cyan', bg='turquoise4', relief='groove', borderwidth=5, width=30)
    lab2.place(x=530,y=60)
    butparcourir=Button(fen, text='Parcourir', font='Callibri 15',command=parcourir)
    butparcourir.place(x=870, y=442) #POSITIONNER LE BOUTTON)
    butretour=Button(fen,text="RETOUR",font='Callibri 15',bg="turquoise4",command=retour)
    butretour.place(x=80,y=10)
    fen.mainloop()
    fen.quit()
"""  --------------------------------    PAGE D'ACCUEIL ---------------------------------"""
def fendelancement(event=""):
    global retour,butretour,pd,fd,defiler,defil1,defil2,stoptout,pd1,pd2,nom1,nom2,TBinoP,TBinoF,BinoP,BinoF,TP,TF,TNP,TNF
    fond=Canvas(fen,width=1366,height=768,bg="white")
    photo=PhotoImage(file= "0.PNG")
    fond.create_image(683,345,image=photo)
    fond.grid(row=0)
    defil1= Canvas(fen,bg='blue', width=500, height=360)
    defil1.place(x=150, y=150)
    defil2= Canvas(fen, bg='purple3', width=500, height=360)
    defil2.place(x=700, y=150)
    nom1=Label(fen, bg='blue',text="Je suis un programmeur",font="AG 20",fg="cyan")
    nom1.place(x=150, y=600, width=500, height=100)
    nom2=Label(fen, bg='blue',text="Je suis un programmeur",font="AG 20",fg="cyan")
    nom2.place(x=700, y=600, width=500, height=100)
    quitter=Label(fen,text="QUITTER",font="arial 15",bg="white",fg="white",relief=FLAT,borderwidth=20)
    quitter.place(x=1230,y=10)
    lancer=Button(fen,text="COMMENCER LE BINÔMAGE",font="arial 15",bg="turquoise4",command=start)
    lancer.place(x=550,y=710)
    butretour=Button(fen,text="RETOUR",font='Callibri 15',bg="turquoise4",command=retour)
    butretour.place(x=80, y=10)
    stoptout=0
    fen.mainloop()
    fen.quit()
"""-----------------------------------------------------------------------------------------"""
""" ------------------------ FONCTION DE DEFILEMENT ALEATOIRE DES IMAGES ------------------- """
"""Initialisation de valeur"""
flag,posP,posF,q=0,0,0,0
BinoP=[]
BinoF=[]
tv=[]
photoP= ['1.PNG', '2.PNG', '3.PNG', '4.PNG', '5.PNG', '6.PNG', '7.PNG', '8.PNG', '9.PNG', '10.PNG', '11.PNG', '12.PNG', '13.PNG', '14.PNG', '15.PNG', '16.PNG', '17.PNG', '18.PNG', '19.PNG', '20.PNG', '21.PNG', '22.PNG', '23.PNG', '24.PNG', '25.PNG', '26.PNG', '27.PNG', '28.PNG', '29.PNG', '30.PNG', '31.PNG', '32.PNG', '33.PNG', '34.PNG', '35.PNG', '36.PNG', '37.PNG', '38.PNG', '39.PNG', '40.PNG', '41.PNG', '42.PNG', '43.PNG', '44.PNG', '45.PNG', '46.PNG', '47.PNG', '48.PNG', '49.PNG', '50.PNG', '51.PNG', '52.PNG', '53.PNG', '54.PNG', '55.PNG', '56.PNG', '57.PNG', '58.PNG', '59.PNG', '60.PNG', '61.PNG', '62.PNG', '63.PNG', '64.PNG', '65.PNG', '66.PNG', '67.PNG', '68.PNG', '69.PNG', '70.PNG', '71.PNG', '72.PNG', '73.PNG', '74.PNG', '75.PNG', '76.PNG', '77.PNG', '78.PNG', '79.PNG', '80.PNG', '81.PNG', '82.PNG', '83.PNG', '84.PNG', '85.PNG', '86.PNG', '87.PNG', '88.PNG', '89.PNG', '90.PNG', '91.PNG', '92.PNG', '93.PNG', '94.PNG', '95.PNG', '96.PNG', '97.PNG', '98.PNG', '99.PNG', '100.PNG', '101.PNG', '102.PNG']
photoF= ['1a.PNG', '2a.PNG', '3a.PNG', '4a.PNG', '5a.PNG', '6a.PNG', '7a.PNG', '8a.PNG', '9a.PNG', '10a.PNG', '11a.PNG', '12a.PNG', '13a.PNG', '14a.PNG', '15a.PNG', '16a.PNG', '17a.PNG', '18a.PNG', '19a.PNG', '20a.PNG', '21a.PNG', '22a.PNG', '23a.PNG', '24a.PNG', '25a.PNG', '26a.PNG', '27a.PNG', '28a.PNG', '29a.PNG', '30a.PNG', '31a.PNG', '32a.PNG', '33a.PNG', '34a.PNG', '35a.PNG', '36a.PNG', '37a.PNG', '38a.PNG', '39a.PNG', '40a.PNG', '41a.PNG', '42a.PNG', '43a.PNG', '44a.PNG', '45a.PNG', '46a.PNG', '47a.PNG', '48a.PNG', '49a.PNG', '50a.PNG', '51a.PNG', '52a.PNG', '53a.PNG', '54a.PNG', '55a.PNG', '56a.PNG', '57a.PNG', '58a.PNG', '59a.PNG', '60a.PNG', '61a.PNG', '62a.PNG', '63a.PNG', '64a.PNG', '65a.PNG', '66a.PNG', '67a.PNG', '68a.PNG', '69a.PNG', '70a.PNG', '71a.PNG', '72a.PNG', '73a.PNG', '74a.PNG', '75a.PNG', '76a.PNG', '77a.PNG', '78a.PNG', '79a.PNG', '80a.PNG', '81a.PNG', '82a.PNG', '83a.PNG', '84a.PNG', '85a.PNG', '86a.PNG', '87a.PNG', '88a.PNG', '89a.PNG', '90a.PNG', '91a.PNG', '92a.PNG', '93a.PNG', '94a.PNG', '95a.PNG', '96a.PNG', '97a.PNG', '98a.PNG', '99a.PNG', '100a.PNG', '101a.PNG', '102a.PNG', '103a.PNG', '104a.PNG', '105a.PNG', '106a.PNG', '107a.PNG', '108a.PNG', '109a.PNG', '110a.PNG', '111a.PNG', '112a.PNG', '113a.PNG', '114a.PNG', '115a.PNG', '116a.PNG', '117a.PNG', '118a.PNG']
nomF=['ABBY BLAGUET ', 'AKA YAH LAETITIA', 'AMANI KOUAKOU ', 'AMON WOTCHE', 'ATSÉ-ACHI HELENA', 'BABAGBETO DOSSI ', 'BALET KACOU', 'BAYO ABOUBAKAR', 'BROU RITA ', 'CAMARA KPAGNIMIN ', 'CHERIF DIAHOU', "CISSE N'FA ADAMA", 'COULIBALY CECILE', 'COULIBALY FADOUGA', 'COULIBALY KATIANA  AICHA', 'COULIBALY KLANA AMARA ', 'COULIBALY KPINTCHA SHEKINA', 'COULIBALY SOHOLO', 'COULIBALY YÉLÉ', 'COULIBALY ZANAN', 'DABIE ABRAHAM GNADJA ', 'DEDI IVAN', 'DEMBELE ABOUBAKAR', 'DEMBELE DRISSA', 'DIABAGATE ABOUBAKARY', 'DIABAGATE BASSIRA', 'DIALLO ABDOULAYE', 'DIALLO AÏSSATOU', 'DIALLO CHEICK HAMED', 'DIALLO MOUSSA', 'DIARRA SEYDOU', 'DIARRASSOUBA FOUGNIGUE', 'DIEGAÏ BELEY', 'DIOMANDE GOLOU', 'DOSSO MOHAMED ROMARIC ', 'EHUI EBRINWA', 'ESSOH YANNIS PIERRE', 'FOFANA ADJA MADOUSSOU', 'FOFANA MORY', 'FOFANA MÉISSÉ', 'GAYE HAIDA', 'GEGEH KODJO VALENTIN', 'GLAI JEAN JULES', 'GOLI AKISSI JEMIMA', 'HAGBONOU ABRAHAM', 'HOUPHOUET YAO JEAN DE DIEU', 'KAKOU JOHAN DIDIER GNOHOHI', 'KAMBO BI GOULEZ HAROLD MARC-ELIE', 'KATO GRACE MANUELLE', 'KOBA NDA AUXEL ROLAND', 'KODJO AMON EUGENE ARNAUD', 'KOFFI AFFOUÉ GRACE DIVINE PRISCILLA ', 'KOFFI KOUASSI CLOVIS ARISTIDE', 'KONATÉ ABDEL AZIZ', 'KONE MOUSSA', "KONE NIAMKEY JEANNE D'ARC", 'KONE SIEMMIN AMA FATIM', 'KONE WOROGBE ', 'KOUADIO APHEY ', 'KOUADIO KAN CYRILLE ', 'KOUAKOU EUNICE ', 'KOUAME HENRI JOEL', 'KOUAME YAO RAOUL', 'KOUROUMA KOULAKO', 'KROKO KOUADIO DIEUDONNE ANICET', 'LOGNON GRACE ANGE MANUELLA', 'LY CHARNON HADIJ', 'MADOUKOU ULRICH ALAN ', 'MAHAMOUD ABDALLAH DIAB', 'MAIGA ZAOUZATA', 'MIMI CARINE MARIE FLORA', "N'DA AYA ANGE CARELLE", "N'DRI BI NADY TONY WILLIAMS ", "N'GOLE KOUASSI  FABRICE ", "N'GORAN ASSAMALA ROSE VALERIE", "N'GUESSAN KONAN GÉRÉMI", "N'GUESSAN NATACHA", "N'GUESSAN YAO", 'NANOU EKORA', 'NGOMA MKOMBO JUDELVY', 'OBAMBI ANDREA ', 'OGOUMOND DON ', 'OKOUA YAN MURIEL', 'ONGOUYA OHOULOU ', 'OUATTARA FOUGNIGUE ', 'OUEDRAOGO ISSA', 'OWOADE STEPHANIE', 'SANGARE MACAGBE', 'SANHO MOHAMED ', 'SASSA DELY HERMANN', 'SILUE DONAKPOR YACOUBA ', 'SILUE KOLO ESTHER', 'SILUE PELEBIN', 'TAHI BONGNET  YVES DAVID', 'THIO YELATO', 'THOMPSON AHAUBAUT', 'TIA CARELLE', 'TOURE ABOUDRAMANE', 'TOURE DIBONAN ANICET', 'TOURE FATIM', 'TOURE NATOYELE MATHIEU', 'TOURE YEGNAN ROMARIC', 'TOURE YENE MANDAMA', 'TRAORE KINAMPARY', 'YAI GUEHAYIBI', 'YAO ANGE ARMEL', 'YAO ASSAMOI', 'YAO KOUADIO', 'YAO KOUAKOU ABEL', 'YAO KRAMO', 'YAO YAO HERMANN', 'YAPO CLAUDE', 'YEBOUET MARIE-GRACE ', "YEO N'GANZA", 'YEO NALAHA BAKARY', 'YEO YEFOUNGNIGUI', 'ZADI JONATHAN ', 'ZAOUI SARA VOLENNA']
nomP=['ABAYE YAWO KEVIN', 'ABONGA KOCHE ', 'ADJEI AKOUA ', "AHIMAN N'NOGBOU ", 'AKA ADJOUA AUDREY', 'ANE KOUASSI ', 'ANZI ABOH JEAN ', 'ASSA MOAHEY', 'BAH ALHOUSSEINI', 'BAH SOULEYMANE', 'BAMBA HADJA ', 'BANCOULI DJOMAN', 'BEUGRE YVAN', 'BONI AMANI  DAVID', 'COULIBALY CHONCODJIRIKI', 'COULIBALY DJENEBA', 'COULIBALY KATI ', 'COULIBALY ZIE LACINA', 'DAGNOGO ZIE IBRAHIM', 'DIABATE MOHAMED', 'DIANE ABDOUL AZIZ', 'DIARRA MOHAMED', 'DIARRASSOUBA KHADARA', 'DINE MOREIRA AMIRATH', 'DJAH SERGES ', 'DJOGO CHO ', 'DOKI KOFFI', 'DOUKOURE AICHA ', 'FOFANA MORIKOUNADI', 'GNABA MARIE-NOELLE ', 'GNANZOU KACOU ', 'GOMA BOUTANDOU', 'GOUHO BI WIZAN', 'GUEI SALOMON', 'IPAUTE HENRI', 'KADIO BLEDOU', 'KASSI IGNAS ', 'KIANG EUNICE  ', 'KOFFI KOUAME GUILLAUME ', "KOFFI N'TAKPE ", 'KOMELA CHAYE ANGE', 'KONAN MARIELLE AURORE', 'KONE ISAAC', 'KONE KAMBO', 'KONE MARIAM', 'KOTIA ADOU AXEL MONDESIR ', 'KOTTA KRAGBE DAVID', 'KOUA AIBA MARIE NOELLE ', 'KOUADIO FRANK JUNIOR', 'KOUADIO KOFFI GUY-SERGE', 'KOUADIO KOUAKOU STEPHANE BRANDONE', 'KOUAKOU AMENAN SILVERE AUDREY', 'KOUAKOU GOSSOWLY SOUANGA DE L. I.', 'KOUAKOU OUATTARA', 'KOUAME ALLA HENRI EMMANUEL', 'KOUAME BOUAFFON HERMANN', 'KOUAME FOUA LOU', 'KOUAME JEAN EMMANUEL', 'KOUAME VANESSA', 'KOUASSI DABILA  ARAMATOU', 'KOUASSI JEAN-FRANCOIS', 'KOUASSI KOFFI', 'KOUASSI KOUADIO AIME', 'KOUASSI KOUAME', 'KOUASSI NELLY', 'LANTA HONORINE', "M'BRA KOUAME", 'MAHAN OUNSEGUI JUDITH MELAINE', 'MIAN KOUADIO PAUL YVES ETTIEN', "N'GUESSAN ANOMAN N'DRI YANNICK", "N'GUESSAN BOGUI", "N'GUESSAN N'FALLY RONALD CAUPHY", "N'GUESSAN YAO BERTIN", "N'ZUE KOUASSI WILFRIED", 'NA ABY NA JUDE ALEXANDRE', 'NAKY DJOUWO', 'OPOKOU ADJOBI .', 'OUATANTIEN KONE', 'RIMKA AL WARIS', 'OUATTARA HABIBA', 'OULAI DEGNAN ', 'SAHIRY MANUELA', 'SALE SAINT', 'SANGARE AWA', 'SANKARA MOISE', 'SANOGO TENIN', 'SIDIBE ABDOUL KARIM', 'SIMIAN DAOUDA', 'SORO KOLO ARNAUD', 'SORO TCHEREGNIMIN', 'SYLLA LADJI', 'SYLLA THIERNO MOUSSA', 'TIZIE ASSAMOA', 'TOGBA ZEH REBECCA', 'TOURE CHEICK', 'TOURE NAGNINLBAN', 'TOURE YINFAN', 'TUO ZANA', 'YAO GLE YAO ', 'YAO REGIS ', 'YAPO APIE', 'YEGBE BETSALEEL']
z=0
controle=0
def melindice(x):
    indtableau=[]
    indice=randint(0,len(x)-1)
    for i in range(len(x)):
        while indice in indtableau:
            indice=randint(0,len(x)-1)
        indtableau.append(indice)
    return indtableau
fin=open('fin.txt','w')
fin.close()
def defiler():
    global z,controle,pd,pf,defil1,defil2,nomP,nomF,posP,posF,flag,photoP,photoF,nom1,nom2,TP,TF,TNP,TNF,tindp,tindf,q
    if len(photoP)!=0 and len(photoF)!=0:
        TP=photoP.copy()
        TF=photoF.copy()
        TNP=nomP.copy()
        TNF=nomF.copy()
        if q==0:
            tindp=melindice(TNP)
            tindf=melindice(TNF)
            ve=[]
            nP=tindp.copy()
            nF=tindf.copy()
            fP=TP.copy()
            fF=TF.copy()
            if len(fP)<len(fF):
                for i in range(len(fF)-len(fP)):
                    s=randint(0,len(fP)-1)
                    while s in ve and len(fP)!=1:
                        s=randint(0,len(fP)-1)
                    ve.append(s)
                    TP.append(fP[s])
                    tindp.append(nP[s])
            elif len(fP)>len(fF):
                for i in range(len(fP)-len(fF)):
                    s=randint(0,len(fF)-1)
                    while s in ve and len(fF)!=1:
                        s=randint(0,len(fF)-1)
                    ve.append(s)
                    TF.append(fF[s])
                    tindf.append(nF[s])
            q+=1
        if (posP<(len(TP))):
            pd=TP[tindp[posP]]
            photoa=PhotoImage(file=pd)
            defil1.create_image(250,180,image=photoa)
            pd=TNP[tindp[posP]]
            nom1.configure(text=pd)
        posP+=1
        if (posF<(len(TF))):
            pf=TF[tindf[posF]]
            photob=PhotoImage(file=pf)
            defil2.create_image(250,180,image=photob)
            pf=TNF[tindf[posF]]
            nom2.configure(text=pf)
        posF+=1
        if (posP==(len(TP))):
            posP=0
        if (posF==(len(TF))):
            posF=0
        if (flag>0) and (z<6):
            z+=1
            fen.after(1000*1,defiler)
        else:
            pass
            le_binomage()
        fen.mainloop()


index=0
temps=5000
def le_binomage():
    global index,controle,temps
    defil1.delete(ALL)
    defil2.delete(ALL)
    pd=TP[tindp[index]]
    photoa=PhotoImage(file=pd)
    defil1.create_image(250,180,image=photoa)
    pd=TNP[tindp[index]]
    nom1.configure(text=pd)
    pf=TF[tindf[index]]
    photob=PhotoImage(file=pf)
    defil2.create_image(250,180,image=photob)
    pf=TNF[tindf[index]]
    nom2.configure(text=pf)
    index+=1
    fin=open('fin.txt','a')
    line='{} <===> {}\n'.format(pd,pf)
    fin.write(line)
    fin.close()
    fen.after(temps,stop)
    controle+=1
    fen.mainloop()




def stop():
        global flag,z,controle,index
        flag=0
        z=0
        if index!=len(tindf):
            defil1.delete(ALL)
            defil2.delete(ALL)
            start()
        else:
            time.sleep(3)
            fond=Canvas(fen,width=1366,height=768,bg="white")
            photo=PhotoImage(file= "0.PNG")
            fond.create_image(683,345,image=photo)
            fond.grid(row=0)
            u="""    FIN DU
BINNOMAGE"""
            fond.create_text(fen.winfo_screenwidth()//2,fen.winfo_screenheight()//2,text=u,fill="blue",font=" algerian 150")
            fen.mainloop()
def start(event=""):
        global flag,TBinoP,TBinoF
        if flag==0:
            flag=1
            defiler()
"""Permert de quitter le programme"""  
def quitter(event=""):
    global retour,butretour
    from tkinter.messagebox import askyesno
    rep = askyesno("QUITTER LE PROGRAMME","VOULEZ-VOUS QUITTER ?")
    if rep:
        fen.quit()
        fen.destroy()
"""------------------  REMPLISSAGE DES COORDONNEES PARRAINS ET FILLEULS    -----------------"""
def preced():
    global verif,nomP,nomF,photoP,photoF
    if verif=="PARRAINS":
        nomP=nomP[:len(nomP)-1]
        photoP=photoP[:len(photoP)-1]
        parrains()
    else:
        photoF=photoF[:len(photoF)-1]
        nomF=nomF[:len(nomF)-1]
        filleuls()
def parrains(event=""):
    global verif
    verif='PARRAINS'
    enregistrement(verif)
def filleuls(event=""):
    global verif
    verif='FILLEULS'
    enregistrement(verif)
def parcourir() :
    global ephoto,enregistrer,butenregistrer,entnom,photoP,photoF
    photo = askopenfilename()
    photo1 = PhotoImage(file=photo)
    ephoto.create_image(190, 190, image=photo1)
    if verif=="PARRAINS":
        photoP.append(photo1)
    else:
        photoF.append(photo1)
    if len(photo)!=0:
        entnom= Entry(fen, fg='black', width=63,relief=SUNKEN, borderwidth=2)
        entnom.place(x=470, y=500)
        entnom.focus_set()
        butenregistrer= Button(fen, text='Enregistrer', font='Callibri 18',bg='blue', command=enregistrer)
        butenregistrer.place(x=600, y=545)
    fen.mainloop()
    fen.quit()
def enregistrer(event=""):
    global nomP,entnom,ephoto,fermentry,butenregistrer,enregistrer,nomF,lbp,lbf
    nom=entnom.get()
    entnom.delete(0,"end")
    ephoto.delete(ALL)
    if verif=="PARRAINS":
        nomP.append(nom)
        lbp.insert(0,nom)
    else:
        nomF.append(nom)
        lbf.insert(0,nom)
    fermenrigistrer=Label(fen, text='Enregistrer', font='Callibri 18', bg='gray', relief=FLAT, borderwidth=9)
    fermenrigistrer.place(x=600,y=545)
    fermentry= Label(fen,relief=GROOVE, bg='gray', width=54)
    fermentry.place(x=470, y=500)
"""------------------------------------ PROGRAMME PRINCIPAL ---------------------------------"""
fen=Tk()

fen.attributes("-fullscreen",1)
fond=Canvas(fen,width=fen.winfo_screenwidth(),height=fen.winfo_screenheight(),bg="white")
photo=PhotoImage(file="0.PNG")
fond.create_image(683,345,image=photo)
fond.grid(row=0)
butretour=Button(fen,text="RETOUR",font='Callibri 15',bg="turquoise4",command=retour)
eparains=Button(fen,text="ENTRER NOM DES PARRAINS",font="arial 15",bg="turquoise4",command=parrains)
eparains.place(x=40,y=700)
efilleuls=Button(fen,text="ENTRER NOM DES FILLEULS",font="arial 15",bg="turquoise4",command=filleuls)
efilleuls.place(x=550,y=700)
aalancement=Button(fen,text="FIN DE L'ENREGISTREMENT",font="arial 15",bg="turquoise4",command=fendelancement)
aalancement.place(x=1040,y=700)
bquitter=Button(fen,text="QUITTER",font="arial 15",bg="turquoise4",command=quitter)
bquitter.place(x=1230,y=10)
"""-------------------------------- LES TOUCHES CLAVIERS -----------------------------------"""
fen.bind("<Escape>",start)
fen.bind("<Return>", enregistrer)
fen.bind("<Alt-p>", parrains)
fen.bind("<Alt-f>",filleuls )
fen.bind("<Alt-w>", fendelancement)
fen.mainloop()
