FROM apache/airflow:2.6.3

USER root

# Install dbt and PostgreSQL client libraries
RUN apt-get update && apt-get install -y libpq-dev && \
    pip install --no-cache-dir dbt-core dbt-postgres

USER airflow
