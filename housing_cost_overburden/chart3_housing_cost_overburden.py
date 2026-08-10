"""
Chart 3: housing cost overburden rate for young people (ages 18-24) in
Hungary, compared to the EU average.
Dataset: ilc_lvho07a (Eurostat housing cost overburden rate).
"""

import eurostat
import matplotlib.pyplot as plt

df = eurostat.get_data_df("ilc_lvho07a")

hu_filtered = df[(df["age"] == "Y18-24") & (df["rskpovth"] == "TOTAL") & (df[r"geo\TIME_PERIOD"] == "HU") & (df["sex"] == "T")]
hu_overburden_series = hu_filtered.loc[:, "2010":"2025"].squeeze()

eu_filtered = df[(df["age"] == "Y18-24") & (df["rskpovth"] == "TOTAL") & (df[r"geo\TIME_PERIOD"] == "EU27_2020") & (df["sex"] == "T")]
eu_overburden_series = eu_filtered.loc[:, "2010":"2025"].squeeze()

plt.plot(hu_overburden_series.index, hu_overburden_series.values, label="Hungary")
plt.plot(eu_overburden_series.index, eu_overburden_series.values, label="EU average")
plt.xlabel("Year")
plt.xticks(["2010", "2015", "2020", "2025"])
plt.ylabel("Housing cost overburden rate (%)")
plt.title("Hungarian youth housing cost overburden vs. EU average 2010-2025")
plt.legend()
plt.savefig("housing_cost_overburden/hu_vs_eu_housing_cost_overburden.png")
