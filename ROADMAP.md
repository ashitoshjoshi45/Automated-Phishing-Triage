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
* [ ] Flag IOCs that cross a specific malicious threshold.

## 📍 Phase 4: AI Context Analysis
* [ ] Integrate the **Google Gemini API**.
* [ ] Pass the email body to the LLM with a highly tuned system prompt.
* [ ] Analyze text for social engineering tactics, urgency cues, and zero-day phishing patterns.

## 📍 Phase 5: Reporting & Integration
* [ ] Aggregate findings from Phase 2, 3, and 4.
* [ ] Generate a structured JSON or Markdown report for the SOC analyst.
* [ ] Prepare the module for integration into the main Autonomous AI SOC Analyst engine.