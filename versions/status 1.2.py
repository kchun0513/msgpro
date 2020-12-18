def status():

    #시험 번호 입력 및 해당 시험의 통계 유무 확인
    while True:
        test_num = input("\n통계를 확인하고자 하는 시험 번호를 입력해주세요.\n")
        try:
            test = open("C:/Users/user/msgpro/status/{0}.txt".format(test_num),'r')
            break;
        except FileNotFoundError:
            print("존재하지 않는 시험 번호입니다. 다시 입력해주세요.")

    #해당 시험의 통계를 가져와 점수가 높은 순서대로 나열, 시험의 평균 점수와 표준편차 산출
    all_stat = test.readlines()
    stat = []
    avg = 0
    st_dev = 0
    for i in all_stat:
        stat += [i.split()]
    for j in stat:
        avg += float(j[1])
    avg = round(avg/len(all_stat),1)
    for k in stat:
        st_dev += (float(k[1])-avg)**2
    st_dev = round((st_dev/len(all_stat))**0.5,1)
    for a in range(len(stat)-1):
        for b in range(len(stat)-1):
            if float(stat[b][1]) > float(stat[b+1][1]):
                stat[b], stat[b+1] = stat[b+1], stat[b]
            
    #해당 시험의 통계 산출 결과 출력
    print("-----------------------------------------------------------------------------------\n")
    print("시험 번호: {0}\n응시 학생 수: {1}\n평균 점수: {2}\n표준편차: {3}\n".format(test_num,len(all_stat),avg,st_dev))
    print("학생 순위\n")
    for n in range(len(stat)):
        print("%d."%(n+1),stat[len(stat)-n-1]) 
        

