def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array
#--------------------ここから記述--------------------
    # 要素数長が１以下なら終了
    if len(array) <= 1:
        return array

    # 左右２つに分割したデータを格納するリスト
    left_arr = []
    right_arr = []

    # 先頭要素を軸要素（基準値）に指定
    pivot = array[0]
    pivot_count = 0

    # 左右２つのグループに分割
    for ele in array:
        if ele < pivot:
            left_arr.append(ele)
        elif ele > pivot:
            right_arr.append(ele)
        # 基準値と同じなら、その個数をカウント
        else:
            pivot_count += 1

    # 左右２つに分割したリストに対して、再帰的に関数を呼び出して繰り返す
    left_arr = sort(left_arr)
    right_arr = sort(right_arr)

    # ソート完了後、分割したリストを結合（ピポッドはカウントされた個数だけ中央に挿入）
    return left_arr + [pivot] * pivot_count + right_arr

#--------------------ここまで記述--------------------

if __name__ == '__main__':
    main()