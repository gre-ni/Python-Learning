import pytest
from youtube_embed import parse_youtube

def test_shortlink():
    assert parse_youtube('<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>') == "https://youtu.be/xvFZjo5PgG0"

def test_longlink():
    assert parse_youtube('<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>') == "https://youtu.be/xvFZjo5PgG0"
    
def test_invalidsite():
    assert not parse_youtube('<iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>')