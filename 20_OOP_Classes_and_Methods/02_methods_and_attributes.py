class Developer:
    # 1. Class Attribute: shared across all instances
    organization = "DevCorp"
    total_developers = 0

    def __init__(self, name, role):
        # Instance attributes: unique per object
        self.name = name
        self.role = role
        Developer.total_developers += 1

    # 2. Instance Method: accepts 'self' to access/modify instance state
    def get_details(self):
        return f"{self.name} works as a {self.role} at {self.organization}"

    # 3. Class Method: accepts 'cls' to access/modify class state
    @classmethod
    def get_total_count(cls):
        return f"Total developers registered: {cls.total_developers}"

    # 4. Static Method: utility function; does not access self or cls
    @staticmethod
    def is_valid_role(role_name):
        valid_roles = {"Frontend", "Backend", "Fullstack", "DevOps"}
        return role_name in valid_roles


# Utilizing instance methods
dev1 = Developer("Paayas", "Backend")
dev2 = Developer("Aarav", "Fullstack")
print(dev1.get_details())
print(dev2.get_details())

# Accessing class attributes and class methods
print(Developer.get_total_count())

# Utilizing static methods
print("Is 'Backend' valid?", Developer.is_valid_role("Backend"))
print("Is 'Manager' valid?", Developer.is_valid_role("Manager"))