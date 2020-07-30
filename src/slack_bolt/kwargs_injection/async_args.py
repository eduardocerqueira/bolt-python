from logging import Logger
from typing import Callable, Awaitable, Dict

from slack_bolt.context import AsyncBoltContext
from slack_bolt.context.ack import AsyncAck
from slack_bolt.context.respond import AsyncRespond
from slack_bolt.context.say import AsyncSay
from slack_bolt.request.async_request import AsyncBoltRequest
from slack_bolt.response import BoltResponse
from slack_sdk.web.async_client import AsyncWebClient


class AsyncArgs():
    logger: Logger
    client: AsyncWebClient
    req: AsyncBoltRequest
    resp: BoltResponse
    context: AsyncBoltContext
    payload: Dict[str, any]
    ack: AsyncAck
    say: AsyncSay
    respond: AsyncRespond
    next: Callable[[], Awaitable[None]]

    def __init__(
        self,
        *,
        logger: Logger,
        client: AsyncWebClient,
        req: AsyncBoltRequest,
        resp: BoltResponse,
        context: AsyncBoltContext,
        payload: Dict[str, any],
        ack: AsyncAck,
        say: AsyncSay,
        respond: AsyncRespond,
        next: Callable[[], Awaitable[None]],
        **kwargs  # noqa
    ):
        self.logger: Logger = logger
        self.client: AsyncWebClient = client
        self.request = self.req = req
        self.response = self.resp = resp
        self.context: AsyncBoltContext = context
        self.payload: Dict[str, any] = payload
        self.body: Dict[str, any] = payload
        self.ack: AsyncAck = ack
        self.say: AsyncSay = say
        self.respond: AsyncRespond = respond
        self.next: Callable[[], Awaitable[None]] = next