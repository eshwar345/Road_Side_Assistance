#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from datetime import datetime
database=[]

def register_vehicle():
    while True:
        vehicle_no = input("Vehicle Number: (TGxxABxxxx)").upper()
        if ((8<=len(vehicle_no) >= 10) and vehicle_no[:2].isalpha() and vehicle_no[2:4].isdigit() and vehicle_no[4:6].isalpha() and vehicle_no[6:].isdigit()):
            break
        else:
            print("Invalid Vehicle Number")
    while True:
        owner=input("Owner Name: ")
        if owner.replace(" ","").isalpha():
            break
        print("Invalid Name")
    services=[]
    total=0
    while True:
        print("\n")
        print("-----------------------------------------")
        print("------------:SELECT_SERVICES:------------")
        print("Note: press 9.Done after choosing services required")
        print("1. Oil Change_____________________Rs1200")
        print("2. Battery Replacement____________Rs4500")
        print("3. Puncture Repair_________________Rs300")
        print("4. Wheel Replacement______________Rs3500")
        print("5. Brake Failure__________________Rs2500")
        print("6. Engine Service_________________Rs8000")
        print("7. Vehicle Inspection______________Rs500")
        print("8. Clutch Replacement_____________Rs6000")
        print("9. Done")
        print("-----------------------------------------")
        choice=int(input("Choice: (1-9) "))
        if choice==1:
            services.append("Oil Change")
            total+=1200
        elif choice==2:
            services.append("Battery Replacement")
            total+=4500
        elif choice==3:
            services.append("Puncture Repair")
            total+=300
        elif choice==4:
            services.append("Wheel Replacement")
            total+=3500
        elif choice==5:
            services.append("Brake Failure")
            total+=2500
        elif choice==6:
            services.append("Engine Service")
            total+=8000
        elif choice==7:
            services.append("Vehicle Inspection")
            total+=500
        elif choice==8:
            services.append("Clutch Replacement")
            total+=6000
        elif choice==9:
            break
        else:
            print("Invalid Choice")
        print("services chosen", services)
    tow_required=input("Do you need towing service? (Yes/No): ")
    if tow_required.lower()=="yes":
        print("Opening Towing Module...")
        towing_required()

    service_date = datetime.now().strftime("%d-%m-%Y")

    spare_required="None"
    record={
        "date":service_date,
        "vehicle":vehicle_no,
        "owner":owner,
        "services":services,
        "price":total,
        "towing":tow_required,
        "parts":spare_required,
        "mechanic":"Not Assigned",
        "status":"Pending"
    }
    database.append(record)

    print("Vehicle Registered Successfully")
    print("Total Amount: Rs",total)

def assign_mechanic():
    print("\n")
    while 1:
        vehicle_no = input("Vehicle Number: (TGxxABxxxx)").upper()
        if ((8<=len(vehicle_no) >= 10) and vehicle_no[:2].isalpha() and vehicle_no[2:4].isdigit() and vehicle_no[4:6].isalpha() and vehicle_no[6:].isdigit()):
            break
        else:
            print("Invalid Vehicle Number")
    for i in database:
        if i["vehicle"]==vehicle_no:
            mechanic=input("Mechanic Name: ")
            i["mechanic"]=mechanic
            spare_required=input("Do you need spare parts? (Yes/No): ")
            if spare_required.lower()=="yes":
                print("Opening Spare Parts Module...")
                required_spare_parts()
            print("Mechanic Assigned")
            return
    print("Vehicle Not Found")

def check_service_status():
    while 1:
        vehicle_no = input("Vehicle Number: (TGxxABxxxx)").upper()
        if ((8<=len(vehicle_no) >= 10) and vehicle_no[:2].isalpha() and vehicle_no[2:4].isdigit() and vehicle_no[4:6].isalpha() and vehicle_no[6:].isdigit()):
            break
        else:
            print("Invalid Vehicle Number")
    for i in database:
        if i["vehicle"]==vehicle_no:
            print("Date:",i["date"])
            print("Services:")
            for j in i["services"]:
                print(j)
            print("Status:",i["status"])
            return
    print("Vehicle Not Found")

def update_status():
    while 1:
        vehicle_no = input("Vehicle Number: (TGxxABxxxx)").upper()
        if ((8<=len(vehicle_no) >= 10) and vehicle_no[:2].isalpha() and vehicle_no[2:4].isdigit() and vehicle_no[4:6].isalpha() and vehicle_no[6:].isdigit()):
            break
        else:
            print("Invalid Vehicle Number")
    for i in database:
        if i["vehicle"]==vehicle_no:
            print("1-->Pending")
            print("2-->In Progress")
            print("3-->Completed")
            choice=int(input("Choice: "))
            if choice==1:
                i["status"]="Pending"
            elif choice==2:
                i["status"]="In Progress"
            elif choice==3:
                i["status"]="Completed"
            print("Status Updated")
            return
    print("Vehicle Not Found")

