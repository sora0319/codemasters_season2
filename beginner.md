## 초급 문제
<br/>

### 1. 스칼라곱 구하기
    1. 두 스칼라 값을 받아서 int 형으로 리스트 저장하기
    2. 각 위치의 곱을 구하여서 하나의 리스트에 저장한다
    3. 새로 만든 리스트이 합을 출력한다.  
-------
<br/>

### 2. 리그
    1. 이차원 리스트(team)로 각 팀의 경기 결과를 받는다
    2. 점수를 저장할 리스트 score 생성하고 0을 4개로 으로 초기화 한다
    3. i번째 팀과 j 번째 팀과의 경기 결과를 비교한다 0<= i, j<4
        - team[i][j] => i번째 팀의 경기 결과
        - team[j][i] => j번째 팀의 경기 결과  
        3-1. i == j 이면 동일한 팀이므로 continue로 넘어간다  
        3-2. team[i][j] > team[j][i] 라면 score[i]에 3점을 더한다  
        3-3. team[i][j] == team[j][i]: 라면 score[i]에 1점을 더한다
    4. score의 모든 점수를 출력한다
-----
<br/>

### 3. 책상 수리
목재 1개가 필요하고 목재의 길이는 최소 K와 같거나 조금만 더 길면 된다  
즉 최소한으로 K보다 더 크면 된다.  
N개의 목재들이 있고 그 중 K 보다 크거 가장 짧은 목재의 길이가 무엇인지 찾으면 된다.  
<br/>

    1. N, K를 입력받는다
    2. N개의 길이(length)를 입력받는다
    3. min_length = 1000000001 을 생성한 후, N만큼 반복하면서  
        3-1. 길이가 K보다 크거나 같을 때 min_length와 비교하여서 작으면 min_length = length[i]에 넣는다.
    4. 결과 값 출력
--------
<br/>

### 4. 화분
    1. 세로 N, 가로 M의 길이를 입력받는다
    2. 만약 N 또는 M 이 2이하이면 N*M
    3. 그렇지 않다면 (M*2) + (N-2) * 2
---------
<br/>

### 5. 종이 자르기
직사각형에서 모서리에 2개의 점을 찍을 때 두 점을 이어서 직사각형을 나눌 수 있는지 아닌지 확인하는 것  
==> 두점이 직사각형을 나누어질 수 없는 경우는 두점이 같은 모서리 면에 위치하는 경우이다.  

    1. 높이 H, 너비 W 를 입력받는다
    2. 두 점의 위치(X1, Y1, X2, Y2)값을 입력받는다
    3. 두 점이 같은 모서리 위에 있을 때 다음과 같은 조건들 중 하나를 만족한다.  
        3-1. X1 == X2 and (X1 == 0 or X1 == W)  
        ==> 두 X값이 같을 때 X값들이 0 또는 W와 같으면 같은 모서리에 위치한다.  
        3-2. Y1 == Y2 and (Y1 == 0 or Y2 == H)  
        ==> 두 Y값이 같을 때 Y값들이 0 또는 H와 같으면 같은 모서리에 위치한다.  
    4. 두 조건 중 하나를 만족하면 'NO'를 출력하고 둘 다 만족하지 않으면 'YES'를 출력한다.
-----------
<br/>

### 6. 간단한 수학문제
어떤 정수 N에 대해서, N 이상의 정수 중에서 K보다 크지 않은 N의 배수의 최댓값을 구하는 문제이다.  

    1. N, K 값을 입력 받는다
    2. K / N 을 해서 몫을 구한 다음 몫 * N을 해서 최대값을 구한다.
-------------
<br/>

