## PostgresSQL - First steps

### Create user 'apartify_api_py_admin'

```sql
CREATE USER apartify_api_py_admin WITH PASSWORD 'apartify_api_py_admin';
```

### Optimizations database

```sql
ALTER ROLE apartify_api_py SET client_encoding TO 'utf8';
ALTER ROLE apartify_api_py SET default_transaction_isolation TO 'read committed';
ALTER ROLE apartify_api_py SET timezone TO 'UTC';
```

### Create database 'apartify_api_py'

```sql
CREATE DATABASE apartify_api_py WITH ENCODING='UTF8';
```

### Grant to user

```sql
GRANT ALL PRIVILEGES ON DATABASE apartify_api_py TO apartify_api_py_admin;
```

{"mode":"full","isActive":false}

### PostgresSQL - Drop steps

###### Drop grant by user

```sql
REVOKE ALL PRIVILEGES ON DATABASE apartify_api_py FROM apartify_api_py_admin;
```

###### Drop user 'apartify_api_py_admin'

```sql
DROP USER apartify_api_py_admin;
```

### Drop database 'apartify_api_py'

```sql
DROP DATABASE apartify_api_py;
```