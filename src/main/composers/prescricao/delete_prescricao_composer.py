from src.presentation.controllers.prescricao.delete_prescricao_controller import PrescricaoDeleteController
from src.data.usecases.prescricao.delete_prescricao import PrescricaoDeleteUseCase
from src.infra.db.repositories.prescricao_repository import PrescricaoRepository

def delete_prescricao_composer():
	repository = PrescricaoRepository()
	usecase = PrescricaoDeleteUseCase(
		prescricao_repository=repository
	)
	controller = PrescricaoDeleteController(usecase=usecase)
	return controller.handle
