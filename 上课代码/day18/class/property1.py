"""
@File    :   property1.py
@Author  :   zhouJunFeng    
@Contact :   zx051225@163.com
@Modify Time :   2019/12/14 20:49
"""

# 受保护,公有私有属性的访问
class A:
    _p = '1_protected_attr'
    p = '1_public_attr'
    __p = '1_private_attr'


num = 1
_num = 1
__num = 1
