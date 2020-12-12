#dashboard.wsgi
import sys
sys.path.insert(0, '/var/www/html/development-dashboard-server')

from dashboard import app as application
