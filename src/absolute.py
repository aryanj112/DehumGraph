# Initial variables
temp = 20  # Measured in Fahrenheit
relHum = 10  # Relative humidity
Rw = 461.5   # Specific gas constant for water vapor (J/(kg·K))

# Convert temperature from Fahrenheit to Celsius and Kelvin
temp_celsius = (temp - 32) * 5 / 9
temp_kelvin = temp_celsius + 273.15
print(f"Temp in Celsius: {temp_celsius:.2f}")
print(f"Temp in Kelvin: {temp_kelvin:.2f}")

# Calculate saturation vapor pressure (satuVap) using Clausius–Clapeyron equation
satuVap = 6.11 * 10 ** ((7.5 * temp_celsius) / (237.3 + temp_celsius))  # Saturation vapor pressure in mb

# Convert saturation vapor pressure from millibar to Pascal
satuVap_pa = satuVap * 100
print(f"Saturation Vapor Pressure: {satuVap_pa:.2f} Pa")

# Calculate absolute humidity (absHum)
absHum = (relHum * satuVap_pa) / (Rw * temp_kelvin * 100)
print(f"Absolute Humidity: {absHum:.6f} kg/m^3")