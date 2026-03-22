# 🎣 Automated Phishing Triage 

An automated security operations tool designed to ingest, analyze, and respond to reported phishing emails. This project simulates a Tier 1 SOC analyst workflow by extracting IOCs (Indicators of Compromise) and utilizing AI for threat scoring.

## 🚀 Core Features
* **Automated Ingestion:** Parses suspicious emails (.eml) or mailbox streams.
* **IOC Extraction:** Automatically extracts URLs, domains, IP addresses, and file hashes.
* **Threat Intelligence Enrichment:** Checks extracted IOCs against threat intelligence feeds (e.g., VirusTotal API).
* **Automated Reporting:** Generates a summarized triage report with a malicious confidence score.

---

## 🔍 Module 1: Automated EML Triage (`eml_parser.py`)

This component acts as the "Eyes" of the Autonomous SOC Analyst. It securely parses raw email files to extract high-fidelity artifacts for investigation.

**Key Features:**
* **Secure Ingestion:** Uses `BytesParser` to safely handle malformed or malicious email structures.
* **Header Forensic Tracking:** Extracts `Subject`, `From`, `To`, and captures all `Received` headers to trace the mail's actual origin path (Hops).
* **Artifact Extraction:** * **URLs:** Automatically identifies unique links using Regex.
  * **Attachments:** Detects and flags file payloads for downstream analysis.
* **Deduplication:** Integrated set-logic to ensure report clarity by removing duplicate indicators.
