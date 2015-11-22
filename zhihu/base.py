from .common import BeautifulSoup
from requests import Response


class BaseZhihu:
    def _gen_soup(self, content):
        self.soup = BeautifulSoup(content)

    def _get_content(self):
        return self._session.get(self.url).content

    def _make_soup(self):
        if self.url and not self.soup:
            content = self._get_content()
            self._gen_soup(content)

    @classmethod
    def from_html(cls, content):
        obj = cls(url=None)
        obj._gen_soup(content)
        return obj


class JsonAsSoupMixin:
    def _gen_soup(self, content):
        # 为了让`from_html`对外提供统一的接口, 判断一下输入, 如果是bytes 或者 str 则转换为json,
        # 否则认为是由_get_content返回的json

        if isinstance(content, (bytes, str)):
            r = Response()
            r._content = content
            soup = r.json()
            self.soup = soup
        else:
            self.soup = content
