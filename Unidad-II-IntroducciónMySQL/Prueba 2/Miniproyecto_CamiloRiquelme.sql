/* Prueba 2 - Bases de Datos - Prof. Alex Slater
Nombre: Camilo Riquelme. */

/* Consulta 1: Calcular los promedios de temperatura y humedad, agrupados por
región. */

SELECT e.region, ROUND(AVG(h.promedio_humedad), 2) AS promedio_humedad, ROUND(AVG(t.promedio_temperatura), 2) AS promedio_temperatura
FROM estaciones AS e
JOIN (SELECT codigonacional, AVG(hrvalor) AS promedio_humedad
      FROM humedad
      GROUP BY codigonacional) AS h ON h.codigonacional = e.codigonacional
JOIN (SELECT codigonacional, AVG(tsvalor) AS promedio_temperatura
      FROM temperatura
      GROUP BY codigonacional) AS t ON t.codigonacional = e.codigonacional
GROUP BY e.region;


/* Consulta 2: Calcular los promedios de temperatura y humedad por década (1980,
1990, 2000, etc.), agrupados por región. */

-- Promedios Temperatura/Decada/Region
SELECT e.region, SUBSTRING(t.momento, 7, 4) AS decada, ROUND(AVG(t.tsvalor), 2) AS promedio_temperatura
FROM estaciones AS e
JOIN temperatura AS t ON e.codigonacional = t.codigonacional
GROUP BY e.region, SUBSTRING(t.momento, 7, 3);

-- Promedios Humedad/Decada/Region
SELECT e.region, SUBSTRING(h.momento, 7, 4) AS decada, ROUND(AVG(h.hrvalor), 2) AS promedio_humedad
FROM estaciones AS e
JOIN humedad AS h ON e.codigonacional = h.codigonacional
GROUP BY e.region, SUBSTRING(h.momento, 7, 3);


/* Consulta 3: Calcular la variación del promedio de temperatura para cada estación
meteorológica, comparando la década actual (2020s) con cada una de las
décadas anteriores. Los resultados deben estar agrupados por estación
meteorológica. */

SELECT e.nombre AS Estacion, 
    ROUND(AVG(CASE WHEN SUBSTRING(t.momento, 7, 3) = '202' THEN t.tsvalor END), 2) AS prom_2020s,
    ROUND(AVG(CASE WHEN SUBSTRING(t.momento, 7, 3) = '201' THEN t.tsvalor END), 2) AS prom_2010s,
    ROUND(AVG(CASE WHEN SUBSTRING(t.momento, 7, 3) = '201' THEN t.tsvalor END) - 
          AVG(CASE WHEN SUBSTRING(t.momento, 7, 3) = '202' THEN t.tsvalor END), 2) AS dif_2010s,
    ROUND(AVG(CASE WHEN SUBSTRING(t.momento, 7, 3) = '200' THEN t.tsvalor END), 2) AS prom_2000s,
    ROUND(AVG(CASE WHEN SUBSTRING(t.momento, 7, 3) = '200' THEN t.tsvalor END) - 
          AVG(CASE WHEN SUBSTRING(t.momento, 7, 3) = '202' THEN t.tsvalor END), 2) AS dif_2000s,
    ROUND(AVG(CASE WHEN SUBSTRING(t.momento, 7, 3) = '199' THEN t.tsvalor END), 2) AS prom_1990s,
    ROUND(AVG(CASE WHEN SUBSTRING(t.momento, 7, 3) = '199' THEN t.tsvalor END) - 
          AVG(CASE WHEN SUBSTRING(t.momento, 7, 3) = '202' THEN t.tsvalor END), 2) AS dif_1990s,
    ROUND(AVG(CASE WHEN SUBSTRING(t.momento, 7, 3) = '198' THEN t.tsvalor END), 2) AS prom_1980s,
    ROUND(AVG(CASE WHEN SUBSTRING(t.momento, 7, 3) = '198' THEN t.tsvalor END) - 
          AVG(CASE WHEN SUBSTRING(t.momento, 7, 3) = '202' THEN t.tsvalor END), 2) AS dif_1980s
FROM estaciones AS e
JOIN temperatura AS t ON e.codigonacional = t.codigonacional
GROUP BY e.nombre;


/* Consulta 4: Obtener el promedio mensual de temperatura y humedad relativa en
cada estación meteorológica. */

-- Promedio Temperatura/Mes/Estación
SELECT e.nombre AS estacion, SUBSTRING(t.momento, 4, 2) AS mes, ROUND(AVG(t.tsvalor), 2) AS promedio_temperatura
FROM estaciones AS e
JOIN temperatura AS t ON e.codigonacional = t.codigonacional
GROUP BY e.nombre, SUBSTRING(t.momento, 4, 2);

-- Promedio Humedad/Mes/Estación
SELECT e.nombre AS estacion, SUBSTRING(h.momento, 4, 2) AS mes, ROUND(AVG(h.hrvalor), 2) AS promedio_humedad
FROM estaciones AS e
JOIN humedad AS h ON e.codigonacional = h.codigonacional
GROUP BY e.nombre, SUBSTRING(h.momento, 4, 2);


/* Consulta 5: Identificar la estación meteorológica con la mayor desviación en la
temperatura media, comparando el promedio del año 2021 con el promedio de las
décadas de 1980 y 1990. */

-- Opción 1
SELECT e.nombre AS Estacion, temp_1980.prom_1980 AS Prom_1980,
    temp_1990.prom_1990 AS Promedio_1990,
    temp_2021.prom_2021 AS Promedio_2021,
    ABS(temp_2021.prom_2021 - temp_1980.prom_1980) AS Dif_1980,
    ABS(temp_2021.prom_2021 - temp_1990.prom_1990) AS Dif_1990
