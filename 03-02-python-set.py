course_dict = {
    'AIコース': {'Aさん', 'Cさん', 'Dさん'},
    'Railsコース': {'Bさん', 'Cさん', 'Eさん'},
    'Railsチュートリアルコース': {'Gさん', 'Fさん', 'Eさん'},
    'JS': {'Aさん', 'Gさん', 'Hさん'},
}


def find_person(want_to_find_person):
    """
    受講生がどのコースに在籍しているかを出力する。
    まずはフローチャートを書いて、どのようにアルゴリズムを解いていくか考えてみましょう。
    """
    # ここにコードを書いてみる
    # コースの数分処理を行う
    for course, person in course_dict.items():
        # 集合の積より、共通する要素を抽出
        Result = person & want_to_find_person
        if not Result:
           # 要素が空の場合
           print("{}に{}は在籍していません。".format(course, want_to_find_person))
        elif len(Result) == 1:
            # 要素が1の場合は一人のみ
            print("{}に{}のみ在籍しています。".format(course, Result))
        else:
            print("{}に{}は在籍しています。".format(course, Result))

def main():
    want_to_find_person = {'Cさん', 'Aさん'}
    print('探したい人: {}'.format(want_to_find_person))
    find_person(want_to_find_person)


if __name__ == '__main__':
    main()