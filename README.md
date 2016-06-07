Python 那些事儿 (三)


Try to deploy a flask demo app 

this is the app structure:

```
.
├── flaskdemo1
│   ├── flaskr.py
│   ├── flaskr_tests.py
│   ├── __init__.py
│   ├── README
│   ├── schema.sql
│   ├── static
│   │   └── style.css
│   └── templates
│       ├── layout.html
│       ├── login.html
│       └── show_entries.html
└── flaskdemo1.wsgi

```

so the file `flaskdemp1.wsgi` is the entry point for this app.
let us check what says in this script file:

```
#!/home/matt/env1/bin/python2.7
import sys
import os
import site
import logging
logging.basicConfig(stream=sys.stderr)

site.addsitedir('~/env1/lib/python2.7/site-packages')
sys.path.insert(0,"/var/www/flaskdemo1/")
# above lines they just prepare the environments.

# this line is to load flaskr app as a entrypoint
from flaskdemo1.flaskr import app as application
```

```
.
├── flaskdemo1
│   ├── flaskr.py
│   ├── flaskr_tests.py
│   ├── __init__.py
│   ├── README
│   ├── schema.sql
│   ├── static
│   │   └── style.css
│   └── templates
│       ├── layout.html
│       ├── login.html
│       └── show_entries.html
```

here, this is a complete flask app, firstly let add a `__init__.py` file to make this folder as a module. so that we can load this app as a module in the `wsgi` file:

```
from flaskdemo1.flaskr import app as application
```


