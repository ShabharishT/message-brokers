#!/usr/bin/env python3
"""
Simple RabbitMQ Producer
Publishes messages to a queue
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

def publish_message(channel, queue_name, message):
    """Publish a message to the queue"""
    try:
        # Prepare message with timestamp
        message_data = {
            'message': message,
            'timestamp': datetime.now().isoformat(),
            'id': int(time.time() * 1000)
        }
        
        # Convert to JSON
        message_body = json.dumps(message_data)
        
        # Publish message
        channel.basic_publish(
            exchange='',
            routing_key=queue_name,
            body=message_body,
            properties=pika.BasicProperties(
                delivery_mode=2,  # Make message persistent
                content_type='application/json'
            )
        )
        
        print(f"📤 Published: {message}")
        return True
        
    except Exception as e:
        print(f"❌ Failed to publish message: {e}")
        return False

def main():
    """Main producer function"""
    print("🐰 RabbitMQ Producer Starting...")
    print("=" * 40)
    
    # Create connection
    connection, channel, queue_name = create_connection()
    if not connection:
        return
    
    try:
        # Send some sample messages
        messages = [
            "Hello from RabbitMQ Producer!",
            "This is a test message",
            "RabbitMQ is awesome!",
            "Message with timestamp",
            "Final message for now"
        ]
        
        print(f"\n📤 Publishing {len(messages)} messages...")
        print("-" * 40)
        
        for i, message in enumerate(messages, 1):
            success = publish_message(channel, queue_name, message)
            if success:
                time.sleep(1)  # Wait 1 second between messages
        
        print("-" * 40)
        print(f"✅ Published {len(messages)} messages to queue '{queue_name}'")
        print(f"🌐 Check RabbitMQ Management UI: http://localhost:15672")
        
    except KeyboardInterrupt:
        print("\n\n⏹️  Producer stopped by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
    finally:
        # Close connection
        if connection:
            connection.close()
            print("🔌 Connection closed")

if __name__ == "__main__":
    main()
