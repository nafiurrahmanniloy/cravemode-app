# CraveMode AI Mobile App - Test Plan
**Date:** 2026-03-12
**App Version:** 1.0.0
**Platform:** React Native (Expo)
**Test Environment:** iOS Simulator / Android Emulator / Physical Device

---

## Test Categories

### 1. Authentication & Onboarding
### 2. Navigation & UI/UX
### 3. Explore Screen
### 4. Enhance Screen (Photo Upload & Generation)
### 5. Video Screen (Video Generation)
### 6. Gallery Screen
### 7. Settings Screen
### 8. API Integration & Error Handling
### 9. Performance & Memory
### 10. Offline Behavior

---

## 1. AUTHENTICATION & ONBOARDING

### Test Case 1.1: First-Time App Launch
**Priority:** HIGH
**Steps:**
1. Fresh install the app
2. Launch the app for the first time
3. Observe loading/splash screen

**Expected:**
- Splash screen displays properly
- App redirects to Sign In screen
- No crashes or white screens

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

### Test Case 1.2: Sign Up with Valid Email
**Priority:** HIGH
**Steps:**
1. Navigate to Sign Up screen
2. Enter valid email (test@example.com)
3. Enter valid password (min 6 chars)
4. Tap "Sign Up"

**Expected:**
- Loading indicator shows during request
- Success: Redirect to main app (Enhance tab)
- User is authenticated
- No error messages

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

### Test Case 1.3: Sign Up with Invalid Email
**Priority:** MEDIUM
**Steps:**
1. Navigate to Sign Up screen
2. Enter invalid email (notanemail)
3. Tap "Sign Up"

**Expected:**
- Validation error shows
- "Please enter a valid email" message
- No API call made

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

### Test Case 1.4: Sign In with Correct Credentials
**Priority:** HIGH
**Steps:**
1. Navigate to Sign In screen
2. Enter registered email
3. Enter correct password
4. Tap "Sign In"

**Expected:**
- Loading indicator shows
- Redirect to main app (Enhance tab)
- User session persists

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

### Test Case 1.5: Sign In with Wrong Password
**Priority:** HIGH
**Steps:**
1. Navigate to Sign In screen
2. Enter registered email
3. Enter wrong password
4. Tap "Sign In"

**Expected:**
- Error message displays: "Invalid credentials"
- No redirect
- User remains on Sign In screen

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

### Test Case 1.6: Session Persistence
**Priority:** HIGH
**Steps:**
1. Sign in successfully
2. Close the app completely
3. Reopen the app

**Expected:**
- User remains signed in
- App opens directly to Enhance tab
- No re-authentication required

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

### Test Case 1.7: Sign Out
**Priority:** HIGH
**Steps:**
1. While signed in, go to Settings tab
2. Tap "Sign Out" button
3. Confirm sign out

**Expected:**
- User is logged out
- Redirect to Sign In screen
- Session cleared from storage

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

## 2. NAVIGATION & UI/UX

### Test Case 2.1: Tab Navigation - All Tabs
**Priority:** HIGH
**Steps:**
1. Tap each tab: Enhance → Video → Explore → Gallery → Settings
2. Verify each screen loads

**Expected:**
- Each tab switches instantly (<100ms)
- No white screens or loading delays
- Tab bar icons highlight correctly
- Previous screen unmounts properly

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

### Test Case 2.2: Tab Bar Visibility
**Priority:** MEDIUM
**Steps:**
1. Navigate to each screen
2. Check tab bar visibility

**Expected:**
- Tab bar visible on all main screens
- Tab bar does not overlap content
- Safe area insets respected

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

### Test Case 2.3: Back Navigation
**Priority:** MEDIUM
**Steps:**
1. Navigate through multiple screens
2. Use device back button (Android) or swipe gesture (iOS)

**Expected:**
- Back navigation works correctly
- No memory leaks from unmounted screens

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

