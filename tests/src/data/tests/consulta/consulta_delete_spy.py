from src.data.interfaces.consulta_interface_repository import ConsultaRepositoryInterface

class ConsultaDeleteSpy(ConsultaRepositoryInterface):
    def __init__(self) -> None:
        self.delete_consulta_id = None
        self.delete_consulta_call_count = 0

    def delete_consulta(self, consulta_id: int) -> None:
        self.delete_consulta_id = consulta_id
        self.delete_consulta_call_count += 1
