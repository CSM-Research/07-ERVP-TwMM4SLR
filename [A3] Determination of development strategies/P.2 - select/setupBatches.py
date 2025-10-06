import pandas as pd
import math
import os

# Input file
arquivo = "firstSelection.xlsx"
output_folder = "batches_output"
os.makedirs(output_folder, exist_ok=True)

# --- Carrega a planilha ---
df = pd.read_excel(arquivo, engine="openpyxl")

# --- Normaliza status para comparação (sem alterar a coluna original) ---
status_lower = df["status"].astype(str).str.strip().str.lower()

# --- Separa rejected ou duplicated ---
filtered_df = df[status_lower.isin(["rejected", "duplicated"])]
unclassified_df = df[status_lower == "unclassified"].copy()

# --- Salva rejected + duplicated ---
if not filtered_df.empty:
    filtered_df.to_excel(os.path.join(output_folder, "rejected_or_duplicated.xlsx"), index=False)
    print(f"Arquivo com rejected e duplicated salvo em {os.path.join(output_folder, 'rejected_or_duplicated.xlsx')}")
else:
    print("Nenhum estudo rejected ou duplicated encontrado.")

# --- Divide unclassified em 4 batches (se houver) ---
if not unclassified_df.empty:
    n_batches = 4
    batch_size = math.ceil(len(unclassified_df) / n_batches)
    batches = [unclassified_df.iloc[i:i + batch_size] for i in range(0, len(unclassified_df), batch_size)]

    # Salva os batches
    for i, batch in enumerate(batches, 1):
        nome_arquivo = os.path.join(output_folder, f"batch_{i}.xlsx")
        batch.to_excel(nome_arquivo, index=False)
        print(f"Batch {i} salvo em {nome_arquivo} com {len(batch)} estudos.")
else:
    print("Nenhum estudo unclassified encontrado.")

# --- Resumo ---
print("\nResumo:")
print(f"✅ Unclassified total: {len(unclassified_df)}")
print(f"❌ Rejected or Duplicated total: {len(filtered_df)}")
print(f"Todos os arquivos salvos na pasta: {output_folder}")
