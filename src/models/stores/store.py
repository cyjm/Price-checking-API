import uuid


class Store(object):
    def __init__(self, name, url_prefix, tag_name, query_path, _id=None):
        self.name = name
        self.url_prefix = url_prefix
        self.tag_name = tag_name
        self.query_path = query_path
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<Store {}>".format(self.name)
