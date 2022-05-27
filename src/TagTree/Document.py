class Document():
    def __init__(self, allowOverride=False) -> None:
        self.items = {}
        self.override = allowOverride
        pass

    def push(self, item):
        if item.id in self.items.keys() and not self.override:
            raise RuntimeError('You cannot add elements with the same Id. To aloow it, set override to True')
        self.items[item.id] = item
