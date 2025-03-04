from azure.eventhub import EventHubConsumerClient
from rich.live import Live
from rich.table import Table
import time
import threading

# Azure Event Hub details
event_hub_connection_str = "<CONNECTION_STRING>"
event_hub_name = "<EVENTHUB_NAME>"
consumer_group = "$Default"

# Message counter and timestamp
message_count = 0
last_reset_time = time.time()
lock = threading.Lock()

def create_table():
    table = Table(title="Azure Event Hub Real-Time Message Counter")
    table.add_column("Time", justify="center", style="cyan")
    table.add_column("Messages Per Second", justify="center", style="magenta")
    return table

def update_table():
    global message_count, last_reset_time
    table = create_table()
    current_time = time.strftime('%H:%M:%S')
    with lock:
        elapsed_time = time.time() - last_reset_time
        if elapsed_time >= 1:
            messages_per_second = message_count / elapsed_time
            table.add_row(current_time, f"{messages_per_second:.2f}")
            message_count = 0
            last_reset_time = time.time()
        else:
            table.add_row(current_time, "Waiting for messages...")
    return table

def on_event(partition_context, event):
    global message_count
    with lock:
        message_count += 1
    partition_context.update_checkpoint(event)

def consume_messages():
    client.receive(on_event=on_event, starting_position="@latest")

def main():
    with Live(create_table(), refresh_per_second=1) as live:
        while True:
            live.update(update_table())
            time.sleep(1)

# Event Hub Consumer Client
client = EventHubConsumerClient.from_connection_string(event_hub_connection_str, consumer_group, eventhub_name=event_hub_name)

# Run consumer and TUI in parallel
threading.Thread(target=consume_messages, daemon=True).start()
main()
