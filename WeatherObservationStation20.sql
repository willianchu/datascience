CREATE TABLE STATION (
    STATION_ID INTEGER NOT NULL,
    CITY VARCHAR(50) NOT NULL,
    STATE VARCHAR(2) NOT NULL,
    LAT_N DECIMAL(9,6) NOT NULL,
    LONG_W DECIMAL(9,6) NOT NULL,
);

-- oracle sql
-- SELECT ROUND(MEDIAN(LAT_N), 4) FROM STATION;
-- correct anwser 83.8913

-- mysql sql
-- there is no median in mysql
-- so we need to use subquery
-- For Median:
-- SELECT LAT_N FROM STATION GROUP BY LAT_N HAVING SUM(SIGN(1-SIGN(LAT-N))) = COUNT(*)+1/2;



-- A median is defined as a number separating the higher half of a data set from the lower half. Query the median of the Northern Latitudes (LAT_N) from STATION and round your answer to 4 decimal places.







