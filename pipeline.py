from prefect import flow, task
import subprocess

@task
def ingestion_task():
    subprocess.run(["python", "src/ingestion.py"], check=True)

@task
def vector_transform_task():
    subprocess.run(["python", "src/data_to_vector.py"], check=True)

@flow
def vector_pipeline():
    ingestion_task()
    vector_transform_task()

if __name__ == "__main__":
    vector_pipeline()