menu = {"Dosa": 59.99, "Idli": 35, "pasta": 199.99 }

print(f"pasta costs : {menu['pasta']}\n")

print("***\tMENU\t***\n")
for k, v in menu.items():
    print(f"{k.capitalize()} \t Rs.{v}")

print("\n==================\n ")