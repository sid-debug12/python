# Dictionaries
band = {
    "vocals": "Robert Plant",
    "guitar": "Page",
}

band2 = dict(vocals="Robert Plant", guitar="Page")

print(band)
print(band2)

# Accessing items in a dictionary

print(band["vocals"])
print(band.get("guitar"))

# list all keys
print(band.keys())

# list all values
print(band.values())

# list of keys/value pairs as tuples
print(band.items())

# verify a key exists
print("guitar" in band)
print("triangle" in band)


# how to change value in dictionary
band["guitar"] = "Jinny Page"
band.update({"bass": "JPJ"})
print(band)

# how to remove items in a dictionary
print(band.pop("bass"))
print(band)
band["drums"] = "John Bonham"
print(band)
print(band.popitem())
print(band)

# delete and clear
band["drums"] = "John Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

# copy value of a dictionary

band3 = band.copy()
print(band3)
band4 = dict(band)
print(band4)


# Nested dictionaries

member1 = {
    "name": "Robert Plant",
    "instrument": "vocals",
}

member2 = {
    "name": "Jinny Page",
    "instrument": "guitar",
}

band = {
    "member1": member1,
    "member2": member2,
}

print()
print(band)
