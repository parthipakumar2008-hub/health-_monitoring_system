import time
import datetime

class Hospital:
    # HOSPITAL DETAILS
    def __init__(self):
        self.hospital_name=str(input("ENTER THE HOSPITAL NAME:"))
        self.hospital_location=str(input("ENTER THE HOSPITAL LOCATION:"))
    def hos_Pho_No(self):
        try:
            self.hospital_phone_no=int(input("ENTER THE HOSPITAl PHONE NUMBER:"))
            print()
        except  ValueError :
            print("ONLY ENTER THE PHONE NUMBER")
            return self.hos_Pho_No()
h=Hospital();h.hos_Pho_No()

class Villages():
        result_water=[];choose=[];number_of_people=[];total_diseases=[]
     # CHOOSE VILLAGE
        while True :
            n=input("WHICH VILLAGE ARE YOU CHOOSING:")
            print()
            if n.isdecimal(): #number 1
                n=int(n)
                choose.append(n)
                break
            else:
                continue
            # VILLAGE CREATE
        for i in range(1,n+1):
            print(f"========= {i} VILLAGE =========")
            running=True
            while running :
                try:
                    water=float(input("ENTER THE WATER QUALITY:"))
                    print()
                except Exception :
                    continue
                else:
            # PH VALUE 
                    if 6.5<= water<=8.5:
                        result_water.append(f"WATER IS SAFE IN VILLAGE {i}")
                    else:
                        result_water.append(f"WATER IS NOT SAFE IN VILLAGE {i}")
                    running=False
            # PERSNAL DETAILS
                    # REGISTER IN NUMBER OF PEPOPLE
                    running=True
                    while running:
                        reg_pep=input("REGISTER IN NUMBER OF PEOPLE:")
                        print()
                        if reg_pep.isnumeric():
                            reg_pep=int(reg_pep)
                            number_of_people.append(f"VILLAGE {i} : TOTAL PEOPLE {reg_pep}")
                            running=False
                        else:
                            running=True
                    for j in range(1,reg_pep+1):
                        # NAME
                        print(j,"PEPOLE")
                        running=True
                        while running:
                            name=input("ENTER THE PATIENT NAME:")
                            if name.isalpha():
                                running=False
                            else:
                                running=True
                        running=True
                        # AGE 
                        while running:
                            age=input("ENTER THE PATIENT AGE:")
                            if age.isnumeric():
                                running=False
                            else:
                                running=True
                        # DISEASE CHECK
                        running=True
                        while running:
                            diseases_check=input("ENTER THE DISEASE IN YES OR NO:").lower()
                            print()
                            if diseases_check.isalpha():
                                if diseases_check=="yes":
                                    running=True
                                    while running:
                                        diseases=input("ENTER THE PATIENT DISEASE:")
                                        if diseases.isalpha():
                                            total_diseases.append(f"VILLAGE {i} : DISEASE =  {diseases}")
                                            running=False
                                        else:
                                            running=True
                                    running=False
                                elif diseases_check=="no":
                                    running=False
                            else:
                                running=True
                        
def loading():
    print("LOADING...".center(15))
    for i in range(1,11):
        print("=",end=" ")
        time.sleep(0.2)
    print()
    print("COMPLETED 100%")
    print()
loading()

class Dashboard(Villages):
    def __init__ (self):
        print(" DASHBOARD ".center(43,"="))           
        date=datetime.date.today()
        print("                     DATE:",date,end="")
        a=Villages()
        print()
        for i in Villages.choose:
            print(f"TOTAL VILLAGE IS = {i}")
        print()
        for j in Villages.result_water:
            print("WATER RESULT=",j)
        print()
        for k in Villages.number_of_people:
            print(k)
        print()
        for l in Villages.total_diseases:
            print(l)
        print("===========================================")
v=Dashboard()