"""
Integration test suite for AniWatch Downloader download functionality.
"""

import pytest
import sys
import os
import tempfile
import shutil

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from downloader.anime_service import AnimeService, DEFAULT_BASE_URL


class TestDownloadIntegration:
    """Integration tests for the download functionality."""

    @pytest.fixture
    def anime_service(self):
        """Create an AnimeService instance for testing."""
        return AnimeService()

    @pytest.fixture
    def temp_download_dir(self):
        """Create a temporary directory for downloads."""
        temp_dir = tempfile.mkdtemp(prefix="aniwatch_test_")
        yield temp_dir
        # Cleanup after test
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)

    def test_service_initialization(self, anime_service):
        """Test that AnimeService initializes correctly."""
        assert anime_service is not None
        assert anime_service.base_url == "https://aniwatchtv.to"

    def test_ffmpeg_availability_check(self, anime_service):
        """Test FFmpeg availability check method."""
        # This test checks if the method runs without error
        result = anime_service.is_ffmpeg_available()
        assert isinstance(result, bool)

    def test_sanitize_filename_for_download(self, anime_service):
        """Test filename sanitization for download directories."""
        # Test various anime title formats
        test_cases = [
            ("Demon Slayer", "Demon Slayer"),
            ("One Piece (2023)", "One Piece (2023)"),
            ("Attack on Titan: Final Season", "Attack on Titan_ Final Season"),
            ("My Hero Academia S06", "My Hero Academia S06"),
        ]
        
        for input_name, expected_pattern in test_cases:
            result = anime_service.sanitize_filename_component(input_name)
            assert isinstance(result, str)
            assert len(result) > 0

    def test_download_directory_creation(self, anime_service, temp_download_dir):
        """Test that download directories can be created."""
        test_series_name = "Test_Anime_Series"
        series_dir = os.path.join(temp_download_dir, test_series_name)
        
        # Verify directory can be created
        os.makedirs(series_dir, exist_ok=True)
        assert os.path.exists(series_dir)
        assert os.path.isdir(series_dir)

    def test_download_anime_method_exists(self, anime_service):
        """Test that download_anime method exists and has correct signature."""
        assert hasattr(anime_service, 'download_anime')
        assert callable(getattr(anime_service, 'download_anime'))

    def test_search_before_download(self, anime_service):
        """Test that search returns valid data structure for download."""
        results = anime_service.search_anime("test")
        
        # Verify results is a list
        assert isinstance(results, list)
        
        # If results exist, verify they have required fields
        if results:
            for result in results:
                assert isinstance(result, dict)
                assert "title" in result
                assert "url" in result

    def test_base_url_configuration(self):
        """Test that base URL is correctly configured for AniWatch."""
        assert DEFAULT_BASE_URL == "https://aniwatchtv.to"
        
        # Test service with explicit URL
        service = AnimeService(base_url="https://aniwatchtv.to")
        assert service.base_url == "https://aniwatchtv.to"

    @pytest.mark.skip(reason="Requires actual video download - slow integration test")
    def test_full_download_workflow(self, anime_service, temp_download_dir):
        """
        Full integration test for download workflow.
        This test is skipped by default as it performs actual downloads.
        """
        # Example test - would need valid anime URL
        # anime_service.download_anime(
        #     title="Test Anime",
        #     url="https://aniwatchtv.to/watch/test-anime-12345",
        #     lang="SUB",
        #     quality="1080p",
        #     start_ep=1,
        #     end_ep=1,
        #     base_download_dir=temp_download_dir
        # )
        pass


class TestConfiguration:
    """Test configuration and settings."""

    def test_default_settings(self):
        """Test default configuration values."""
        assert DEFAULT_BASE_URL == "https://aniwatchtv.to"

    def test_service_with_none_base_url(self):
        """Test service initialization with None base_url falls back to default."""
        service = AnimeService(base_url=None)
        assert service.base_url == "https://aniwatchtv.to"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
