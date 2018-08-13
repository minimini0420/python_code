# 연구자의 연구업적을 평가할 때 사용되는 지표 중 h-index와 g-index라는 것이 있다.
#
# h-index : 인용 횟수가 h번 이상인 논문이 h개일 때 가능한 h의 최댓값
# g-index : 인용 횟수가 높은 상위 g개 논문의 인용 횟수 총합이 g²이상일 때 가능한 g의 최댓값
# 어떤 학자가 쓴 논문 각각의 인용 횟수가 주어질 때, h-index와 g-index를 계산하시오.
#
# e.g.)
#
# 입력 : 0 15 4 0 7 10 0
# h-index : 4
# g-index : 6

# Function to find h-index
# def FindHIndex(cntList):
#     cntDict = {}
#
#     for cnt in cntList:
#         cntDict[cnt] = 1 + (0 if cntDict.get(cnt) is None else cntDict.get(cnt))
#
#     beforeCnt = 0
#
#     for cnt in sorted(cntDict, reverse = True):
#         cntDict[cnt] += beforeCnt
#         beforeCnt = cntDict[cnt]
#
#         if cntDict[cnt] >= cnt:
#             return cnt
#
# # Function to find g-index
# def FindGIndex(cntList):
#     sumList = sorted(cntList, reverse = True)
#
#     beforeSum = 0
#
#     for i in range(len(sumList)):
#         sumList[i] += beforeSum
#         beforeSum = sumList[i]
#
#         if i * i >= sumList[i]:
#             return i
#
# # Main
# # Input string
# input = '0 15 4 0 7 10 0'
#
# # Input list from input string
# quoteCnt = [int(x) for x in input.split(' ')]
#
# # Find h-index
# hIndex = FindHIndex(quoteCnt)
# print('h-index: '+str(hIndex))
#
# # Find g-index
# gIndex = FindGIndex(quoteCnt)
# print('g-index: '+str(gIndex))