### 7. 디스플레이 제작
픽셀 N개로 항상 직사각형 모양이면서 가로 a칸, 세로 b칸의 디스플레이를 만들어야 한다. 이때 a ≤ b이면서 a × b의 값은 N이어야 한다.  
또한 가능하면 정사각형에 가까워야 한다는 것입니다. 즉, b - a가 가능한 한 작아야 한다는 것이다.  

    1. 픽셀의 개수 N을 입력 받는다.
    2. 1부터 N+1 까지 반복하면서 다음을 수행한다.  
        2-1. i == b와 같다면 같은 약수를 모두 구한 것이기 때문에 break  
        2-2. 그렇지 않고 N % i == 0 일 때 a = i, b = N//i 를 수행  
            2-2-1. N//i == i 인 경우가 있으므로 그 경우에는 break
    3.  a, b 값을 출력
-------------
<br/>

### 8. 암호해독
각 글자수 위치만큼 글자를 반복한 암호문에 있다. 예를 들어 'pob'이라는 단어가 있다면,  
1. p는 첫번째 글자라서 1번 반복
2. o는 두번째 글자라서 2번 반복
3. b는 세번째 글자라서 3번 반복  
결과는 poobbb가 된다.  

이러한 규칙으로 만들어진 암호문을 보고 원래 단어를 맞추어 보자.  

    1. 단어를 입력받는다.
    2. start = 0에는 시작 순서가 i = 1 는 몇번째 숫자인지를 표시한다
    3. while문으로 반복하면서 start != 단어의 길이 일때까지  
        3-1. answer += word[start]  
        3-2. start += i  
        3-3. i += 1  
    4. 결과를 출력한다.
-------------
<br/>

### 9. DNA
염기서열 아데닌(A), 티민(T), 구아닌(G), 사이토신(C) 이 있고
A - T, G - C가 쌍으로 배열되어야 한다.
한쪽 염기서열이 주어지만 다른 쪽 염기서열을 알려주는 것을 하자.  

    1. 문자열 길이를 입력받는다
    2. 염기서열을 입력받는다
    3. A-T, G-C, T-A, C-G 인 dictionary 생성
    4. 문자 하나를 dictionary에 넣어서 정답을 print한다. 단, end = ''
-------------
<br/>

### 10. 배열 평준화
배열 A 가 있을 때 A의 평준화 정도 = (A에서 가장 큰 값) - (A에서 가장 작은 값) 이 성립합니다.  
이때 평균화 정도를 가장 작게 만들기 위해 하나의 수를 제외하여 작은 평준화 값을 구해라  

    1. 배열 크기 N을 받는다
    2. 배열 A를 받는다
    3. 배열을 sort해서 오름차순으로 정렬한다.
    4. A[-1] - A[0], A[-2] - A[0], A[-1] - A[1]의 min 값을 구한다  
==> 시간복잡도 sort() + min()함수 = O(nlongn) + O(3) 이다  

-------------
<br/>

### 11. 위치 추적
위치추적기의 이동 거리를 보고 최종적으로 얼마나 떨어져 있는지 계산하는 것이다.  
위치 추적기는 북쪽을 1, 동쪽을 2, 남쪽을 3, 서쪽을 4로 정하고 거리는 자연수로 나타낸다.  
결과 값은 ((북쪽+ or 남쪽-) 정수, (동쪽+ or 서쪽-) 정수)로 나타낸다. 각 정수를 이동한 거리를 타나내고 부호는 방향을 나타낸다.  

    1. 데이터 개수 N을 입력받는다.
    2. distance = [0,0] 생성하고 이 값은 최종 결과값을 나타낸다
    3. N 번 반복하면서 위치를 입력받는다
        3-1. D, L에 위치를 입력받는다  
        3-2. 만약 D이 1이라면 distance[0] += L  
        3-3. 그렇지 않고  D이 3이라면 distance[0] -= L  
        3-4. 그렇지 않고 D이 2이라면 distance[1] += L   
        3-5. 그렇지 않고 D이 4이라면 distance[1] -= L  
    4. 결과값 distance를 출력한다  
==> 시간복잡도 N 번 반복 O(N)

-------------
<br/>

