#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2025 - Present Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam (谭淞)
# @Email  : sepinetam@gmail.com
# @File   : client_polling.py

from typing import List

import anthropic
from google import genai
from openai import AsyncOpenAI, OpenAI

from .api_polling import APIPolling


class ClientPolling:
    def __init__(self,
                 api_keys: APIPolling | List[str],
                 *args, **kwargs):
        self.api_polling = APIPolling(api_keys)
        self.client_kwargs = kwargs.copy()

    def __len__(self):
        return self.api_polling.polling_length

    @property
    def client(self) -> OpenAI:
        client = OpenAI(
            api_key=self.api_polling.api_key,
            **self.client_kwargs
        )
        return client

    @property
    def async_client(self) -> AsyncOpenAI:
        client = AsyncOpenAI(
            api_key=self.api_polling.api_key,
            **self.client_kwargs
        )
        return client


class GeminiClientPolling(ClientPolling):
    @property
    def client(self) -> genai.Client:
        client = genai.Client(
            api_key=self.api_polling.api_key,
            **self.client_kwargs
        )
        return client

    @property
    def async_client(self) -> genai.Client:
        """
        Google GenAI SDK not support async client. (At least I have not found that)
        """
        return self.client


class ClaudeClientPolling(ClientPolling):
    @property
    def client(self) -> anthropic.Anthropic:
        client = anthropic.Anthropic(
            api_key=self.api_polling.api_key,
            **self.client_kwargs
        )
        return client

    @property
    def async_client(self) -> anthropic.AsyncAnthropic:
        client = anthropic.AsyncAnthropic(
            api_key=self.api_polling.api_key,
            **self.client_kwargs
        )
        return client
