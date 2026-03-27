import ollama

class AIAnalyzer:
    def __init__(self, model_name="llama3"):
        """Initializes the analyzer using a local Ollama model for data privacy."""
        self.model_name = model_name

    def analyze_email_context(self, email_body):
        """Passes the email body to the local LLM to detect social engineering."""
        if not email_body:
            return "No email body provided for analysis."

        prompt = f"""
        You are an expert Tier 3 SOC Analyst. Review the following email body for phishing attempts and social engineering tactics.
        
        Analyze the text and provide a concise report focusing on:
        1. Urgency Cues (Are they trying to panic the user?)
        2. Authority Spoofing (Are they pretending to be a CEO, IT admin, or bank?)
        3. Suspicious Requests (Are they asking for credentials, wire transfers, or gift cards?)
        4. Overall Phishing Probability (Low, Medium, High) with a 1-sentence justification.

        Email Body to Analyze:
        '''
        {email_body}
        '''
        """
        
        try:
            # Calls the local Ollama API
            response = ollama.chat(model=self.model_name, messages=[
                {
                    'role': 'user',
                    'content': prompt,
                },
            ])
            return response['message']['content']
        except Exception as e:
            return f"Error during local AI analysis: {e}. Is Ollama running?"

# --- Quick Test Block ---
if __name__ == "__main__":
    # Uses llama3 by default, completely free and local
    analyzer = AIAnalyzer(model_name="llama3")
    
    sample_phish = "URGENT: Your account will be locked in 2 hours. Click here to verify your credentials immediately or lose access to your payroll."
    
    print(f"[*] Running Local AI Context Analysis using {analyzer.model_name}...")
    result = analyzer.analyze_email_context(sample_phish)
    print("\n--- AI SOC Analyst Report ---\n")
    print(result)