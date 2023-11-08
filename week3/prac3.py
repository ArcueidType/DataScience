import re
id = input("Your ID: ")
if len(id) != 18:
    print("Invalid")
    exit(0)
    
pattern = "(^[1-9]\\d{5}(18|19|20)\\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\\d{3}[0-9Xx]$)"

if re.match(pattern, id): 
    match = True
else:
    match = False

if match:
    print("Valid")
else:
    print("Invalid");
