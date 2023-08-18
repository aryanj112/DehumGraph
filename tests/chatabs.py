import math

def calculate_absolute_humidity(temperature, relative_humidity):
    T = temperature
    RH = relative_humidity
    
    absolute_humidity = (6.112 * math.exp(17.67 * T / (T + 243.5)) * RH * 2.1674) / (273.15 + T)
    
    return absolute_humidity

def main():
    try:
        temperature = float(input("Enter temperature in Celsius: "))
        relative_humidity = float(input("Enter relative humidity in percentage: "))
        
        absolute_humidity = calculate_absolute_humidity(temperature, relative_humidity)
        
        print(f"Absolute Humidity: {absolute_humidity:.2f} g/m³")
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")

if __name__ == "__main__":
    main()
