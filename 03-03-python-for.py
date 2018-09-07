WEEK_LIST = ['月', '火', '水', '木', '金', '土', '日']
SUBJECT_LIST = ['Python', '数学', '機械学習', '深層学習','エンジニアプロジェクト']

def output_schedule(study_time_list):
    '''今週の勉強予定を出力します'''
    # イテレータをセット
    itr_week = iter(WEEK_LIST)
    # SUBJECT_LIST のインデックス(数学からなので、初期値は1)
    index_SUBJECT = 1
    # study_time_list の数分処理を行う
    for today_time_list in study_time_list:
        # today_time_listの場合はお休みを表示
        if today_time_list == 0:
            print("{}曜日は、お休みです。".format(next(itr_week)))
        else:
            # 勉強時間の分処理を行う
            print("{}曜日は、{}時間勉強する予定です。".format(next(itr_week), today_time_list))
            for index in range(today_time_list):
                print("{}限目 {}".format(index + 1, SUBJECT_LIST[index_SUBJECT]))
                # SUBJECT_LIST のインデックスを一つ進める
                index_SUBJECT = index_SUBJECT + 1
                if index_SUBJECT == 5:
                    # SUBJECT_LIST の要素は5つまでので、インデックスを0にする
                    index_SUBJECT = 0

def main():
    '''勉強情報をoutput_scheduleに渡します'''
    # 1日に何時間勉強するか（1週間　月曜日〜日曜日）
    study_time_list = [3, 1, 3, 0, 4, 2, 2]
    output_schedule(study_time_list)


if __name__ == '__main__':
    main()