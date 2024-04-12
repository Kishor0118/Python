from hora import const, utils
from hora.panchanga import drik
from hora.panchanga import drik1

# Take user input for date of birth
dob_input = input("Enter date of birth (YYYY-MM-DD): ")
year, month, day = map(int, dob_input.split('-'))
dob = drik.Date(year, month, day)

# Take user input for time of birth
tob_input = input("Enter time of birth (HH:MM:SS): ")
hours, minutes, seconds = map(int, tob_input.split(':'))
tob = (hours, minutes, seconds)

# Take user input for place details
place_name = input("Enter place name: ")
latitude = float(input("Enter latitude (decimal degrees): "))
longitude = float(input("Enter longitude (decimal degrees): "))
timezone = float(input("Enter timezone offset (e.g., +5.5 for IST): "))

drik.set_ayanamsa_mode(const._DEFAULT_AYANAMSA_MODE)
dob = drik.Date(1996, 12, 7)
tob = (10, 34, 0)
place = drik.Place('Chennai,IN', 13.0389, 80.2619, +5.5)
jd = utils.julian_day_number(dob, tob)

# Call the sree_lagna function
sree_lagna_constellation, sree_lagna_longitude = drik1.sree_lagna(jd, place)

# Print the Sree Lagna output
print(f"Sree Lagna Constellation: {sree_lagna_constellation}")
print(f"Sree Lagna Longitude: {sree_lagna_longitude}")
