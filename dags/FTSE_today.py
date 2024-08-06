from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import timedelta
from datetime import date
import yfinance as yf

default_args = {
    'owner': 'armaanPy',
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

# Fetch FTSE price.
def fetch_ftse_price():
    ticker = "^FTSE"
    ftse = yf.Ticker(ticker)
    todays_data = ftse.history(period='1d')
    ftse_price = todays_data['Close'][0]
    print(f"FTSE closing price today ({date.today()}): {ftse_price}.")
    

with DAG(
    'FTSE_today_DAG',
    default_args=default_args,
    schedule_interval='@daily', # Schedule daily
    catchup=False               # Do not catchup on missed intervals.
) as dag:
    # Define the Python task.
    FTSE_today_task = PythonOperator(
        task_id = 'FTSE_today_task',
        python_callable=fetch_ftse_price
    )