def required_spare_parts():
    print("\n")
    try:
        import Spare_parts
        Spare_parts.main()
    except Exception:
        print("available")

def towing_required():
    print("\n")
    try:
        import TOW
        TOW.main()
    except Exception:
        print("available")   

def completed_database():
    found=False
    print("\n")
    for i in database:
        if i["status"]=="Completed":
            found=True
            print("_____COMPLETED_SERVICE_____")
            print("Date:",i["date"])
            print("Vehicle:",i["vehicle"])
            print("Owner:",i["owner"])
            print("Services:")
            for j in i["services"]:
                print(j)
            print("Mechanic:",i["mechanic"])
            print("Amount: Rs",i["price"])
        if i["status"]=="In Progress":
            found=True
            print("_____IN PROGRESS_SERVICE_____")
            print("Date:",i["date"])
            print("Vehicle:",i["vehicle"])
            print("Owner:",i["owner"])
            print("Services:")
            for j in i["services"]:
                print(j)
            print("Mechanic:",i["mechanic"])
            print("Amount: Rs",i["price"])
        if i["status"]=="Pending":
            found=True
            print("_____PENDING_SERVICE_____")
            print("Date:",i["date"])
            print("Vehicle:",i["vehicle"])
            print("Owner:",i["owner"])
            print("Services:")
            for j in i["services"]:
                print(j)
            print("Mechanic:",i["mechanic"])
            print("Amount: Rs",i["price"])
    if found==False:
        print("No records found")

def bill():
    print("\n")
    while 1:
        vehicle_no = input("Vehicle Number: (TGxxABxxxx)").upper()
        if ((8<=len(vehicle_no) >= 10) and vehicle_no[:2].isalpha() and vehicle_no[2:4].isdigit() and vehicle_no[4:6].isalpha() and vehicle_no[6:].isdigit()):
            break
        else:
            print("Invalid Vehicle Number")
    for i in database:
        if i["vehicle"]==vehicle_no:
            print("\n")
            print("_____BILL_____")
            print("Date:",i["date"])
            print("Vehicle:",i["vehicle"])
            print("Owner:",i["owner"])
            print("Services:")
            for j in i["services"]:
                print(j)
            print("Towing:",i["towing"])
            print("Spare Parts:",i["parts"])
            print("Total Amount: Rs",i["price"])
            return
    print("Vehicle Not Found")

def main():
    while True:
        try:
            print("\n")
            print("----------------------------")
            print("_____SERVICE_MANAGEMENT_____")
            print("1-->Register Vehicle")
            print("2-->Assign Mechanic")
            print("3-->Check Service Status")
            print("4-->Update Status")
            print("5-->Required Spare Parts")
            print("6-->Towing Required")
            print("7-->Completed Database")
            print("8-->Bill")
            print("9-->Exit")
            print("-----------------------------")
            choice=int(input("Choice: "))

            if choice==1:
                register_vehicle()
            elif choice==2:
                assign_mechanic()
            elif choice==3:
                check_service_status()
            elif choice==4:
                update_status()
            elif choice==5:
                required_spare_parts()
            elif choice==6:
                towing_required()
            elif choice==7:
                completed_database()
            elif choice==8:
                bill()
            elif choice==9:
                print("Thank you")
                break
            else:
                print("Invalid Choice")
        except Exception as e:
            print("please enter valid information",e)

main()

# import gradio as gr

# with gr.Blocks(title="Service Management System") as demo:

#     gr.Markdown("# SERVICE MANAGEMENT")

#     with gr.Row():
#         gr.Button("1. Register Vehicle").click(fn=register_vehicle)

#     with gr.Row():
#         gr.Button("2. Assign Mechanic").click(fn=assign_mechanic)

#     with gr.Row():
#         gr.Button("3. Check Service Status").click(fn=check_service_status)

#     with gr.Row():
#         gr.Button("4. Update Status").click(fn=update_status)

#     with gr.Row():
#         gr.Button("5. Required Spare Parts").click(fn=required_spare_parts)

#     with gr.Row():
#         gr.Button("6. Towing Required").click(fn=towing_required)

#     with gr.Row():
#         gr.Button("7. Completed Database").click(fn=completed_database)

#     with gr.Row():
#         gr.Button("8. Bill").click(fn=bill)

#     with gr.Row():
#         exit_btn = gr.Button("9. Exit")

# demo.launch()

#pip install gradio

