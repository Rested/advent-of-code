from typing import Tuple, Union, List

BusIds = List[Union[int, None]]


def parse_bus_times(input_text: str) -> Tuple[int, BusIds]:
    earliest_depart_timestamp, bus_ids, *_ = input_text.split("\n")
    return int(earliest_depart_timestamp), [int(x.strip()) if x.strip() != "x" else None for x in bus_ids.split(",")]


def get_wait_time_for_bus_id(earliest_depart_timestamp, bus_id):
    rem = earliest_depart_timestamp % bus_id
    return bus_id - rem if rem != 0 else 0


def get_earliest_bus(earliest_depart_timestamp: int, bus_ids: BusIds) -> Tuple[int, int]:
    best_bus_id = None
    best_wait_time = None
    for bus_id in bus_ids:
        if bus_id:
            wait_time = get_wait_time_for_bus_id(earliest_depart_timestamp, bus_id)
            if not best_bus_id and not best_wait_time:
                best_bus_id = bus_id
                best_wait_time = wait_time
                continue
            if best_wait_time > wait_time:
                best_bus_id = bus_id
                best_wait_time = wait_time

    return best_bus_id, best_wait_time


def get_earliest_timestamp_for_sequential_departures(bus_ids: BusIds) -> int:
    timestamp = 0
    max_ts = 10_000_000_000_000
    max_depth = 0
    bus_id_encounters_tracker = {
        bid: {"count": 0, "first_encounter_ts": None, "encounter_period": None} for bid in bus_ids
    }
    increment = bus_ids[0]
    bus_id_indxs = [(i, bid) for i, bid in enumerate(bus_ids) if bid is not None]
    x = 1
    offset = 0
    next_bid_indx = bus_id_indxs[0]
    while True:
        for i, bus_id in bus_id_indxs:
            if get_wait_time_for_bus_id(timestamp, bus_id) != i:
                break
            bus_id_encounters_tracker[bus_id]["count"] += 1
            if bus_id_encounters_tracker[bus_id]["first_encounter_ts"] is None:
                bus_id_encounters_tracker[bus_id]["first_encounter_ts"] = timestamp
                print(f"first time encountered {bus_id} is at {timestamp}, offset {i} ({timestamp + i})")
                max_depth += 1
            elif bus_id_encounters_tracker[bus_id]["encounter_period"] is None:
                bus_id_encounters_tracker[bus_id]["encounter_period"] = timestamp - bus_id_encounters_tracker[bus_id][
                    "first_encounter_ts"]
                print(
                    f"got encounter period for bus id {bus_id} of {bus_id_encounters_tracker[bus_id]['encounter_period']}")
                if bus_id_encounters_tracker[bus_id]["encounter_period"] > increment:
                    print(f"increased increment from {increment} to {bus_id_encounters_tracker[bus_id]['encounter_period']}")
                    increment = bus_id_encounters_tracker[bus_id]["encounter_period"]

        else:
            return timestamp
        # prevent infinite loop
        if timestamp > max_ts:
            break

        timestamp += increment


def a(input_text: str):
    earliest_depart_timestamp, bus_ids = parse_bus_times(input_text)
    best_bus_id, best_wait_time = get_earliest_bus(earliest_depart_timestamp, bus_ids)
    return best_bus_id * best_wait_time


if __name__ == "__main__":
    with open("advent_2020/inputs/13") as f:
        inputs = f.read()

    print("a)", a(inputs))
    print("b)", get_earliest_timestamp_for_sequential_departures(parse_bus_times(inputs)[1]))
