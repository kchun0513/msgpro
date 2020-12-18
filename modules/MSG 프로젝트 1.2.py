retry = 'y'
while retry == 'y':
    print("===================================================================================")
    print("===================================================================================")
    print("MMMMM     MMMMM      SSSSSSSS      GGGGGGGG       PPPPPPPP    RRRRRRRR     OOOOO")
    print("MM  MM   MM  MM     SSS          GGG              PP     PP   RR     RR   OO   OO")
    print("MM   MM MM   MM    SS           GG                PP      P   RR      R  OO     OO")
    print("MM    MMM    MM     SSSSSSSS    GG     GGGGG      PPPPPPPP    RRRRRRRR   OO     OO")
    print("MM     M     MM            SS    GG       GG      PP          RR RR      OO     OO")
    print("MM     M     MM          SSS      GGG     GG      PP          RR  RRR     OO   OO")
    print("MM     M     MM    SSSSSSSS         GGGGGGG       PP          RR    RRR    OOOOO")
    print("===================================================================================")
    print("1. 성적 입력\n2. 성적 확인\n3. 시험 통계 확인\n종료하려면 아무 키를 입력해주세요.")
    print("===================================================================================\n")
    n = input("입력: ")
    print("\n-----------------------------------------------------------------------------------")
    if n == '1':
        from check import check
        check()
    if n == '2':
        from achievement import record
        record()
    if n == '3':
        from status import status
        status()
    
    print("\n-----------------------------------------------------------------------------------")
    print("\n이용해주셔서 감사합니다.")
    retry = 'n'
    retry = input("\n메인 화면으로 이동하시려면 y를, 종료하려면 아무 키를 입력해주세요.\n")
       
    
