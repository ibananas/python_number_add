# python_number_add

实现大数相加的两种算法.

- 直接相加法：由于python3具有无限精度的int类型，所以大数直接运算。

- 按位相加法：1.先让长度不一致的数补零到位数一致。2.然后按位相加，如果求和数值大于10，则只保留个位数，
并把数组的前一位加1。
如果进位后超出数组长度范围，则用插入操作。
