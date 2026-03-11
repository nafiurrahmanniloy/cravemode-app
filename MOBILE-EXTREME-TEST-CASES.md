# Mobile App - EXTREME EDGE CASE TEST SCENARIOS
**Date:** 2026-03-12
**Test Type:** Stress Testing, Edge Cases, Race Conditions, Memory Limits
**Difficulty:** MAXIMUM
**Purpose:** Break the app and find hidden bugs

---

## 🔥 EXTREME TEST CATEGORIES

### 1. Memory & Performance Torture Tests
### 2. Race Conditions & Timing Attacks
### 3. Data Corruption & Invalid States
### 4. Network Chaos Engineering
### 5. Auth & Security Edge Cases
### 6. UI/UX Breaking Points
### 7. State Management Corruption
### 8. File System Chaos

---

## 1. MEMORY & PERFORMANCE TORTURE TESTS

### Test E1.1: Video Memory Bomb
**Severity:** CRITICAL
**Steps:**
1. Navigate to Explore screen
2. Rapidly scroll down and up through ALL videos (6 showcase + 20 category)
3. Play and pause videos in rapid succession (tap 20 times in 5 seconds)
4. Monitor memory usage

**Expected Failure Points:**
- Videos not unloading fast enough
- Memory leak from rapid mount/unmount
- App crashes at ~2GB RAM

**Pass Criteria:**
- Memory stays under 500MB
- No crashes after 50+ rapid taps
- Videos unload properly when off-screen

---

### Test E1.2: FlatList Infinite Scroll Bomb
**Severity:** HIGH
**Steps:**
1. Go to Gallery with 500+ items
2. Scroll to bottom as fast as possible
3. Scroll back to top
4. Repeat 10 times

**Expected Failure Points:**
- useInfiniteQuery loads all pages into memory
- FlatList doesn't unmount off-screen items
- Jank/frame drops during rapid scroll

**Pass Criteria:**
- Smooth 60 FPS scrolling
- Memory doesn't grow unbounded
- No white screens or crashes

---

### Test E1.3: Simultaneous Large File Uploads
**Severity:** HIGH
**Steps:**
1. Select 10 photos (max allowed)
2. Each photo should be >5MB (near 10MB limit)
3. Generate with 4 variations each
4. Total: 40 API calls, ~500MB upload

**Expected Failure Points:**
- Out of memory during base64 encoding
- Network timeout
- Device freezes

**Pass Criteria:**
- Upload completes successfully
- Progress indicators update
- App remains responsive

---

## 2. RACE CONDITIONS & TIMING ATTACKS

### Test E2.1: Double-Tap Upload Button
**Severity:** CRITICAL
**Steps:**
1. Upload 1 photo
2. Configure settings
3. Tap "Enhance" button TWICE in rapid succession (<100ms)
4. Check if 2 API calls are made

**Expected Failure Points:**
- Duplicate uploads (charged twice)
- Race condition in mutation state
- Credits deducted twice

**Pass Criteria:**
- Only ONE upload happens
- Button disables immediately
- No duplicate charges

---

### Test E2.2: Auth State Race Condition
**Severity:** CRITICAL
**Steps:**
1. Sign in
2. Immediately (within 1 second) navigate to Enhance tab
3. Try to upload photo

**Expected Failure Points:**
- useUsageStats() returns null (auth not ready)
- Credit check fails
- 401 error from API

**Pass Criteria:**
- Usage stats load before allowing upload
- Graceful loading state
- No crashes

---

### Test E2.3: Tab Switch During API Call
**Severity:** MEDIUM
**Steps:**
1. Start video generation (2-4 min process)
2. Immediately switch to Gallery tab
3. Switch back to Video tab
4. Switch to Settings
5. Repeat tab switching 20 times

**Expected Failure Points:**
- useGenerationStatus polling breaks
- Memory leak from unmounted listeners
- Stale state updates

**Pass Criteria:**
- Polling continues in background
- Progress updates correctly
- No crashes or memory leaks

---

## 3. DATA CORRUPTION & INVALID STATES

### Test E3.1: Corrupted UsageStats Response
**Severity:** CRITICAL
**Simulated Backend Response:**
```json
{
  "credits": null,
  "photos": { "used": -5, "limit": 0 },
  "videos": { "used": 9999999, "limit": 10 },
  "plan": "invalid_plan",
  "renewalDate": "not a date"
}
```

