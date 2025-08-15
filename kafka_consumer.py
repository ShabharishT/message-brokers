"""
Simple Kafka Consumer

Examples:
  python kafka_consumer.py --topic test-topic --group test-group \
    --bootstrap-servers localhost:9092 --auto-offset-reset earliest

Environment variables (used as defaults if flags omitted):
  KAFKA_BOOTSTRAP_SERVERS (default: localhost:9092)
  KAFKA_TOPIC (default: test-topic)
  KAFKA_GROUP_ID (default: test-group)
"""

import argparse
import json
import os

from kafka import KafkaConsumer


def create_consumer(
    bootstrap_servers: str,
    topic: str,
    group_id: str,
    auto_offset_reset: str,
) -> KafkaConsumer:
    """Create and return a configured KafkaConsumer."""
    return KafkaConsumer(
        topic,
        bootstrap_servers=bootstrap_servers,
        group_id=group_id,
        auto_offset_reset=auto_offset_reset,
        enable_auto_commit=True,
        value_deserializer=lambda v: json.loads(v.decode("utf-8")),
    )


def consume_messages(consumer: KafkaConsumer) -> None:
    """Continuously consume messages and print them."""
    for record in consumer:  # type: ignore[assignment]
        try:
            print(
                f"Received from topic='{record.topic}', partition={record.partition}, offset={record.offset}: {record.value}"
            )
        except Exception as process_error:
            print(f"Processing failed: {process_error}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Simple Kafka Consumer")
    parser.add_argument(
        "--bootstrap-servers",
        default=os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092"),
        help="Kafka bootstrap servers host:port",
    )
    parser.add_argument(
        "--topic",
        default=os.getenv("KAFKA_TOPIC", "test-topic"),
        help="Kafka topic to consume from",
    )
    parser.add_argument(
        "--group",
        default=os.getenv("KAFKA_GROUP_ID", "test-group"),
        help="Consumer group id",
    )
    parser.add_argument(
        "--auto-offset-reset",
        choices=["earliest", "latest", "none"],
        default="earliest",
        help="Where to start if no committed offset",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    print("Kafka Consumer starting…")
    print(f"Bootstrap servers: {args.bootstrap_servers}")
    print(f"Topic: {args.topic}, Group: {args.group}, AutoOffsetReset: {args.auto_offset_reset}")

    consumer = create_consumer(
        bootstrap_servers=args.bootstrap_servers,
        topic=args.topic,
        group_id=args.group,
        auto_offset_reset=args.auto_offset_reset,
    )
    try:
        consume_messages(consumer)
    except KeyboardInterrupt:
        print("Stopped by user")
    finally:
        try:
            consumer.close()
            print("Consumer closed")
        except Exception:
            pass


if __name__ == "__main__":
    main()



