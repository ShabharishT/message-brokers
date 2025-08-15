# Copilot Instructions for message-brokers

## Project Overview
This repository provides local development setups for RabbitMQ and Kafka using Docker Compose, along with Python scripts for producing and consuming messages. It is designed for quick experimentation and integration testing of message broker workflows.

## Architecture & Components
- **Docker Compose Files**: `docker-compose.yml`, `rabbitmq-docker-compose.yml`, `kafka-docker-compose.yml` define service orchestration for RabbitMQ and Kafka. Zookeeper is required for Kafka.
- **Python Scripts**:
  - `rabbitmq_producer.py` / `rabbitmq_consumer.py`: Example producer/consumer for RabbitMQ.
  - `interactive_producer.py`, `demo.py`, `test-connection.py`: Utility scripts for testing broker connectivity and message flows.
  - Kafka scripts should use `kafka-python` and connect to `localhost:9092`.
- **README.md**: Contains essential connection details, management UI URLs, and quickstart commands.

## Developer Workflows
- **Start All Services**: `docker-compose up -d`
- **Start RabbitMQ Only**: `docker-compose -f rabbitmq-docker-compose.yml up -d`
- **Start Kafka Only**: `docker-compose -f kafka-docker-compose.yml up -d`
- **Stop Services**: `docker-compose down`
- **View Logs**: `docker-compose logs -f [service_name]`
- **Check Status**: `docker-compose ps`

## Integration Points
- **RabbitMQ**: Default credentials are `admin`/`admin123`. Management UI at `http://localhost:15672`.
- **Kafka**: Connect to `localhost:9092`. Kafka UI at `http://localhost:8080`.
- **Zookeeper**: Required for Kafka, runs on `localhost:2181`.

## Patterns & Conventions
- Python scripts use direct connections to brokers (no abstraction layers).
- Message formats are typically UTF-8 encoded strings.
- Scripts are standalone and do not require frameworks.
- Use `requirements.txt` for Python dependencies (e.g., `kafka-python`, `pika`).
- No custom build or test runners; run scripts directly with Python.

## Example Usage
- To produce messages to Kafka:
  ```python
  from kafka import KafkaProducer
  producer = KafkaProducer(bootstrap_servers='localhost:9092')
  producer.send('test-topic', b'Hello Kafka')
  ```
- To consume messages from RabbitMQ:
  ```python
  import pika
  connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
  channel = connection.channel()
  channel.basic_consume(queue='test', on_message_callback=callback)
  ```

## Troubleshooting
- If ports are busy, update mappings in compose files.
- Use Docker Compose logs and status commands for debugging.

---

For unclear workflows or missing conventions, consult `README.md` or ask for clarification.
