-- 3-1번
SELECT 영화이름 FROM movies WHERE 상영시간>=150;

-- 3-2번
SELECT 영화코드, 영화이름 FROM movies WHERE 장르='애니메이션';

-- 3-3번
SELECT 영화이름 FROM movies WHERE 제작국가='덴마크' AND 장르='애니메이션';

-- 3-4번
SELECT 영화이름, 누적관객수 FROM movies WHERE 누적관객수>=1000000 AND 관람등급='청소년관람불가';

-- 3-5번
SELECT * FROM movies WHERE 개봉연도>=20000101 AND 개봉연도<=20091231;
SELECT * FROM movies WHERE 개봉연도 LIKE '200%';

-- 3-6번
SELECT DISTINCT 장르 FROM movies;
