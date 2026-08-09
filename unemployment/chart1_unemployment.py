"""
Chart 1: youth vs total unemployment in Hungary.
Dataset: une_rt_a (Eurostat annual unemployment by age).
"""

import eurostat
import matplotlib.pyplot as plt

df = eurostat.get_data_df("une_rt_a")

youth_unemployment = df[(df[r"geo\TIME_PERIOD"] == "HU") & (df["age"] == "Y15-24")]
all_unemployment = df[(df[r"geo\TIME_PERIOD"] == "HU") & (df["age"] == "Y15-74")]

total_youth_unemployment = youth_unemployment[(youth_unemployment["sex"] == "T") & (youth_unemployment["unit"] == "PC_ACT")]
total_all_unemployment = all_unemployment[(all_unemployment["sex"] == "T") & (all_unemployment["unit"] == "PC_ACT")]

total_youth_unemployment = total_youth_unemployment.loc[:, "2009":"2025"]
total_all_unemployment = total_all_unemployment.loc[:, "2009":"2025"]

youth_ue_series = total_youth_unemployment.squeeze()
all_ue_series = total_all_unemployment.squeeze()

plt.plot(youth_ue_series.index, youth_ue_series.values, label="Ages 15-24")
plt.plot(all_ue_series.index, all_ue_series.values, label="Ages 15-74")
plt.xlabel("Year")
plt.xticks(["2010", "2015", "2020", "2025"])
plt.ylabel("Unemployment rate")
plt.title("Hungarian youth unemployment vs. overall unemployment 2009-2025")
plt.legend()
plt.savefig("unemployment/youth_vs_all_unemployment.png")
