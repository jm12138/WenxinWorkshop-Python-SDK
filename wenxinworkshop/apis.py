import json
import requests

from typing import Optional, Generator, Union

from .types import Messages, Embeddings, Texts

from .types import Message
from .types import Headers, Params
from .types import ChatData, ChatResponse
from .types import EmbeddingData, EmbeddingResponse
from .types import AccessTokenParams, AccessTokenResponse
from .types import PromptTemplateParams, PromptTemplateResponse


__all__ = ['LLMAPI', 'EmbeddingAPI', 'PromptTemplateAPI', 'get_access_token']


def get_access_token(
    api_key: str,
    secret_key: str
) -> str:
    '''
    Get access token from Baidu AI Cloud.

    Parameters
    ----------
    api_key : str
        API key from Baidu AI Cloud.
    secret_key : str
        Secret key from Baidu AI Cloud.

    Returns
    -------
    str
        Access token from Baidu AI Cloud.

    Raises
    ------
    ValueError
        If request failed. Please check your API key and secret key.

    Examples
    --------
    >>> from wenxinworkshop import get_access_token
    >>> api_key = ''
    >>> secret_key = ''
    >>> access_token = get_access_token(
    ...     api_key=api_key,
    ...     secret_key=secret_key
    ... )
    >>> print(access_token)
    24.6b3b3f7b0b3b3f7b0b3b3f7b0b3b3f7b.2592000.1628041234.222222-44444444
    '''
    url = "https://aip.baidubce.com/oauth/2.0/token"

    headers: Headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    params: AccessTokenParams = {
        'grant_type': 'client_credentials',
        'client_id': api_key,
        'client_secret': secret_key
    }

    response: requests.Response = requests.request(
        method="POST",
        url=url,
        headers=headers,
        params=params
    )

    try:
        response_json: AccessTokenResponse = response.json()
        return response_json['access_token']
    except:
        raise ValueError(response.text)