## 3. EXPLORE SCREEN

### Test Case 3.1: Featured Videos Load
**Priority:** HIGH
**Steps:**
1. Navigate to Explore tab
2. Observe "Featured" horizontal scroll section

**Expected:**
- 6 showcase video cards display
- Thumbnails load properly
- Cards are scrollable horizontally
- No missing images

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

### Test Case 3.2: Video Playback - Showcase Card
**Priority:** HIGH
**Steps:**
1. Tap on a featured video card
2. Observe video playback
3. Tap again to pause

**Expected:**
- Video plays on first tap
- Play button hides when playing
- Video pauses on second tap
- Play button reappears
- No audio (muted)
- Video loops smoothly

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

### Test Case 3.3: Before/After Section
**Priority:** MEDIUM
**Steps:**
1. Scroll to "Before & After" section
2. Tap on a before/after card

**Expected:**
- Before/After cards display in horizontal scroll
- Tap switches between before/after images
- Smooth transition between states

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

### Test Case 3.4: Category Filter
**Priority:** HIGH
**Steps:**
1. Scroll to "Browse by Category" section
2. Tap different categories: All → Burgers → Pizza → Desserts

**Expected:**
- Category tabs highlight on selection
- Video grid updates to show filtered videos
- "All" shows all videos
- Specific categories show only matching videos

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

### Test Case 3.5: Video Grid Scrolling Performance
**Priority:** HIGH
**Steps:**
1. Select "All" category
2. Scroll through the 2-column video grid rapidly
3. Monitor FPS and smoothness

**Expected:**
- Smooth 60 FPS scrolling
- No lag or stuttering
- Videos load thumbnails progressively
- Off-screen videos unload (memory management)

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

### Test Case 3.6: Video Grid - Play/Pause
**Priority:** HIGH
**Steps:**
1. Tap a video card in the grid
2. Let it play for 3 seconds
3. Tap to pause

**Expected:**
- Video plays in card
- Play button disappears
- Video loops when finished
- Pause works correctly

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

### Test Case 3.7: Memory Management - Multiple Videos
**Priority:** HIGH
**Steps:**
1. Play a video in Featured section
2. Scroll down to category grid
3. Play a video in grid
4. Return to Featured section

**Expected:**
- Only one video plays at a time
- Previous video stops and unloads
- No memory leaks
- App memory stays under 500MB

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

## 4. ENHANCE SCREEN (Photo Upload & Generation)

### Test Case 4.1: Screen Layout & Usage Stats
**Priority:** HIGH
**Steps:**
1. Navigate to Enhance tab (index)
2. Observe screen layout

**Expected:**
- Usage stats card displays at top
- Credits, photos, videos usage shown
- Plan name visible (Starter/Growth/Pro)
- Renewal date shown

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

### Test Case 4.2: Upload Photo from Camera Roll
**Priority:** HIGH
**Steps:**
1. Tap "Upload Photo" or camera icon
2. Select "Choose from Library"
3. Pick a photo from camera roll

**Expected:**
- Image picker opens
- Selected photo displays as preview
- Photo thumbnail loads
- File size shown

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

### Test Case 4.3: Upload Photo from Camera
**Priority:** HIGH
**Steps:**
1. Tap "Upload Photo"
2. Select "Take Photo"
3. Take a new photo
4. Confirm selection

**Expected:**
- Camera opens
- Photo captures correctly
- Preview shows captured image
- Photo ready for upload

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

### Test Case 4.4: Select Style & Format
**Priority:** HIGH
**Steps:**
1. Upload a photo
2. Select style: Bright & Fresh / Dark & Moody / etc.
3. Select format: 9:16 / 1:1 / 16:9

**Expected:**
- Style options display as chips/buttons
- Selected style highlights
- Format options show aspect ratio preview
- Selections persist during session

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

### Test Case 4.5: Cost Preview
**Priority:** HIGH
**Steps:**
1. Upload photo
2. Select style and format
3. Choose number of variations (1-4)

