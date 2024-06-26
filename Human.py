from uuid import uuid4


class Human:
    name: str
    last_name: str

    ids = set()

    def __init__(self, name, last_name, _id=None):
        self.name = name
        self.last_name = last_name
        if _id:
            if _id in Human.ids:
                raise "Fuck"
        else:
            _id = self.get_unique_id()

        Human.ids.add(_id)

    @staticmethod
    def get_unique_id():
        new_id = uuid4().int
        if new_id in Human.ids:
            return Human.get_unique_id()
        return new_id







        #
        # if id is not None:
        #     self = id
        #     if not id in self.ids:
        #         self.ids.add(id)
        # else:
        #     self.ids.add(id(self))