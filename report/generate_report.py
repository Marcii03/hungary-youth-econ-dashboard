"""
Combines the three charts into a single HTML report (report.html).
"""

html = """
<!DOCTYPE html>
<html>
<head>
<title>The Reality of the Hungarian Youth's Economic Position</title>
</head>
<body>
<h1>The reality of the Hungarian youth's economic position</h1>
<p>This report looks at what the Hungarian economy currently looks like for young people, using public data from Eurostat.
It covers youth unemployment, house prices versus youth income, and housing cost overburden, comparing Hungary to the wider EU where relevant.</p>
<p>Note: if the charts below don't appear, this is a known Safari limitation with local files, not a broken report - try opening this page in Chrome or Firefox instead.</p>
<img src="../unemployment/youth_vs_all_unemployment.png" alt="Chart comparing Hungarian unemployment rates for ages 15-24 and ages 15-74, from 2009 to 2025">
<p>Caption: [To be written after doing research]</p>
<img src="../house_prices/house_prices_vs_youth_income.png" alt="Chart comparing indexed Hungarian house prices and youth income (ages 18-24), from 2007 to 2025">
<p>Caption: [To be written after doing research]</p>
<img src="../housing_cost_overburden/hu_vs_eu_housing_cost_overburden.png" alt="Chart comparing housing cost overburden rates between Hungarian and EU youth (ages 18-24), from 2010 to 2025">
<p>Caption: [To be written after doing research]</p>
</body>
</html>
"""
with open("report/report.html", "w") as file:
    file.write(html)
