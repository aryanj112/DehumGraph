def relToAbs(temp,relHum):
    # Initial variables
    temp = temp  # Measured in Fahrenheit
    relHum = relHum  # Relative humidity
    Rw = 461.5   # Specific gas constant for water vapor (J/(kg·K))

    # Convert temperature from Fahrenheit to Celsius and Kelvin
    temp_celsius = (temp - 32) * 5 / 9
    temp_kelvin = temp_celsius + 273.15

    # Calculate saturation vapor pressure (satuVap) using Clausius–Clapeyron equation
    satuVap = 6.11 * 10 ** ((7.5 * temp_celsius) / (237.3 + temp_celsius))  # Saturation vapor pressure in mb
    satuVap_pa = satuVap * 100 # Convert saturation vapor pressure from millibar to Pascal

    # Calculate absolute humidity (absHum)
    absHum = (relHum * satuVap_pa) / (Rw * temp_kelvin * 100)
    absHum_g = absHum * 1000 # Convert abs hum from kg/m^3 to g/m^3 
    return absHum_g

print(relToAbs(40,40))