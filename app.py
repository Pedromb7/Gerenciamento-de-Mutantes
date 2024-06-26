import tkinter as tk
from tkinter import ttk, messagebox
from backend import Backend

class App:
    def __init__(self, root, backend):
        self.root = root
        self.backend = backend
        self.root.title("Sistema de Gerenciamento da Escola de Mutantes")
        self.root.geometry("900x600")

        self.create_populate_button()
        self.create_main_tabs()
        self.create_sub_tabs()
        self.create_widgets()

    
    def create_populate_button(self):
        frame = ttk.Frame(self.root)
        frame.pack(anchor='ne', padx=10, pady=10)

        self.button_populate = ttk.Button(frame, text="Popular Database", command=self.populate_database)
        self.button_populate.grid(row=0, column=0, padx=5)

        self.button_purge = ttk.Button(frame, text="Apagar Database", command=self.backend.purge_database)
        self.button_purge.grid(row=0, column=1, padx=5)

    def populate_database(self):
        alunos_data = [
            ("Jean Grey", 30, "Telepathy, Telekinesis", 9, "X-Men", "Ativo"),
            ("Scott Summers", 32, "Optic Blasts", 8, "X-Men", "Ativo"),
            ("Ororo Munroe", 28, "Weather Manipulation", 9, "X-Men", "Ativo"),
            ("Logan", 130, "Regeneration, Adamantium Claws", 10, "X-Men", "Ativo"),
        ]

        for aluno in alunos_data:
            self.backend.cadastrar_aluno(*aluno)

        classes_data = [
            ("Mutant Ethics", 5, 30, "Professor X"),
            ("Combat Training", 6, 20, "Wolverine"),
            ("Advanced Telepathy", 1, 15, "Jean Grey")
        ]
        for classe in classes_data:
            self.backend.cadastrar_classe(*classe)

        matriculas_data = [
            (1, 1),
            (2, 2),
            (3, 1),
            (4, 2),
            (5, 3)
        ]
        for matricula in matriculas_data:
            self.backend.matricular_aluno(*matricula)

        missoes_data = [
            ("Sentinel Recon", "Investigate sentinel activity", 1, [1, 2, 3], "2023-01-01", "2023-01-31", "Ativa"),
            ("Magneto's Lair", "Locate and infiltrate Magneto's base", 2, [2, 3, 4], "2023-02-01", "2023-02-28", "Ativa"),
        ]
        for missao in missoes_data:
            nome, descricao, lider_id, integrantes_ids, data_inicio, data_fim, status = missao
            self.backend.cadastrar_missao(nome, descricao, lider_id, integrantes_ids, data_inicio, data_fim, status)
        
        equipes_data = [
            ("X-Men", 2, [1, 2, 3, 4]),
            ("Brotherhood of Mutants", 4, [2, 3, 4]),
        ]

        for equipe in equipes_data:
            nome, lider_id, integrantes_ids = equipe
            self.backend.criar_equipe(nome, lider_id, integrantes_ids)

        messagebox.showinfo("Success", "Database populated with fictional data successfully!")

    def create_main_tabs(self):
        self.main_tabs = ttk.Notebook(self.root)
        self.main_tabs.pack(expand=True, fill='both')

        self.tab_cadastrar = ttk.Frame(self.main_tabs)
        self.tab_consultar = ttk.Frame(self.main_tabs)

        self.main_tabs.add(self.tab_cadastrar, text='Cadastrar')
        self.main_tabs.add(self.tab_consultar, text='Consultar')

    def create_sub_tabs(self):
        self.tabs_cadastrar = ttk.Notebook(self.tab_cadastrar)
        self.tabs_cadastrar.pack(expand=True, fill='both')

        self.tabs_consultar = ttk.Notebook(self.tab_consultar)
        self.tabs_consultar.pack(expand=True, fill='both')

        self.tab_cadastro_alunos = ttk.Frame(self.tabs_cadastrar)
        self.tab_cadastro_classes = ttk.Frame(self.tabs_cadastrar)
        self.tab_cadastro_matriculas = ttk.Frame(self.tabs_cadastrar)
        self.tab_cadastro_missoes = ttk.Frame(self.tabs_cadastrar)
        self.tab_cadastro_equipes = ttk.Frame(self.tabs_cadastrar)

        self.tabs_cadastrar.add(self.tab_cadastro_alunos, text='Cadastro de Alunos')
        self.tabs_cadastrar.add(self.tab_cadastro_classes, text='Cadastro de Classes')
        self.tabs_cadastrar.add(self.tab_cadastro_matriculas, text='Matrícula em Classes')
        self.tabs_cadastrar.add(self.tab_cadastro_missoes, text='Cadastro de Missões')
        self.tabs_cadastrar.add(self.tab_cadastro_equipes, text='Gerenciamento de Equipes')

        self.tab_consulta_alunos = ttk.Frame(self.tabs_consultar)
        self.tab_consulta_matriculas = ttk.Frame(self.tabs_consultar)
        self.tab_consulta_missoes = ttk.Frame(self.tabs_consultar)
        self.tab_consulta_equipes = ttk.Frame(self.tabs_consultar)

        self.tabs_consultar.add(self.tab_consulta_alunos, text='Consulta de Alunos')
        self.tabs_consultar.add(self.tab_consulta_matriculas, text='Ver Matrículas')
        self.tabs_consultar.add(self.tab_consulta_missoes, text='Consulta de Missões')
        self.tabs_consultar.add(self.tab_consulta_equipes, text='Consulta de Equipes')

    def create_widgets(self):
        self.create_cadastro_alunos_tab()
        self.create_cadastro_classes_tab()
        self.create_cadastro_matriculas_tab()
        self.create_cadastro_missoes_tab()
        self.create_cadastro_equipes_tab()
        self.create_consulta_alunos_tab()
        self.create_consulta_matriculas_tab()
        self.create_consulta_missoes_tab()
        self.create_consulta_equipes_tab()

    def create_cadastro_alunos_tab(self):
        frame = ttk.LabelFrame(self.tab_cadastro_alunos, text="Cadastro de Alunos")
        frame.pack(padx=10, pady=10, fill="both", expand=True)

        ttk.Label(frame, text="Nome:").grid(row=0, column=0, padx=10, pady=10)
        self.entry_nome = ttk.Entry(frame)
        self.entry_nome.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(frame, text="Idade:").grid(row=1, column=0, padx=10, pady=10)
        self.entry_idade = ttk.Entry(frame)
        self.entry_idade.grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(frame, text="Habilidades Mutantes:").grid(row=2, column=0, padx=10, pady=10)
        self.entry_habilidades = ttk.Entry(frame)
        self.entry_habilidades.grid(row=2, column=1, padx=10, pady=10)

        ttk.Label(frame, text="Nível de Poder (1-10):").grid(row=3, column=0, padx=10, pady=10)
        self.entry_nivel_poder = ttk.Entry(frame)
        self.entry_nivel_poder.grid(row=3, column=1, padx=10, pady=10)

        ttk.Label(frame, text="Equipe:").grid(row=4, column=0, padx=10, pady=10)
        self.entry_equipe = ttk.Entry(frame)
        self.entry_equipe.grid(row=4, column=1, padx=10, pady=10)

        ttk.Label(frame, text="Status:").grid(row=5, column=0, padx=10, pady=10)
        self.combo_status = ttk.Combobox(frame, values=["Ativo", "Inativo"])
        self.combo_status.current(0)
        self.combo_status.grid(row=5, column=1, padx=10, pady=10)

        self.button_cadastrar = ttk.Button(frame, text="Cadastrar", command=self.cadastrar_aluno)
        self.button_cadastrar.grid(row=6, column=0, columnspan=2, pady=10)

    def cadastrar_aluno(self):
        nome = self.entry_nome.get()
        idade = self.entry_idade.get()
        habilidades = self.entry_habilidades.get()
        nivel_poder = self.entry_nivel_poder.get()
        equipe = self.entry_equipe.get()
        status = self.combo_status.get()

        if not all([nome, idade, habilidades, nivel_poder, equipe, status]):
            messagebox.showwarning("Aviso", "Todos os campos devem ser preenchidos")
            return

        try:
            idade = int(idade)
            if idade <= 0:
                raise ValueError("Idade deve ser um número positivo.")
        except ValueError as e:
            messagebox.showwarning("Aviso", str(e))
            return

        self.backend.cadastrar_aluno(nome, idade, habilidades, int(nivel_poder), equipe, status)
        messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso!")
        self.clear_cadastro_fields()

    def clear_cadastro_fields(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_idade.delete(0, tk.END)
        self.entry_habilidades.delete(0, tk.END)
        self.entry_nivel_poder.delete(0, tk.END)
        self.entry_equipe.delete(0, tk.END)
        self.combo_status.current(0)

    def create_cadastro_classes_tab(self):
        frame = ttk.LabelFrame(self.tab_cadastro_classes, text="Cadastro de Classes")
        frame.pack(padx=10, pady=10, fill="both", expand=True)

        ttk.Label(frame, text="Nome:").grid(row=0, column=0, padx=10, pady=10)
        self.entry_nome_classe = ttk.Entry(frame)
        self.entry_nome_classe.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(frame, text="Duração (meses):").grid(row=1, column=0, padx=10, pady=10)
        self.entry_duracao = ttk.Entry(frame)
        self.entry_duracao.grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(frame, text="Capacidade:").grid(row=2, column=0, padx=10, pady=10)
        self.entry_capacidade = ttk.Entry(frame)
        self.entry_capacidade.grid(row=2, column=1, padx=10, pady=10)

        ttk.Label(frame, text="Instrutor:").grid(row=3, column=0, padx=10, pady=10)
        self.entry_instrutor = ttk.Entry(frame)
        self.entry_instrutor.grid(row=3, column=1, padx=10, pady=10)

        self.button_cadastrar_classe = ttk.Button(frame, text="Cadastrar Classe", command=self.cadastrar_classe)
        self.button_cadastrar_classe.grid(row=4, column=0, columnspan=2, pady=10)

    def cadastrar_classe(self):
        nome = self.entry_nome_classe.get()
        duracao = self.entry_duracao.get()
        capacidade = self.entry_capacidade.get()
        instrutor = self.entry_instrutor.get()

        if not all([nome, duracao, capacidade, instrutor]):
            messagebox.showwarning("Aviso", "Todos os campos devem ser preenchidos")
            return

        self.backend.cadastrar_classe(nome, int(duracao), int(capacidade), instrutor)
        messagebox.showinfo("Sucesso", "Classe cadastrada com sucesso!")
        self.clear_classes_fields()

    def clear_classes_fields(self):
        self.entry_nome_classe.delete(0, tk.END)
        self.entry_duracao.delete(0, tk.END)
        self.entry_capacidade.delete(0, tk.END)
        self.entry_instrutor.delete(0, tk.END)

    def create_cadastro_matriculas_tab(self):
        frame = ttk.LabelFrame(self.tab_cadastro_matriculas, text="Matrícula em Classes")
        frame.pack(padx=10, pady=10, fill="both", expand=True)

        ttk.Label(frame, text="ID do Aluno:").grid(row=0, column=0, padx=10, pady=10)
        self.entry_aluno_id = ttk.Entry(frame)
        self.entry_aluno_id.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(frame, text="ID da Classe:").grid(row=1, column=0, padx=10, pady=10)
        self.entry_classe_id = ttk.Entry(frame)
        self.entry_classe_id.grid(row=1, column=1, padx=10, pady=10)

        self.button_matricular = ttk.Button(frame, text="Matricular", command=self.matricular_aluno)
        self.button_matricular.grid(row=2, column=0, columnspan=2, pady=10)

    def matricular_aluno(self):
        aluno_id = self.entry_aluno_id.get()
        classe_id = self.entry_classe_id.get()

        if not all([aluno_id, classe_id]):
            messagebox.showwarning("Aviso", "Todos os campos devem ser preenchidos")
            return

        self.backend.matricular_aluno(int(aluno_id), int(classe_id))
        messagebox.showinfo("Sucesso", "Aluno matriculado com sucesso!")
        self.clear_matriculas_fields()

    def clear_matriculas_fields(self):
        self.entry_aluno_id.delete(0, tk.END)
        self.entry_classe_id.delete(0, tk.END)

    def create_cadastro_missoes_tab(self):
        frame = ttk.LabelFrame(self.tab_cadastro_missoes, text="Cadastro de Missões")
        frame.pack(padx=10, pady=10, fill="both", expand=True)

        ttk.Label(frame, text="Nome:").grid(row=0, column=0, padx=10, pady=10)
        self.entry_nome_missao = ttk.Entry(frame)
        self.entry_nome_missao.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(frame, text="Descrição:").grid(row=1, column=0, padx=10, pady=10)
        self.entry_descricao = ttk.Entry(frame)
        self.entry_descricao.grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(frame, text="ID do Líder:").grid(row=2, column=0, padx=10, pady=10)
        self.entry_lider_id = ttk.Entry(frame)
        self.entry_lider_id.grid(row=2, column=1, padx=10, pady=10)

        ttk.Label(frame, text="IDs dos Integrantes (separados por vírgula):").grid(row=3, column=0, padx=10, pady=10)
        self.entry_integrantes_ids = ttk.Entry(frame)
        self.entry_integrantes_ids.grid(row=3, column=1, padx=10, pady=10)

        ttk.Label(frame, text="Data de Início (YYYY-MM-DD):").grid(row=4, column=0, padx=10, pady=10)
        self.entry_data_inicio = ttk.Entry(frame)
        self.entry_data_inicio.grid(row=4, column=1, padx=10, pady=10)

        ttk.Label(frame, text="Data de Fim (YYYY-MM-DD):").grid(row=5, column=0, padx=10, pady=10)
        self.entry_data_fim = ttk.Entry(frame)
        self.entry_data_fim.grid(row=5, column=1, padx=10, pady=10)

        ttk.Label(frame, text="Status:").grid(row=6, column=0, padx=10, pady=10)
        self.combo_status_missao = ttk.Combobox(frame, values=["Ativa", "Concluída", "Cancelada"])
        self.combo_status_missao.current(0)
        self.combo_status_missao.grid(row=6, column=1, padx=10, pady=10)

        self.button_cadastrar_missao = ttk.Button(frame, text="Cadastrar Missão", command=self.cadastrar_missao)
        self.button_cadastrar_missao.grid(row=7, column=0, columnspan=2, pady=10)

    def cadastrar_missao(self):
        nome = self.entry_nome_missao.get()
        descricao = self.entry_descricao.get()
        lider_id = self.entry_lider_id.get()
        integrantes_ids = self.entry_integrantes_ids.get().split(',')
        data_inicio = self.entry_data_inicio.get()
        data_fim = self.entry_data_fim.get()
        status = self.combo_status_missao.get()

        if not all([nome, descricao, lider_id, integrantes_ids, data_inicio, data_fim, status]):
            messagebox.showwarning("Aviso", "Todos os campos devem ser preenchidos")
            return

        self.backend.cadastrar_missao(nome, descricao, int(lider_id), [int(id) for id in integrantes_ids], data_inicio, data_fim, status)
        messagebox.showinfo("Sucesso", "Missão cadastrada com sucesso!")
        self.clear_missions_fields()

    def clear_missions_fields(self):
        self.entry_nome_missao.delete(0, tk.END)
        self.entry_descricao.delete(0, tk.END)
        self.entry_lider_id.delete(0, tk.END)
        self.entry_integrantes_ids.delete(0, tk.END)
        self.entry_data_inicio.delete(0, tk.END)
        self.entry_data_fim.delete(0, tk.END)
        self.combo_status_missao.current(0)

    def create_cadastro_equipes_tab(self):
        frame = ttk.LabelFrame(self.tab_cadastro_equipes, text="Gerenciamento de Equipes")
        frame.pack(padx=10, pady=10, fill="both", expand=True)

        ttk.Label(frame, text="Nome da Equipe:").grid(row=0, column=0, padx=10, pady=10)
        self.entry_nome_equipe = ttk.Entry(frame)
        self.entry_nome_equipe.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(frame, text="ID do Líder:").grid(row=1, column=0, padx=10, pady=10)
        self.entry_lider_id_equipe = ttk.Entry(frame)
        self.entry_lider_id_equipe.grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(frame, text="IDs dos Integrantes (separados por vírgula):").grid(row=2, column=0, padx=10, pady=10)
        self.entry_integrantes_ids_equipe = ttk.Entry(frame)
        self.entry_integrantes_ids_equipe.grid(row=2, column=1, padx=10, pady=10)

        self.button_criar_equipe = ttk.Button(frame, text="Criar Equipe", command=self.criar_equipe)
        self.button_criar_equipe.grid(row=3, column=0, columnspan=2, pady=10)

    def criar_equipe(self):
        nome = self.entry_nome_equipe.get()
        lider_id = self.entry_lider_id_equipe.get()
        integrantes_ids = self.entry_integrantes_ids_equipe.get().split(',')

        if not all([nome, lider_id, integrantes_ids]):
            messagebox.showwarning("Aviso", "Todos os campos devem ser preenchidos")
            return

        self.backend.criar_equipe(nome, int(lider_id), [int(id) for id in integrantes_ids])
        messagebox.showinfo("Sucesso", "Equipe criada com sucesso!")
        self.clear_teams_fields()

    def clear_teams_fields(self):
        self.entry_nome_equipe.delete(0, tk.END)
        self.entry_lider_id_equipe.delete(0, tk.END)
        self.entry_integrantes_ids_equipe.delete(0, tk.END)

    def create_consulta_alunos_tab(self):
        frame = ttk.LabelFrame(self.tab_consulta_alunos, text="Consulta de Alunos")
        frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.combo_buscar_por = ttk.Combobox(frame, values=["Nome", "Idade", "Equipe", "Status"])
        self.combo_buscar_por.current(0)
        self.combo_buscar_por.grid(row=0, column=0, padx=10, pady=10)

        self.entry_termo = ttk.Entry(frame)
        self.entry_termo.grid(row=0, column=1, padx=10, pady=10)

        self.button_consultar = ttk.Button(frame, text="Consultar", command=self.consultar_aluno)
        self.button_consultar.grid(row=0, column=2, padx=10, pady=10)

        self.tree_consulta = ttk.Treeview(frame, columns=("ID", "Nome", "Idade", "Habilidades", "Nível de Poder", "Equipe", "Status"), show="headings")
        self.tree_consulta.heading("ID", text="ID")
        self.tree_consulta.heading("Nome", text="Nome")
        self.tree_consulta.heading("Idade", text="Idade")
        self.tree_consulta.heading("Habilidades", text="Habilidades")
        self.tree_consulta.heading("Nível de Poder", text="Nível de Poder")
        self.tree_consulta.heading("Equipe", text="Equipe")
        self.tree_consulta.heading("Status", text="Status")

        self.tree_consulta.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky='nsew')

        frame.grid_rowconfigure(1, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)
        frame.grid_columnconfigure(2, weight=1)

    def consultar_aluno(self):
        buscar_por = self.combo_buscar_por.get().lower()
        termo = self.entry_termo.get()

        resultados = self.backend.consultar_aluno(buscar_por, termo)
        self.update_treeview(self.tree_consulta, resultados)

    def create_consulta_matriculas_tab(self):
        frame = ttk.LabelFrame(self.tab_consulta_matriculas, text="Matrículas")
        frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.tree_matriculas = ttk.Treeview(frame, columns=("ID", "Nome do Aluno", "Nome da Classe", "Instrutor"), show="headings")
        self.tree_matriculas.heading("ID", text="ID")
        self.tree_matriculas.heading("Nome do Aluno", text="Nome do Aluno")
        self.tree_matriculas.heading("Nome da Classe", text="Nome da Classe")
        self.tree_matriculas.heading("Instrutor", text="Instrutor")

        self.tree_matriculas.pack(padx=10, pady=10, fill="both", expand=True)

        self.button_atualizar_matriculas = ttk.Button(frame, text="Atualizar", command=self.consultar_matriculas)
        self.button_atualizar_matriculas.pack(pady=10)

    def consultar_matriculas(self):
        resultados = self.backend.consultar_matriculas()
        self.update_treeview(self.tree_matriculas, resultados)

    def create_consulta_missoes_tab(self):
        frame = ttk.LabelFrame(self.tab_consulta_missoes, text="Consulta de Missões")
        frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.tree_missoes = ttk.Treeview(frame, columns=("ID", "Nome", "Descrição", "Líder", "Integrantes", "Data Início", "Data Fim", "Status"), show="headings")
        self.tree_missoes.heading("ID", text="ID")
        self.tree_missoes.heading("Nome", text="Nome")
        self.tree_missoes.heading("Descrição", text="Descrição")
        self.tree_missoes.heading("Líder", text="Líder")
        self.tree_missoes.heading("Integrantes", text="Integrantes")
        self.tree_missoes.heading("Data Início", text="Data Início")
        self.tree_missoes.heading("Data Fim", text="Data Fim")
        self.tree_missoes.heading("Status", text="Status")

        self.tree_missoes.pack(padx=10, pady=10, fill="both", expand=True)

        self.button_atualizar_missoes = ttk.Button(frame, text="Atualizar", command=self.consultar_missoes)
        self.button_atualizar_missoes.pack(pady=10)

    def consultar_missoes(self):
        resultados = self.backend.consultar_missoes()
        self.update_treeview(self.tree_missoes, resultados)

    def create_consulta_equipes_tab(self):
        frame = ttk.LabelFrame(self.tab_consulta_equipes, text="Consulta de Equipes")
        frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.tree_equipes = ttk.Treeview(frame, columns=("ID", "Nome", "Líder", "Integrantes"), show="headings")
        self.tree_equipes.heading("ID", text="ID")
        self.tree_equipes.heading("Nome", text="Nome")
        self.tree_equipes.heading("Líder", text="Líder")
        self.tree_equipes.heading("Integrantes", text="Integrantes")

        self.tree_equipes.pack(padx=10, pady=10, fill="both", expand=True)

        self.button_atualizar_equipes = ttk.Button(frame, text="Atualizar", command=self.buscar_equipes)
        self.button_atualizar_equipes.pack(pady=10)

    def buscar_equipes(self):
        resultados = self.backend.buscar_equipes()
        self.update_treeview(self.tree_equipes, resultados)

    def update_treeview(self, treeview, data):
        treeview.delete(*treeview.get_children())
        for item in data:
            treeview.insert("", tk.END, values=item)

if __name__ == "__main__":
    root = tk.Tk()
    backend = Backend()
    app = App(root, backend)
    root.mainloop()