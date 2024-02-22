import sys
import json

print("Starting make sequence...")

if len(sys.argv) != 5:
    print("Invalid number of arguments")
    print("Usage: python make.py <path_prefix> <connection_string> <migrations_folder> <name>")
    sys.exit(1)

path_prefix = sys.argv[1]

connection_string = sys.argv[2]

migrations_folder = sys.argv[3]

name = sys.argv[4]

path_depth = "../" * (len(path_prefix.split("/")))

with open(f'./{path_depth}{migrations_folder}/journal.json', 'r') as f:
    journal = json.loads(f.read())

n_migration = len(journal)

with open(f'./{path_depth}{migrations_folder}/{n_migration:04d}{name}.sql', 'w') as f:
    f.write(f'-- {name}\n\n')

with open(f'./{path_depth}{migrations_folder}/journal.json', 'w') as f:
    journal.append(f'{n_migration:04d}{name}.sql')
    f.write(json.dumps(journal))

print(f'Created migration {n_migration:04d}{name}.sql')
