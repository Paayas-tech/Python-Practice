from abc import ABC, abstractmethod


# 1. Abstraction: Base blueprint enforcing method implementation in derived classes
class DatabaseService(ABC):
    @abstractmethod
    def connect(self) -> None:
        pass

    @abstractmethod
    def fetch_data(self, query: str) -> list:
        pass


# 2. Inheritance & Polymorphism: Subclass providing its own concrete behavior
class PostgresService(DatabaseService):
    def __init__(self, host: str, port: int):
        # 3. Encapsulation: Protected (_) and Private (__) attributes
        self.host = host
        self._port = port               # Convention: protected attribute
        self.__is_connected = False      # Name mangling: private attribute

    def connect(self) -> None:
        self.__is_connected = True
        print(f"Connected to PostgreSQL at {self.host}:{self._port}")

    def fetch_data(self, query: str) -> list:
        if not self.__is_connected:
            raise ConnectionError("Database connection is closed.")
        # Polymorphic return matching contract
        return [{"status": "success", "query": query}]


class MockDatabaseService(DatabaseService):
    def connect(self) -> None:
        print("Connected to in-memory mock database.")

    def fetch_data(self, query: str) -> list:
        return [{"mock_id": 1, "result": "sample"}]


# Polymorphic execution: treats any DatabaseService uniformly
def run_query(db: DatabaseService, query: str):
    db.connect()
    data = db.fetch_data(query)
    print("Query results:", data)


pg = PostgresService("localhost", 5432)
mock = MockDatabaseService()

run_query(pg, "SELECT * FROM users;")
run_query(mock, "SELECT 1;")

"""Custom math utility module inside a subfolder."""

def calculate_discount(price: float, rate: float) -> float:
    return price * (1 - rate)


def format_currency(amount: float) -> str:
    return f"${amount:,.2f}"