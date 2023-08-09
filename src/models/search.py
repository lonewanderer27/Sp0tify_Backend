# generated by datamodel-codegen:
#   filename:  search_all.json
#   timestamp: 2023-08-09T02:43:00+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class Range(BaseModel):
    start: int
    end: int


class Highlight(BaseModel):
    property: str
    value: str
    snippet: bool
    ranges: List[Range]


class ReleaseDateComponent(BaseModel):
    year: int
    month: int
    day: int


class Stats(BaseModel):
    unreviewed_annotations: int
    concurrents: Optional[int] = None
    hot: bool
    pageviews: int


class PrimaryArtist(BaseModel):
    field_type: str = Field(..., alias='_type')
    api_path: str
    header_image_url: str
    id: int
    image_url: str
    index_character: str
    is_meme_verified: bool
    is_verified: bool
    name: str
    slug: str
    url: str
    iq: Optional[int] = None


class Artist(BaseModel):
    field_type: str = Field(..., alias='_type')
    api_path: str
    header_image_url: str
    id: int
    image_url: str
    index_character: str
    is_meme_verified: bool
    is_verified: bool
    name: str
    slug: str
    url: str
    iq: Optional[int] = None


class DfpKvItem(BaseModel):
    name: str
    values: List[str]


class PosterAttributes(BaseModel):
    height: int
    width: int


class ProviderParam(BaseModel):
    name: str
    value: str


class VideoAttributes(BaseModel):
    width: int
    height: int


class Interactions(BaseModel):
    following: bool


class CurrentUserMetadata(BaseModel):
    permissions: List
    excluded_permissions: List[str]
    interactions: Optional[Interactions] = None


class BoundingBox(BaseModel):
    width: int
    height: int


class Tiny(BaseModel):
    url: str
    bounding_box: BoundingBox


class Thumb(BaseModel):
    url: str
    bounding_box: BoundingBox


class Small(BaseModel):
    url: str
    bounding_box: BoundingBox


class Medium(BaseModel):
    url: str
    bounding_box: BoundingBox


class Avatar(BaseModel):
    tiny: Tiny
    thumb: Thumb
    small: Small
    medium: Medium


class CurrentUserMetadata1(BaseModel):
    permissions: List
    excluded_permissions: List[str]
    interactions: Interactions


class Author(BaseModel):
    field_type: str = Field(..., alias='_type')
    about_me_summary: str
    api_path: str
    avatar: Avatar
    header_image_url: str
    human_readable_role_for_display: str
    id: int
    iq: int
    is_meme_verified: bool
    is_verified: bool
    login: str
    name: str
    role_for_display: str
    url: str
    current_user_metadata: CurrentUserMetadata1


class Sponsorship(BaseModel):
    field_type: str = Field(..., alias='_type')
    api_path: str
    sponsor_image: Optional[str] = None
    sponsor_image_style: str
    sponsor_link: Optional[str] = None
    sponsor_phrase: Optional[str] = None
    sponsored: bool


class Tiny1(BaseModel):
    url: str
    bounding_box: BoundingBox


class Thumb1(BaseModel):
    url: str
    bounding_box: BoundingBox


class Small1(BaseModel):
    url: str
    bounding_box: BoundingBox


class Medium1(BaseModel):
    url: str
    bounding_box: BoundingBox


class Avatar1(BaseModel):
    tiny: Tiny1
    thumb: Thumb1
    small: Small1
    medium: Medium1


class Result(BaseModel):
    field_type: str = Field(..., alias='_type')
    annotation_count: Optional[int] = None
    api_path: str
    artist_names: Optional[str] = None
    full_title: Optional[str] = None
    header_image_thumbnail_url: Optional[str] = None
    header_image_url: Optional[str] = None
    id: int
    instrumental: Optional[bool] = None
    lyrics_owner_id: Optional[int] = None
    lyrics_state: Optional[str] = None
    lyrics_updated_at: Optional[int] = None
    path: Optional[str] = None
    pyongs_count: Optional[int] = None
    relationships_index_url: Optional[str] = None
    release_date_components: Optional[ReleaseDateComponent] = None
    release_date_for_display: Optional[str] = None
    release_date_with_abbreviated_month_for_display: Optional[str] = None
    song_art_image_thumbnail_url: Optional[str] = None
    song_art_image_url: Optional[str] = None
    stats: Optional[Stats] = None
    title: Optional[str] = None
    title_with_featured: Optional[str] = None
    updated_by_human_at: Optional[int] = None
    url: str
    featured_artists: Optional[List] = None
    primary_artist: Optional[PrimaryArtist] = None
    image_url: Optional[str] = None
    index_character: Optional[str] = None
    is_meme_verified: Optional[bool] = None
    is_verified: Optional[bool] = None
    name: Optional[str] = None
    slug: Optional[str] = None
    cover_art_thumbnail_url: Optional[str] = None
    cover_art_url: Optional[str] = None
    name_with_artist: Optional[str] = None
    artist: Optional[Artist] = None
    article_url: Optional[str] = None
    author_list_for_display: Optional[str] = None
    dek: Optional[str] = None
    description: Optional[str] = None
    dfp_kv: Optional[List[DfpKvItem]] = None
    duration: Optional[int] = None
    poster_attributes: Optional[PosterAttributes] = None
    poster_url: Optional[str] = None
    provider: Optional[str] = None
    provider_id: Optional[str] = None
    provider_params: Optional[List[ProviderParam]] = None
    short_title: Optional[str] = None
    type: Optional[str] = None
    video_attributes: Optional[VideoAttributes] = None
    current_user_metadata: Optional[CurrentUserMetadata] = None
    published_at: Optional[int] = None
    view_count: Optional[int] = None
    author: Optional[Author] = None
    sponsorship: Optional[Sponsorship] = None
    article_type: Optional[str] = None
    draft: Optional[bool] = None
    featured_slot: None = None
    for_homepage: Optional[bool] = None
    for_mobile: Optional[bool] = None
    generic_sponsorship: Optional[bool] = None
    preview_image: Optional[str] = None
    sponsor_image: None = None
    sponsor_image_style: Optional[str] = None
    sponsor_link: Optional[str] = None
    sponsor_phrase: Optional[str] = None
    sponsored: Optional[bool] = None
    votes_total: Optional[int] = None
    about_me_summary: Optional[str] = None
    avatar: Optional[Avatar1] = None
    human_readable_role_for_display: Optional[str] = None
    iq: Optional[int] = None
    login: Optional[str] = None
    role_for_display: Optional[str] = None


class Hit(BaseModel):
    highlights: List[Highlight]
    index: str
    type: str
    result: Result


class Section(BaseModel):
    type: str
    hits: List[Hit]


class Search(BaseModel):
    sections: List[Section]
