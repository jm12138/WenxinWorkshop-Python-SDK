from typing import List
from typing import TypedDict, Literal


__all__ = [
    "Texts",
    "Message",
    "Messages",
    "Embedding",
    "Embeddings",
    "ChatResponse",
    "ChatUsage",
    "AccessTokenResponse",
    "PromptTemplateResult",
    "PromptTemplateResponse",
    "EmbeddingResponse",
    "EmbeddingUsage",
    "EmbeddingObject",
    "AIStudioChatUsage",
    "AIStudioChatResult",
    "AIStudioChatResponse",
    "AIStudioEmbeddingObject",
    "AIStudioEmbeddingUsage",
    "AIStudioEmbeddingResult",
    "AIStudioEmbeddingResponse",
]


"""
Type definitions of Wenxin Workshop.
"""


class Message(TypedDict):
    """
    Message object.

    Attributes
    ----------
    role : Literal['user', 'assistant']
        Role of the message.

    content : str
        Content of the message.
    """

    role: Literal["user", "assistant"]
    content: str


class ChatUsage(TypedDict):
    """
    Chat API usage object.

    Attributes
    ----------
    prompt_tokens : int
        Prompt tokens of the chat.

    completion_tokens : int
        Completion tokens of the chat.

    total_tokens : int
        Total tokens of the chat.
    """

    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


class ChatResponse(TypedDict):
    """
    Chat API response object.

    Attributes
    ----------
    id : str
        ID of the response.

    object : Literal['chat.completion']
        Object of the response.

    created : int
        Created time of the response.

    sentence_id : int
        Sentence ID of the response.

    is_end : bool
        Whether the response is end.

    is_truncated : bool
        Whether the response is truncated.

    result : str
        Result of the response.

    need_clear_history : bool
        Whether to clear the history.

    ban_round : int
        Ban round of the response.

    usage : ChatUsage
        Usage of the response.
    """

    id: str
    object: Literal["chat.completion"]
    created: int
    sentence_id: int
    is_end: bool
    is_truncated: bool
    result: str
    need_clear_history: bool
    ban_round: int
    usage: ChatUsage


class EmbeddingObject(TypedDict):
    """
    Embedding API object object.

    Attributes
    ----------
    object : Literal['embedding']
        Object of the embedding.

    embedding : Embedding
        Embedding of the embedding.

    index : int
        Index of the embedding.
    """

    object: Literal["embedding"]
    embedding: "Embedding"
    index: int


class EmbeddingUsage(TypedDict):
    """
    Embedding API usage object.

    Attributes
    ----------
    prompt_tokens : int
        Prompt tokens of the embedding.

    total_tokens : int
        Total tokens of the embedding.
    """

    prompt_tokens: int
    total_tokens: int


class EmbeddingResponse(TypedDict):
    """
    Embedding API response object.

    Attributes
    ----------
    id : str
        ID of the response.

    object : Literal['embedding_list']
        Object of the response.

    created : int
        Created time of the response.

    data : List[EmbeddingObject]

    usage : EmbeddingUsage
    """

    id: str
    object: Literal["embedding_list"]
    created: int
    data: List[EmbeddingObject]
    usage: EmbeddingUsage


class AccessTokenResponse(TypedDict):
    """
    Access token response object.

    Attributes
    ----------
    refresh_token : str
        Refresh token of the access token.

    expires_in : int
        Expires in of the access token.

    session_key : str
        Session key of the access token.

    access_token : str
        Access token of the access token.

    scope : str
        Scope of the access token.

    session_secret : str
        Session secret of the access token.
    """

    refresh_token: str
    expires_in: int
    session_key: str
    access_token: str
    scope: str
    session_secret: str


class PromptTemplateResult(TypedDict):
    """
    Prompt template result object.

    Attributes
    ----------
    templateId : str
        Template ID of the prompt template.

    templateName : str
        Template name of the prompt template.

    templateContent : str
        Template content of the prompt template.

    templateVariables : str
        Template variables of the prompt template.

    content : str
        Content of the prompt template.
    """

    templateId: str
    templateName: str
    templateContent: str
    templateVariables: str
    content: str


class PromptTemplateResponse(TypedDict):
    """
    Prompt template response object.

    Attributes
    ----------
    log_id : int
        Log ID of the prompt template.

    result : PromptTemplateResult
        Result of the prompt template.
    """

    log_id: int
    result: PromptTemplateResult


"""
Type definitions of AI Studio.
"""


class AIStudioChatUsage(TypedDict):
    """
    AIStudio Chat API usage object.

    Attributes
    ----------
    prompt_tokens : int
        Prompt tokens of the chat.

    completion_tokens : int
        Completion tokens of the chat.

    total_tokens : int
        Total tokens of the chat.
    """

    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


class AIStudioChatResult(TypedDict):
    """
    AI Studio Chat API result object.

    Attributes
    ----------
    id : str
        ID of the chat.

    object : str
        Object of the chat.

    created : int
        Created time of the chat.

    result : str
        Result of the chat.

    need_clear_history : bool
        Whether the chat need clear history.

    usage : ChatUsage
        Usage of the chat.
    """

    id: str
    object: Literal["chat.completion"]
    created: int
    result: str
    need_clear_history: bool
    usage: AIStudioChatUsage


class AIStudioChatResponse(TypedDict):
    """
    AI Studio Chat API response object.

    Attributes
    ----------
    logId : str
        Log ID of the chat.

    errorCode : int
        Error code of the chat.

    errorMsg : str
        Error message of the chat.

    result : AIStudioChatResult
        Result of the chat.
    """

    logId: str
    errorCode: int
    errorMsg: str
    result: AIStudioChatResult


class AIStudioEmbeddingObject(TypedDict):
    """
    AI Studio Embedding API object object.

    Attributes
    ----------
    object : Literal['embedding']
        Object of the embedding.

    embedding : Embedding
        Embedding of the embedding.

    index : int
        Index of the embedding.
    """

    object: Literal["embedding"]
    embedding: "Embedding"
    index: int


class AIStudioEmbeddingUsage(TypedDict):
    """
    AI Studio Embedding API usage object.

    Attributes
    ----------
    prompt_tokens : int
        Prompt tokens of the embedding.

    total_tokens : int
        Total tokens of the embedding.
    """

    prompt_tokens: int
    total_tokens: int


class AIStudioEmbeddingResult(TypedDict):
    """
    AI Studio Embedding API result object.

    Attributes
    ----------
    id : str
        ID of the embedding.

    object : Literal['embedding_list']
        Object of the embedding.

    created : int
        Created time of the embedding.

    data : List[EmbeddingObject]
        Data of the embedding.

    usage : EmbeddingUsage
        Usage of the embedding.
    """

    id: str
    object: Literal["embedding_list"]
    created: int
    data: List[EmbeddingObject]
    usage: AIStudioEmbeddingUsage


class AIStudioEmbeddingResponse(TypedDict):
    """
    AI Studio Embedding API response object.

    Attributes
    ----------
    logId : str
        Log ID of the embedding.

    errorCode : int
        Error code of the embedding.

    errorMsg : str
        Error message of the embedding.

    result : AIStudioEmbeddingResult
        Result of the embedding.
    """

    logId: str
    errorCode: int
    errorMsg: str
    result: AIStudioEmbeddingResult


"""
Type aliases.
"""
# A List of str
Texts = List[str]

# A List of float
Embedding = List[float]

# A List of Embedding
Embeddings = List[Embedding]

# A List of Message
Messages = List[Message]
