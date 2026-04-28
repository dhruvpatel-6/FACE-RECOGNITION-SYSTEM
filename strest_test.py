import time
import random
import multiprocessing as mp
from collections import Counter

# ---------------- CONFIG ---------------- #

TOTAL_EVENTS = 100000
NUM_WORKERS = 8

VALID_USERS = [f"U{i:05d}" for i in range(1,5001)]

INVALID_USERS = [
    "BAD001",
    "12345",
    "UNKNOWN",
    "",
    None
]

METHODS = [
    "FACE",
    "RFID"
]

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

EVENT_WEIGHTS = {
    "valid":60,
    "invalid":15,
    "repeat":15,
    "failure":10
}

# ---------------------------------------- #

def random_event():

    event_type = random.choices(
        population=list(EVENT_WEIGHTS.keys()),
        weights=list(EVENT_WEIGHTS.values())
    )[0]

    if event_type == "valid":
        return {
            "type":"valid",
            "user_id":random.choice(VALID_USERS),
            "method":random.choice(METHODS)
        }

    elif event_type == "invalid":
        return {
            "type":"invalid",
            "user_id":random.choice(INVALID_USERS),
            "method":random.choice(
                ["FACE","RFID","UNKNOWN",""]
            )
        }

    elif event_type == "repeat":
        return {
            "type":"repeat",
            "user_id":random.choice(VALID_USERS)
        }

    else:
        return {
            "type":"failure",
            "failure":random.choice(
                FAILURE_EVENTS
            )
        }


def worker(worker_id, event_count, result_queue):

    stats = Counter()

    for i in range(event_count):

        event = random_event()

        stats[event["type"]] += 1

        # simulate duplicate storms
        if event["type"] == "repeat":
            if random.random() < 0.05:
                stats["duplicate_burst"] += 1

        # random latency spikes
        if random.random() < 0.001:
            time.sleep(0.2)

        # simulated system faults
        if random.random() < 0.0005:
            stats["simulated_faults"] += 1

        # optional progress every 20k events
        if i % 20000 == 0 and i != 0:
            print(
              f"Worker {worker_id} processed {i}"
            )

    result_queue.put(stats)


def main():

    print("="*70)
    print("HIAS MASSIVE STRESS TEST START")
    print("="*70)

    start = time.time()

    result_queue = mp.Queue()

    events_per_worker = TOTAL_EVENTS // NUM_WORKERS

    workers = []

    for i in range(NUM_WORKERS):

        p = mp.Process(
            target=worker,
            args=(
                i,
                events_per_worker,
                result_queue
            )
        )

        workers.append(p)
        p.start()

    combined = Counter()

    for _ in workers:
        partial = result_queue.get()
        combined.update(partial)

    for p in workers:
        p.join()

    end = time.time()

    elapsed = end - start

    eps = TOTAL_EVENTS / elapsed

    print("\n----- RESULTS -----")
    print(
        f"Total Events: {TOTAL_EVENTS}"
    )

    print(
        f"Workers: {NUM_WORKERS}"
    )

    print(
        f"Duration: {elapsed:.2f} sec"
    )

    print(
        f"Events/sec: {eps:.2f}"
    )

    print("\nEvent Breakdown")

    for k,v in combined.items():
        print(f"{k}: {v}")

    print("\nStress Grade")

    if eps > 10000:
        print("EXTREME LOAD PASSED")

    elif eps > 3000:
        print("HIGH LOAD PASSED")

    else:
        print("MODERATE LOAD ONLY")

    print("="*70)


if __name__ == "__main__":
    main()