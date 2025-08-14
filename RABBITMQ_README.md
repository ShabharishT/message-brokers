# RabbitMQ Producer and Consumer Examples

This directory contains simple Python examples for RabbitMQ message publishing and consuming.

## Files

- `rabbitmq_producer.py` - Simple producer that sends 5 predefined messages
- `rabbitmq_consumer.py` - Consumer that listens for and processes messages
- `interactive_producer.py` - Interactive producer for sending custom messages
- `requirements.txt` - Python dependencies

## Prerequisites

1. **RabbitMQ running locally** (via Docker Compose)
2. **Python 3.6+**
3. **Required packages installed**

## Installation

```bash
# Install dependencies
pip3 install -r requirements.txt
```

## Usage

### 1. Start RabbitMQ Services

```bash
# Start all services (including RabbitMQ)
docker-compose up -d

# Or start only RabbitMQ
docker-compose -f rabbitmq-docker-compose.yml up -d
```

### 2. Run the Examples

#### Option A: Simple Producer (5 predefined messages)
```bash
python3 rabbitmq_producer.py
```

#### Option B: Interactive Producer (send custom messages)
```bash
python3 interactive_producer.py
```

#### Option C: Consumer (listen for messages)
```bash
python3 rabbitmq_consumer.py
```

### 3. Test the Complete Flow

1. **Terminal 1**: Start the consumer
   ```bash
   python3 rabbitmq_consumer.py
   ```

2. **Terminal 2**: Start the producer
   ```bash
   python3 rabbitmq_producer.py
   ```

3. **Watch the consumer receive and process messages!**

## Message Format

Messages are sent as JSON with the following structure:
```json
{
  "message": "Your message text",
  "timestamp": "2025-08-14T17:30:00.123456",
  "id": 1692030600123
}
```

## Queue Details

- **Queue Name**: `demo_queue`
- **Durable**: Yes (survives broker restarts)
- **Message Persistence**: Yes (survives broker restarts)

## Connection Details

- **Host**: localhost
- **Port**: 5672
- **Username**: admin
- **Password**: admin123
- **Virtual Host**: /

## Management UI

Access RabbitMQ Management Interface:
- **URL**: http://localhost:15672
- **Username**: admin
- **Password**: admin123

## Features

### Producer Features
- ✅ Automatic queue declaration
- ✅ Message persistence
- ✅ JSON message format
- ✅ Timestamp and ID generation
- ✅ Error handling

### Consumer Features
- ✅ Automatic queue declaration
- ✅ Message acknowledgment
- ✅ JSON message parsing
- ✅ Error handling with message requeuing
- ✅ QoS settings (prefetch count = 1)

## Troubleshooting

### Connection Issues
- Ensure RabbitMQ is running: `docker-compose ps`
- Check RabbitMQ logs: `docker-compose logs rabbitmq`
- Verify port 5672 is accessible

### Message Issues
- Check queue exists in Management UI
- Verify consumer is running before producer
- Check for error messages in consumer output

## Next Steps

1. **Add Exchanges**: Implement routing with exchanges
2. **Multiple Queues**: Create different queue types
3. **Message Patterns**: Implement pub/sub, work queues, etc.
4. **Error Handling**: Add dead letter queues
5. **Monitoring**: Add metrics and health checks
