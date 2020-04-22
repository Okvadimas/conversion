def conversion():
    jedak = "." * 55  # contoh menggunakan variable

    def jeda():  # contoh menggunakan function
        titik = "." * 55
        print(titik)

    print("Welcome to World Conversion")
    print(jedak)
    print("type help for more information")
    jeda()
    while 1 != 2:  # 
        pilih = input("Konversi Celcius/Reamur/Kelvin/Fahrenheit ? ").lower()
        try:
            if pilih == "celcius":
                celcius_input = float(input("Input Temperature in Celsius : "))
                celcius_fahrenheit = celcius_input * 9 / 5 + 32
                celcius_reamur = celcius_input * 4 / 5
                celcius_kelvin = celcius_input * 5 / 5 + 273.15
                print(f"""
Temperature in Fahrenheit  = {celcius_fahrenheit}
Temperature in Reamur      = {celcius_reamur}
Temperature in Kelvin      = {celcius_kelvin}
                    """)
            elif pilih == "reamur":
                reamur_input = float(input("Input Temperature in Reamur : "))
                reamur_fahrenheit = reamur_input * 9 / 4 + 32
                reamur_celcius = reamur_input * 5 / 4
                reamur_kelvin = reamur_input * 5 / 5 + 273.15
                print(f"""
Temperature in Fahrenheit  = {reamur_fahrenheit}
Temperature in Celcius     = {reamur_celcius}
Temperature in Kelvin      =  {reamur_kelvin}
                    """)
            elif pilih == "fahrenheit":
                fahrenheit_input = float(input("Input Temperature in Fahrenheit : "))
                fahrenheit_celcius = (fahrenheit_input - 32) * 5 / 9
                fahrenheit_reamur = (fahrenheit_input - 32) * 4 / 9
                fahrenheit_kelvin = (fahrenheit_input - 32) * 5 / 9 + 273.15
                print(f"""
Temperature in Celcius     = {fahrenheit_celcius}
Temperature in Reamur      = {fahrenheit_reamur}
Temperature in Kelvin      = {fahrenheit_kelvin}
                    """)
            elif pilih == "kelvin":
                kelvin_input = float(input("Input Temperature in Kelvin : "))
                kelvin_celcius = (kelvin_input - 273.15) * 5 / 5
                kelvin_reamur = (kelvin_input - 273.15) * 4 / 5
                kelvin_fahrenheit = (kelvin_input - 273.15) * 9 / 5 + 32
                print(f"""
Temperature in Celcius     = {kelvin_celcius} 
Temperature in Reamur      = {kelvin_reamur}
Temperature in Fahrenheit  = {kelvin_fahrenheit}
                    """)
            elif pilih == "help":
                print("""
            To Start Conversion Choose One and type on the List !
            To Quit type exit !
                    """)
            elif pilih == "exit":
                print("Thanks for using World Conversion")
                break
            else:
                print("Something went wrong, type help for more information")
        except ValueError:
            print("Something Went Wrong, You should type number value")

conversion()
