def record():
    
    #학생 이름 입력 및 해당 학생 성적 파일 유무 확인
    while True:
        name = input("\n성적을 확인하고자 하는 학생의 이름을 입력하시오.\n")
        try:
            achievement = open("C:/Users/user/msgpro/students/{0}.txt".format(name),'r')
            break;
        except FileNotFoundError:
            print("존재하지 않는 이름입니다. 다시 입력하시오.")

    #해당 학생이 응시한 시험 번호, 점수, 오답 불러오기
    records = achievement.readlines()
    test_num = []
    test_score = []
    test_wrong = []
    for i in records:
        test = i.split()
        test_num.append(test[0])
        test_score.append(test[1])
        test_wrong.append(test[2:])
    
    #해당 학생의 이름, 응시한 시험에 대한 정보 출력
    print("-----------------------------------------------------------------------------------")
    print("\n학생이름:",name,"\n")
    for j in range(len(test_num)):
        print("시험번호:",test_num[j],"점수:",test_score[j],"틀린 번호:",test_wrong[j])

    #해당 학생의 평균점수, 표준편차 출력
    avg = 0
    st_dev = 0
    for k in test_score:
        avg += float(k)
    avg = round(avg/len(test_num),1)
    for j in test_score:
        st_dev += (float(j)-avg)**2
    st_dev = round((st_dev/len(test_num))**0.5,1)
    print("\n평균점수:",avg,"학생 표준편차:",st_dev,"\n")
    
    #해당 학생이 응시한 시험을 성적이 우수한 순서로 출력
    print(name,"학생의 성적(성취도)이 높은 시험의 순서는 다음과 같습니다.\n")
    
    for a in range(len(test_score)-1):
        for b in range(len(test_score)-1):
            if float(test_score[b]) > float(test_score[b+1]):
                test_num[b], test_num[b+1] = test_num[b+1], test_num[b]
                test_score[b], test_score[b+1] = test_score[b+1], test_score[b]
                test_wrong[b], test_wrong[b+1] = test_wrong[b+1], test_wrong[b]
                
    for j in range(len(test_num)):
        n = len(test_num)-1-j
        print("시험번호:",test_num[n],"점수:",test_score[n],"틀린 번호:",test_wrong[n])

                
    achievement.close()
