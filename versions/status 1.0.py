def status():
    try:
        test_num = input("통계를 확인하고자 하는 시험 번호를 입력해주세요.\n")
        test = open("C:/msgpro/status/{0}.txt".format(test_num),'r')
    except FileNotFoundError:
        print("존재하지 않는 시험 번호입니다. 파일 유무를 확인하시고 프로그램을 다시 실행해주십시오.")
        input()
    all_stat = test.readline().split()
    avg = 0
    st_dev = 0
    for i in all_stat:
        avg += float(i)
    avg = round(avg/len(all_stat),1)
    for k in all_stat:
        st_dev += (float(k)-avg)**2
    st_dev = round((st_dev/len(all_stat))**0.5,1)
    print("시험 번호 {0}의 평균 점수는 {1}이고, 표준편차는 {2}입니다.".format(test_num,avg,st_dev))

