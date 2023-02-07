"""Lab Purpose: Separate an IP address after receiving it from a user, and convert it to a binary value."""

print ("This program will separate and convert each octet of an IPv4 address into a binary value.\n") # explains the purpose of the script

ip_address = input("Please enter an IPv4 address: ") # 192.168.88.12
ip_octets = ip_address.split(".") # 

print(ip_octets) # ['192', '168', '88', '12']

First = int(ip_octets[0]) # integer 192
Second = int(ip_octets[1]) # 168 
Third = int(ip_octets[2]) # 88
Fourth = int(ip_octets[3]) # 12

print(f"{First} : {bin(First)[2:]}")

print("{} : {}".format(Second, bin(Second)[2:]))
print("{} : {}".format(Third, bin(Third)[2:]))
print("{} : {}".format(Fourth, bin(Fourth)[2:]))

input("\nPress 'Enter' to exit the program") # prevents program from closing upon execution

