"""
DAG for scraping Hacker News headlines daily, transforming them, and loading into PostgreSQL.
"""

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.email import send_email
from datetime import datetime

from scripts.scrape import scrape_data
from scripts.transform import clean_data
from scripts.load import save_data


def notify_failure(context):
    subject = f"❌ DAG Failed: {context.get('task_instance').dag_id}"
    html_content = f"""
    DAG: {context.get('task_instance').dag_id} <br>
    Task: {context.get('task_instance').task_id} <br>
    Execution Time: {context.get('execution_date')} <br>
    Log URL: <a href="{context.get('task_instance').log_url}">View Logs</a>
    """
    send_email(
        to=["pandeyash1706@gmail.com"],
        subject=subject,
        html_content=html_content
    )


def notify_success(context):
    subject = f"✅ DAG Succeeded: {context.get('task_instance').dag_id}"
    html_content = f"""
    🎉 DAG completed successfully! <br><br>
    DAG: {context.get('task_instance').dag_id} <br>
    Task: {context.get('task_instance').task_id} <br>
    Execution Time: {context.get('execution_date')} <br>
    Log URL: <a href="{context.get('task_instance').log_url}">View Logs</a>
    """
    send_email(
        to=["pandeyash1706@gmail.com"],
        subject=subject,
        html_content=html_content
    )


def run_scrape_pipeline():
    print("Starting ScrapeForce pipeline...")
    raw = scrape_data()
    cleaned = clean_data(raw)
    save_data(cleaned)
    print("Pipeline completed successfully.")


default_args = {
    "on_failure_callback": notify_failure,
    "email_on_failure": True,
    "email_on_retry": False,
    "retries": 1,
}

with DAG(
    dag_id="scrapeforce_web_scraping",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["web_scraping", "scrapeforce"],
    default_args=default_args,
) as dag:
    run_pipeline = PythonOperator(
        task_id="run_scrape_pipeline",
        python_callable=run_scrape_pipeline,
        on_success_callback=notify_success
    )
