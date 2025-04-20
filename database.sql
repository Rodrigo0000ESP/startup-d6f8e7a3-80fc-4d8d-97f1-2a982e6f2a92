CREATE TABLE receipts (
    date DATE NOT NULL,
    vendor VARCHAR(255) NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (date, vendor)
);