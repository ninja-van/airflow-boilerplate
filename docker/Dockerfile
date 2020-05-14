# NOTE: paths are relative to the project root since the build context we specify is the project root

FROM puckel/docker-airflow:1.10.8
USER root

ENV SPARK_HOME /usr/local/lib/python3.7/site-packages/pyspark
ENV PATH $PATH:$SPARK_HOME/bin
ENV PYTHONPATH $PYTHONPATH:$AIRFLOW_HOME/dags

RUN mkdir -p /usr/share/man/man1 && \
    apt-get update -y && \
    apt-get install -y \
                    procps \
                    libsnappy-dev \
                    openjdk-8-jdk \
                    unzip \
                    && \
    apt-get autoremove -y

COPY docker/entrypoint.sh /entrypoint.sh
RUN rm $AIRFLOW_HOME/airflow.cfg

COPY requirements-airflow.txt requirements.txt
RUN pip3 install -r requirements.txt

RUN ln -s /spark-conf $SPARK_HOME/conf

USER airflow