**Expected Failure Points:**
- Division by zero in progress calculation
- Negative credits allow unlimited uploads
- UI shows NaN or Infinity

**Pass Criteria:**
- Graceful handling of null/invalid data
- Fallback to safe defaults
- Clear error message to user

---

### Test E3.2: Empty Gallery Page Response
**Severity:** MEDIUM
**Simulated API Response:**
```json
{
  "items": [],
  "nextPage": 999,
  "total": -1
}
```

**Expected Failure Points:**
- Infinite loading loop (nextPage exists but no items)
- UI shows "0 items" but loading spinner persists
- Negative total breaks UI

**Pass Criteria:**
- Shows empty state correctly
- No infinite loading
- Handles negative/invalid pagination

---

### Test E3.3: Malformed Generation Status
**Severity:** HIGH
**Simulated API Response:**
```json
{
  "id": "job123",
  "status": "unknown_status",
  "progress": 150,
  "eta": -10,
  "errorMessage": null
}
```

**Expected Failure Points:**
- Progress bar shows >100%
- Unknown status breaks polling logic
- Negative ETA causes crash

**Pass Criteria:**
- Clamps progress to 0-100
- Handles unknown status gracefully
- No crashes from invalid data

---

## 4. NETWORK CHAOS ENGINEERING

### Test E4.1: Intermittent Network (Flaky Connection)
**Severity:** HIGH
**Steps:**
1. Enable/disable airplane mode every 2 seconds
2. Try to upload photo
3. Try to load gallery
4. Try to generate video

**Expected Failure Points:**
- Retry logic enters infinite loop
- Cached data corrupts
- UI freezes waiting for network

**Pass Criteria:**
- Offline banner shows/hides correctly
- React Query retry works
- User can still view cached content

---

### Test E4.2: Slow 2G Network
**Severity:** MEDIUM
**Steps:**
1. Throttle network to 2G (50kb/s)
2. Upload 10MB photo
3. Navigate away during upload
4. Check if upload continues

**Expected Failure Points:**
- Upload timeout (default 30s)
- No progress indicator
- App freezes during upload

**Pass Criteria:**
- Upload completes (may take minutes)
- Progress indicator updates
- App remains responsive

---

### Test E4.3: API Returns 500 for ALL Requests
**Severity:** CRITICAL
**Steps:**
1. Mock all API endpoints to return 500 error
2. Try to sign in
3. Try to load usage stats
4. Try to upload photo

**Expected Failure Points:**
- Infinite retry loop
- App unusable
- No offline fallback

**Pass Criteria:**
- Retries max 3 times, then fails
- Clear error messages
- App doesn't crash

---

## 5. AUTH & SECURITY EDGE CASES

### Test E5.1: Expired Token Mid-Session
**Severity:** CRITICAL
**Steps:**
1. Sign in
2. Manually expire Supabase token (or wait 1 hour)
3. Try to upload photo
4. Try to view gallery

**Expected Failure Points:**
- 401 error with no redirect
- User stuck in limbo state
- Data loss (staged photos)

**Pass Criteria:**
- Auto-redirects to sign-in
- Saves staged work (if possible)
- Clear "session expired" message

---

### Test E5.2: Concurrent Sessions (2 Devices)
**Severity:** MEDIUM
**Steps:**
1. Sign in on Device A
2. Sign in on Device B (same account)
3. Upload photo on Device A
4. Check gallery on Device B

**Expected Failure Points:**
- Cache invalidation doesn't work across devices
- Credits deducted twice
- Data inconsistency

**Pass Criteria:**
- Both devices eventually sync
- React Query invalidation works
- No data corruption

---

### Test E5.3: Sign Out During Active Upload
**Severity:** HIGH
**Steps:**
1. Start uploading 10 photos
2. Immediately sign out (tap Sign Out button)
3. Check if upload continues or aborts

**Expected Failure Points:**
- Upload completes but credits charged to no one
- App crashes
- API calls with invalid auth

**Pass Criteria:**
- Upload cancels gracefully
- No zombie requests
- User redirected to sign-in

---

## 6. UI/UX BREAKING POINTS

### Test E6.1: Rapid Tab Switching (Seizure Test)
**Severity:** MEDIUM
**Steps:**
1. Tap between Enhance → Video → Explore → Gallery tabs as fast as possible
2. Do this for 60 seconds straight
3. Monitor FPS and crashes

