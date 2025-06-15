# 중복된 숫자를 제거하는 함수
def remove_duplicates(nums):
    result = []
    for n in nums:
        if n not in result:
            result.append(n)
    return result

numbers = [1, 2, 2, 3, 4, 4, 5]
unique = remove_duplicates(numbers)
print("중복 제거 결과:", unique)  # 출력: [1, 2, 3, 4, 5]
