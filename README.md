# 🚀 Azure Event Hub Real-Time Message Counter

This project **monitors real-time messages** arriving in **Azure Event Hub** and **displays live message counts per second** in a **Terminal UI (TUI)**. 

## 📌 Features
✅ **Real-time message tracking** from Azure Event Hub  
✅ **Terminal UI (TUI) dashboard** powered by `rich`  
✅ **Live messages per second count**  
✅ **Minimal setup & lightweight**  
✅ **Works with any Event Hub source (IoT, logs, telemetry, etc.)**  

1️⃣ Clone the Repo:
git clone https://github.com/BanuVinay1/eventhub-message-counter.git
cd eventhub-message-counter

2️⃣ Create a Virtual Environment (Optional but Recommended):
python -m venv iot_env
iot_env\Scripts\activate     # Windows

3️⃣ Install Dependencies:
pip install -r requirements.txt

4️⃣ Set Up Azure Event Hub Connection:
Go to Azure Portal → Event Hubs.
Copy your Event Hub connection string from Shared Access Policies.
Update event_hub_tui.py: event_hub_connection_str = "YOUR_EVENT_HUB_CONNECTION_STRING"

5️⃣ Run the Message Counter:
python event_hub_tui.py

📊 Example Output:

┏━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┓
┃   Time   ┃ Messages Per Second ┃
┡━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━┩
│ 16:18:16 │        25.00        │
│ 16:18:17 │        32.00        │
│ 16:18:18 │        18.00        │
└──────────┴─────────────────────┘


🔥 How It Works
1️⃣ The script connects to Azure Event Hub and listens for incoming messages.
2️⃣ It counts messages per second and updates the TUI dashboard in real time.
3️⃣ The data refreshes every second, providing a live message ingestion rate.

⚙️ Configuration
Modify these settings in event_hub_tui.py:
event_hub_connection_str = "YOUR_EVENT_HUB_CONNECTION_STRING"
consumer_group = "$Default"  # Change if using a custom consumer group

🏷️ Requirements
This project uses:
Python 3.8+
azure-eventhub for connecting to Azure Event Hub
rich for the TUI dashboard


📌 Notes
This project may incur Azure costs if left running for extended periods.
If no messages are received, the script will display 0.00 messages per second.
Stop the script anytime using CTRL+C.

📜 License
MIT License. Free to use & modify.

🤝 Contributing
Pull requests are welcome! Feel free to submit issues or suggestions.


