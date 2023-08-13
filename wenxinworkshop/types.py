from typing import List
from typing import TypedDict, Literal, Optional


__all__ = [
    'Texts',
    'Headers', 'Params',
    'Message', 'Messages',
    'Embedding', 'Embeddings',
    'ChatData', 'ChatResponse', 'ChatUsage',
    'AccessTokenParams', 'AccessTokenResponse',
    'PromptTemplateParams', 'PromptTemplateResult', 'PromptTemplateResponse',
    'EmbeddingData', 'EmbeddingResponse', 'EmbeddingUsage', 'EmbeddingObject'
]


class Message(TypedDict):
    role: Literal['user', 'assistant']
    content: str


class Params(TypedDict):
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


class EmbeddingData(TypedDict):
    input: List[str]
    user_id: Optional[str]


class EmbeddingObject(TypedDict):
    object: Literal['embedding']
    embedding: 'Embedding'
    index: int


class EmbeddingUsage(TypedDict):
    prompt_tokens: int
    total_tokens: int


class EmbeddingResponse(TypedDict):
    id: str
    object: str
    created: int
    data: List[EmbeddingObject]
    usage: EmbeddingUsage


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


class PromptTemplateParams(TypedDict):
    access_token: str
    id: int


class PromptTemplateResult(TypedDict):
    templateId: str
    templateName: str
    templateContent: str
    templateVariables: str
    content: str


class PromptTemplateResponse(TypedDict):
    log_id: int
    result: PromptTemplateResult


class Headers(TypedDict):
    Content_Type: str
    Accept: Optional[str]


Texts = List[str]
Embedding = List[float]
Embeddings = List[Embedding]
Messages = List[Message]
