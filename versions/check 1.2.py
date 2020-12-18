def check():
    
    #실시한 시험의 번호 입력 및 해당 시험의 답안지 유무 확인
    while True:
        test_num = input("\n시험 번호를 입력해주세요.\n")
        try:
            test = open("C:/Users/user/msgpro/answer/{0}.txt".format(test_num),'r')
            exam_stat = open("C:/Users/user/msgpro/status/{0}.txt".format(test_num),'a')
            break;
        except FileNotFoundError:
            print("존재하지 않는 시험 번호입니다. 다시 입력해주세요.")
        
    #응시한 학생의 수를 입력받고 각 학생들의 이름과 답안을 입력하면
    answer = test.readline().split()
    que = len(answer)
    n = int(input("\n학생 수를 입력해주세요.\n"))
    for _ in range(n):
        name = input("\n학생의 이름을 입력해주세요\n")
        students = open("C:/Users/user/msgpro/students/{0}.txt".format(name),'a')
        user_answer = input("\n{0} 학생의 답안을 문항별로 띄어서 기입해주세요.\n".format(name)).split()
        correct = []
        wrong = []
        while que != len(user_answer):
            user_answer = input("\n문항 수가 맞지 않습니다. 문제 수와 띄어쓰기를 확인하고 다시 기입해주세요.\n").split()
            
    #답안을 비교후 맞춘 문제와 틀린 문제 구분하여 리스트에 저장
        for x in range(que):
            if answer[x] == user_answer[x] :
                correct.append(str(x+1))
            else:
                wrong.append(str(x+1))
                
    #맞힌 문제 수/총 문제 수로 정답률을 산출
        score = round(len(correct)/que*100,1)
        std_ach = "{0} {1} ".format(test_num,score)
        std_stat = "{0} {1} \n".format(name,score)
        for i in wrong:
            std_ach += "{0} ".format(i)
        std_ach += "\n"
        
    #status폴더에 해당 시험의 결과를,
        students.write(std_ach)
        
    #students 폴더에 해당 학생의 점수와 틀린 문제를 저장
        exam_stat.write(std_stat)
    students.close()
    test.close()














































    
