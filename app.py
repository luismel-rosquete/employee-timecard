print("*******************************************************")
role = input("* Hello there. What's your role? Employee or Manager  *")
print("*******************************************************")
if role != "Employee":
    import manager
else:
    import employee
