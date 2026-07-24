from __future__ import annotations

from safaribookmarks.models import WebBookmarkType, WebBookmarkTypeLeaf, WebBookmarkTypeList


def test_leaf_title_maps_to_safari_uri_dictionary() -> None:
    leaf = WebBookmarkTypeLeaf(URLString="https://example.com")

    leaf.title = "Example"

    assert leaf.title == "Example"
    assert leaf.uri_dictionary == {"title": "Example"}


def test_list_children_keep_mixed_safari_types() -> None:
    folder = WebBookmarkTypeList(
        Title="Folder",
        Children=[WebBookmarkTypeLeaf(URLString="https://example.com")],
    )
    child = WebBookmarkTypeLeaf(URLString="https://python.org")

    folder.insert(0, child)
    folder.remove(child)

    item = WebBookmarkType()
    assert hash(item) == hash(item.web_bookmark_uuid)
    assert len(folder.children) == 1
    assert isinstance(folder.children[0], WebBookmarkTypeLeaf)
    assert folder.children[0].url_string == "https://example.com"
