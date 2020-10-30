from tkinter import *
import tkinter
import tkinter as tk
import requests
from tkinter import messagebox,filedialog
import webbrowser

def single():
	textShow.delete("1.0",END)
	url=urlEntry.get()
	if(url==""):
		messagebox.showerror("Error","No URL Given")
	else:
		try:
			scan=requests.get(url)
			showText=f"{url} -------> {scan.status_code}"
			textShow.insert(END,showText)
		except:
			showText=f"{url} -------> URL Error"
			textShow.insert(END,showText)

def bulk():
	textShow.delete("1.0",END)
	fileName=urlPathEntry.get()
	if(fileName==""):
		messagebox.showerror("Error","No PATH Given")
	else:
		urList = open(fileName, 'r')
		url=(urList.readlines())
		for i in range(len(url)):
			a=url[i]
			a=a.replace("\n","")
			a="http://"+a
			try:
				scan=requests.get(a)
				showText=f"{a} -------> {scan.status_code}\n"
				textShow.insert(END,showText)
			except:
				showText=f"{a} -------> URL Error\n"
				textShow.insert(END,showText)

def save():
	root.filename = filedialog.asksaveasfile(mode="w",defaultextension='.txt')
	if root.filename is None:
		return
	file_save =  str(textShow.get(1.0,END))
	root.filename.write(file_save)
	root.filename.close()

root=tk.Tk()
root.title("URL Response Checker | Manjunathan C")
root.geometry("1300x600")
root.config(bg="#ff6e40")
root.iconphoto(True,tk.PhotoImage(file="icon.png"))

urlLabel=Label(root,text="SINGLE URL SCAN",fg="#3b4d61",bg="#ff6e40",font=("courier",15,"bold italic"))
urlLabel.place(x=50,y=20)

urlEntry=Entry(root,bg="#3b4d61",fg="#ff6e40",font=("courier",15,"bold italic"),width=30,borderwidth=6)
urlEntry.place(x=50,y=50)

singleButtonScan=Button(root,text="Scan",bg="#3b4d61",fg="#ff6e40",font=("courier",15,"bold italic"),width=7,borderwidth=6,activebackground="white",command=single)
singleButtonScan.place(x=250,y=100)

singleButtonClear=Button(root,text="Clear",bg="#3b4d61",fg="#ff6e40",font=("courier",15,"bold italic"),width=7,borderwidth=6,activebackground="white",command=lambda:urlEntry.delete(0,END))
singleButtonClear.place(x=100,y=100)




pathLabel=Label(root,text="BULK URL SCAN",fg="#3b4d61",bg="#ff6e40",font=("courier",15,"bold italic"))
pathLabel.place(x=50,y=250)

urlPathEntry=Entry(root,bg="#3b4d61",fg="#ff6e40",font=("courier",15,"bold italic"),width=30,borderwidth=6)
urlPathEntry.place(x=50,y=290)

bulkButtonScan=Button(root,text="Scan",bg="#3b4d61",fg="#ff6e40",font=("courier",15,"bold italic"),width=7,borderwidth=6,activebackground="white",command=bulk)
bulkButtonScan.place(x=250,y=340)

pathButtonClear=Button(root,text="Clear",bg="#3b4d61",fg="#ff6e40",font=("courier",15,"bold italic"),width=7,borderwidth=6,activebackground="white",command=lambda:urlPathEntry.delete(0,END))
pathButtonClear.place(x=100,y=340)

textShow=Text(root,bg="#3b4d61",fg="#ff6e40",font=("courier",15,"bold italic"),width=60,height=16,borderwidth=6)
textShow.place(x=500,y=47)

textButtonClear=Button(root,text="Clear",bg="#3b4d61",fg="#ff6e40",font=("courier",15,"bold italic"),width=7,borderwidth=6,activebackground="white",command=lambda:textShow.delete("1.0",END))
textButtonClear.place(x=650,y=430)

textButtonSave=Button(root,text="Save",bg="#3b4d61",fg="#ff6e40",font=("courier",15,"bold italic"),width=7,borderwidth=6,activebackground="white",command=save)
textButtonSave.place(x=800,y=430)

exitButton=Button(root,text="Exit",bg="#3b4d61",fg="#ff6e40",font=("courier",15,"bold italic"),width=7,borderwidth=6,activebackground="white",command=lambda:root.destroy())
exitButton.place(x=950,y=430)

buttonContact=Button(root,text="Contact",bg="#3b4d61",fg="#ff6e40",font=("courier",15,"bold italic"),width=7,borderwidth=6,activebackground="white",command=lambda:webbrowser.open("https://github.com/cmanjunathan45"))
buttonContact.place(x=175,y=430)

root.mainloop()
