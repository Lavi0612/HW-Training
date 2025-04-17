CREATE DATABASE OrderManagementDB;
GO

USE OrderManagementDB;
GO

CREATE TABLE Users (
    userId INT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL,
    role VARCHAR(20) CHECK (role IN ('Admin', 'User')) NOT NULL
);

CREATE TABLE Products (
    productId INT PRIMARY KEY,
    productName VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2),
    quantityInStock INT,
    type VARCHAR(50) CHECK (type IN ('Electronics', 'Clothing')) NOT NULL
);

CREATE TABLE Electronics (
    productId INT PRIMARY KEY,
    brand VARCHAR(100),
    warrantyPeriod INT,
    FOREIGN KEY (productId) REFERENCES Products(productId)
);

CREATE TABLE Clothing (
    productId INT PRIMARY KEY,
    size VARCHAR(10),
    color VARCHAR(50),
    FOREIGN KEY (productId) REFERENCES Products(productId)
);

CREATE TABLE Orders (
    orderId INT PRIMARY KEY,
    userId INT,
    orderDate DATE DEFAULT GETDATE(),
    FOREIGN KEY (userId) REFERENCES Users(userId)
);

CREATE TABLE OrderProduct (
    orderId INT,
    productId INT,
    quantity INT,
    PRIMARY KEY (orderId, productId),
    FOREIGN KEY (orderId) REFERENCES Orders(orderId),
    FOREIGN KEY (productId) REFERENCES Products(productId)
);
--
INSERT INTO Users VALUES (1, 'Arun', 'arun123', 'User');
INSERT INTO Users VALUES (2, 'Divya', 'divya456', 'User');
INSERT INTO Users VALUES (3, 'Neha', 'neha789', 'Admin');
INSERT INTO Users VALUES (4, 'Karan', 'karan101', 'User');
INSERT INTO Users VALUES (5, 'Meera', 'meera202', 'Admin');
INSERT INTO Users VALUES (6, 'Rohit', 'rohit111', 'User');
INSERT INTO Users VALUES (7, 'Simran', 'sim999', 'User');
INSERT INTO Users VALUES (8, 'Ravi', 'ravi321', 'Admin');
INSERT INTO Users VALUES (9, 'Kajal', 'kajal101', 'User');
INSERT INTO Users VALUES (10, 'Ankur', 'ankur789', 'User');
INSERT INTO Users VALUES (11, 'Pooja', 'poo555', 'User');
INSERT INTO Users VALUES (12, 'Manoj', 'manoj808', 'User');
INSERT INTO Users VALUES (13, 'Sneha', 'sneha007', 'Admin');
INSERT INTO Users VALUES (14, 'Vikas', 'vikasxyz', 'User');
INSERT INTO Users VALUES (15, 'Isha', 'isha999', 'User');
INSERT INTO Users VALUES (16, 'Rahul', 'rahul123', 'Admin');
INSERT INTO Users VALUES (17, 'Priya', 'priya007', 'User');
INSERT INTO Users VALUES (18, 'Deepak', 'deep123', 'User');
INSERT INTO Users VALUES (19, 'Reena', 'reena789', 'Admin');
INSERT INTO Users VALUES (20, 'Gaurav', 'gaurav999', 'User');
--
INSERT INTO Products VALUES (101, 'TV', 'Smart LED TV', 20000, 15, 'Electronics');
INSERT INTO Products VALUES (102, 'Phone', 'Android Phone', 15000, 20, 'Electronics');
INSERT INTO Products VALUES (103, 'Shirt', 'Cotton Shirt', 800, 50, 'Clothing');
INSERT INTO Products VALUES (104, 'Jeans', 'Slim Fit Jeans', 1400, 35, 'Clothing');
INSERT INTO Products VALUES (105, 'Laptop', 'Gaming Laptop', 50000, 10, 'Electronics');
INSERT INTO Products VALUES (106, 'Kurta', 'Ethnic Wear', 1000, 25, 'Clothing');
INSERT INTO Products VALUES (107, 'Washing Machine', 'Front Load', 25000, 8, 'Electronics');
INSERT INTO Products VALUES (108, 'T-shirt', 'Casual Tee', 499, 60, 'Clothing');
INSERT INTO Products VALUES (109, 'Refrigerator', 'Double Door', 28000, 12, 'Electronics');
INSERT INTO Products VALUES (110, 'Blazer', 'Formal Wear', 3000, 18, 'Clothing');
INSERT INTO Products VALUES (111, 'Microwave', 'Convection', 12000, 14, 'Electronics');
INSERT INTO Products VALUES (112, 'Shoes', 'Running Shoes', 2400, 20, 'Clothing');
INSERT INTO Products VALUES (113, 'Camera', 'DSLR', 45000, 9, 'Electronics');
INSERT INTO Products VALUES (114, 'Saree', 'Silk Saree', 3500, 13, 'Clothing');
INSERT INTO Products VALUES (115, 'Tablet', 'Android Tablet', 10000, 11, 'Electronics');
INSERT INTO Products VALUES (116, 'Skirt', 'Denim Skirt', 899, 17, 'Clothing');
INSERT INTO Products VALUES (117, 'Air Conditioner', '1.5 Ton AC', 33000, 6, 'Electronics');
INSERT INTO Products VALUES (118, 'Sweater', 'Woollen Sweater', 1300, 19, 'Clothing');
INSERT INTO Products VALUES (119, 'Smartwatch', 'Fitness Watch', 4999, 24, 'Electronics');
INSERT INTO Products VALUES (120, 'Jacket', 'Winter Jacket', 2800, 15, 'Clothing');
--
INSERT INTO Electronics VALUES (101, 'Sony', 24);
INSERT INTO Electronics VALUES (102, 'Samsung', 18);
INSERT INTO Electronics VALUES (105, 'Asus', 12);
INSERT INTO Electronics VALUES (107, 'Whirlpool', 36);
INSERT INTO Electronics VALUES (109, 'LG', 24);
INSERT INTO Electronics VALUES (111, 'IFB', 12);
INSERT INTO Electronics VALUES (113, 'Canon', 18);
INSERT INTO Electronics VALUES (115, 'Lenovo', 12);
INSERT INTO Electronics VALUES (117, 'Voltas', 24);
INSERT INTO Electronics VALUES (119, 'Noise', 6);
--
INSERT INTO Clothing VALUES (103, 'M', 'Blue');
INSERT INTO Clothing VALUES (104, 'L', 'Black');
INSERT INTO Clothing VALUES (106, 'S', 'Green');
INSERT INTO Clothing VALUES (108, 'M', 'White');
INSERT INTO Clothing VALUES (110, 'XL', 'Navy');
INSERT INTO Clothing VALUES (112, '9', 'Gray');
INSERT INTO Clothing VALUES (114, 'Free', 'Red');
INSERT INTO Clothing VALUES (116, 'S', 'Black');
INSERT INTO Clothing VALUES (118, 'M', 'Brown');
INSERT INTO Clothing VALUES (120, 'L', 'Olive');
--
INSERT INTO Orders VALUES (1001, 1, '2025-04-01');
INSERT INTO Orders VALUES (1002, 2, '2025-04-02');
INSERT INTO Orders VALUES (1003, 3, '2025-04-03');
INSERT INTO Orders VALUES (1004, 4, '2025-04-04');
INSERT INTO Orders VALUES (1005, 5, '2025-04-05');
INSERT INTO Orders VALUES (1006, 6, '2025-04-06');
INSERT INTO Orders VALUES (1007, 7, '2025-04-07');
INSERT INTO Orders VALUES (1008, 8, '2025-04-08');
INSERT INTO Orders VALUES (1009, 9, '2025-04-09');
INSERT INTO Orders VALUES (1010, 10, '2025-04-10');
INSERT INTO Orders VALUES (1011, 11, '2025-04-11');
INSERT INTO Orders VALUES (1012, 12, '2025-04-12');
INSERT INTO Orders VALUES (1013, 13, '2025-04-13');
INSERT INTO Orders VALUES (1014, 14, '2025-04-14');
INSERT INTO Orders VALUES (1015, 15, '2025-04-15');
INSERT INTO Orders VALUES (1016, 16, '2025-04-16');
INSERT INTO Orders VALUES (1017, 17, '2025-04-17');
INSERT INTO Orders VALUES (1018, 18, '2025-04-18');
INSERT INTO Orders VALUES (1019, 19, '2025-04-19');
INSERT INTO Orders VALUES (1020, 20, '2025-04-20');
--
INSERT INTO OrderProduct VALUES (1001, 101, 1);
INSERT INTO OrderProduct VALUES (1002, 102, 1);
INSERT INTO OrderProduct VALUES (1003, 103, 2);
INSERT INTO OrderProduct VALUES (1004, 104, 1);
INSERT INTO OrderProduct VALUES (1005, 105, 1);
INSERT INTO OrderProduct VALUES (1006, 106, 2);
INSERT INTO OrderProduct VALUES (1007, 107, 1);
INSERT INTO OrderProduct VALUES (1008, 108, 3);
INSERT INTO OrderProduct VALUES (1009, 109, 1);
INSERT INTO OrderProduct VALUES (1010, 110, 1);
INSERT INTO OrderProduct VALUES (1011, 111, 1);
INSERT INTO OrderProduct VALUES (1012, 112, 1);
INSERT INTO OrderProduct VALUES (1013, 113, 1);
INSERT INTO OrderProduct VALUES (1014, 114, 1);
INSERT INTO OrderProduct VALUES (1015, 115, 1);
INSERT INTO OrderProduct VALUES (1016, 116, 1);
INSERT INTO OrderProduct VALUES (1017, 117, 1);
INSERT INTO OrderProduct VALUES (1018, 118, 1);
INSERT INTO OrderProduct VALUES (1019, 119, 1);
INSERT INTO OrderProduct VALUES (1020, 120, 1);
--
SELECT name FROM sqlite_master WHERE type='table' AND name='Users';