### 12. 팀 나누기
6명 참가지의 실력을 주고 3명씩 그룹지을 때 두 그룹의 전체 실력이 같으면 possible, 같지 않으면 impossible으로 출력해라  
==> 결국 6C3의 조합값을 구하고 그 값들의 합들을 비교  
    1. 6개의 실력 값을 입력받아 리스트로 저장
    2. itertools의 combination을 사용해서 조합을 만들어 준다
    3. 한 그룹이 만들어지면 다른 그룹은 나머지 값으로 만들어 지기 때문에 그것을 비교해야 한다. 6C3은 20개가 나오는데 10개만 비교하면 자연스럽게 두 그룹을 모두 비교하는 것이다.  
    for 문으로  10번만 반복하면서 리스트에서 만들어진 조합을 제외한 나머지 값과 비교한다.  

        3-1. 실력 리스트를 복사한다.  
        3-2. 복사한 리스트에서 만들어진 조합의 값을 remove()로 지운다  
        3-3. 조합의 합과 복사한 리스트의 합을 비교한다.  
        3-4. 같은 합이 있으면 possible을 출력하고 break를 한다.  
        3-5. for문의 마지막인 9가 될때까지 없으면 impossible를 출력한다.  
==> 시간 복잡도 for문 O(N*(3 * O(N))), N = 6, remove() 시간복잡도 O(N)

-------------
<br/>

### 13. 가장 많이 등장하는 수
주어진 배열이 있을 때 가장 많이 등장하는 숫자를 찾는 문제이다. 만약 이때 빈도 수가 같은 숫자가 있다면 값이 작은 숫자를 출력한다.  

    1. 배열의 숫자 개수 N을 입력받는다
    2. 배열의 값들을 리스트로 입력받는다.
    3. dictonary(temp)를 생성한다.
    4. maxScore = 0, score = 0을 생성한다
    5. for문으로 배열 값(a)들을 반복한다.  
        5-1. 만약 temp.get(a) == None이면 temp[a] = 1  
        5-2. 그렇지 않다면 temp[a] += 1 를 한다  
        5-3. 만약 maxScore < temp[a] or (maxScore == temp[a] and score > a) 이라면,   
        (최대값이 크면 새로 바꾸고, 최대값이 같은데 숫자가 작으면 바꾼다)  
        maxScore = temp[a], score = a 를 넣는다.
    6. score를 출력한다.
==> 시간복잡도 : for문 O(N)

-------------
<br/>

