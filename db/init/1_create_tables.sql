CREATE DATABASE IF NOT EXISTS spoiler_label_db;

USE spoiler_label_db;

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name TEXT NOT NULL,
    password TEXT NOT NULL,
    progress INT NOT NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS labels (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    video_id TEXT NOT NULL,
    user TEXT NOT NULL,
    spoiler_degree INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS images (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    video_id TEXT NOT NULL,
    channel TEXT
);