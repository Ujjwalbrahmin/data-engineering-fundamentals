#!/home/ujjwalbrahmin/SoftwareDevelopment/Tools/AirFlowTutorial/.venv/bin/python

echo Initializing AirFlow home dir...
export AIRFLOW_HOME=/home/ujjwalbrahmin/SoftwareDevelopment/Tools/AirFlowTutorial

echo Initializing DB...
# creates a SQLite Database, log folders and configurations files
airflow db init
