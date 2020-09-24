def record():
    try:
        name = input("성적을 확인하고자 하는 학생의 이름을 입력하시오.\n")
        achievement = open("C:/msgpro/students/{0}.txt".format(name),'r')
    except FileNotFoundError:
        print("존재하지 않는 이름입니다. 학생 이름과 성적파일 유무를 students 폴더에서 확인하시고 프로그램을 다시 실행해주십시오.")
        input()
    records = achievement.readlines()
    test_num = []
    test_score = []
    test_wrong = []
    for i in records:
        test = i.split()
        test_num.append(test[0])
        test_score.append(test[1])
        test_wrong.append(test[2:])

    print("학생이름:",name,"\n")
    for j in range(len(test_num)):
        print("시험번호:",test_num[j],"점수:",test_score[j],"틀린 번호:",test_wrong[j],"\n")
    avg = 0
    for k in test_score:
        avg += float(k)
    avg = round(avg/len(test_num),1)
    print("평균점수:",avg)
    achievement.close()
