class TextEditor:

    def __init__(self):
        self.pos = 0
        self.txt = ""

    def addText(self, text: str) -> None:
        length = len(text)
        self.txt = self.txt[:self.pos] + text + self.txt[self.pos:]
        self.pos += length

    def deleteText(self, k: int) -> int:
        new = max(0, self.pos - k)
        old = self.pos
        res = self.pos - new
        self.pos = new
        self.txt = self.txt[:new] + self.txt[old:]
        return res

    def cursorLeft(self, k: int) -> str:
        self.pos = max(0, self.pos - k)
        res = self.txt[max(0, self.pos - 10):self.pos]
        return res
