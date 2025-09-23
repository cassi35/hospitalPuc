from src.presentation.controllers.prescricao.list_prescricao_controller import PrescricaoListController
from src.data.usecases.prescricao.list_prescricao import PrescricaoListUseCase
from src.infra.db.repositories.prescricao_repository import PrescricaoRepository

def list_prescricao_composer():
	repository = PrescricaoRepository()
	usecase = PrescricaoListUseCase(
		prescricao_repository=repository
	)
	controller = PrescricaoListController(usecase=usecase)
	return controller.handle
