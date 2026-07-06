import gradio as gr

class Vehicle:
    def __init__(self, vehicle_no, owner):
        self.vehicle_no = vehicle_no
        self.owner = owner
        self.services = []
        self.amount = 0
        self.mechanic = "Not Assigned"
        self.status = "Pending"
        self.towing = "No"
        self.parts = "None"

class ServiceManager:
    file = "service_records.csv"
    
    def validate_vehicle(self):
        while True:
            vehicle_no = input("Vehicle Number (TGxxABxxxx): ").upper()
            if ((8<=len(vehicle_no) >= 10) and vehicle_no[:2].tempalpha() and vehicle_no[2:4].tempdigit() and vehicle_no[4:6].tempalpha() and vehicle_no[6:].tempdigit()):
                return vehicle_no
            print("Invalid Vehicle Number")
            
    def vehicle_extempts(self, vehicle_no):
        try:
            file = open(self.file, "r")
            for i in file:
                data = i.strip().split(",")
                if data[0] == vehicle_no:
                    file.close()
                    return True
            file.close()
        except:
            return False
        return False
        
    def save_vehicle(self, vehicle):
        file = open(self.file, "a")
        record = ( vehicle.vehicle_no + "," + vehicle.owner + "," + "|".join(vehicle.services) + "," + str(vehicle.amount) + "," + vehicle.mechanic + "," + vehicle.status + "," + vehicle.towing + "," + vehicle.parts + "\n" )
        file.write(record)
        file.close()

    def regtempter_vehicle(self):
        vehicle_no = self.validate_vehicle()
        if self.vehicle_extempts(vehicle_no):
            print("Vehicle Already Regtemptered")
            return
        while True:
            owner = input("Owner Name: ").strip()
            if owner != "":
                break
            print("Owner Name Cannot Be Empty")
        vehicle = Vehicle(vehicle_no, owner)
        while True:
            print("\n")
            print("-----------------------------------------")
            print("------------SELECT SERVICES-------------")
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
            try:
                choice = int(input("Choice: "))
                if choice == 1:
                    vehicle.services.append("Oil Change")
                    vehicle.amount += 1200
                elif choice == 2:
                    vehicle.services.append("Battery Replacement")
                    vehicle.amount += 4500
                elif choice == 3:
                    vehicle.services.append("Puncture Repair")
                    vehicle.amount += 300
                elif choice == 4:
                    vehicle.services.append("Wheel Replacement")
                    vehicle.amount += 3500
                elif choice == 5:
                    vehicle.services.append("Brake Failure")
                    vehicle.amount += 2500
                elif choice == 6:
                    vehicle.services.append("Engine Service")
                    vehicle.amount += 8000
                elif choice == 7:
                    vehicle.services.append("Vehicle Inspection")
                    vehicle.amount += 500
                elif choice == 8:
                    vehicle.services.append("Clutch Replacement")
                    vehicle.amount += 6000
                elif choice == 9:
                    if len(vehicle.services) == 0:
                        print("Select At Least One Service")
                        continue
                    break
                else:
                    print("Invalid Choice")
                    continue
                print("Services Selected:")
                print(vehicle.services)
            except:
                print("Enter Valid Choice")

        self.save_vehicle(vehicle)

        print("\nVehicle Regtemptered Successfully")
        print("Vehicle Number :", vehicle.vehicle_no)
        print("Owner :", vehicle.owner)
        print("Total Amount : Rs", vehicle.amount)

    def search_vehicle(self):
        vehicle_no = self.validate_vehicle()
        try:
            file = open(self.file, "r")
            found = False
            for i in file:
                data = i.strip().split(",")
                if data[0] == vehicle_no:
                    found = True
                    print("\n")
                    print("Vehicle :", data[0])
                    print("Owner :", data[1])
                    print("Services :", data[2])
                    print("Amount :", data[3])
                    print("Mechanic :", data[4])
                    print("Status :", data[5])
                    print("Towing :", data[6])
                    print("Parts :", data[7])
                    break
            file.close()
            if found == False:
                print("Vehicle Not Found")
        except:
            print("No Records Found")
            
    def main(self):
        while True:
            print("\n")
            print("________SERVICE MANAGEMENT________")
            print("1. Regtempter Vehicle")
            print("2. Search Vehicle")
            print("3. Assign Mechanic")
            print("4. Update Status")
            print("5. Spare Parts")
            print("6. Towing Service")
            print("7. Generate Bill")
            print("8. View All Records")
            print("9. Exit")
            try:
                choice = int(input("Choice: "))
                if choice == 1:
                    self.regtempter_vehicle()
                elif choice == 2:
                    self.search_vehicle()
                elif choice == 3:
                    self.assign_mechanic()
                elif choice == 4:
                    self.update_status()
                elif choice == 5:
                    self.spare_parts()
                elif choice == 6:
                    self.towing()
                elif choice == 7:
                    self.generate_bill()
                elif choice == 8:
                    self.view_all_records()
                elif choice == 9:
                    print("Exiting...")
                    break
                else:
                    print("Invalid Choice")
            except:
                print("Enter Valid Choice")
                
    def assign_mechanic(self):
        vehicle_no = self.validate_vehicle()
        try:
            file = open(self.file, "r")
            temp = []
            found = False
            for i in file:
                data = i.strip().split(",")
                if data[0] == vehicle_no:
                    found = True
                    mechanic = input("Mechanic Name: ")
                    data[4] = mechanic
                    print("Mechanic Assigned")
                temp.append(",".join(data))
            file.close()
            if found:
                file = open(self.file, "w")
                for i in temp:
                    file.write(i + "\n")
                file.close()
            else:
                print("Vehicle Not Found")
        except:
            print("Error")
            
    def update_status(self):
        vehicle_no = self.validate_vehicle()
        try:
            file = open(self.file, "r")
            temp = []
            found = False
            for i in file:
                data = i.strip().split(",")
                if data[0] == vehicle_no:
                    found = True
                    print("1. Pending")
                    print("2. In Progress")
                    print("3. Completed")
                    choice = int(input("Choice: "))
                    if choice == 1:
                        data[5] = "Pending"
                    elif choice == 2:
                        data[5] = "In Progress"
                    elif choice == 3:
                        data[5] = "Completed"
                    else:
                        print("Invalid Choice")
                        return
                temp.append(",".join(data))
            file.close()
            if found:
                file = open(self.file, "w")
                for i in temp:
                    file.write(i + "\n")
                file.close()
                print("Status Updated")
            else:
                print("Vehicle Not Found")
        except:
            print("Error")

    def generate_bill(self):
        vehicle_no = self.validate_vehicle()
        try:
            file = open(self.file, "r")
            found = False
            for i in file:
                data = i.strip().split(",")
                if data[0] == vehicle_no:
                    found = True
                    print("\n")
                    print("_________BILL_________")
                    print("Vehicle :", data[0])
                    print("Owner :", data[1])
                    print("Services :", data[2])
                    print("Mechanic :", data[4])
                    print("Status :", data[5])
                    print("Towing :", data[6])
                    print("Parts :", data[7])
                    print("Amount : Rs", data[3])
                    break
            file.close()
            if found == False:
                print("Vehicle Not Found")
        except:
            print("Error")
            
    def view_all_records(self):
        try:
            file = open(self.file, "r")
            found = False
            for i in file:
                data = i.strip().split(",")
                found = True
                print("\n------------------")
                print("Vehicle :", data[0])
                print("Owner :", data[1])
                print("Services :", data[2])
                print("Amount :", data[3])
                print("Mechanic :", data[4])
                print("Status :", data[5])
            file.close()
            if found == False:
                print("No Records Found")
        except:
            print("No Records Found")
            
    def spare_parts(self):
        vehicle_no = self.validate_vehicle()
        if self.vehicle_extempts(vehicle_no):
            spare = SparePartsManager()
            spare.add_parts(vehicle_no)
        else:
            print("Vehicle Not Found")

    def spare_parts_gradio(self, vehicle_no, parts):

        prices = {
            "Brake Pads": 500,
            "Spark Plug": 300,
            "Oil Filter": 400,
            "Car Battery": 4500
        }

        try:

            total_parts_cost = 0

            for part in parts:
                total_parts_cost += prices[part]

            file = open(self.file, "r")

            temp = []

            found = False

            for line in file:

                data = line.strip().split(",")

                if data[0] == vehicle_no.upper():

                    found = True

                    data[7] = "|".join(parts)

                    amount = int(data[3])
                    amount += total_parts_cost

                    data[3] = str(amount)

                temp.append(",".join(data))

            file.close()

            if not found:
                return "Vehicle Not Found"

            file = open(self.file, "w")

            for row in temp:
                file.write(row + "\n")

            file.close()

            return f"Parts Added Successfully\nAdded Cost : Rs {total_parts_cost}"

        except Exception as e:
            return str(e)
                
        def towing(self):
            vehicle_no = self.validate_vehicle()
            if self.vehicle_extempts(vehicle_no):
                tow = TowingManager()
                tow.create_request(vehicle_no)
            else:
                print("Vehicle Not Found")

    def towing_gradio(self, vehicle_no, towing_service):

        towing_prices = {
            "Fuel Delivery": 800,
            "Battery Service": 500,
            "Puncture Service": 400,
            "Emergency Towing": 3500
        }

        try:

            file = open(self.file, "r")

            temp = []

            found = False

            for line in file:

                data = line.strip().split(",")

                if data[0] == vehicle_no.upper():

                    found = True

                    data[6] = towing_service

                    amount = int(data[3])
                    amount += towing_prices[towing_service]

                    data[3] = str(amount)

                temp.append(",".join(data))

            file.close()

            if not found:
                return "Vehicle Not Found"

            file = open(self.file, "w")

            for row in temp:
                file.write(row + "\n")

            file.close()

            return f"Towing Service Added\nCharge : Rs {towing_prices[towing_service]}"

        except Exception as e:
            return str(e)       
                
    def regtempter_vehicle_gradio(self, vehicle_no, owner):
        if self.vehicle_extempts(vehicle_no.upper()):
            return "Vehicle Already Regtemptered"
        vehicle = Vehicle(vehicle_no.upper(), owner)
        vehicle.services.append("Vehicle Inspection")
        vehicle.amount = 500
        self.save_vehicle(vehicle)
        return "Vehicle Regtemptered Successfully"

    def search_vehicle_gradio(self, vehicle_no):
        try:
            file = open(self.file, "r")
            for i in file:
                data = i.strip().split(",")
                if data[0] == vehicle_no.upper():
                    file.close()

                    return (
                        f"Vehicle : {data[0]}\n"
                        f"Owner : {data[1]}\n"
                        f"Services : {data[2]}\n"
                        f"Amount : {data[3]}\n"
                        f"Mechanic : {data[4]}\n"
                        f"Status : {data[5]}"
                    )

            file.close()
            return "Vehicle Not Found"
        except:
            return "Error"
    def assign_mechanic_gradio(self, vehicle_no, mechanic):

        try:
            file = open(self.file, "r")
            temp = []
    
            for line in file:
                data = line.strip().split(",")
    
                if data[0] == vehicle_no.upper():
                    data[4] = mechanic
    
                temp.append(",".join(data))
    
            file.close()
    
            file = open(self.file, "w")
    
            for row in temp:
                file.write(row + "\n")
    
            file.close()
    
            return "Mechanic Assigned Successfully"
    
        except:
            return "Error"

    def update_status_gradio(self, vehicle_no, status):

        try:
            file = open(self.file, "r")
            temp = []
    
            for line in file:
                data = line.strip().split(",")
    
                if data[0] == vehicle_no.upper():
                    data[5] = status
    
                temp.append(",".join(data))
    
            file.close()
    
            file = open(self.file, "w")
    
            for row in temp:
                file.write(row + "\n")
    
            file.close()
    
            return "Status Updated"
    
        except:
            return "Error"


    def generate_bill_gradio(self, vehicle_no):

            try:
                file = open(self.file, "r")
        
                for line in file:
        
                    data = line.strip().split(",")
        
                    if data[0] == vehicle_no.upper():
        
                        file.close()
        
                        return f"""
        BILL
        
        Vehicle : {data[0]}
        Owner : {data[1]}
        
        Services :
        {data[2]}
        
        Amount : Rs {data[3]}
        
        Mechanic : {data[4]}
        Status : {data[5]}
        Towing : {data[6]}
        Parts : {data[7]}
        """
        
                file.close()
                return "Vehicle Not Found"
        
            except:
                return "Error"



    def view_all_records_gradio(self):

        try:
    
            file = open(self.file, "r")
    
            result = ""
    
            for line in file:
    
                data = line.strip().split(",")
    
                result += f"""
    Vehicle : {data[0]}
    Owner : {data[1]}
    Status : {data[5]}
    Amount : Rs {data[3]}
    -------------------------
    """
    
            file.close()
    
            return result if result else "No Records Found"
    
        except:
            return "No Records Found"

            
