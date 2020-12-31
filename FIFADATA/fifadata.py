import matplotlib.pyplot as plt
import pandas as pd

fifa = pd.read_csv("FIFADATA/fifa_data.csv")

plt.figure(figsize = (9, 5), dpi = 100)
plt.title("Skill Levels of Players in FIFA 2018")

bins = [40, 50, 60, 70, 80, 90, 100]

plt.hist(fifa.Overall, bins = bins, color = "#abcdef")

plt.xticks(bins)

plt.ylabel('Number of Players')
plt.xlabel('Skill Level')

# plt.savefig('FIFAScores.png', dpi = 300)

plt.show()