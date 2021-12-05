from typing import List

def number_of_increases(depth_measurements: List[int]) -> int:
    depth_increase_count = 0
    for i, measurement in enumerate(depth_measurements[:-1]):
        match (measurement, depth_measurements[i+1]):
            case (shallower, deeper) if shallower < deeper:
                depth_increase_count += 1
            case _:
                continue
    return depth_increase_count


def sliding_window(depth_measurements: List[int]) -> int:
    depth_increase_count = 0
    for i, measurement in enumerate(depth_measurements[:-3]):
        match depth_measurements[i+1:i+4]:
            case (second, third, fourth) if sum((measurement, second, third)) < sum((second, third, fourth)):
                depth_increase_count += 1
            case _:
                continue
    return depth_increase_count

def run(input_text: str):
    measurements = [int(l) for l in input_text.split("\n")]
    part_1 = number_of_increases(measurements)
    part_2 = sliding_window(measurements)
    return part_1, part_2