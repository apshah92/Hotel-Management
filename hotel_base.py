import pymysql



def hotel_database(db):
    cursor = db.cursor()    
    sql = """SELECT *
             FROM HOTEL;"""

    cursor.execute(sql)
    results=cursor.fetchall()
    return results

def room_database(db):
    cursor = db.cursor()    
    sql = """Select * from Room 
            GROUP BY hotelId;
          """

    cursor.execute(sql)
    results=cursor.fetchall()
    return results
    
    
    



