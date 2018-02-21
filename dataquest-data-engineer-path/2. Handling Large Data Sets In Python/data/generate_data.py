from faker import Faker
import csv
import random
from datetime import datetime

HEADERS = ["name", "address", "previous_address", "gender", "ssn", "birthdate", "job", "phone"]
LINES = 2400
ZIP_RANGE = list(range(90001, 96162, 1))

def generate_line():
    fake = Faker()
    profile = fake.profile()
    name = profile["name"].replace(",", " ")
    address = "{} {} CA {}".format(fake.street_address(), fake.city(), random.choice(ZIP_RANGE))
    previous_address = profile["residence"].replace("\n", " ").replace(",", " ")
    gender = profile["sex"]
    ssn = profile["ssn"]
    birthdate = fake.date_time_between_dates(datetime_start=datetime(1920,1,1), datetime_end=datetime(1997,1,1), tzinfo=None)
    job = profile["job"].replace(",", "")
    phone = fake.phone_number()
    
    return [name, address, previous_address, gender, ssn, birthdate, job, phone]
    
if __name__ == "__main__":
    all_lines = [HEADERS]
    for i in range(LINES):
        line = generate_line()
        all_lines.append(line)
    
    with open('applications.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(all_lines)