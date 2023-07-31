# Notes

- This project was designed to work just with the version 4.6.2 of PhpMyAdmin.
- It was maded just for users who don't have access to the server of a database, but can interact with it using PhpMyAdmin (it's the only case of use of this code).

# How to use it

Just set some env. vars in your server:

```
PMA_USER="superuser"
PMA_PASS="secretpass"
DOMAIN="http://myphpmyadmin.com"
FILES="./my_backups"
TABLES="table1,table2,table3"
```

# How it works

First, it makes an HTTP request to login into the server (for get a token and cookies), after that it does another HTTP request to export the tables that you want (it generate an sql file).
