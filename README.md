# Twinkly-haha
OpenC2 messages using MQTT Transfer Specification

## HTTP
Using HTTP Producer connects directly to a single Consumer:
```mermaid
sequenceDiagram
    Producer->>+Consumer: Command A
    Consumer->>-Producer: Response A
```

# MQTT
MQTT requires a topic overlay to support request-response, for a single or multiple Consumers:
```mermaid
sequenceDiagram
    Producer->>Broker: Connect and subscribe to all participants
    Consumer1->>+Broker: Connect and subscribe to topic C1
    Producer->>Broker: Publish Command A to topic C1
    Broker->>+Consumer1: Command A
    Consumer1->>-Broker: Publish Response A to topic R1
    Broker->>Producer: Response A
```
