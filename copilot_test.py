from dataclasses import dataclass
from datetime import datetime


@dataclass
class Person:
    name: str
    family_name: str
    birth: datetime

    def age_in_years(self):
        return (datetime.now() - self.birth).days / 365

    @property
    def full_name(self):
        return f"{self.name} {self.family_name}"


query_users_by_last_name = """
SELECT name, family_name, birth
FROM users
WHERE family_name = :family_name
"""


def save_json(url, filename):
    import requests
    import json

    response = requests.get(url)
    response.raise_for_status()
    with open(filename, "w") as f:
        json.dump(response.json(), f, indent=2)
