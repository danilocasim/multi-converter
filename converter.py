from rich.console import Console
from rich.theme import Theme
from rich.table import Table
from rich.progress import track
import time

custom_theme = Theme({"success": "green", "error": "bold red", "blue": "bold blue", "underline_cyan": "underline cyan"})

console = Console(theme=custom_theme)

accounts = [
    {"email": "danilo.casim@cvsu.edu.ph", "password": "casim1"},
    {"email": "alessandra.herico@cvsu.edu.ph", "password": "herico1"},
    {"email": "aljon.vijungco@cvsu.edu.ph", "password": "vijunco1"},
    {"email": "mark.respicio@cvsu.edu.ph", "password": "respicio1"},
    {"email": "admin", "password": "password"}
]

def login(email, password):
    found_account = next(
        (account for account in accounts if account["email"] == email and account["password"] == password),
        None
    )

    if found_account:
        print("")
        for i in track(range(5), description="Logging In..."):
            time.sleep(0.5) 
        print("")
        console.print("\nLOGIN SUCCESSFULLY", style="bold green")
        print("")
        return True
    elif any(account["email"] == email for account in accounts):
        print("")
        console.print("Incorrect password. Please try again.", style="error")
        print("")
    else:
        print("")
        console.print("Account does not exist. Please create an account.", style="error")
        print("")

    return False

def create_account():
    print("")
    console.print("CREATE ACCOUNT", style="underline cyan")
    print("")
    first_name = input("Enter your first name: ").lower()
    print("")
    last_name = input("Enter your last name: ").lower()
    print("")
    created_email = f"{first_name}.{last_name}@cvsu.edu.ph"
    created_password = f"{last_name}1"
    new_account = {"email": created_email, "password": created_password}
    console.print("========================================",style="yellow")
    print("")
    for i in track(range(5), description="Generating..."):
        time.sleep(0.5) 
    print("")
    console.print("ACCOUNT GENERATED", style="bold green underline")
    print("")
    console.print(f"This is your email: [cyan]{created_email}[/cyan]")
    print("")
    console.print(f"This is your password: [cyan]{created_password}[/cyan]")
    print("")
    console.print("========================================", style="yellow")
    accounts.append(new_account)
    print("")
    console.print("ACCOUNT ADDED SUCCESSFULLY", style="bold green")
    print("")
    return {"email": created_email, "password": created_password}

def money_converter():
    def convert_currency(amount, from_currency, to_currency):
        exchange_rates = {
            "USD": 1,
            "EUR": 0.85,
            "JPY": 110,
            "PHP": 50.25,
            "CNY": 6.38,
            "THB": 31.15,
        }

        if from_currency not in exchange_rates or to_currency not in exchange_rates or not amount:
            print("Invalid input. Please provide a valid amount and currency codes.")
            return

        exchange_rate = exchange_rates[to_currency] / exchange_rates[from_currency]
        converted_amount = amount * exchange_rate

        console.print(f"{amount} {from_currency} is approximately {converted_amount:.2f} {to_currency}.", style="bold green")

    table = Table()
    table.add_column("MONEY CONVERTER", style="magenta", justify="center")
    table.add_row("USD")
    table.add_row("EUR")
    table.add_row("JPY")
    table.add_row("PHP")
    table.add_row("CNY")
    table.add_row("THB")
    console = Console()
    console.print(table)
    print("")
    from_currency = input("Enter the source currency code: ").upper()
    print("")
    amount = float(input("Enter the amount: "))
    print("")
    to_currency = input("Enter the target currency code: ").upper()
    print("")
    console.print("========================================", style="yellow")

    if amount and from_currency.strip() and to_currency.strip():
        convert_currency(amount, from_currency, to_currency)
    else:
        print("Invalid input. Please provide a valid amount and currency codes")

