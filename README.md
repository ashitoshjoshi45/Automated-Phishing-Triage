## 🔍 Module 1: Automated EML Triage (`eml_parser.py`)
This component acts as the "Eyes" of the Autonomous SOC Analyst. It securely parses raw email files to extract high-fidelity artifacts for investigation.

### Key Features:
* **Secure Ingestion:** Uses `BytesParser` to safely handle malformed or malicious email structures.
* **Header Forensic Tracking:** Extracts `Subject`, `From`, `To`, and captures all `Received` headers to trace the mail's actual origin path (Hops).
* **Artifact Extraction:** * **URLs:** Automatically identifies unique links using Regex.
    * **Attachments:** Detects and flags file payloads for downstream analysis.
* **Deduplication:** Integrated set-logic to ensure report clarity by removing duplicate indicators.