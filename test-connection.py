#!/usr/bin/env python3
"""
Simple test script to verify RabbitMQ and Kafka connections
"""

import socket
import requests
import json

def test_rabbitmq():
    """Test RabbitMQ connection"""
    try:
        # Test AMQP port
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('localhost', 5672))
        sock.close()
        
        if result == 0:
            print("✅ RabbitMQ AMQP port (5672) is accessible")
        else:
            print("❌ RabbitMQ AMQP port (5672) is not accessible")
            
        # Test management UI
        response = requests.get('http://localhost:15672', timeout=5)
        if response.status_code == 200:
            print("✅ RabbitMQ Management UI (15672) is accessible")
        else:
            print("❌ RabbitMQ Management UI (15672) returned status:", response.status_code)
            
    except Exception as e:
        print(f"❌ RabbitMQ test failed: {e}")

def test_kafka():
    """Test Kafka connection"""
    try:
        # Test Kafka port
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('localhost', 9092))
        sock.close()
        
        if result == 0:
            print("✅ Kafka port (9092) is accessible")
        else:
            print("❌ Kafka port (9092) is not accessible")
            
        # Test Zookeeper port
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('localhost', 2181))
        sock.close()
        
        if result == 0:
            print("✅ Zookeeper port (2181) is accessible")
        else:
            print("❌ Zookeeper port (2181) is not accessible")
            
        # Test Kafka UI
        response = requests.get('http://localhost:8080', timeout=5)
        if response.status_code == 200:
            print("✅ Kafka UI (8080) is accessible")
        else:
            print("❌ Kafka UI (8080) returned status:", response.status_code)
            
    except Exception as e:
        print(f"❌ Kafka test failed: {e}")

if __name__ == "__main__":
    print("🔍 Testing Message Broker Connections...")
    print("=" * 50)
    
    test_rabbitmq()
    print()
    test_kafka()
    
    print("\n" + "=" * 50)
    print("📋 Access URLs:")
    print("   RabbitMQ Management: http://localhost:15672 (admin/admin123)")
    print("   Kafka UI:           http://localhost:8080")
    print("   RabbitMQ AMQP:      localhost:5672")
    print("   Kafka:              localhost:9092")
    print("   Zookeeper:          localhost:2181")
