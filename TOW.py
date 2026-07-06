#!/usr/bin/env python
# coding: utf-8

# In[1]:


information = []


# In[2]:


def fuel_delivery():   
    try:
        print("Assigned Service : Fuel Delivery Vehicle")
        litres = float(input("Fuel Required (Litres): "))
        fuel=str(input("petrol or Diesel"))
        if fuel.lower() == "petrol":
            fuel_price=115.73
            print("petrol = ₹ 115.73")
        elif fuel.lower() =="diesel":
            fuel_price=103.82
            print("diesel = ₹ 103.82 ")
        else:
            print("enter vaild fuel")
            return
        fuel_cost = litres * fuel_price
        delivery_charge = 300
        total = fuel_cost + delivery_charge
        print("Advice Until Assistance Arrives:")
        print("Share your exact location with the service team.")
        print("Keep the vehicle parked safely away from traffic.")
        print("The fuel operator will verify the vehicle number before refuelling.")
        return "Fuel Delivery", total
    except Exception as e:
            print("enter valid information",e)


# In[3]:


def battery_service():
    try:
        print("Assigned Service : Battery Technician")
        print("1. Jump Start")
        print("2. Battery Replacement")
        choice = int(input("Select Service: "))
        if choice == 1:
            battery_cost = 0
            service_charge = 500
            total = service_charge
            service = "Jump Start Service"
        elif choice == 2:
            battery_cost = 3000
            service_charge = 500
            total = battery_cost + service_charge
            service = "Battery Replacement"
        else:
            print("enter valid info")
            return
        print("Advice Until Technician Arrives:")
        print("Keep ignition switched off.")
        print("Avoid repeatedly attempting to start the vehicle.")
        print("Keep your vehicle documents ready for verification.")
        return "battery checkup", total
    except Exception as e:
            print("enter valid information",e)


# In[4]:


def puncture_service():
    print("SERVICE ASSIGNED : Roadside Mechanic")
    print("Charge : ₹400")
    print("please wait until our men reaches you")
    return "Puncture Repair", 400


# In[7]:


def overheating_service():
    print("SERVICE ASSIGNED : Roadside Mechanic")
    print("Charge : ₹800")
    print("please wait until our men reaches you")
    print("Safety Tips:")
    print("Turn OFF AC")
    print("Stop vehicle safely")
    print("Do NOT open radiator cap")
    return "Engine Inspection", 800


# In[8]:


def clutch_service():
    print("SERVICE ASSIGNED : Tow Vehicle")
    print("Charge : ₹2500")
    print("our men reaches you within 20 min")
    print("Safety Tips:")
    print("Do not continue driving")
    print("Move vehicle to roadside if possible")
    print("Wait for towing vehicle")
    return "Vehicle Towing", 2500


# In[9]:


def engine_seized_service():
    print("SERVICE ASSIGNED : Tow Vehicle")
    print("Charge : ₹3000")
    print("please wait until our men reaches you")
    print("Safety Tips:")
    print("Do not restart engine")
    print("Keep vehicle stationary")
    print("Wait for towing assistance")
    return "Heavy Vehicle Towing", 3000


# In[10]:


def accident_service():
    print("SERVICE ASSIGNED : Emergency Tow Vehicle")
    print("Charge : ₹5000")
    print("please wait until our men reaches you")
    print("Safety Tips:")
    print("Check for injuries")
    print("Call Toll emergency contacts:1033")
    return "Accident Recovery", 5000


# In[11]:


def brake_failure_service():
    print("SERVICE ASSIGNED : Emergency Tow Vehicle")
    print("Charge : ₹3500")
    print("please wait until our men reaches you")
    print("Safety Tips:")
    print("Use handbrake gradually")
    print("Shift to lower gear")
    print("Move away from traffic")
    return "Emergency Towing", 3500



# In[12]:


