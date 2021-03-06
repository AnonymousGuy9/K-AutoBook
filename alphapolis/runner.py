# --- coding: utf-8 ---
"""
アルファポリスの実行クラスモジュール
"""

import re
from runner import AbstractRunner
from alphapolis.manager import Manager


class Runner(AbstractRunner):
    """
    アルファポリスの実行クラス
    """

    domain_pattern = 'www\.alphapolis\.co\.jp'
    """
    サポートするドメイン
    """

    patterns = [
        'manga\/official\/\d+',
        'manga\/viewManga\/(\?.*no=)?\d+',
        'manga\/official\/\d+/\d+'
    ]
    """
    サポートするアルファポリスのパスの正規表現のパターンのリスト
    """

    def run(self):
        """
        アルファポリスの実行
        """
        _destination = input('Output Path > ')
        _manager = Manager(_destination)
        _manager.start(self.url)
        return
