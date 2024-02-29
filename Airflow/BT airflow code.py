import os
from airflow import DAG
from airflow.models import Variable
from airflow.operators.dummy import DummyOperator
from airflow.contrib.operators.bigquery_operator import BigQueryOperator 
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryOperator
from airflow.providers.google.cloud.operators.pubsub import PubSubPullOperator, PubSubPublishMessageOperator
from airflow import models
from datetime import datetime , timedelta, timezone
from google.cloud import logging as cloud_logging
import logging
from urllib.parse import unquote
from airflow.hooks.base_hook import BaseHook
from google.protobuf.json_format import MessageToDict
import re
from airflow.operators.python_operator import PythonOperator
default_args = {'owner': 'insert_rows_ms',
                'start_date': datetime.now() - timedelta(minutes=45),
                'retries': 0   
                }


dag_id = 'External_table_count_dag'
L2DataprocSAConnGrprevassuran="L2DataprocSAConnGrprevassuran"
impersonation_chain = unquote(BaseHook.get_connection(L2DataprocSAConnGrprevassuran).get_uri())
impersonation_chain = impersonation_chain.split('//')[-1].split(',')
dag = DAG(dag_id,
          catchup=False,
          max_active_runs=1,
		  schedule_interval='1 1 1 1 1',
          default_args=default_args,
          description='Dag for milestone Load')


task_start = DummyOperator(task_id='start', do_xcom_push=False, dag=dag)




external_table_count1 = BigQueryOperator(
    task_id = "external_table_count1", 
    sql = f"select count(*) from `bt-grp-revassuran-r-data.ds_milestone_ext.eeb_motorola_med_hist`",
    use_legacy_sql = False,
    location = "europe-west2",
    gcp_conn_id = "L2DataprocSAConnGrprevassuran",
    impersonation_chain = impersonation_chain,
    dag = dag   
)


external_table_count2 = BigQueryOperator(
    task_id = "external_table_count2", 
    sql = f"select count(*) from `bt-grp-revassuran-r-data.ds_milestone_ext.eeb_motorola_unbilled_hist`",
    use_legacy_sql = False,
    location = "europe-west2",
    gcp_conn_id = "L2DataprocSAConnGrprevassuran",
    impersonation_chain = impersonation_chain,
    dag = dag   
)
external_table_count3 = BigQueryOperator(
    task_id = "external_table_count3", 
    sql = f"select count(*) from `bt-grp-revassuran-r-data.ds_milestone_ext.eeb_rda_hist`",
    use_legacy_sql = False,
    location = "europe-west2",
    gcp_conn_id = "L2DataprocSAConnGrprevassuran",
    impersonation_chain = impersonation_chain,
    dag = dag   
)
external_table_count4 = BigQueryOperator(
    task_id = "external_table_count4", 
    sql = f"select count(*) from `bt-grp-revassuran-r-data.ds_milestone_ext.eeb_split_hist`",
    use_legacy_sql = False,
    location = "europe-west2",
    gcp_conn_id = "L2DataprocSAConnGrprevassuran",
    impersonation_chain = impersonation_chain,
    dag = dag   
)
external_table_count5 = BigQueryOperator(
    task_id = "external_table_count5", 
    sql = f"select count(*) from `bt-grp-revassuran-r-data.ds_milestone_ext.gba_usage_callplan_breach`",
    use_legacy_sql = False,
    location = "europe-west2",
    gcp_conn_id = "L2DataprocSAConnGrprevassuran",
    impersonation_chain = impersonation_chain,
    dag = dag   
)


task_end = DummyOperator(task_id='end', trigger_rule="none_failed",do_xcom_push=False, dag=dag)


task_start >> external_table_count1 >> external_table_count2 >> external_table_count3 >> external_table_count4 >> external_table_count5 >> task_end
