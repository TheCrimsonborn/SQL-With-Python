import mysql.connector

def insertProduct(name, price, imgUrl, description):
    connection = mysql.connector.connect(host="localhost",user="root",password="root",database="node-app")
    cursor = connection.cursor()

    sql="INSERT INTO products(name,price,imgUrl,description) VALUES (%s,%s,%s,%s)"
    values=(name,price,imgUrl,description)

    cursor.execute(sql,values)

    try:
        connection.commit()
        print(f'{cursor.rowcount} product(s) added.')
        print(f'the id of the last product added: {cursor.lastrowid} ')

    except mysql.connector.Error as err:
        print("Error: ", err)
    finally:
        connection.close()
        print("The Database connections closed!")

def insertProducts(list):
    connection = mysql.connector.connect(host="localhost",user="root",password="root",database="node-app")
    cursor = connection.cursor()

    sql="INSERT INTO products(name,price,imgUrl,description) VALUES (%s,%s,%s,%s)"
    values=list

    cursor.executemany(sql,values)

    try:
        connection.commit()
        print(f'{cursor.rowcount} product(s) added.')
        print(f'the id of the last product added: {cursor.lastrowid} ')

    except mysql.connector.Error as err:
        print("Error: ", err)
    finally:
        connection.close()
        print("The Database connections closed!")

# list=[]
# while True:
#     name=input("Product name: ")
#     price=float(input("Price: "))
#     imgUrl=input("Image URL: ")
#     description=input("Description: ")

#     list.append((name, price, imgUrl, description))

#     nextRecord=input("Will you add a new record? (y/n)")
#     if nextRecord =="n":
#         print("The record has been added to the database.")
#         print(list)
#         insertProducts(list)
#         break

# insertProduct(name, price, imgUrl, description)

def getProducts():
    connection = mysql.connector.connect(host="localhost",user="root",password="root",database="node-app")
    cursor = connection.cursor()

    # cursor.execute('SELECT * FROM products')
    cursor.execute('SELECT name,price FROM products')

    result= cursor.fetchall()

    for product in result:
        # print(f'Product Name: {product[1]} | Price: {product[2]} ')
        print(f'Product Name: {product[0]} | Price: {product[1]} ')

def getProductsWhere():
    connection = mysql.connector.connect(host="localhost",user="root",password="root",database="node-app")
    cursor = connection.cursor()

    #WHERE
    # cursor.execute("SELECT * FROM products WHERE name='Xiaomi Mi Note 3' OR price>1300 ")

    #LIKE
    cursor.execute("SELECT * FROM products WHERE name LIKE '%Xiaomi%' AND price=2300 ")


    result= cursor.fetchall()

    for product in result:
        print(f'ID: {product[0]} | Product Name: {product[1]} | Price: {product[2]} ')

def getProductsById(id):
    connection = mysql.connector.connect(host="localhost",user="root",password="root",database="node-app")
    cursor = connection.cursor()

    sql = "SELECT * FROM products WHERE id=%s"
    params=(id,)

    cursor.execute(sql,params)
    result = cursor.fetchall()

    for product in result:
        print(f'ID: {product[0]} | Product Name: {product[1]} | Price: {product[2]} ')
# id=int(input("Enter an ID: "))

def getProductsOrderBy():
    connection = mysql.connector.connect(host="localhost",user="root",password="root",database="node-app")
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM products ORDER BY price DESC')

    try:
        result= cursor.fetchall()
        for product in result:
            print(f'ID: {product[0]} | Product Name: {product[1]} | Price: {product[2]} ')
    except mysql.connector.Error as err:
        print("Error: ", err)
    finally:
        connection.close()
        print("The Database connections closed!")

def getProductInfo():
    connection = mysql.connector.connect(host="localhost",user="root",password="root",database="node-app")
    cursor = connection.cursor()

    #Counts all records in table.
    # sql = "SELECT COUNT(*) FROM products"

    #Counts records with price greater than 2000 in the table.
    # sql = "SELECT COUNT(*) FROM products WHERE price > 2000"

    #Prints the average of the prices in the table.
    # sql = "SELECT AVG(price) FROM products"

    #Prints the sum of the prices in the table.
    # sql = "SELECT SUM(price) FROM products"

    #Prints the max price in the table.
    # sql = "SELECT MAX(price) FROM products"

    #Prints the min price in the table.
    # sql = "SELECT MIN(price) FROM products"

    #Prints the name of the record with the highest price.
    sql = "SELECT name,price FROM products WHERE price = (SELECT MAX(price) FROM products)"



    cursor.execute(sql)
    result = cursor.fetchone()
    
    print(f'Result: {result[0]}, {result[1]}')

def updateProduct(id,name,price):
    connection = mysql.connector.connect(host="localhost",user="root",password="root",database="node-app")
    cursor = connection.cursor()

    sql = "UPDATE products SET name=%s, price=%s WHERE id=%s"
    values = (name,price,id)
    cursor.execute(sql,values)

    try:
        connection.commit()
        print(f'{cursor.rowcount} product(s) updated.')
    except mysql.connector.Error as err:
        print("Error: ", err)
    finally:
        connection.close()
        print("The Database connections closed!")
# id=int(input("Enter an ID: "))
# name=(input("Enter the prodcut's name: "))
# price=int(input("Enter the prodcut's price: "))

def deleteProduct(name):
    connection = mysql.connector.connect(host="localhost",user="root",password="root",database="node-app")
    cursor = connection.cursor()

    sql = "DELETE FROM products WHERE name=%s"
    values = (name,)
    cursor.execute(sql,values)

    try:
        connection.commit()
        print(f'{cursor.rowcount} product(s) deleted.')
    except mysql.connector.Error as err:
        print("Error: ", err)
    finally:
        connection.close()
        print("The Database connections closed!")
# name=(input("Enter a name: "))






