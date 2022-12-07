DROP TABLE IF EXISTS metadatas;
DROP TABLE IF EXISTS ticket_headers;
DROP TABLE IF EXISTS note_activities;
DROP TABLE IF EXISTS other_activites;

CREATE TABLE metadatas (
    start_at TEXT,
    end_at TEXT,
    activities_count INTEGER
);

CREATE TABLE ticket_headers (
    performed_at TEXT,
    id INTEGER PRIMARY KEY, 
    performer_type TEXT,
    performer_id INTEGER
);

CREATE TABLE note_activities (
    id INTEGER,
    type INTEGER
);

CREATE TABLE other_activites (
    shipping_address TEXT,
    shipment_date TEXT,
    category TEXT,
    contactedP_customer BOOLEAN,
    issue_type TEXT,
    souce INTEGER,
    status TEXT,
    priority INTEGER,
    group_id TEXT,
    agent_id INTEGER,
    requester INTEGER,
    product TEXT
)