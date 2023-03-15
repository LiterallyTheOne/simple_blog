Simple blog
===========

A simple blog, based on Django,
to share your posts in a good looking style.

I use this code for my weblog,
https://raminzarebidoky.pythonanywhere.com

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


Files that you have to change
-----------------------------


+---------------------------------------------------+--------------------------------+
| File                                              | action                         |
+===================================================+================================+
| main_blog/templates/main_blog/about_me.html       | Put your own information there |
+---------------------------------------------------+--------------------------------+
| main_blog/templates/main_blog/index.html          | Title and meta information     |
+---------------------------------------------------+--------------------------------+
| main_blog/templates/main_blog/post_view.html      | Meta information               |
+---------------------------------------------------+--------------------------------+
| main_blog/templates/main_blog/r_footer.html       | Put your own information there |
+---------------------------------------------------+--------------------------------+
| main_blog/templates/main_blog/r_header.html       | Put your own information there |
+---------------------------------------------------+--------------------------------+
| main_blog/templates/main_blog/tag_view.html       | Meta information               |
+---------------------------------------------------+--------------------------------+
| main_blog/templates/main_blog/about_me.html       | Put your own information there |
+---------------------------------------------------+--------------------------------+
| main_blog/static/main_blog/icons/*                | Put your own icons             |
+---------------------------------------------------+--------------------------------+
| main_blog/static/main_blog/manifest/manifest.json | Put your own information there |
+---------------------------------------------------+--------------------------------+

Add Posts and Tags
------------------
To add new posts or tags you can
connect with the superuser.
