from tkinter import *
import pymysql
import review_base

db = pymysql.connect("localhost","root","cs631","hrs")

def review_window():
    top_review=Tk()
    view_reviews_button=Button(top_review,text='View\nReviews',command=view)
    view_reviews_button.pack(side=LEFT)

    submit_reviews_button=Button(top_review,text='Submit\nReviews',command=submit_reviews)
    submit_reviews_button.pack(side=LEFT)

    top_review.mainloop()

def view():
    view_review=Tk()
    
    Room_Reviews=Button(view_review,text='Room\nReviews',command=room_reviews)
    Room_Reviews.pack(side=LEFT)

    Service_Reviews=Button(view_review,text='Service\nReviews',command=service_reviews)
    Service_Reviews.pack(side=LEFT)
    
    Breakfast_Reviews=Button(view_review,text='Breakfast\nReviews',command=breakfast_reviews)
    Breakfast_Reviews.pack(side=LEFT)

    view_review.mainloop()

def room_reviews():
    room=Tk()
    text=Text(room)
    result=review_base.room_review(db)

    for row in result:
        line=' '.join([str(i) for i in row])+'\n'
        text.insert(INSERT,line)

    text.pack()
    room.mainloop()

def service_reviews():
    service=Tk()
    text=Text(service)
    result=review_base.service_review(db)

    for row in result:
        line=' '.join([str(i) for i in row])+'\n'
        text.insert(INSERT,line)

    text.pack()
    service.mainloop()

def breakfast_reviews():    
    breakfast=Tk()
    text=Text(breakfast)
    result=review_base.breakfast_review(db)

    for row in result:
        line=' '.join([str(i) for i in row])+'\n'
        text.insert(INSERT,line)

    text.pack()
    breakfast.mainloop()

def submit_reviews():
    submit=Tk()
    upperframe=Frame(submit)
    upperframe.pack()
    room_review_button=Button(upperframe,text='Add\nRoom\nReview',command=lambda:add_review(submit,'room'))
    room_review_button.pack(side=LEFT)

    service_review_button=Button(upperframe,text='Add\nservice\nReview',command=lambda:add_review(submit,'service'))
    service_review_button.pack(side=LEFT)

    breakfast_review_button=Button(upperframe,text='Add\nbreakfast\nReview',command=lambda:add_review(submit,'breakfast'))
    breakfast_review_button.pack(side=LEFT)
    submit.mainloop()

def add_review(root,review_name):
    bottomframe=Frame(root)
    bottomframe.pack(side=BOTTOM)

    if review_name=='room':
        Hotel_Id=Label(bottomframe,text='Hotel ID')
        Hotel_Id.grid(row=0,column=0)        
        Hotel_entry=Entry(bottomframe,bd=4)
        Hotel_entry.grid(row=0,column=1)

        Room_ID=Label(bottomframe,text='Room ID')
        Room_ID.grid(row=1,column=0)
        Room_Entry=Entry(bottomframe,bd=4)
        Room_Entry.grid(row=1,column=1)

        Rating=Label(bottomframe,text='Rating')
        Rating.grid(row=2,column=0)        
        Rating_Entry=Entry(bottomframe,bd=4)
        Rating_Entry.grid(row=2,column=1)

        Description=Label(bottomframe,text='Description')
        Description.grid(row=3,column=0)       
        Description_Entry=Entry(bottomframe,bd=4,width=50)
        Description_Entry.grid(row=3,column=1)

        submit_button=Button(bottomframe,text='Submit',command=lambda:review_base.update_database(db,Hotel_entry.get(),Room_Entry.get(),Rating_Entry.get(),\
                                                                                                  Description_Entry.get()))
        submit_button.grid(row=4,column=1)
        
    elif review_name=='service':
        Hotel_Id=Label(bottomframe,text='Hotel ID')
        Hotel_Id.grid(row=0,column=0)        
        Hotel_entry=Entry(bottomframe,bd=4)
        Hotel_entry.grid(row=0,column=1)

        Service_Type=Label(bottomframe,text='Service Type')
        Service_Type.grid(row=1,column=0)
        Service_Entry=Entry(bottomframe,bd=4)
        Service_Entry.grid(row=1,column=1)

        Rating=Label(bottomframe,text='Rating')
        Rating.grid(row=2,column=0)        
        Rating_Entry=Entry(bottomframe,bd=4)
        Rating_Entry.grid(row=2,column=1)

        Description=Label(bottomframe,text='Description')
        Description.grid(row=3,column=0)        
        Description_Entry=Entry(bottomframe,bd=4,width=50)
        Description_Entry.grid(row=3,column=1)

        submit_button=Button(bottomframe,text='Submit',command=lambda:review_base.update_database(db,Hotel_entry.get(),Service_Entry.get(),Rating_Entry.get(),\
                                                                                                  Description_Entry.get()))
        submit_button.grid(row=4,column=1)

    else:
        Hotel_Id=Label(bottomframe,text='Hotel ID')
        Hotel_Id.grid(row=0,column=0)       
        Hotel_entry=Entry(bottomframe,bd=4)
        Hotel_entry.grid(row=0,column=1)

        Breakfast_Type=Label(bottomframe,text='Breakfast Type')
        Breakfast_Type.grid(row=1,column=0)
        Breakfast_Entry=Entry(bottomframe,bd=4)
        Breakfast_Entry.grid(row=1,column=1)

        Rating=Label(bottomframe,text='Rating')
        Rating.grid(row=2,column=0)        
        Rating_Entry=Entry(bottomframe,bd=4)
        Rating_Entry.grid(row=2,column=1)

        Description=Label(bottomframe,text='Description')
        Description.grid(row=3,column=0)        
        Description_Entry=Entry(bottomframe,bd=4,width=50)
        Description_Entry.grid(row=3,column=1)

        submit_button=Button(bottomframe,text='Submit',command=lambda:review_base.update_database(db,Hotel_entry.get(),Breakfast_Entry.get(),Rating_Entry.get(),\
                                                                                                  Description_Entry.get()))
        submit_button.grid(row=4,column=1)
db.close()
    
      
                      
    

        

        

        

        

        
    
    
    
    
    

    
    
