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
    '''
    Message object.

    Attributes
    ----------
    role : Literal['user', 'assistant']
        Role of the message.

    content : str
        Content of the message.

    Examples
    --------
    >>> Message(
    ...     role='user',
    ...     content='你好！'
    ... )
    {
        'role': 'user', 
        'content': '你好！'
    }
    '''
    role: Literal['user', 'assistant']
    content: str


class Params(TypedDict):
    '''
    Params object for APIs.

    Attributes
    ----------
    access_token : str
        Access token for APIs.

    Examples
    --------
    >>> Params(
    ...     access_token='...'
    ... )
    {
        'access_token': '...'
    }
    '''

    access_token: str


class ChatData(TypedDict):
    '''
    Chat API data object.

    Attributes
    ----------
    messages : Messages
        Messages to chat.

    temperature : Optional[float]
        Temperature of the chat.

    top_p : Optional[float]
        Top p of the chat.

    penalty_score : Optional[float] 
        Penalty score of the chat.

    stream : Optional[bool]
        Whether to stream the response.

    user_id : Optional[str]
        User ID of the chat.

    Examples
    --------
    >>> ChatData(
    ...     messages=[
    ...         Message(
    ...             role='user',
    ...             content='你好！'
    ...         )
    ...     ],
    ...     temperature=0.8,
    ...     top_p=0.9,
    ...     penalty_score=1.0,
    ...     stream=False,
    ...     user_id='...'
    ... )
    {
        'messages': [
            {
                'role': 'user',
                'content': '你好！'
            }
        ],  
        'temperature': 0.8,
        'top_p': 0.9,
        'penalty_score': 1.0,
        'stream': False,
        'user_id': '...'
    }
    '''
    messages: 'Messages'
    temperature: Optional[float]
    top_p: Optional[float]
    penalty_score: Optional[float]
    stream: Optional[bool]
    user_id: Optional[str]


class ChatUsage(TypedDict):
    '''
    Chat API usage object.

    Attributes
    ----------
    prompt_tokens : int
        Prompt tokens of the chat.

    completion_tokens : int
        Completion tokens of the chat.

    total_tokens : int
        Total tokens of the chat.

    Examples
    --------
    >>> ChatUsage(
    ...     prompt_tokens=0,
    ...     completion_tokens=0,
    ...     total_tokens=0
    ... )
    {
        'prompt_tokens': 0,
        'completion_tokens': 0,
        'total_tokens': 0
    }
    '''
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


class ChatResponse(TypedDict):
    '''
    Chat API response object.

    Attributes
    ----------
    id : str
        ID of the response.

    object : str
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

    Examples
    --------
    >>> ChatResponse(
    ...     id='...',
    ...     object='...',
    ...     created=0,
    ...     sentence_id=0,
    ...     is_end=False,
    ...     is_truncated=False,
    ...     result='...',
    ...     need_clear_history=False,
    ...     ban_round=0,
    ...     usage=ChatUsage(
    ...         prompt_tokens=0,
    ...         completion_tokens=0,
    ...         total_tokens=0
    ...     )
    ... )
    {
        'id': '...',
        'object': '...',
        'created': 0,
        'sentence_id': 0,
        'is_end': False,
        'is_truncated': False,
        'result': '...',
        'need_clear_history': False,
        'ban_round': 0,
        'usage': {
            'prompt_tokens': 0, 
            'completion_tokens': 0,
            'total_tokens': 0
        }
    }
    '''
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
    '''
    Embedding API data object.

    Attributes
    ----------
    texts : List[str]
        Texts to embed.

    user_id : Optional[str]
        User ID of the embedding.

    Examples
    --------
    >>> EmbeddingData(
    ...     texts=[
    ...         '你好！'
    ...     ],
    ...     user_id='...'
    ... )
    {
        'texts': [
            '你好！'
        ],
        'user_id': '...'
    }
    '''
    input: List[str]
    user_id: Optional[str]


class EmbeddingObject(TypedDict):
    '''
    Embedding API object object.

    Attributes
    ----------
    object : Literal['embedding']
        Object of the embedding.

    embedding : Embedding
        Embedding of the embedding.

    index : int
        Index of the embedding.

    Examples
    --------    
    >>> EmbeddingObject(
    ...     object='embedding',
    ...     embedding=[
    ...         0.0,
    ...         0.0,
    ...         0.0,
    ...         ...
    ...     ],
    ...     index=0
    ... )
    {
        'object': 'embedding',
        'embedding': [
            0.0,
            0.0,
            0.0,
            ...
        ],
        'index': 0
    }
    '''
    object: Literal['embedding']
    embedding: 'Embedding'
    index: int


class EmbeddingUsage(TypedDict):
    '''
    Embedding API usage object.

    Attributes
    ----------
    prompt_tokens : int
        Prompt tokens of the embedding.

    total_tokens : int
        Total tokens of the embedding.

    Examples
    --------
    >>> EmbeddingUsage(
    ...     prompt_tokens=0,
    ...     total_tokens=0
    ... )   
    {   
        'prompt_tokens': 0,
        'total_tokens': 0
    }
    '''
    prompt_tokens: int
    total_tokens: int


