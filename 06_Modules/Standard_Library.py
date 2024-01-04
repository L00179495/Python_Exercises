from datetime import datetime, date, time, timedelta

# Get the current date and time
current_datetime = datetime.now()
print("Current Date and Time:", current_datetime)

# Access individual components of the date and time
current_date = current_datetime.date()
current_time = current_datetime.time()

print("Current Date:", current_date)
print("Current Time:", current_time)

# Create a specific date
specific_date = date(2022, 12, 31)
print("Specific Date:", specific_date)

# Create a specific time
specific_time = time(14, 30)
print("Specific Time:", specific_time)

# Combine a date and time to create a datetime object
combined_datetime = datetime.combine(specific_date, specific_time)
print("Combined Datetime:", combined_datetime)

# Perform arithmetic operations on dates
future_date = specific_date + timedelta(days=10)
print("Future Date:", future_date)

# Format a datetime object as a string
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Datetime:", formatted_datetime)

# Parse a string to create a datetime object
parsed_datetime = datetime.strptime("2022-01-15 08:30:00", "%Y-%m-%d %H:%M:%S")
print("Parsed Datetime:", parsed_datetime)
