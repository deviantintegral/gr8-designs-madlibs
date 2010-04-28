= Runtime Notes =

- Use ./manage.py runserver 0.0.0.0:8000 to run a test server. Note that all imported code shares the same memory space, so this isn't a good idea for parallel access.

- Apache's mod_python stores compiled python files in memory, and they take a while to expire.

- mod_wsgi doesn't have the issues of the built-in server and doesn't cache code, so it's the best solution.

