from typing import List

from collections import defaultdict


class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.last_index = defaultdict(int)
        self.tables = defaultdict(dict)

    def insertRow(self, name: str, row: List[str]) -> None:
        self.last_index[name] += 1
        index = self.last_index[name]

        self.tables[name][index] = row

    def deleteRow(self, name: str, rowId: int) -> None:
        del self.tables[name][rowId]

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        return self.tables[name][rowId][columnId - 1]


# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# obj.insertRow(name,row)
# obj.deleteRow(name,rowId)
# param_3 = obj.selectCell(name,rowId,columnId)
