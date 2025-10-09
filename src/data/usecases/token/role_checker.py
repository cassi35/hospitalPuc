from src.domain.usecases.token.role_checker import RoleCheckerUseCase
from src.errors.types.AccountIsNotVerified import AccountIsNotVerified
from src.errors.types.InsufficientPermissions import InsufficientPermissions
class RoleCheckerUsecaseImpl(RoleCheckerUseCase):
    def check_role(self, user_data:dict, allowed_roles:list)->bool:
        if not user_data.get("is_verified", False):
            raise AccountIsNotVerified("Account is not verified")
        user_role = user_data.get("role", None)
        if user_role not in allowed_roles:
            raise InsufficientPermissions("Insufficient permissions")
        return True