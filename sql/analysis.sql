SELECT * FROM jobs;

SELECT title, AVG(salary) AS avg_salary
FROM jobs
GROUP BY title;

SELECT location, COUNT(*) AS total_jobs
FROM jobs
GROUP BY location;