class LLMAPI:
    '''
    LLM API.

    Attributes
    ----------
    url : str
        URL of LLM API.

    access_token : str
        Access token from Baidu AI Cloud.

    ERNIEBot : str
        URL of ERNIEBot LLM API.

    ERNIEBot_turbo : str
        URL of ERNIEBot turbo LLM API.

    Methods
    -------
    __init__(
        self,
        api_key: str,
        secret_key: str,
        url: Optional[str] = LLMAPI.ERNIEBot
    ) -> None:
        Initialize LLM API.

    __call__(
        self,
        messages: Messages,
        temperature: Optional[float] = None,
        top_p: Optional[float] = None,
        penalty_score: Optional[float] = None,
        stream: Optional[bool] = None,
        user_id: Optional[str] = None,
        chunk_size: Optional[int] = 512
    ) -> Union[str, Generator[str, None, None]]:
        Get response from LLM API.

    stream_response(
        response: requests.Response,
        chunk_size: Optional[int] = 512
    ) -> Generator[str, None, None]:
        Stream response from LLM API.

    Examples
    --------
    >>> from wenxinworkshop import LLMAPI
    >>> api_key = ''
    >>> secret_key = ''
    >>> erniebot = LLMAPI(
    ...     api_key=api_key,
    ...     secret_key=secret_key,
    ...     url=LLMAPI.ERNIEBot
    ... )

    >>> message = Message(
    ...     role='user',
    ...     content='你好！'
    ... )
    >>> messages: Messages = [message]

    >>> response = erniebot(
    ...     messages=messages,
    ...     temperature=None,
    ...     top_p=None,
    ...     penalty_score=None,
    ...     stream=None,
    ...     user_id=None,
    ...     chunk_size=512
    ... )

    >>> print(response)
    你好，有什么可以帮助你的。
    '''
    ERNIEBot = 'https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions'
    ERNIEBot_turbo = 'https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/eb-instant'

    def __init__(
        self: 'LLMAPI',
        api_key: str,
        secret_key: str,
        url: Optional[str] = ERNIEBot
    ) -> None:
        '''
        Initialize LLM API.

        Parameters
        ----------
        api_key : str
            API key from Baidu AI Cloud.

        secret_key : str
            Secret key from Baidu AI Cloud.

        url : Optional[str], optional
            URL of LLM API, by default LLMAPI.ERNIEBot. You can also use LLMAPI.ERNIEBot_turbo or other LLM API urls.

        Examples
        --------
        >>> from wenxinworkshop import LLMAPI
        >>> api_key = ''
        >>> secret_key = ''
        >>> erniebot = LLMAPI(
        ...     api_key=api_key,
        ...     secret_key=secret_key,
        ...     url=LLMAPI.ERNIEBot
        ... )
        '''
        self.url = url
        self.access_token = get_access_token(
            api_key=api_key,
            secret_key=secret_key
        )

    def __call__(
        self: 'LLMAPI',
        messages: Messages,
        temperature: Optional[float] = None,
        top_p: Optional[float] = None,
        penalty_score: Optional[float] = None,
        stream: Optional[bool] = None,
        user_id: Optional[str] = None,
        chunk_size: Optional[int] = 512
    ) -> Union[str, Generator[str, None, None]]:
        '''
        Get response from LLM API.

        Parameters
        ----------
        messages : Messages
            Messages from user and assistant.

        temperature : Optional[float], optional
            Temperature of LLM API, by default None.

        top_p : Optional[float], optional
            Top p of LLM API, by default None.

        penalty_score : Optional[float], optional
            Penalty score of LLM API, by default None.

        stream : Optional[bool], optional
            Stream of LLM API, by default None.

        user_id : Optional[str], optional
            User ID of LLM API, by default None.

        chunk_size : Optional[int], optional
            Chunk size of LLM API, by default 512.

        Returns
        -------
        Union[str, Generator[str, None, None]]
            Response from LLM API.

        Raises
        ------
        ValueError
            If request failed. Please check your API key and secret key. Or check the parameters.

        Examples
        --------
        >>> message = Message(
        ...     role='user',
        ...     content='你好！'
        ... )
        >>> messages: Messages = [message]

        >>> response = erniebot(
        ...     messages=messages,
        ...     temperature=None,
        ...     top_p=None,
        ...     penalty_score=None,
        ...     stream=None,
        ...     user_id=None,
        ...     chunk_size=512
        ... )

        >>> print(response)
        你好，有什么可以帮助你的。

        >>> response_stream = erniebot(
        ...     messages=messages,
        ...     temperature=None,
        ...     top_p=None,
        ...     penalty_score=None,
        ...     stream=True,
        ...     user_id=None,
        ...     chunk_size=512
        ... )

        >>> for item in response_stream:
        ...     print(item, end='')
        你好，有什么可以帮助你的。
        '''
        headers: Headers = {
            'Content-Type': 'application/json'
        }

        params: Params = {
            'access_token': self.access_token
        }

        data: ChatData = {
            'messages': messages,
            'temperature': temperature,
            'top_p': top_p,
            'penalty_score': penalty_score,
            'stream': stream,
            'user_id': user_id
        }

        response = requests.request(
            method="POST",
            url=self.url,
            headers=headers,
            params=params,
            data=json.dumps(data),
            stream=stream
        )

        if stream:
            return self.stream_response(
                response=response,
                chunk_size=chunk_size
            )
        else:
            try:
                response_json: ChatResponse = response.json()
                return response_json['result']
            except:
                raise ValueError(response.text)

    @staticmethod
    def stream_response(
        response: requests.Response,
        chunk_size: Optional[int] = 512
    ) -> Generator[str, None, None]:
        '''
        Stream response from LLM API.

        Parameters
        ----------
        response : requests.Response
            Response from LLM API.

        chunk_size : Optional[int], optional
            Chunk size of LLM API, by default 512.

        Yields
        -------
        Generator[str, None, None]
            Response from LLM API.

        Raises
        ------
        ValueError
            If request failed. Please check your API key and secret key. Or check the parameters.

        Examples
        --------
        >>> stream_response = erniebot.stream_response(
        ...     response=response,
        ...     chunk_size=512
        ... )

        >>> for item in stream_response:
        ...     print(item, end='')
        你好，有什么可以帮助你的。
        '''
        for response_line in response.iter_lines(
            chunk_size=chunk_size,
            decode_unicode='UTF-8'
        ):
            if response_line:
                try:
                    response_json: ChatResponse = json.loads(response_line[5:])
                    yield response_json['result']
                except:
                    raise ValueError(response_line)


