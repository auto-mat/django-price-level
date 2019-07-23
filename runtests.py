import sys

try:
    import django.conf
    from django.test.utils import get_runner
    from model_utils import Choices

    settings = django.conf.settings
    settings.configure(
        DEBUG=True,
        USE_TZ=True,
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
            }
        },
        INSTALLED_APPS=[
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sites",
            "price_level",
            "tests",
        ],
        SITE_ID=1,
        MIDDLEWARE=(
            'author.middlewares.AuthorDefaultBackendMiddleware',
        ),
        PRICE_LEVEL_MODEL='tests.PriceableModel',
        PRICE_LEVEL_CATEGORY_CHOICES=Choices(('basic', 'Basic'), ('company', 'For companies')),
        PRICE_LEVEL_CATEGORY_DEFAULT='basic',
    )

    try:
        import django
        setup = django.setup
    except AttributeError:
        pass
    else:
        setup()

except ImportError:
    import traceback
    traceback.print_exc()
    msg = "To fix this error, run: pip install -r requirements_test.txt"
    raise ImportError(msg)


def run_tests(*test_args):
    if not test_args:
        test_args = ['tests']

    # Run tests
    TestRunner = get_runner(settings)
    test_runner = TestRunner()

    failures = test_runner.run_tests(test_args)

    if failures:
        sys.exit(bool(failures))


if __name__ == '__main__':
    run_tests(*sys.argv[1:])
