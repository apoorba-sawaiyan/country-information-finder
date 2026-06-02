import requests


def get_country_data(country):

    url = f"https://restcountries.com/v3.1/name/{country}"

    try:
        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()[0]

            name = data["name"]["common"]

            capital = data.get("capital", ["N/A"])[0]

            population = data["population"]

            currency = list(data.get("currencies", {}).keys())[0]

            flag = data["flags"]["png"]

            return {
                "name": name,
                "capital": capital,
                "population": population,
                "currency": currency,
                "flag": flag
            }

        else:
            return None

    except Exception as e:
        print("Error:", e)
        return None


def save_history(country_data):

    with open("country_history.txt", "a", encoding="utf-8") as file:

        file.write(
            f"{country_data['name']} | "
            f"{country_data['capital']} | "
            f"{country_data['population']} | "
            f"{country_data['currency']}\n"
        )


def search_country():

    country = input("\nEnter country name: ")

    data = get_country_data(country)

    if data:

        print("\n===== COUNTRY INFORMATION =====")

        print("Country:", data["name"])
        print("Capital:", data["capital"])
        print("Population:", data["population"])
        print("Currency:", data["currency"])
        print("Flag URL:", data["flag"])

        save_history(data)

    else:

        print("Country not found.")


def compare_countries():

    country1 = input("\nEnter first country: ")
    country2 = input("Enter second country: ")

    c1 = get_country_data(country1)
    c2 = get_country_data(country2)

    if c1 and c2:

        print("\n===== COUNTRY COMPARISON =====")

        print(f"\n{c1['name']}")
        print("Capital:", c1["capital"])
        print("Population:", c1["population"])
        print("Currency:", c1["currency"])

        print(f"\n{c2['name']}")
        print("Capital:", c2["capital"])
        print("Population:", c2["population"])
        print("Currency:", c2["currency"])

        if c1["population"] > c2["population"]:

            print(
                f"\n{c1['name']} has a larger population."
            )

        elif c2["population"] > c1["population"]:

            print(
                f"\n{c2['name']} has a larger population."
            )

        else:

            print("\nBoth countries have equal population.")

    else:

        print("One or both countries not found.")


def view_history():

    try:

        with open(
            "country_history.txt",
            "r",
            encoding="utf-8"
        ) as file:

            print("\n===== SEARCH HISTORY =====\n")

            print(file.read())

    except FileNotFoundError:

        print("No search history found.")


while True:

    print("\n========== COUNTRY INFORMATION FINDER ==========")
    print("1. Search Country")
    print("2. Compare Countries")
    print("3. View Search History")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        search_country()

    elif choice == "2":

        compare_countries()

    elif choice == "3":

        view_history()

    elif choice == "4":

        print("Thank you for using Country Information Finder.")
        break

    else:

        print("Invalid choice. Please try again.")