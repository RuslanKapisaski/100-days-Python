import csv
import pandas

# Open file
def print_data():
    with open('weather_data.csv.csv') as f:
       data = f.readlines()
       print(data)

#CSV
# Print Temperatures
def print_temp():
    with open('weather_data.csv.csv') as f:
        data = csv.reader(f)
        temperatures = []
        next(data)
        for row in data:
            temp = int(row[1])
            temperatures.append(temp)
        print(temperatures)

#Pandas
data = pandas.read_csv("weather_data.csv")
# Calculate average temp
def calc_avg_temp():
    temps_sum = 0
    for temp in data["temp"]:
        temps_sum += float(temp)
    avg_temp = round((temps_sum / len(data)),2)
    print(f"Average temp for the week is: {avg_temp} degrees celsius")

    # Simplest method for calculating average
    avg_temp2 = round(data["temp"].mean(),2)
    print(f"Average temp for the week is: {avg_temp2} degrees celsius")

# Calculate max temp
def calc_max_temp():
    # Simplest method for calculating max
    max_temp = round(data["temp"].max(),2)
    print(f"Max temp for the week is: {max_temp} degrees celsius")

# Get the row of data with maximum temp
def calc_max_row_temp():
    max_temp = data.temp.max()
    print(max_temp)

# Get the Monday Celsius and convert it to Fahrenheit
def convert_c_to_f():
    monday_temp_cels  = data[data.day == "Monday"].temp.values[0]
    monday_temp_fahr = (9/5 * monday_temp_cels) + 32
    print(f"Monday temp in Fahrenheit: {monday_temp_fahr}")

# Create a dataframe from scratch
def create_dataframe():
    dict = {
        "names": ["Peter Bobkov", "Bobi Petkov", "Ivan Ivanov"],
        "cities": ["Sofia", "Petrich", "Blagoevgrad"]
    }

    df = pandas.DataFrame(dict)
    df.to_csv("sample.csv")
    print(df)

# Try:
# print_data()
# print_temp()
# calc_avg_temp()
# calc_max_temp()
#calc_max_row_temp()
# convert_c_to_f()
# create_dataframe()
