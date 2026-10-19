def initialize_system():
    print("[System] Core services initialized successfully.")


def compute_metrics(val: int) -> int:
    return val * 10


# __name__ is set to "__main__" ONLY when this file is executed directly.
# If imported as a module elsewhere, __name__ equals "03_name_and_main".
if __name__ == "__main__":
    print(f"Running script directly. __name__ is: '{__name__}'")
    initialize_system()
    sample_val = compute_metrics(5)
    print("Calculated test metric:", sample_val)
else:
    print(f"Module imported into another file. __name__ is: '{__name__}'")