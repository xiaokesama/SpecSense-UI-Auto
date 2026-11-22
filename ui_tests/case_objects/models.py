from dataclasses import dataclass


@dataclass(frozen=True)
class BaseCase:
    case_id: str
    title: str


@dataclass(frozen=True)
class SearchCase(BaseCase):
    keyword: str
    empty_expected: bool


@dataclass(frozen=True)
class PageCase(BaseCase):
    page_key: str
    buttons: tuple
    headers: tuple
    table_expected: bool = True


@dataclass(frozen=True)
class DrawerCase(BaseCase):
    page_key: str
    trigger: str
    drawer_title: str
    fields: tuple


@dataclass(frozen=True)
class FilterCase(BaseCase):
    page_key: str
    method_name: str
    value: str


@dataclass(frozen=True)
class ColumnCase(BaseCase):
    columns: tuple


@dataclass(frozen=True)
class MenuGroupCase(BaseCase):
    menu_name: str
    links: tuple