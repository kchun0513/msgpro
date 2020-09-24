name = input("성적을 확인하고자 하는 학생의 이름을 입력해주세요.\n")
achievement = open("C:/msgpro/students/{0}.txt".format(name),'r')
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
    