def length_converter():
    def mm_to_cm(mm):
        return mm / 10

    def cm_to_mm(cm):
        return cm * 10

    def cm_to_m(cm):
        return cm / 100

    def m_to_cm(m):
        return m * 100

    def km_to_m(km):
        return km * 1000

    def m_to_km(m):
        return m / 1000

    def inch_to_cm(inch):
        return inch * 2.54

    def cm_to_inch(cm):
        return cm / 2.54

    def convert_length(value, from_unit, to_unit):
        units = {"mm": 1, "cm": 2, "m": 3, "km": 4, "inch": 5}

        value_mm = value * 10 ** units[from_unit]
        converted_value_mm = value * 10 ** units[to_unit]

        result = {
            to_unit: value_mm / 10 ** units[to_unit],
            from_unit: converted_value_mm / 10 ** units[from_unit],
        }

        return result
    
    console.print("========================================", style="yellow")
    print("")
    console.print("Length Converter", style="bold green underline")
    print("")
    console.print("Available units: mm, cm, m, km, inch", style="magenta")
    print("")
    value = float(input("Enter the length value: "))
    print("")
    from_unit = input("Enter the unit to convert from: ").lower()
    print("")
    to_unit = input("Enter the unit to convert to: ").lower()
    print("")
    result = convert_length(value, from_unit, to_unit)
    console.print("========================================", style="yellow")
    print("")
    console.print(f"{value} {from_unit} is equal to {result[to_unit]} {to_unit}", style="bold green")
    print("")
    console.print(f"{value} {to_unit} is equal to {result[from_unit]} {from_unit}", style="bold green")
    print("")
def temperature_converter():
    console = Console()

    def fahrenheit_to_celsius(f):
        return (f - 32) * 5 / 9

    def celsius_to_fahrenheit(c):
        return (c * 9 / 5) + 32

    def celsius_to_kelvin(c):
        return c + 273.15

    def kelvin_to_celsius(k):
        return k - 273.15

    def fahrenheit_to_kelvin(f):
        c = fahrenheit_to_celsius(f)
        return celsius_to_kelvin(c)

    def kelvin_to_fahrenheit(k):
        c = kelvin_to_celsius(k)
        return celsius_to_fahrenheit(c)

    console.print("========================================", style="yellow")
    print("")
    
    table = Table()
    table.add_column("Temperature Converter", style="magenta")
    table.add_row("1. Fahrenheit to Celsius")
    table.add_row("2. Celsius to Fahrenheit")
    table.add_row("3. Celsius to Kelvin")
    table.add_row("4. Kelvin to Celsius")
    table.add_row("5. Fahrenheit to Kelvin")
    table.add_row("6. Kelvin to Fahrenheit")

    console.print(table)
    print("") 

    choice = int(input("Enter your choice (1-6): "))
    print("")
    console.print("========================================", style="yellow")
    print("")
    
    if 1 <= choice <= 6:
        temperature = float(input("Enter the temperature: "))
        print("")
        if choice == 1:
            result = fahrenheit_to_celsius(temperature)
            console.print(f"{temperature} Fahrenheit is {result:.2f} Celsius.", style="bold green")
            print("")
        elif choice == 2:
            result = celsius_to_fahrenheit(temperature)
            console.print(f"{temperature} Celsius is {result:.2f} Fahrenheit.", style="bold green")
            print("")
        elif choice == 3:
            result = celsius_to_kelvin(temperature)
            console.print(f"{temperature} Celsius is {result:.2f} Kelvin.", style="bold green")
            print("")
        elif choice == 4:
            result = kelvin_to_celsius(temperature)
            console.print(f"{temperature} Kelvin is {result:.2f} Celsius.", style="bold green")
            print("")
        elif choice == 5:
            result = fahrenheit_to_kelvin(temperature)
            console.print(f"{temperature} Fahrenheit is {result:.2f} Kelvin.", style="bold green")
            print("")
        elif choice == 6:
            result = kelvin_to_fahrenheit(temperature)
            console.print(f"{temperature} Kelvin is {result:.2f} Fahrenheit.", style="bold green")
            print("")
    else:
        console.print("Invalid choice. Please enter a number between 1 and 6.", style="error")
        print("")


