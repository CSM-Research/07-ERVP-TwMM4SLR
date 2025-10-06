import glob

def merge_bib_files(output_file="merged.bib"):
    """
    Junta todos os arquivos .bib da pasta local em um único arquivo .bib.
    """
    bib_files = glob.glob("*.bib")

    if not bib_files:
        print("Nenhum arquivo .bib encontrado na pasta local.")
        return

    with open(output_file, "w", encoding="utf-8") as outfile:
        for bib_file in bib_files:
            with open(bib_file, "r", encoding="utf-8") as infile:
                content = infile.read().strip()
                outfile.write(content + "\n\n")  # separador entre arquivos
            print(f"✔ Arquivo adicionado: {bib_file}")

    print(f"\n✅ Arquivo final gerado: {output_file}")


if __name__ == "__main__":
    merge_bib_files()
