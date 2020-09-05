import psycopg2
try:
    # connection = psycopg2.connect(user = "postgres",
    #                               password = "lolo",
    #                               host = "127.0.0.1",
    #                               port = "5432",
    #                               database = "testpy")
    connection = psycopg2.connect('dbname=testpy')

    cursor = connection.cursor()
    
    create_table_query = '''CREATE TABLE mobile
          (id serial PRIMARY KEY     NOT NULL,
          model           varchar(50)    NOT NULL,
          price         varchar(50)); '''
    
    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully in PostgreSQL ")

    insert_query = '''insert into mobile (model, price) values ('honor', 50);'''
    cursor.execute(insert_query)
    connection.commit()
    print("insert done")
    

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")