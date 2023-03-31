import pytest
from viewing_party.movie import Movie

def test_create_movie():
    # Arrange/Act
    finding_nemo = Movie("Finding Nemo", "Kids Movie", 5)

    # Assert
    assert isinstance(finding_nemo, Movie)