class EmbeddingAPI:
    '''
    Embedding API.

    Attributes
    ----------
    url : str
        URL of Embedding API.

    access_token : str
        Access token from Baidu AI Cloud.

    EmbeddingV1 : str
        URL of Embedding V1 API.

    Methods
    -------
    __init__(
        self,
        api_key: str,
        secret_key: str,
        url: Optional[str] = EmbeddingAPI.EmbeddingV1
    ) -> None:
        Initialize Embedding API.

    __call__(
        self,
        texts: Texts,
        user_id: Optional[str] = None
    ) -> Embeddings:
        Get embeddings from Embedding API.

    Examples
    --------
    >>> from wenxinworkshop import EmbeddingAPI
    >>> api_key = ''
    >>> secret_key = ''
    >>> ernieembedding = EmbeddingAPI(
    ...     api_key=api_key,
    ...     secret_key=secret_key,
    ...     url=EmbeddingAPI.EmbeddingV1
    ... )

    >>> texts: Texts = [
    ...     '你好！',
    ...     '你好吗？',
    ...     '你是谁？'
    ... ]

    >>> response = ernieembedding(
    ...     texts=texts,
    ...     user_id=None
    ... )

    >>> print(response)
    [[0.123, 0.456, 0.789, ...], [0.123, 0.456, 0.789, ...], [0.123, 0.456, 0.789, ...]]
    '''
    EmbeddingV1 = 'https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/embeddings/embedding-v1'

    def __init__(
        self: 'EmbeddingAPI',
        api_key: str,
        secret_key: str,
        url: Optional[str] = EmbeddingV1
    ) -> None:
        '''
        Initialize Embedding API.

        Parameters
        ----------
        api_key : str
            API key from Baidu AI Cloud.

        secret_key : str
            Secret key from Baidu AI Cloud.

        url : Optional[str], optional
            URL of Embedding API, by default EmbeddingAPI.EmbeddingV1. You can also use other Embedding API urls.

        Examples
        --------
        >>> from wenxinworkshop import EmbeddingAPI
        >>> api_key = ''
        >>> secret_key = ''
        >>> ernieembedding = EmbeddingAPI(
        ...     api_key=api_key,
        ...     secret_key=secret_key,
        ...     url=EmbeddingAPI.EmbeddingV1
        ... )
        '''
        self.url = url
        self.access_token = get_access_token(
            api_key=api_key,
            secret_key=secret_key
        )

    def __call__(
        self: 'EmbeddingAPI',
        texts: Texts,
        user_id: Optional[str] = None
    ) -> Embeddings:
        '''
        Get embeddings from Embedding API.

        Parameters
        ----------
        texts : Texts
            Texts of inputs.

        user_id : Optional[str], optional
            User ID of Embedding API, by default None.

        Returns
        -------
        Embeddings
            Embeddings from Embedding API.

        Raises
        ------
        ValueError
            If request failed. Please check your API key and secret key. Or check the parameters.

        Examples
        --------
        >>> texts: Texts = [
        ...     '你好！',
        ...     '你好吗？',
        ...     '你是谁？'
        ... ]

        >>> response = ernieembedding(
        ...     texts=texts,
        ...     user_id=None
        ... )

        >>> print(response)
        [[0.123, 0.456, 0.789, ...], [0.123, 0.456, 0.789, ...], [0.123, 0.456, 0.789, ...]]
        '''
        headers: Headers = {
            'Content-Type': 'application/json'
        }

        params: Params = {
            'access_token': self.access_token
        }

        data: EmbeddingData = {
            'input': texts,
            'user_id': user_id
        }

        response = requests.request(
            method="POST",
            url=self.url,
            headers=headers,
            params=params,
            data=json.dumps(data)
        )

        try:
            response_json: EmbeddingResponse = response.json()
            embeddings: Embeddings = [
                embedding['embedding']
                for embedding in response_json['data']
            ]
            return embeddings
        except:
            raise ValueError(response.text)


