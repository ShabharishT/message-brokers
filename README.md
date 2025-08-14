# Local Message Brokers Setup

This directory contains Docker Compose configurations for running RabbitMQ and Kafka locally.

## Services

### RabbitMQ
- **Port**: 5672 (AMQP), 15672 (Management UI)
- **Username**: admin
- **Password**: admin123
- **Management UI**: http://localhost:15672

### Kafka
- **Port**: 9092 (Kafka), 2181 (Zookeeper), 8080 (Kafka UI)
- **Zookeeper**: Required for Kafka coordination
- **Kafka UI**: http://localhost:8080

## Quick Start

### Start all services:
```bash
docker-compose up -d
```

### Start only RabbitMQ:
```bash
docker-compose -f rabbitmq-docker-compose.yml up -d
```

### Start only Kafka:
```bash
docker-compose -f kafka-docker-compose.yml up -d
```

### Stop services:
```bash
docker-compose down
```

### View logs:
```bash
docker-compose logs -f [service_name]
```

## Management Interfaces

1. **RabbitMQ Management**: http://localhost:15672
   - Login with admin/admin123
   - Monitor queues, exchanges, connections

2. **Kafka UI**: http://localhost:8080
   - Browse topics, consumers, and messages
   - Create and manage topics

## Connection Details

### RabbitMQ
- Host: localhost
- Port: 5672
- Username: admin
- Password: admin123

### Kafka
- Bootstrap Servers: localhost:9092
- Zookeeper: localhost:2181

## Troubleshooting

- If ports are already in use, modify the port mappings in the compose files
- Use `docker-compose ps` to check service status
- Use `docker-compose logs` to view service logs
