= Gr8 Designs Madlibs =
Author: Andrew Berry
Email: andrewberry@sentex.net
http://www.abdevelopment.ca/

This Django module is used to teach about the basics of Python. Topics covered
in session include methods, string concatenation, and dictionaries, though those
terms are rarely used in session. By the end of 90 minutes, participants will be
able to run their own Python Madlibs, both in the console and in the Django
environment. This allows them to create their own Madlibs, and put them "on the
web" to share with their peers.

For more information about Gr8 Designs for Gr8 Girls, see:
http://www.gr8-designs.ca/

= Requirements =

To use the web frontend, Django is required. For best use with a lab of
participants, Apache and mod_wsgi are recommended. These are easily installed on
most Linux distributions.

The session could be run without Django, though I imagine it would be less
interesting for most of the participants.

The client machines are best run with Linux or some other Unix. Contrary to my
expectations, two years of participants are just fine adapting to Linux with no
prior experience :)

= Runtime Notes =

* Use ./manage.py runserver 0.0.0.0:8000 to run a test server. Note that all
imported code shares the same memory space, so this isn't a good idea for
parallel access.

* Be sure to set SECRET_KEY in gr8girls/settings.py.

* Apache's mod_python stores compiled python files in memory, and they take a
while to expire.

* mod_wsgi doesn't have the issues of the built-in server and doesn't cache
code, so it's the best solution.

* Currently, the module is always reloaded with reload(), but it's unclear how
the various server implementations handle this call. mod_wsgi is the only one
tested in production.

* The directory paths to look for MyMadLibs.py are currently hardcoded to match
the University of Guelph systems. They will need to be changed or refactored to
work on your own setup. See gr8girls/models/views.py for more details.

* For simplicity, create your guest user accounts with a numbered suffix for easy
generation by the web application.

* The instructions on the Madlibs home page are for KDE 3.5 on Linux; modify or
make pluggable for your own system if it's different.

