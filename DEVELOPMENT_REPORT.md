# AniWatch Downloader Development Report

## Session Summary

**Date:** March 14, 2026  
**Project:** HiAnime Downloader → AniWatch Downloader (Rebranding)  
**Repository:** https://github.com/SawyerTheNerd/AniWatchDownloader  
**Status:** Completed

---

## Changes Made

### 1. Rebranding Changes

| File | Change |
|------|--------|
| `main.pyw` | App name: "HiAnime Downloader" → "AniWatch Downloader" |
| `gui/ui_main_window.py` | Window title updated, URL placeholder changed |
| `gui/ui_about_dialog.py` | Dialog title, app name, repo URL updated |
| `gui/about_dialog.py` | Repo URL changed to SawyerTheNerd/AniWatchDownloader |
| `gui/main_window.py` | Context menu: "View on HiAnime" → "View on AniWatch" |
| `gui/settings_dialog.py` | Download folder name updated |
| `pyproject.toml` | Project name: "hianimedownloader" → "aniwatch-downloader" |
| `README.md` | Complete rewrite with AniWatch branding |

### 2. URL Changes

| File | Change |
|------|--------|
| `downloader/anime_service.py` | `DEFAULT_BASE_URL = "https://aniwatchtv.to"` |
| `gui/ui_main_window.py` | Placeholder text updated |
| `gui/ui_settings_dialog.py` | Placeholder text updated |

### 3. yt-dlp Plugin Fixes

**File:** `yt_dlp_plugins/extractor/hianime.py`

| Issue | Fix |
|-------|-----|
| URL pattern only matched hianime.to | Added aniwatchtv.to to regex pattern |
| Server provider names wrong | Changed from ["HD-1", "HD-2", "HD-3"] to ["MegaCloud", "VidSrc", "HD-1", "HD-2", "HD-3"] |
| Variable name error | Fixed `mirror` → `provider_name` in error messages |

**Root Cause:** The site structure on aniwatchtv.to uses different server provider names (MegaCloud, VidSrc) instead of the expected "HD-1", "HD-2", "HD-3" labels.

### 4. Test Suite Created

**New Files:**
- `tests/test_search.py` - 8 tests for search HTML parsing
- `tests/test_download_integration.py` - 19 tests for download functionality

**Test Results:** 22-24 tests passing (depending on network availability)

**Test Coverage:**
- URL pattern matching (aniwatchtv.to, hianime.to, hianimez.to)
- Search result HTML parsing
- Episode extraction
- yt-dlp plugin integration
- AnimeService functionality
- Filename sanitization
- Language parameter handling

### 5. Executable Build

**Tool:** PyInstaller  
**Command:**
```bash
pyinstaller --onefile --windowed --name "AniWatchDownloader" --add-data "yt_dlp_plugins;yt_dlp_plugins" main.pyw
```

**Output:**
- File: `dist/AniWatchDownloader.exe`
- Size: 58.4 MB
- Type: Single-file standalone executable

---

## Technical Issues Encountered

### Issue 1: Search Not Working on aniwatchtv.to
**Problem:** Search returned 0 results  
**Cause:** URL regex pattern `/watch/` didn't match aniwatchtv.to's URL structure  
**Fix:** Updated regex to `/[^"]+` and added URL normalization

### Issue 2: Download Failed - "No video formats found"
**Problem:** yt-dlp extractor couldn't find video formats  
**Cause:** Extractor looked for mirror names "HD-1", "HD-2", "HD-3" but site uses "MegaCloud", "VidSrc"  
**Fix:** Updated `server_provider_names` array to include actual provider names

### Issue 3: GitHub Push Failed - Large File
**Problem:** `ffmpeg.exe` (190MB) exceeded GitHub's 100MB limit  
**Fix:** Removed ffmpeg.exe from git tracking, added to .gitignore

### Issue 4: PyInstaller Build Failed
**Problem:** Obsolete `typing` package incompatible with PyInstaller  
**Fix:** Uninstalled typing package (`pip uninstall typing`)

---

## Files Modified (Complete List)

1. `main.pyw`
2. `downloader/anime_service.py`
3. `gui/main_window.py`
4. `gui/ui_main_window.py`
5. `gui/ui_about_dialog.py`
6. `gui/about_dialog.py`
7. `gui/settings_dialog.py`
8. `gui/ui_settings_dialog.py`
9. `yt_dlp_plugins/extractor/hianime.py`
10. `pyproject.toml`
11. `README.md`
12. `.gitignore`

**Files Created:**
13. `tests/test_search.py`
14. `tests/test_download_integration.py`

---

## Current State

| Item | Status |
|------|--------|
| Git Commit | Latest - Rebranding complete |
| Default URL | `https://aniwatchtv.to` |
| App Name | "AniWatch Downloader" |
| Repository | https://github.com/SawyerTheNerd/AniWatchDownloader |
| Tests | 22-24 tests passing |
| Executable | Built successfully (58.4 MB) |
| GitHub | Pushed and up to date |

---

## Recommendations for Future Enhancements

1. **Add More Tests:** Expand test coverage for edge cases
2. **Auto-Update Feature:** Add automatic update checking
3. **Download Queue:** Support for queuing multiple anime downloads
4. **Dark Mode:** Add theme switching support
5. **Proxy Support:** Add proxy configuration for region-restricted content

---

## Credits

Original Project: **HiAnime Downloader** by Pratik Patel  
Repository: https://github.com/pratikpatel8982/HiAnimeDownloader  
License: MIT

---

**Report Generated:** March 14, 2026  
**Status:** Completed successfully
