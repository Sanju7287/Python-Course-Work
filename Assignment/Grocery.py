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