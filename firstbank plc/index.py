# bank App
pin = "*894#"
import time
import os
class Bank_app:
    def __init__(Bank):
        mypin = input("enter any pin here>> ")
        global pin
        if mypin == "*894#":
            time.sleep(2)
            print("""1.Quick Banking \n2.Open an account \n3.Loans \n4.FirstMonie""")
            Bank.quick()
        else:
            print("invalid pin")
            
    def quick(Bank):
        os.system('cls')
        value =input("enter any value ")
        if value  == "1":
            print("""1.Transfer Money \n2.Airtime(Bank) \n3.Airtime(others) \n4.Enquiry \n5.Data \n6.Pay bills \n7.Next page.""")
            Bank.money()
        elif value  == "2":
            print("you have an account")
        elif value  == "3":
            print("FirstAdvance")
        elif value  == "4":
            print("Link Account to FirstMoonie wallet")
            Bank.link()
        else:
            print("try again")

    def money(Bank):
        code = input("enter any code ")
        os.system("cls")
        if code == "1":
            print("enter any amount")
        elif code == "2":
            print("enter amount")
        elif code == "3":
            print("enter amount")
        elif code == "4":
            print("""1.Balance Enquiry \n2.BVN Enquiry \n3.Account Number Enquiry \n4.Mini statement""")
            Bank.balance()
        elif code == "5":
            print("""1.Bank \n2.Third Party""")
            Bank.services()
        elif code == "6":
            print("""1.Cable TV \n2.Electricity \n3.Renewable energy \n4.Betting and Lottery \n5.investment and Insurance \n6.Next Page""")
            Bank.cable()
        elif code == "7":
            print("""1.Insurance \n2.other services \n3.Merchant services \n4.card control \n5.Reserve cash \n6.Prev page""")
            Bank.insurance()
        else:
            print("invalid code")

    def balance(Bank):
        cod = input("enter any number.. ")
        if cod =="1":
            print("please wait fetching your account balance")
        elif cod =="2":
            print("Request Bank Verification Number \nEnter PIN to confirm:")
        elif cod =="3":
            print("Request Account Number \nEnter PIN to confirm:")
        elif cod =="4":
            print("Please wait fetching your mini-statement selected account. firstBank.You first")
        else:
            print("try again")

    def services(Bank):
        co = input("enter any value.. ")
        if co == "1":
            print("""1. 2GB 30Days #1200 \n2.12GB 30days #3500 \n3.25GB 30Days #6000 \n4.75MB 1Day #100 \n5.200MB 2Days #200 \n6.2.5GB 2Days #500 \n7.Next Page""")
        elif co == "2":
            print("enter mobile number:")
        else:
            print("invalid value")

    def cable(Bank):
        number = input("enter any number ")
        if number == "1":
            print("""1.Gotv \n2.Dstv Subscription \n3.Startimes Payments \n4.Iroko Tv \n5.Showmax""")
        elif number == "2":
            print("""1.PHCN Prepaid (EKO) \n2.Enugu Electricity Distribution Company. \n3.Ikeja Electric(prepaid and Postpaid) \n4.Next Page""")
        elif number == "3":
            print("""1.AZURI TECHNOLOGIES \n2.Cloud Energy \n3.Lumis \n4.Dlight \n5.Bboxx """)
        elif number == "4":
            print("""1.PlentyMillions \n2.BETWAY \n3.NaijaBet \n4.Bet9ja \n5.Zoom Lifestyle \n6.Winners Golden Bet \n7.Next Page""")
        elif number == "5":
            print("1,LeadWay Insurance")
        elif number == "6":
            print("""1.School and Exam Fees \n2.Religious Institutions \n3.internet Services \n4.Gift and Reward \n5.Next Page \n6.prev page""")
        else:
            print("invalid code")
        
    def insurance():
        num = input("enter any code  ")
        if num == "1":
            print("""1.Life Insurance \n2.General Insuramce""")
        elif num == "2":
            print("""1.Change PIN \n2.BVN Linkage""")
        elif num == "3":
            print("Enrol for Payment")
        elif num == "4":
            print("539923****1714")
        elif num == "5":
            print("enter amount to reserve")
        elif num == "6":
            Bank.money()
        else:
            print("try again")
            
    
    def link():
        account = input("input any account.. ")
        if account == "1":
            print("""1.3113XXXX659 \n2.3113XXXX659""")
        else:
            print("try again")
Bank_app()

