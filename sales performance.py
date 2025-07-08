print("sales performance analyser")

daily_sales = [10,85,34,56,150,22,46]
days = ["mon,tue,wed,thur,fri sat,sun"]
average_sales = sum(daily_sales)/ 7
total_sales = sum(daily_sales)
print(total_sales," products have been sold")
if total_sales==403:
 print("each product has a cost of 20 $ ")
 total_revenue = total_sales * 20
 print("sum = ", total_sales,  "* 20 $ = ", total_revenue, " $")
 average_revenueperday = total_revenue / 7
 print("averaage_revenue per day = total_revenue / 7= ", average_revenueperday, "$")
 total_revenue_per_year = 365 * average_revenueperday
 print("365 * average_revenueperday = total_revenue_per_year = ", total_revenue_per_year,"$" )