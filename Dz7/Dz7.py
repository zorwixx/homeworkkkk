result = []

def divider(a, b):
    if b == 0:
        raise ValueError("Неможна ділити на нуль")
    return a / b


data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except (ValueError, TypeError) as e:
        print(f"Error: {e} for key {key}")

print(result)
