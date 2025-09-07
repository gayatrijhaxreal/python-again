import json
import random
import string
from pathlib import Path

class Bank:

    database = 'data.json'
    data = []
    try:
        if Path(database).exixts():
            with open(database) as fs:
               data = json.loads(fs.read())
        else:
            print("no such file exists")
    except Exception as err:
        print(f"an exception occured as {err}")

    @staticmethod
    def update():
        with open(Bank.database,'w') as fs:
            fs.write(json.dumps(Bank.data))



    def Createaccount(self):

        info = {
            "name" : input ("Tell your name" ),
            "age" : int(input("tell your age:-")),
            "email" : input("tell your email"),
            "pin" : input("tell your 4 number pin :-"),
            "accountNo." :1234,
            "balance": 0
            }
        
        if info ['age']< 18 or len(str(info['pin'])) != 4:
            print("sorry you cannot  reate your account")
        else:
            print("your account has sucessfully created ")

            for i in info :

                print(f"{i}:{info[i]}")
            
            print("please note down your accn number")

            Bank.data.append()
            Bank.update(info)

user = Bank()
print("press 1 for creating an account")
print("press 2 for depositing the money")
print("press 3 for withdrawing the money")
print("press 4 for details")
print("press 5 for updating the details")
print("press 6 for deeting your account")

check = int(input("tell your response:-"))

