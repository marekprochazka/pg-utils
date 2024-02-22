import sys
from psycopg import connect
from psycopg.conninfo import conninfo_to_dict
import json

print("Starting execute sequence...")

if len(sys.argv) != 4:
    print("Invalid number of arguments")
    print("Usage: python execute.py <path_prefix> <connection_string> <migrations_folder>")
    sys.exit(1)

# init arguments
exec_prefix = sys.argv[1]
connection_string = sys.argv[2]
migrations_folder = sys.argv[3]

path_depth = "../" * (len(exec_prefix.split("/")) - 1)

# read journal
with open(f'./{path_depth}{migrations_folder}/journal.json', 'r') as f:
    journal = json.loads(f.read())

print("Connecting to database...")
# connect to database
connection_dict = conninfo_to_dict(connection_string)
connection = connect(**connection_dict)
cursor = connection.cursor()

print("Collecting migrations...")

# get last migration
try:
    cursor.execute("""
    SELECT id from migrations order by created_at desc limit 1;
    """)
    last_migration = cursor.fetchone()[0]
except:
    print("Error while fetching last migration")
    cursor.close()
    connection.close()
    sys.exit(1)

last_committed_migration_index = journal.index(f'{last_migration}.sql')

# execute pending migrations
for migration in journal[last_committed_migration_index + 1:]:
    print(f'Executing {migration}...')
    with open(f'./{path_depth}{migrations_folder}/{migration}') as f:
        cursor.execute(f.read())

    cursor.execute("""
    INSERT INTO migrations (id) VALUES (%s);
    """, (migration.split(".")[0],))
    connection.commit()

cursor.close()

connection.close()

print("All done, goodbye!")
