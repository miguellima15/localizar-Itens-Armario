import tkinter as tk
from tkinter import messagebox
import sqlite3
import sys
import os
import sqlite3
def resource_path(relative_path):
    """ Obter o caminho absoluto do arquivo, seja em desenvolvimento ou em execução no executável PyInstaller """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def connect_db():
    if getattr(sys, 'frozen', False):  # verifica se está rodando no executável
        db_path = os.path.join(sys._MEIPASS, 'banco/armarios.db')
    else:
        db_path = 'banco/armarios.db'

    conn = sqlite3.connect(db_path)
    return conn


def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS items (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL UNIQUE,
                        Armario INTEGER NOT NULL,
                        coluna INTEGER NOT NULL)''')
    conn.commit()
    conn.close()

def add_item(name, Armario, coluna):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        if not (1 <= Armario <= 3) or not (1 <= coluna <= 5):
            messagebox.showerror("Erro", "Armário deve ser 1, 2 ou 3 e Coluna deve ser entre 1 e 5!")
            return
        cursor.execute('INSERT INTO items (name, Armario, coluna) VALUES (?, ?, ?)', (name, Armario, coluna))
        conn.commit()
        messagebox.showinfo("Sucesso", "Item Adicionado com Sucesso!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Erro", "Este item já existe!")
    finally:
        conn.close()

def find_item(name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM items WHERE name = ?', (name,))
    result = cursor.fetchone()
    conn.close()
    return result

# Funções da Interface Gráfica
def search_item():
    name = entry_name.get()
    result = find_item(name)
    if result:
        messagebox.showinfo("Item Encontrado", f"Nome: {result[1]}\nArmário: {result[2]}\nColuna: {result[3]}")
    else:
        messagebox.showinfo("Item Não encontrado", "Nenhum item encontrado com esse nome.")

def open_add_item_window():
    add_window = tk.Toplevel(root)
    add_window.title("Adicionar Item")
    
    tk.Label(add_window, text="Nome do Item:", bd=2, relief="ridge").pack(pady=5)
    entry_add_name = tk.Entry(add_window)
    entry_add_name.pack(pady=5)
    
    tk.Label(add_window, text="Armário (1, 2 ou 3):", bd=2, relief="ridge").pack(pady=5)
    entry_add_armario = tk.Entry(add_window)
    entry_add_armario.pack(pady=5)
    
    tk.Label(add_window, text="Coluna (1 a 5):", bd=2, relief="ridge").pack(pady=5)
    entry_add_coluna = tk.Entry(add_window)
    entry_add_coluna.pack(pady=5)
    
    def submit_item():
        name = entry_add_name.get()
        try:
            armario = int(entry_add_armario.get())
            coluna = int(entry_add_coluna.get())
        except ValueError:
            messagebox.showerror("Erro", "Armário e coluna devem ser números inteiros!")
            return
        add_item(name, armario, coluna)
        add_window.destroy()  # Fechar a janela após adicionar o item
    
    tk.Button(add_window, text="Adicionar Item", command=submit_item, font=("Helvetica", 12, "bold"), bg="red", fg="white", bd=5, relief="groove", padx=10, pady=5).pack(pady=10)

# Configuração da Janela Principal
create_table()
root = tk.Tk()
root.title("Localizar Item")

logo_path = resource_path("imagem/download.png")
logo_image = tk.PhotoImage(file=logo_path)
logo_label = tk.Label(root, image=logo_image)
logo_label.pack()

# Entrada de Nome
label_name = tk.Label(root, text="Digite o Nome:", bd=1, relief="ridge")
label_name.pack(pady=10)

entry_name = tk.Entry(root)
entry_name.pack(pady=10)

# Botão de Pesquisa
button_search = tk.Button(root, text="Procurar", command=search_item, font=("Helvetica", 12, "bold"), bg="blue", fg="white", bd=5, relief="groove", padx=10, pady=5)
button_search.pack(pady=10)

# Botão para Abrir Janela de Adição de Itens
button_add_item = tk.Button(root, text="Adicionar Item", command=open_add_item_window, font=("Helvetica", 12, "bold"), bg="red", fg="white", bd=5, relief="groove", padx=10, pady=5)
button_add_item.pack(pady=10)

# Rodando a Interface
root.mainloop()
