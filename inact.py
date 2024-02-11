import asyncio

class InactivityChecker:
    def __init__(self, state, message):
        self.state = state
        self.message = message
        self.task = None

    async def check_inactivity(self):
        while True:
            await asyncio.sleep(86400)
            try:
                data = await self.state.get_data()
                if data['awaiting'] > 0:
                    break
            except KeyError:
                await self.message.answer(random.choice(consts.inactivity_caption))

    async def start(self):
        if self.task is not None:
            self.task.cancel()
        self.task = asyncio.create_task(self.check_inactivity())
