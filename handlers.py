from anthill.framework.handlers import RequestHandler
from anthill.platform.handlers import UserHandlerMixin, LoginHandlerMixin, LogoutHandlerMixin
from anthill.framework.auth import authenticate


class LoginHandler(LoginHandlerMixin, RequestHandler, UserHandlerMixin):
    async def post(self, *args, **kwargs):
        credentials = self.get_credentials()
        user = await authenticate(self.request, **credentials)
        self.login(user=user)

    def get_credentials(self):
        field_names = ('username', 'password')
        return dict(map(lambda x: (x, self.get_argument(x)), field_names))


class LogoutHandler(LogoutHandlerMixin, RequestHandler, UserHandlerMixin):
    async def get(self, *args, **kwargs):
        await self.logout()

    async def post(self, *args, **kwargs):
        await self.get(*args, **kwargs)


class RegisterHandler(RequestHandler, UserHandlerMixin):
    pass
