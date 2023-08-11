

# 종이 자르기

# width, height = list(map(int, input().split()))  # 가로 세로의 초기값
# cut_cnt = int(input())              # 자르는 횟수
# cut_num_list_height = [0, height]   # 세로 자르는 부분 리스트, 양 끝은 미리 넣어놓는다.
# cut_num_list_width = [0, width]     # 가로 자르는 부분 리스트, 양 끝은 미리 넣어놓는다.
# height_box = []     # 마지막에 넓이 계산을 위한 리스트
# width_box = []      # 마지막에 넓이 계산을 위한 리스트
# max_v = 0
#
# for i in range(cut_cnt):
#     choose, cut_num = list(map(int, input().split()))   # 가로인지 세로인지 판별, 자르는 부분
#     if choose == 0:
#         cut_num_list_height.append(cut_num)    # 가로로 판별되면 자르는 부분을 가로 리스트에 넣는다.
#     elif choose == 1:
#         cut_num_list_width.append(cut_num)     # 세로로 판별되면 자르는 부분을 세로 리스트에 넣는다.
#
# cut_num_list_height = sorted(cut_num_list_height)   # 가로 오름차순 정렬하기
# cut_num_list_width = sorted(cut_num_list_width)     # 세로 오름차순 정렬하기
#
# for j in range(len(cut_num_list_height)-1):
#     height_box.append(abs(cut_num_list_height[j] - cut_num_list_height[j+1]))
#     # 가로 리스트를 돌면서 붙어있는 숫자끼리 빼준 절댓값을 height_box에 담는다.
#
# for k in range(len(cut_num_list_width)-1):
#     width_box.append(abs(cut_num_list_width[k] - cut_num_list_width[k+1]))
#     # 세로 리스트를 돌면서 붙어있는 숫자끼리 빼준 절댓값을 width_box에 담는다.
#
# for m in height_box:  # for 문을 돌면서 height_box 와 width_box 원소를 곱하고 그 중 최대 값 찾는다.
#     for n in width_box:
#         if max_v < m * n:
#             max_v = m * n
#
# print(max_v)



# 빙고

# my_bingo = [list(map(int, input().split())) for _ in range(5)]
# bingo = 0
# result_num = 0
# result_list = []
# min_v = 100
#
# for i in range(5):      # 5개 짜리 리스트를 5번에 나눠서 입력을 받는다.
#     announcer = list(map(int, input().split()))
#     for announce in range(5):     # 5개 짜리 입력을 받았으니 5번에 걸쳐서 번호를 선언한다.
#         result_num += 1     # 전체에서 봤을 때 몇번 째 선언인지 계산한다.
#         bingo = 0           # 빙고 몇 줄인지 초기값
#         for row in range(5):
#             for col in range(5):
#                 if announcer[announce] == my_bingo[row][col]:
#                     my_bingo[row][col] = 0      # 2차원 배열을 돌면서 부른 번호가 있는 장소를 0으로 마킹
#                     break           # 어차피 겹치는 번호 없으니까 번호 0 마킹 하고 이 for문 탈출
#
#         for row2 in range(5):           # 가로 빙고 판별 - 가로로 2차원 배열 돌면서 0이 5개 있는 줄이 있는지 찾음
#             energe = 0
#             for col2 in range(5):
#                 if my_bingo[row2][col2] == 0:
#                     energe += 1
#                     if energe == 5:
#                         bingo += 1
#
#         for col2 in range(5):           # 세로 빙고 판별 - 세로로 2차원 배열 돌면서 0이 5개 있는 줄이 있는지 찾음
#             energe = 0
#             for row2 in range(5):
#                 if my_bingo[row2][col2] == 0:
#                     energe += 1
#                     if energe == 5:
#                         bingo += 1
#
#         energe = 0
#         for row2 in range(5):           # 왼쪽에서 오른쪽 대각 빙고 판별
#             for col2 in range(5):
#                 if row2 == col2:
#                     if my_bingo[row2][col2] == 0:
#                         energe += 1
#                         if energe == 5:
#                             bingo += 1
#
#         energe = 0
#         for row2 in range(5):           # 오른쪽에서 왼쪽 대각 빙고 판별
#             for col2 in range(5):
#                 if row2 + col2 == 4:
#                     if my_bingo[row2][col2] == 0:
#                         energe += 1
#                         if energe == 5:
#                             bingo += 1
#
#         # 대각선은 energe 수치 초기화를 밖에 둔 이유는 대각선 빙고의 경우는 25개를 다 살펴도 딱 5개 뿐이기에 이중 포문 아래에서
#         # 한 번 돌때마다 energe를 초기화하면 판별을 할 수가 없기 때문
#
#         if bingo >= 3:                      # 빙고 수치가 한 숫자가 칠해지면서 4가 되는 경우를 대비해 >= 으로 범위 설정
#             result_list.append(result_num)  # 빙고 3줄 이상이 됐을 때가 몇번 째 선언인지 리스트에 담아둠
#             # 이걸 따로 리스트에 담아서 하는 이유는 빙고 3줄 이상이 됐을 때 딱 입력을 그만 받을 수 있는 방법을 몰라서
#             # 아마 입력을 5번 따로 받지 말고 한번에 받아서 25개 짜리 숫자 리스트로 만들어서 했으면 이렇게 안 해도 됐을듯합니다.
#             # 이 이후로 루프 돌면서 항상 3빙고 이상이 나올거라 리스트에 숫자가 계속 쌓입니다. 그 중 가장 먼저 입력된 숫자가
#             # 가장 작을 것이고 그 숫자가 빙고 3줄이 처음 됐을 때 입니다.
#
# for j in result_list:  # 그러므로 저장된 값 중 최저 값 구하기
#     if min_v > j:
#         min_v = j
#
# print(min_v)



# 수열

N, K = list(map(int, input().split()))
arr = list(map(int, input().split()))
max_v = 0

for idx in range(N-K+1):
    my_sum = 0
    for j in range(K):
        my_sum += arr[idx+j]

    if max_v < my_sum:
        max_v = my_sum

print(max_v)























