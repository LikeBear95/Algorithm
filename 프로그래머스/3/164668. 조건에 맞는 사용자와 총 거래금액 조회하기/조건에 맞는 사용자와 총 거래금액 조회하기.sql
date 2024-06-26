-- 코드를 입력하세요
SELECT
    WRITER_ID AS USER_ID,
    NICKNAME,
    SUM(PRICE) AS TOTAL_SALES
FROM
    USED_GOODS_BOARD
LEFT JOIN USED_GOODS_USER
    ON USED_GOODS_USER.USER_ID = USED_GOODS_BOARD.WRITER_ID
WHERE
    STATUS = 'DONE'
GROUP BY
    NICKNAME
HAVING
    TOTAL_SALES >= 700000
ORDER BY
    TOTAL_SALES