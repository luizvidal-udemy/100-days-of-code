import os
import pandas

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_PATH = os.path.join(
    CURRENT_DIR, "2018-central-park-squirrel-census-squirrel-data.csv"
)

OUTPUT_PATH = os.path.join(CURRENT_DIR, "squirrel_count.csv")

FUR_COLORS = ["Gray", "Cinnamon", "Black"]


def get_squirrel_count(squirrel_data, color):
    color_series = squirrel_data["Primary Fur Color"]
    return len(squirrel_data[color_series == color])


data = pandas.read_csv(DATA_PATH)


squirrel_count_data = {
    "Fur Color": [],
    "Count": []
}

for color in FUR_COLORS:
    squirrel_count_data["Count"].append(get_squirrel_count(data,color))
    squirrel_count_data["Fur Color"].append(
        "red" if color == "Cinnamon" else str.lower(color)
    )


pandas.DataFrame(squirrel_count_data).to_csv(OUTPUT_PATH)
