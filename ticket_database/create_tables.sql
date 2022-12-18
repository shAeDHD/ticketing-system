DROP TABLE IF EXISTS metadata;
DROP TABLE IF EXISTS tickets;
DROP TABLE IF EXISTS note_activities;
DROP TABLE IF EXISTS other_activities;

CREATE TABLE metadata (
    id INTEGER PRIMARY KEY,
    performer_id INTEGER,
    start_at TEXT,
    end_at TEXT,
    activities_count INTEGER
);

CREATE TABLE tickets (
    id INTEGER PRIMARY KEY,
    ticket_id INTEGER,
    activities_assigned INTEGER
)


CREATE TABLE note_ticket (
    id INTEGER PRIMARY KEY, 
    performed_at TEXT,
    performer_type TEXT,
    performer_id INTEGER,
    note_id INTEGER
    note_type INTEGER
);

CREATE TABLE other_ticket (
    id INTEGER PRIMARY KEY, 
    performed_at TEXT,
    performer_type TEXT,
    performer_id INTEGER,
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
