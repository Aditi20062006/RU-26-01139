# Bus Route Management System

A simple console-based Python program that stores a bus network and finds routes between bus stops.

## Features

- Show the direct connections of a bus stop
- Show all available stops
- Find a route with the fewest stops using BFS
- Calculate the total distance
- Calculate the fare at Rs. 1.50 per km

## Bus Network

The program uses the following roads:

- Durg - Bhilai: 10 km
- Bhilai - Raipur: 30 km
- Durg - Raipur: 40 km
- Raipur - Bilaspur: 110 km
- Raipur - Dhamtari: 80 km
- Durg - Rajnandgaon: 45 km
- Jagdalpur - Kondagaon: 75 km

All roads work in both directions.

## Requirements

- Python 3
- No external libraries are required

## How to Run

1. Save the project as `main.py`.
2. Open a terminal in the project folder.
3. Run:

```bash
python main.py
```

## Menu Options

1. Show connections
2. Find route
3. Show all stops
4. Exit

## Example

Finding a route from Bhilai to Bilaspur:

```text
Route: Bhilai -> Raipur -> Bilaspur
Stops: 3 | Distance: 140 km | Fare: Rs. 210.00
```

## Concepts Used

- Dictionaries
- Lists
- Functions
- BFS (Breadth-First Search)