### 14. 색 반전
헥사 코드로 변환된 색상값이 입력을 들어온다.  
#RRGBB로 나누어져 있고, 이 색의 반전색을 찾으려고 한다.  
반전 색은 예를 들어 RR값에 대해 10진수로 바꾸고 255- 10진수로 바꾼 값을 한 후 그 값을 다시 16진수로 변환하면 된다.  
그렇게 RGB에 대해 모두 변환을 하면 헥사 코드 반전 색을 찾을 수 있다.  

    1. 헥사코드(hex)를 입력받는다.
    2. result = [#]을 생성한다.
    3. 16진수 변환 코드, 10진수 변환 코드를 dictoinary(change10, change16)로 생성한다.
    4. for 문을 (1,6,2) i로 반복한다.
        4-1. decimal = change10[hex[i]] * 16 + change10[hex[i+1]] 로 색깔에 대한 10진수 값을 구한다.  
        4-2. decimal = 255- decimal을 해서 반전 색의 10진수 값을 구한다.  
        4-3. result.append(change16[decimal // 16]) 으로 16진수로 변환된 16자리 수를 넣는다.  
        4-4.  result.append(change16[decimal % 16]) 으로 16진수로 변환된 1의자리 수를 넣는다.  
    5. print를 할 때 join()을 사용해서 result를 문자열로 바꾸어 출력한다.  
==> 시간복잡도 for문, append() O(N/2 * 2) + join() O(N)  
즉 O(N/2 * 2) + O(N)

-------------
<br/>

### 15. 나무
나무가 일렬로 서 있다. 이때 왼쪽에 있는 나무가 1번째 나무이고, 맨 오른쪽 나무가 N번째 나무이다.  
1번째 나무 앞에서 나무들을 보았을 때 볼 수 있는 나무의 개수를 구하는 것이다.
그러므로 i 번째 나무는 i-1번째 나무보다 커야 볼 수 있다.  

    1. 나무의 개수 N을 입력받는다.
    2. 나무들을 입력받아 리스트 tree에 저장한다.
    3. height = tree[0], count = 1을 하여 첫번째 나무를 볼 수 있다고 저장한다.
    4. for 문을 (1,5) i 를 반복시킨다.  
        4-1. 만약 tree[i] > height 라면 height = tree[i] 이고 count += 1을 한다.  
    5. count를 출력한다.  
==> 시간복잡도 : for문 O(N-1)

-------------
<br/>

### 16. 반도
N X N 크기의 지도에 땅은 O, 바다는 X로 표시되어 있습니다.
땅의 삼면만 바다로 둘러싸인 반도를 찾으려고 한다.  

    1. N의 크기를 입력받는다
    2. 지도를 받는데 for문으로 N번 반복으로 이차원 리스트 map으로 받는다
    2-1. 반도의 개수를 저장할 count = 0, 바다의 개수 저장하는 sea = 0
    3. for문으로 N 번 반복한다.  
        3-1. 지도에서 각 모서리는 닿아있는 면이 2개만 있어서 반도가 되는 조건이 안되므로 이중 for문 시작과 끝에서 미리 빼 놓는다.  
        start = 1, end = N-1  
        3-3. for 문 (start, end) j로 반복한다.  
            3-3-1. 만약 map[i][j] == 'X' 면 continue  
            3-2-2. 만약 j-1 >=0 이고, map[i][j-1] == 'X' 이면 sea += 1
            3-2-3. 만약 j+1 <=N-1 이고, map[i][j+1] == 'X' 이면 sea += 1
            3-2-4. 만약 i-1 >= 0 이고, map[i-1][j] == 'X' 이면  sea += 1
            3-2-5. 만약 i+1 <=N-1 이고, map[i+1][j] == 'X' 이면  sea += 1
            3-2-6. 만약 sea == 3 이면 count += 1
            3-2-7. sea = 0으로 초기화
        3-4. 만약 map[i][0] == 'O'이면 start = 1 아니면 start = 0
        3-5. 만약 map[i][N-1] == 'O'이면 end = N-1 아니면 end = N
    4. count를 출력  
==> 시간복잡도 : 지도 입력 받기 O(N), 최악의 경우 이중 for문 O(N*N)  
O(N) + O(N * N)

-------------
<br/>

### 17. 비밀번호
비밀번호 힌트 숫자와 알파벳이 섞인 문자열이 주어진다. 이때 알파벳을 지운 뒤 나타나는 숫자 값들을 더한 값이 비밀번호이다. 문자열이 주어질때 비밀번호를 찾아라  

    1. 문자열을 입력 받는다.
    2. 문자열을 re.sub() 함수를 사용해서 문자열에 있는 알파벳 소문자를 빈칸으로 변환한다.
    3. 변환된 문자열을 int(), split() 함수를 사용해서 숫자를 담은 리스트로 변환한다.
    4. sum() 함수를 사용하여 합을 구한 결과 값을 출력한다.  
==> 시간복잡도 : re.sub() O(N), split() O(N)  
O(N) + O(N)

-------------
<br/>

### 18. 세포AB
세포 A, B 가 있다. A는 1분마다 세포 B로 변한다. B는 1분마다 새로운 세포 A,B 2개로 변환된다. 분 (N) 이 주어졌을 때 N분 이후 세포 A, B의 개수를 구해라  

    1. 분 N 을 입력받는다.
    2. list cell을 만들어 세포 A,B를 1 , 1 씩 저장한다.
    3. for 문을 N 번 반복한다.  
        3-1. tempA = cell[0] 으로 B로 변환하는 A를 저장한다.
        3-2. cell[0] -= cell[0] 으로 B로 변환된 A를 없앤다.
        3-3. cell[0] += cell[1] 으로 A로 변환된 B를 저장한다.
        3-4. cell[1] += tempA로 B로 변환된 A를 저장한다.
    4. cell 값을 출력한다.
==> 시간복잡도 : for문 O(N)

-------------
<br/>

### 19. 소수점 이진비트
양의 실수가 주어졌을 때 이진법으로 나타내라  

    1. 실수 N을 입력받는다.
    2. 이진으로 나타낼 공간 리스트 binary = ['0.']를 생성한다.
    3. while문으로 binary 길이가 11이 아닐때까지 반복한다.
        3-1. N *= 2 를 한다.
        3-2. 1번을 한 N에서 정수 부분을 추출하기 위해 integer = int(N)을 한다.
        3-3. binary.append(str(integer))를 해서 이진 값을 저장한다.
        3-4. N -= integer로 소수부분만 남긴다.
        3-5. 만약 N == 0이면 이진법으로 다 변환 한 것이므로 break
    4. join을 사용해서 binary를 문자열로 변환해 출력한다.
==> 시간복잡도 : 최악의 경우 while() O(10)  
str() O(1) : integer가 무조건 1자리 수이고, while문 안에 있으므로 10번 반복  
O(10) + O(10)

-------------
<br/>

### 20. 구독형 서비스
N명의 사람들이 주어지고 각 사람들별로 최대한 낼 수 있는 구독료를 제시합니다. 최대한 구독료를 많이 받기 위해 얼마로 책정해야 많은 돈을 벌 수 있는지 구해라  

    1. N명의 사람을 입력받습니다.
    2. N개의 구독료 제시 가격을 입력받습니다. buy
    3. sort()함수를 사용해서 가격을 오름차순으로 정렬합니다.
    5. maxTotal = 0 으로 저장한다.
    5. N번 반복 하는 for문을 실행한다.
        5-1. 만약 같은 값이 있을 수도 있고, 이전 값이 존재 할때,
        if i-1 >=0 and buy[i] == buy[i-1] 이면 continue로 넘어간다.
        5-2. 만약 maxTotal < buy[i] * (N-i) 이면 maxTotal = buy[i] * (N-i)
    6. maxTotal을 출력한다.
==> 시간복잡도 : sort() O(NlogN), for() O(N)  
O(NlogN) + O(N)  

-------------
<br/>

### 21. over_underflow
두 정수를 입력 받아 두 정수의 합이 -8 이상 7이하가 아니면 16을 더하거나 뺀 값을 출력하자  

    1. 두 정수를 입력받는다.
    2. bit 에 두 정수의 합을 저장한다.
    3. 만약 bit가 -8보다 작다면 +16 을 한 수를 출력한다.
    4. 그렇지 않고 bit 가 7보다 크다면 -16 을 한 수를 출력한다.
    5. 그렇지도 않다면 그냥 출력한다.  

-------------
<br/>

### 22. 수 계단
N 값이 주어지면 1층에 1개의 수, 2층에 2개의 수, i 층에 i개의 수, N층에 N개의 숫자를 출력하는 문제이다. 이 문제는 삼긱수 문제와 같고 삼각수는 n(n+1) /2 의 규칙을 가진다.

    1. N을 입력받는다.
    2. check = 1로 줄바꿈할 기준을 정한다.
    3. for 문으로 (1, N(N+1)/2) i로 반복한다.
        3-1. i를 출력한다. end = '' 로
        3-2. 만약 check(check+1) /2 == i 라면 print()를 하고 check += 1을 한다.
        3-3. 그렇지 않다면 print(end = ' ')로 한다.
==> 시간복잡도 : O(N(N+1)/2)

-------------
<br/>

### 23. 블럭 쌓기 수열


-------------
<br/>

### 24. 계승진법


-------------
<br/>

### 25. 피보나치 피보나치 수열


-------------
<br/>

### 26. 사내 복지


-------------
<br/>

### 27. 문서 통계


-------------
<br/>

### 28. 팰린드롬의 날


-------------
<br/>

### 29. 난수 생성


-------------
<br/>

### 30. 직각 삼각형

