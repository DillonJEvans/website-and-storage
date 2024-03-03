from typing import Any, Dict, Iterable, List, Tuple

from . import container


def query_people(attributes: Dict[str, str]) -> Iterable[Dict[str, Any]]:
  """
  Queries the database for people with the matching name(s).
  :param attributes: The attributes to query for.
  :returns: A list of people that matches the query.
  """
  # Create the query.
  query, parameters = create_query(attributes)
  limit = get_limit(attributes, 20)
  query += f' OFFSET 0 LIMIT {limit}'
  # Query the database (after printing a logging message).
  print(f'\tQuerying {query}')
  people = container.query_items(
    query=query,
    parameters=parameters,
    enable_cross_partition_query=True
  )
  # Return the results (after sanitizing them and converting them to an iterable).
  return [sanitize_person(person) for person in people]


def create_query(attributes: Dict[str, str]) -> Tuple[str, List[Dict[str, str]]]:
  """
  Creates a SQL-like query for people with the matching name(s).
  :param attributes: The first and/or last name to query for.
  :returns: The query string, and the parameters for the query string.
  """
  # The base query.
  query = 'SELECT * FROM people p'
  parameters = []
  # Get the firstName and lastName from attributes (if present).
  first_name = attributes.get('firstName', None)
  last_name = attributes.get('lastName', None)
  # Add 'WHERE' to the query if either names were given.
  if first_name or last_name:
    query += ' WHERE '
  # Add firstName to the query if it was given.
  if first_name:
    query += 'p.firstName = @firstName'
    parameters.append({'name': '@firstName', 'value': first_name})
  # Add 'AND' to the query if both names were given.
  if first_name and last_name:
    query += ' AND '
  # Add lastName to the query if it was given.
  if last_name:
    query += 'p.lastName = @lastName'
    parameters.append({'name': '@lastName', 'value': last_name})
  # Return the query and it's parameters.
  return query, parameters


def get_limit(attributes: Dict[str, str], max_limit: int) -> int:
  """
  Gets the limit of results for the query.
  :param attributes: The attributes potentially containing a 'limit' key.
  :param max_limit: The maximum limit allowed.
  :returns: The limit for the query.
  """
  limit = attributes.get('limit', max_limit)
  try:
    limit = int(limit)
  except ValueError:
    limit = max_limit
  return min(limit, max_limit)


def sanitize_person(person: Dict[str, Any]) -> Dict[str, Any]:
  """
  Removes attributes from the person that the client should not see.
  :param person: The person to sanitize.
  :returns: The original person after sanitizing (the original is altered).
  """
  person.pop('id', None)
  person.pop('_rid', None)
  person.pop('_self', None)
  person.pop('_etag', None)
  person.pop('_attachments', None)
  person.pop('_ts', None)
  return person
