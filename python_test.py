#problem 1: variables and Data Types 
print("=== Problem 1 ===")
market_name = "Balogun market"
num_traders = 5000
location_coords = (6.4541,3.3947)
is_open_sundays = False
print ("Market:", market_name)
print("Type:", type(market_name))
print("Traders:",num_traders)
print("Type:", type(num_traders))
print("Coordinates:",location_coords)
print("Type:", type(location_coords))
print("Open sundays:", is_open_sundays)
print("Type:", type(is_open_sundays))
total_market_revenue = 25000000 
avg_revenue_per_trader = total_market_revenue /num_traders
print("Average Daily Revenue per Trader:")
print(avg_revenue_per_trader)
print("===Problem 2 ===") 
host_countries = ["Ghana","Egypt","Nigeria","Senegal","Cameroon"]
host_countries.append("Ivory Coast") 
host_countries.insert(1,'Morocco')
host_countries.remove("Senegal")
print("Total numbers of countries")
print(len(host_countries))
print("Countries in alphabetical order:")
print(sorted(host_countries))
print("Every second country:")
print(host_countries[::2])
print("=== Problem 3 ===")
river_data ={} 
river_data["Nile"] = {"length_km":6650, "countries": 11}
river_data["Congo"] = {"length_km": 4700,"countries":9}
river_data["Niger"]={"length_km": 4180, "countries":5}
river_data["Zambezi"] = {"length_km": 2574, "countries":6}
river_data["Niger"]["countries"] =6
print("All river names:")
print(list(river_data.keys()))
print("Congo river countries:")
print(river_data["Congo"]["countries"])
nile_len = river_data["Nile"]["length_km"]
congo_len =river_data["Congo"]["length_km"]
niger_len =river_data["Niger"]["length_km"]
zambezi_len = river_data["Zambezi"]["length_km"]
total_length = nile_len + congo_len + niger_len + zambezi_len
print("Total combined length:")
print(total_length)
print("=== Problem 4: Part A ===")
print('Multplication table of 7:')
for i in range(1,11):
     print(7*i)
     print("Letters in AFRICA:")
for letters in "AFRICA":
     print(letters)
even_sum = 0
for num in range(1, 51):
    if num % 2 == 0:
        even_sum = even_sum + num
print("Sum of even numbers from 1 to 50:")
print(even_sum)
print("=== Problem 4: Part B ===")
print("Countdown from 20 to 1:")
count = 20
while count >= 1:
    print(count)
    count = count - 1
number = 501
while True:
    if number % 3 == 0 and number % 7 == 0:
        print("First number greater than 500 divisible by 3 and 7:")
        print(number)
        break
    number = number + 1
    print("=== Problem 5 ===")
    def classify_rainfall(mm):
        if mm > 300:
            return "Flood Risk"
        elif mm >= 200:
            return "Heavy Rain"
        elif mm >= 100:
            return "Moderate Rain"
        elif mm >= 1:
            return "Light Rain"
        else:
            return "Dry"
test_cases = [350, 250, 150, 50, 0]
for rain in test_cases:
    result = classify_rainfall(rain)
    print(rain, "mm:", result)
print("=== Problem 6 ===")
def calculate_exchange(amount, rate):
    return amount * rate
print(calculate_exchange(100, 1580))
def format_price(amount, currency="NGN"):
    return currency + " " + str(amount)
print(format_price(5000))
print(format_price(200, "GHS"))
def analyze_scores(scores): return min(scores), sum(scores) / len(scores)
score_list = [55, 72, 88, 61, 94, 47, 79]
print(analyze_scores(score_list))
print("=== Problem 7 ===")
proverb = "Slowly, slowly, catches the monkey, African African wisdom"
print(proverb.upper())
print(proverb.split(","))
print("wisdom" in proverb)
print(proverb.replace("African wisdom", "African proverb"))
print(proverb.lower().count("o"))
print("=== Problem 8 ===")
try:
    with open("crops.txt", "w") as file:
        file.write("Cocoa, Nigeria, 320000\nCoffee, Ethiopia, 480000\nCassava, Ghana, 210000\n")
except Exception as e:
    print("Error creating file:", e)
try:
    total_production = 0
    with open("crops.txt", "r") as file:
        for line in file:
            print(line.strip())
            parts = line.split(",")
            total_production += int(parts[2])
    print("Total Production:", total_production)
except FileNotFoundError:
    print("Error: The file crops.txt does not exist. ")
print("=== Problem 9 ===")
temperatures =[18, 23, 31, 27, 35, 19, 29, 33, 22, 28]
fahr_temps = [(c * 9/5) + 32 for c in temperatures]
print("Fahrenheit:", fahr_temps)
above_30 = [c for c in temperatures if c > 30]
print("Above 30C:", above_30)
between_20_29 = [c for c in temperatures if 20 <= c <= 29]
print("Between 20 and 29C:", between_20_29)
print("=== Problem 10 ===")
try:
    balance = float(input("Enter withdrawal amount: "))
    withdrawal = float(input("Enter withdrawal amount: "))
    if withdrawal > balance:
        print("Error: Insufficient funds! You cannot withdraw more than your balance.")
    else:
        remaining_balance = balance - withdrawal
        print("Remaining Balance:", remaining_balance)
except ValueError:
    print("Error: Invalid input! Please enter a valid number.")
finally:
    print("Transaction attempt completed")
