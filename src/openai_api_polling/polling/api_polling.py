#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2025 - Present Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam (谭淞)
# @Email  : sepinetam@gmail.com
# @File   : api_polling.py

from __future__ import annotations

from os import PathLike
from pathlib import Path
from typing import List


class APIPolling:
    def __init__(self,
                 api_keys: APIPolling | List[str]):
        if isinstance(api_keys, APIPolling):
            self.api_polling = list(api_keys.api_polling).copy()
        else:
            self.api_polling = api_keys
        self._index = 0

    def __str__(self):
        r = f"API Polling, this polling has {self.polling_length} APIs:\n"
        for index in range(self.polling_length):
            r += f"index: {index:>3} | API: {self.mask_api_key(self.api_polling[index])}\n"
        return r

    def __len__(self):
        return self.polling_length

    @property
    def api_key(self):
        return self._get_next_api()

    @property
    def polling_length(self):
        return len(self.api_polling)

    def _index_plus(self):
        self._index += 1
        if self._index >= self.polling_length:
            self.reset_index(0)
        return self._index

    def _get_next_api(self):
        next_api = self.api_polling[self._index]
        self._index_plus()
        return next_api

    def reset_index(self, index: int = 0):
        if index > self.polling_length:
            index = 0
        self._index = index

    @staticmethod
    def mask_api_key(api_key: str,
                     visible: int = 3,
                     mask_char: str = "*",
                     mask_len: int = 3):
        if not api_key:
            return ""
        prefix = api_key[:visible]
        suffix = api_key[-visible:]
        return prefix + (mask_char * mask_len) + suffix

    @classmethod
    def load_api(cls,
                 api_file: str | PathLike = Path.home() / ".api") -> APIPolling:
        api_file = Path(api_file).expanduser().absolute().as_posix()
        api_keys: List[str] = []
        with open(api_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):  # 只添加非空行且不以#开头的行
                    api_keys.append(line)
        return cls(api_keys)


if __name__ == "__main__":
    api_list = [
        "sk-thisiskey1", "sk-thisiskey2", "sk-thisiskey3",
    ]
    api_polling = APIPolling(api_list)

    print(api_polling)

    # To show 10 times api
    for _ in range(10):
        print(api_polling.api_key)
