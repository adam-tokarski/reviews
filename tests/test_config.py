import os

from decouple import Csv, config

from app import config as application_config


def test_repository_configuration():
    os.environ[
        "REPOSITORY_CONFIGURATION"
    ] = "apoclyps/code-review-manager, apoclyps/my-dev-space, apoclyps/magic-home"

    application_config.REPOSITORY_CONFIGURATION = config(
        "REPOSITORY_CONFIGURATION",
        cast=Csv(),
    )
    configuration = application_config.get_configuration()

    assert configuration == [
        ("apoclyps", "code-review-manager"),
        ("apoclyps", "my-dev-space"),
        ("apoclyps", "magic-home"),
    ]