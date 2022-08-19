from tkinter import *
from itertools import permutations
import tkinter as tk
import time
root = tk.Tk()
root.title("Chordopolis")
root.resizable(False,False)
root.configure(bg = "black")
root.iconbitmap(r"icon.ico")
root.geometry("330x700")
bottomE = []
bottomE_vars = [IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar()]
a = []
a_vars = [IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar()]
d = []
d_vars = [IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar()]
g = []
g_vars = [IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar()]
b = []
b_vars = [IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar()]
topE = []
topE_vars = [IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar()]
bg = PhotoImage(file = "woodBoard.png")
# Show image using label
bg_image = Label( root, image = bg,bg = "black")
bg_image.place(x = 0, y = 0)
#Building Keys and placing them
for i in range(13):
  bottomE.append(tk.Checkbutton(root,text = str(i),bg = "#c87f39",variable = bottomE_vars[i], onvalue = 1, offvalue = 0))
  bottomE[i].grid(column=1,row=i,sticky="W",pady = 10,padx=5)
  
  a.append(tk.Checkbutton(root,text = str(i),bg = "#c87f39", variable = a_vars[i], onvalue = 1, offvalue = 0))
  a[i].grid(column=2,row=i,sticky="W",padx=5)

  
  d.append(tk.Checkbutton(root,text = str(i),bg = "#c87f39", variable = d_vars[i], onvalue = 1, offvalue = 0))
  d[i].grid(column=3,row=i,sticky="W",padx=5)

  
  g.append(tk.Checkbutton(root,text = str(i),bg = "#c87f39", variable = g_vars[i], onvalue = 1, offvalue = 0))
  g[i].grid(column=4,row=i,sticky="W",padx=5)

  
  b.append(tk.Checkbutton(root,text = str(i),bg = "#c87f39", variable = b_vars[i], onvalue = 1, offvalue = 0))
  b[i].grid(column=5,row=i,sticky="W",padx=5)

  
  topE.append(tk.Checkbutton(root,text = str(i),bg = "#c87f39", variable = topE_vars[i], onvalue = 1, offvalue = 0))
  topE[i].grid(column=6,row=i,sticky="W",padx=5)
