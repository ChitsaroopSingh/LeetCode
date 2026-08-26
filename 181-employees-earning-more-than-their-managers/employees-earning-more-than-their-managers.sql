# Write your MySQL query statement below
SELECT name AS Employee FROM Employee AS emp
WHERE salary > (
    SELECT salary FROM Employee
    WHERE id = emp.managerId
);