#Task 1: Create a Simple List
linux_distros = ["Ubuntu", "CentOS", "Debian", "Rocky Linux"]
print(linux_distros)

#Task 2: Access List Items
linux_distros = ["Ubuntu", "CentOS", "Debian", "Rocky Linux"]
print(f"first distro: {linux_distros[0]} \nLast distro: {linux_distros[-1]}")


#Task 3: List Indexing
#Create a list:

tools = ["Git", "Docker", "Kubernetes", "Jenkins", "Terraform"]
print(f"{tools[1]} \n{tools[2]} \n{tools[-1]}")
print(tools[1])
print(tools[2])
print(tools[-1])
print(tools[0])

#Task 4: Negative Indexing in Lists
tools = ["Git", "Docker", "Kubernetes", "Jenkins", "Terraform"]
print(tools[-2])
print(tools[-1])

#Task 5: Add Items to a List
cloud_providers = ["AWS", "Azure"]
cloud_providers.insert(2,"Google Cloud")
print(cloud_providers)
cloud_providers.append("Docker")
print(cloud_providers)

# Insert Item at a Specific Position
services = ["nginx", "mysql", "redis"]
services.insert(1, "apache")
print(services)
#Task 7: Update a List Item
environments = ["dev", "test", "stage"]
environments[1]="qa"
print(environments)

#Task 8: Remove an Item from a List
packages = ["httpd", "nginx", "mysql", "php"]
packages.pop()
print(packages)

#Task 9: List Length
users = ["alice", "bob", "charlie", "david"]
print(len(users))

#Task 10: List Slicing
servers = ["web01", "web02", "db01", "db02", "cache01"]
print(servers[0:3])

###Part 2: Working with Dictionaries
#Task 11: Create a Simple Dictionary
student = {
    "name":"Kesari",
    "Course":"Python for GenAI",
    "City":"Dallas"
}
print(student)

#Task 12: Access Dictionary Values
student = {
    "name": "Rahul",
    "course": "Python for DevOps",
    "city": "Delhi"
}
print(f"Name: {student["name"]}")
print(f"Course: {student["course"]}")
print(f"City: {student["city"]}")

#Task 13: Create a Server Dictionary

server = {
    "hostname": "web01",
    "ip": "192.168.1.10",
    "os": "Ubuntu",
    "status": "running"
}

print(f"Server {server["hostname"]} is {server["status"]} on {server["ip"]}")

#Task 14: Update Dictionary Value
service = {
    "name": "nginx",
    "status": "stopped"
}
service["status"]="running"
print(service)

#Task 15: Add a New Key to Dictionary
employee = {
    "name": "Amit",
    "role": "DevOps Engineer"
}
employee["experience"]= "2 years"
print(employee)

#Delete a Key from Dictionary
vm = {
    "name": "vm01",
    "cpu": 2,
    "memory": "4GB",
    "temporary": True
}
del vm["temporary"]
print(vm)

#Task 17: Dictionary Keys and Values
docker_container = {
    "name": "webapp",
    "image": "nginx:latest",
    "port": 80
}
print((docker_container).keys())
print((docker_container).values())

#Task 18: Check if Key Exists

config = {
    "debug": True,
    "port": 8000,
    "host": "0.0.0.0"
}
if "port" in config:
    print("port configuration exists")

    ##Part 3: Working with Tuples
    #Task 19: Create a Tuple

    ports =(22, 80, 443, 3306)
    print(ports)

# Task 21: Negative Indexing in Tuples
protocols = ("ssh", "http", "https", "mysql")

print(protocols[-1])

#Task 22: Tuple Length

regions = ("ap-south-1", "us-east-1", "eu-west-1")
print(len(regions))

#Tuple Slicing
backup_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
print(backup_days[0:3])

#Task 24: Understand Tuple Immutability
#database_ports = (3306, 5432, 27017)
#database_ports[0] = 3307
#print(database_ports)

#Part 4: Mixed Practice
#Task 25: List of Dictionaries

servers = [
    {"name": "web01", "ip": "10.0.0.11", "role": "web"},
    {"name": "db01", "ip": "10.0.0.12", "role": "database"},
    {"name": "cache01", "ip": "10.0.0.13", "role": "cache"}
]
print(servers[1]["ip"])

##Task 26: Dictionary with List Value
project = {
    "name": "RAG Application",
    "services": ["frontend", "backend", "qdrant"],
    "environment": "dev"
}

print(project["services"])

#Task 27: Add a Service to Dictionary List
project = {
    "name": "RAG Application",
    "services": ["frontend", "backend", "qdrant"],
    "environment": "dev"
}
project["services"].append("reddis")
print(project["services"])

#Task 28: Tuple Inside Dictionary
app_config = {
    "app_name": "student-api",
    "allowed_ports": (8000, 8080),
    "debug": True
}
print(app_config["allowed_ports"])

#Task 29: DevOps Inventory Structure

inventory = {
    "web_servers": ["web01", "web02"],
    "db_servers": ["db01"],
    "load_balancer": "lb01"
}
print(inventory)