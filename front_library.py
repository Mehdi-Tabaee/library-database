# LIBRARY MANAGEMENT FRONT
from tkinter import  *
import back_library
window = Tk()

window.title ( 'Library')
window.geometry( '500x400')






def clear():
    list1.delete( 0 , END)

def  insert(books):
    for book in books:
        list1.insert( END , book)


def view():
    clear()
    books = back_library.view()
    insert(books)


def search():
    clear()
    books = back_library.search( name_text.get() , issue_text.get() , auther_text.get() , publisher_text.get() , serialNo_text.get() , inventory_text.get() )
    insert(books)

def add():
    back_library.insert( name_text.get() , issue_text.get() , auther_text.get() , publisher_text.get() , serialNo_text.get() , inventory_text.get() )
    view()





# --- Labels ----
l1 = Label ( window , text= 'Name' )
l1.grid ( row = 0 , column = 0 )
l2 = Label ( window  , text= 'Topic')
l2.grid ( row = 0   , column = 2 )
l3 = Label ( window , text= 'Auther')
l3.grid ( row = 1 , column = 0 )
l4 = Label (window , text= 'Publisher')
l4.grid ( row = 1 , column = 2 )
l5 = Label( window , text= 'SerialNo')
l5.grid ( row = 2  , column = 0 )
l6 = Label (window , text= 'Inventory')
l6.grid ( row = 2 , column = 2 )

# --- Entries ----
name_text = StringVar()
e1 = Entry ( window , textvariable= name_text)
e1.grid ( row = 0 , column = 1  )
issue_text = StringVar()
e2 = Entry (window , textvariable= issue_text)
e2.grid ( row = 0 , column = 3 )
auther_text = StringVar()
e3 = Entry ( window , textvariable= auther_text)
e3.grid ( row = 1 , column = 1 )
publisher_text = StringVar()
e4 = Entry ( window , textvariable= publisher_text)
e4.grid ( row = 1 , column = 3 )
serialNo_text = StringVar()
e5 = Entry ( window , textvariable= serialNo_text)
e5.grid ( row = 2 , column = 1 )
inventory_text = StringVar()
e6 = Entry ( window , textvariable= inventory_text)
e6.grid ( row = 2 , column = 3 )

# -----ListBox-----
list1 = Listbox ( window , height= 6 , width= 35 )
list1.grid ( row = 3 , column = 0 , rowspan = 3 , columnspan = 3 )


def select(books):
    global selected_book
    if len ( list1.curselection()) > 0 :
        index = list1.curselection()[0]
        selected_book = list1.get(index)
        # name
        e1.delete( 0 , END )
        e1.insert( END , selected_book[1])
        # issue
        e2.delete(0 , END)
        e2.insert(END, selected_book[2])
        # auther
        e3.delete(0 , END)
        e3.insert(END, selected_book[3])
        # publisher
        e4.delete(0 , END)
        e4.insert(END, selected_book[4])
        # serialNo
        e5.delete(0 , END)
        e5.insert(END, selected_book[5])
        # inventory
        e6.delete(0 , END)
        e6.insert(END, selected_book[6])



list1.bind('<<ListboxSelect>>' , select)



def update():
    back_library.update( selected_book[0] , selected_book[1] , selected_book[2] , selected_book[3] , selected_book[4] , selected_book[5] )

def delete():
    back_library.delete( selected_book[0])
    view()

def close():
    window.destroy()


# ----- Scrollbar ----
sb1 = Scrollbar ( window)
sb1.grid ( row = 3 , column = 2 , rowspan = 15)
list1.configure( yscrollcommand= sb1.set)
sb1.configure( command= list1.yview)


# -----Button -----

b1 = Button ( window , text= 'View All ' , height= 3 ,  width= 15 , command= view )
b1.grid ( row = 3 , column = 0 )
b2 = Button ( window , text= 'Search' , height= 3 , width= 15 , command= search )
b2.grid ( row = 4 , column = 0 )
b3 = Button ( window , text= 'Add ' , height= 3 ,  width= 16 , command= add )
b3.grid ( row = 3 , column = 3 )
b4 = Button ( window , text= 'Update ' , height= 3 ,  width= 16 , command= update )
b4.grid ( row = 4 , column = 3  )
b4 = Button ( window , text= 'Delete ' , height= 3 ,  width= 15 , command= delete )
b4.grid ( row = 15 , column = 1  )
b4 = Button ( window , text= 'Close ' , height= 3 ,  width= 15 , command= close )
b4.grid ( row = 15 , column = 2  )







window.mainloop()
