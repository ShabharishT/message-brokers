"""
Simple Kafka Producer

Examples:
  python kafka_producer.py --topic test-topic --messages 5 --interval 0.5 \
    --bootstrap-servers localhost:9092

Environment variables (used as defaults if flags omitted):
  KAFKA_BOOTSTRAP_SERVERS (default: localhost:9092)
  KAFKA_TOPIC (default: test-topic)
"""

import argparse
import json
import os
import time
from datetime import datetime

from kafka import KafkaProducer


def create_producer(bootstrap_servers: str) -> KafkaProducer:
    """Create and return a configured KafkaProducer."""
    return KafkaProducer(
        bootstrap_servers=bootstrap_servers,
        acks="all",
        linger_ms=10,
        retries=3,
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )


def publish_messages(
    producer: KafkaProducer,
    topic: str,
    total_messages: int,
    interval_seconds: float,
) -> None:
    """Publish a set number of JSON messages to a topic, waiting between sends."""
    for i in range(total_messages):
        payload = {
            "id": int(time.time() * 1000),
            "sequence": i,
            "message": f"Hello from Kafka Producer #{i}",
            "timestamp": datetime.now().isoformat(),
        }
        future = producer.send(topic, payload)
        try:
            record_metadata = future.get(timeout=10)
            print(
                f"Sent to topic='{record_metadata.topic}', partition={record_metadata.partition}, offset={record_metadata.offset}: {payload}"
            )
        except Exception as send_error:
            print(f"Send failed: {send_error}")
        time.sleep(interval_seconds)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Simple Kafka Producer")
    parser.add_argument(
        "--bootstrap-servers",
        default=os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092"),
        help="Kafka bootstrap servers host:port",
    )
    parser.add_argument(
        "--topic",
        default=os.getenv("KAFKA_TOPIC", "test-topic"),
        help="Kafka topic to publish to",
    )
    parser.add_argument(
        "--messages",
        type=int,
        default=10,
        help="Number of messages to send",
    )
    parser.add_argument(
        "--interval",
        type=float,
        default=1.0,
        help="Seconds to wait between messages",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    print("Kafka Producer starting…")
    print(f"Bootstrap servers: {args.bootstrap_servers}")
    print(f"Topic: {args.topic}")
    print(f"Messages: {args.messages}, Interval: {args.interval}s")

    producer = create_producer(args.bootstrap_servers)
    try:
        publish_messages(
            producer=producer,
            topic=args.topic,
            total_messages=args.messages,
            interval_seconds=args.interval,
        )
        producer.flush()
        print("All messages flushed")
    except KeyboardInterrupt:
        print("Stopped by user")
    finally:
        try:
            producer.close()
            print("Producer closed")
        except Exception:
            pass


if __name__ == "__main__":
    main()



