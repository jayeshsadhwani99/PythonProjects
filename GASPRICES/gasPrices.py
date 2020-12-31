import matplotlib.pyplot as plt
import pandas as pd

gas = pd.read_csv('GASPRICES\gas_prices.csv')

plt.figure(figsize = (8, 5), dpi = 300)
plt.title("Gas Prices over time(in USD)", fontdict=None)

plt.plot(gas.Year, gas.USA, 'b.-', label="USA")
plt.plot(gas.Year, gas.Canada, 'r.-', label="Canada")
plt.plot(gas.Year, gas['South Korea'], 'g.-', label="South Korea")
plt.plot(gas.Year, gas.Australia, 'y.-', label="Australia")

plt.xticks(gas.Year[::3].tolist() + [2011])

plt.xlabel('Year')
plt.ylabel('US Dollars')

plt.legend()
# plt.savefig('GasPrice.png', dpi = 300)

plt.show()