CREATE TABLE STATION (
    STATION_ID INTEGER NOT NULL,
    CITY VARCHAR(50) NOT NULL,
    STATE VARCHAR(2) NOT NULL,
    LAT_N DECIMAL(9,6) NOT NULL,
    LONG_W DECIMAL(9,6) NOT NULL,
);

-- A median is defined as a number separating the higher half of a data set from the lower half. Query the median of the Northern Latitudes (LAT_N) from STATION and round your answer to 4 decimal places.

-- where LAT_N is the northern latitude and LONG_W is the western longitude.

SELECT LAT_N FROM STATION ORDER BY LAT_N LIMIT (SELECT COUNT(LAT_N) / 2 FROM STATION);

(SELECT ROUND(COUNT(LAT_N) / 2) FROM STATION)
