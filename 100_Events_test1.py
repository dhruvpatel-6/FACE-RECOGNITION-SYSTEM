import time
import random

VALID_USERS = [f"U{i:04d}" for i in range(1, 101)]
INVALID_USERS = ["BAD001", "12345", "UNKNOWN", "", None]

METHODS = ["FACE", "RFID"]
FAILURE_EVENTS = [
    "EMERGENCY",
    "FIRE",
    "SYSTEM_FAILURE",
    "POWER_FAILURE",
    "NETWORK_FAILURE",
    "RELAY_FAILURE",
    "GATE_JAM",
    "INTRUSION_DETECTED"
]

print("=" * 70)
print("HIAS 100 EVENT FAILURE + LOAD SIMULATION STARTED")
print("=" * 70)

for event_no in range(1, 101):

    # Decide event type
    event_type = random.choices(
        ["valid", "invalid", "repeat", "failure"],
        weights=[60, 15, 15, 10]
    )[0]

    # ---------------- VALID ----------------
    if event_type == "valid":
        user_id = random.choice(VALID_USERS)
        method = random.choice(METHODS)

        print(f"[{event_no}] VALID | {user_id} | {method}")
        print("✅ ALLOW → Relay ON → Gate Open")

    # ---------------- INVALID ----------------
    elif event_type == "invalid":
        user_id = random.choice(INVALID_USERS)
        method = random.choice(["FACE", "RFID", "", "UNKNOWN"])

        print(f"[{event_no}] INVALID | {user_id} | {method}")
        print("❌ DENY → Invalid / Unauthorized")

    # ---------------- REPEAT ----------------
    elif event_type == "repeat":
        user_id = random.choice(VALID_USERS)

        print(f"[{event_no}] REPEATED SCAN | {user_id}")
        print("🔁 Duplicate scan detected")

    # ---------------- FAILURE EVENTS ----------------
    else:
        failure = random.choice(FAILURE_EVENTS)

        print(f"[{event_no}] EVENT | {failure}")

        if failure == "EMERGENCY":
            print("🚨 Emergency mode activated")

        elif failure == "FIRE":
            print("🔥 Fire alarm triggered")

        elif failure == "SYSTEM_FAILURE":
            print("⚠️ System failure detected")

        elif failure == "POWER_FAILURE":
            print("🔌 Switched to backup power")

        elif failure == "NETWORK_FAILURE":
            print("📡 Offline mode enabled")

        elif failure == "RELAY_FAILURE":
            print("⚠️ Relay malfunction")

        elif failure == "GATE_JAM":
            print("🚪 Gate jam detected")

        elif failure == "INTRUSION_DETECTED":
            print("🚨 Security breach detected")

    print("-" * 70)

    # small delay
    time.sleep(0.05)

print("\n✅ 100 EVENT TEST COMPLETED")
print("=" * 70)