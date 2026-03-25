#用unittest库测试
import unittest    #引入python自带的测试库unittest
from shopping_list import ShoppingList    #从你写的shopping_list.py里，把ShoppingList这个类导入过来，没有这句测试文件就不知道是啥

class TestShoppingList(unittest.TestCase):    #现在要跑一个测试类，继承 unittest.TestCase（规定写法）
    def test_get_item_count(self):    #函数名以 test_ 开头才会被当成测试执行
        shopping_list = ShoppingList({"纸巾": 8, "帽子": 30, "拖鞋": 15})    #造一个测试对象
        self.assertEqual(shopping_list.get_item_count(), 3)    #断言（assert） = 我来检查你对不对  意思就是我认为shopping_list.get_item_count()应该等于3，如果不等于你就报错


    def test_get_total_price(self):
        shopping_list = ShoppingList({"纸巾": 8, "帽子": 30, "拖鞋": 15})
        self.assertEqual(shopping_list.get_total_price(), 53)

"""能看到我们一直是在重复的创造测试对象
shopping_list = ShoppingList({"纸巾": 8, "帽子": 30, "拖鞋": 15})
可以采用 setUp 的方法"""

class TestShoppingList(unittest.TestCase):
    def setUp(self):
        self.shopping_list = ShoppingList({"纸巾": 8, "帽子": 30, "拖鞋": 15})

    def test_get_item_count(self):
        self.assertEqual(self.shopping_list.get_item_count(), 3)


    def test_get_total_price(self):
        self.assertEqual(self.shopping_list.get_total_price(), 53)