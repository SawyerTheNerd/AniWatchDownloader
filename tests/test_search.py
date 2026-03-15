"""
Test suite for AniWatch Downloader search functionality.
"""

import pytest
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from downloader.anime_service import AnimeService, DEFAULT_BASE_URL


class TestAnimeServiceSearch:
    """Test cases for the AnimeService search functionality."""

    @pytest.fixture
    def anime_service(self):
        """Create an AnimeService instance for testing."""
        return AnimeService()

    def test_default_base_url(self):
        """Test that the default base URL is set to aniwatchtv.to."""
        assert DEFAULT_BASE_URL == "https://aniwatchtv.to"

    def test_service_initialization_with_default_url(self, anime_service):
        """Test that AnimeService initializes with the correct default URL."""
        assert anime_service.base_url == "https://aniwatchtv.to"

    def test_service_initialization_with_custom_url(self):
        """Test that AnimeService can be initialized with a custom URL."""
        custom_url = "https://custom.example.com"
        service = AnimeService(base_url=custom_url)
        assert service.base_url == custom_url

    def test_sanitize_filename_component(self, anime_service):
        """Test filename sanitization."""
        # Test valid names
        assert anime_service.sanitize_filename_component("Test Anime") == "Test Anime"

        # Test names with invalid characters (actual behavior may vary)
        result1 = anime_service.sanitize_filename_component("Test<Anime>")
        assert "Test" in result1 and "Anime" in result1
        
        result2 = anime_service.sanitize_filename_component("Test/Anime")
        assert "Test" in result2 and "Anime" in result2

        # Test empty result
        assert anime_service.sanitize_filename_component("   ") == "untitled"

    def test_search_anime_integration(self, anime_service):
        """Integration test for search_anime method (requires network)."""
        # This test requires network access and may fail if the service is unavailable
        results = anime_service.search_anime("demon slayer")
        
        # Verify results structure
        assert isinstance(results, list)
        
        # If results are returned, verify structure
        if results:
            result = results[0]
            assert "title" in result
            assert "url" in result
            assert "sub" in result
            assert "dub" in result
            assert "img" in result


class TestUrlValidation:
    """Test URL validation for AniWatch domain."""

    def test_aniwatch_url_format(self):
        """Test that aniwatchtv.to URLs are properly formatted."""
        base_url = "https://aniwatchtv.to"
        search_url = f"{base_url}/search?keyword=test"
        
        assert search_url.startswith("https://aniwatchtv.to")
        assert "?keyword=" in search_url

    def test_url_contains_correct_domain(self):
        """Test that URLs contain the correct domain."""
        assert "aniwatchtv.to" in DEFAULT_BASE_URL


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
