from tkinter import *
from tkinter import messagebox
import webbrowser
from ctypes import windll

url = "https://www.youtube.com/results?search_query="
url2 = "https://www.google.com/search?client=firefox-b-d&q="
search_qg_text = "Search Google"
search_yt_text = "Search Youtube"

def quitter(e):
    root.quit()

def delete_qg_text(e):
    global search_qg_text
    search_qg.delete(0, END)
    search_qg.insert(0, "")
    root.bind("<Return>", enter_query_qg)

def delete_yt_text(e):
    global search_yt_text
    search_yt.delete(0, END)
    search_yt.insert(0, "")
    root.bind("<Return>", enter_query_yt)

def move_app(e):
    root.geometry(f"+{e.x_root}+{e.y_root}")

def popup():
    messagebox.askquestion('hello', 'hello')

def enter_query_qg(e):
    global url2
    if search_qg.get() == search_qg.get():
        url2 = url2 + search_qg.get()
        webbrowser.open(url2)

def enter_query_yt(e):
    global url
    if search_yt.get() == search_yt.get():
        url = url + search_yt.get()
        webbrowser.open(url)

def search_query():
    global url2
    if search_qg.get() == search_qg.get():
        url2 = url2 + search_qg.get()
        webbrowser.open(url2)

def search_query2():
    global url
    if search_yt.get() == search_yt.get():
        url = url + search_yt.get()
        webbrowser.open(url)

def link_e():
    webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

def link_m():
    webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

def link_m2():
    webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

root = Tk()
root.title("ELDSimple")
root.geometry("884x532")
root["bg"] = "indian red"



#removes titile bar
root.overrideredirect(True)
#create fake bar
title_bar = Frame(root, bg="darkgreen", relief="raised", bd=1, padx=6, pady=3)
title_label = Label(title_bar, text="ELDSimple", bg="darkgreen", font=("CenturySchoolbookl 10 bold"))
#binding title to title_bar
title_bar.bind("<B1-Motion>", move_app)

close_label = Label(title_bar, text=" X ", bg="darkgreen", fg="white", relief="sunken")
close_label.bind("<Button-1>", quitter)
space4 = Label(title_bar, bg="darkgreen", padx=383, pady=0, text="  ")
space4.bind("<B1-Motion>", move_app)
title_label.bind("<B1-Motion>", move_app)

space = Label(root,bg="indian red",)
space2 = Label(root,bg="indian red",)
bg_frame = LabelFrame(root, bg="indian red", padx=10, pady=10)
lbl = LabelFrame(bg_frame, bg="indian red", fg="white", text="ELDSimple", padx=5, pady=5, font=('CenturySchoolbookl 10 bold'))
lbl3 = LabelFrame(lbl, padx=5, pady=5, bg="red4",)
lbl_search1 = LabelFrame(lbl, bg="goldenrod", padx=5, pady=5)
lbl_search2 = LabelFrame(lbl, bg="maroon", padx=5, pady=5)
lbl_g_query = LabelFrame(lbl, bg="goldenrod", padx=5, pady=5)
lbl_yt_query = LabelFrame(lbl, bg="maroon", padx=5, pady=5)
space3 = Label(lbl3, padx=1, pady=140)
search_qg = Entry(lbl_g_query, width=50, font=("Arial 20"), bg="indian red", fg="goldenrod")
search_yt = Entry(lbl_yt_query, width=50, font=("Arial 20"), bg="indian red", fg="maroon")
search_qg.bind("<Button-1>", delete_qg_text)
search_yt.bind("<Button-1>", delete_yt_text)


button1 = Button(lbl, text="Email", font=('Arial 20'), bg="indian red", command=link_e, padx=339, pady=29)
button2 = Button(lbl, text="Email", font=('Arial 20'), bg="indian red", command=link_m, padx=339, pady=30)
button3 = Button(lbl, text="Email", font=('Arial 20'), bg="indian red", command=link_m2, padx=339, pady=28)
search1 = Button(lbl_search1, text="Search", font=('Arial 12'), bg="indian red", command=search_query, padx=1, pady=5)
search2 = Button(lbl_search2, text="Search", font=('Arial 12'), bg="indian red", command=search_query2, padx=1, pady=5)
help_b = Button(lbl3, text="Help", bg="red4", font=('Arial 11'), command=popup, padx=11, pady=145)




title_bar.grid(row=0, column=0, sticky="nw")
title_label.grid(row=0, column=1)
close_label.grid(row=0, column=6)
space4.grid(row=0, column=5)

bg_frame.grid(row=1, column=0)
search_yt.grid(row=4, column=1)
search_qg.grid(row=0, column=0)
lbl_g_query.grid(row=0, column =1)
lbl_yt_query.grid(row=4, column=1)
lbl_search1.grid(row=0, column=2)
lbl_search2.grid(row=4, column=2)
#creates space on grid
space.grid(row=0, column=1)
space2.grid(row=1, column=4)
#space3.grid()
lbl.grid(row=2, column=3)
lbl3.grid(rowspan=3, row=1, column=2, columnspan=5)
button1.grid(row=1, column=1)
button2.grid(row=2, column=1)
button3.grid(row=3, column=1)
search1.grid(row=0, column=0, sticky="n")
search2.grid(row=2, column=0, sticky="n")
help_b.grid(row=1, column=0)
search_qg.insert(0, search_qg_text)
search_yt.insert(0, search_yt_text)

root.mainloop()