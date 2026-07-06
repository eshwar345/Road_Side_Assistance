#!/usr/bin/env python
# coding: utf-8

# In[15]:


parts = [{"name": "Brake Pads", "Quantity": 4, "Price": 45,"used": 0},
{"name": "Spark Plug", "Quantity": 6, "Price": 12,"used": 0},
{"name": "Oil Filter", "Quantity": 2, "Price": 15,"used": 0},
{"name": "Car Battery", "Quantity": 1, "Price": 120,"used": 0},
{"name": "Windshield Wipers", "Quantity": 2, "Price": 25,"used": 0},
{"name": "Air Filter", "Quantity": 2, "Price": 20,"used": 0},
{"name": "Cabin Air Filter", "Quantity": 1, "Price": 22,"used": 0},
{"name": "Brake Rotor", "Quantity": 2, "Price": 85,"used": 0},
{"name": "Alternator", "Quantity": 1, "Price": 150,"used": 0},
{"name": "Starter Motor", "Quantity": 1, "Price": 130,"used": 0},
{"name": "Serpentine Belt", "Quantity": 1, "Price": 35,"used": 0},
{"name": "Radiator Hose", "Quantity": 2, "Price": 18,"used": 0},
{"name": "Thermostat", "Quantity": 1, "Price": 25,"used": 0},
{"name": "Water Pump", "Quantity": 1, "Price": 75,"used": 0},
{"name": "Fuel Pump", "Quantity": 1, "Price": 110,"used": 0},
{"name": "Fuel Filter", "Quantity": 1, "Price": 28,"used": 0},
{"name": "Oxygen Sensor", "Quantity": 2, "Price": 65,"used": 0},
{"name": "Ignition Coil", "Quantity": 4, "Price": 40,"used": 0},
{"name": "Headlight Bulb", "Quantity": 2, "Price": 15,"used": 0},
{"name": "Tail Light Bulb", "Quantity": 2, "Price": 8,"used": 0},
{"name": "Shock Absorber", "Quantity": 2, "Price": 95,"used": 0},
{"name": "Strut Assembly", "Quantity": 2, "Price": 140,"used": 0},
{"name": "Control Arm", "Quantity": 2, "Price": 70,"used": 0},
{"name": "Ball Joint", "Quantity": 2, "Price": 30,"used": 0},
{"name": "Tie Rod End", "Quantity": 2, "Price": 25,"used": 0},
{"name": "Wheel Bearing", "Quantity": 2, "Price": 55,"used": 0},
{"name": "CV Axle", "Quantity": 1, "Price": 115,"used": 0},
{"name": "Clutch Kit", "Quantity": 1, "Price": 220,"used": 0},
{"name": "Brake Caliper", "Quantity": 2, "Price": 90,"used": 0},
{"name": "Distributor Cap", "Quantity": 1, "Price": 32,"used": 0},
{"name": "Timing Belt", "Quantity": 1, "Price": 60,"used": 0},
{"name": "Drive Belt Tensioner", "Quantity": 1, "Price": 45,"used": 0},
{"name": "Radiator", "Quantity": 1, "Price": 160,"used": 0},
{"name": "Condenser", "Quantity": 1, "Price": 125,"used": 0},
{"name": "EGR Valve", "Quantity": 1, "Price": 85,"used": 0},
{"name": "PCV Valve", "Quantity": 1, "Price": 10,"used": 0},
{"name": "Wheel Hub Assembly", "Quantity": 2, "Price": 105,"used": 0},
{"name": "Brake Master Cylinder", "Quantity": 1, "Price": 75,"used": 0},
{"name": "Sway Bar Link", "Quantity": 2, "Price": 22,"used": 0},
{"name": "Engine Mount", "Quantity": 3, "Price": 50,"used": 0},
{"name": "Transmission Mount", "Quantity": 1, "Price": 45,"used": 0},
{"name": "Brake Hose", "Quantity": 2, "Price": 20,"used": 0},
{"name": "Muffler", "Quantity": 1, "Price": 95,"used": 0},
{"name": "Catalytic Converter", "Quantity": 1, "Price": 250,"used": 0},
{"name": "Exhaust Manifold Gasket", "Quantity": 1, "Price": 15,"used": 0}
]


# In[16]:


