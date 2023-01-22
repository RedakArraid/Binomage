from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import *
from random import randint
import time
import sys
from alea_image import fenetre
import sys
import pandas as pd
import numpy as np
class bino(object):
	"""docstring for HydroDk"""
	def __init__(self, tabp="",tabf=""):
		self.fen=Tk()
		self.fen.attributes("-fullscreen",1)
		self.h,self.l=self.fen.winfo_screenheight(),self.fen.winfo_screenwidth()
		self.pos=0
		self.niv=0
		self.fond=Canvas(self.fen,width=self.l,height=self.h,bg="white")
		self.photo=PhotoImage(file="1.png")
		self.fond.create_image(self.l//3,self.h//2.5,image=self.photo)
		self.fond.grid(row=0)
		self.fond.create_text(self.l//3+250,self.h//2.5,text="BIENVENU AU"+"\n"+"BINÔMAGE"+"\n"+"DE LA P46",font="Callibri 80",fill="orange")
		self.butretour=Button(self.fen,text="RETOUR",font='Callibri 15',bg="turquoise4",command="retour")
		self.blancer=Button(self.fond,text="ALLONS A LA DECOUVERTE"+"\n"+"DE VOS AINES DIRECTE",font="arial 15",bg="turquoise4",command=self.lancer2)
		self.blancer.place(x=self.l-int((self.l)*0.65),y=600)
		self.butretour.place(x=1230,y=10)
		self.but_charger=Button(self.fond,text="CHARGER DONNEES",font="arial 15",bg="turquoise4",command=self.charger)
		self.but_charger.place(x=10,y=100)
		
		self.fen.mainloop()
	def lancer2(self):
		self.fond.destroy()
		self.fond=Canvas(self.fen,width=self.fen.winfo_screenwidth(),height=self.fen.winfo_screenheight(),bg="white")
		self.photo=PhotoImage(file="1.PNG")
		self.fond.create_image(self.l//3,self.h//2.5,image=self.photo)
		self.fond.grid(row=0)
		self.butretour=Button(self.fen,text="RETOUR",font='Callibri 15',bg="turquoise4",command="retour")
		self.butretour.place(x=1230,y=10)
		self.fond.create_text(1250,200,text="A QUI LE TOUR ?",font="Callibri 50",fill="orange")
		self.chercher=Button(self.fen,text="JE CHERCHE",font='Callibri 40',bg="blue",fg="white",command=self.reserch)
		self.chercher.place(x=1000,y=300)
		self.sdtm=Button(None,text="SAHE DANS TA "+"\n"+"MAIN",font="arial 40",relief=FLAT,bg="red",command="",fg="white")
		self.sdtm.place(x=1000,y=600)
		self.can_aine=Canvas(self.fond,width=self.fen.winfo_screenwidth()//4,height=self.fen.winfo_screenheight()//2,bg="turquoise4")
		self.can_aine.place(x=10,y=200)
		self.can_fieul=Canvas(None,width=self.fen.winfo_screenwidth()//4,height=self.fen.winfo_screenheight()//2,bg="turquoise4")
		self.can_fieul.place(x=60+self.fen.winfo_screenwidth()//4,y=200)
		self.can_fieul1=Canvas(None,width=self.fen.winfo_screenwidth()//4,height=self.fen.winfo_screenheight()//2,bg="turquoise4")
		self.can_fieul1.place(x=60+self.fen.winfo_screenwidth()//4,y=200)
		self.labelf=Label(self.fond,font="Calibri20")
		self.labelp=Label(self.fond,font="Calibri20")
		self.labelp.place(x=60+380,y=120)
		self.labelf.place(x=10,y=200+500)
		
	def reserch(self):
		if self.niv==0:
			self.pf=PhotoImage(file=self.tab[0][1][self.pos])
			self.labelf.configure(text=self.tab[0][0][self.pos])
			self.can_aine.create_image(int(self.can_aine.winfo_screenwidth())//8,self.can_aine.winfo_screenheight()//4,image=self.pf)
			self.chercher.configure(command="",relief=RIDGE,bg="red")
			self.sdtm.configure(command=self.binomer,bg="blue",relief=GROOVE)
			self.niv=1

	def armoniser(self,t1,t2):
		if len(t1)>len(t2):
			for i in range(len(t1)-len(t2)):
				t2.append(t1[i])
		else:
			for i in range(len(t2)-len(t1)):
				t1.append(t2[i])
	def binomer(self):
		if self.niv==1:
			self.sdtm.configure(command="",relief=RIDGE,bg="red")
			self.pp=PhotoImage(file=self.tab[1][1][self.pos])
			self.labelp.configure(text=self.tab[1][0][self.pos])
			self.can_fieul1.create_image(int(self.l//8),self.h//4,image=self.pp)
			self.chercher.configure(command=self.reserch,bg="blue",relief=GROOVE)
			fin=open('fin.txt','a')
			line='{} <===> {}\n'.format(self.tab[1][0][self.pos],self.tab[0][0][self.pos])
			fin.write(line)
			fin.close()
			self.pos+=1
			self.niv=0
		
	def meltab(self,t):
	    b=[]
	    verif=[]
	    for i in range(len(t)):
	        j=randint(0,len(t)-1)
	        while j in verif:
	            j=randint(0,len(t)-1)
	        b.append(t[j])
	        verif.append(j)
	    return b
	def charger(self):
		self.data=askopenfilename()
		self.tab=[[self.recp_col(self.data,1),self.recp_col(self.data,2)],[self.recp_col(self.data,3),self.recp_col(self.data,4)]]
		v=randint(0,len(self.tab[0][0]))
		self.tab[0][0][-1]=self.tab[0][0][v]
		self.tab[0][1][-1]=self.tab[0][1][v]
		t1=[[self.tab[1][0][i],self.tab[1][1][i]] for i in range(len(self.tab[1][1]))]
		t2=[[self.tab[0][0][i],self.tab[0][1][i]] for i in range(len(self.tab[0][1]))]
		t1,t2=self.meltab(t1),self.meltab(t2)
		ta1,ta2,ta3,ta4=[t1[i][0] for i in range(len(t1))],[t1[i][1] for i in range(len(t1))],[t2[i][0] for i in range(len(t1))],[t2[i][1] for i in range(len(t1))]
		self.tab=[[ta1,ta2],[ta3,ta4]]
		#print("2 ",self.tab)
	def recp_col(self,fic,n):
		t=pd.read_excel(fic)
		return list(t[list(t.columns)[n-1]])

if __name__=="__main__":
	from tkinter import*
	from tkinter.filedialog import askopenfilename
	from tkinter.messagebox import *
	from random import randint
	import time
	
	limite=sys.getrecursionlimit()
	print(limite)
	sys.setrecursionlimit(2000)
	bino()
#Fenetre principale

"""-------------------------------- LES TOUCHES CLAVIERS -----------------------------------"""