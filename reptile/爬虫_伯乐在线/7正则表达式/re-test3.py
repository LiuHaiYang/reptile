#re.split(pattern, string[, maxsplit])

#按照能够匹配的子串将string分割后返回列表。
#maxsplit用于指定最大分割次数，不指定将全部分割。

import re

pattern = re.compile(r'\d+')
print re.split(pattern,'one1two2three3four4')

### 输出 ###
# ['one', 'two', 'three', 'four', '']
