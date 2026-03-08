"""
冒泡排序算法演示
Bubble Sort Algorithm
"""

import random
import time


def bubble_sort(arr):
    """冒泡排序算法"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # 交换元素
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def bubble_sort_optimized(arr):
    """优化版冒泡排序（提前结束）"""
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # 如果没有交换，说明已经排序完成
        if not swapped:
            break
    return arr


# ============================================================
# 测试运行
# ============================================================

print("=" * 60)
print("🔢 冒泡排序算法演示 - Bubble Sort Demo")
print("=" * 60)

# 测试数据1：随机数组
print("\n📋 测试1: 随机数组")
random_array = [64, 34, 25, 12, 22, 11, 90]
print(f"原始数组: {random_array}")

start_time = time.time()
sorted_array = bubble_sort(random_array.copy())
end_time = time.time()

print(f"排序后:   {sorted_array}")
print(f"耗时:     {(end_time - start_time) * 1000:.4f} ms")

# 测试数据2：更大的数组
print("\n📋 测试2: 10000个随机数")
large_array = [random.randint(1, 10000) for _ in range(10000)]
print(f"数组大小: {len(large_array)}")

start_time = time.time()
sorted_large = bubble_sort(large_array.copy())
end_time = time.time()

print(f"排序完成!")
print(f"耗时:     {(end_time - start_time) * 1000:.2f} ms")

# 测试数据3：优化版
print("\n📋 测试3: 优化版冒泡排序 (10000个数)")
start_time = time.time()
sorted_optimized = bubble_sort_optimized(large_array.copy())
end_time = time.time()

print(f"排序完成!")
print(f"耗时:     {(end_time - start_time) * 1000:.2f} ms")

# 验证排序正确性
print("\n✅ 验证排序结果:")
print(f"前10个数: {sorted_large[:10]}")
print(f"后10个数: {sorted_large[-10:]}")

print("\n" + "=" * 60)
print("🎉 冒泡排序算法运行完成!")
print("=" * 60)

print("""
📚 算法说明:
   冒泡排序是一种简单的排序算法:
   1. 比较相邻的两个元素
   2. 如果顺序错误就交换
   3. 重复遍历直到排序完成
   
   时间复杂度: O(n²)
   空间复杂度: O(1)
   稳定性:     ✓ 稳定
""")
