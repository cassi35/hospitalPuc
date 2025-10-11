from src.domain.usecases.auth.generateVerification import GenerateVerification
from src.data.interfaces.urSafeTokenService_interface import URSafeTokenServiceInterface
class GenerateVerificationImpl(GenerateVerification):
    def __init__(self,urSafeTokenService: URSafeTokenServiceInterface):
        self.urSafeTokenService = urSafeTokenService
    def generate(self, user_data:dict)->str:
        token = self.urSafeTokenService.create_url_safe_token(user_data)
        return token