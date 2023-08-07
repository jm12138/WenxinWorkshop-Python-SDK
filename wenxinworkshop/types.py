from typing import List
from typing import TypedDict, Literal, Optional


__all__ = [
    'Headers',
    'Message', 'Messages',
    'ChatParams', 'ChatData', 'ChatResponse',
    'AccessTokenParams', 'AccessTokenResponse'
]


class Message(TypedDict):
    role: Literal['user', 'assistant']
    content: str


class ChatParams(TypedDict):
    access_token: str


class ChatData(TypedDict):
    messages: 'Messages'
    temperature: Optional[float]
    top_p: Optional[float]
    penalty_score: Optional[float]
    stream: Optional[bool]
    user_id: Optional[str]


class ChatUsage(TypedDict):
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


class ChatResponse(TypedDict):
    id: str
    object: str
    created: int
    sentence_id: int
    is_end: bool
    is_truncated: bool
    result: str
    need_clear_history: bool
    ban_round: int
    usage: ChatUsage


class AccessTokenParams(TypedDict):
    grant_type: str
    client_id: str
    client_secret: str


class AccessTokenResponse(TypedDict):
    refresh_token: str
    expires_in: int
    Messages_key: str
    access_token: str
    scope: str
    Messages_secret: str


class Headers(TypedDict):
    Content_Type: str
    Accept: Optional[str]


class StateDict(TypedDict):
    user_id: str
    messages: 'Messages'


Messages = List[Message]
