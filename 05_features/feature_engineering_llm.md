´´´!pip install -q llama-cpp-python pandas tqdm

import json
import os
import pandas as pd
from datetime import datetime
from tqdm import tqdm
from llama_cpp import Llama

# ===== CONFIGURAÇÕES =====
DATASET_PATH = "/content/corpus-simple.jsonl"   # arquivo que você subiu no Colab
MODEL_PATH = "/content/mistral-7b-instruct-v0.2.Q4_K_M.gguf"
OUTPUT = "products_features_item5.csv"

MAX_ROWS = 100        # quantidade total desejada
BATCH_SIZE = 2       

def build_prompt(title, description):
    return f"""
You are a data extraction system.

Given a product TITLE and DESCRIPTION, extract structured features.
Return ONLY valid JSON.
Do not add explanations.

JSON format:
{{
  "category": "",
  "material": "",
  "compatibility": "",
  "features": {{
    "key_features": [],
    "functions": [],
    "certifications": [],
    "other_attributes": []
  }}
}}

TITLE:
{title}

DESCRIPTION:
{description}
"""
!wget https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF/resolve/main/mistral-7b-instruct-v0.2.Q4_K_M.gguf

llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=2048
)
rows = []
total_saved = 0

with open(DATASET_PATH, "r", encoding="utf-8") as f:
    for i, line in enumerate(tqdm(f)):
        if i >= MAX_ROWS:
            break

        item = json.loads(line)
        prompt = build_prompt(item["title"], item["text"])

        out = llm(prompt, max_tokens=300, temperature=0.2)
        raw = out["choices"][0]["text"].strip()

        start = raw.find("{")
        end = raw.rfind("}") + 1
        if start == -1 or end == -1:
            continue

        try:
            features = json.loads(raw[start:end])
        except:
            continue

        feat = features.get("features", {})

        row = {
            "product_id": item.get("docid", i),
            "title": item["title"],
            "category": features.get("category"),
            "material": features.get("material"),
            "compatibility": features.get("compatibility"),
            "key_features": ", ".join(feat.get("key_features", [])),
            "functions": ", ".join(feat.get("functions", [])),
            "other_attributes": ", ".join(feat.get("other_attributes", [])),
            "processing_timestamp": datetime.utcnow()
        }

        rows.append(row)

        # ===== SALVAMENTO INCREMENTAL COM LOG =====
        if len(rows) == BATCH_SIZE:
            pd.DataFrame(rows).to_csv(
                OUTPUT,
                mode="a",
                header=not os.path.exists(OUTPUT),
                index=False
            )
            total_saved += len(rows)
            print(f"✅ Arquivo '{OUTPUT}' atualizado. Total de registros salvos: {total_saved}")
            rows = []

# ===== SALVAR RESTANTE =====
if rows:
    pd.DataFrame(rows).to_csv(
        OUTPUT,
        mode="a",
        header=not os.path.exists(OUTPUT),
        index=False
    )
    total_saved += len(rows)
    print(f"✅ Arquivo '{OUTPUT}' finalizado. Total de registros salvos: {total_saved}")
´´´

