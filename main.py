class CheckResult:
    EQUAL = "EQUAL"
    SUBLIST = "SUBLIST"
    SUPERLIST = "SUPERLIST"
    UNEQUAL = "UNEQUAL"


class SublistPython:

    @staticmethod
    def check_sublist(list1, list2) -> str:
        if list1 == list2:
            return CheckResult.EQUAL
        elif SublistPython.is_sublist(list1, list2):
            return CheckResult.SUBLIST
        elif SublistPython.is_sublist(list2, list1):
            return CheckResult.SUPERLIST
        else:
            return CheckResult.UNEQUAL

    @staticmethod
    def is_sublist(list1, list2) -> bool:
        len1 = len(list1)
        len2 = len(list2)

        if len1 > len2:
            return False

        for i in range(len2 - len1 + 1):
            if list1 == list2[i:i + len1]:
                return True

        return False


# Testing the class
list1 = [1, 2]
list2 = [1, 2]
assert SublistPython.check_sublist(list1, list2) == CheckResult.EQUAL

list1 = [1]
list2 = [1, 2]
assert SublistPython.check_sublist(list1, list2) == CheckResult.SUBLIST

list1 = [1, 2]
list2 = [1]
assert SublistPython.check_sublist(list1, list2) == CheckResult.SUPERLIST

list1 = [1, 2]
list2 = [2, 1]
assert SublistPython.check_sublist(list1, list2) == CheckResult.UNEQUAL

list1 = []
list2 = []
assert SublistPython.check_sublist(list1, list2) == CheckResult.EQUAL

list1 = []
list2 = [1, 2, 3]
assert SublistPython.check_sublist(list1, list2) == CheckResult.SUBLIST

list1 = [1, 2, 3]
list2 = []
assert SublistPython.check_sublist(list1, list2) == CheckResult.SUPERLIST

print("All assertions passed!")
