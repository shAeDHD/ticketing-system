DROP TABLE IF EXISTS metadatas;
DROP TABLE IF EXISTS ticket_headers;
DROP TABLE IF EXISTS note_activities;
DROP TABLE IF EXISTS other_activities;

CREATE TABLE metadatas (
    id INTEGER PRIMARY KEY,
    start_at TEXT,
    end_at TEXT,
    activities_count INTEGER
);

CREATE TABLE ticket_headers (
    id INTEGER PRIMARY KEY, 
    performed_at TEXT,
    ticket_id INTEGER,
    performer_type TEXT,
    performer_id INTEGER
);

CREATE TABLE note_activities (
    id INTEGER PRIMARY KEY,
    note_type INTEGER
);

CREATE TABLE other_activities (
    id INTEGER PRIMARY KEY,
    shipping_address TEXT,
    shipment_date TEXT,
    category TEXT,
    contacted_customer BOOLEAN,
    issue_type TEXT,
    source INTEGER,
    status TEXT,
    priority INTEGER,
    group_id TEXT,
    agent_id INTEGER,
    requester INTEGER,
    product TEXT
)