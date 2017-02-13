SELECT count(name) FROM jobs WHERE id IN
  (SELECT job_id from jobs_locations where location_name='New York City Metro Area');

SELECT name FROM jobs WHERE id IN
  (SELECT job_id from jobs_locations where location_name='New York City Metro Area');
