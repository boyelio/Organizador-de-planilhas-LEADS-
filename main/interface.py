import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, ttk
from processador import (
    carregar_planilha,
    remover_colunas,
    renomear_colunas,
    reorganizar_colunas,
    analisar_colunas,
    salvar
)

df = None


def carregar():
    global df
    caminho = filedialog.askopenfilename(
        title="Selecione a planilha",
        filetypes=[("Planilhas", "*.xlsx *.xls *.csv")]
    )
    if not caminho:
        return

    try:
        df = carregar_planilha(caminho)
    except Exception as e:
        messagebox.showerror("Erro", str(e))
        return

    atualizar_lista_colunas()
    messagebox.showinfo("OK", "Planilha carregada com sucesso!")


def atualizar_lista_colunas():
    lista_colunas.delete(0, tk.END)
    for col in df.columns:
        lista_colunas.insert(tk.END, col)


def remover():
    global df
    if df is None:
        return

    selecionadas = lista_colunas.curselection()
    if not selecionadas:
        messagebox.showwarning("Atenção", "Selecione ao menos uma coluna.")
        return

    colunas = [lista_colunas.get(i) for i in selecionadas]
    df = remover_colunas(df, colunas)
    atualizar_lista_colunas()
    messagebox.showinfo("OK", "Colunas removidas!")


def renomear():
    global df
    if df is None:
        return

    novos = {}

    for col in df.columns:
        novo = simpledialog.askstring("Renomear", f"Novo nome para '{col}' (deixe vazio p/ manter):")
        if novo:
            novos[col] = novo

    if novos:
        df = renomear_colunas(df, novos)
        atualizar_lista_colunas()
        messagebox.showinfo("OK", "Colunas renomeadas!")


def reordenar():
    global df
    if df is None:
        return

    ordem_str = simpledialog.askstring(
        "Reordenar",
        "Digite a nova ordem separada por vírgulas:\n" + ", ".join(df.columns)
    )

    if not ordem_str:
        return

    nova_ordem = [c.strip() for c in ordem_str.split(",")]

    try:
        df = reorganizar_colunas(df, nova_ordem)
    except:
        messagebox.showerror("Erro", "Ordem inválida. Verifique os nomes das colunas.")
        return

    atualizar_lista_colunas()
    messagebox.showinfo("OK", "Colunas reorganizadas!")

def limpar_telefones():
    global df
    if df is None:
        return

    selecionadas = lista_colunas.curselection()
    if not selecionadas:
        messagebox.showwarning("Atenção", "Selecione uma coluna de telefone.")
        return

    if len(selecionadas) > 1:
        messagebox.showwarning("Atenção", "Selecione apenas 1 coluna para limpar.")
        return

    coluna = lista_colunas.get(selecionadas[0])

    from processador import limpar_coluna_telefone
    df = limpar_coluna_telefone(df, coluna)

    messagebox.showinfo("OK", f"Coluna '{coluna}' limpa e padronizada!")

def analisar():
    global df
    if df is None:
        return

    analise = analisar_colunas(df)

    janela = tk.Toplevel(app)
    janela.title("Análise da Planilha")
    janela.geometry("600x500")

    texto = tk.Text(janela, wrap="word")
    texto.pack(fill="both", expand=True)

    for col, dados in analise.items():
        texto.insert(tk.END, f"=== {col} ===\n")
        for k, v in dados.items():
            texto.insert(tk.END, f"{k}: {v}\n")
        texto.insert(tk.END, "\n")


def salvar_arquivo():
    global df
    if df is None:
        return

    caminho = filedialog.asksaveasfilename(
        title="Salvar como",
        defaultextension=".xlsx",
        filetypes=[("Excel", "*.xlsx")]
    )

    if not caminho:
        return

    salvar(df, caminho)
    messagebox.showinfo("OK", "Arquivo salvo!")

app = tk.Tk()
app.title("Organizador de Leads")
app.geometry("420x500")

tk.Button(app, text="Carregar Planilha", command=carregar, width=40).pack(pady=10)

tk.Label(app, text="Colunas encontradas:").pack()
lista_colunas = tk.Listbox(app, selectmode=tk.MULTIPLE, width=50, height=12)
lista_colunas.pack()

tk.Button(app, text="Remover Colunas", command=remover, width=40).pack(pady=5)
tk.Button(app, text="Renomear Colunas", command=renomear, width=40).pack(pady=5)
tk.Button(app, text="Reordenar Colunas", command=reordenar, width=40).pack(pady=5)
tk.Button(app, text="Limpar Telefones (55XXXXXXXXX)", command=limpar_telefones, width=40).pack(pady=5)
tk.Button(app, text="Analisar Colunas", command=analisar, width=40).pack(pady=10)

tk.Button(app, text="Salvar Nova Planilha", command=salvar_arquivo, width=40).pack(pady=15)

app.mainloop()