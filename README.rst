
ExperimentDB
============

The experimentDB is a web-based application for the storage, organization and communication of experimental data with a focus on molecular biology and biochemical data. This application also stores data regarding reagents, including antibodies, constructs and other biomolecules as well as tracks the distribution of reagents. There is also some preliminary interfaces to other web resources.

Current Build and Testing Status
---------------------------------

.. image:: https://travis-ci.org/BridgesLab/ExperimentDB.png?branch=master   
    :target: https://travis-ci.org/BridgesLab/mousedb

.. image:: https://coveralls.io/repos/BridgesLab/ExperimentDB/badge.png?branch=master
    :target: https://coveralls.io/r/BridgesLab/mousedb

This project contains several sub-applications as described below:

Data
----
This package defines experiments and the related data associated with them. The Experiment model is the focus of this entire project. It contains details about protocols, notes, reagents and project details. Results are associated with Experiment objects allowing for an Experiment to contain several results.

Projects
--------
The intent of this app is to co-ordinate specific projects.  Projects are intended to be large, grant-sized larger projects in the laboratory.  Subprojects are intended to be smaller,  potentially paper sized groups of experiments.  An experiment can be part of one, none or several projects or subprojects.

Cloning
-------
The cloning app defines the parameters for the synthesis and maintenance of constructs generated as part of an experiment.  Constructs can be generated via either cloning or mutagenesis and will result in a Cloning or Mutagenesis object respectively.

Proteins
--------
The proteins referenced by this application may be targets of an experiment or reagent.  This app also contains more detailed information about specific proteins, normally as accessed from public databases using either external databases or through Biopython tools.

Reagents
--------
The reagents app stores information about all tools used in research, most of which are defined by a particular Experiment object.  These include Primer, Cell (cell lines), Antibody, Strain, Chemical and Construct objects.  These models are abstract base classes of a superclass ReagentInfo which defines most of the common relevant information.

External
--------
The idea is to attribute particular models with references regarding external contacts or vendors or to link in specific references important to the experiments or projects.

Datasets
--------
The datasets app contains data and views for some external databases.  This may include external databases accessed directly or with a mirrored internal database.  This module is fairly research-interest specific and will likely be removed eventually.


ExperimentDB Installation
=========================

Configuration
-------------
ExperimentDB requires both a database and a webserver to be set up.  Ideally, the database should be hosted separately from the webserver and ExperimentDB installation, but this is not necessary, as both can be used from the same server.  If you are using a remote server for the database, it is best to set up a user for this database that can only be accessed from the webserver.  If you want to set up several installations (ie for different users or different laboratories), you need separate databases and ExperimentDB installations for each.  You will also need to set up the webserver with different addresses for each installation.

Software Dependencies
---------------------
1. **ExperimentDB source code**.  Download from one of the following:  

  a. http://github.com/davebridges/ExperimentDB/downloads for the current release
  b. http://github.com/davebridges/ExperimentDB for the source code
  c. from pypi by entering::

      pip install experimentdb

Downloading and/or unzipping will create a directory named ExperimentDB.  You can update to the newest revision at any time either using git or downloading and re-installing the newer version.  Changing or updating software versions will not alter any saved data, but you will have to update the localsettings.py file (described below).

2. **Python**.  Requires Version 2.6, is not yet compatible with Python 3.0.  Download from Python_.
3. **Django**.  Download from Django_.  This will be automatically installed if you installed experimentdb with pip.  This will be automatically installed if you installed experimentdb with pip.  The current version supported is Django 1.4
4. **Database software**.  Typically MySQL is used, but PostgreSQL, Oracle or SQLite can also be used.  You also need to install the python driver for this database (unless you are using SQLite, which is internal to Python 2.5+).  For more information see Instructions_.
5. **Python Dependencies** These can be automatically installed using pip with the following command from the root directory::

    pip install -r requirements.txt

.. _Python: http://www.python.org/download
.. _Django: http://www.djangoproject.com/download/
.. _Instructions: http://docs.djangoproject.com/en/dev/topics/install/database-installation

