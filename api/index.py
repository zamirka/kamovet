import os
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kamovet.settings')

from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()
