# 問題 in Chinese:
# 共有n張白紙(每一點預設darkness是0), 在上面滴墨水, 坐標i, j, darkness:255黑. 每滴一滴就會從中心擴散
# 每隔一格就 darkness-1. 如果遇到之前已經有顏色的, 就比較現有的跟擴散的誰較黑, 以較黑的值為新的值
# input 為下面的stdin input. output請用stdout輸出(python即print)每一張紙的總濃(黑)度, 如下面的example

# test cases: hackerrank uses stdin to input the arguments
# 2  # 幾個 paper
# 3 4 # 1st paper 大小
# 2  # 幾滴
# 0 0 255 # 1st drop
# 1 2 255 # 2nd drop
# 5 6 # 2nd paper size
# 4
# 1 0 10
# 2 2 9
# 2 3 5
# 4 2 9
# answers in stdout (要印出 每張的總濃度):
# 3046
# 217 (這一行答案不確定有否記錯 hackerrank 的答案)
# -----------------------------
# paper1 case - initial:
# 0 0 0 0
# 0 0 0 0
# 0 0 0 0
# 1st drop:
# (應該是菱型擴散)
# 255 254 253 252
# 254 253 252 251
# 253 252 251 250
# 2nd drop:
# 255 254 254 253
# 254 254 255 254
# 253 253 254 253

# O(darkness*darkness) ignore the case: it may be hit boundary before decaying to 0
def try_drop(darkness, paper, m, n,  i, j, direction):
    for delta_x in range(-darkness, darkness):
        for delta_y in range(-darkness, darkness):
            new_dark = darkness-abs(delta_x)-abs(delta_y)
            if new_dark >0:
                x = i + delta_x
                y = j + delta_y
                if x >= 0 and x < m and y>=0 and y<n:
                    if paper[x][y] < new_dark:
                        paper[x][y] = new_dark
    # bug4: 原本下面的 recursive 作法沒有考慮到菱型, 只有十字放射線:
    # 所以已修正成上面的兩個 loop 作法. 若還是要用 recursrive, 則會需要另外存一個 2d array防止走過
    # direciton: 0:all, 1: i+1, 2: i-1, 3:j+1. 4:j-1
    # 5, 右下
    # 6  右上
    # 7  左上
    # 8  左下
    # if darkness <= 0:
    #     return
    # if i >= m or j >= n or i<0 or j<0: # bug2, 打成<=
    #     return
    # if paper[i][j] < darkness:
    #     paper[i][j] = darkness
    # new_dark = darkness-1
    # new_dark2 = darkness-2
    # if new_dark>0:
    #     if direction == 0 or direction == 1:
    #         try_drop(new_dark, paper, m, n, i+1, j, 1) # bug1: 打成h
    #     if direction == 0 or direction == 2:
    #         try_drop(new_dark, paper, m, n, i-1, j, 2) # bug3 會導致往回, 要加direction
    #     if direction == 0 or direction == 3:
    #         try_drop(new_dark, paper, m, n, i, j+1, 3)
    #     if direction == 0 or direction == 4:
    #         try_drop(new_dark, paper, m, n, i, j-1, 4)
    # if new_dark2>0:
    #     if direction == 0 or direction == 5:
    #         try_drop(new_dark2, paper, m, n, i+1, j+1, 5)
    #     if direction == 0 or direction == 6:
    #         try_drop(new_dark2, paper, m, n, i-1, j+1, 6)
    #     if direction == 0 or direction == 7:
    #         try_drop(new_dark2, paper, m, n, i-1, j-1, 7)
    #     if direction == 0 or direction == 8:
    #         try_drop(new_dark2, paper, m, n, i+1, j-1, 8)
def cal_sum(h, w, drop_list):
    print(drop_list)
    paper = []
    for i in range(h): # num_ rows
        paper.append([0]*w)
    print(paper)

    for drop in drop_list:
        r= drop[0]
        c= drop[1]
        darkness = drop[2]
        try_drop(darkness, paper, h, w, r, c, 0)
    # iterate the map to get sum
    sum = 0
    for i in range(h):
        for j in range(w):
            sum += paper[i][j]
    print(sum)

if __name__ == '__main__':
    # case1
    # int(input()) # n papers, comment 掉問題所需的 input 處理部份, 直接 assign arguments, 方便測試
    n = 1
    print(n)
    for _ in range(n):
        h, w = 3, 4 # map(int, input().strip().split())
        print(h, w)
        n_drop = 2 #int(input().strip())
        print(n_drop)
        drop_list = []
        for i in range(n_drop):
            #list(map(int, input().strip().split()))
            if i == 0:
                drop = [0, 0, 255]
            elif i == 1:
                drop = [1, 2, 255]
            drop_list.append(drop)
            # print(drop)
        cal_sum(h, w, drop_list) # 3046
    # case 2,
    h  = 5
    w  = 6
    drop_list = []
    drop_list.append([1, 0, 10])
    drop_list.append([2, 2, 9])
    drop_list.append([2, 3, 5])
    drop_list.append([4, 2, 9])
    cal_sum(h, w, drop_list) # it will output the answer, 217
