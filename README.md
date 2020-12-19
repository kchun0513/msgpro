# msgpro
- MSG project는 초,중,고등학생들을 위해 모의시험을 채점하고, 통계 및 정답률을 산출하여
  유형별 취약점을 파악해주는 성적 관리 프로그램 입니다.

Last Version - 1.2  
	     - 학생 개별로 성적이 우수한 순서대로 응시한 시험 정보 확인 가능  
	     - 메인화면 리뉴얼, 가독성 향상을 위한 구분선 추가  
	     - 채점, 성적 확인을 할 때 학생의 이름이나 시험 번호 오입력시 프로그램 재실행 권유가 아닌 재입력 받도록 수정

- 참여 인원 1명

- 프로그램 작성 언어 - Python

- 프로그램 이용 방법

-- 시험 별 학생들의 성적 입력

<img width="800" src="https://user-images.githubusercontent.com/62457974/102629864-19911780-418f-11eb-9347-985cfa700fac.png">

-- 1. 시험 번호 입력 (정답지(txt파일)의 파일명)

-- 2. 학생 수 입력  

-- 3. 학생 이름 입력 및 학생의 답안 입력 (학생 수만큼 반복)

<img width="800" src="https://user-images.githubusercontent.com/62457974/100537639-70c95980-326d-11eb-9581-458baf905140.png">
처음 작성된 학생은 students 라이브러리에 학생의 성적이 txt파일로 생성되며,
   
이미 작성된 적이 있는 학생은 해당 txt파일 이전 시험 성적 밑에 추가로 내용이 생성됩니다.  

그리고 해당 시험을 본 모든 학생의 결과는 status 폴더에 해당 시험 번호의 파일명을 가진 txt파일이 생성되며,  

그 파일에 학생들의 이름 및 점수가 표기 됩니다.


-- 특정 학생의 성적 확인

<img width="800" src="https://user-images.githubusercontent.com/62457974/102629927-32013200-418f-11eb-9925-1d546b332f58.png">

굳이 students 폴더에 들어가지 않아도 특정 학생의 역대 모의시험 성적을 확인할 수 있습니다.
  
해당 학생이 치룬 시험 목록과 점수, 틀린 문제의 번호가 나오며 평균 점수와 표준편차도 표기됩니다.

-- 특정 시험의 통계 확인

<img width="800" src="https://user-images.githubusercontent.com/62457974/102629931-34fc2280-418f-11eb-92d2-4d159b30ab0e.png">

status 폴더에서 해당 시험을 치룬 학생 수, 평균 점수, 표준 편차가 기록으로 나오며 순위가 표기됩니다.

-- 로드맵

1.0 ~ : 학생의 점수 평균 등의 통계 산출

1.3 : 틀린 문제를 따로 저장하여 재시험시 취약 유형 구별

2.0 ~ : 문제 유형, 난이도 등을 구분, excel로 변경  
3.0 ~ : 학생의 유형별 정답률 산출 및 취약 유형 도출

