import pymysql

# Open database connection
db = pymysql.connect("localhost","arpan","hiarpanshah","hotel_management" )


def viewhotel(db):
    cursor = db.cursor()    
    sql = """SELECT *
             FROM HOTEL"""

    cursor.execute(sql)
    results=cursor.fetchall()
    return results

    