class SparePartsManager:
    def add_parts(self, vehicle_no):
        parts_bill = 0
        parts_ltempt = []
        while True:
            print("\nAvailable Parts")
            print("1. Brake Pads      Rs 500")
            print("2. Spark Plug      Rs 300")
            print("3. Oil Filter      Rs 400")
            print("4. Car Battery     Rs 4500")
            print("5. Done")
            choice = int(input("Choice: "))
            if choice == 1:
                parts_ltempt.append("Brake Pads")
                parts_bill += 500
            elif choice == 2:
                parts_ltempt.append("Spark Plug")
                parts_bill += 300
            elif choice == 3:
                parts_ltempt.append("Oil Filter")
                parts_bill += 400
            elif choice == 4:
                parts_ltempt.append("Car Battery")
                parts_bill += 4500
            elif choice == 5:
                break
            else:
                print("Invalid Choice")
        try:
            file = open("service_records.csv", "r")
            temp = []
            for i in file:
                data = i.strip().split(",")
                if data[0] == vehicle_no:
                    data[7] = "|".join(parts_ltempt)
                    amount = int(data[3])
                    amount += parts_bill
                    data[3] = str(amount)
                temp.append(",".join(data))
            file.close()
            file = open("service_records.csv", "w")
            for i in temp:
                file.write(i + "\n")
            file.close()
            print("Parts Added Successfully")
        except:
            print("Error")
            
