#!/usr/bin/env python3
"""
Simple RabbitMQ Consumer
Consumes messages from a queue
"""

import pika
import json
import time
from datetime import datetime

def create_connection():
    """Create connection to RabbitMQ"""
    try:
        # Connection parameters
        credentials = pika.PlainCredentials('admin', 'admin123')
        // Use default RabbitMQ port and virtual host

        parameters = pika.ConnectionParameters(
            host='localhost',
            port=5672,
            virtual_host='/',
            credentials=credentials
        )
        
        # Create connection
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        
        # Declare queue
        queue_name = 'queue_name'
        channel.queue_declare(queue=queue_name, durable=True)
        
        print(f"✅ Connected to RabbitMQ successfully!")
        print(f"📝 Queue '{queue_name}' declared")
        return connection, channel, queue_name
        
    except Exception as e:
        print(f"❌ Failed to connect to RabbitMQ: {e}")
        return None, None, None

def callback(ch, method, properties, body):
    """Callback function to process received messages"""
    try:
        # Parse message
        message_data = json.loads(body.decode('utf-8'))
        
        # Extract information
        message = message_data.get('message', 'Unknown message')
        timestamp = message_data.get('timestamp', 'Unknown time')
        message_id = message_data.get('id', 'Unknown ID')
        
        # Process message
        print(f"\n📥 Received Message #{message_id}")
        print(f"   Content: {message}")
        print(f"   Time: {timestamp}")
        print(f"   Delivery Tag: {method.delivery_tag}")
        
        # Simulate some processing time
        time.sleep(0.5)
        
        # Acknowledge message
        ch.basic_ack(delivery_tag=method.delivery_tag)
        print(f"   ✅ Message acknowledged")
        
    except Exception as e:
        print(f"❌ Error processing message: {e}")
        # Reject message and requeue
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)

def main():
    """Main consumer function"""
    print("🐰 RabbitMQ Consumer Starting...")
    print("=" * 40)
    
    # Create connection
    connection, channel, queue_name = create_connection()
    if not connection:
        return
    
    try:
        # Set QoS (prefetch count)
        channel.basic_qos(prefetch_count=1)
        
        # Set up consumer
        print(f"👂 Listening for messages on queue '{queue_name}'...")
        print("   Press Ctrl+C to stop")
        print("-" * 40)
        
        channel.basic_consume(
            queue=queue_name,
            on_message_callback=callback
        )
        
        # Start consuming
        channel.start_consuming()
        
    except KeyboardInterrupt:
        print("\n\n⏹️  Consumer stopped by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
    finally:
        # Close connection
        if connection:
            connection.close()
            print("🔌 Connection closed")

if __name__ == "__main__":
    main()
