import json
import warnings

from .error import PathException


class Connect:
    def __init__(self, path: str, encoding: str, ensure_ascii: bool) -> None:
        """
        `path` Json파일의 경로를 입력합니다.\n
        `encoding` json파일의 인코딩 형식을 지정합니다.\n
        `ensure_ascii` ascii문자가 아닌 문자의 손실을 방지합니다. (기본값 추천)

        ### Exception:
        `PathException` : json파일의 경로가 잘못되었거나 찾을 수 없을때 반환됩니다.\n
        `FormatExcepton` : json파일의 찾았으나 `Dict`타입으로 변환이 불가할때 반환되는 예외 클래스 입니다.
        """
        try:
            with open(path, "r", encoding=encoding) as f:
                json.load(f)
        except Exception as exception:
            if str(exception).endswith("line 1 column 1 (char 0)"):
                dic = {}
                dic = dic.setdefault(None, {})
                with open(path, "w", encoding=encoding) as f:
                    json.dump(dic, f, indent=4, ensure_ascii=ensure_ascii)
                warnings.warn("빈 Json파일을 초기값으로 자동 설정 하였습니다.", UserWarning)
            else:
                raise PathException(exception)
        else:
            self.path = path
            self.encoding = encoding
            self.ensure_ascii = ensure_ascii

            