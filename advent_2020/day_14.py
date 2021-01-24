from typing import List, Literal, Tuple, Union, Dict

"""
Bitmask to init program
values and memory addresses are 36bit unsigned ints
bitmask str of 36 bits - biggest bit at the left
"""

ActionTypes = Literal['SETMASK', 'SETMEM']
SET_MASK: ActionTypes = 'SETMASK'
SET_MEM: ActionTypes = 'SETMEM'
MemorySetter = Tuple[int, int]
Mask = str

ProgramSteps = List[Tuple[ActionTypes, Union[Mask, MemorySetter]]]

MemoryAddressValues = Dict[int, int]


def combine_num_with_mask_v2(mask: str, original_addr: int) -> str:
    original_addr_bit_str = bin(original_addr)[2:]
    output = ""
    for i, c in enumerate(mask):
        addr_bit_str_indx = len(original_addr_bit_str) - len(mask) + i
        if addr_bit_str_indx >= 0 and c == "0":
            output += original_addr_bit_str[addr_bit_str_indx]
        else:
            output += c
    return output


def get_memory_addresses_v2_mask(mask: str, original_addr: int) -> List[int]:
    combined_bit_str = combine_num_with_mask_v2(mask, original_addr)
    # generate floating combinations from combined string
    floating_combos = [combined_bit_str]
    did_a_replace = "X" in combined_bit_str
    finished_addrs = []
    while did_a_replace:
        new_combos = []
        did_a_replace = False
        for addr in floating_combos:
            if "X" in addr:
                did_a_replace = True
                new_combos.append(addr.replace("X", "0", 1))
                new_combos.append(addr.replace("X", "1", 1))
            else:
                finished_addrs.append(addr)
        floating_combos = new_combos
    return [int(c, 2) for c in finished_addrs]


def combine_num_with_mask(mask: str, base_10_num: int) -> int:
    """
    the behaviour we want here is for X to be replaced with any values of the num
    but any 0s in the mask should take precedence over 1s in the num. Lets call this operation #
    then:
    1XX0X # 10011 -> 10001
    ===
    10000 | 10011 -> 10011 (a)
    preserve the 0s from the mask
    00010 & 10011 -> 00010 (b)
    a ^ b -> 10001
    :param mask:
    :param base_10_num:
    :return:
    """
    mask_bin_0_replace = int(mask.replace("X", "0"), 2)
    mask_bin_not_then_0_replace = int(
        mask.replace("1", "Y").replace("0", "Z").replace("X", "0").replace("Y", "0").replace("Z", "1"), 2)
    return (mask_bin_0_replace | base_10_num) ^ (mask_bin_not_then_0_replace & base_10_num)


def execute_program(steps: ProgramSteps, version: Literal[1, 2] = 1) -> MemoryAddressValues:
    current_mask = None
    memory_address_values = {}
    for action_type, action in steps:
        if action_type == SET_MASK:
            current_mask = action
            continue
        # we need a mask to do mem sets
        if current_mask is None:
            continue
        memory_addr, memory_set_number = action
        if version == 1:
            memory_address_values[memory_addr] = combine_num_with_mask(current_mask, memory_set_number)
        else:
            new_memory_addresses = get_memory_addresses_v2_mask(current_mask, memory_addr)
            memory_address_values.update({addr: memory_set_number for addr in new_memory_addresses})

    return memory_address_values


def parse_input_to_steps(input_text: str) -> ProgramSteps:
    steps = []
    for line in input_text.split("\n"):
        if not line:
            continue
        if "mask" in line:
            steps.append((SET_MASK, line.split("=")[-1].strip()))
        else:
            addr, val = line.split("=")
            steps.append((
                SET_MEM,
                (
                    int(addr.split("[")[-1].split("]")[0].strip()),
                    int(val.strip()),
                )
            ))
    return steps


def a(steps: ProgramSteps):
    memory_addr_values = execute_program(steps)
    return sum(memory_addr_values.values())


def b(steps: ProgramSteps):
    memory_addr_values = execute_program(steps, version=2)
    return sum(memory_addr_values.values())


if __name__ == "__main__":
    with open("advent_2020/inputs/14") as f:
        step_text = parse_input_to_steps(f.read())

    print("a)", a(step_text))
    print("b)", b(step_text))
