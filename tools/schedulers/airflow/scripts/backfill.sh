#!/home/ujjwalbrahmin/SoftwareDevelopment/Tools/AirFlowTutorial/.venv/bin/python

export AIRFLOW_HOME=/home/ujjwalbrahmin/SoftwareDevelopment/Tools/AirFlowTutorial

echo Backfilling a DAG...
airflow dags backfill -s 2023-03-15 -e 2023-03-25 catch-up_and_back-fill_v2