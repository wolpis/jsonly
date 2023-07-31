import json

from .connect import Connect
from .error import GetExcetion, UpdateExcetion


class UseJsonly(Connect):
    """
    ### "누구나 쉽게 데이터베이스 작업을"
    Github : https://github.com/VoidAsMad/jsonly \n
    Docs : link \n
    """

    def __init__(
        self, path: str, encoding: str = "utf-8", ensure_ascii: bool = False
    ) -> None:
        super().__init__(path, encoding, ensure_ascii)

    def get(self, path: str = None) -> dict[str, any]:
        """
        JSON 파일의 데이터를 가져옵니다.\n
        Load data from the database.

        ## <Parameter>
        #### path:
        `/` 구분 기호로 경로를 지정하여 데이터를 바로 불러올 수 있습니다.
        기본적으론 모든 데이터를 가져옵니다.

        ## <Excetion>
        #### GetExcetion
        `path` 파리미터의 값이 잘못된 경우 반환되는 예외 클래스 입니다.
        """
        try:
            with open(self.path, "r", encoding=self.encoding) as f:
                data = json.load(f)
            if path != None:
                path = path.split("/")
                for i in path:
                    data = data[str(i)]
            return data
        except Exception as exception:
            raise GetExcetion(exception)

    def set(self, data: dict[str, any]) -> bool:
        """
        `data` 파라미터의 값을 데이터베이스에 덮어씁니다. 저장에 성공하면 `True`를 반환합니다.\n
        Overwrite the entire database with new data. Return True if saving was successful

        ## <Parameter>
        #### data:
        데이터베이스에 덮어쓸 데이터를 지정합니다.

        ## <Excetion>
        #### UpdateExcetion
        데이터베이스에 값이 갱신되는 중 오류가 발생하면 반환되는 예외 클래스 입니다.
        """
        try:
            with open(self.path, "w", encoding=self.encoding) as f:
                json.dump(data, f, indent=4, ensure_ascii=self.ensure_ascii)
            return True
        except Exception as exception:
            raise UpdateExcetion(exception)

    def update(self, data: dict[str, any]) -> bool:
        """
        `data` 파라미터의 값을 데이터베이스에 추가합니다.\n
        Add to the root of database with new value.

        ## <Parameter>
        #### data:
        데이터베이스에 추가할 데이터를 지정합니다.

        ## <Excetion>
        #### UpdateExcetion
        데이터베이스에 값이 갱신되는 중 오류가 발생하면 반환되는 예외 클래스 입니다.
        """
        get_data = self.get()
        key_list = list(data.keys())
        try:
            for i in key_list:
                get_data[i] = data[i]
            with open(self.path, "w", encoding=self.encoding) as f:
                json.dump(get_data, f, indent=4, ensure_ascii=self.ensure_ascii)
            return True
        except Exception as exception:
            raise UpdateExcetion(exception)

    def insert(self, data: dict[str, any], path: str = "/") -> bool:
        """
        `data` 파라미터의 값을 데이터베이스에 추가합니다.\n
        Add to the root of database with new value.

        ## <Parameter>
        #### data:
        데이터베이스에 추가할 데이터를 지정합니다.

        ## <Excetion>
        #### UpdateExcetion
        데이터베이스에 값이 갱신되는 중 오류가 발생하면 반환되는 예외 클래스 입니다.
        """
        get_data = self.get()
        try:
            if path != None:
                path = path.split("/")

                def nested_set(dic: dict, keys: list[str], value: str):
                    for key in keys[:-1]:
                        dic = dic.setdefault(key, {})
                    dic[keys[-1]] = value

                nested_set(get_data, path, data)
            with open(self.path, "w", encoding=self.encoding) as f:
                json.dump(get_data, f, indent=4, ensure_ascii=self.ensure_ascii)
            return True
        except Exception as exception:
            raise UpdateExcetion(exception)
