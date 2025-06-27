-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS user;
USE user;

-- Drop existing tables (optional, useful during resets)
DROP TABLE IF EXISTS jobs;
DROP TABLE IF EXISTS users;

-- Create users table
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(20) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_date DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Create jobs table
CREATE TABLE jobs (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    company_name VARCHAR(100) NOT NULL,
    location VARCHAR(100) NOT NULL,
    job_type VARCHAR(50) NOT NULL,
    description TEXT,
    skills TEXT,
    reference VARCHAR(40) NOT NULL,
    date_created DATETIME DEFAULT CURRENT_TIMESTAMP,
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);