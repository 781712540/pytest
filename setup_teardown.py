import pytest

# 模块中的方法
def setup_module():
    print("setup_module：整个test_module.py模块只执行一次")
def teardown_module():
    print("teardown_module：整个test_module.py模块只执行一次")
# 测试模块中的用例1

# 函数级
def setup_function():
    print("setup_function方法执行")

def teardown_function():
    print("teardown_function方法执行")

def test_one():
    print("test_one 函数执行")
    assert 1 == 1

def test_two():
    print("test_two函数执行")
    assert "o" in "love"

# 类级别
class TestClass:

    # 类级别
    def setup_class(self):  # 仅类开始之前执行一次
        print("---setup_class---")

    def teardown_class(self):
        print("---teardown_class---")

    # 方法级
    def setup(self):
        print('setup')

    def teardown(self):
        print('teardown')

    # 方法级
    def setup_method(self):
        print('setup_method')

    def teardown_method(self):
        print('teardown_method')

    def test_a(self):
        print("test_a,  方法")

    def test_b(self):
        print("test_b, 方法")

    def test_clsa(cls):
        print("test_clsa,  类方法")

    def test_clsb(cls):
        print("test_clsb, 类方法")

    @staticmethod
    def test_test_statica():
        print("test_statica,  静态方法")

    @staticmethod
    def test_test_staticb():
        print("test_staticb, 静态方法")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "-ra", "setup_teardown.py"])
