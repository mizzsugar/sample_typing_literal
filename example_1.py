from typing import Literal


def open_helper_before(file: str, mode: str) -> str:
    """Pythonの標準ライブラリの例を、typing.Literalを使わないで書いた例です。
    ソースコード内にあるif文を読まないとmodeにどんな値がくるか想定しにくいです。
    https://docs.python.org/3/library/typing.html#typing.Literal
    """
    if mode == 'r':
        return f'読込専用でファイル「{file}」を開きます'
    if mode == 'r':
        return f'読込専用バイナリモードでファイル「{file}」を開きます'
    if mode == 'w':
        return f'書込専用でファイル「{file}」を開きます'
    if mode == 'wb':
        return f'書込専用バイナリモードでファイル「{file}」を開きます'
    raise ValueError('モードは r, rb, w, wb のうちいずれかを指定してください')


MODE = Literal['r', 'rb', 'w', 'wb']


def open_helper_after(file: str, mode: MODE) -> str:
    """Pythonの標準ライブラリの例を一部改変しています。
    https://docs.python.org/3/library/typing.html#typing.Literal
    """
    if mode == 'r':
        return f'読込専用でファイル「{file}」を開きます'
    if mode == 'r':
        return f'読込専用バイナリモードでファイル「{file}」を開きます'
    if mode == 'w':
        return f'書込専用でファイル「{file}」を開きます'
    if mode == 'wb':
        return f'書込専用バイナリモードでファイル「{file}」を開きます'
    raise ValueError(f'モードは r, rb, w, wb のうちいずれかを指定してください')