chord_label = tk.Label(root, text = " waiting ",font=("Arial", 10),height = 2, width = 12,fg = "white",bg = "black" )
#Fret Labels
'''
label_0= tk.Label(root,text = "0")
label_0.grid(column = 7, row = 0)
label_3= tk.Label(root,text = "3")
label_3.grid(column = 7, row = 3)
label_5= tk.Label(root,text = "5")
label_5.grid(column = 7, row = 5)
label_7= tk.Label(root,text = "7")
label_7.grid(column = 7, row = 7)
label_9= tk.Label(root,text = "9")
label_9.grid(column = 7, row = 9)
label_12= tk.Label(root,text = "12")
label_12.grid(column = 7, row = 12)
'''
output_keys = [["E","F","FS","G","GS","A","AS","B","C","CS","D","DS","E"],["B","C","CS","D","DS","E","F","FS","G","GS","A","AS","B"],["G","GS","A","AS","B","C","CS","D","DS","E","F","FS","G"],["D","DS","E","F","FS","G","GS","A","AS","B","C","CS","D"],["A","AS","B","C","CS","D","DS","E","F","FS","G","GS","A"],["E","F","FS","G","GS","A","AS","B","C","CS","D","DS","E"]]
def rename_keys():
	global bottomE,a,d,g,b,topE
	#Renaming Keys
	#  E section
	bottomE[0].config(text = "E")
	bottomE[12].config(text = "E")
	a[7].config(text = "E")
	d[2].config(text = "E")
	g[9].config(text = "E")
	b[5].config(text = "E")
	topE[0].config(text = "E")
	topE[12].config(text = "E")
	#  A Sharp
	bottomE[6].config(text = "A♯")
	a[1].config(text = "A♯")
	d[8].config(text = "A♯")
	b[11].config(text = "A♯")
	g[3].config(text = "A♯")
	topE[6].config(text = "A♯")
	#  A
	bottomE[5].config(text = "A")
	a[0].config(text = "A")
	a[12].config(text = "A")
	d[7].config(text = "A")
	g[2].config(text = "A")
	b[10].config(text = "A")
	topE[5].config(text = "A")
	#  B
	bottomE[7].config(text = "B")
	a[2].config(text = "B")
	d[9].config(text = "B")
	g[4].config(text = "B")
	b[0].config(text = "B")
	b[12].config(text = "B")
	topE[7].config(text = "B")
	#  C♯
	bottomE[9].config(text = "C♯")
	a[4].config(text = "C♯")
	d[11].config(text = "C♯")
	g[6].config(text = "C♯")
	b[2].config(text = "C♯")
	topE[9].config(text = "C♯")
	#  C
	bottomE[8].config(text = "C")
	a[3].config(text = "C")
	d[10].config(text = "C")
	g[5].config(text = "C")
	b[1].config(text = "C")
	topE[8].config(text = "C")
	#  D♯
	bottomE[11].config(text = "D♯")
	a[6].config(text = "D♯")
	d[1].config(text = "D♯")
	g[8].config(text = "D♯")
	b[4].config(text = "D♯")
	topE[11].config(text = "D♯")
	#	D
	bottomE[10].config(text = "D")
	a[5].config(text = "D")
	d[0].config(text = "D")
	d[12].config(text = "D")
	g[7].config(text = "D")
	b[3].config(text = "D")
	topE[10].config(text = "D")
	#	F♯
	bottomE[2].config(text = "F♯")
	a[9].config(text = "F♯")
	d[4].config(text = "F♯")
	g[11].config(text = "F♯")
	b[7].config(text = "F♯")
	topE[2].config(text = "F♯")
	#	F
	bottomE[1].config(text = "F")
	a[8].config(text = "F")
	d[3].config(text = "F")
	g[10].config(text = "F")
	b[6].config(text = "F")
	topE[1].config(text = "F")
	#	G♯
	bottomE[4].config(text = "G♯")
	a[11].config(text = "G♯")
	d[6].config(text = "G♯")
	g[1].config(text = "G♯")
	b[9].config(text = "G♯")
	topE[4].config(text = "G♯")
	#	G
	bottomE[3].config(text = "G")
	a[10].config(text = "G")
	d[5].config(text = "G")
	g[0].config(text = "G")
	g[12].config(text = "G")
	b[8].config(text = "G")
	topE[3].config(text = "G")

rename_keys()
chords={}
with open("Chords.txt",'r') as f:
  chords={}
  for line in f.readlines():
    n,c=line.split('x')
    c = c.strip()
    c = c.replace(" ","")
    chords.update({c:n})
def check_keys():
	global bottomE_vars, a_vars,d_vars,g_vars,b_vars,topE_vars, chords, chord_label
	key = [topE_vars,b_vars,g_vars,d_vars, a_vars,bottomE_vars]
	c = 0
	d = 0
	output = []
	for i in key:
		for j in i:
			if j.get() == 1:
				output.append(output_keys[c][d])
			d +=1
			
		c+=1
		d=0
	output.sort()
	final_list = list(dict.fromkeys(output))
	all_combos = list(permutations(final_list, len(final_list)))
#print(final_list)
#print(all_combos)
#print("Lenght", len(all_combos))
	count = 0 
	for i in range(len(all_combos)):
		final_list = all_combos[i]
		final = ""
		for i in final_list:
			final += i
#print(final)
#print(count)
		count+=1
		if chords.get(final) == None:
			if count == len(all_combos):
				chord_label.config(text="None Found")
			else:
				continue
		else:
			sentence = chords.get(final).replace("S","♯")
			chord_label.config(text = (chords.get(final).replace("S","♯")))
			break
def reset():
	global bottomE,a,d,g,b,topE
	key = [bottomE,a,d,g,b,topE]
	for i in key:
		for k in i:
			k.deselect()
check = tk.Button(text = "Click for chord", command = check_keys, height = 2, width = 20,font=("Arial", 10),fg = "white",bg = "black")
check.place(x = 10, y = 602)
reset = tk.Button(text = "Click to reset", command = reset, heigh = 2, width = 35, font=("Arial", 10),fg = "white",bg = "black")
reset.place(x = 10, y = 650)
chord_label.place(x = 200, y = 605)
root.mainloop()
