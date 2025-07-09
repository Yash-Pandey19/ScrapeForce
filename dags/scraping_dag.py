from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from scripts.scrape import scrape_data
from scripts.transform import clean_data
from scripts.load import save_data

def run_scrape_pipeline():
    raw = scrape_data()
    cleaned = clean_data(raw)
    save_data(cleaned)

with DAG(
    dag_id="scrapeforce_web_scraping",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["web_scraping", "scrapeforce"]
) as dag:
    run_pipeline = PythonOperator(
        task_id="run_scrape_pipeline",
        python_callable=run_scrape_pipeline
    )
