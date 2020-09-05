import psycopg2
try:
    # connection = psycopg2.connect(user = "postgres",
    #                               password = "lolo",
    #                               host = "127.0.0.1",
    #                               port = "5432",
    #                               database = "testpy")
    connection = psycopg2.connect('dbname=testpy')

    cursor = connection.cursor()

    # insert_query = '''insert into mobile (model, price) values (%s, %s);'''
    
    # data= ('huwawi', 100)
    # cursor.execute(insert_query,data)
    cursor.execute('update mobile set price = %s where id = %s;',(70,1))
    connection.commit()
    print("update done")

    
    selectQuery = "select * from mobile"
    cursor.execute(selectQuery)
    result= cursor.fetchone()
    print('fetchone',result)
    print("Selecting rows from mobile table using cursor.fetchall")
    mobile_records = cursor.fetchall() 
   
    

    print("Print each row and it's columns values")
    for row in mobile_records:
        print("Id = ", row[0], )
        print("Model = ", row[1])
        print("Price  = ", row[2], "\n")
    

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")