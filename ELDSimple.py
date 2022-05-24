from tkinter import *
from tkinter import messagebox
import webbrowser

url = "https://www.youtube.com/results?search_query="
url2 = "https://www.google.com/search?client=firefox-b-d&q="
search_qg_text = "Search Google"
search_yt_text = "Search Youtube"


root1 = Tk()
root1.geometry("884x532")
#removing default Title bar.
root1.overrideredirect(True)
root1["bg"] = "indian red"

class window(Frame):
    def __init__(self):

        Frame.__init__(self)
        self.title_bar = Frame(self, bg="darkgreen", relief="raised", bd=1, padx=6, pady=3)
        self.title_label = Label(self.title_bar, text="ELDSimple", bg="darkgreen", font=("CenturySchoolbookl 10 bold"))
        self.title_bar.bind("<B1-Motion>", move_app)

        self.close_label = Label(self.title_bar, text=" X ", bg="darkgreen", fg="white", relief="sunken")
        self.close_label.bind("<Button-1>", quitter)
        self.space4 = Label(self.title_bar, bg="darkgreen", padx=382, pady=0, text="  ")
        self.space4.bind("<B1-Motion>", move_app)
        self.title_label.bind("<B1-Motion>", move_app)

        self.space = Label(self,bg="indian red",)
        self.space2 = Label(self,bg="indian red",)
        self.bg_frame = LabelFrame(self, bg="indian red", padx=10, pady=10)
        self.lbl = LabelFrame(self.bg_frame, bg="indian red", fg="black", text="ELDSimple", padx=5, pady=5, font=('CenturySchoolbookl 10 bold'))
        self.lbl3 = LabelFrame(self.lbl, padx=5, pady=5, bg="red4",)
        self.lbl_search1 = LabelFrame(self.lbl, bg="goldenrod", padx=5, pady=5)
        self.lbl_search2 = LabelFrame(self.lbl, bg="maroon", padx=5, pady=5)
        self.lbl_g_query = LabelFrame(self.lbl, bg="goldenrod", padx=5, pady=5)
        self.lbl_yt_query = LabelFrame(self.lbl, bg="maroon", padx=5, pady=5)
        self.search_qg = Entry(self.lbl_g_query, width=50, font=("Arial 20"), bg="indian red", fg="goldenrod")
        self.search_yt = Entry(self.lbl_yt_query, width=50, font=("Arial 20"), bg="indian red", fg="maroon")
      



        self.button1 = Button(self.lbl, text="Email", font=('Arial 20'), bg="indian red", command=link_e, padx=339, pady=29)
        self.button2 = Button(self.lbl, text="Email", font=('Arial 20'), bg="indian red", command=link_m, padx=339, pady=30)
        self.button3 = Button(self.lbl, text="Email", font=('Arial 20'), bg="indian red", command=link_m2, padx=339, pady=28)
        self.search1 = Button(self.lbl_search1, text="Search", font=('Arial 12'), command=search_query, padx=1, pady=5)
        self.search2 = Button(self.lbl_search2, text="Search", font=('Arial 12'), command=search_query2, padx=1, pady=5)
        self.help_b = Button(self.lbl3, text="Help", bg="red4", font=('Arial 11'), command=popup, padx=11, pady=145)

        self.title_bar.grid(row=0, column=0, sticky="nw")
        self.title_label.grid(row=0, column=1)
        self.close_label.grid(row=0, column=6)
        self.space4.grid(row=0, column=5)

        self.bg_frame.grid(row=1, column=0)
        self.search_yt.grid(row=4, column=1)
        self.search_qg.grid(row=0, column=0)
        self.lbl_g_query.grid(row=0, column =1)
        self.lbl_yt_query.grid(row=4, column=1)
        self.lbl_search1.grid(row=0, column=2)
        self.lbl_search2.grid(row=4, column=2)
        #creates space on grid
        self.space.grid(row=0, column=1)
        self.space2.grid(row=1, column=4)
        self.lbl.grid(row=2, column=3)
        self.lbl3.grid(rowspan=3, row=1, column=2, columnspan=5)
        self.button1.grid(row=1, column=1)
        self.button2.grid(row=2, column=1)
        self.button3.grid(row=3, column=1)
        self.search1.grid(row=0, column=0, sticky="n")
        self.search2.grid(row=2, column=0, sticky="n")
        self.help_b.grid(row=1, column=0)
        self.search_qg.insert(0, search_qg_text)
        self.search_yt.insert(0, search_yt_text)



def quitter(e):
    quit()

def move_app(e):
    root1.geometry(f"+{e.x_root}+{e.y_root}")

def delete_qg_text(e):
    global search_qg_text
    root.search_qg.delete(0, END)
    root.search_qg.insert(0, "")
    root.search_qg.bind("<Return>", enter_query_qg)


def delete_yt_text(e):
    global search_yt_text
    root.search_yt.delete(0, END)
    root.search_yt.insert(0, "")
    root.search_yt.bind("<Return>", enter_query_yt)

def enter_query_qg(e):
    global url2
    if root.search_qg.get() == root.search_qg.get():
        url2 = url2 + root.search_qg.get()
        webbrowser.open(url2)

def enter_query_yt(e):
    global url
    if root.search_yt.get() == root.search_yt.get():
        url = url + root.search_yt.get()
        webbrowser.open(url)

def search_query():
    global url2
    if root.search_qg.get() == root.search_qg.get():
        url2 = url2 + root.search_qg.get()
        webbrowser.open(url2)

def search_query2():
    global url
    if root.search_yt.get() == root.search_yt.get():
        url = url + root.search_yt.get()
        webbrowser.open(url)

def link_e():
    webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

def link_m():
    webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

def link_m2():
    webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

def popup():
    messagebox.askquestion('hello', 'hello')


root = window()
root.grid()
root.close_label.bind("<Button-1>", quitter)
root.search_qg.bind("<Button-1>", delete_qg_text)
root.search_yt.bind("<Button-1>", delete_yt_text)
root1.mainloop()