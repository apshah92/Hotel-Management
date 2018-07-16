from tkinter import *
import hotel_view
import checkin_view
import reviews_view
import manage_reservations_view

# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):

        self.master=master  # This is reference to master object. since otherwise master can not be referenced from other functions.
        # parameters that you want to send through the Frame class. 
        self.frame=Frame(master)   
        self.frame.pack()        
        
        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("Hotel Jersey Inn Management")

        # creating a button instance
        view_hotels = Button(self.frame, text="View Hotels\n& Rooms",command=self.hotel_window)
        check_in = Button(self.frame, text="Check-In\nConfirmation",command=self.checkin_window)
        view_reviews=Button(self.frame, text="View or Submit\nReviews",command=self.review_window)
        manage_reservation=Button(self.frame, text="Manage\nReservation",command=self.reservation_window)
        
        view_hotels.grid(row=0,column=0)

        check_in.grid(row=0,column=1)

        view_reviews.grid(row=1,column=0)

        manage_reservation.grid(row=1,column=1)
        
        
       

    
    def hotel_window(self):
        hotel_view.viewhotels()

    def checkin_window(self):
        checkin_view.input_checkin()

    def review_window(self):
        reviews_view.review_window()

    def reservation_window(self):
        manage_reservations_view.show()
        
        
        
        
        
if __name__=='__main__':
    root = Tk()
    #creation of an instance
    app = Window(root)

    #mainloop 
    root.mainloop() 
    

