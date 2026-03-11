# Mobile App Test Cases
**Generated:** 2026-03-11
**App:** CraveMode AI (React Native + Expo)

---

## 🧪 TEST SUITE 1: Performance Optimizations

### TC-001: Video Memory Management
**Objective:** Verify videos unload when off-screen
**Steps:**
1. Open Explore screen
2. Scroll through 10+ video cards
3. Monitor memory usage (should stay ~400MB)
4. Scroll back up
5. Play a video, then scroll away
**Expected:** Video stops and unloads when scrolled off-screen
**Priority:** CRITICAL

### TC-002: React.memo Optimization
**Objective:** Verify components don't re-render unnecessarily
**Steps:**
1. Open Explore screen
2. Change category filter
3. Monitor component renders in DevTools
**Expected:** Only new category videos render, existing ones stay mounted
**Priority:** HIGH

### TC-003: FlatList Windowing
**Objective:** Verify only visible items render
**Steps:**
1. Open Explore screen (20+ videos)
2. Monitor rendered components
3. Scroll down slowly
**Expected:** Initially 4 items, adds 2 at a time while scrolling
**Priority:** HIGH

### TC-004: Animation Performance
**Objective:** Verify smooth 60 FPS scrolling
**Steps:**
1. Open Explore screen
2. Scroll up/down rapidly
3. Monitor FPS in DevTools
**Expected:** Consistent 55-60 FPS, no jank
**Priority:** HIGH

### TC-005: API Polling Optimization
**Objective:** Verify 5-second polling interval
**Steps:**
1. Start video generation
2. Monitor network requests
3. Count requests over 30 seconds
**Expected:** 6 requests in 30 seconds (every 5s)
**Priority:** MEDIUM

---

## 🧪 TEST SUITE 2: Core Functionality

### TC-101: User Authentication
**Steps:**
1. Launch app (logged out)
2. Navigate to Sign In
3. Enter valid credentials
4. Submit
**Expected:** Redirects to Enhance screen, shows user data
**Priority:** CRITICAL

### TC-102: Photo Upload
**Steps:**
1. Navigate to Enhance screen
2. Tap "Upload Photos"
3. Select 3 photos from gallery
4. Verify preview thumbnails
**Expected:** Shows 3 thumbnails with remove buttons
**Priority:** CRITICAL

### TC-103: Image Enhancement Generation
**Steps:**
1. Upload 2 photos
2. Select style "Bright & Fresh"
3. Select format "Instagram Square (1:1)"
4. Tap "Generate"
**Expected:** Shows processing state, redirects to gallery on complete
**Priority:** CRITICAL

### TC-104: Video Generation
**Steps:**
1. Navigate to Video screen
2. Upload 1 photo
3. Select "Slow Zoom" motion
4. Select "10s" duration
5. Select "9:16" aspect ratio
6. Tap "Generate"
**Expected:** Shows progress ring, redirects to gallery on complete
**Priority:** CRITICAL

### TC-105: Gallery Filtering
**Steps:**
1. Navigate to Gallery
2. Generate 2 photos + 1 video
3. Tap "Videos" filter
**Expected:** Shows only the video, hides photos
**Priority:** HIGH

### TC-106: Gallery Bulk Delete
**Steps:**
1. Navigate to Gallery
2. Tap select mode button
3. Select 3 items
4. Tap "Delete"
5. Confirm
**Expected:** Shows confirmation, deletes 3 items, exits select mode
**Priority:** HIGH

### TC-107: Gallery Download
**Steps:**
1. Navigate to Gallery
2. Tap item
3. Tap "Save" button
**Expected:** Shows share sheet, can save to camera roll
**Priority:** MEDIUM

### TC-108: Queue Monitoring
**Steps:**
1. Start 2 generations (1 image, 1 video)
2. Navigate to Queue screen
**Expected:** Shows both jobs with progress/status
**Priority:** MEDIUM

### TC-109: Settings Profile Update
**Steps:**
1. Navigate to Settings
2. Update display name
3. Save changes
**Expected:** Shows success toast, name updates everywhere
**Priority:** MEDIUM

### TC-110: Usage Stats Display
**Steps:**
1. Generate 2 photos
2. Check usage meter in nav
**Expected:** Shows updated count (e.g., "2/50 photos used")
**Priority:** HIGH

---

## 🧪 TEST SUITE 3: Edge Cases & Error Handling

### TC-201: Upload Limit Exceeded
**Steps:**
1. Use account with 0 credits
2. Try to upload photo
3. Tap "Generate"
**Expected:** Shows error toast "Insufficient credits"
**Priority:** HIGH

### TC-202: Network Offline - Upload
**Steps:**
1. Turn on Airplane mode
2. Upload photo
3. Tap "Generate"
**Expected:** Shows error "No internet connection"
**Priority:** HIGH

### TC-203: Network Offline - Gallery Load
**Steps:**
1. Turn on Airplane mode
2. Navigate to Gallery
**Expected:** Shows cached items OR "No connection" message
**Priority:** MEDIUM

