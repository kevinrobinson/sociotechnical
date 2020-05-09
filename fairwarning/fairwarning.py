import sys
import datetime
import json
import os
import pathlib
import requirements


def load_rc():
  rc_path = str(pathlib.Path().absolute()) + '/fairwarning.json'
  with open(rc_path) as f:
    return json.load(f)
  
def load_requirements():
  requirements_path = str(pathlib.Path().absolute()) + '/requirements.txt'
  with open(requirements_path, 'r') as f:
    deps = []
    for dep in requirements.parse(f):
      deps.append(dep)
    return deps

def load_db():
  requirements_path = str(pathlib.Path().absolute()) + '/requirements.txt'
  with open('../_data/db.json', 'r') as f:
    db = json.load(f)

  index = {}
  for i, post in enumerate(db['posts']):
    key = (post['dep']['name'], post['dep']['spec'])
    index[key] = i

  return (db, index)


def find_any_notices(rc, dep, db, db_deps_index):
  notices = []

  spec_key = None if len(dep.specs) == 0 else dep.specs[0][1] # obvs hacked :)
  key = (dep.name, spec_key) 
  if key in db_deps_index:
    post = db['posts'][db_deps_index[key]]
    url = 'http://sociotechnical.org/notice/' + str(post['id'])

    from_countries = post['context']['fromCountries']
    deployment_countries = rc['deployment']['countries']
    if deployment_countries != from_countries:
      notices.append( 'deployment-countries: {}, more at: {}'.format(key, url))

    years_range = post['context']['yearsRange']
    years_in_service = rc['deployment']['yearsInService']
    year_now = datetime.datetime.now().year
    if years_in_service[1] < year_now:
      notices.append('years-in-service: {}, more at: {}'.format(key, url))

    flags = set(post['context']['flagsForScrutiny'])
    concerns = set(rc['concerns'].keys())
    flags_to_raise = (flags - concerns)
    if len(flags_to_raise) > 0:
      for flag in flags_to_raise:
        notices.append('flags-to-raise: {} {}, more at: {}'.format(flag, key, url))

  return notices    


    # {
    #   "deployment": {
    #     "countries": [
    #       "US", 
    #       "Mexico",
    #       "Canada"
    #     ],
    #     "yearsInService": [2019, 2024]
    #   },
    #   "concerns": [
    #     "people"
    #   ]
    # }

    # "context": {
    #   "yearsRange": [2009, null],
    #   "fromCountries": ["US"],
    #   "flagsForScrutiny": [
    #     "people"
    #   ]
    # }

def cli():
  print("Loading...")
  rc = load_rc()
  deps = load_requirements()
  db, db_deps_index = load_db()

  notices = []

  print('Checking dependencies...')
  for dep in deps:
    print("  checking {}...".format(dep.name))
    notices_for_dep = find_any_notices(rc, dep, db, db_deps_index)
    notices += notices_for_dep
  
  do_report(notices)


def do_report(notices):
  if len(notices) > 0:
    print('')
    print("Fairness notices found: {}".format(len(notices)))
    print("-----------------------------")
    print('')
    for notice in notices:
      print("  {}".format(notice))
    print('')
    print("-----------------------------")
    print("Fairness notices found: {}".format(len(notices)))
    sys.exit(126)
  else:
    print("Done.")
    sys.exit(0)
  
