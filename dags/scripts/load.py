import pandas as pd
from sqlalchemy import create_engine, String, DateTime
from datetime import datetime

def save_data(data):
    df = pd.DataFrame(data, columns=["Headline"])
    df["date_scraped"] = datetime.now()

    db_url = "postgresql://airflow:airflow@postgres:5432/airflow"
    engine = create_engine(db_url)

    df.to_sql(
        "scraped_data",
        engine,
        if_exists="append",
        index=False,
        dtype={
            "Headline": String(),
            "date_scraped": DateTime()
        }
    )
