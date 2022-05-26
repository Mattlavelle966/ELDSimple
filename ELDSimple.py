from tkinter import *
from tkinter import messagebox
import webbrowser

url = "https://www.youtube.com/results?search_query="
url2 = "https://www.google.com/search?client=firefox-b-d&q="
search_qg_text = "Search Google"
search_yt_text = "Search Youtube"

#tk is being initialized here and is creating our first window
root1 = Tk()
#geometry is setting the dimensions of the first window to "widthxheight"
root1.geometry("890x530")
#removing default Title bar.
root1.overrideredirect(True)
#changing background color 
root1["bg"] = "#003d80"

#creating window class 
class window(Frame):
    #creating first constructor for the window class 
    def __init__(self):
        #blueprinting/defining Frame, window object
        Frame.__init__(self)
        #creating new title bar to replace the default one 
        self.title_bar = Frame(self, bg="#001833", relief="raised", bd=1, padx=6, pady=3)
        #adds text to new title bar        
        self.title_bar.bind("<B1-Motion>", move_app)
        #binds left mouse click to move_app func which allows user to move the program window anywhere  
        self.title_label = Label(self.title_bar, fg="#0062cc", text="ELDSimple", bg="#001833", font=("CenturySchoolbookl 10 bold"))
        #binds label to move app func 
        self.title_label.bind("<B1-Motion>", move_app)

        #close_label is adding a small x that will allow user to close the program 
        self.close_label = Label(self.title_bar, text=" X ", bg="#001833", fg="#0062cc")
        #binds the close_label widget to the quitter fuction which will close the program     
        self.close_label.bind("<Button-1>", quitter)
        #space4 is creating a empty space in order to create the correct dimmensions for the title bar 
        self.space4 = Label(self.title_bar, bg="#001833", padx=385, pady=0, text="  ")
        #binding empty space to move app func
        self.space4.bind("<B1-Motion>", move_app)
       
       
        #creating the background frame 
        self.bg_frame = LabelFrame(self, bg="#001833", padx=10, pady=10)
        #creating inner frame with "ELDSimple"
        self.lbl = LabelFrame(self.bg_frame, bg="#001833", fg="#0062cc", text="ELDSimple", padx=5, pady=5, font=('CenturySchoolbookl 10 bold'))
        #lbl3 is creating a frame around our help button widget
        self.lbl3 = LabelFrame(self.lbl, padx=5, pady=5, bg="red4",)
        #creating a frame for the search1 button         
        self.lbl_search1 = LabelFrame(self.lbl, bg="goldenrod", padx=5, pady=5)
        #creating a frame for the search2 button
        self.lbl_search2 = LabelFrame(self.lbl, bg="maroon", padx=5, pady=5)
        #creating a frame around the search google entry widget 
        self.lbl_g_query = LabelFrame(self.lbl, bg="goldenrod", padx=5, pady=5)
        #creating a frame around the youtube search entry widget 
        self.lbl_yt_query = LabelFrame(self.lbl, bg="maroon", padx=5, pady=5)
        #entry widget where the user can enter whatever they would like to search on google
        self.search_qg = Entry(self.lbl_g_query, width=50, font=("Arial 20"), bg="#003d80", fg="goldenrod")
        #entry widget where the user can enter whatever they would like to search on youtube
        self.search_yt = Entry(self.lbl_yt_query, width=50, font=("Arial 20"), bg="#003d80", fg="maroon")
      


        #creating the first of the three shortcut buttons 
        self.button1 = Button(self.lbl, text="Email", font=('Arial 20'),fg="#001833", bg="#003d80", command=link_e, padx=339, pady=29)
        #creating the second of the three shortcut buttons
        self.button2 = Button(self.lbl, text="Email", font=('Arial 20'),fg="#001833", bg="#003d80", command=link_m, padx=339, pady=30)
        #creating the third of the three shortcut buttons
        self.button3 = Button(self.lbl, text="Email", font=('Arial 20'),fg="#001833", bg="#003d80", command=link_m2, padx=339, pady=28)
        #this button will activate search_query
        self.search1 = Button(self.lbl_search1, text="Search",fg="#001833", bg="#003d80", font=('Arial 12 bold'), command=search_query, padx=1, pady=5)
        #this button will activate search_query2
        self.search2 = Button(self.lbl_search2, text="Search",fg="#001833", bg="#003d80", font=('Arial 12 bold'), command=search_query2, padx=1, pady=5)
        #this is a help button that activates popup
        self.help_b = Button(self.lbl3, text="Help", fg="#001833", bg="#003d80", font=('Arial 11'), command=popup, padx=11, pady=145)

        '''each line of code here is taking the previously
         created widgets self.>>widget variable name<< and then calling the grid() function to display that widget in the grid'''   
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
        self.lbl.grid(row=2, column=3)
        self.lbl3.grid(rowspan=3, row=1, column=2, columnspan=5)
        self.button1.grid(row=1, column=1)
        self.button2.grid(row=2, column=1)
        self.button3.grid(row=3, column=1)
        self.search1.grid(row=0, column=0, sticky="n")
        self.search2.grid(row=2, column=0, sticky="n")
        self.help_b.grid(row=1, column=0)
        #these two lines add "Search Google" to the search_qg and search_yt entry widgets
        self.search_qg.insert(0, search_qg_text)
        self.search_yt.insert(0, search_yt_text)


