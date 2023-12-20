import math

def cal_dewPnt(temp, relHum):
    temp = temp  # Measured in Fahrenheit
    relHum = relHum  # Relative humidity
    a = 17.625 #smth
    b = 243.04 #smtj

    # Convert temperature from Fahrenheit to Celsius and Kelvin
    temp_celsius = (temp - 32) * 5 / 9

    # Calculate numerator
    numer = b * (math.log(relHum/100) + (a * temp_celsius/ (b + temp_celsius)))

    # Calculate demoninator
    denom = a - math.log(relHum/100) - (a * temp_celsius/ (b + temp_celsius))

    # Calculate absolute humidity (absHum)
    dewPnt = numer/denom
    dewPnt = (dewPnt * 9 / 5) + 32 # Convert dewPnt from Celsius to Fahrenheit 
    return dewPnt

if __name__ == '__main__':
    try:
        temp = float(input("Enter Temperature in F: "))
        relHum = float(input("Enter Relative Humidity: "))
        print(f"Dewpoint (F): {cal_dewPnt(temp,relHum):.2f} F")
    except ValueError:
        print("Invalid input. Please enter a valid number.")