class TowingManager:
    def create_request(self, vehicle_no):
        print("\n")
        print("1. Fuel Empty")
        print("2. Battery Dead")
        print("3. Puncture")
        print("4. Brake Failure")
        choice = int(input("Choice: "))
        service = ""
        charge = 0
        if choice == 1:
            service = "Fuel Delivery"
            charge = 800
        elif choice == 2:
            service = "Battery Service"
            charge = 500
        elif choice == 3:
            service = "Puncture Service"
            charge = 400
        elif choice == 4:
            service = "Emergency Towing"
            charge = 3500
        else:
            print("Invalid Choice")
            return
        try:
            file = open("service_records.csv", "r")
            temp = []
            for i in file:
                data = i.strip().split(",")
                if data[0] == vehicle_no:
                    data[6] = service
                    amount = int(data[3])
                    amount += charge
                    data[3] = str(amount)
                temp.append(",".join(data))
            file.close()
            file = open("service_records.csv", "w")
            for i in temp:
                file.write(i + "\n")
            file.close()
            print("Towing Request Created")
        except:
            print("Error")
service = ServiceManager()
with gr.Blocks() as app:
    gr.Markdown("# Vehicle Service Management")
    with gr.Tab("Regtempter Vehicle"):
        vehicle = gr.Textbox(label="Vehicle Number")
        owner = gr.Textbox(label="Owner Name")
        regtempter_btn = gr.Button("Regtempter")
        regtempter_output = gr.Textbox()
        regtempter_btn.click(
            service.regtempter_vehicle_gradio,
            inputs=[vehicle, owner],
            outputs=regtempter_output
        )
    with gr.Tab("Search Vehicle"):
        search_vehicle = gr.Textbox(
            label="Vehicle Number"
        )
        search_btn = gr.Button("Search")
        search_output = gr.Textbox(lines=10)
        search_btn.click(
            service.search_vehicle_gradio,
            inputs=search_vehicle,
            outputs=search_output
        )
    with gr.Tab("Assign Mechanic"):

        vehicle_no = gr.Textbox(label="Vehicle Number")
        mechanic = gr.Textbox(label="Mechanic Name")
    
        btn = gr.Button("Assign")
    
        output = gr.Textbox()
    
        btn.click(
            service.assign_mechanic_gradio,
            inputs=[vehicle_no, mechanic],
            outputs=output
        )    
    
    with gr.Tab("Update Status"):

        vehicle_no = gr.Textbox(label="Vehicle Number")
    
        status = gr.Dropdown(
            ["Pending", "In Progress", "Completed"],
            label="Status"
        )
    
        btn = gr.Button("Update")
    
        output = gr.Textbox()
    
        btn.click(
            service.update_status_gradio,
            inputs=[vehicle_no, status],
            outputs=output
        )

    with gr.Tab("Generate Bill"):

            vehicle_no = gr.Textbox(label="Vehicle Number")
        
            btn = gr.Button("Generate Bill")
        
            output = gr.Textbox(lines=15)
        
            btn.click(
                service.generate_bill_gradio,
                inputs=vehicle_no,
                outputs=output
            )

    with gr.Tab("View Records"):

        btn = gr.Button("Show All Records")
    
        output = gr.Textbox(lines=20)
    
        btn.click(
            service.view_all_records_gradio,
            outputs=output
        )

    with gr.Tab("Spare Parts"):

        vehicle_no = gr.Textbox(
            label="Vehicle Number"
        )

        parts = gr.CheckboxGroup(
            choices=[
                "Brake Pads",
                "Spark Plug",
                "Oil Filter",
                "Car Battery"
            ],
            label="Select Spare Parts"
        )

        btn = gr.Button("Add Parts")

        output = gr.Textbox()

        btn.click(
            service.spare_parts_gradio,
            inputs=[vehicle_no, parts],
            outputs=output
        )

    with gr.Tab("Towing Service"):

        vehicle_no = gr.Textbox(
            label="Vehicle Number"
        )

        towing_service = gr.Radio(
            [
                "Fuel Delivery",
                "Battery Service",
                "Puncture Service",
                "Emergency Towing"
            ],
            label="Select Service"
        )

        btn = gr.Button("Create Request")

        output = gr.Textbox()

        btn.click(
            service.towing_gradio,
            inputs=[vehicle_no, towing_service],
            outputs=output
        )


app.launch()