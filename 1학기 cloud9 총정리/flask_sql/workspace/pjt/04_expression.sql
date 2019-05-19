-- 4-1번
SELECT SUM(누적관객수) FROM movies;

-- 4-2번
SELECT 영화이름, MAX(누적관객수) AS 최대누적관객수 FROM movies;

-- 4-3번
SELECT 장르, MIN(상영시간) AS 최소상영시간 FROM movies;

-- 4-4번
SELECT SUM(누적관객수)/COUNT(영화코드) FROM movies WHERE 제작국가='한국';
SELECT ROUND(AVG(누적관객수), 0) FROM movies WHERE 제작국가='한국';

-- 4-5번
SELECT COUNT(*) FROM movies WHERE 관람등급='청소년관람불가';

-- 4-6번
SELECT COUNT(영화코드) FROM movies WHERE 상영시간>=100 AND 장르='애니메이션';
