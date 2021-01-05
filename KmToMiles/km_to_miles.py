# create programme to convert distance in kilometers to miles
# distance_km= 564.5
# 1 km = 0.621371 miles

# constant value for conversion
km_mile_const = 0.621371
# Get distance input from user for conversion
dist_km= input("Enter Distance In KM : ")
# Convert to miles
dist_miles = km_mile_const * int(dist_km)
# Print Calculated Distance
print("Converted Distance In Miles : ", dist_miles)
