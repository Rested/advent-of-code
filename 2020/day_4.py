from typing import Dict, List
import re

REQUIRED_FIELDS = {
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    "cid",
}


def parse_passports(passports_text: str) -> List[Dict[str, str]]:
    parsed_ports = []
    for passport in passports_text.split("\n\n"):
        if passport:
            passport_dict = {}
            data = passport.replace("\n", " ").split()
            for datum in data:
                field, value = datum.split(":")
                passport_dict[field.strip()] = value.strip()
            parsed_ports.append(passport_dict)
    return parsed_ports


def a(parsed_ports: List[Dict[str, str]]):
    required_fields = REQUIRED_FIELDS.copy()
    required_fields.remove("cid")
    return len([0 for pp in parsed_ports if set(pp.keys()).issuperset(required_fields)])


def length_validate(pp, field, length):
    return len(pp[field]) == length


def range_validate(pp, field, min_val, max_val):
    val = int(pp[field])
    return min_val <= val <= max_val


def regex_validate(pp, field, regex):
    pattern = re.compile(regex)
    return pattern.match(pp[field])


VALID_EYE_COLOURS = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}


def b(parsed_ports: List[Dict[str, str]]):
    required_fields = REQUIRED_FIELDS.copy()
    required_fields.remove("cid")
    valid_count = 0
    for pp in parsed_ports:
        if not set(pp.keys()).issuperset(required_fields):
            continue
        # do length based validations
        length_criteria = (
            ("byr", 4),
            ("iyr", 4),
            ("eyr", 4),
            ("hcl", 7),
            ("pid", 9),
        )
        failed_validation = False
        for criterion in length_criteria:
            if not length_validate(pp, *criterion):
                print(
                    f"failed due to length of field {criterion[0]} not being {criterion[1]} but {len(pp[criterion[0]])}")
                failed_validation = True
                break
        if failed_validation:
            continue

        # do range based validation
        range_criteria = (
            ("byr", 1920, 2002),
            ("iyr", 2010, 2020),
            ("eyr", 2020, 2030),
        )
        for criterion in range_criteria:
            if not range_validate(pp, *criterion):
                print(f"failed due to {criterion[0]}: {pp[criterion[0]]} not in range {criterion[1]}-{criterion[2]}")
                failed_validation = True
                break
        if failed_validation:
            continue

        # do regex based validation
        regex_criteria = (
            ("hcl", "#[0-9a-f]{6}"),
            ("pid", "[0-9]{9}")
        )
        for criterion in regex_criteria:
            if not regex_validate(pp, *criterion):
                print(f"failed due to {criterion[0]}: {pp[criterion[0]]} not matching regex {criterion[1]}")
                failed_validation = True
                break
        if failed_validation:
            continue

        # eye colour validate
        if pp["ecl"] not in VALID_EYE_COLOURS:
            print(f"failed due to eye colour {pp['ecl']} not in {VALID_EYE_COLOURS}")
            continue

        # height validation
        units = pp["hgt"][-2:]
        num = int(pp["hgt"][:-2])
        if units == "cm":
            if num < 150 or num > 193:
                print(f"failed height validation due to height in inches {num} not in range 59-76")
                continue
        elif units == "in":
            if num < 59 or num > 76:
                print(f"failed height validation due to height in inches {num} not in range 59-76")
                continue
        else:
            print(f"failed due to wrong unit {units}")
            continue
        # valid!!
        print("valid!")
        valid_count += 1
    return valid_count


if __name__ == "__main__":
    with open("inputs/4") as f:
        real_parsed_ports = parse_passports(f.read())

    print("a)", a(parsed_ports=real_parsed_ports))
    print("b)", b(parsed_ports=real_parsed_ports))
