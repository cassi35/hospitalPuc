from abc import ABC, abstractmethod

class RoleCheckerUseCase(ABC):
    @abstractmethod
    def check_role(self, user_data: dict, allowed_roles: list) -> bool:
        pass