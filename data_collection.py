from langchain_community.document_loaders import AsyncHtmlLoader
from langchain_community.document_transformers import Html2TextTransformer
import asyncio


async def load_and_transform(url: str) -> str:
    """
    Args:
        url (str): 웹 페이지 URL.

    Returns:
        str: 텍스트로 변환된 웹 페이지 내용.
    """
    try:
        # HTML 데이터 로드
        loader = AsyncHtmlLoader(
            [url],
            header_template={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
            }
        )
        print(f"URL에서 HTML 데이터를 로드 중: {url}")
        docs = await loader.aload()  # 비동기 방식으로 HTML 로드

        # HTML 데이터를 텍스트로 변환
        html2text = Html2TextTransformer()
        docs_transformed = html2text.transform_documents(docs)
        plain_text = docs_transformed[0].page_content
        print("텍스트로 변환 완료.")

        return plain_text
    except Exception as e:
        print(f"데이터 로드 및 변환 중 오류 발생: {e}")
        return ""
if __name__ == "__main__":
    url = "https://namu.wiki/w/%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD"
    result = asyncio.run(load_and_transform(url))
    print("결과 텍스트:\n", result)
