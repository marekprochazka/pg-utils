import sys
from pathlib import Path
from psycopg import connect
from psycopg.conninfo import conninfo_to_dict

print("Starting init sequence...")

if len(sys.argv) != 4:
    print("Invalid number of arguments")
    print("Usage: python init.py <path_prefix> <connection_string> <migrations_folder>")
    sys.exit(1)

path_prefix = sys.argv[1]

connection_string = sys.argv[2]

migrations_folder = sys.argv[3]

print("Creating migrations folder...")

Path(f'{migrations_folder}').mkdir(parents=True, exist_ok=True)

print("Creating init.sql...")

with open(f'{path_prefix}/init.sql', 'r') as source:
    with open(f'{migrations_folder}/init.sql', 'w') as target:
        target.write(source.read())

print("Creating journal.json...")

with open(f'{migrations_folder}/journal.json', 'w') as f:
    f.write('[\"init.sql\"]')

print("Connecting to database...")
connection_dict = conninfo_to_dict(connection_string)
connection = connect(**connection_dict)
cursor = connection.cursor()

print("Executing init.sql...")
with open(f'{migrations_folder}/init.sql') as f:
    cursor.execute(f.read())

connection.commit()
cursor.close()

connection.close()

print("All done, goodbye!")