# Membuat dictionary
data = {"name": "Alice", "age": 30, "city": "Surabaya"}

# Mengakses nilai dengan key
print(data["name"])  # Output: Alice

# Mengubah nilai dengan key
data["age"] = 31

# Menambahkan key-value baru
data["occupation"] = "Software Engineer"

# Menghapus key-value
del data["city"]

# Meloop melalui key-value
for key, value in data.items():
  print(key, ":", value)
