import random

class SeatMatrixAgent:
    def __init__(self, rows=10, cols=4):
        self.rows = rows
        self.cols = cols
        self.seats = [['O' for _ in range(cols)] for _ in range(rows)]

    def is_available(self, row, col):
        return self.seats[row][col] == 'O'

    def book_seat(self, row, col):
        if self.is_available(row, col):
            self.seats[row][col] = 'X'
            return True
        return False

    def display(self):
        print("\nSeat Matrix:")
        for idx, row in enumerate(self.seats):
            print(f"Row {idx+1}: {' '.join(row)}")

    def get_available_seats(self):
        return [(r, c) for r in range(self.rows) for c in range(self.cols) if self.is_available(r, c)]

class RequestAgent:
    def __init__(self, name, num_passengers):
        self.name = name
        self.num_passengers = num_passengers

    def create_request(self):
        print(f"\n{self.name} requests {self.num_passengers} seat(s)")
        return self.num_passengers

class AllocatorAgent:
    def __init__(self, seat_matrix_agent):
        self.matrix = seat_matrix_agent

    def allocate_seats(self, num_seats):
        available = self.matrix.get_available_seats()
        if len(available) < num_seats:
            return []

        for row in range(self.matrix.rows):
            contiguous = []
            for col in range(self.matrix.cols):
                if self.matrix.is_available(row, col):
                    contiguous.append((row, col))
                    if len(contiguous) == num_seats:
                        return contiguous
                else:
                    contiguous = []
        return available[:num_seats]

    def book_seats(self, seat_list):
        for row, col in seat_list:
            self.matrix.book_seat(row, col)

def simulate_bus_allocation():
    bus = SeatMatrixAgent()
    allocator = AllocatorAgent(bus)

    requests = [
        RequestAgent("Alice", 1),
        RequestAgent("Bob", 2),
        RequestAgent("Family Group", 3),
        RequestAgent("Charlie", 1),
    ]

    for agent in requests:
        num = agent.create_request()
        seats = allocator.allocate_seats(num)
        if seats:
            allocator.book_seats(seats)
            print(f"Seats booked for {agent.name}: {seats}")
        else:
            print(f"Could not book seats for {agent.name} (insufficient space)")
        bus.display()

simulate_bus_allocation()
