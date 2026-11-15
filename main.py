bus_network = {
    "Durg": {
        "Bhilai": 10,
        "Raipur": 40,
        "Rajnandgaon": 45
    },
    "Bhilai": {
        "Durg": 10,
        "Raipur": 30
    },
    "Raipur": {
        "Bhilai": 30,
        "Durg": 40,
        "Bilaspur": 110,
        "Dhamtari": 80
    },
    "Bilaspur": {
        "Raipur": 110
    },
    "Dhamtari": {
        "Raipur": 80
    },
    "Rajnandgaon": {
        "Durg": 45
    },
    "Jagdalpur": {
        "Kondagaon": 75
    },
    "Kondagaon": {
        "Jagdalpur": 75
    }
}

FARE_PER_KM = 1.50


def show_connections():
    stop = input("Enter stop: ").title()

    if stop not in bus_network:
        print(f"Stop {stop} not found.")
        return

    print(f"{stop} connects to:")

    for neighbour, distance in bus_network[stop].items():
        print(f"{neighbour} ({distance} km)")


def find_route():
    start = input("From: ").title()
    destination = input("To: ").title()

    if start not in bus_network:
        print(f"Stop {start} not found.")
        return

    if destination not in bus_network:
        print(f"Stop {destination} not found.")
        return

    if start == destination:
        print("Source and destination are the same. Distance: 0 km")
        print("Fare: Rs. 0.00")
        return

    queue = [[start]]
    visited = [start]

    route = None

    while len(queue) > 0:
        current_route = queue.pop(0)
        current_stop = current_route[-1]

        if current_stop == destination:
            route = current_route
            break

        for neighbour in bus_network[current_stop]:
            if neighbour not in visited:
                visited.append(neighbour)
                new_route = current_route + [neighbour]
                queue.append(new_route)

    if route is None:
        print(f"No route available between {start} and {destination}.")
        return

    distance = 0

    for i in range(len(route) - 1):
        distance += bus_network[route[i]][route[i + 1]]

    fare = distance * FARE_PER_KM

    print("Route:", " -> ".join(route))
    print(f"Stops: {len(route)} | Distance: {distance} km | Fare: Rs. {fare:.2f}")


def show_all_stops():
    print("Stops:")

    for stop in bus_network:
        print(stop)


def main():
    while True:
        print("\n--- Bus Route Management System ---")
        print("1. Show connections")
        print("2. Find route")
        print("3. Show all stops")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_connections()
        elif choice == "2":
            find_route()
        elif choice == "3":
            show_all_stops()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


main()
