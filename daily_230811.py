

# 9489. 고대 유적

import sys
sys.stdin = open('input_9489.txt', 'r')

# 시간 초과 코드

# T = int(input())
# for tc in range(1, T+1):
#     N, M = list(map(int, input().split()))
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     max_v = 0
#
#     for row in range(N):                    # 가로
#         length = 0
#         for col in range(M):
#             if arr[row][col] == 1:
#                 length += 1
#             else:
#                 if max_v < length:
#                     max_v = length
#                 length = 0
#
#         if max_v < length:
#             max_v = length
#
#     for col in range(M):                    # 세로
#         length = 0
#         for row in range(N):
#             if arr[row][col] == 1:
#                 length += 1
#             else:
#                 if max_v < length:
#                     max_v = length
#                 length = 0
#
#         if max_v < length:
#             max_v = length
#
#     print(f'#{tc} {max_v}')
