
from typing import Dict, Final, Literal, Set, Union


def check_if_transition_is_valid_before(_from: str, to: str) -> bool:
    """文字列だけで申請状況の遷移をチェックする関数
    """
    if _from == '審査中' and to in {'差し戻し中', '承認済み'}:
        return True
    if _from == '差し戻し中' and to in {'審査中', '終了'}:
        return True
    if _from == '承認済み' and to in {'実施中', '終了'}:
        return True
    if _from == '実施中' and to in {'終了', '中断中'}:
        return True
    if _from == '中断中' and to in {'実施中', '終了'}:
        return True
    return False


APPLICATION_STATUS =\
    Literal['審査中', '差し戻し中', '承認済み', '実施中', '中断中', '終了']


class ApplicationStatusTransition:
    allowed: Dict[APPLICATION_STATUS, Set[APPLICATION_STATUS]]

    def __init__(self) -> None:
        self.allowed = {
            '審査中': {'差し戻し中', '承認済み'},
            '差し戻し中': {'審査中', '終了'},
            '承認済み': {'実施中', '終了'},
            '実施中': {'終了', '中断中'},
            '中断中': {'実施中', '終了'},
        }

    def check_if_transition_is_valid_after(
            self, _from: APPLICATION_STATUS, to: APPLICATION_STATUS) -> bool:
        """typing.Literalを使い、状態遷移専用のクラスを使ってチェック
        """
        allowd_states: Final = self.allowed[_from]
        return to in allowd_states
