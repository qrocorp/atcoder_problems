import math
import itertools


def main():  # itertools.permutationsをつかったきれいな解法
    n = int(input())
    p = tuple(map(int, input().split()))
    q = tuple(map(int, input().split()))

    # 1からnまでの整数組み合わせを昇順にすべて生成
    s = itertools.permutations(range(1, n+1))
    l = []
    for v in s:
        l.append(v)

    # p,qが昇順リストの何番目に該当するかを特定
    p_index = l.index(p)
    q_index = l.index(q)

    print(abs(p_index - q_index))


'''
def main_sub():
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))

    p_order = 1
    q_order = 1

    p_diff = []
    q_diff = []
    # 昇順の連番リスト作成
    p_sort = list(range(1, 9))
    q_sort = list(range(1, 9))

    for i in range(n):
        # 先頭から順に、残っている要素の下から何番目かを特定する
        p_diff.append(p_sort.index(p[i]))
        q_diff.append(q_sort.index(q[i]))
        p_sort.remove(p[i])
        q_sort.remove(q[i])

    for i in range(n):
        rest_p = len(p_diff[i+1:]) if i < n else 0
        rest_q = len(q_diff[i+1:]) if i < n else 0
        p_order += p_diff[i] * math.factorial(rest_p)
        q_order += q_diff[i] * math.factorial(rest_q)

    answer = abs(p_order - q_order)
    print(answer)
'''


if __name__ == "__main__":
    main()
