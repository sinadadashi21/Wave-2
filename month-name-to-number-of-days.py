month = input("Enter the name of the month: ")
days_in_month = 31

if month == "April" or month == "June" or month == "September" or month == "November":
    days_in_month = 30
elif month == "February":
    days_in_month = "28 or 29"

print(month, "has", days_in_month, "days in it.")

