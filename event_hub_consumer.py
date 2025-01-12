from azure.eventhub import EventHubConsumerClient

CONNECTION_STRING = "<Event Hub Namespace Connection String>"
EVENT_HUB_NAME = "<Event Hub Name>"
CONSUMER_GROUP = "$Default"  # Default consumer group

def on_event(partition_context, event):
    # Print event data.
    print(f"Received event: {event.body_as_str()}")
    
    # Update checkpoint so the program doesn't reprocess the event.
    partition_context.update_checkpoint(event)

def main():
    client = EventHubConsumerClient.from_connection_string(
        conn_str=CONNECTION_STRING, consumer_group=CONSUMER_GROUP, eventhub_name=EVENT_HUB_NAME
    )
    try:
        with client:
            print("Listening for events...")
            client.receive(
                on_event=on_event,
                starting_position="-1",  # Start reading from the beginning of the stream
            )
    except KeyboardInterrupt:
        print("Stopped receiving.")

if __name__ == "__main__":
    main()
