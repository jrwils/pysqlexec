# pysqlexec #
### PostreSQL at the Python prompt ###

`pysqlexec` is a functional way to communicate with a PostgreSQL database through Python. It uses the [psycopg2](http://initd.org/psycopg/) adapter. 

### Setup ###

Enter your database credentials in the `dbs` dictionary located in `dbconfig.py`. For example:

    dbs = {'default':
       {'dbname': 'mydb',
        'dbuser': 'myuser',
        'dbpass': 'mypass',
        'dbhost': 'myhost',
        'dbport': 'myport'}}

More than one database can be added to the `dbs` dictionary. The `default` database will be used if `database` is not passed as a keyword argument in the function. For example, the following query would connect to the `default` database:

    data = sqlexec("select * from mytable limit 1")

While this query would connect to the `other` database (provided it was defined in `dbs`):

    data = sqlexec("select * from mytable limit 1", database="other")

### Usage Examples ###

    from pysqlexec.sqlexec import sqlexec

    # Pass query parameters with string formatting

    data = sqlexec("select * from people where firstname = %s", ("John",))

    # Insertions

    sqlexec("insert into states ('stateshort', 'statelong') values (%s, %s)", ('CA', 'California',))

For full documentation on passing parameters to queries, see the [psycopg2 documentation](http://initd.org/psycopg/docs/usage.html#passing-parameters-to-sql-queries)

### Written and tested with ###

Python 3.4

PostgreSQL 9.4


