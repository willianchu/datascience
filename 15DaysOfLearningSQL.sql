CREATE TABLE submissions (submission_date date, submission_id integer, hacker_id integer, score integer);
INSERT INTO "submissions" VALUES('2016-03-01',8494,20703,0);
INSERT INTO "submissions" VALUES('2016-03-01',22403,53473,15);
INSERT INTO "submissions" VALUES('2016-03-01',23965,79722,60);
INSERT INTO "submissions" VALUES('2016-03-01',30173,36396,70);
INSERT INTO "submissions" VALUES('2016-03-02',34928,20703,0);
INSERT INTO "submissions" VALUES('2016-03-02',38740,15758,60);
INSERT INTO "submissions" VALUES('2016-03-02',42769,79722,60);
INSERT INTO "submissions" VALUES('2016-03-02',44364,79722,60);
INSERT INTO "submissions" VALUES('2016-03-03',45440,20703,0);
INSERT INTO "submissions" VALUES('2016-03-03',49050,36396,70);
INSERT INTO "submissions" VALUES('2016-03-03',50273,79722,5);
INSERT INTO "submissions" VALUES('2016-03-04',50344,20703,0);
INSERT INTO "submissions" VALUES('2016-03-04',51360,44065,90);
INSERT INTO "submissions" VALUES('2016-03-04',54404,53473,65);
INSERT INTO "submissions" VALUES('2016-03-04',61533,79722,45);
INSERT INTO "submissions" VALUES('2016-03-05',72852,20703,0);
INSERT INTO "submissions" VALUES('2016-03-05',74546,38289,0);
INSERT INTO "submissions" VALUES('2016-03-05',76487,62529,0);
INSERT INTO "submissions" VALUES('2016-03-05',82439,36396,10);
INSERT INTO "submissions" VALUES('2016-03-05',9006,36396,40);
INSERT INTO "submissions" VALUES('2016-03-06',90404,20703,0);
CREATE TABLE hackers (hacker_id integer, name string);
INSERT INTO "hackers" VALUES(15758,'Rose');
INSERT INTO "hackers" VALUES(20703,'Angela');
INSERT INTO "hackers" VALUES(36396,'Frank');
INSERT INTO "hackers" VALUES(38289,'Patrick');
INSERT INTO "hackers" VALUES(44065,'Lisa');
INSERT INTO "hackers" VALUES(53473,'Kimberly');
INSERT INTO "hackers" VALUES(62529,'Bonnie');
INSERT INTO "hackers" VALUES(79722,'Michael');

-- expected output
-- 2016-03-01 112 81314 Denise 
-- 2016-03-02 59 39091 Ruby 
-- 2016-03-03 51 18105 Roy 
-- 2016-03-04 49 533 Patrick 
-- 2016-03-05 49 7891 Stephanie 
-- 2016-03-06 49 84307 Evelyn 
-- 2016-03-07 35 80682 Deborah 
-- 2016-03-08 35 10985 Timothy 
-- 2016-03-09 35 31221 Susan 
-- 2016-03-10 35 43192 Bobby 
-- 2016-03-11 35 3178 Melissa 
-- 2016-03-12 35 54967 Kenneth 
-- 2016-03-13 35 30061 Julia 
-- 2016-03-14 35 32353 Rose 
-- 2016-03-15 35 27789 Helen 

select submission_date ,( SELECT COUNT(distinct hacker_id)  
                        FROM Submissions s2  
                        WHERE s2.submission_date = s1.submission_date AND 
                        (SELECT COUNT(distinct s3.submission_date) 
                         FROM Submissions s3 
                         WHERE s3.hacker_id = s2.hacker_id AND  
         s3.submission_date < s1.submission_date) = dateDIFF(s1.submission_date , '2016-03-01')) ,

            (select hacker_id  from submissions s2 
             where s2.submission_date = s1.submission_date 
               group by hacker_id 
             order by count(submission_id) desc , hacker_id limit 1) as hack,
        (select name from hackers where hacker_id = hack)
        from 
        (select distinct submission_date from submissions) s1
        group by submission_date;