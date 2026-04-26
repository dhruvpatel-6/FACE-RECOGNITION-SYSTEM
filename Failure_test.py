import time

test_cases = [
    # Normal / Input failures
    {"user_id": "", "method": "FACE"},
    {"user_id": None, "method": "RFID"},
    {"user_id": "123", "method": ""},
    {"user_id": "!!!@@@", "method": "FACE"},
    {"user_id": "U0001", "method": "UNKNOWN"},
    {"user_id": "U0001"},
    {"method": "FACE"},
    {},
    {"user_id": "U0001", "method": "FACE"},
    {"user_id": "U0001", "method": "FACE"},  # repeated

    # Emergency cases
    {"event": "EMERGENCY"},
    {"event": "FIRE"},
    {"event": "SYSTEM_FAILURE"},
    {"event": "POWER_FAILURE"},
    {"event": "NETWORK_FAILURE"},
    {"event": "RELAY_FAILURE"},
    {"event": "GATE_JAM"},
    {"event": "INTRUSION_DETECTED"},
]

print("=" * 60)
print("HIAS FAILURE + EMERGENCY TESTING STARTED")
print("=" * 60)

for i, test in enumerate(test_cases, start=1):
    print(f"\nTest {i}: {test}")

    # ---------- Emergency events ----------
    if "event" in test:
        event = test["event"]

        if event == "EMERGENCY":
            print("🚨 EMERGENCY MODE ACTIVATED")
            print("→ Unlock emergency exits")
            print("→ Send alert to dashboard")
            print("→ Log emergency event")

        elif event == "FIRE":
            print("🔥 FIRE ALERT TRIGGERED")
            print("→ Open safety exits")
            print("→ Trigger buzzer/alarm")
            print("→ Notify control room")

        elif event == "SYSTEM_FAILURE":
            print("⚠️ SYSTEM FAILURE")
            print("→ Switch to safe mode")
            print("→ Notify maintenance team")

        elif event == "POWER_FAILURE":
            print("🔌 POWER FAILURE")
            print("→ Switch to backup power")
            print("→ Log outage event")

        elif event == "NETWORK_FAILURE":
            print("📡 NETWORK FAILURE")
            print("→ Use offline local validation")
            print("→ Queue logs for sync later")

        elif event == "RELAY_FAILURE":
            print("⚠️ RELAY FAILURE")
            print("→ Gate trigger failed")
            print("→ Raise maintenance alert")

        elif event == "GATE_JAM":
            print("🚪 GATE JAM DETECTED")
            print("→ Stop motor")
            print("→ Send operator alert")

        elif event == "INTRUSION_DETECTED":
            print("🚨 INTRUSION DETECTED")
            print("→ Lock secure areas")
            print("→ Trigger alarm")
            print("→ Notify security")

    # ---------- Access validation ----------
    else:
        if "user_id" not in test or "method" not in test:
            print("❌ FAIL: Missing required field")

        elif not test["user_id"]:
            print("❌ FAIL: Invalid user_id")

        elif test["method"] not in ["FACE", "RFID"]:
            print("❌ FAIL: Invalid method")

        elif not str(test["user_id"]).startswith("U"):
            print("❌ FAIL: Unauthorized / Unknown user")

        else:
            print("✅ PASS: Valid access")
            print("→ ALLOW")
            print("→ Relay Trigger")
            print("→ Gate Open")
            print("→ Log Entry")

    print("-" * 60)
    time.sleep(1)

print("\n✅ ALL FAILURE TESTS COMPLETED")
print("=" * 60)