#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2025 - Present Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam (谭淞)
# @Email  : sepinetam@gmail.com
# @File   : client_polling.py

from typing import List

from openai import AsyncOpenAI, OpenAI

from .api_polling import APIPolling


class ClientPolling:
    def __init__(self,
                 api_keys: List[str],
                 *args, **kwargs):
        self.api_key_polling = APIPolling(api_keys)
        self.openai_kwargs = kwargs.copy()

    def __len__(self):
        return self.api_key_polling.polling_length

    @property
    def client(self) -> OpenAI:
        client = OpenAI(
            api_key=self.api_key_polling.api_key,
            **self.openai_kwargs
        )
        return client

    @property
    def async_client(self) -> OpenAI:
        client = AsyncOpenAI(
            api_key=self.api_key_polling.api_key,
            **self.openai_kwargs
        )
        return client

