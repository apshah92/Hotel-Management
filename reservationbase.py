import pymysql

def reservationdata(db):
    cursor = db.cursor()    
    sql = """
Select c.cid, c.name, r.invoice_no, r1.hotelid, r1.roomno, r1.checkindate, r1.checkoutdate
from customer c, reservation r, room_reservation r1 
where c.cid = r.cid and r.invoice_no = r1.invoice_no;
          """

    cursor.execute(sql)
    results=cursor.fetchall()    
    return results

def update_database(*args):
    cursor = args[0].cursor()
    sql=''
    if args[1]=='customer':
        sql = "insert into customer(name,address,phone_no,email)\
                values(%s,%s,%s,%s);"%(args[2],args[3],args[4],args[5])
    elif args[1]=='room reservation':
        sql =  "insert into room_reservation(hotelid,roomno,checkindate,checkoutdate)\
                values(%d,%d,%s,%s);"%(int(args[2]),int(args[3]),args[4],args[5])
    elif args[1]=='Credit Card':
        sql = "insert into credit_card\
                values(%d,%s,%s,%d,%s,%s);"%(int(args[2]),args[3],args[4],int(args[5]),args[6],args[7])
    else:
        pass
    

    try:
       # Execute the SQL command
       cursor.execute(sql)
       # Commit your changes in the database
       args[0].commit()
    except Exception as e:
       # Rollback in case there is any error
       print(e)
       args[0].rollback()
