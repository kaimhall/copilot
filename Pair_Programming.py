# import perosn class from other module
from copilot_test import Person


employees = [
    Person("John", "Doe", datetime(1990, 1, 1)),
    Person("Jane", "Doe", datetime(1995, 1, 1)),
    Person("John", "Smith", datetime(1990, 1, 1)),
    Person("Jane", "Smith", datetime(1995, 1, 1)),
]


def test_should_not_be_able_to_set_full_name():
    with pytest.raises(AttributeError):
        employees[0].full_name = "John Doe"
