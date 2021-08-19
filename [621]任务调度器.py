# 给你一个用字符数组 tasks 表示的 CPU 需要执行的任务列表。其中每个字母表示一种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1 个
# 单位时间内执行完。在任何一个单位时间，CPU 可以完成一个任务，或者处于待命状态。 
# 
#  然而，两个 相同种类 的任务之间必须有长度为整数 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。 
# 
#  你需要计算完成所有任务所需要的 最短时间 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：tasks = ["A","A","A","B","B","B"], n = 2
# 输出：8
# 解释：A -> B -> (待命) -> A -> B -> (待命) -> A -> B
#      在本示例中，两个相同类型任务之间必须间隔长度为 n = 2 的冷却时间，而执行一个任务只需要一个单位时间，所以中间出现了（待命）状态。 
# 
#  示例 2： 
# 
#  
# 输入：tasks = ["A","A","A","B","B","B"], n = 0
# 输出：6
# 解释：在这种情况下，任何大小为 6 的排列都可以满足要求，因为 n = 0
# ["A","A","A","B","B","B"]
# ["A","B","A","B","A","B"]
# ["B","B","B","A","A","A"]
# ...
# 诸如此类
#  
# 
#  示例 3： 
# 
#  
# 输入：tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
# 输出：16
# 解释：一种可能的解决方案是：
#      A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> (待命) -> (待命) -> A -> (待
# 命) -> (待命) -> A
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= task.length <= 104 
#  tasks[i] 是大写英文字母 
#  n 的取值范围为 [0, 100] 
#  
#  Related Topics 贪心 数组 哈希表 计数 排序 堆（优先队列） 
#  👍 697 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = collections.Counter(tasks)
        # 次数最多任务的次数
        maxexe = max(freq.values())
        # 次数最多任务的数量
        maxsimc = sum(1 for i in freq.values() if i==maxexe)
        """
        公式：(maxexe-1)*(n+1)+maxsimc
        把任务队列想成一个maxexe*(n+1)的矩阵，为什么n+1:因为下次执行该任务需要间隔n,执行该任务就是n+1
        (maxexe-1)*(n+1)就是矩阵除了最后一行的数量，即时间，
        +maxsimc就是加上最后一行次数最多任务的数量
        其余的任务就填充在(maxexe-1)*(n+1-maxsimc)里面，
        如果填充到了最后一行(需要等待时间的格子填满了)，那么任务就没有需要等待的时间了，即执行时间len(tasks)
        """
        return max(len(tasks),(maxexe-1)*(n+1)+maxsimc)

# leetcode submit region end(Prohibit modification and deletion)
