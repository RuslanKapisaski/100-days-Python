import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_Squirrel_Data.csv", encoding="latin1")

cinnamon_c = data[data["Primary Fur Color"] == "Cinnamon"].shape[0]
gray_c = data[data["Primary Fur Color"] == "Gray"].shape[0]
black_c = data[data["Primary Fur Color"] == "Black"].shape[0]

# N.B: In pandas, every DataFrame has a shape attribute! shape[0] returns number of rows; shape[1] return number of columns
data_dic = {
    "Color": ['Gray','Cinnamon','Black'],
    "Count": [gray_c,cinnamon_c,black_c]
}

df = pandas.DataFrame(data_dic)
df.to_csv("squirrel_analytics.csv")
