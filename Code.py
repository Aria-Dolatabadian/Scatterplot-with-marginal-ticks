import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


# Read data from CSV into Python
mpg_from_csv = pd.read_csv("data.csv")

# Set seaborn theme
sns.set_theme(style="white", color_codes=True)

# Use JointGrid directly to draw a custom plot
g = sns.JointGrid(data=mpg_from_csv, x="Height", y="Leaf number", space=0, ratio=17)
g.plot_joint(sns.scatterplot, size=mpg_from_csv["Yield"], sizes=(30, 120),
             color="b", alpha=.6, legend=False)
g.plot_marginals(sns.rugplot, height=1, color="g", alpha=.6)

plt.show()
