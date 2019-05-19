sqlite3 pjt.sqlite3
.databases

--1-1번
CREATE TABLE movies (
'영화코드' INTEGER PRIMARY KEY,
'영화이름' TEXT,
'관람등급' TEXT,
'감독' TEXT,
'개봉연도' INTEGER,
'누적관객수' INTEGER,
'상영시간' INTEGER,
'제작국가' TEXT,
'장르' TEXT
);


--1-2번
.mode csv   -- csv 읽어오는 모드
.read 01_create_table.sql    -- 스키마 생성
.import boxoffice.csv movies

.headers on
.mode column


--1-3번
SELECT * FROM movies;
