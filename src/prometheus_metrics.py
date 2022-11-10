from prometheus_client import start_http_server, Summary, Counter
import random
import time

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
TEST_METRICS = Counter('request_processing_seconds1', 'Time spent processing request')

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