def add_item():
    try:
        part_name = str(input("Part Name: "))
        required_quantity = int(input("Quantity: "))
        if required_quantity <= 0:
            print("Invalid Quantity")
            return
        part_price = int(input("Price: "))
        if part_price <= 0:
            print("Invalid Price")
            return
        temp = {
            "name": part_name,
            "Quantity": required_quantity,
            "Price": part_price,
            "used": 0
        }
        parts.append(temp)
        print("Part Added")
    except Exception as e:
        print("please enter valid details",e)


# In[17]:


def search_part():
    try:
        search_name = str(input("Part Name: "))
        for i in parts:
            if i["name"].lower() == search_name.lower():
                print(f"+-------Part Found-----------+")
                print(f"| Name: {i['name']}            |")
                print(f"| Quantity: {i['Quantity']}    |")
                print(f"| Price: {i['Price']}          |")
                print(f"+----------------------------+")
                return
        print("Part Not Found")
    except Exception as e :
            print("enter valid information",e)


# In[24]:


def issue_part():
    bill = []
    grand_total = 0

    try:
        while True:
            name = input("Part Name: ").strip()
            qty = int(input("Required Quantity: "))

            if qty <= 0:
                print("Quantity must be greater than 0")
                continue

            found = False

            for part in parts:
                if part["name"].lower() == name.lower():
                    found = True

                    if part["Quantity"] >= qty:
                        part["Quantity"] -= qty
                        part["used"] += qty

                        total = qty * part["Price"]
                        grand_total += total

                        bill.append({
                            "name": part["name"],
                            "qty": qty,
                            "price": part["Price"],
                            "total": total
                        })

                        print("Part Added")
                    else:
                        print(f"Insufficient Stock. Available: {part['Quantity']}")
                    break

            if not found:
                print("Part Not Found")

            more = input("Add Another Part? (yes/no): ").strip().lower()
            if more != "yes":
                break

        if bill:
            print("\n" + "=" * 40)
            print("         SPARE PARTS RECEIPT")
            print("=" * 40)

            for item in bill:
                print(f"Part Name : {item['name']}")
                print(f"Quantity  : {item['qty']}")
                print(f"Unit Price: ₹{item['price']}")
                print(f"Total     : ₹{item['total']}")
                print("-" * 40)

            print(f"Grand Total: ₹{grand_total}")
            print("=" * 40)
        else:
            print("No parts issued.")

    except ValueError:
        print("Please enter a valid numeric quantity.")
    except Exception as e:
        print("Error:", e)


# In[19]:


def restock_part():
    try:
        name = str(input("Part Name: "))
        qty = int(input("New Quantity: "))
        for i in parts:
            if i["name"].lower() == name.lower():
                if qty <= 0:
                    print("Quantity must be positive")
                    return
                i["Quantity"] += qty
                print("Stock Updated")
                return
        print("Part Not Found")
    except Exception as e:
            print("enter valid information",e)


# In[20]:


def low_stock_alert():
    print("LOW STOCK PARTS")
    found = False
    for i in parts:
        if i["Quantity"] <= 5:
            found = True
            print(i["name"], "-", i["Quantity"])
    if found == False:
        print("No Low Stock Parts")


# In[21]:


def most_used_parts():
    highest = 0
    part_name = ""
    for i in parts:
        if i["used"] > highest:
            highest = i["used"]
            part_name = i["name"]
    if part_name == "":
        print("No Parts Used Yet")
    else:
        print("Most Used Part:", part_name)
        print("Used:", highest)


# In[22]:


def parts_report():
    print("\nPARTS REPORT")
    for i in parts:
        print("\nName:", i["name"])
        print("Quantity:", i["Quantity"])
        print("Price:", i["Price"])
        print("Used:", i["used"])


# In[23]:


def main():
    while True:
        try:
            parts
            print("\nSPARE PARTS MANAGEMENT")
            print("1. Add Part")
            print("2. Search Part")
            print("3. purchase Part")
            print("4. Restock Part")
            print("5. Low Stock Alert")
            print("6. Most Used Part")
            print("7. Parts Report")
            print("8. Exit")
            choice = int(input("Choice: "))
            if choice == 1:
                add_item()
            elif choice == 2:
                search_part()
            elif choice == 3:
                issue_part()
            elif choice == 4:
                restock_part()
            elif choice == 5:
                low_stock_alert()
            elif choice == 6:
                most_used_parts()
            elif choice == 7:
                parts_report()
            elif choice == 8:
                break
            else:
                print("Invalid Choice")
        except Exception as e:
            print("please enter valid information",e)


# In[ ]:





# In[ ]:





# In[ ]:




