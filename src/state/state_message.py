from pydantic import BaseModel, Field
from typing import Literal

class Section(BaseModel):
    name: str = Field(
        description="name of section",
    )
    description: str = Field(
        description="description of section",
    )
    research: bool = Field(
        description="this section is for web research or not", 
    )

class Sections(BaseModel):
    sections: list[Section] = Field(
        description="list of sections",
    )

class ReportState(BaseModel):
    topic: str = Field(
        description="topic of report",
    )

class FeedbackUser(BaseModel):
    result: Literal['pass', 'fail'] = Field(
        description="feedback result of user",
    )

class Query(BaseModel):
    query: str = Field(
        description="query for search web",
    )
class Queries(BaseModel):
    queries: list[Query] = Field(
        description="list of queries",
    )