#closes the program 
def quitter(e):
    quit()

#allows user to move the screen where ever you like 
def move_app(e):
    root1.geometry(f"+{e.x_root}+{e.y_root}")

#deletes text within the search_qg entry widget and binds <return> to enter_query_qg function
def delete_qg_text(e):
    #turns search_yt_text into a global variable 
    global search_qg_text
    root.search_qg.delete(0, END)
    root.search_qg.insert(0, "")
    root.search_qg.bind("<Return>", enter_query_qg)

#deletes text within the search_yt entry widget and binds <return> to enter_query_yt function
def delete_yt_text(e):
    #turns search_yt_text into a global variable 
    global search_yt_text
    root.search_yt.delete(0, END)
    root.search_yt.insert(0, "")
    root.search_yt.bind("<Return>", enter_query_yt)

#adds search_qg entry widget contents to the url2 variable and then opens it in the webbrowser with "e" as event parameter  
def enter_query_qg(e):
    #turns url2 into a global variable 
    global url2
    if root.search_qg.get() == root.search_qg.get():
        url2 = url2 + root.search_qg.get()
        webbrowser.open(url2)

#adds search_yt entry widget contents to the url variable and then opens it in the webbrowser with "e" as event parameter
def enter_query_yt(e):
    #turns url into a global variable 
    global url
    if root.search_yt.get() == root.search_yt.get():
        url = url + root.search_yt.get()
        webbrowser.open(url)

#adds search_qg entry widget contents to the url2 variable and then opens it in the webbrowser
def search_query():
    #turns url2 into a global variable 
    global url2
    if root.search_qg.get() == root.search_qg.get():
        url2 = url2 + root.search_qg.get()
        webbrowser.open(url2)

#adds search_yt entry widget contents to the url variable and then opens it in the webbrowser
def search_query2():
    #turns url into a global variable 
    global url
    if root.search_yt.get() == root.search_yt.get():
        url = url + root.search_yt.get()
        webbrowser.open(url)

#opens url link 
def link_e():
    webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

#opens url link
def link_m():
    webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

#opens url link
def link_m2():
    webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

#opens url link
def popup():
    messagebox.askquestion('hello', 'hello')

#initiating window object equal to root  
root = window()
#displaying window object
root.grid()
#binds close_label to left mouse click that activates quitter  
root.close_label.bind("<Button-1>", quitter)
#binds search_qg to left mouse click that activates delete_qg_text
root.search_qg.bind("<Button-1>", delete_qg_text)
#binds search_yt to left mouse click that activates delete_yt_text
root.search_yt.bind("<Button-1>", delete_yt_text)

root1.mainloop()