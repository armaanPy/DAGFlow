### Requirements
Install Docker Community Edition (CE) on your workstation. Depending on your OS, you may need to configure Docker to use at least 4.00 GB of memory for the Airflow containers to run properly.

Install Docker Compose v2.14.0 or newer on your workstation.

### Initialise the Database
On all operating systems, you need to run database migrations and create the first user account. To do this, run:
```docker compose up airflow-init```

After initialisation is complete, you should see a message like this:
```
airflow-init_1       | Upgrades done
airflow-init_1       | Admin user airflow created
airflow-init_1       | 2.9.3
start_airflow-init_1 exited with code 0
```

The account has created the login airflow and the password airflow.

### Build image that contains custom Poetry dependencies
```docker-compose build```

### Running Airflow
You can start all services with the following command:
```docker compose up```
You can use the ```-d``` flag to run in detached, but it is not recommended as you will want to see when the instance has spun up.

### Stopping Airflow
You can stop and delete containers, volumes with database data and images with the following command:
```docker compose down --volumes --rmi all```

### Cleaning up the environment
The docker-compose environment we have prepared is a “quick-start” one. It was not designed to be used in production and it has a number of caveats - one of them being that the best way to recover from any problem is to clean it up and restart from scratch.

The best way to do this is to:

Run ```docker compose down --volumes --remove-orphans``` command in the directory where the docker-compose.yaml file is present.

Remove the entire directory where the docker-compose.yaml file is present: ```rm -rf '<DIRECTORY>'```

Pull the docker-compose.yaml file again, and follow the previous steps in this guide: ```curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.9.3/docker-compose.yaml'```

### Developing DAGs
An environment to develop DAGs has already been set up for you, simply open your DevContainer in VS Code and create your DAGs in the /dags directory.
After you have developed your DAGs, reopen the folder in SSH to be able to spin up Airflow.

### Misc
If you are not using a Linux-based OS, you may get a warning that the AIRFLOW_UID is not set, but you can safely ignore this.

If you want to get rid of the warning, you can manually create a .env file in the same folder as docker-compose.yaml with this content to get rid of the warning:
```AIRFLOW_UID=50000```

### More info
https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html