CREATE TABLE pipeline (
    pipeline_id INTEGER PRIMARY KEY AUTOINCREMENT,
    pipeline_name TEXT NOT NULL,
    pipeline_version TEXT NOT NULL
);
CREATE TABLE running_state (
    run_id INTEGER PRIMARY KEY AUTOINCREMENT,
    pipeline_id INTEGER NOT NULL,
    resource_id INTEGER NOT NULL,
    running_status TEXT NOT NULL,
    working_directory TEXT NOT NULL,
    FOREIGN KEY (pipeline_id) REFERENCES pipeline(pipeline_id),
    FOREIGN KEY (resource_id) REFERENCES resources(resource_id)
);
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE profile (
    profile_id INTEGER PRIMARY KEY AUTOINCREMENT,
    profile_name TEXT NOT NULL,
    pipeline_id INTEGER NOT NULL,
    profile_executor TEXT NOT NULL,
    FOREIGN KEY (pipeline_id) REFERENCES pipeline(pipeline_id)
);