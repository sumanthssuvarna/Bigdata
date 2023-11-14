Enable Dataflow API.

Create two buckets
1.python code
2.project→data_files—>csv file


export PROJECT=
gcloud config set project $PROJECT



Create a bq dataset
bq mk splitwise


Run the following in Cloud Shell to start up a Python Container:
docker run -it -e PROJECT=$PROJECT -v $(pwd)/dataflow-python-examples:/dataflow python:3.8 /bin/bash




pip install apache-beam[gcp]==2.24.0

cd dataflow/

python dataflow_python_examples/data_ingestion.py \
  --project=$PROJECT --region= \
  --runner=DataflowRunner \
  --machine_type=e2-standard-2 \
  --staging_location=gs://$PROJECT/test \
  --temp_location gs://$PROJECT/test \
  --input gs://$PROJECT/data_files/splitwise_transformed.csv.csv \
  --save_main_session