class PromptTemplateAPI:
    '''
    Prompt Template API.

    Attributes
    ----------
    url : str
        URL of Prompt Template API.

    access_token : str
        Access token from Baidu AI Cloud.

    PromptTemplate : str
        URL of Prompt Template API.

    Methods
    -------
    __init__(
        self,   
        api_key: str,
        secret_key: str,
        url: Optional[str] = PromptTemplate
    ) -> None:
        Initialize Prompt Template API.

    __call__(
        self,
        template_id: int,
        **kwargs: str
    ) -> str:
        Get prompt template from Prompt Template API.

    Examples
    --------
    >>> from wenxinworkshop import PromptTemplateAPI
    >>> api_key = ''
    >>> secret_key = ''
    >>> prompttemplate = PromptTemplateAPI(
    ...     api_key=api_key,
    ...     secret_key=secret_key,
    ...     url=PromptTemplateAPI.PromptTemplate
    ... )

    >>> response = prompttemplate(
    ...     template_id=1968,
    ...     content='侏罗纪世界'
    ... )

    >>> print(response)
    我希望你充当一个电影评论家。你将编写一篇引人入胜和有创意的影评。你可以涵盖诸如情节、主题和基调、演技和角色、方向、配乐、电影摄影、制作设计、特效、剪辑、节奏、对话等主题。但最重要的方面是强调电影给你的感觉。什么是真正引起你的共鸣。你也可以对电影进行批评。请避免剧透。电影名称是侏罗纪世界。
    '''
    PromptTemplate = 'https://aip.baidubce.com/rest/2.0/wenxinworkshop/api/v1/template/info'

    def __init__(
        self: 'PromptTemplateAPI',
        api_key: str,
        secret_key: str,
        url: Optional[str] = PromptTemplate
    ) -> None:
        '''
        Initialize Prompt Template API.

        Parameters
        ----------
        api_key : str
            API key from Baidu AI Cloud.

        secret_key : str
            Secret key from Baidu AI Cloud.

        url : Optional[str], optional
            URL of Prompt Template API, by default PromptTemplateAPI.PromptTemplate. You can also use other Prompt Template API urls.

        Examples
        --------
        >>> from wenxinworkshop import PromptTemplateAPI
        >>> api_key = ''
        >>> secret_key = ''
        >>> prompttemplate = PromptTemplateAPI(
        ...     api_key=api_key,
        ...     secret_key=secret_key,
        ...     url=PromptTemplateAPI.PromptTemplate
        ... )
        '''
        self.url = url
        self.access_token = get_access_token(
            api_key=api_key,
            secret_key=secret_key
        )

    def __call__(self, template_id: int, **kwargs: str) -> str:
        '''
        Get prompt template from Prompt Template API.

        Parameters
        ----------
        template_id : int
            ID of prompt template.

        **kwargs : str
            Variables of prompt template.

        Returns
        -------
        str
            Prompt template content.

        Raises
        ------
        ValueError
            If request failed. Please check your API key and secret key. Or check the parameters.

        Examples
        --------
        >>> response = prompttemplate(
        ...     template_id=1968,
        ...     content='侏罗纪世界'
        ... )

        >>> print(response)

        '''
        headers: Headers = {
            'Content-Type': 'application/json'
        }

        params: PromptTemplateParams = {
            'access_token': self.access_token,
            'id': template_id
        }

        response = requests.request(
            method="GET",
            url=self.url,
            headers=headers,
            params={
                **params,
                **kwargs
            }
        )

        try:
            response_json: PromptTemplateResponse = response.json()
            return response_json['result']['content']
        except:
            raise ValueError(response.text)


if __name__ == "__main__":
    '''
    Configurations
    '''
    # Set API key and Secret key
    api_key = ''
    secret_key = ''

    '''
    LLM API Examples
    '''
    # create a LLM API
    erniebot = LLMAPI(
        api_key=api_key,
        secret_key=secret_key,
        url=LLMAPI.ERNIEBot
    )

    # create a message
    message = Message(
        role='user',
        content='你好！'
    )

    # create messages
    messages: Messages = [message]

    # get response from LLM API
    response = erniebot(
        messages=messages,
        temperature=None,
        top_p=None,
        penalty_score=None,
        stream=None,
        user_id=None,
        chunk_size=512
    )

    # print response
    print(response)

    # get response stream from LLM API
    response_stream = erniebot(
        messages=messages,
        temperature=None,
        top_p=None,
        penalty_score=None,
        stream=True,
        user_id=None,
        chunk_size=512
    )

    # print response stream
    for item in response_stream:
        print(item, end='')

    '''
    Embedding API Examples
    '''
    # create a Embedding API
    ernieembedding = EmbeddingAPI(
        api_key=api_key,
        secret_key=secret_key,
        url=EmbeddingAPI.EmbeddingV1
    )

    # create texts
    texts: Texts = [
        '你好！',
        '你好吗？',
        '你是谁？'
    ]

    # get embeddings from Embedding API
    response = ernieembedding(
        texts=texts,
        user_id=None
    )

    # print embeddings
    print(response)

    '''
    Prompt Template API Examples
    '''
    # create a Prompt Template API
    prompttemplate = PromptTemplateAPI(
        api_key=api_key,
        secret_key=secret_key,
        url=PromptTemplateAPI.PromptTemplate
    )

    # get prompt template from Prompt Template API
    response = prompttemplate(
        template_id=1968,
        content='侏罗纪世界'
    )

    # print prompt template
    print(response)
