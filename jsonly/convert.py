import json
import sqlite3
from typing import Union

from .client import UseJsonly
from .error import ConverException, ConvertTypeExcetion, SaveException


class Convert:
    """SQL 파일을 Json파일로 변환하는 기능을 지원하는 클래스입니다."""

    def __init__(self, jsonly: UseJsonly, sql_path: str) -> None:
        """
        `jsonly` : `jsonly.UseJsonly`의 클래스입니다.\n
        `sql_path` db파일의 경로를 지정합니다.\n

        ### Exception:
        `ConverException` : DB파일을 dict타입의 데이터로 변환 중 오류가 발생하였을 때 반환되는 예외 클래스입니다.\n
        `ConvertTypeExcetion` : `save` 메소드 파라미터중 type에서 set 또는 update 의외의 값을 지정하였을 때 반환되는 예외 클래스입니다.\n
        `SavaException` : json파일을 저장 중 오류가 발생했을 때 반환되는 예외 클래스입니다.
        """
        self.jsonly = jsonly
        self.sql = sql_path

    def to_dict(
        self, table_name: str, filter: dict[str, Union[str, int]] = None
    ) -> list[dict[str, any]]:
        """
        DB파일을 dict타입으로 변환합니다.\n
        Convert DB file to dict type.

        ## <Parameter>
        #### table_name:
        데이터를 가져올 데이터베이스의 테이블 명을 지정합니다.

        #### filter:
        조건에 맞는 데이터만 불러옵니다. 만약 필요한 경우 이 인수를 지정하세요.\n
        ex) id가 1인 유저 : { "id" : 1 }
        """
        try:
            connect = sqlite3.connect(self.sql)
            dict_factory = lambda columns, rows: dict(
                zip((x[0] for x in columns.description), rows)
            )
            connect.row_factory = dict_factory
            cursor = connect.cursor()
            if filter:
                result = {}
                for key in filter.keys():
                    print(key)
                    cursor.execute(
                        f"SELECT * FROM {table_name} WHERE {key}='{filter[key]}'"
                    )
                    if len(filter.keys()) == 1:
                        return cursor.fetchall()
                    result[filter[key]] = cursor.fetchall()
                return result

            else:
                cursor.execute(f"SELECT * FROM {table_name}")
                result = cursor.fetchall()
            cursor.close()
            connect.close()
            return result
        except Exception as exception:
            raise ConverException(exception)

    def save(self, table_name: str, type: str = "set") -> bool:
        """
        DB파일의 데이터를 json파일에 저장합니다.\n
        Save data from DB file to json file

        ## <Parameter>
        #### table_name:
        데이터를 변환 시킬 테이블을 지정합니다.

        #### type:
        저장할 유형을 선택합니다. set 또는 update 중에서 선택 가능합니다.
        """
        if type == "set":
            return self.jsonly.set(self.to_dict(table_name=table_name))
        elif type == "update":
            data = self.to_dict(table_name=table_name)
            if isinstance(data, list):
                return self.jsonly.update({table_name: data})
            return self.jsonly.update(self.to_dict(table_name=table_name))
        else:
            raise ConvertTypeExcetion("'set' 또는 'update' 타입만 입력해주세요!")

    def save_as(self, table_name: str, path: str) -> bool:
        """
        새로운 json파일을 생성해 데이터를 저장합니다.\n
        Create a new json file to save the data.

        ## <Parameter>
        #### table_name:
        데이터를 변환 시킬 테이블을 지정합니다.

        #### path:
        새로운 json파일을 생성할 경로를 지정합니다.
        """
        if path.endswith(".json"):
            data = self.to_dict(table_name=table_name)
            try:
                with open(path, "w", encoding=self.jsonly.encoding) as f:
                    json.dump(data, f, indent=4, ensure_ascii=self.jsonly.ensure_ascii)
                return True
            except Exception as exception:
                raise SaveException(exception)
        else:
            raise SaveException("path 파라미터는 반드시 .json으로 끝나야 합니다.")
