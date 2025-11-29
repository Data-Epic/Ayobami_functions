# Function That Uses a Global Variable
school_name = "OAU"

def print_school():
    school_name = "OUI"
    print(f"The name of the school is: {school_name}")
print_school()

print(f"The name of the school is: {school_name}")