from hora.horoscope.chart import charts
from hora import const, utils
from hora.panchanga import drik

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

place = drik.Place(place_name, latitude, longitude, timezone)
drik.set_ayanamsa_mode(const._DEFAULT_AYANAMSA_MODE)

jd = utils.julian_day_number(dob, tob)
planet_positions = charts.rasi_chart(jd, place)

# Print Rasi Chart Output
for item in planet_positions:
    planet, (raasi, planet_longitude) = item
    print(f"{planet}: Raasi {raasi} {planet_longitude} degrees")
    break  # Only printing the first planet's information
