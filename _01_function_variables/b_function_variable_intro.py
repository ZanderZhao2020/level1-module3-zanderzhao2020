"""
Introduction to storing functions in variables
"""
import unittest


def surprise():
    return 'SURPRISE!'

# TODO 1) Change what is assigned into the func_1 variable so test_1 will pass
def func_1_func():
    return "SURPRISE!"
func_1 = func_1_func

# TODO 2) Change the return statement below so that test_2 will pass
def pizza_surprise():
    return "SURPRISE, here's a pizza!"

# TODO 3) Implement the birthday_surprise function so that test_3 will pass
def birthday_surprise(years_old):
    suffix = "th"
    years_old_str = str(years_old)
    if years_old_str.endswith("1") and years_old_str != "11":
        suffix = "st"
    elif years_old_str.endswith("2") and years_old_str != "12":
        suffix = "nd"
    elif years_old_str.endswith("3") and years_old_str != "13":
        suffix = "rd"
    return "SURPRISE, Happy " + years_old_str + suffix + " birthday!!!"

# TODO 4) Implement the surprise_guests function so that test_3 will pass
#  *HINT* You will have to add input parameters to the function
def surprise_guests(func, guests):
    final = ""
    for guest in guests:
        final += guest + " says " + func() + "\n"
    return final

# ================== DO NOT MODIFY THE CODE BELOW ============================

class WriteClassesTests(unittest.TestCase):

    def test_1(self):
        self.assertEqual('SURPRISE!', func_1())

    def test_2(self):
        func_2 = pizza_surprise
        self.assertEqual("SURPRISE, here's a pizza!", func_2())

    def test_3(self):
        func_3 = birthday_surprise
        self.assertEqual('SURPRISE, Happy 1st birthday!!!', func_3(1))
        self.assertEqual('SURPRISE, Happy 2nd birthday!!!', func_3(2))
        self.assertEqual('SURPRISE, Happy 3rd birthday!!!', func_3(3))
        self.assertEqual('SURPRISE, Happy 38th birthday!!!', func_3(38))

    def test_4(self):
        guests = ['Jerry', 'Summer', 'Yusef']
        expected_message =  guests[0] + ' says ' + 'SURPRISE!\n'
        expected_message += guests[1] + ' says ' + 'SURPRISE!\n'
        expected_message += guests[2] + ' says ' + 'SURPRISE!\n'
        self.assertEqual(expected_message, surprise_guests(surprise, guests))

        expected_message =  guests[0] + ' says ' + "SURPRISE, here's a pizza!\n"
        expected_message += guests[1] + ' says ' + "SURPRISE, here's a pizza!\n"
        expected_message += guests[2] + ' says ' + "SURPRISE, here's a pizza!\n"
        self.assertEqual(expected_message, surprise_guests(pizza_surprise, guests))

if __name__ == '__main__':
    unittest.main()
