pnr=int(input("PNR ID: "))
name=input("Passenger Name: ")
price=float(input("Ticket Price (₹): "))
booking=input("Booking Type (Online/Counter): ")
stock=(int(input("Available Tickets: ")), int(input("Sold Tickets: ")))
discount=float(input("Aged Discount (%): "))
bus_type=input("Bus Type (AC/Sleeper): ")
features=set(input("Bus Features (comma-separated): ").split(','))
org={
    "name":input("Travel Company: "),
    "contact":input("Contact No: "),
    "location":input("Office Location: ")
}
print("\n--- Booking Summary ---")
print("PNR,Name,Price:",pnr,name,price,sep=", ")
print("Aged Discount:%.2f%%"% discount)
print(f"Passenger:{name},Price:₹{price},Type:{bus_type}")
print(f"Available:{stock[0]}|Sold:{stock[1]}")
print("Agency:{},{},{}".format(org["name"],org["contact"],org["location"]))
print("Features:", ", ".join(f.strip() for f in features))

#output
#PNR ID: 234567
#Passenger Name: sanjay
#Ticket Price (₹): 239
#Booking Type (Online/Counter): Online
#Available Tickets: 24
#Sold Tickets: 56
#Aged Discount (%): 23
#Bus Type (AC/Sleeper): Sleeper
#Bus Features (comma-separated): yes
#Travel Company: Morning star
#Contact No: 9846673837  
#Office Location: Hyderabad

#--- Booking Summary ---
#PNR,Name,Price:, 234567, sanjay, 239.0
#Aged Discount:23.00%
#Passenger:sanjay,Price:₹239.0,Type:Sleeper
#Available:24|Sold:56
#Agency:Morning star,9846673837,Hyderabad
#Features: yes