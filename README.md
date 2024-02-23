# Postgres Util

Set of simple utilities for *my* nuxt + postgres projects.

## Pre-requisites
[Python3](https://www.python.org/downloads/) && [Poetry](https://python-poetry.org/) && [Node.js](https://nodejs.org/en/)

## Installation

```bash
    # In your nuxt project
    git submodule add <this-repo> <target-path>
    
    # Either
    cd <target-path>
    ./init .
    
    # Or
    ./<target-path>/init <target-path>
```

## Modules

### `generate`
- Creates typescript + zod schema notations from the database schema.

```bash
    # In your nuxt project
    ./<target-path>/generate <target-path> <db-connection-string> <schema-folder-name>
```

### `migrator`
- Creates migration files from the database schema.

```bash
    # Initialize first
    ./<target-path>/migrator init <target-path> <db-connection-string> <migrations-folder-name>
    # Creates init.sql and journal.json
    
    # Make new migration
    ./<target-path>/migrator make <target-path> <db-connection-string> <migrations-folder-name> <migration-name>
    # Creates a new migration file xxxx<migration-name>.sql
    # Updates journal.json
    
    # Apply migrations
    ./<target-path>/migrator execute <target-path> <db-connection-string> <migrations-folder-name>
```

### Notes
- I highly recommend creating your own `generate` and `migrator` scripts at the project level so you don't always need to type down all the parameters that (besides new migrations name) are constant for each project.
- At this moment I'm not planing to develop the library for more than my own needs.