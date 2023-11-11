from utils.async_service import AsyncService
import qi

class QiAsyncService(AsyncService):
    def future(self, action, *args):
        return qi.async(action, *args)