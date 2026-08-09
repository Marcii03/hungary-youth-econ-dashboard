"""
Chart 2: house prices vs. youth income in Hungary.
Datasets: prc_hpi_a (house price index) and ilc_di03 (median income by age),
both indexed to 2015 = 100.
"""

import eurostat
import matplotlib.pyplot as plt

df = eurostat.get_data_df("prc_hpi_a")
avg_house_prices = df[(df["purchase"] == "TOTAL") & (df["unit"] == "I15_A_AVG") & (df[r"geo\TIME_PERIOD"] == "HU")]
house_prices_series = avg_house_prices.loc[:, "2007":"2025"].squeeze()

income_df = eurostat.get_data_df("ilc_di03")
youth_income = income_df[(income_df["age"] == "Y18-24") & (income_df["statinfo"] == "MED_EI") & (income_df["sex"] == "T") & (income_df["unit"] == "NAC") & (income_df[r"geo\TIME_PERIOD"] == "HU")]
youth_income_series = youth_income.loc[:, "2007":"2025"].squeeze()

reference_point_income = youth_income_series["2015"]
youth_income_index = youth_income_series / reference_point_income * 100

plt.plot(house_prices_series.index, house_prices_series.values, label="House price index")
plt.plot(youth_income_index.index, youth_income_index.values, label="Median income, ages 18-24")
plt.xlabel("Year")
plt.xticks(["2010", "2015", "2020", "2025"])
plt.ylabel("Index (2015 = 100)")
plt.title("Hungarian house prices vs. youth income 2007-2025")
plt.legend()
plt.savefig("house_prices/house_prices_vs_youth_income.png")
