import os
import sys
import traceback

print("cwd:", os.getcwd())
print("python:", sys.executable)
print("before files:", sorted(os.listdir('.')))

try:
    from django.core import management
    print("django imported, version:", __import__('django').get_version())
    management.call_command('startproject', 'RiffMates', '.')
    print("startproject completed")
    print("after files:", sorted(os.listdir('.')))
except Exception:
    print("Exception during startproject:")
    traceback.print_exc()
    sys.exit(1)