### TC-204: Large File Upload
**Steps:**
1. Upload 10MB+ image
2. Attempt generation
**Expected:** Shows "File too large" error OR uploads successfully
**Priority:** MEDIUM

### TC-205: Corrupted Image Upload
**Steps:**
1. Upload non-image file (PDF/DOC)
2. Attempt generation
**Expected:** Shows "Invalid file type" error
**Priority:** MEDIUM

### TC-206: Generation Failure
**Steps:**
1. Simulate API error (mock)
2. Start generation
**Expected:** Shows error toast, doesn't leave broken state
**Priority:** HIGH

### TC-207: Cancel Active Generation
**Steps:**
1. Start video generation (10s)
2. Immediately tap "Cancel"
**Expected:** Stops polling, resets UI, shows cancelled state
**Priority:** MEDIUM

### TC-208: App Backgrounding During Generation
**Steps:**
1. Start video generation
2. Press home button (background app)
3. Wait 30 seconds
4. Return to app
**Expected:** Resumes polling OR shows completion/failure
**Priority:** MEDIUM

### TC-209: Multiple Rapid Tab Switches
**Steps:**
1. Rapidly tap: Enhance → Video → Gallery → Queue → Settings (5x)
**Expected:** No crashes, smooth transitions
**Priority:** HIGH

### TC-210: Scroll to Bottom - Pagination
**Steps:**
1. Navigate to Gallery (50+ items)
2. Scroll to bottom
**Expected:** Loads next page automatically
**Priority:** MEDIUM

---

## 🧪 TEST SUITE 4: UI/UX Validation

### TC-301: Explore Page Layout
**Steps:**
1. Open Explore screen
2. Verify all sections render:
   - Header with icon
   - Featured Showcase (horizontal scroll)
   - Before/After section
   - Category tabs
   - Video grid (2 columns)
**Expected:** All sections visible, proper spacing
**Priority:** HIGH

### TC-302: Video Card Interactions
**Steps:**
1. Open Explore screen
2. Tap video thumbnail
**Expected:** Video plays inline, shows play/pause button
**Priority:** HIGH

### TC-303: Before/After Card Flip
**Steps:**
1. Navigate to Explore
2. Tap Before/After card
**Expected:** Flips to show "after" photo
**Priority:** MEDIUM

### TC-304: Category Filter
**Steps:**
1. Navigate to Explore
2. Tap "Pizza & Italian" category
**Expected:** Shows only pizza/italian videos in grid
**Priority:** HIGH

### TC-305: Cost Preview Display
**Steps:**
1. Navigate to Enhance screen
2. Select 5 photos
3. Select 3 variations
**Expected:** Shows "15 photos • X credits" at bottom
**Priority:** HIGH

### TC-306: Empty States
**Steps:**
1. Navigate to Gallery (empty account)
**Expected:** Shows empty state with icon + message
**Priority:** MEDIUM

### TC-307: Loading Skeletons
**Steps:**
1. Navigate to Gallery
2. Pull to refresh
**Expected:** Shows skeleton loading states during fetch
**Priority:** LOW

### TC-308: Toast Notifications
**Steps:**
1. Complete any generation
**Expected:** Shows success toast "Photos generated!"
**Priority:** MEDIUM

### TC-309: Haptic Feedback
**Steps:**
1. Tap various buttons
2. Switch tabs
3. Toggle filters
**Expected:** Subtle vibration on each interaction
**Priority:** LOW

### TC-310: Dark Theme Consistency
**Steps:**
1. Navigate through all screens
2. Check colors, contrast, readability
**Expected:** All screens use consistent dark theme
**Priority:** MEDIUM

---

## 🧪 TEST SUITE 5: Cross-Platform Compatibility

### TC-401: iOS - Basic Flow
**Platform:** iOS 14+
**Steps:** Complete TC-103 (Image Enhancement)
**Expected:** Works identically to Android
**Priority:** CRITICAL

### TC-402: Android - Basic Flow
**Platform:** Android 10+
**Steps:** Complete TC-103 (Image Enhancement)
**Expected:** Works identically to iOS
**Priority:** CRITICAL

### TC-403: iOS - Video Playback
**Platform:** iOS
**Steps:** Play 3 videos in Explore screen
**Expected:** Videos play smoothly, audio muted
**Priority:** HIGH

### TC-404: Android - Video Playback
**Platform:** Android
**Steps:** Play 3 videos in Explore screen
**Expected:** Videos play smoothly, audio muted
**Priority:** HIGH

### TC-405: iOS - Image Picker
**Platform:** iOS
**Steps:** Upload photos from gallery
**Expected:** Shows iOS native picker, respects permissions
**Priority:** HIGH

### TC-406: Android - Image Picker
**Platform:** Android
**Steps:** Upload photos from gallery
**Expected:** Shows Android native picker, respects permissions
**Priority:** HIGH

