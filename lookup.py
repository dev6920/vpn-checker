import requests

def check_ip(ip_address):
    api_url = f"https://proxycheck.io/v2/{ip_address}?vpn=1&asn=1"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return {"error": "An error occurred while checking the IP address"}
with open("results.txt", "w") as file:
    while True:
        ip_address = input("Enter an IP address: ")
        result = check_ip(ip_address)
        print(result)
        file.write(str(result))
        file.write("\n")
        another = input("Want to check another IP address? (y/n) ")
        if another.lower() != "y":
            break
