from src.data.interfaces.convenio_interface_repository import ConvenioRepositoryInterface

class ConvenioDeleteSpy(ConvenioRepositoryInterface):
    def __init__(self) -> None:
        self.delete_convenio_id = None
        self.delete_convenio_call_count = 0

    def delete_convenio(self, convenio_id: int) -> None:
        self.delete_convenio_id = convenio_id
        self.delete_convenio_call_count += 1
