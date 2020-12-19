def status():
    try:
        test_num = input("통계를 확인하고자 하는 시험 번호를 입력해주세요.\n")
        test = open("C:/msgpro/status/{0}.txt".format(test_num),'r')
    except FileNotFoundError:
        print("존재하지 않는 시험 번호입니다. 파일 유무를 확인하시고 프로그램을 다시 실행해주십시오.")
        input()
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
                
    print("시험 번호: {0}\n응시 학생 수: {1}\n평균 점수: {2}\n표준편차: {3}\n".format(test_num,len(all_stat),avg,st_dev))
    print("학생 순위")
    for n in range(len(stat)):
        print("%d."%(n+1),stat[len(stat)-n-1]) 
        

