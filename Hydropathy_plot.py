# G		Glycine		Gly									P		Proline		    Pro
# A		Alanine		Ala									V		Valine		    Val
# L		Leucine		Leu									I		Isoleucine		Ile
# M		Methionine		Met								C	    Cysteine		Cys
# F		Phenylalanine		Phe							Y		Tyrosine		Tyr
# W		Tryptophan	    Trp								H		Histidine		His
# K		Lysine		Lys									R		Arginine		Arg
# Q		Glutamine		Gln								N		Asparagine		Asn
# E		Glutamic Acid		Glu							D		Aspartic Acid	Asp
# S		Serine		Ser									T		Threonine		Thr

import tkinter
# dpi stands for dots per inches
from tkinter import Checkbutton, Image, IntVar, PhotoImage, StringVar, ttk
from tkinter.constants import BOTTOM, CENTER, LEFT
from typing import KeysView

import matplotlib.figure as Fig
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageTk
import tkhtmlview

# from tkinter.ttk import *



class Hydropathy :

    # print(self.aminoAcids[3])
    def __init__(self,sequence):
        self.databaseSqn = {'G':'Glycine', 'P':'Proline', 'A':'Alanine', 'V':'Valine' ,'L':'Leucine', 'I':'Isoleucine', 'M':'Methionine', 'C':'Cysteine', 'F':'Phenylalanine', 'Y':'Tyrosine', 'W':'Tryptophan', 'H':'Histidine', 'K':'Lysine', 'R':'Arginine', 'Q':'Glutamine', 'N':'Asparagine', 'E':'GlutamicAcid', 'D':'Aspartic Acid', 'S':'Serine','T':'Threonine'}
        self.database = {'Asparagine':-3.5,'Valine':4.2,'Glycine':-0.4,'Proline':-1.6,'Alanine':1.8,'Histidine':-3.2,'GlutamicAcid':-3.5,'Leucine':3.8,'Isoleucine':4.5,'Aspartic Acid':-3.5,'Methionine':1.9,'Tyrosine':-1.3,'Tryptophan':-0.9,'Phenylalanine':2.8,'Serine':-0.8,'Cysteine':2.5,'Glutamine':-3.5,'Arginine':-4.5,'Threonine':-0.7,'Asparagine':-3.5,'Lysine':-3.9}
        self.aminoAcids = list(self.database.keys())
        self.sequence = str(sequence).upper()
        self.info = list(self.sequence)
    def protein(self):
        num = len(self.info)-8
        for n in range(len(self.info)):
            self.info[n]=self.databaseSqn.get(f"{self.info[n]}")
            self.info[n]=self.database.get(f"{self.info[n]}")
        for n in range(0,len(self.info)):
                # self.info[n] = (self.info[n]+self.info[n+1]+self.info[n+2])/3
                if n==num:
                    while len(self.info)!=num:
                        self.info.pop(-1)
                    break
                else:
                    try:
                        self.info[n] = (self.info[n]+self.info[n+1]+self.info[n+2]+self.info[n+3]+self.info[n+4]+self.info[n+5]+self.info[n+6]+self.info[n+7]+self.info[n+8])/9
                    # print(self.info)
                    except:
                        break
        x = np.arange(4,len(self.info)+4)
        y =(self.info)
        plt.grid()
        plt.bar(x,y, color = 'blue')
        plt.axhline(y=0,linestyle=':')
        plt.title('Hydropathy Plot')
        plt.xlabel('Amino Acid')
        plt.ylabel('Hydropathy Index')
        plt.show()




# temp = Hydropathy('MGLSDGEWQLVLNVWGKVEADIPGHGQEVLIRLFKGHPETLEKFDKFKHLKSEDEMKASEDLKKHGATVLTALGGILKKKGHHEAEIKPLAQSHATKHKIPVKYLEFISECIIQVLQSKHPGDFGADAEGAMNKALELFRKDMASNYKELGFQG')
# temp.protein()

    window = tkinter.Tk()
    # window.minsize(500,400)
    # window.maxsize(1000,900)
    window.title('Hydropathy Plot')
    window.config(background='White')
    # label1 = tkinter.Label(text='GGlycineGly, PProlinePro, AAlanineAla, VValineVal, LLeucineLeu, IIsoleucineIle, MMethionineMet, CCysteineCys, FPhenylalaninePhe, YTyrosineTyr, WTryptophanTrp, HHistidineHis, KLysineLys, RArginineArg, QGlutamineGln, NAsparagineAsn, EGlutamicAcidGlu, DAspartic AcidAsp, SSerineSer, TThreonineThr').pack()

# def Nucleotide_chk():
    # Nucleotide_self.database = {}
    
# img = ImageTk.PhotoImage(Image.open('D:\My Files\python\List-of-amino-acids-abbreviations.png'))
# ButImg = tkinter.Button(window,image=img).pack()
ProSqn = tkinter.StringVar()
SingleSeq = ttk.Entry(window, width = 50, textvariable=ProSqn).pack()


# var = StringVar(window,"1")

# values = {"Nucleotide sequence":"0", "Amino acids sequence":"1"}
# for (text, value) in values.items():
#     tkinter.Radiobutton(window, text = text, variable = var,
#                 value = value, indicator = 0,
#                 background = "light blue").pack()

# def check(var):
#     if var == '0':
#         data()
#     elif var == '1':
trial = Translation()
#         trial.ProtienSq(ProSqn.get())
# temp = ProSqn.get()
temp = ''

# MainLable = tkinter.Label(window, text='Amino acid sequence').pack()
# but1 = tkinter.Button(window,text='Hydropathy plot',command=data).pack()
MainLable2 = tkinter.Label(window, text='Nucleotide sequence').pack()
but2 = tkinter.Button(window,text='Plot',command=protein(trial.ProtienSq(temp))).pack()
# def Doc():
with open('Hydropathy_plot.html','r') as file:
    content=file.read()
lable = tkhtmlview.HTMLLabel(window, html=content).pack()


# Help = tkinter.Button(window, text='Help', foreground='green',command=Doc()).pack()
window.mainloop()