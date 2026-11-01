CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    product VARCHAR(100),
    amount INT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

INSERT INTO users (id, name, email) VALUES 
    (1, 'Robin Windey', 'ro.windey@gmail.com'),
    (2, 'Kevin Kiefer', 'kevin@example.com');

INSERT INTO orders (user_id, product, amount) VALUES
    (1, 'Laptop', 1299.99),
    (2, 'Mouse', 29.99),
    (1, 'Keyboard', 89.99);