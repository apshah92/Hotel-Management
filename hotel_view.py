from tkinter import *
import pymysql
import hotel_base


db = pymysql.connect("localhost","root","cs631","hrs")
    
    
def viewhotels():
    root = Tk()
    text = Text(root)

    hotel_data=hotel_base.hotel_database(db)
    for row in hotel_data:
        line=' '.join([str(i) for i in row])+'\n'
        text.insert(INSERT,line)
    text.pack()
    view_room=Button(root,text='View\nRooms',command=viewrooms)
    view_room.pack(side=BOTTOM)
    root.mainloop()
    
def viewrooms():
    root = Tk()
    text = Text(root)

    hotel_data=hotel_base.room_database(db)
    for row in hotel_data:
        line=' '.join([str(i) for i in row])+'\n'
        text.insert(INSERT,line)
    text.pack()
    root.mainloop()
    
    
