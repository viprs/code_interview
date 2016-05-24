#sed命令使用方法

## 替换字符串
把其中的my字符串替换成Hao Chen's，下面的语句应该很好理解（s表示替换命令，/my/表示匹配my，/Hao Chen’s/表示把匹配替换成Hao Chen's，/g 表示一行上的替换所有的匹配

`sed "s/my/Hao Chen's/g" test_data.txt`

