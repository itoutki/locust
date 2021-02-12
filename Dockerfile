FROM locustio/locust:1.4.3

ADD locust_scripts /locust_scripts

ENTRYPOINT ["/locust_scripts/run.sh"]
