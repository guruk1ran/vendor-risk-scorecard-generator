-- V1__init.sql
-- Initial schema for Vendor Risk Scorecard

CREATE TABLE vendors (
    id SERIAL PRIMARY KEY,

    name VARCHAR(255) NOT NULL,
    category VARCHAR(100),

    -- risk score between 0–100
    risk_score INT NOT NULL CHECK (risk_score BETWEEN 0 AND 100),

    -- keeping status controlled to avoid random values later
    status VARCHAR(50) NOT NULL DEFAULT 'ACTIVE'
        CHECK (status IN ('ACTIVE', 'INACTIVE', 'HIGH_RISK')),

    description TEXT,
    ai_summary TEXT,

    -- soft delete (we’ll use this instead of actual delete)
    is_deleted BOOLEAN DEFAULT FALSE,

    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- indexes for common queries (search, filters, dashboard)
CREATE INDEX idx_vendors_name ON vendors(name);
CREATE INDEX idx_vendors_status ON vendors(status);
CREATE INDEX idx_vendors_risk_score ON vendors(risk_score);
CREATE INDEX idx_vendors_created_at ON vendors(created_at);

-- helps when we only fetch active (non-deleted) vendors
CREATE INDEX idx_vendors_active 
ON vendors(is_deleted)
WHERE is_deleted = FALSE;