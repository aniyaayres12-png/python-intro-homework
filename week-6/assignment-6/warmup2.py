def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32 

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

c1, c2, f1 = 0, 100, 72

print(f"{c1}°C = {round(celsius_to_fahrenheit(c1), 1)}°F")
print(f"{c2}°C = {round(celsius_to_fahrenheit(c2), 1)}°F")
print(f"{f1}°F = {round(fahrenheit_to_celsius(f1), 1)}°C")

