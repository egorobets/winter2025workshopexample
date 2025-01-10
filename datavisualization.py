import pandas
import matplotlib.pyplot as plt
import plotly.graph_objs as go

print("all packages imported successfully")

cities = ["Austin","Dallas","Houston","San Antonio","El Paso","Abilene"]
developercounts = [20000,10000,15000,8000,6000, 1000]

fig, axs = plt.subplots()
axs.set_title("Count of Developers in Major Texas Cities")
axs.bar (cities, developercounts, color="#00aa00", edgecolor="#005500")
plt.savefig(r"C:\Users\eduar\OneDrive\Documentos\Scripts\pythonworkshop\barchart.png")


treedata - pd.read_csv(r"C:\Users\eduar\OneDrive\Desktop\treedata.csv")

print(treedata['DBH'])
print(treedata['TreeHeight'])