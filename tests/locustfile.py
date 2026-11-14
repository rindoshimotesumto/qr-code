from locust import FastHttpUser, task, constant_throughput


class QRLoadTest(FastHttpUser):
    # Гарантирует ровно 1 запрос в секунду от каждого виртуального юзера
    # Если запустить 100 юзеров — получишь ровно 100 RPS
    wait_time = constant_throughput(1)

    @task
    def generate_qr(self):
        payload = {
            "data": "https://example.com",
            "format": "PNG",
            "size": 10,
            "accuracy": 7
        }
        self.client.post("/qrcode", json=payload)
