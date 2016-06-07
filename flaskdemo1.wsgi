#!/home/matt/env1/bin/python2.7
import sys
import os 
import site
site.addsitedir('/home/matt/env1/lib/python2.7/site-packages')

import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/flaskdemo1/")

#activate_this = '/home/matt/env1/bin/activate_this.py'
#execfile(activate_this, dict(__file__=activate_this))


#from flask import Flask
from flaskdemo1.flaskr import app as application
#application.secret_key = 'xxoo'
