# unittest 框架介绍

import unittest

def add(x,y):
    z = x+y
    return z
'''
1.断言：预期结果和实际结果进行比较
常用断言：assertEqual(a,b)  a==b 
        assertin(a,b)    a  in  b
        assertGreater(a,b)  a>b
2.初始化和清除方法：
初始化方法--setUp()，每次运行测试方法前都需要先执行
        setUpClass()--  整个类在运行前，先运行
清空方法：tearDown(),每次运行测试方法后都需要执行
        tearDownClass(),整个类在运行后，执行一次
3.Testsuit:

addTest(test)--添加单个用例
addTest(tests)--添加一组用例

'''

class TestDemoAdd(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('==========执行setupClass方法========')
    @classmethod
    def tearDownClass(cls) -> None:
        print('==========执行teardownClass方法========')

    def setUp(self) -> None:
        print('==========执行setup方法========')

    def tearDown(self) -> None:
        print('==========执行teardown方法========')

    def test_add01(self):
        print('==========执行add01=======')
        self.assertEqual(7,add(3,4))

    def test_add02(self):
        print('==========执行add02=======')
        self.assertEqual(None,add(3, 4))

    def test_add03(self):
        print('==========执行add03=======')
        self.assertEqual(5.7,add(1.2,4.5))

if __name__ == '__main__':

    # suite = unittest.TestSuite()
    # suite.addTest(TestDemoAdd('test_add01'))
    # #suite.addTest(TestDemoAdd('test_add02'))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    unittest.main()

