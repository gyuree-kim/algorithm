-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME IN ("Lucy", "Ella", "Pickle", "Rogan", "Sabrina", "Mitty")

-- 이름에 el이 들어가는 동물 찾기
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE NAME LIKE "%EL%" AND ANIMAL_TYPE = "Dog"
ORDER BY NAME

-- 중성화 여부 파악하기
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE AS '중성화' -- WRONG
FROM ANIMAL_INS
WHERE SEX_UPON_INTAKE LIKE "SPAYED%" OR SEX_UPON_INTAKE LIKE "NEUTERED%"

-- https://mungto.tistory.com/285?category=734741
SELECT ANIMAL_ID, NAME, 
CASE WHEN SEX_UPON_INTAKE LIKE "%NE%" OR SEX_UPON_INTAKE 
LIKE "SP%" THEN 'O' ELSE 'X' END AS "중성화" 
FROM ANIMAL_INS
 
-- 오랜 기간 보호한 동물(2)
SELECT I.ANIMAL_ID, I.NAME
FROM ANIMAL_INS AS I, ANIMAL_OUTS AS O
WHERE I.ANIMAL_ID IN (SELECT ANIMAL_ID FROM ANIMAL_OUTS) AND I.ANIMAL_ID = O.ANIMAL_ID
ORDER BY O.DATETIME - I.DATETIME DESC
LIMIT 2

-- DATETIME에서 DATE로 형 변환
SELECT ANIMAL_ID, NAME, DATE(DATETIME) AS "날짜" --틀림
FROM ANIMAL_INS
ORDER BY ANIMAL_ID

SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME, "%Y-%m-%d") AS "날짜" --구글링!
FROM ANIMAL_INS
ORDER BY ANIMAL_ID