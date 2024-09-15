import os
import pandas

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_PATH = os.path.join(
    CURRENT_DIR, "2018-central-park-squirrel-census-squirrel-data.csv"
)

OUTPUT_PATH = os.path.join(CURRENT_DIR, "squirrel_count.csv")

data = pandas.read_csv(DATA_PATH)

grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

squirrel_count_data = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(squirrel_count_data)

df.to_csv(OUTPUT_PATH)
