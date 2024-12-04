# score_calculator
친구들끼리 게임할 때 점수 내기 하는데 일일히 계산하기 귀찮아서 만들었음.

## 사용법
main.py 코드 실행

![image](https://github.com/user-attachments/assets/694ca76a-6f9a-42ed-bd00-2f1e651cbd63)

![image](https://github.com/user-attachments/assets/9ff97878-423a-4df8-9a25-a8340033f85e)

해당 콤보 박스를 눌러서 원하는 원하는 경기 종류? 를 선택

예) 롤토체스, 서든어택 등

※ 기본값은 1,2,3 이지만 변경가능 추후 설명


![image](https://github.com/user-attachments/assets/1e8bfce7-749d-4446-9372-ab7e97dcc00a)

![image](https://github.com/user-attachments/assets/193ee4cb-b241-4ad1-8bda-cd3ab5f42402)


사용자 추가 버튼을 클릭하여 플레이어를 추가

(예시로 철수 영희 맹구를 추가)


![image](https://github.com/user-attachments/assets/3a18abdb-317e-470e-8f6c-15df5612e105)

추가를 하게되면 해당 플레이어의 이름이 추가가됨


경기가 끝나면 해당 경기에 참여했던 인원을 선택하고 점수를 매기고 데이터 추가 버튼을 클릭

![image](https://github.com/user-attachments/assets/d1a8f20c-9c3a-4926-8cd5-6a466483b7c1)

![image](https://github.com/user-attachments/assets/56633739-76e3-4e0a-aff8-ded4f8ef4df4)

해당 경기의 정보가 데이터 베이스에 등록이됌

![image](https://github.com/user-attachments/assets/c24b0c79-4638-4659-8ff3-d78811c0f342)


![image](https://github.com/user-attachments/assets/3116ea0b-0248-4f7d-ab5d-1402d1d44cc7)

모든 전적 가져오기 버튼으로 지금 까지쌓인 데이터들의 정보를 가져올수 있음 (클립 보드에 복사되어 붙여넣기로 확인)

![image](https://github.com/user-attachments/assets/22458f46-040a-4b41-aa29-c2dafa50a206)


간단한 예시

플레이어 몇명을 더 추가하고 데이터를 추가한다음 전적 가져오기 한 결과 

![image](https://github.com/user-attachments/assets/cf7b9d1c-9d3c-436d-b8c7-903ca2389ffc)

![image](https://github.com/user-attachments/assets/1fd74ad8-aafe-4401-ad75-c234b86f133a)

![image](https://github.com/user-attachments/assets/d4b04a4e-5d1b-48b6-be94-234cd6e94bbe)

-안에 들어있는 전적의 경우는 해당인원이 같이한 경기의 포인트 점수 합

철수, 영희가 속한 경기의 포인트 합 점수가 아닌 철수, 영희 둘만 있는 경기의 포인트합 (만약 철수, 영희, 맹구 세명이 같이한 경기라면 따로 카운트)

=안에 들어있는 전적의 경우 해당 플레이어와 나머지 플레이어와의 역대 전적 포인트 합 (이 경우는 두사람이 포함된 모든 게임 카운트)



