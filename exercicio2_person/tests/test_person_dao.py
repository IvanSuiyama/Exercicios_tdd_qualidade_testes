"""Casos de teste do Exercício 2 - PersonDAO.isValidToInclude()."""

import pytest

from exercicio2_person.email import Email
from exercicio2_person.person import Person
from exercicio2_person.person_dao import PersonDAO


def criar_pessoa(**campos) -> Person:
    """Cria uma Person válida, permitindo sobrescrever campos no teste."""
    dados = {
        "id": 1,
        "name": "Ivan Suiyama",
        "age": 30,
        "emails": [Email(id=1, name="ivan@fatec.br")],
    }
    dados.update(campos)
    return Person(**dados)


@pytest.fixture
def dao() -> PersonDAO:
    return PersonDAO()


class TestPessoaValida:
    def test_pessoa_valida_nao_retorna_erros(self, dao):
        assert dao.is_valid_to_include(criar_pessoa()) == []

    @pytest.mark.parametrize("idade", [1, 200])
    def test_idade_limites_do_intervalo(self, dao, idade):
        assert dao.is_valid_to_include(criar_pessoa(age=idade)) == []

    def test_nome_com_tres_partes(self, dao):
        pessoa = criar_pessoa(name="Ivan Suiyama Silva")
        assert dao.is_valid_to_include(pessoa) == []

    def test_multiplos_emails_validos(self, dao):
        pessoa = criar_pessoa(
            emails=[
                Email(id=1, name="ivan@fatec.br"),
                Email(id=2, name="ivan.suiyama@gmail.com"),
            ]
        )
        assert dao.is_valid_to_include(pessoa) == []


class TestNomeInvalido:
    @pytest.mark.parametrize("nome", ["Ivan", "", "   "])
    def test_nome_com_menos_de_duas_partes(self, dao, nome):
        erros = dao.is_valid_to_include(criar_pessoa(name=nome))
        assert "O nome deve ser composto por ao menos 2 partes." in erros

    @pytest.mark.parametrize(
        "nome",
        ["Ivan 2", "Ivan Suiyama1", "Ivan @Suiyama", "Ivan Suiyama!"],
    )
    def test_nome_com_caracteres_que_nao_sao_letras(self, dao, nome):
        erros = dao.is_valid_to_include(criar_pessoa(name=nome))
        assert "O nome deve ser composto apenas por letras." in erros

    def test_nome_vazio_acumula_os_dois_erros_de_nome(self, dao):
        erros = dao.is_valid_to_include(criar_pessoa(name=""))
        assert "O nome deve ser composto por ao menos 2 partes." in erros
        assert "O nome deve ser composto apenas por letras." in erros


class TestIdadeInvalida:
    @pytest.mark.parametrize("idade", [0, -1, 201, 1000])
    def test_idade_fora_do_intervalo(self, dao, idade):
        erros = dao.is_valid_to_include(criar_pessoa(age=idade))
        assert "A idade deve estar entre 1 e 200." in erros

    @pytest.mark.parametrize("idade", ["30", 30.5, None])
    def test_idade_que_nao_e_inteiro(self, dao, idade):
        erros = dao.is_valid_to_include(criar_pessoa(age=idade))
        assert "A idade deve ser um número inteiro." in erros


class TestEmailInvalido:
    def test_pessoa_sem_email(self, dao):
        erros = dao.is_valid_to_include(criar_pessoa(emails=[]))
        assert "O objeto Person deve ter pelo menos um Email associado." in erros

    @pytest.mark.parametrize(
        "nome_email",
        [
            "ivanfatec.br",       # sem @
            "ivan@fatec",         # sem ponto
            "ivan@.br",           # parte do domínio vazia
            "ivan@fatec.",        # parte final vazia
            "@fatec.br",          # parte local vazia
            "ivan@fa tec.br",     # espaço
            "ivan@fatec@br.com",  # dois @
            " ivan@fatec.br",     # espaço à esquerda
        ],
    )
    def test_email_fora_do_formato(self, dao, nome_email):
        erros = dao.is_valid_to_include(
            criar_pessoa(emails=[Email(id=1, name=nome_email)])
        )
        assert any("deve estar no formato '_____@____._____'" in e for e in erros)

    def test_um_email_invalido_entre_validos(self, dao):
        pessoa = criar_pessoa(
            emails=[
                Email(id=1, name="ivan@fatec.br"),
                Email(id=2, name="invalido"),
            ]
        )
        erros = dao.is_valid_to_include(pessoa)
        assert len(erros) == 1
        assert "'invalido'" in erros[0]

    def test_email_com_nome_nulo(self, dao):
        erros = dao.is_valid_to_include(
            criar_pessoa(emails=[Email(id=1, name=None)])
        )
        assert any("deve estar no formato" in e for e in erros)


class TestSave:
    def test_salva_pessoa_valida(self, dao):
        pessoa = criar_pessoa()
        dao.save(pessoa)
        assert dao._pessoas[1] is pessoa

    def test_recusa_pessoa_invalida(self, dao):
        with pytest.raises(ValueError, match="Pessoa inválida"):
            dao.save(criar_pessoa(age=0))
        assert dao._pessoas == {}

    def test_sobrescreve_pessoa_com_mesmo_id(self, dao):
        dao.save(criar_pessoa(name="Ivan Suiyama"))
        atualizada = criar_pessoa(name="Ivan Silva")
        dao.save(atualizada)
        assert dao._pessoas[1] is atualizada
