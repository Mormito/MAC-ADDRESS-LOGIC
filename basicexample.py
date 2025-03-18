
# Yes, I know, always adding a MAC address to the address list is incorrect, I did this because it is just an example.
# If i wanted to improve this code, i would add a system to validate if the MAC is equals a "real computer in network" 

addresslist = ["AA-AA", "BB-BB"]

def sendMessage():
    
    destination = "AA-AA"
    origin = "CC-CC"
    type = "text"
    data = 60

    mindata = 64
    pad = mindata - data

    if data < mindata:
        data = data + pad
        print("Pad added to data")
    else: print("Maximum data exceeded")

    # NO CRC...
    return destination, origin, type, data

def ethernetframe():
    destination, origin, type, data = sendMessage()
    print("Preamble started")

    if destination in addresslist:
        print("Destination address found in address list")
    else:
        print("Destination address not found in address list")
        addresslist.append(destination)  
        print("- Destination address added in adress list")

    if origin in addresslist:
        print("Origin address found in address list")
    else:
        print("Origin address not found in address list")      
        addresslist.append(origin)  
        print("- Origin address added in adress list")

ethernetframe()
