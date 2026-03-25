# 🗺️ Automated Phishing Triage - Development Roadmap

This document outlines the development phases for the Automated Phishing Triage module, a core component of the overarching Autonomous AI SOC Analyst architecture.

## 📍 Phase 1: Environment Setup & Basic Ingestion
* [x] Initialize project structure and virtual environment.
* [x] Write initial Python script to securely open, read, and parse raw `.eml` (email) files.
* [x] Extract basic metadata (Sender, Recipient, Subject, Date).

## 📍 Phase 2: Parsing & IOC Extraction
* [x] Implement regex/parsing logic to extract URLs from the email body.
* [x] Implement logic to extract IP addresses from email headers.
* [x] Safely detach and calculate SHA-256 hashes of file attachments.

## 📍 Phase 3: Threat Intelligence Enrichment
* [x] Integrate the **VirusTotal API**.
* [x] Automate reputation checks for extracted URLs, IPs, and file hashes.
* [x] Flag IOCs that cross a specific malicious threshold.

## 📍 Phase 4: Campaign Correlation & Blast Radius (Detection & Analysis)
* [ ] Build a local `SQLite` or in-memory database to store parsed email IOCs.
* [ ] Develop a `correlation_engine.py` to cross-reference IPs, senders, and hashes across multiple `.eml` files.
* [ ] Generate a "Blast Radius" report identifying Patient Zero and the full scope of the phishing campaign.

## 📍 Phase 5: Reporting & IR Handoff
* [ ] Aggregate findings from the Parser, Enricher, and Correlation Engine.
* [ ] Generate a structured text/JSON report formatted for immediate ingestion by Tier 2 analysts or SIEMs.
* [ ] Map outputs directly to the "Detection and Analysis" phase of the NIST Incident Response Lifecycle.