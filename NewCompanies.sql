-- Amber's conglomerate corporation just acquired some new companies. Each of the companies follows this hierarchy:
-- Founder > Lead Manager > Senior Manager > Manager > Employee

-- Given the table schemas below, write a query to print the company_code, founder name, total number of lead managers, total number of senior managers, total number of managers, and total number of employees. Order your output by ascending company_code.

-- Note:

-- The tables may contain duplicate records.
-- The company_code is string, so the sorting should not be numeric. For example, if the company_codes are C_1, C_2, and C_10, then the ascending company_codes will be C_1, C_10, and C_2.

CREATE TABLE Company 
(
    company_code VARCHAR(6) NOT NULL,
    founder VARCHAR(20) NOT NULL,
);

CREATE TABLE Lead_Manager 
(
    company_code VARCHAR(6) NOT NULL,
    lead_manager_code VARCHAR(6) NOT NULL,
);

CREATE TABLE Senior_Manager 
(
    senior_manager_code VARCHAR(6) NOT NULL,
    lead_manager_code VARCHAR(6) NOT NULL,
    company_code VARCHAR(6) NOT NULL,
);

CREATE TABLE Manager 
(
    manager_code VARCHAR(6) NOT NULL,
    senior_manager_code VARCHAR(6) NOT NULL,
    lead_manager_code VARCHAR(6) NOT NULL,
    company_code VARCHAR(6) NOT NULL,
);

CREATE TABLE Employee 
(
    employee_code VARCHAR(6) NOT NULL,
    manager_code VARCHAR(6) NOT NULL,
    senior_manager_code VARCHAR(6) NOT NULL,
    lead_manager_code VARCHAR(6) NOT NULL,
    company_code VARCHAR(6) NOT NULL,
);

SELECT c.company_code, c.founder, COUNT(DISTINCT lm.lead_manager_code) AS lead_managers, COUNT(DISTINCT sm.senior_manager_code) AS senior_managers, COUNT(DISTINCT m.manager_code) AS managers, COUNT(DISTINCT e.employee_code) AS employees
FROM Company c
LEFT JOIN Lead_Manager lm ON c.company_code = lm.company_code
LEFT JOIN Senior_Manager sm ON c.company_code = sm.company_code
LEFT JOIN Manager m ON c.company_code = m.company_code
LEFT JOIN Employee e ON c.company_code = e.company_code
GROUP BY c.company_code, c.founder
ORDER BY c.company_code;
