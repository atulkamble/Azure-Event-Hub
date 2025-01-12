from azure.eventhub import EventHubProducerClient, EventData

CONNECTION_STRING = "<Event Hub Namespace Connection String>"
EVENT_HUB_NAME = "<Event Hub Name>"

def send_event_batch():
    producer = EventHubProducerClient.from_connection_string(
        conn_str=CONNECTION_STRING, eventhub_name=EVENT_HUB_NAME
    )
    try:
        with producer:
            # Create a batch.
            event_data_batch = producer.create_batch()
            
            # Add events to the batch.
            for i in range(10):
                event_data_batch.add(EventData(f"Message {i+1}"))
            
            # Send the batch of events.
            producer.send_batch(event_data_batch)
            print("Batch of events sent!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    send_event_batch()
