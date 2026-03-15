#Nesting Lists inside dictionaries
# See if you can figure out how to print out "Lille" from the nested List called travel_log.
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

print(travel_log["France"][1])

# Nesting Lists inside other Lists
# We've previously seen Nested Lists:
# How to print 'D'
nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][1])

# Figure out how to print "Stuttgart" in this nested dictionary:

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
}


print(travel_log["Germany"]["cities_visited"][2])