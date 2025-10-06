import pandas as pd
import matplotlib.pyplot as plt

# Lê a planilha
df = pd.read_excel("dataExtraction.xls")

# Explode os métodos em linhas separadas
df_expanded = df.assign(design_strategy=df['design_strategy'].str.split('[;\n]')).explode('design_strategy')
df_expanded['design_strategy'] = df_expanded['design_strategy'].str.strip()  # remove espaços extras
df_expanded = df_expanded[df_expanded['design_strategy'] != '']  # remove vazios

# Conta o número de estudos por combinação Domain x Method
counts = df_expanded.groupby(['maturity_model_domain', 'design_strategy']).size().reset_index(name='StudyCount')

# Ordena métodos para o eixo X
methods_sorted = sorted(counts['design_strategy'].unique())
domains_sorted = sorted(counts['maturity_model_domain'].unique())

# Mapeia métodos e domínios para índices numéricos (para matplotlib)
counts['x'] = counts['design_strategy'].apply(lambda x: methods_sorted.index(x))
counts['y'] = counts['maturity_model_domain'].apply(lambda x: domains_sorted.index(x))

# Plot
plt.figure(figsize=(16, 8))
plt.scatter(
    counts['x'],
    counts['y'],
    s=counts['StudyCount']*150,  # tamanho da bolha proporcional ao número de estudos
    c='white',
    edgecolors='black',
    alpha=0.8,
    linewidth=1.2
)

# Coloca o número de estudos dentro da bolha
for _, row in counts.iterrows():
    plt.text(row['x'], row['y'], str(row['StudyCount']),
             ha='center', va='center', fontsize=9, weight='bold', color='black')

# Ajustes dos eixos
plt.xticks(range(len(methods_sorted)), methods_sorted, rotation=45, ha='right')
plt.yticks(range(len(domains_sorted)), domains_sorted)
plt.xlabel("Design strategies (methods)")
plt.ylabel("Domain")

# Guidelines
plt.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray', alpha=0.7)

plt.tight_layout()
plt.show()