class EmbeddingResponse(TypedDict):
    '''
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

    Examples
    --------
    >>> EmbeddingResponse(
    ...     id='...',
    ...     object='embedding_list',
    ...     created=0,
    ...     data=[
    ...         EmbeddingObject(
    ...             object='embedding',
    ...             embedding=[
    ...                 0.0,
    ...                 0.0,
    ...                 0.0,
    ...                 ...
    ...             ],
    ...             index=0
    ...         )
    ...     ],
    ...     usage=EmbeddingUsage(
    ...         prompt_tokens=0,
    ...         total_tokens=0
    ...     )
    ... )
    {
        'id': '...',
        'object': 'embedding_list',
        'created': 0,
        'data': [
            {
                'object': 'embedding',
                'embedding': [
                    0.0,
                    0.0,
                    0.0,
                    ...
                ],
                'index': 0
            }
        ],
        'usage': {
            'prompt_tokens': 0,
            'total_tokens': 0
        }
    }
    '''
    id: str
    object: Literal['embedding_list']
    created: int
    data: List[EmbeddingObject]
    usage: EmbeddingUsage


class AccessTokenParams(TypedDict):
    '''
    Access token params object.

    Attributes
    ----------
    grant_type : str
        Grant type of the access token.

    client_id : str
        Client ID of the access token.

    client_secret : str
        Client secret of the access token.

    Examples
    --------
    >>> AccessTokenParams(
    ...     grant_type='...',
    ...     client_id='...',
    ...     client_secret='...'
    ... )
    {
        'grant_type': '...',
        'client_id': '...',
        'client_secret': '...'
    }
    '''
    grant_type: str
    client_id: str
    client_secret: str


class AccessTokenResponse(TypedDict):
    '''
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

    Examples
    --------
    >>> AccessTokenResponse(
    ...     refresh_token='...',
    ...     expires_in=0,
    ...     session_key='...',
    ...     access_token='...',
    ...     scope='...',
    ...     session_secret='...'
    ... )
    {
        'refresh_token': '...',
        'expires_in': 0,
        'seesion_key': '...',
        'access_token': '...',
        'scope': '...',
        'session_secret': '...'
    }
    '''
    refresh_token: str
    expires_in: int
    session_key: str
    access_token: str
    scope: str
    session_secret: str


class PromptTemplateParams(TypedDict):
    '''
    Prompt template params object.

    Attributes
    ----------  
    access_token : str
        Access token of the prompt template.

    id : int
        ID of the prompt template.

    Examples
    --------
    >>> PromptTemplateParams(
    ...     access_token='...',
    ...     id=0
    ... )
    {
        'access_token': '...',
        'id': 0
    }
    '''
    access_token: str
    id: int


class PromptTemplateResult(TypedDict):
    '''
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

    Examples
    --------
    >>> PromptTemplateResult(
    ...     templateId='...',   
    ...     templateName='...',
    ...     templateContent='...',
    ...     templateVariables='...',
    ...     content='...'
    ... )
    {
        'templateId': '...',
        'templateName': '...',
        'templateContent': '...',
        'templateVariables': '...',
        'content': '...'
    }
    '''
    templateId: str
    templateName: str
    templateContent: str
    templateVariables: str
    content: str


class PromptTemplateResponse(TypedDict):
    '''
    Prompt template response object.

    Attributes
    ----------
    log_id : int
        Log ID of the prompt template.

    result : PromptTemplateResult
        Result of the prompt template.

    Examples
    --------
    >>> PromptTemplateResponse(
    ...     log_id=0,
    ...     result=PromptTemplateResult(
    ...         templateId='...',
    ...         templateName='...',
    ...         templateContent='...',
    ...         templateVariables='...',
    ...         content='...'
    ...     )
    ... )
    {
        'log_id': 0,
        'result': {
            'templateId': '...',
            'templateName': '...',
            'templateContent': '...',
            'templateVariables': '...',
            'content': '...'
        }
    }
    '''
    log_id: int
    result: PromptTemplateResult


class Headers(TypedDict):
    '''
    Headers object.

    Attributes
    ----------
    Content_Type : str
        Content type of the headers.

    Accept : Optional[str]
        Accept of the headers.

    Examples
    --------
    >>> Headers(
    ...     Content_Type='...',
    ...     Accept='...'
    ... )
    {
        'Content_Type': '...',  
        'Accept': '...'
    }
    '''
    Content_Type: str
    Accept: Optional[str]


'''
Type aliases.
'''
# A List of str
Texts = List[str]

# A List of float
Embedding = List[float]

# A List of Embedding
Embeddings = List[Embedding]

# A List of Message
Messages = List[Message]
