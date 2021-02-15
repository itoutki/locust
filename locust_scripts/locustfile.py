import random
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 1)

    @task
    def index_page(self):
        self.client.get("/select")
