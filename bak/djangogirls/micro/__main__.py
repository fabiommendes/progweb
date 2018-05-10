import click
import os


def setup_settings_module(mod, app):
    mod.INSTALLED_APPS.insert(0, app)


def runserver():
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(['manage.py', 'runserver'])


@click.command()
@click.option('--run', help='web application')
def main(run):
    """Management commands for the micro-framework"""

    from micro import settings

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'micro.settings')
    setup_settings_module(settings, run)
    
    runserver()

if __name__ == '__main__':
    main()