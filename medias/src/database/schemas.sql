CREATE TABLE IF NOT EXISTS activity_entries (
    id TEXT PRIMARY KEY,               -- Maps to args['identifier']
    begin_time TEXT NOT NULL,          -- Maps to args['btime'] (e.g., '08h45')
    end_time TEXT NOT NULL,            -- Maps to args['etime'] (e.g., '11h15')
    duration TEXT NOT NULL,            -- Maps to calculated DURATION (e.g., '02h30')
    title TEXT NOT NULL,               -- Maps to args['title']
    tags TEXT,                         -- Maps to args['tags']
    description TEXT,                  -- Maps to args['description']
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    modified_at DATETIME
);
