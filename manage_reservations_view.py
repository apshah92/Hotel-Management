from tkinter import *
import pymysql
import reservationbase

db = pymysql.connect("localhost","root","cs631","hrs")

def show():
    reservation=Tk()
    View_Reservation_button=Button(reservation,text='View\nReservation',command=view)
    View_Reservation_button.pack(side=LEFT)

    add_res_button=Button(reservation,text='Add\nNew\nReservation',command=add_reservation)
    add_res_button.pack(side=LEFT)

    reservation.mainloop()

def view():
    view_window=Tk()
    text=Text(view_window)
    result=reservationbase.reservationdata(db)
    for row in result:
        line=' '.join([str(i) for i in row])+'\n'
        text.insert(INSERT,line)

    text.pack()
    view_window.mainloop()

def add_reservation():
    add_reservation_window=Tk()
    add_reservation_window.title('Reservation Details')


    frame1=Frame(add_reservation_window)
    frame2=Frame(add_reservation_window)
    frame3=Frame(add_reservation_window)
    
    frame1.pack()

    Customer_Name=Label(frame1,text='Customer_Name')
    Customer_Name.grid(row=0,column=0)        
    Customer_Entry=Entry(frame1,bd=4)
    Customer_Entry.grid(row=0,column=1)

    Address=Label(frame1,text='Address')
    Address.grid(row=1,column=0)
    Address_Entry=Entry(frame1,bd=4)
    Address_Entry.grid(row=1,column=1)

    Phone=Label(frame1,text='Phone')
    Phone.grid(row=2,column=0)        
    Phone_Entry=Entry(frame1,bd=4)
    Phone_Entry.grid(row=2,column=1)

    Email=Label(frame1,text='Email')
    Email.grid(row=3,column=0)       
    Email_Entry=Entry(frame1,bd=4)
    Email_Entry.grid(row=3,column=1)

    Next_Button=Button(frame1,text='Next',command=lambda:[f for f in [frame1.pack_forget(),frame2.pack(),reservationbase.update_database(db,'customer',Customer_Entry.get(),Address_Entry.get(),Phone_Entry.get(),Email_Entry.get())]])    
                                                                                  
                                                                        
    Next_Button.grid(row=4,column=1)

    #room reservation
    
    Hotel_Id=Label(frame2,text='Hotel ID')
    Hotel_Id.grid(row=0,column=0)        
    Hotel_entry=Entry(frame2,bd=4)
    Hotel_entry.grid(row=0,column=1)

    Room_ID=Label(frame2,text='Room ID')
    Room_ID.grid(row=1,column=0)
    Room_Entry=Entry(frame2,bd=4)
    Room_Entry.grid(row=1,column=1)

    CheckIn_Date=Label(frame2,text='CheckIn_Date')
    CheckIn_Date.grid(row=2,column=0)        
    CheckIn_Entry=Entry(frame2,bd=4)
    CheckIn_Entry.grid(row=2,column=1)

    CheckOut_Date=Label(frame2,text='CheckOut_Date')
    CheckOut_Date.grid(row=3,column=0)       
    CheckOut_Entry=Entry(frame2,bd=4)
    CheckOut_Entry.grid(row=3,column=1)

    Next_Button=Button(frame2,text='Next',command=lambda:[f for f in [frame2.pack_forget(),frame3.pack(),\
                                                                        reservationbase.update_database(db,'room reservation',\
                                                                        Hotel_entry.get(),Room_Entry.get(),CheckIn_Entry.get(),CheckOut_Entry.get())]])
    Next_Button.grid(row=4,column=1)

    #credit card
    CNum=Label(frame3,text='Card Number')
    CNum.grid(row=0,column=0)        
    CNum_Entry=Entry(frame3,bd=4)
    CNum_Entry.grid(row=0,column=1)

    CType=Label(frame3,text='Card Type')
    CType.grid(row=1,column=0)
    CType_Entry=Entry(frame3,bd=4)
    CType_Entry.grid(row=1,column=1)

    BAdrr=Label(frame3,text='Billind Address')
    BAdrr.grid(row=2,column=0)        
    BAdrr_Entry=Entry(frame3,bd=4)
    BAdrr_Entry.grid(row=2,column=1)

    Code=Label(frame3,text='CVV code')
    Code.grid(row=3,column=0)       
    Code_Entry=Entry(frame3,bd=4)
    Code_Entry.grid(row=3,column=1)

    ExpDate=Label(frame3,text='Expiry Date')
    ExpDate.grid(row=4,column=0)        
    ExpDate_Entry=Entry(frame3,bd=4)
    ExpDate_Entry.grid(row=4,column=1)

    CardName=Label(frame3,text='Card_Name')
    CardName.grid(row=5,column=0)        
    CardName_Entry=Entry(frame3,bd=4)
    CardName_Entry.grid(row=5,column=1)

    Submit_Button=Button(frame3,text='Submit',command=lambda:[f for f in [frame3.pack_forget(),reservationbase.update_database(db,'Credit Card',CNum_Entry.get(),\
                                                                            CType_Entry.get(),BAdrr_Entry.get(),Code_Entry.get(),ExpDate_Entry.get(),\
                                                                            CardName_Entry.get()),add_reservation_window.destroy]])
    Submit_Button.grid(row=6,column=1)    
    
    
    add_reservation_window.mainloop()

