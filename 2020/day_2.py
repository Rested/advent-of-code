from dataclasses import dataclass
from typing import List


@dataclass
class PasswordEntry:
    # policy
    char_low: int
    char_high: int
    character: str

    password: str

    def is_valid(self, policy_type: str):
        if policy_type == "a" and self.char_low <= self.password.count(self.character) <= self.char_high:
            return True
        if policy_type == "b" and \
                ((self.password[self.char_low - 1] == self.character and self.password[
                    self.char_high - 1] != self.character)
                 or (self.password[self.char_high - 1] == self.character and self.password[
                            self.char_low - 1] != self.character)):
            return True
        return False


def a(entries: List[PasswordEntry]):
    return len([0 for entry in entries if entry.is_valid("a")])


def b(entries: List[PasswordEntry]):
    return len([0 for entry in entries if entry.is_valid("b")])


def parse_entry(line: str):
    password_policy, password_text = line.split(":")
    num_chars, char = password_policy.split()
    min_num, max_num = (int(x) for x in num_chars.split("-"))
    return PasswordEntry(char_low=min_num, char_high=max_num, character=char, password=password_text.strip())


if __name__ == '__main__':
    with open("inputs/2") as f:
        password_lines = f.read().split("\n")
    password_entries = []
    for line in password_lines:
        if line:
            password_entries.append(parse_entry(line))

    print("total entries:", len(password_entries))

    print("a)", a(password_entries))
    print("b)", b(password_entries))
