from .bookmarks import SafariBookmarkItem, SafariBookmarks

open = SafariBookmarks.open  # noqa: A001,RUF067

__all__ = ["SafariBookmarkItem", "SafariBookmarks", "open"]
