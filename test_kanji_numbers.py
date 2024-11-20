import unittest
from io import StringIO
import sys


kanji_numbers = {
    3: '三', 6: '六', 9: '九', 12: '十二', 13: '十三', 15: '十五', 
    18: '十八', 21: '二十一', 23: '二十三', 24: '二十四',
    27: '二十七', 30: '三十', 31: '三十一', 32: '三十二', 33: '三十三',
    34: '三十四', 35: '三十五', 36: '三十六', 37: '三十七', 38: '三十八',
    39: '三十九'
}

def print_numbers():
    result = []
    for i in range(1, 41):
        if i % 3 == 0 or '3' in str(i):
            result.append(kanji_numbers.get(i, i))  
        else:
            result.append(i)  
    return result


class TestKanjiNumbers(unittest.TestCase):

    def test_print_numbers(self):
        expected_output = [
            1, 2, '三', 4, 5, '六', 7, 8, '九', 10, 11, '十二', '十三', '十五', 
            14, '十八', '二十一', '二十三', '二十四', '二十七', '三十', '三十一', 
            '三十二', '三十三', '三十四', '三十五', '三十六', '三十七', '三十八', '三十九', 40
        ]
        
        captured_output = StringIO()
        sys.stdout = captured_output

        print_numbers()

        output = captured_output.getvalue().strip().split("\n")
        self.assertEqual(output, [str(item) for item in expected_output])

    
        sys.stdout = sys.__stdout__

if __name__ == "__main__":
    unittest.main()

