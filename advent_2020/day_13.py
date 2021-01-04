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
    max_ts = 100_000_000
    while True:
        for i, bus_id in enumerate(bus_ids):
            if bus_id is not None and get_wait_time_for_bus_id(timestamp, bus_id) != i:
                break
        else:
            return timestamp
        if timestamp % 10_000:
            print(timestamp, i)
        if timestamp > max_ts:
            break
        timestamp += bus_ids[0]  # a bit cheeky because could be x but it isnt so it is what it is

def a(input_text: str):
    earliest_depart_timestamp, bus_ids = parse_bus_times(input_text)
    best_bus_id, best_wait_time = get_earliest_bus(earliest_depart_timestamp, bus_ids)
    return best_bus_id * best_wait_time


if __name__ == "__main__":
    with open("advent_2020/inputs/13") as f:
        inputs = f.read()

    print("a)", a(inputs))
    print("b)", get_earliest_timestamp_for_sequential_departures(parse_bus_times(inputs)[1]))
