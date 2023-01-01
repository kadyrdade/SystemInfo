import pyfiglet, socket, uuid, requests, platform

# Banner
ascii_banner = pyfiglet.figlet_format("System Info")
print(ascii_banner)

# Get system info 
my_system = platform.uname()

print(f"System            : {my_system.system}")
print(f"Node Name         : {my_system.node}")
print(f"Release           : {my_system.release}")
print(f"Version           : {my_system.version}")
print(f"Machine           : {my_system.machine}")

# Get localhost and localhost adress
hostname = socket.gethostname()   
IPAddr = socket.gethostbyname(hostname)   
print("Hostname          : " + hostname)   
print("Localhost Address : " + IPAddr) 

# get MAC adress
print("MAC address       : ", end="")
print (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
for ele in range(0,8*6,8)][::-1]))

# Get ip adress
# ip = get('https://api.ipify.org').content.decode('utf8')
# print('My public IP address is: {}'.format(ip))

# # Get ip adress
# def get_ip():
#     response = requests.get('https://api64.ipify.org?format=json').json()
#     return response["ip"]

# # get location with ip adress
# def get_location():
#     ip_address = get_ip()

#     response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    
#     location_data = {
#         "Public IP adress  :": ip_address,
#         "Country           :": response.get("country_name"),
#         "City              :": response.get("city"),
#         "Region            :": response.get("region")
#     }
    
#     for key, value in location_data.items():
#         if key == 'Region            :':
#             print(key, value)
#             break
#         else:
#             print(key, value)

# print(get_location())