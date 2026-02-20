inventory = {"laptop": 1200.99, "mouse": 25.50, "printer": 13.45}

print("-"*30)
print(f"{'Item':<12}{'Price':>10}")
print("-"*30)

for k, v in inventory.items():
    print(f"{k.capitalize():<12} \t ${v:>9.2f}")