**Expected:**
- Cost preview updates dynamically
- Credits cost shown based on plan tier
- "X credits per image" label
- Total credits displayed

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

### Test Case 4.6: Generate Image - Success
**Priority:** HIGH
**Steps:**
1. Upload photo
2. Configure style/format
3. Tap "Generate" button
4. Wait for completion

**Expected:**
- Loading indicator shows
- Progress bar or percentage displays
- Success message on completion
- Redirect to Gallery or Queue
- Credits deducted from account

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

### Test Case 4.7: Generate Image - Insufficient Credits
**Priority:** HIGH
**Steps:**
1. Upload photo
2. Configure generation that exceeds available credits
3. Tap "Generate"

**Expected:**
- Error message: "Insufficient credits"
- Prompt to upgrade plan or buy credits
- No generation starts
- No API call made

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

### Test Case 4.8: Upload Multiple Photos (Batch)
**Priority:** MEDIUM
**Steps:**
1. Tap "Upload Multiple" or select multiple from picker
2. Select 3-5 photos
3. Configure style/format for batch

**Expected:**
- All photos display as thumbnails
- Cost multiplies by number of photos
- Batch generation starts
- Each photo gets separate job in Queue

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

## 5. VIDEO SCREEN (Video Generation)

### Test Case 5.1: Screen Layout & Usage Stats
**Priority:** HIGH
**Steps:**
1. Navigate to Video tab
2. Observe screen layout

**Expected:**
- Usage stats card shows video credits
- "Videos used / limit" displayed
- Upload area visible

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

### Test Case 5.2: Upload Source Photo for Video
**Priority:** HIGH
**Steps:**
1. Tap "Upload Photo"
2. Select a food photo

**Expected:**
- Image picker opens
- Selected photo displays
- Photo is staged for video generation

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

### Test Case 5.3: Configure Video Settings
**Priority:** HIGH
**Steps:**
1. Upload photo
2. Select style
3. Select duration (5s / 10s / 15s)
4. Select aspect ratio (9:16 for Reels)

**Expected:**
- All configuration options display
- Selections update cost preview
- Duration affects credit cost

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

### Test Case 5.4: Generate Video - Success
**Priority:** HIGH
**Steps:**
1. Upload photo
2. Configure settings
3. Tap "Generate Video"
4. Wait for completion (2-4 minutes)

**Expected:**
- Loading indicator shows
- Estimated time displayed
- Progress updates periodically
- Success message on completion
- Video available in Gallery

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

### Test Case 5.5: Video Generation - Long Wait Time
**Priority:** MEDIUM
**Steps:**
1. Start video generation
2. Navigate to other tabs during generation
3. Return to Video tab after completion

**Expected:**
- Generation continues in background
- Status updates even when tab is inactive
- Notification shows when complete (if implemented)

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

## 6. GALLERY SCREEN

### Test Case 6.1: Gallery Loads with Items
**Priority:** HIGH
**Steps:**
1. Navigate to Gallery tab
2. Observe gallery grid

**Expected:**
- Gallery items display in grid (2 columns)
- Thumbnails load progressively
- Scroll is smooth
- All generated items visible

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

### Test Case 6.2: Filter Gallery Items
**Priority:** HIGH
**Steps:**
1. Tap filter dropdown
2. Select: All → Enhanced → Videos → Originals

**Expected:**
- Filter updates gallery content
- Only matching items show
- Filter selection persists during session

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

### Test Case 6.3: Sort Gallery Items
**Priority:** HIGH
**Steps:**
1. Tap sort dropdown
2. Select: Newest → Oldest

**Expected:**
- Gallery re-sorts items
- Newest shows most recent first
- Oldest shows oldest first

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

### Test Case 6.4: View Full Image/Video
**Priority:** HIGH
**Steps:**
1. Tap on a gallery item
2. View full-screen preview

