#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2025 - Present Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam (谭淞)
# @Email  : sepinetam@gmail.com
# @File   : client_polling.py

from __future__ import annotations

from os import PathLike
from pathlib import Path
from typing import List

import anthropic
from google import genai
from openai import AsyncOpenAI, OpenAI

from .api_polling import APIPolling


class ClientPolling:
    api_file = Path.home() / ".api"  # Default api file path

    def __init__(self,
                 api_keys: APIPolling | List[str] = None,
                 *args, **kwargs):
        if api_keys is None:
            self.api_polling = APIPolling.load_api()
        else:
            if isinstance(api_keys, APIPolling):
                self.api_polling = api_keys
            elif isinstance(api_keys, list):
                self.api_polling = APIPolling(api_keys)
            else:
                raise TypeError(f"api_keys must be APIPolling or list or None, but got {type(api_keys)}")
        self.client_kwargs = kwargs.copy()

    def __len__(self):
        return self.api_polling.polling_length

    @classmethod
    def load_from_api(cls,
                      api_file: str | PathLike = None,
                      *args, **kwargs) -> ClientPolling:
        api_polling = APIPolling.load_api(api_file or cls.api_file)
        return cls(api_polling, *args, **kwargs)

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
    api_file = Path.home() / ".gemini.api"

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
    api_file = Path.home() / ".claude.api"

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