def create_request():
    try:
        owner = str(input("Owner Name : "))
        while True:
            vehicle_no = input("Vehicle Number: (TGxxABxxxx)").upper()
            if (8<= len(vehicle_no) <= 10 and vehicle_no[:2].isalpha() and vehicle_no[2:4].isdigit() and vehicle_no[4:6].isalpha() and vehicle_no[6:].isdigit()):
                break
            else:
                print("Invalid Vehicle Number")

        print("1.Fuel Empty")
        print("2.Battery Dead")
        print("3.Puncture")
        print("4.Engine Overheating")
        print("5.Clutch Failure")
        print("6.Engine Seized")
        print("7.Major Accident")
        print("8.Brake Failure")
        choice = int(input("Select Problem : "))
        if choice == 1:
            problem = "Fuel Empty"
            service, charge = fuel_delivery()
        elif choice == 2:
            problem = "Battery Dead"
            service, charge = battery_service()
        elif choice == 3:
            problem = "Puncture"
            service, charge = puncture_service()
        elif choice == 4:
            problem = "Engine Overheating"
            service, charge = overheating_service()
        elif choice == 5:
            problem = "Clutch Failure"
            service, charge = clutch_service()
        elif choice == 6:
            problem = "Engine Seized"
            service, charge = engine_seized_service()
        elif choice == 7:
            problem = "Major Accident"
            service, charge = accident_service()
        elif choice == 8:
            problem = "Brake Failure"
            service, charge = brake_failure_service()
        else:
            print("Invalid Choice")
            return

        issues = {
            "vehicle": vehicle_no,
            "owner": owner,
            "problem": problem,
            "service": service,
            "charge": charge,
            "status": "Pending"
        }
        information.append(issues)
        print("Request Created Successfully")
    except Exception as e:
            print("enter valid information",e)


# In[13]:


def view_requests():
    if len(information) == 0:
        print("No Requests Found")
        return
    for i in information:
        print("_"*40)
        print("Vehicle :",   i["vehicle"])
        print("Owner   :",   i["owner"])
        print("Problem :",   i["problem"])
        print("Service :",   i["service"])
        print("Charge  : ₹", i["charge"])
        print("Status  :",   i["status"])



# In[14]:


def search_request():
    try:

        while True:
            vehicle_no = input("Vehicle Number: (TGxxABxxxx)").upper()
            if (8<= len(vehicle_no) <= 10 and vehicle_no[:2].isalpha() and vehicle_no[2:4].isdigit() and vehicle_no[4:6].isalpha() and vehicle_no[6:].isdigit()):
                break
            else:
                print("Invalid Vehicle Number")


        for i in information:
            if i["vehicle"] == vehicle_no:
                print("Vehicle :" ,   i["vehicle"])
                print("Owner   :" ,   i["owner"])
                print("Problem :" ,   i["problem"])
                print("Service :" ,   i["service"])
                print("Charge  : ₹", i["charge"])
                print("Status  :" ,   i["status"])
                return
        print("Request Not Found")
    except Exception as e:
        print("invalid entry",e)


# In[15]:


def status_update():
    try:

        while True:
            vehicle_no = input("Vehicle Number: (TGxxABxxxx)").upper()
            if ((8<= len(vehicle_no) <= 10) and vehicle_no[:2].isalpha() and vehicle_no[2:4].isdigit() and vehicle_no[4:6].isalpha() and vehicle_no[6:].isdigit()):
                break
            else:
                print("Invalid Vehicle Number")

        for i in information:
            if i["vehicle"]==vehicle_no:
                print("1=Pending")
                print("2=In Progress")
                print("3=Completed")
                choice=int(input("Select Status : "))
                if choice==1:
                    i["status"]="Pending"
                elif choice==2:
                    i["status"]="In Progress"
                elif choice==3:
                    i["status"]="Completed"
                else:
                    print("invalid choice")
                    return

                print("Status Updated")

        print("Vehicle Not Found")
    except Exception as e:
            print("enter valid information",e)



# In[16]:


def completed_services():
    for i in information:
        if i["status"] == "Pending":
            print(i)
        if i["status"] == "In Progress":
            print(i)
        if i["status"] == "Completed":
            print(i)


# In[17]:


def main():
    while True:
        try:
            information
            print("______TOWING________")
            print("1.Create Request")
            print("2.View Requests")
            print("3.Search Request")
            print("4.Update Status")
            print("5.Completed Services")
            print("6.Exit")
            choice = int(input("Enter Choice : "))
            if choice == 1:
                create_request()
            elif choice == 2:
                view_requests()
            elif choice == 3:
                search_request()
            elif choice == 4:
                status_update()
            elif choice == 5:
                completed_services()
            elif choice == 6:
                for i in information:
                    print("_________TOWING BILL_________")
                    print("Vehicle :",  i["vehicle"])
                    print("Owner   :",  i["owner"])
                    print("Problem :",  i["problem"])
                    print("Services :", i["service"])
                    print("Amount  : ₹",i["charge"])
                print("Thank You")
                break
            else:
                print("Invalid Choice")
        except Exception as e:
            print("enter valid information",e)


main()


# In[ ]:




