Simple blog
===========

A simple blog, based on Django,
to share your posts in a good looking style.

usage
-----
1. for the first step you should clone this repository::

    git clone https://github.com/LiterallyTheOne/simple_blog.git


2. then make a file named ``manual_settings.py``
   at ``./simple_blog/`` to load your manual settings
   to overwrite the main settings.

3. install the requirements using the code bellow::

    pip install -r requirements.txt

4. migrate the data
   structure to your database using code bellow::

    python3 manage.py migrate

5. make a superuser using the code bellow::

    python3 manage.py createsuperuser

6. run your server, for example::

    python3 manage.py runserver


Add Posts and tags
------------------
To add new posts or Tags you can
connect with the superuser.
