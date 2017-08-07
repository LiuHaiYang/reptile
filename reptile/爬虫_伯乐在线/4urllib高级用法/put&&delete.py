#http协议有六种请求方法，get,head,put,delete,post,options，
#我们有时候需要用到PUT方式或者DELETE方式请求
#PUT：这个方法比较少见。HTML表单也不支持这个。
#本质上来讲， PUT和POST极为相似，都是向服务器发送数据，
#但它们之间有一个重要区别，PUT通常指定了资源的存放位置，
#而POST则没有，POST的数据存放位置由服务器自己决定。
#DELETE：删除某一个资源。基本上这个也很少见，
#不过还是有一些地方比如amazon的S3云服务里面就用的这个方法来删除资源。

import urllib2
request = urllib2.Request(uri, data=data)
request.get_method = lambda: 'PUT' # or 'DELETE'
response = urllib2.urlopen(request)