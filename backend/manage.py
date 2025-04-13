# manage.py
import os
import sys
import dotenv # Import dotenv

def main():
    """Run administrative tasks."""
    # Load .env file ----> ADD THIS BLOCK <----
    try:
        print("Attempting to load .env file...") # DEBUG PRINT
        loaded = dotenv.load_dotenv()
        print(f".env file loaded: {loaded}") # DEBUG PRINT (Should be True if file found)
    except ImportError:
        print(".env load skipped: dotenv not installed?") # DEBUG PRINT
        pass
    # ----> END OF BLOCK <----

    # ----> ADD THESE DEBUG PRINTS <----
    print(f"DEBUG: DB_HOST from env = {os.environ.get('DB_HOST')}")
    print(f"DEBUG: DB_PORT from env = {os.environ.get('DB_PORT')}")
    print(f"DEBUG: DB_NAME from env = {os.environ.get('DB_NAME')}")
    print(f"DEBUG: DB_USER from env = {os.environ.get('DB_USER')}")
    print(f"DEBUG: DB_PASSWORD from env = {'<set>' if os.environ.get('DB_PASSWORD') else '<not set>'}") # Don't print the actual password
    # ----> END DEBUG PRINTS <----

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'productBackendCore.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()