-- Create a new database called 'hbtn_0c_0;'
-- Connect to the 'master' database to run this snippet
USE master
GO
-- Create the new database if it does not exist already
IF NOT EXISTS (
    SELECT name
        FROM sys.databases
        WHERE name = N'hbtn_0c_0;'
)
CREATE DATABASE hbtn_0c_0;
GO