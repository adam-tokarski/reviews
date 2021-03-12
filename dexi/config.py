from pathlib import Path
from typing import List, Tuple

from decouple import Csv, config

# Github Config
GITHUB_TOKEN = config("GITHUB_TOKEN")
DEFAULT_PAGE_SIZE = config("DEFAULT_PAGE_SIZE", cast=int, default=100)

# Database Config
DATA_PATH = config("DATA_PATH", cast=str, default=f"{str(Path.home())}/.dexi")
FILENAME = config("FILENAME", cast=str, default="dexi.db")

# Application Config
ENABLE_NOTIFICATIONS = config("ENABLE_NOTIFICATIONS", cast=bool, default=False)
REPOSITORY_CONFIGURATION = config(
    "REPOSITORY_CONFIGURATION",
    cast=Csv(),
    default="slicelife/ros-service, slicelife/delivery-service, slicelife/pos-integration, slicelife/candidate-code-challenges, apoclyps/dexi, apoclyps/micropython-by-example",
)


def get_configuration() -> List[Tuple[str, str]]:
    """converts a comma seperated list of organizations/repositories into a list of tuples."""

    def to_tuple(values):
        return (values[0], values[1])

    return [
        to_tuple(values=configuration.split(sep="/", maxsplit=1))
        for configuration in REPOSITORY_CONFIGURATION
    ]
