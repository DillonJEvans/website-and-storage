from . import container


def query_people(attributes):
  query, parameters = create_query(attributes)
  limit = get_limit(attributes, 20)
  query += f' OFFSET 0 LIMIT {limit}'
  print(f'Query: {query}')
  people = container.query_items(
    query=query,
    parameters=parameters,
    enable_cross_partition_query=True
  )
  return [sanitize_person(person) for person in people]


def create_query(attributes):
  query = 'SELECT * FROM people p'
  parameters = []
  first_name = attributes.get('firstName', None)
  last_name = attributes.get('lastName', None)
  if first_name or last_name:
    query += ' WHERE '
    if first_name:
      query += 'p.firstName = @firstName'
      parameters.append({'name': '@firstName', 'value': first_name})
    if first_name and last_name:
      query += ' AND '
    if last_name:
      query += 'p.lastName = @lastName'
      parameters.append({'name': '@lastName', 'value': last_name})
  return query, parameters


def get_limit(attributes, max_limit):
  limit = attributes.get('limit', max_limit)
  try:
    limit = int(limit)
  except ValueError:
    limit = max_limit
  return min(limit, max_limit)


def sanitize_person(person):
  person.pop('id', None)
  person.pop('_rid', None)
  person.pop('_self', None)
  person.pop('_etag', None)
  person.pop('_attachments', None)
  person.pop('_ts', None)
  return person
