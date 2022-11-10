from prometheus_client import start_http_server
from prometheus_client import Counter, Gauge, Histogram, Summary, generate_latest, CollectorRegistry
from random import randint
import random
import time

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
TEST_METRICS = Counter('request_processing_seconds1', 'Time spent processing request')

registry = CollectorRegistry()
counter = Counter('my_counter', 'an example showed how to use counter', ['machine_ip'], registry=registry)
gauge = Gauge('my_gauge', 'an example showed how to use gauge', ['machine_ip'], registry=registry)

buckets = (100, 200, 300, 500, 1000, 3000, 10000, float('inf'))
histogram = Histogram('my_histogram', 'an example showed how to use histogram',
                      ['machine_ip'], registry=registry, buckets=buckets)
summary = Summary('my_summary', 'an example showed how to use summary', ['machine_ip'], registry=registry)



# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)

def main():
    # Start up the server to expose the metrics.
    start_http_server(18002)
    # Generate some requests.
    # while True:
    #     process_request(random.random())
    #     time.sleep(3)

if __name__ == '__main__':
    main()