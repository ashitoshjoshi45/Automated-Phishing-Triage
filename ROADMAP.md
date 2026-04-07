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

#📍 Phase 4: Internal Threat Intel & Campaign Correlation
[x] Implement real-time honeypot log ingestion to extract local IOCs.
[x] Develop basic cross-referencing logic to match .eml IOCs against active honeypot threats.
[x] Upgrade the in-memory honeypot IOC set to a persistent local SQLite database.
[x] Develop correlation_engine.py to cross-reference IPs, senders, and hashes across multiple .eml files.
[ ] Generate a "Blast Radius" report identifying Patient Zero and the full scope of the internal phishing campaign.

📍 Phase 5: SIEM Integration & IR Handoff
[ ] Aggregate findings from the Parser, Enricher, and Correlation Engine.
[ ] Generate a structured JSON report formatted for automated ingestion into SIEMs (like Splunk or Wazuh).
[ ] Map outputs directly to the "Detection and Analysis" phase of the NIST Incident Response Lifecycle.