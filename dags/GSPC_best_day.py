from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from datetime import timedelta
from datetime import date
import yfinance as yf

default_args = {
    'owner': 'armaanPy',
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

# Get highest closing price for S&P 500 this year.
def get_gspc_best_day():
    start_date = datetime(datetime.now().year, 1, 1).strftime('%Y-%m-%d')
    end_date = datetime.now().strftime('%Y-%m-%d')
    sp500_data = yf.download('^GSPC', start=start_date, end=end_date)
    max_close = sp500_data['Close'].max()
    max_close_date = sp500_data['Close'].idxmax()
    print(f"The highest closing price for the S&P 500 this year was ${max_close:.2f} on {max_close_date.strftime('%Y-%m-%d')}")

with DAG(
    'GSPC_close_DAG',
    default_args=default_args,
    schedule_interval='@daily', # Schedule daily
    catchup=False               # Do not catchup on missed intervals.
) as dag:
    # Define the Python task.
    FTSE_today_task = PythonOperator(
        task_id = 'GSPC_close_task',
        python_callable=get_gspc_best_day
    )