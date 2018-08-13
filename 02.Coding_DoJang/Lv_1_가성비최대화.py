# 기계를 구입하려 하는데 이 기계는 추가 부품을 장착할 수 있다.
# 추가 부품은 종류당 하나씩만 장착 가능하고, 모든 추가 부품은 동일한 가격을 가진다.
# 원래 기계의 가격과 성능, 추가 부품의 가격과 각 부품의 성능이 주어졌을 때
# 추가 부품을 장착하여 얻을 수 있는 최대 가성비를 정수 부분까지 구하시오
# (가격 및 성능은 상대적인 값으로 수치화되어 주어진다).

# e.g.)
# 원래 기계의 가격 : 10
# 원래 기계의 성능 : 150
# 추가 부품의 가격 : 3
# 추가 부품의 성능 : 각각 30, 70, 15, 40, 65
# 추가 부품을 장착하여 얻을 수 있는 최대 가성비 : 17.81... → 17
# (성능이 70과 65인 부품을 장착하면 됨)


# 한글 처리 in Atom 1.21.1 + Anaconda(Python 3.6.3)
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# 기계를 구입하려 하는데 이 기계는 추가 부품을 장착할 수 있다.
# 추가 부품은 종류당 하나씩만 장착 가능하고, 모든 추가 부품은 동일한 가격을 가진다.
# 원래 기계의 가격과 성능, 추가 부품의 가격과 각 부품의 성능이 주어졌을 때,
# 추가 부품을 장착하여 얻을 수 있는 최대 가성비를 정수 부분까지 구하시오.
# (가격 및 성능은 상대적인 값으로 수치화되어 주어진다)
# e.g.)
# 원래 기계의 가격 : 10
# 원래 기계의 성능 : 150
# 추가 부품의 가격 : 3
# 추가 부품의 성능 : 각각 30, 70, 15, 40, 65
# 추가 부품을 장착하여 얻을 수 있는 최대 가성비 : 17.81... → 17
# (성능이 70과 65인 부품을 장착하면 됨)

mashine_price = 10
mashine_performance = 150
part_price = 3
parts_performance = [30, 70, 15, 40, 65]
number_parts = len(parts_performance)
performance_rate = mashine_performance / mashine_price
best_rate = performance_rate
best_parts = []
print("원래 기계 가성비 :", performance_rate)

# 부품 조합 모두 점검
for x in range(2 ** number_parts):
    combination = bin(x + 1)[2:].zfill(number_parts)

    addparts_performance = mashine_performance
    addparts_price = mashine_price
    for i in range(number_parts):
        if combination[i] == '1':
            addparts_performance += parts_performance[i]
            addparts_price += part_price
    addparts_rate = addparts_performance / addparts_price
    # print(combination, addparts_performance, addparts_price, addparts_rate)

    if addparts_rate > best_rate:
        best_parts = [[combination, addparts_performance, addparts_price, addparts_rate]]
        best_rate = addparts_rate
    elif addparts_rate == best_rate:
        best_parts += [[combination, addparts_performance, addparts_price, addparts_rate]]

if len(best_parts) > 0:
    for combination_number in range(len(best_parts)):
        print("다음 부품을 추가하세요")
        for i in range(number_parts):
            # print(best_parts[combination_number][0][i], i)
            if best_parts[combination_number][0][i] == '1':
                print("-", i + 1, "부품 : 가성비", parts_performance[i])
        print("총 성능 :", best_parts[combination_number][1])
        print("총 가격 :", best_parts[combination_number][2])
        print("총 가성비 :", best_parts[combination_number][3])
else:
    print("부품을 추가하지 마십시오")