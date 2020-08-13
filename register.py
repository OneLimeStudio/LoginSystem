import json


database = open("main.txt","r+")

def register():
    username = input(print("Plz tell the username"))
    
    #if username in database.read():

    with database as f:
        if username in f.read():
            print("This Username Already Exists")
            f.close()

        else:
            f.write(" , " + username) 
            print("Username Added !!")
            f.close()

