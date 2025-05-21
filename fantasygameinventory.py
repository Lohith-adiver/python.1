
print("name: Lohith Adiver")
print("USN: 1AY24AI063")
print("Section: O\n")

def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for item, count in inventory.items():
        print(f"{count} {item}")
        item_total += count
    print(f"Total number of items: {item_total}\n")

def add_to_inventory(inventory, added_items):
    for item in added_items:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory

inventory = {
    'rope': 1,
    'torch': 6,
    'gold coin': 42,
    'dagger': 1,
    'arrow': 12
}

dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

print("Initial Inventory:")
display_inventory(inventory)

inventory = add_to_inventory(inventory, dragon_loot)

print("Updated Inventory after collecting dragon loot:")
display_inventory(inventory)