**Expected Failure Points:**
- Memory leak from rapid mount/unmount
- Animation queue overflow
- App freeze or crash

**Pass Criteria:**
- No crashes after 60s
- FPS stays above 30
- All tabs load correctly

---

### Test E6.2: Super Long Restaurant Name
**Severity:** LOW
**Input:**
```
"The Most Amazing Delicious Incredible Fantastic Extraordinary Wonderful Beautiful Perfect Restaurant & Bar & Grill & Cafe & Bistro & Lounge & Pizzeria Located in Downtown Los Angeles California USA 90001"
```

**Expected Failure Points:**
- Text overflow breaks layout
- Database field length limit exceeded
- UI elements overlap

**Pass Criteria:**
- Text truncates with ellipsis
- No layout breaks
- Saves to DB correctly

---

### Test E6.3: Emoji Bomb in Input Fields
**Severity:** LOW
**Input:**
```
🔥🍕🍔🍟🌮🌯🥙🥗🍝🍜🍲🍱🍣🍤🍥🥟🍡🍧🍨🍩🍪🎂🍰🧁🥧🍫🍬🍭🍮🍯🍼🥛☕🍵🍶🍾🍷🍸🍹🍺🍻🥂🥃
```

**Expected Failure Points:**
- Text input crashes
- Database encoding issues (UTF-8)
- UI renders incorrectly

**Pass Criteria:**
- Emojis display correctly
- Saves and retrieves properly
- No encoding errors

---

## 7. STATE MANAGEMENT CORRUPTION

### Test E7.1: Zustand Store Persistence Corruption
**Severity:** HIGH
**Steps:**
1. Upload 5 photos (staged in upload store)
2. Force close app (kill process)
3. Reopen app
4. Check if staged photos persist or clear

**Expected Failure Points:**
- Staged photos persist with broken URIs
- App tries to upload invalid files
- Zustand hydration fails

**Pass Criteria:**
- Staged photos clear on app restart
- No broken state
- Fresh start each session

---

### Test E7.2: React Query Cache Poisoning
**Severity:** MEDIUM
**Steps:**
1. Load usage stats (cached for 30s)
2. Manually modify cache via DevTools
3. Set `credits.limit` to -999
4. Try to upload photo

**Expected Failure Points:**
- Negative limit allows infinite uploads
- UI breaks from invalid data
- Credit check bypassed

**Pass Criteria:**
- Validation on cache read
- Refetch if data invalid
- Safe fallbacks

---

## 8. FILE SYSTEM CHAOS

### Test E8.1: Photo Picker Returns Corrupted File
**Severity:** HIGH
**Steps:**
1. Mock ImagePicker to return:
```json
{
  "uri": "file:///path/to/nonexistent.jpg",
  "fileSize": 0,
  "mimeType": null
}
```
2. Try to upload

**Expected Failure Points:**
- File not found error
- Zero-byte file uploads
- Crash during file read

**Pass Criteria:**
- Validation before upload
- Clear error message
- No crash

---

### Test E8.2: Storage Permission Denied
**Severity:** MEDIUM
**Steps:**
1. Deny storage permission
2. Try to download gallery item
3. Try to share gallery item

**Expected Failure Points:**
- Silent failure (no error message)
- App crashes
- Permission prompt loop

**Pass Criteria:**
- Clear "Permission denied" message
- Prompt user to enable permission
- Graceful handling

---

## 🎯 EXECUTION PLAN

### Phase 1: Automated Code Analysis
- [ ] Read all screen files
- [ ] Check for race condition vulnerabilities
- [ ] Verify input validation
- [ ] Check error boundaries

### Phase 2: Manual Simulated Tests
- [ ] Test invalid API responses
- [ ] Test null/undefined states
- [ ] Test boundary values
- [ ] Test concurrent operations

### Phase 3: Critical Bug Triage
- [ ] CRITICAL: Must fix before launch
- [ ] HIGH: Should fix ASAP
- [ ] MEDIUM: Fix in next sprint
- [ ] LOW: Nice to have

---

**Total Extreme Test Cases:** 24
**Estimated Execution Time:** 3-4 hours (manual)
**Expected Bug Discovery Rate:** 30-50%

---

**Test Plan Created:** 2026-03-12
**Next Step:** Execute these tests and document all failures
