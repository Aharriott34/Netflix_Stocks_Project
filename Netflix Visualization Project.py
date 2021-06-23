from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd

pd.set_option("display.max_columns", 10)
netflix_stocks = pd.read_csv("NFLX.csv")
dowjones_stocks = pd.read_csv("DJI.csv")
netflix_quarterly_stocks = pd.read_csv("NFLX_daily_by_quarter.csv")

# 2017 is represented in the dataframes. "DJI" and "NFLX" is represented by months and "NFLX_daily_by_quarter" is represented by days. "DJI" and "NFLX" are the averages per month. "NFLX_daily_by_quarter" are the highs and lows of each business day. "netflix_stocks_quarterly" has a Quarter column, whereas "netflix_stocks"  does not have that column.

netflix_stocks.rename(columns={"Adj Close": "Price"},inplace=True)
netflix_quarterly_stocks.rename(columns={"Adj Close": "Price"},inplace=True)
dowjones_stocks.rename(columns={"Adj Close": "Price"},inplace=True)
print(netflix_quarterly_stocks.head(5))

# Violinplot to visualize Netflix's quarterly data.
ax = sns.violinplot(data=netflix_quarterly_stocks, x="Quarter", y="Price")
sns.set_palette("Set2")
sns.set_style("darkgrid")
ax.set_title("Distribution of 2017 Netflix Stock Prices by Quarter")
ax.set_yticks(range(100, 220, 20))
ax.set_yticklabels(["$100", "$120", "$140", "$160", "$180", "$200"])
ax.set_xlabel("Business Quarters in 2017")
ax.set_ylabel("Closing Stock Price (USD)")
plt.savefig("Distribution of 2017 Netflix Stock Prices by Quarter.png")
plt.show()
# In the violinplot, most of the ranges in the plot fell around $140-$155. The highest price was around 210, and the lowest price was 131

# Visualizing Earnings Per Share in 2017 using Yahoos estimated earnings compared to their actual earnings.
x_positions = [1, 2, 3, 4]
chart_labels = ["1Q2017","2Q2017","3Q2017","4Q2017"]
earnings_actual =[.4, .15,.29,.41]
earnings_estimate = [.37,.15,.32,.41 ]

plt.clf()
plt.scatter(x_positions, earnings_actual, color="red", alpha=0.5)
plt.scatter(x_positions, earnings_estimate, color="blue", alpha=0.5)
plt.legend(["Actual", "Estimate"])
plt.xticks(x_positions, chart_labels)
plt.xlabel("Business Quarters")
plt.ylabel("Cents (USD)")
plt.title("Netflix: Earnings Per Share in Cents")
plt.savefig("Netflix: Earnings and Revenue Reports.png")
plt.show()
# The estimated earnings were either on par with the actual earning, or slightly off with the actual earnings.

# Visualizing Netflix's revenue and earnings.
# Units are in billions of dollars
revenue_by_quarter = [2.79, 2.98,3.29,3.7]
earnings_by_quarter = [.0656,.12959,.18552,.29012]
quarter_labels = ["2Q2017","3Q2017","4Q2017", "1Q2018"]

# Revenue
n = 1  # This is our first dataset (out of 2)
t = 2 # Number of dataset
d = 4 # Number of sets of bars
w = 0.5 # Width of each bar
bars1_x = [t*element + w*n for element
             in range(d)]

# Earnings
n = 2  # This is our second dataset (out of 2)
t = 2 # Number of dataset
d = 4 # Number of sets of bars
w = 0.5 # Width of each bar
bars2_x = [t*element + w*n for element
             in range(d)]

middle_x = [ (a + b) / 2.0 for a, b in zip(bars1_x, bars2_x)]
labels = ["Revenue", "Earnings"]

plt.clf()
plt.bar(bars1_x, revenue_by_quarter)
plt.bar(bars2_x, earnings_by_quarter)
plt.xticks(middle_x, quarter_labels)
plt.xlabel("Business Quarters")
plt.ylabel("Billions of Dollars (USD)")
plt.legend(labels)
plt.title("Netflix: Earnings and Revenue Reports")
plt.savefig("Netflix: Earnings and Revenue Reports.png")
plt.show()
#  "Revenue" and "Earnings" both had a small increase every quarter. Both "Revenue" and "Earnings" followed an upward trend.

# Visualizing Netflix and Dow Jones stocks over the 2017 fiscal year.
month_label = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

plt.clf()
ax1 = plt.subplot(121)
plt.suptitle("Netflix vs. Dow Jones in 2017")
net_x_axis = netflix_stocks["Date"]
net_y_axis = netflix_stocks["Price"]
ax1.set_title("Netflix")
ax1.set_xticks(range(len(net_y_axis)))
ax1.set_xticklabels(month_label)
ax1.set_xlabel("Months")
ax1.set_ylabel("Stock Price (USD)")
ax1.plot(net_x_axis, net_y_axis, marker="o")
plt.subplots_adjust(wspace=.5)
plt.xticks(rotation=90)

ax2= plt.subplot(122)
dow_x_axis = dowjones_stocks["Date"]
dow_y_axis = dowjones_stocks["Price"]
ax2.set_title("Dow Jones")
ax2.set_xticks(range(len(dow_y_axis)))
ax2.set_xticklabels(month_label)
ax2.set_xlabel("Months")
ax2.set_ylabel("Stock Price (USD)")
ax2.plot(dow_x_axis, dow_y_axis, marker="o")
plt.subplots_adjust(wspace=0.5)
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("Netflix vs. Dow Jones in 2017.png")
plt.show()
