def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temp_c = float(input("Digite a temperatura em Celsius: "))

print(f"{temp_c}°C em Fahrenheit é: {celsius_para_fahrenheit(temp_c)}°F")
