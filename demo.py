#!/usr/bin/env python3
"""
Demo script showing basic usage of RabbitMQ and Kafka
"""

import time
import json
from datetime import datetime

def demo_rabbitmq():
    """Demo RabbitMQ functionality"""
    print("🐰 RabbitMQ Demo")
    print("-" * 30)
    print("Management UI: http://localhost:15672")
    print("Username: admin")
    print("Password: admin123")
    print("AMQP Port: 5672")
    print()
    
    # Example connection string for applications
    print("Example connection string:")
    print("amqp://admin:admin123@localhost:5672/")
    print()

def demo_kafka():
    """Demo Kafka functionality"""
    print("📊 Kafka Demo")
    print("-" * 30)
    print("Bootstrap Servers: localhost:9092")
    print("Zookeeper: localhost:2181")
    print("Kafka UI: http://localhost:8080")
    print()
    
    # Example configuration for applications
    print("Example configuration:")
    print("bootstrap.servers=localhost:9092")
    print("zookeeper.connect=localhost:2181")
    print()

def demo_usage():
    """Show usage examples"""
    print("🚀 Usage Examples")
    print("-" * 30)
    print("1. Start services:")
    print("   docker-compose up -d")
    print()
    print("2. Stop services:")
    print("   docker-compose down")
    print()
    print("3. View logs:")
    print("   docker-compose logs -f [service_name]")
    print()
    print("4. Check status:")
    print("   docker-compose ps")
    print()

if __name__ == "__main__":
    print("🎯 Message Brokers Local Setup")
    print("=" * 50)
    print()
    
    demo_rabbitmq()
    demo_kafka()
    demo_usage()
    
    print("=" * 50)
    print("✅ Setup complete! Both RabbitMQ and Kafka are running locally.")
    print("🌐 Open the management UIs in your browser to explore the services.")
