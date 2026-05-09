######################## Commands #########################

#newrelic-admin generate-config YOURLICENSEKEY newrelic.ini
#NEWRELICCONFIGFILE=newrelic.ini newrelic-admin run-program python app.py
#source test/bin/activate -"to activate or resume your env"
#deactivate - "to close your environment"
#Note - never upload your venv folder to GitHub or Bitbucket
#pip install -r requirements.txt
#pip freeze > requirements.txt ("taking a snapshot" of your current sandbox) & (to update your "recipe" list)

##mypythonapp/
├── app.py              <-- The Entry Point (Run this)
├── config.py           <-- Configuration Loader
├── extensions.py       <-- Shared objects (like the DB)
├── routes.py           <-- All your URL endpoints
├── models.py           <-- Database structure
├── .env                <-- Secrets (Postgres URL)
├── .gitignore          <-- Keep Git clean
├── newrelic.ini        <-- Monitoring
├── logs/
│   └── api.log         <-- App logs
└── templates/
    ├── base.html       <-- Main Design (CSS/Layout)
    ├── index.html      <-- Home Page
    └── users.html      <-- User Table Page
