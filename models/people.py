from . import people_container


def add_people_to_database(people):
  for line in people.splitlines():
    print(f'Adding: {line}')
    attributes = line.split()
    if len(attributes) < 2:
      continue
    first_name = attributes[1]
    last_name = attributes[0]
    person = {
      'id': f'{first_name} {last_name}',
      'firstName': first_name,
      'lastName': last_name
    }
    for attribute in attributes[2:]:
      key_and_value = attribute.split('=', 1)
      if len(key_and_value) < 2:
        continue
      key = key_and_value[0]
      value = key_and_value[1]
      if key in person:
        continue
      person[key] = value
    people_container.upsert_item(person)


def clear_database():
  return 404
