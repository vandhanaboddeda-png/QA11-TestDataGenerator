from faker import Faker
from validator import validate_record
import yaml
import random
import json
import pandas as pd

fake = Faker()

# Read schema file
with open("schemas/customer.yaml", "r") as file:
    schema = yaml.safe_load(file)

rows = schema["rows"]

data = []

for i in range(1, rows + 1):

    while True:

        record = {
            "customer_id": i,
            "name": fake.name(),
            "age": random.randint(
                schema["columns"]["age"]["min"],
                schema["columns"]["age"]["max"]
            ),
            "email": fake.user_name() + "@gmail.com"
        }

        if validate_record(record):
            data.append(record)
            break

# Save JSON file
with open("outputs/generated_data.json", "w") as outfile:
    json.dump(data, outfile, indent=4)

print("JSON file generated successfully!")

# Save CSV file
df = pd.DataFrame(data)
df.to_csv("outputs/generated_data.csv", index=False)

print("CSV file generated successfully!")

# Save SQL file
with open("outputs/generated_data.sql", "w") as sql_file:

    for record in data:

        query = f"""
INSERT INTO customers
(customer_id, name, age, email)
VALUES
({record['customer_id']},
'{record['name']}',
{record['age']},
'{record['email']}');
"""

        sql_file.write(query)

print("SQL file generated successfully!")