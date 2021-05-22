from enum import Enum


class TypeOFMatch(Enum):
    Under5 = 5
    Under10 = 10
    Under16 = 16
    Under32 = 32
    Under64 = 64


def correctTypeFromLength(length):
    if length == 2:
        return TypeOFMatch(2)
    if length <= 5:
        return TypeOFMatch(5)
    if length <= 10:  # (5,10]
        return TypeOFMatch(10)
    if length <= 16:  # (10,16]
        return TypeOFMatch(16)
    if length <= 32:  # (16,32]
        return TypeOFMatch(32)
    if length <= 64:
        return TypeOFMatch(64)