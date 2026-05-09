######################## Commands #########################

1. newrelic-admin generate-config YOURLICENSEKEY newrelic.ini
2. NEWRELICCONFIGFILE=newrelic.ini newrelic-admin run-program python app.py
3. source test/bin/activate -"to activate or resume your env"
4. deactivate - "to close your environment"
5. Note - never upload your venv folder to GitHub or Bitbucket
6. pip install -r requirements.txt
7. pip freeze > requirements.txt ("taking a snapshot" of your current sandbox) & (to update your "recipe" list)


0. mypythonapp/
1. ├── app.py              <-- The Entry Point (Run this)
2. ├── config.py           <-- Configuration Loader
3. ├── extensions.py       <-- Shared objects (like the DB)
4. ├── routes.py           <-- All your URL endpoints
5. ├── models.py           <-- Database structure
6. ├── .env                <-- Secrets (Postgres URL)
7. ├── .gitignore          <-- Keep Git clean
8. ├── newrelic.ini        <-- Monitoring
9. ├── logs/
10. │   └── api.log         <-- App logs
11. └── templates/
12.     ├── base.html       <-- Main Design (CSS/Layout)
13.     ├── index.html      <-- Home Page
14.     └── users.html      <-- User Table Page
