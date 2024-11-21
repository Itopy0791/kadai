import unittest

kanji_numbers = {
    3: '三', 6: '六', 9: '九', 12: '十二', 13: '十三', 15: '十五', 
    18: '十八', 21: '二十一', 23: '二十三', 24: '二十四',
    27: '二十七', 30: '三十', 31: '三十一', 32: '三十二', 33: '三十三',
    34: '三十四', 35: '三十五', 36: '三十六', 37: '三十七', 38: '三十八',
    39: '三十九'
}

class TestKanjiNumbers(unittest.TestCase):
    def test_print_numbers(self):
        expected_output = [
            '1', '2', '三', '4', '5', '六', '7', '8', '九', '10',
            '11', '十二', '十三', '14', '十五', '16', '17', '十八',
            '19', '20', '二十一', '22', '二十三', '二十四', '25', 
            '26', '二十七', '28', '29', '三十', '三十一', '三十二', 
            '三十三', '三十四', '三十五', '三十六', '三十七', '三十八', 
            '三十九', '40'
        ]

        output = []
        for i in range(1, 41):
            if i % 3 == 0 or '3' in str(i):
                output.append(str(kanji_numbers.get(i, i)))  
            else:
                output.append(str(i))  

        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()


