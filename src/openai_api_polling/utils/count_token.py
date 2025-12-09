#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2025 - Present Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam (谭淞)
# @Email  : sepinetam@gmail.com
# @File   : count_token.py

from typing import Dict, List

from tiktoken import Encoding, get_encoding

from ..core import OpenAIResources


class CountToken:
    ENCODING_MODEL_MAPPING: Dict[str, Encoding] = {
        OpenAIResources.CHAT: get_encoding("o200k_base"),
        OpenAIResources.EMBEDDING: get_encoding("cl100k_base"),
    }

    def __init__(self, method: OpenAIResources | str = OpenAIResources.CHAT):
        self.method = method

    @property
    def encoding_fn(self) -> Encoding:
        return self.ENCODING_MODEL_MAPPING.get(self.method, self.ENCODING_MODEL_MAPPING[OpenAIResources.CHAT])

    def encoding(self, text: str) -> List[int]:
        """Encodes a string into tokens."""
        return self.encoding_fn.encode(text)

    def token(self, text: str) -> int:
        """Returns the number of tokens."""
        return len(self.encoding(text))


if __name__ == "__main__":
    token_counter = CountToken(OpenAIResources.EMBEDDING)
    print(token_counter.token("Hello, world!"))