### TC-407: Small Screen (iPhone SE)
**Device:** 4.7" screen
**Steps:** Navigate through all screens
**Expected:** All content visible, no overflow
**Priority:** MEDIUM

### TC-408: Large Screen (iPad)
**Device:** 12.9" screen
**Steps:** Navigate through all screens
**Expected:** Layout scales appropriately
**Priority:** LOW

---

## 🧪 TEST SUITE 6: Memory & Performance

### TC-501: Memory Leak - Long Session
**Steps:**
1. Use app for 10 minutes
2. Navigate through all screens 5x
3. Generate 10 items
4. Monitor memory usage
**Expected:** Memory stays < 500MB, no leaks
**Priority:** CRITICAL

### TC-502: Battery Drain - Active Generation
**Steps:**
1. Start 3 video generations
2. Monitor battery drain over 10 minutes
**Expected:** Reasonable battery usage (< 10%)
**Priority:** MEDIUM

### TC-503: App Launch Time
**Steps:**
1. Kill app completely
2. Relaunch
3. Time until interactive
**Expected:** < 2 seconds to interactive
**Priority:** HIGH

### TC-504: Network Data Usage
**Steps:**
1. Reset network stats
2. Use app for 10 minutes
3. Check data usage
**Expected:** Reasonable usage (< 50MB)
**Priority:** LOW

### TC-505: Rapid Scroll Stress Test
**Steps:**
1. Navigate to Gallery (50+ items)
2. Scroll up/down rapidly for 30 seconds
**Expected:** No crashes, smooth scrolling
**Priority:** HIGH

---

## 🧪 TEST SUITE 7: Regression Tests (Post-Optimization)

### TC-601: Video Component Mount/Unmount
**Objective:** Verify memo optimization doesn't break video playback
**Steps:**
1. Open Explore screen
2. Tap to play video
3. Scroll away
4. Scroll back
5. Tap to play again
**Expected:** Video plays both times, no errors
**Priority:** CRITICAL

### TC-602: FlatList Scroll Stability
**Objective:** Verify windowing doesn't cause scroll jumps
**Steps:**
1. Open Gallery (20+ items)
2. Scroll down to item 15
3. Scroll back up to item 5
4. Scroll down again to item 15
**Expected:** Smooth scroll, no jumps or resets
**Priority:** HIGH

### TC-603: Category Filter After Optimization
**Objective:** Verify memo doesn't break filtering
**Steps:**
1. Open Explore screen
2. Select "Pizza & Italian"
3. Wait for grid to update
4. Select "All"
**Expected:** Grid updates correctly both times
**Priority:** HIGH

### TC-604: API Polling During Background
**Objective:** Verify 5s polling doesn't break on app background
**Steps:**
1. Start video generation
2. Background app
3. Wait 15 seconds
4. Foreground app
**Expected:** Polling resumes, shows current progress
**Priority:** MEDIUM

### TC-605: RemoveClippedSubviews Side Effects
**Objective:** Verify off-screen unmount doesn't break interactions
**Steps:**
1. Open Gallery (30+ items)
2. Scroll to item 20
3. Scroll back to item 5
4. Tap item 5 to view
**Expected:** Item 5 still interactive, no errors
**Priority:** HIGH

---

## 📊 TEST EXECUTION CHECKLIST

### Pre-Test Setup
- [ ] Clean install app on device
- [ ] Clear app data & cache
- [ ] Verify test account has credits
- [ ] Enable React DevTools for profiling
- [ ] Prepare test images (5x JPG, various sizes)

### Critical Path Tests (Must Pass)
- [ ] TC-101: Authentication
- [ ] TC-103: Image Enhancement
- [ ] TC-104: Video Generation
- [ ] TC-201: Upload Limit Error
- [ ] TC-209: Rapid Tab Switches
- [ ] TC-501: Memory Leak Test
- [ ] TC-601: Video Mount/Unmount Regression

### Performance Validation (Post-Optimization)
- [ ] TC-001: Video Memory < 400MB
- [ ] TC-003: FlatList renders 4-6 items initially
- [ ] TC-004: Scroll FPS 55-60
- [ ] TC-005: API polling every 5s

### Platform Coverage
- [ ] iOS: TC-401, TC-403, TC-405
- [ ] Android: TC-402, TC-404, TC-406

---

## 🐛 BUG REPORT TEMPLATE

```
**Test Case:** TC-XXX
**Severity:** Critical / High / Medium / Low
**Platform:** iOS / Android / Both
**Device:** iPhone 14 / Pixel 7
**OS Version:** iOS 16.5 / Android 13

**Steps to Reproduce:**
1. ...
2. ...

**Expected Result:**
...

**Actual Result:**
...

**Screenshots/Video:**
[Attach]

**Console Logs:**
[Attach]
```

---

**Total Test Cases:** 67
**Estimated Execution Time:** 3-4 hours (manual)
**Critical Tests:** 15
**High Priority Tests:** 28