Database Setup
--------------
1. Create a new database.  You need to record the user, password, host and database name.  Refer to the database documentation for how to do this with a specific database engine.  If you are using SQLite3, you only need to set the engine and the database name.  It is recommended to use PostgreSQL.
2. Go to experimentdb/localsettings_empty.py and edit the ADMINS and TIME_ZONE settings.  Change the secret key to a random sequence of letters.  Depending on your webserver you may also want to set the MEDIA_URL, LOGIN_URL and STATIC_URL settings::

    ENGINE: 'django.db.backends.sqlite3', #  Choose one of 'django.db.backends.postgresql_psycopg2','django.db.backends.postgresql', 'django.db.backends.mysql', 'django.db.backends.sqlite3', 'django.db.backends.oracle' depending on the database software used.
    NAME: database name
    USER: database user.  Unless using sqlite3
    PASSWORD: database password.  Unless using sqlite3
    HOST: database host.

3. Save this file as localsettings.py in the experimentdb directory.
4. Run the test client by going into the main directory and running the following.  There should be no errors at this point::

    python manage.py test
    
6. ExperimentDB upgrades may involve schema changes.  We use south to control schema migrations.  To update database schema, first initial migrations must be run, shortly after installation.  If an upgrade (either via SVN or by a new download) involves a change in the database schema, errors may occur.  Look at HISTORY in the root folder to see if an upgrade invovles schema migrations.  To set up south, shortly after installation enter at the command line::

    python manage.py syncdb
    python manage.py schemamigration data --initial
    python manage.py schemamigration datasets --initial
    python manage.py schemamigration reagents --initial
    python manage.py schemamigration cloning --initial	
    python manage.py schemamigration sharing --initial
    python manage.py schemamigration projects --initial
    python manage.py schemamigration external --initial	
    python manage.py schemamigration proteins --initial
    python manage.py schemamigration hypotheses --initial    
	 
7. Generate the initial database tables then move the static files to the STATIC_ROOT by entering::

    python manage.py migrate --fake
    python manage.py collectstatic

8. When asked, generate an administrative superuser and set the email and password.

Web Server Setup
----------------
You need to set up a server to serve both the django installation and saved files.  Ideally a separate webserver would be set up to serve both the /static and /media files.  Although if it is easier you can use apache for both.  You can serve media and static files from any location on your server, just indicate this by setting STATIC_ROOT and MEDIA_ROOT in localsettings.  You can also choose to serve from a different url (rather than /media or /static) by changing the MEDIA_URL or STATIC_URL respectively.
The preferred setup for the django files is to use Apache2 with mod\_wsgi.  The following is a httpd.conf example where the code is placed in /usr/src/django/ExperimentDB::
    
    #this is for static files (css, images and javascript)
    Alias /static /usr/src/django/ExperimentDB/experimentdb/static
    <Directory /usr/src/django/ExperimentDB/experimentdb/static>
        Order allow,deny
        Allow from all
    </Directory>
    
    #this is for media files (user uploaded files)
    Alias /media /usr/src/django/ExperimentDB/experimentdb/media
    <Directory /usr/src/django/ExperimentDB/experimentdb/media>
        Order allow,deny
        Allow from all
    </Directory>

    #this is for the base code serving
    WSGIScriptAlias /experimentdb /usr/src/django/ExperimentDB/apache/django.wsgi
    <Directory /usr/src/django/ExperimentDB/apache>
        Order deny,allow
        Allow from all
    </Directory>

If you want to restrict access to these files, change the Allow from all directive to specific domains or ip addresses (for example Allow from 192.168.0.0/99 would allow from 192.168.0.0 to 192.168.0.99)

Final Configuration and User Setup
----------------------------------
Go to experimentdb/admin/auth/users/ and create users, selecting usernames, full names, password (or have the user set the password) and then choose group permissions.

Future Schema Changes
---------------------
	
If an app is migrated during an upgrade enter the following where "APP" is data, datasets, reagents, cloning, sharing, projects, external, proteins or hypotheses without the quotes and the "OPTIONAL DESCRIPTION" is something describing the changes, if desired::

    python manage.py schemamigration "APP" "OPTIONAL DESCRIPTION" --auto
    python manage.py migrate

See the South documentation, or submit an issue if problems occur.	
