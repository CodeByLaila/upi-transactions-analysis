CREATE DATABASE digital_payments_db;
SHOW DATABASES;
USE digital_payments_db;
SELECT * FROM transactions
LIMIT 10;
SELECT COUNT(*) AS total_transactions
FROM transactions;
SELECT
    Status,
    COUNT(*) AS Total_Transactions
FROM transactions
GROUP BY Status;
SELECT
    Status,
    COUNT(*) AS Total,
    ROUND(
        COUNT(*) * 100.0 / (SELECT COUNT(*) FROM transactions),
        2
    ) AS Percentage
FROM transactions
GROUP BY Status;
SELECT
    Status,
    ROUND(AVG(`Amount (INR)`), 2) AS Average_Amount
FROM transactions
GROUP BY Status;
SELECT
    `Sender Name`,
    COUNT(*) AS Total_Transactions
FROM transactions
GROUP BY `Sender Name`
ORDER BY Total_Transactions DESC
LIMIT 5;
SELECT
    Status,
    ROUND(SUM(`Amount (INR)`), 2) AS Total_Amount
FROM transactions
GROUP BY Status;
SELECT
    DATE(Timestamp) AS Transaction_Date,
    COUNT(*) AS Total_Transactions,
    ROUND(SUM(`Amount (INR)`), 2) AS Total_Amount
FROM transactions
GROUP BY DATE(Timestamp)
ORDER BY Transaction_Date;
SELECT
    HOUR(Timestamp) AS Transaction_Hour,
    COUNT(*) AS Total_Transactions
FROM transactions
GROUP BY HOUR(Timestamp)
ORDER BY Total_Transactions DESC;
SELECT
    COUNT(*) AS Failed_Transactions,
    ROUND(SUM(`Amount (INR)`), 2) AS Total_Failed_Amount,
    ROUND(AVG(`Amount (INR)`), 2) AS Average_Failed_Amount,
    ROUND(MAX(`Amount (INR)`), 2) AS Largest_Failed_Transaction
FROM transactions
WHERE Status = 'FAILED';
SELECT
    `Receiver Name`,
    COUNT(*) AS Total_Transactions,
    ROUND(SUM(`Amount (INR)`), 2) AS Total_Amount_Received
FROM transactions
GROUP BY `Receiver Name`
ORDER BY Total_Transactions DESC
LIMIT 5;
