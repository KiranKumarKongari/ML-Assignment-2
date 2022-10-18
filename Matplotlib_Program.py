# 1.Write a Python programming to create a below chart of the popularity of programming Languages.
# 2. Sample data:
# Programming languages: Java, Python, PHP, JavaScript, C#, C++
# Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7

# Imported pyplot sub package from matplotlib for creating the pie chart
from matplotlib import pyplot as plt

language = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# Creating explode data which helps us adjust partitions of the pie chart
explode = (0.1, 0.0, 0.0, 0.0, 0.0, 0.0)

# Creating color parameters which will be used for the partitions in the pie chart
colors = ("blue", "orange", "green", "red", "indigo", "brown")

# Wedge properties for setting the borders width and color
wedge_properties = {'linewidth': 1, 'edgecolor': "black"}


# Creating autocpt arguments
def autopact(pct):
    return "{:.1f}%".format(pct)


# Creating plot
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotext = ax.pie(popularity,
                                 autopct=lambda pct: autopact(pct),
                                 explode=explode,
                                 labels=language,
                                 shadow=True,
                                 colors=colors,
                                 startangle=140,
                                 wedgeprops=wedge_properties)

plt.setp(autotext, size=8, weight="bold")

# show plot
plt.show()
