# 测试报告
import unittest
from HTMLTestRunner import HTMLTestRunner
# 定义一个测试报告的文件
report_file = 'test_report.html'

# 创建一个套件
suite = unittest.TestLoader().discover(start_dir='.',pattern='test*.py')

# 生成一个runner
with open(report_file,'wb') as f:    #  Wb代表写入的是二进制文件，W表示写入文本文件
    runner = HTMLTestRunner(f,title='测试报告',description='v1.2')
    runner.run(suite)


