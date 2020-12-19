print("MSG 프로젝트")
retry = 'y'
while retry == 'y':
    n = input("1. 성적 입력, 2. 성적 확인, 3. 시험 통계 확인, 종료하려면 아무 키를 입력해주세요.\n")
    if n == '1':
        from check import check
        check()
    if n == '2':
        from achievement import record
        record()
    if n == '3':
        from status import status
        status()
    else:
        print("이용해주셔서 감사합니다.")
        retry = 'n'
    retry = input("메인 화면으로 이동하시려면 y를, 종료하려면 아무 키를 입력해주세요.\n")       
    
