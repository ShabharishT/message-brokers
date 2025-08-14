#!/usr/bin/env python3
"""
Interactive RabbitMQ Producer
Allows user to send custom messages interactively
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
        queue_name = 'demo_queue'
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
    """Main interactive producer function"""
    print("🐰 Interactive RabbitMQ Producer")
    print("=" * 40)
    
    # Create connection
    connection, channel, queue_name = create_connection()
    if not connection:
        return
    
    try:
        print(f"\n📝 Ready to send messages to queue '{queue_name}'")
        print("💡 Type your message and press Enter to send")
        print("💡 Type 'quit' or 'exit' to stop")
        print("💡 Type 'help' for available commands")
        print("-" * 40)
        
        message_count = 0
        
        while True:
            try:
                # Get user input
                user_input = input("\n📝 Enter message: ").strip()
                
                if user_input.lower() in ['quit', 'exit', 'q']:
                    print("👋 Goodbye!")
                    break
                elif user_input.lower() in ['help', 'h', '?']:
                    print("\n📚 Available Commands:")
                    print("   help, h, ?  - Show this help")
                    print("   quit, exit, q - Stop the producer")
                    print("   <any text>  - Send a message")
                    continue
                elif not user_input:
                    print("⚠️  Please enter a message")
                    continue
                
                # Send message
                success = publish_message(channel, queue_name, user_input)
                if success:
                    message_count += 1
                    print(f"�� Total messages sent: {message_count}")
                
            except KeyboardInterrupt:
                print("\n\n⏹️  Producer stopped by user")
                break
            except EOFError:
                print("\n\n⏹️  End of input")
                break
        
        print(f"\n📊 Session Summary:")
        print(f"   Messages sent: {message_count}")
        print(f"   Queue: {queue_name}")
        print(f"🌐 Check RabbitMQ Management UI: http://localhost:15672")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
    finally:
        # Close connection
        if connection:
            connection.close()
            print("🔌 Connection closed")

if __name__ == "__main__":
    main()
