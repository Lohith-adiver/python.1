def comma_code(items):
    if not items:
        return ''
    elif len(items) == 1:
        return items[0]
    else:
        return ', '.join(items[:-1]) + ' and ' + items[-1]

items = input("Enter items separated by commas: ").split(',')
items = [item.strip() for item in items]  
result = comma_code(items)
print("Formatted list:", result)
