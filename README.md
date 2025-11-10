# kg-rag

To work with vanilla RAG - Prototyping &amp; Learning

Day 1-2: Environment Setup + Hello World RAG
Tasks:

1. Set up Python environment
2. Build a minimal RAG system
3. Run it and understand output
   Does it retrieve the right documents?
   What happens if you change k?

Day 3-4: Load Real Data + FAISS Basics
Tasks:

1. Download HotpotQA dev set
2. Build FAISS index on HotpotQA paragraphs
3. Test retrieval for one question

Day 5-6: Cross-Encoder Reranking
Tasks:

1. Understand bi-encoder vs. cross-encoder
   Bi-encoder (FAISS): Fast, approximate, encodes Q and D separately
   Cross-encoder: Slow, accurate, encodes Q+D together
2. Implement reranking

Day 7: Generate Answers with GPT
Tasks:

1. Set up OpenAI API (or use local model)
2. Simple RAG generation
3. Compute Exact Match

End Goal

- ✅ Working vanilla RAG on HotpotQA (bi-encoder + cross-encoder + GPT)
- ✅ FAISS index for 100 dev questions
- ✅ Basic evaluation (EM) on 10 questions

Setup steps

## 1. Clone repo

git clone <repo-url>
cd kg-rag

## 2. Create environment

conda create -n kg-rag python=3.10
conda activate kg-rag

## 3. Install dependencies

pip install -r requirements.txt
python -m spacy download en_core_web_sm

## 4. Test
