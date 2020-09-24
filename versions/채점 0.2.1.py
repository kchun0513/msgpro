try:
    test_num = input("시험 번호를 입력해주세요.\n")
    test = open("C:/msgpro/answer/{0}.txt".format(test_num),'r')
except FileNotFoundError:
    print("존재하지 않는 시험 번호입니다. 파일 유무를 확인하시고 프로그램을 다시 실행해주십시오.")
    input()
achieve = open("achievement.txt",'a')
answer = test.readline().split()
que = len(answer)
n = int(input("학생 수를 입력해주세요.\n"))
for _ in range(n):
    name = input("학생의 이름을 입력해주세요\n")
    user_answer = input("{0} 학생의 답안을 문항별로 띄어서 기입해주세요.\n".format(name)).split()
    correct = []
    wrong = []
    while que != len(user_answer):
        user_answer = input("문항 수가 맞지 않습니다. 문제 수와 띄어쓰기를 확인하고 다시 기입해주세요.\n").split()
    for x in range(que):
        if answer[x] == user_answer[x] :
            correct.append(str(x+1))
        else:
            wrong.append(str(x+1))

    score = round(len(correct)/que*100,1)
    std_ach = "{0} 학생의 시험번호 {1}의 점수는 {2}%입니다.\n".format(name,test_num,score)
    achieve.write(std_ach)
    wrong_ = '{0} 학생이 시험번호 {1}에서 틀린 문제는 '.format(name,test_num)
    for i in wrong:
        wrong_ += "{0}번 ".format(i)
    wrong_ += "입니다.\n"
    achieve.write(wrong_)
achieve.close()
test.close()
