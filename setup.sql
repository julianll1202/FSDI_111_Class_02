CREATE TABLE task (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(128),
    subtitle VARCHAR(256),
    body TEXT,
    active BOOLEAN DEFAULT 1
);

INSERT INTO task (
    title,
    subtitle,
    body
) VALUES (
    "Wash the car",
    "Go outside and wash the car",
    "Either do it yoursel or take it to the car wash"
);

INSERT INTO task (
    title,
    subtitle,
    body
) VALUES (
    "Dinner",
    "Prepare dinner",
    "Tonight's dinner should be pizza or tacos; buy or order"
);