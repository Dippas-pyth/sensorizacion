WITH Franjas_edad AS (
    SELECT
        ID,
        NAME,
        AGE,
        EMAIL,
        SPORT,
        CASE
            WHEN AGE BETWEEN 18 AND 30 THEN '18-30'
            WHEN AGE BETWEEN 31 AND 50 THEN '31-50'
            WHEN AGE BETWEEN 51 AND 70 THEN '51-70'
            WHEN AGE > 70 THEN '71+'
            ELSE 'Menor de 18'
        END AS franjaedad
    FROM Users
),
Conteo_deportes AS (
    SELECT
        franjaedad,
        SPORT,
        COUNT(*) AS cantidad,
        RANK() OVER (PARTITION BY franjaedad ORDER BY COUNT(*) DESC) AS ranking
    FROM Franjas_edad
    GROUP BY franjaedad, SPORT
)

SELECT 
    franjaedad,
    SPORT as deporte_mayoritario,
    cantidad
FROM Conteo_deportes
WHERE ranking = 1
ORDER BY 
    CASE franjaedad
        WHEN '18-30' THEN 1
        WHEN '31-50' THEN 2
        WHEN '51-70' THEN 3
        WHEN '71+' THEN 4
        ELSE 5
    END;