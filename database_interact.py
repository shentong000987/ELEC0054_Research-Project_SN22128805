import pymysql
  
def mysqlconnect():
    # To connect MySQL database
    conn = pymysql.connect(
        host='localhost',
        user='root', 
        password = "ST19950412",
        db='person_fact',
        )
      
    #setting up cursor
    cur = conn.cursor()
    
    # ask the user's name to start a private conversation
    user_name = input('Hi! What is your name? \n')
    cur.execute("SELECT * FROM user WHERE UserName = %s", user_name)
    UserID_results = cur.fetchall()
    UserID = [row[0] for row in UserID_results]

    # select the fact contains the keyword provided by the user
    key_word = input('What is the key word? \n')
    search_string = key_word
    cur.execute("SELECT * FROM fact WHERE funFact LIKE %s AND userID = %s", ('%' + search_string + '%', UserID))

    # get the result and save the corresponding funFact contains the keyword
    results = cur.fetchall()
    column_data = [row[1] for row in results]
    
    # To close the connection
    conn.close()

    print(column_data[0])

# Driver Code
if __name__ == "__main__" :
    mysqlconnect()

