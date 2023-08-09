import json
import requests

from typing import Optional, Generator, Union

from .types import Messages, Embeddings, Texts

from .types import Message
from .types import Headers, Params
from .types import ChatData, ChatResponse
from .types import EmbeddingData, EmbeddingResponse
from .types import AccessTokenParams, AccessTokenResponse


__all__ = ['ERNIEBot', 'ERNIEEmbedding', 'get_access_token']


def get_access_token(
    api_key: str,
    secret_key: str
) -> str:
    '''
    根据 API Key 和 Secret Key 获取 Access Token
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


class ERNIEBot:
    ERNIEBot = 'https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions'
    ERNIEBot_turbo = 'https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/eb-instant'

    def __init__(
        self: 'ERNIEBot',
        api_key: str,
        secret_key: str,
        url: str = ERNIEBot
    ) -> None:
        self.url = url
        self.access_token = get_access_token(
            api_key=api_key,
            secret_key=secret_key
        )

    def __call__(
        self: 'ERNIEBot',
        messages: Messages,
        temperature: Optional[float] = None,
        top_p: Optional[float] = None,
        penalty_score: Optional[float] = None,
        stream: Optional[bool] = None,
        user_id: Optional[str] = None,
        chunk_size: Optional[int] = 512
    ) -> Union[str, Generator[str, None, None]]:
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


class ERNIEEmbedding:
    EmbeddingV1 = 'https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/embeddings/embedding-v1'

    def __init__(
        self: 'ERNIEEmbedding',
        api_key: str,
        secret_key: str,
        url: str = EmbeddingV1
    ) -> None:
        self.url = url
        self.access_token = get_access_token(
            api_key=api_key,
            secret_key=secret_key
        )

    def __call__(
        self: 'ERNIEEmbedding',
        texts: Texts,
        user_id: Optional[str] = None
    ) -> Embeddings:
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


if __name__ == "__main__":
    api_key = ''
    secret_key = ''

    erniebot = ERNIEBot(
        api_key=api_key,
        secret_key=secret_key,
        url=ERNIEBot.ERNIEBot
    )

    message = Message(
        role='user',
        content='你好！'
    )
    messages: Messages = [message]

    response = erniebot(
        messages=messages,
        temperature=None,
        top_p=None,
        penalty_score=None,
        stream=None,
        user_id=None,
        chunk_size=512
    )

    print(response)

    response_stream = erniebot(
        messages=messages,
        temperature=None,
        top_p=None,
        penalty_score=None,
        stream=True,
        user_id=None,
        chunk_size=512
    )

    for item in response_stream:
        print(item, end='')

    ernieembedding = ERNIEEmbedding(
        api_key=api_key,
        secret_key=secret_key,
        url=ERNIEEmbedding.EmbeddingV1
    )

    texts: Texts = [
        '你好！',
        '你好吗？',
        '你是谁？'
    ]

    response = ernieembedding(
        texts=texts,
        user_id=None
    )

    print(response)
