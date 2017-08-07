#re.search(pattern, string[, flags])
#导入re模块
#search方法与match方法极其类似，
#区别在于match()函数只检测re是不是在string的开始位置匹配，
#search()会扫描整个string查找匹配，
#match（）只有在0位置匹配成功的话才有返回，
#如果不是开始位置匹配成功的话，match()就返回None。
#同样，search方法的返回对象同样match()返回对象的方法和属性
import re
 
# 将正则表达式编译成Pattern对象
pattern = re.compile(r'world')
# 使用search()查找匹配的子串，不存在能匹配的子串时将返回None
# 这个例子中使用match()无法成功匹配
match = re.search(pattern,'hello world!')
if match:
    # 使用Match获得分组信息
    print match.group()
### 输出 ###
# world