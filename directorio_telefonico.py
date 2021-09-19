import re
tel=input("Introduzca el numero telefonico \n")
#pattern=r"\d{8}"
match= re.match(r"[1|8|9][\d]{7}",tel)
print(match)
if match:
    print("valid")
else:
    print("invalid")




