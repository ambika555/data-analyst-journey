# 3. Install an external module and use it to perform an operation of your interest
# NOTE: Do NOT run shell commands like `pip install` inside a .py file.
# Install packages from your terminal/PowerShell (examples below).

from faker import Faker

fake = Faker()
print( fake.name() , fake.address())
