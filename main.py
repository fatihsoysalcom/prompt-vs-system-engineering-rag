import textwrap

# --- Simulated Components for Demonstration ---

# A very basic "Large Language Model" simulator
def simulated_llm(prompt: str) -> str:
    """
    Simulates an LLM's response. Without specific context, it might be generic
    or even "hallucinate" if asked about specific, non-general knowledge.
    With context, it should use the provided information.
    """
    prompt_lower = prompt.lower()
    
    if "prompt engineering" in prompt_lower and "system engineering" in prompt_lower:
        return "Prompt engineering focuses on crafting effective prompts. System engineering encompasses a broader design for robust AI solutions."
    elif "prompt engineering" in prompt_lower:
        return "Prompt engineering is about designing effective inputs for AI models."
    elif "system engineering" in prompt_lower:
        return "System engineering for AI involves designing, integrating, and managing complex AI components for reliability and scalability."
    elif "kurumsal yapay zeka" in prompt_lower or "enterprise ai" in prompt_lower:
        return "Enterprise AI solutions require careful planning beyond simple prompting."
    elif "finansal rapor" in prompt_lower or "financial report" in prompt_lower:
        if "gelir" in prompt_lower or "revenue" in prompt_lower:
            return "Without specific data, I can't provide exact financial figures. Enterprise AI needs integrated data sources."
        return "Financial reports contain various metrics like revenue, expenses, and profit."
    elif "gelir" in prompt_lower and "1.5 milyar tl" in prompt_lower:
         return "Şirketinizin 2023 yılı geliri 1.5 Milyar TL'dir. (Your company's 2023 revenue is 1.5 Billion TL.)"
    elif "gelir" in prompt_lower or "revenue" in prompt_lower:
         return "Revenue is the income generated from normal business operations."
    
    return "I'm a simulated AI. Please provide more context or ask a general question."

# A simple "Knowledge Base" (KB)
KNOWLEDGE_BASE = [
    "Şirketimizin 2023 yılı toplam geliri 1.5 Milyar TL'dir.",
    "2023 yılındaki ana büyüme alanlarımız SaaS ürünleri ve danışmanlık hizmetleridir.",
    "Prompt mühendisliği, LLM'lerden istenen çıktıyı almak için komut tasarlama sanatıdır.",
    "Sistem mühendisliği, kurumsal yapay zeka projelerinde ölçeklenebilirlik, güvenilirlik ve entegrasyonu sağlar.",
    "Kurumsal yapay zeka sistemleri, veri entegrasyonu, model yönetimi ve güvenlik gibi bileşenleri içerir."
]

def retrieve_documents(query: str, kb: list[str]) -> list[str]:
    """
    Simulates a simple document retrieval system based on keywords.
    In a real system, this would involve vector databases, semantic search, etc.
    """
    query_lower = query.lower()
    relevant_docs = []
    for doc in kb:
        if any(keyword in doc.lower() for keyword in query_lower.split()):
            relevant_docs.append(doc)
    return relevant_docs

# --- Main Demonstration Logic ---

def main():
    print("--- Prompt Engineering vs. System Engineering for Enterprise AI ---")
    print(textwrap.dedent("""
        This example demonstrates the difference between relying solely on prompt engineering
        and incorporating a basic 'system engineering' approach (like RAG) for enterprise AI.
        Simple prompting might lead to generic or incorrect answers, while a system
        that provides context can yield more accurate and relevant results.
    """))

    user_query = "Şirketimizin 2023 yılı geliri ne kadardır?" # What is our company's 2023 revenue?

    print(f"\nUser Query: '{user_query}'")
    print("\n--- Approach 1: Pure Prompt Engineering ---")
    # In this approach, we just send the raw query to the LLM.
    # The LLM has no specific knowledge about "our company's" revenue.
    # This simulates how a generic LLM might respond without specific context.
    
    # --- PROMPT ENGINEERING CONCEPT ILLUSTRATED ---
    # Here, we only focus on the prompt itself, without external data sources.
    prompt_only = user_query
    response_only = simulated_llm(prompt_only)
    print(f"Prompt sent: '{prompt_only}'")
    print(f"LLM Response (Prompt Only): {response_only}")
    print("Comment: The LLM gives a generic answer because it lacks specific company data.")

    print("\n--- Approach 2: System Engineering (Retrieval Augmented Generation - RAG) ---")
    # In this approach, we first retrieve relevant information from a knowledge base
    # and then augment the LLM's prompt with this context.
    # This is a basic form of system engineering beyond just prompt crafting.
    
    # --- SYSTEM ENGINEERING CONCEPT ILLUSTRATED ---
    # This involves multiple steps: retrieval, context assembly, and then prompting.
    # This is more robust for enterprise scenarios requiring specific, up-to-date data.
    
    # Step 1: Retrieve relevant documents from the knowledge base
    retrieved_docs = retrieve_documents(user_query, KNOWLEDGE_BASE)
    print(f"Retrieved Documents: {retrieved_docs if retrieved_docs else 'None'}")

    # Step 2: Construct an augmented prompt
    if retrieved_docs:
        context = "\n".join(retrieved_docs)
        augmented_prompt = f"Aşağıdaki bağlamı kullanarak soruyu yanıtla:\n\nBağlam:\n{context}\n\nSoru: {user_query}" # Answer the question using the following context:
    else:
        augmented_prompt = user_query # Fallback if no docs found

    # Step 3: Send the augmented prompt to the LLM
    response_rag = simulated_llm(augmented_prompt)
    print(f"Augmented Prompt sent: '{augmented_prompt}'")
    print(f"LLM Response (RAG System): {response_rag}")
    print("Comment: By providing relevant context, the LLM can give a more specific and accurate answer.")

if __name__ == "__main__":
    main()