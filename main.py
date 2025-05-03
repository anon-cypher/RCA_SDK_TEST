from observability.logger import setup_logger
import time
import random

logger = setup_logger()

def simulate_service():
    logger.info("Service started")
    while True:
        val = random.randint(0, 100)
        logger.info(f"Processing value: {val}")
        if val % 15 == 0:
            logger.error("Simulated error occurred")
        time.sleep(2)

if __name__ == "__main__":
    simulate_service()