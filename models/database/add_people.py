from typing import Any

from . import container


def add_people(people: str) -> None:
  """
  Adds people to the database.
  :param people: A string representing the people to add.
  """
  # Split the people into individual people (1 person per line).
  # Upsert each person to the database.
  for line in people.splitlines():
    attributes = line.split()
    # If the person doesn't have both a first and last name, ignore them.
    if len(attributes) < 2:
      continue
    # Create the person with their name and add their attributes.
    person = create_basic_person(attributes)
    for attribute in attributes[2:]:
      add_attribute(person, attribute)
    # Upsert the person (after printing a logging message).
    print(f'\tUpserting {person["id"]}')
    container.upsert_item(person)


def create_basic_person(attributes: list[str]) -> dict[str, Any]:
  """
  Creates a person with just the basic attributes (id, firstName, and lastName).
  :param attributes: The attributes that make up a person.
  :return: A dictionary representing a person.
  """
  first_name = attributes[1]
  last_name = attributes[0]
  person = {
    'id': f'{first_name} {last_name}',
    'firstName': first_name,
    'lastName': last_name
  }
  return person


def add_attribute(person: dict[str, Any], attribute: str) -> bool:
  """
  Adds an attribute to the person.
  :param person: The person to add the attribute to.
  :param attribute: The attribute to add to the person.
  :returns: True if the attribute was added, False if it was not.
  """
  key_and_value = attribute.split('=', 1)
  # If the attribute does not contain an '=', ignore it.
  if len(key_and_value) < 2:
    return False
  key = key_and_value[0]
  value = key_and_value[1]
  # If this attribute is a duplicate, ignore it.
  if key in person:
    return False
  # Convert the value of the attribute if possible.
  person[key] = to_implicit_type(value)
  return True


def to_implicit_type(string: str) -> str | int | float:
  """
  Converts the string to an int or float if it can.
  :param string: The string that may represent a string, int, or float.
  :returns: The converted string.
  """
  # Convert it an int if possible.
  try:
    return int(string)
  except ValueError:
    pass
  # Convert it a float if possible.
  try:
    return float(string)
  except ValueError:
    pass
  # Both conversions failed, keep it as a string.
  return string
