# unittest 框架介绍
#  数据参数化

import unittest

def mul(x,y):
    z = x * y
    return z


class TestDemoAdd(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls) -> None:
    #     print('==========执行setupClass方法========')
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     print('==========执行teardownClass方法========')
    #
    # def setUp(self) -> None:
    #     print('==========执行setup方法========')
    #
    # def tearDown(self) -> None:
    #     print('==========执行teardown方法========')
    # @parameterized.expand([(16,4,4),(25,5,5),(88,11,7)])
    # def test_mul(self,c,a,b):
    #     res = mul(a,b)
    #     self.assertEqual(c,res)

    # def test_add07(self):
    #     print('==========执行add07=======')
    #     res1 =mul(3,4)
    #     self.assertEqual(12,res1)
    #
    def test_add10(self):
        print('==========执行add10=======')
        res2 = mul(4,7,)
        self.assertEqual(28, res2)
    #
    # def test_add09(self):
    #     print('==========执行add09=======')
    #     res3 = mul(5,5)
    #     self.assertEqual(25,res3)

if __name__ == '__main__':

    suite = unittest.TestSuite()
    suite.addTest(TestDemoAdd('test_mul'))
    #suite.addTest(TestDemoAdd('test_add02'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
    #unittest.main()

