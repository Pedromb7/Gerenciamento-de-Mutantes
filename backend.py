import sqlite3

class Backend:
    def __init__(self, db_name="mutantes.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        with self.conn:
            
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS alunos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    idade INTEGER,
                    habilidades TEXT,
                    nivel_poder INTEGER,
                    equipe TEXT,
                    status TEXT
                )
            """)
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS classes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    duracao INTEGER,
                    capacidade INTEGER,
                    instrutor TEXT
                )
            """)
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS matriculas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    aluno_id INTEGER,
                    classe_id INTEGER,
                    FOREIGN KEY (aluno_id) REFERENCES alunos(id),
                    FOREIGN KEY (classe_id) REFERENCES classes(id)
                )
            """)
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS missoes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    descricao TEXT,
                    lider_id INTEGER,
                    integrantes_ids TEXT,
                    data_inicio TEXT,
                    data_fim TEXT,
                    status TEXT,
                    FOREIGN KEY (lider_id) REFERENCES alunos(id)
                )
            """)
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS equipes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    lider_id INTEGER,
                    integrantes_ids TEXT,
                    FOREIGN KEY (lider_id) REFERENCES alunos(id)
                )
            """)

    def purge_database(self):
        with self.conn:
            self.conn.execute("DROP TABLE IF EXISTS alunos")
            self.conn.execute("DROP TABLE IF EXISTS classes")
            self.conn.execute("DROP TABLE IF EXISTS matriculas")
            self.conn.execute("DROP TABLE IF EXISTS missoes")
            self.conn.execute("DROP TABLE IF EXISTS equipes")
            self.create_tables()

    def cadastrar_aluno(self, nome, idade, habilidades, nivel_poder, equipe, status):
        with self.conn:
            self.conn.execute("""
                INSERT INTO alunos (nome, idade, habilidades, nivel_poder, equipe, status)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (nome, idade, habilidades, nivel_poder, equipe, status))

    def consultar_aluno(self, buscar_por, termo):
        with self.conn:
            cursor = self.conn.execute(f"SELECT * FROM alunos WHERE {buscar_por} LIKE ?", ('%' + termo + '%',))
            return cursor.fetchall()

    def cadastrar_classe(self, nome, duracao, capacidade, instrutor):
        with self.conn:
            self.conn.execute("""
                INSERT INTO classes (nome, duracao, capacidade, instrutor)
                VALUES (?, ?, ?, ?)
            """, (nome, duracao, capacidade, instrutor))

    def matricular_aluno(self, aluno_id, classe_id):
        with self.conn:
            # Check class capacity before enrolling
            cursor = self.conn.execute("""
                SELECT capacidade, (SELECT COUNT(*) FROM matriculas WHERE classe_id = ?) as inscritos
                FROM classes WHERE id = ?
            """, (classe_id, classe_id))
            capacidade, inscritos = cursor.fetchone()
            if inscritos >= capacidade:
                raise Exception("Capacidade da classe excedida")

            self.conn.execute("""
                INSERT INTO matriculas (aluno_id, classe_id)
                VALUES (?, ?)
            """, (aluno_id, classe_id))

    def consultar_matriculas(self):
        with self.conn:
            cursor = self.conn.execute("""
                SELECT m.id, a.nome, c.nome, c.instrutor
                FROM matriculas m
                JOIN alunos a ON m.aluno_id = a.id
                JOIN classes c ON m.classe_id = c.id
            """)
            return cursor.fetchall()

    def cadastrar_missao(self, nome, descricao, lider_id, integrantes_ids, data_inicio, data_fim, status):
        with self.conn:
            self.conn.execute("""
                INSERT INTO missoes (nome, descricao, lider_id, integrantes_ids, data_inicio, data_fim, status)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (nome, descricao, lider_id, ','.join(map(str, integrantes_ids)), data_inicio, data_fim, status))

    def criar_equipe(self, nome, lider_id, integrantes_ids):
        with self.conn:
            self.conn.execute("""
                INSERT INTO equipes (nome, lider_id, integrantes_ids)
                VALUES (?, ?, ?)
            """, (nome, lider_id, ','.join(map(str, integrantes_ids))))

    def buscar_equipes(self):
        with self.conn:
            cursor = self.conn.execute("SELECT * FROM equipes")
            return cursor.fetchall()
        
    def consultar_missoes(self):
        with self.conn:
            cursor = self.conn.execute("SELECT * FROM missoes")
            return cursor.fetchall()

    def buscar_membros_equipe(self, equipe_nome):
        with self.conn:
            cursor = self.conn.execute("""
                SELECT a.id, a.nome
                FROM alunos a
                JOIN equipes e ON ',' || e.membros_ids || ',' LIKE '%,' || a.id || ',%'
                WHERE e.nome = ?
            """, (equipe_nome,))
            return cursor.fetchall()
