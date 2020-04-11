from tce_api.base import Base

class BasicRequester(Base):
    def __init__(self, cls):
        super().__init__()
        self.initialize_variables_by_method(cls.__table__.name)
        self.cls = cls

    def execute(self):
        try:
            if self.requestable():
                response = self.request_tce_api()
                array = []
                for params in response['rsp']['_content']:
                    array.append(self.cls(params))
                self.cls.save_multiple(array)
                self.save_progress('', True)
        except Exception as e:
            self.save_progress(e, False)