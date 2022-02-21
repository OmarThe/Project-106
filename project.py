import plotly.express as px
import numpy as np
import csv

def plot():
    with open("Data3.csv") as f:
        df = csv.DictReader(f)
        fig1 = px.scatter(df, x ="Marks In Percentage", y ="Days Present")
        fig1.show()
# plot()

def getSource(data_file):
    marks = []
    daysPresent = []
    with open("Data3.csv") as f:
        df = csv.DictReader(f)
        for x in f:
            marks.append(float(x["Marks In Percentage"]))
            daysPresent.append(float(x["Days Present"]))

    return {"x":marks,"y":daysPresent}

source = getSource("Data3.csv")
correlation = np.corrcoef(source["x"], source["y"])

print(correlation)


    