**Expected:**
- Item opens in full screen
- Image shows at full resolution
- Video plays with controls
- Swipe to dismiss works

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

### Test Case 6.5: Download Item
**Priority:** HIGH
**Steps:**
1. Long-press on gallery item (or tap menu)
2. Tap "Download"

**Expected:**
- Download starts
- Progress indicator shows
- File saves to device
- Success message appears
- Item accessible in Photos app

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

### Test Case 6.6: Delete Item
**Priority:** HIGH
**Steps:**
1. Long-press on gallery item
2. Tap "Delete"
3. Confirm deletion

**Expected:**
- Confirmation dialog appears
- Item deletes on confirm
- Item removed from gallery
- Gallery updates immediately

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

### Test Case 6.7: Select Mode - Multiple Selection
**Priority:** MEDIUM
**Steps:**
1. Tap "Select" button
2. Tap 3-5 items to select
3. Tap "Download All" or "Delete All"

**Expected:**
- Select mode activates
- Checkboxes appear on items
- Multiple items selectable
- Batch actions work (download/delete)

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

### Test Case 6.8: Gallery Pagination
**Priority:** HIGH
**Steps:**
1. Scroll to bottom of gallery
2. Wait for next page to load
3. Continue scrolling

**Expected:**
- useInfiniteQuery loads next page automatically
- Loading indicator shows at bottom
- New items append (don't replace)
- Smooth infinite scroll

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

## 7. SETTINGS SCREEN

### Test Case 7.1: Profile Information Display
**Priority:** HIGH
**Steps:**
1. Navigate to Settings tab
2. Observe profile section

**Expected:**
- Email displays correctly
- Full name shown (if set)
- Restaurant name shown (if set)
- Avatar displays (or default placeholder)

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

### Test Case 7.2: Edit Profile
**Priority:** MEDIUM
**Steps:**
1. Tap "Edit Profile"
2. Update full name and restaurant name
3. Tap "Save"

**Expected:**
- Edit form opens
- Changes save successfully
- Profile updates in UI
- API call succeeds

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

### Test Case 7.3: View Plan Details
**Priority:** HIGH
**Steps:**
1. Tap "Plan & Billing" or view current plan

**Expected:**
- Current plan name displays (Starter/Growth/Pro)
- Credits limit shown
- Renewal date visible
- Upgrade button available (if not on Pro)

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

### Test Case 7.4: Change Password
**Priority:** MEDIUM
**Steps:**
1. Tap "Change Password"
2. Enter current password
3. Enter new password
4. Confirm new password
5. Tap "Update"

**Expected:**
- Form validates correctly
- Password updates successfully
- Success message shows
- User remains signed in

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

### Test Case 7.5: Dark Mode Toggle
**Priority:** LOW
**Steps:**
1. Toggle dark mode switch

**Expected:**
- App theme switches to dark
- All screens update immediately
- Preference saves

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

### Test Case 7.6: About/Help Section
**Priority:** LOW
**Steps:**
1. Tap "About" or "Help"

**Expected:**
- App version displays
- Support email/link available
- Terms & Privacy links work

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

## 8. API INTEGRATION & ERROR HANDLING

### Test Case 8.1: API Connection - Happy Path
**Priority:** HIGH
**Steps:**
1. Ensure app is connected to correct API
2. Perform any API-dependent action (load usage stats)

**Expected:**
- API responds successfully
- Data loads correctly
- No errors in console

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

### Test Case 8.2: Network Error - No Internet
**Priority:** HIGH
**Steps:**
1. Disable WiFi and mobile data
2. Try to load Enhance screen (usage stats)

**Expected:**
- Error message: "No internet connection"
- Retry button available
- App doesn't crash
- Cached data shows (if available)

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

### Test Case 8.3: API Error - 401 Unauthorized
**Priority:** HIGH
**Steps:**
1. Manually expire auth token (or simulate 401)
2. Perform any API action

**Expected:**
- Error message shows
- User redirected to Sign In screen
- Session cleared
- No infinite retry loop

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

### Test Case 8.4: API Error - 404 Not Found
**Priority:** MEDIUM
**Steps:**
1. Try to access non-existent resource
2. Observe error handling

**Expected:**
- Friendly error message
- No retry attempts (smart retry logic)
- App remains stable

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

### Test Case 8.5: API Error - 500 Server Error
**Priority:** MEDIUM
**Steps:**
1. Simulate server error
2. Perform API action

**Expected:**
- Error message: "Something went wrong"
- Retry up to 3 times (network error retry)
- User can manually retry

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

### Test Case 8.6: Polling - Generation Status
**Priority:** HIGH
**Steps:**
1. Start a video generation
2. Observe polling behavior

**Expected:**
- Status polls every 5 seconds
- Polling stops when status is "complete" or "failed"
- No polling when app is backgrounded

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

## 9. PERFORMANCE & MEMORY

### Test Case 9.1: App Launch Time
**Priority:** MEDIUM
**Steps:**
1. Close app completely
2. Launch app
3. Measure time to first screen

**Expected:**
- App launches in <2 seconds
- Splash screen shows briefly
- No white screen flashes

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

### Test Case 9.2: Memory Usage - Normal Operation
**Priority:** HIGH
**Steps:**
1. Navigate through all tabs
2. Play 3-4 videos in Explore
3. Check memory usage

**Expected:**
- Memory stays under 500MB
- No memory leaks
- Videos unload when off-screen

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

### Test Case 9.3: FPS - Scrolling Performance
**Priority:** HIGH
**Steps:**
1. Scroll rapidly in Explore screen
2. Scroll rapidly in Gallery screen
3. Monitor FPS

**Expected:**
- Maintains 55-60 FPS
- No dropped frames
- Smooth scrolling feel

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

### Test Case 9.4: App Doesn't Crash - Extended Use
**Priority:** HIGH
**Steps:**
1. Use app for 10+ minutes
2. Navigate through all screens multiple times
3. Generate 2-3 images/videos

**Expected:**
- No crashes
- No white screens
- Performance stays consistent

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

## 10. OFFLINE BEHAVIOR

### Test Case 10.1: Offline Mode - Cached Data
**Priority:** MEDIUM
**Steps:**
1. Use app while online
2. Navigate to Gallery (load items)
3. Go offline
4. Return to Gallery

**Expected:**
- Previously loaded gallery items still visible
- Cached data displays
- Clear message about offline state

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

### Test Case 10.2: Offline Mode - New Actions
**Priority:** MEDIUM
**Steps:**
1. Go offline
2. Try to upload photo or generate content

**Expected:**
- Error message: "You're offline"
- Action doesn't proceed
- No crashes

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

### Test Case 10.3: Reconnection - Auto Retry
**Priority:** MEDIUM
**Steps:**
1. Start an action (load gallery)
2. Go offline mid-request
3. Wait for error
4. Reconnect to internet
5. Tap retry

**Expected:**
- Action retries automatically or on button press
- Data loads successfully after reconnection

**Actual:**
- [ ] Pass
- [ ] Fail - Error: ___________

---

## SUMMARY

**Total Test Cases:** 68
**Priority Breakdown:**
- HIGH: 48 test cases
- MEDIUM: 18 test cases
- LOW: 2 test cases

---

## EXECUTION CHECKLIST

- [ ] Review all test cases with team
- [ ] Set up test environment (API URLs, test accounts)
- [ ] Execute HIGH priority tests first
- [ ] Document all bugs found
- [ ] Fix critical bugs immediately
- [ ] Re-test failed cases after fixes
- [ ] Execute MEDIUM/LOW priority tests
- [ ] Generate final test report

---

**Test Plan Created:** 2026-03-12
**Next Step:** Execute tests systematically and log results