def weight_converter():
    def mg_to_g(mg):
        return mg / 1000

    def g_to_mg(g):
        return g * 1000

    def g_to_kg(g):
        return g / 1000

    def kg_to_g(kg):
        return kg * 1000

    def mg_to_kg(mg):
        return mg / 1000000

    def kg_to_mg(kg):
        return kg * 1000000

    def convert_weight(value, from_unit, to_unit):
        units = {"mg": 1, "g": 2, "kg": 3}

        value_mg = value * 10 ** units[from_unit]
        converted_value_mg = value * 10 ** units[to_unit]

        result = {
            to_unit: value_mg / 10 ** units[to_unit],
            from_unit: converted_value_mg / 10 ** units[from_unit],
        }

        return result
    
    console.print("========================================", style="yellow")
    print("")
    console.print("Weight Converter", style="bold green underline")
    print("")
    console.print("Available units: mg, g, kg", style="magenta")
    print("")
    value = float(input("Enter the weight value: "))
    print("")
    from_unit = input("Enter the unit to convert from: ").lower()
    print("")
    to_unit = input("Enter the unit to convert to: ").lower()
    print("")

    result = convert_weight(value, from_unit, to_unit)
    
    console.print("========================================", style="yellow")
    print("")
    console.print(f"{value} {from_unit} is equal to {result[to_unit]} {to_unit}", style="bold green")
    print("")
    console.print(f"{value} {to_unit} is equal to {result[from_unit]} {from_unit}", style="bold green")
    print("")

def main_menu():
    console = Console()

    console.print("========================================", style="yellow")
    print("")

    table = Table()
    table.add_column("CONVERTER", style="magenta", justify="left")
    table.add_row("1. MONEY CONVERTER")
    table.add_row("2. LENGTH CONVERTER")
    table.add_row("3. TEMPERATURE CONVERTER")
    table.add_row("4. WEIGHT CONVERTER")
    table.add_row("5. EXIT")

    console.print(table)
    print("")
    console.print("========================================", style="yellow")


logged_in = False

while True:
    console.print("========================================", style="yellow")
    print("")
    print("1. LOGIN")
    print("2. CREATE ACCOUNT")
    print("3. EXIT")
    print("")
    login_choice = float(input("Enter your choice (1/2/3): "))
    print("")
    console.print("========================================", style="yellow")


    if login_choice == 1:
        print("")
        email = input("Email: ").lower()
        print("")
        password = input("Password: ").lower()
        logged_in = login(email, password)
    elif login_choice == 2:
        created_account = create_account()
        if created_account:
            for i in track(range(5), description="Redirecting..."):
                time.sleep(0.5) 
            print("")
            print("REDIRECTED TO LOGIN......")
            logged_in = login(created_account["email"], created_account["password"])
    elif login_choice == 3:
        print("")
        for i in track(range(5), description="Closing..."):
            time.sleep(0.5) 
        print("")
        print("Exiting the program. Goodbye!")
        print("")
        console.print("========================================", style="yellow")
        break

    if logged_in:
        while True:
            main_menu()
            print("")
            feature_choices = float(input("Enter your choice (1/2/3/4/5): "))
            print("")
            if feature_choices == 5:
                for i in track(range(5), description="Closing..."):
                    time.sleep(0.5) 
                print("")
                print("Exiting to the main menu.")
                print("")
                break

            if 1 <= feature_choices <= 4:
                if feature_choices == 1:
                    print("")
                    for i in track(range(5), description="Redirecting..."):
                        time.sleep(0.5) 
                    print("")
                    print("Redirected to MONEY CONVERTER")
                    print("")
                    money_converter()
                elif feature_choices == 2:
                    print("")
                    for i in track(range(5), description="Redirecting..."):
                        time.sleep(0.5) 
                    print("")
                    print("Redirected to LENGTH CONVERTER")
                    print("")
                    length_converter()
                elif feature_choices == 3:
                    print("")
                    for i in track(range(5), description="Redirecting..."):
                        time.sleep(0.5) 
                    print("")
                    print("Redirected to TEMPERATURE CONVERTER")
                    print("")
                    temperature_converter()
                elif feature_choices == 4:
                    print("")
                    for i in track(range(5), description="Redirecting..."):
                        time.sleep(0.5) 
                    print("")
                    print("Redirected to WEIGHT CONVERTER")
                    print("")
                    weight_converter()
            else:
                print("")
                print("Invalid choice. Please enter a number between 1 and 5.")
