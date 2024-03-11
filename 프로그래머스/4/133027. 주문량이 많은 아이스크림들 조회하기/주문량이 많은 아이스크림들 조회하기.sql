-- 코드를 입력하세요
SELECT J.FLAVOR
FROM FIRST_HALF AS F
RIGHT JOIN JULY AS J
ON F.SHIPMENT_ID = J.SHIPMENT_ID
GROUP BY J.FLAVOR
ORDER BY F.TOTAL_ORDER + SUM(J.TOTAL_ORDER) DESC
LIMIT 3