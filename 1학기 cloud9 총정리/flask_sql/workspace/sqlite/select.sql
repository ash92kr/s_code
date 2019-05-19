-- 테이블 값 모두 가져오기
SELECT * FROM classmate;


-- 특정 컬럼만 가져오기
SELECT id, name FROM classmate;


-- 상위 2개 열만 가져오기
SELECT id, name FROM classmate LIMIT 2;


-- 앞의 2개를 생략하고 그 다음 것을 1개 가져온다
SELECT * FROM classmate LIMIT 1 OFFSET 2;


-- 특정 값을 가지는 행 전체 가져오기
SELECT * FROM classmate WHERE address="서울";
SELECT * FROM classmate WHERE id=2;
SELECT name FROM classmate WHERE address="서울";


-- 중복 행 제거하기
SELECT DISTINCT age FROM classmate;