FROM estaciones AS e
LEFT JOIN (SELECT codigonacional, ROUND(AVG(tsvalor), 2) AS prom_1980
           FROM temperatura
           WHERE SUBSTRING(momento, 7, 4) BETWEEN "1980" AND "1989"
           GROUP BY codigonacional) AS temp_1980 
           ON e.codigonacional = temp_1980.codigonacional
LEFT JOIN (SELECT codigonacional, ROUND(AVG(tsvalor), 2) AS prom_1990
           FROM temperatura
           WHERE SUBSTRING(momento, 7, 4) BETWEEN "1990" AND "1999"
           GROUP BY codigonacional) AS temp_1990 
           ON e.codigonacional = temp_1990.codigonacional
LEFT JOIN (SELECT codigonacional, ROUND(AVG(tsvalor), 2) AS prom_2021
           FROM temperatura
           WHERE SUBSTRING(momento, 7, 4) = "2021"
           GROUP BY codigonacional) AS temp_2021 
           ON e.codigonacional = temp_2021.codigonacional
ORDER BY GREATEST(ABS(temp_2021.prom_2021 - temp_1980.prom_1980), ABS(temp_2021.prom_2021 - temp_1990.prom_1990)) DESC
LIMIT 1;

-- Opción 2
WITH Promedios_Desviaciones AS (SELECT e.nombre AS Estacion, '2021' AS Ano,
                                ROUND(AVG(CASE WHEN SUBSTRING(t.momento, 7, 4) = '2021' THEN t.tsvalor END), 2) AS Promedio_2021,
                                ROUND(STDDEV_POP(CASE WHEN SUBSTRING(t.momento, 7, 4) = '2021' THEN t.tsvalor END), 2) AS Desviacion_2021,
                                ROUND(AVG(CASE WHEN SUBSTRING(t.momento, 7, 4) BETWEEN '1980' AND '1989' THEN t.tsvalor END), 2) AS Promedio_1980s,
                                ROUND(STDDEV_POP(CASE WHEN SUBSTRING(t.momento, 7, 4) BETWEEN '1980' AND '1989' THEN t.tsvalor END), 2) AS Desviacion_1980s,
                                ROUND(AVG(CASE WHEN SUBSTRING(t.momento, 7, 4) BETWEEN '1990' AND '1999' THEN t.tsvalor END), 2) AS Promedio_1990s,
                                ROUND(STDDEV_POP(CASE WHEN SUBSTRING(t.momento, 7, 4) BETWEEN '1990' AND '1999' THEN t.tsvalor END), 2) AS Desviacion_1990s
             FROM estaciones AS e
             JOIN temperatura AS t ON e.codigonacional = t.codigonacional
             WHERE SUBSTRING(t.momento, 7, 4) IN ('2021', '1980', '1990')
             GROUP BY e.nombre)
SELECT Estacion,
CASE WHEN Desviacion_1980s = (SELECT MAX(Desviacion_1980s) FROM Promedios_Desviaciones) THEN Desviacion_1980s END AS Max_Desviacion_1980s,
CASE WHEN Desviacion_1990s = (SELECT MAX(Desviacion_1990s) FROM Promedios_Desviaciones) THEN Desviacion_1990s END AS Max_Desviacion_1990s,
CASE WHEN Desviacion_2021 = MAX(Desviacion_2021) OVER (PARTITION BY Estacion) THEN Promedio_2021 END AS Promedio_2021,
CASE WHEN Desviacion_2021 = MAX(Desviacion_2021) OVER (PARTITION BY Estacion) THEN Desviacion_2021 END AS Desviacion_2021,
CASE WHEN Desviacion_1990s = MAX(Desviacion_1990s) OVER (PARTITION BY Estacion) THEN Promedio_1990s END AS Promedio_1990s,
CASE WHEN Desviacion_1990s = MAX(Desviacion_1990s) OVER (PARTITION BY Estacion) THEN Desviacion_1990s END AS Desviacion_1990s,
CASE WHEN Desviacion_1980s = MAX(Desviacion_1980s) OVER (PARTITION BY Estacion) THEN Promedio_1980s END AS Promedio_1980s,
CASE WHEN Desviacion_1980s = MAX(Desviacion_1980s) OVER (PARTITION BY Estacion) THEN Desviacion_1980s END AS Desviacion_1980s
FROM Promedios_Desviaciones;


/* Consulta 6: Calcular el promedio de humedad relativa, agrupado por hora del día
y por región. */

SELECT e.region, SUBSTRING(h.momento, 12, 5) AS hora, ROUND(AVG(h.hrvalor), 2) AS promedio_humedad
FROM estaciones AS e
JOIN humedad AS h ON e.codigonacional = h.codigonacional
GROUP BY e.region, SUBSTRING(h.momento, 12, 5);


/* Consulta 7: Generar una consulta que calcule la diferencia porcentual en los
promedios de temperatura entre la década de 1980 y la década de 2020. */

SELECT prom_1980, prom_2020, ROUND((((prom_2020 - prom_1980) / prom_1980) * 100), 2) AS dif_porc
FROM (SELECT ROUND(AVG(tsvalor), 2) AS prom_1980
      FROM temperatura
      WHERE SUBSTRING(momento, 7, 4) BETWEEN "1980" AND "1989")
      AS temp_1980,
	(SELECT ROUND(AVG(tsvalor), 2) AS prom_2020
     FROM temperatura
     WHERE SUBSTRING(momento, 7, 4) BETWEEN "2020" AND "2029")
     AS temp_2020;
