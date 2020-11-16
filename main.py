import sqlite3
from accesso import accesso
from os import system, name
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
from randomPassword import RandomPassword

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')


conn = sqlite3.connect("nameoftheDB.sqlite")
cur = conn.cursor()

password = " "
while(accesso(password)!=0):
    password = input("Insert your Database Password\n")
    if(accesso(password)==0):
        print("Access Granted")
        clear()
        print("--------------------------------------")
        decisione = '0'
        while(decisione!='4'):
            decisione = input("inserisci: \n 1 If you want to store a new password.\n 2 to generate a new password\n 3 to retrieve a password\n 4 Exit\n")
            if(decisione == '1'):
                sito = input("for which site is this password used? (in lower case)\n ")
                existPassword = input("Insert Password:\n")
                username = input("Is there any existing username linked to the site?\n")
                existPassword = existPassword.encode()
                key = #import a key (you can use a encrypted store_password...see accesso.py)
                f = Fernet(key)
                encrypted = f.encrypt(existPassword)
                cur.execute('INSERT INTO Password_Store (password, site, username) VALUES (?,?,?)', (encrypted,sito,username,))
                
            if(decisione == '3'):
                sito = input("Insert the name of the site for which you desire to retrieves the password: \n")
                cur.execute('SELECT password FROM Password_Store WHERE site=?', (sito,))
                for row in cur:
                    key = #key
                    f = Fernet(key)
                    decr = f.decrypt(row[0])
                    print(decr.decode("utf-8"))
                    print("\n")
        
            if(decisione == '2'):
                sito = input("Name of the site for which you desire to generate a password:\n")
                randmPassword = RandomPassword()
                print(f'Here your password: {randmPassword}')
                cur.execute('INSERT INTO Password_Store (password, site,) VALUES (?,?,?)', (randmPassword,sito,))


        conn.commit()
        cur.close()
    else:
        print("Wrong password--Access denied")
