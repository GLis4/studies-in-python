from unittest.mock import patch, MagicMock
from src.data import CreateTxt
from src.connector import Connection

@patch('src.connector.Connection')  # mocka a classe Connection
def test_insert_name_in_txt(MockConnection):
    # Configura o mock de Connection
    mock_conn_instance = MagicMock()
    MockConnection.return_value = mock_conn_instance

    # Injeta o mock diretamente na classe
    CreateTxt.conn = mock_conn_instance

    # Chama o método que será testado
    CreateTxt.insert_name_in_txt()

    # Verifica se o método insert foi chamado com o valor correto
    mock_conn_instance.insert.asser_called_once()

def test_connector():
    with patch("src.data.Connection") as mock_txt:
        conn = Connection()
    pass