# Mobile Device Testing Guide
**App:** CraveMode AI Mobile
**Date:** 2026-03-12
**Status:** Ready for iPhone & Android Testing

---

## 📱 Pre-Testing Setup

### Step 1: Start Development Server
```bash
cd mobile
npx expo start
```

### Step 2: Connect Devices

**For iPhone:**
1. Install Expo Go from App Store
2. Scan QR code from terminal
3. Wait for app to load

**For Android:**
1. Install Expo Go from Play Store
2. Scan QR code from terminal
3. Wait for app to load

---

## 🧪 Critical Bug Tests (Must Pass!)

### Test Case 1: Enhance Screen Upload (Fix #1)
**Priority:** 🔴 CRITICAL
**What was fixed:** Missing `useState` import would crash app

**Steps:**
1. Open app → Navigate to "Enhance" tab
2. Tap "Tap to select photos" button
3. Select 1-3 photos from gallery
4. Photos should appear in grid below
5. Tap "Enhance X Photos" button at bottom

**Expected Result:** ✅
- App does NOT crash
- Photos upload successfully
- Success toast appears: "Enhancement started! Check the Gallery tab for results."

**Failure Indicator:** ❌
- App crashes immediately when tapping "Enhance" button
- Error message in console about undefined `useState`

---

### Test Case 2: Sign-In Email Validation (Fix #2)
**Priority:** 🟡 HIGH
**What was fixed:** Added email format validation

**Steps:**
1. Navigate to Sign In screen
2. Enter invalid email: `testuser` (no @ or domain)
3. Enter any password
4. Tap "Sign in" button

**Expected Result:** ✅
- Red error text appears: "Please enter a valid email address"
- Sign-in does NOT proceed
- No server request made

**Additional Test Cases:**
- `test@` → Should fail (no domain)
- `@example.com` → Should fail (no username)
- `test@example` → Should fail (no TLD)
- `test@example.com` → Should pass ✅

---

### Test Case 3: Sign-In Password Min Length (Fix #3)
**Priority:** 🟡 HIGH
**What was fixed:** Added password minimum length check

**Steps:**
1. Navigate to Sign In screen
2. Enter valid email: `test@example.com`
3. Enter short password: `12345` (5 chars)
4. Tap "Sign in" button

**Expected Result:** ✅
- Red error text appears: "Password must be at least 6 characters"
- Sign-in does NOT proceed

**Additional Test Cases:**
- `12345` (5 chars) → Should fail
- `123456` (6 chars) → Should pass ✅
- `12345678901234567890...` (129 chars) → Should fail ("must be less than 128 characters")

---

### Test Case 4: Queue Empty State CTA (Fix #4)
**Priority:** 🟡 HIGH
**What was fixed:** Added "Go to Enhance" button with clear description

**Steps:**
1. Sign in to app (if not already signed in)
2. Navigate to "Queue" tab
3. If queue has jobs, filter to a status with no jobs (e.g., "Failed")
4. OR ensure you have no jobs at all

**Expected Result:** ✅
- Empty state shows icon + "No jobs yet" title
- Description reads: "Upload photos in the Enhance tab to get started"
- Blue button appears: "Go to Enhance"
- Tapping button navigates to Enhance tab

**Old Behavior (should NOT see):** ❌
- Description: "Your photo and video jobs will appear here"
- No button

---

### Test Case 5: Video Cancel Confirmation (Fix #5)
**Priority:** 🟡 HIGH
**What was fixed:** Added confirmation alert before canceling video generation

**Steps:**
1. Navigate to "Video" tab
2. Upload 1 start frame image
3. Select motion preset (e.g., "Slow Zoom")
4. Tap "Generate 1 Video" button
5. Wait for processing state to appear (progress ring)
6. Tap "Cancel" button

**Expected Result:** ✅
- Haptic feedback vibrates
- Alert dialog appears with:
  - Title: "Cancel Generation"
  - Message: "Are you sure? This will stop the video generation."
  - Two buttons: "Keep Generating" (left) | "Yes, Cancel" (right, red)
- Tapping "Keep Generating" closes alert, continues generation
- Tapping "Yes, Cancel" stops generation, returns to upload state

**Old Behavior (should NOT see):** ❌
- Tapping "Cancel" immediately stops generation with no confirmation

---

## 🎨 UI Consistency Tests

### Test Case 6: Bottom Button Padding Consistency (Fix #6)
**Priority:** 🔵 MEDIUM
**What was fixed:** Standardized bottom padding formula across screens

**Steps:**
1. Navigate to "Enhance" tab
2. Upload 1+ photos to show bottom button
3. Note the vertical position of "Enhance X Photos" button
4. Navigate to "Video" tab
5. Upload 1+ frames to show bottom button
6. Note the vertical position of "Generate X Videos" button

**Expected Result:** ✅
- Both buttons sit at **exactly the same height** from bottom
- Both have **same spacing** above the button
- Both buttons feel **aligned** when switching tabs

**Visual Check:**
- Enhance button should be ~86px from bottom on iPhone (16 + 70)
- Video button should match exactly
- On Android (no safe area), both should be 86px from bottom

---

### Test Case 7: Gallery Select Label Clarity (Fix #7)
**Priority:** 🔵 MEDIUM
**What was fixed:** Changed "Select All Loaded" to "Select Visible"

**Steps:**
1. Navigate to "Gallery" tab
2. Ensure you have at least 1 photo/video in gallery
3. Tap checkbox icon (top right) to enter select mode
4. Look at the action bar that appears

**Expected Result:** ✅
- Action bar shows "0 selected" on left
- Blue text link says: "Select Visible"
- Tapping "Select Visible" selects all items currently visible on screen

**Old Label (should NOT see):** ❌
- "Select All Loaded"

---

### Test Case 8: Queue Processing Icon Animation (Fix #8)
**Priority:** 🟢 LOW
**What was fixed:** Made Loader2 icon actually spin during processing

**Steps:**
1. Start a photo enhancement or video generation
2. Navigate to "Queue" tab
3. Find a job with status "Processing"
4. Look at the icon next to "Photo/Video Generation" text

**Expected Result:** ✅
- Loader2 icon (circle with gap) **spins continuously** clockwise
- Smooth animation, 1 full rotation per second
- Stops spinning when job completes/fails

**Old Behavior (should NOT see):** ❌
- Icon is static, doesn't move

---

### Test Case 9: Video Progress Label Smoothness (Fix #9)
**Priority:** 🟢 LOW
**What was fixed:** Improved progress label thresholds from 10/30/70/95 to 20/40/60/80

**Steps:**
1. Start a video generation
2. Watch the progress labels change as percentage increases

**Expected Result:** ✅
- Labels change at these thresholds:
  - 0-19%: "Initializing..."
  - 20-39%: "Analyzing frames..."
  - 40-59%: "Generating motion..."
  - 60-79%: "Rendering video..."
  - 80-100%: "Finalizing..."
- Transitions feel smooth, evenly spaced

**Visual Check:**
- No flickering between labels
- Each label shows for roughly equal time

---

## 🔍 Regression Tests (Make Sure Nothing Broke)

### Regression Test 1: Sign-Up Flow
**What to check:** Ensure sign-up still works with existing validation

**Steps:**
1. Navigate to Sign Up screen
2. Enter email: `test@example.com`
3. Enter password: `123456`
4. Tap "Create account"

**Expected Result:** ✅
- Validation runs (email regex + password 6-128 chars)
- Success screen appears with green checkmark
- Message: "Check your email"

---

### Regression Test 2: Settings Password Change
**What to check:** Password change feature still works

**Steps:**
1. Navigate to Settings tab
2. Tap "Change Password" → "Update"
3. Enter new password: `newpass123`
4. Confirm password: `newpass123`
5. Tap "Update Password"

**Expected Result:** ✅
- Validates min 6 chars, max 128 chars
- Success toast: "Password updated successfully"
- Section collapses back to closed state

---

### Regression Test 3: Gallery Filtering
**What to check:** Filter tabs still work correctly

**Steps:**
1. Navigate to Gallery tab
2. Tap each filter: All → Enhanced → Videos → Originals
3. Each filter should show correct items

**Expected Result:** ✅
- Filter tabs respond to taps
- Gallery updates to show matching items
- "Select Visible" button still works in each filter

---

### Regression Test 4: Explore Screen
**What to check:** Showcase videos and before/after still work

**Steps:**
1. Navigate to Explore tab
2. Scroll through featured videos (horizontal)
3. Scroll through before/after photos (horizontal)
4. Tap category filters (All, Burgers, Pizza, etc.)

**Expected Result:** ✅
- All sections render correctly
- Videos load and play
- Before/after tap-to-compare works
- Category filtering updates grid

---

## 📊 Device-Specific Tests

### iPhone Tests (Safe Area Insets)

**Test on:** iPhone with notch/Dynamic Island (iPhone 14, 15, etc.)

**Check:**
1. Top safe area insets respected (no content under notch)
2. Bottom buttons sit above home indicator
3. Padding formula works: `Math.max(insets.bottom, 16) + 70`

**Expected Bottom Space:**
- iPhone 14: ~120px (44px inset + 16 min + 70 button space)
- iPhone SE: ~86px (0px inset + 16 min + 70 button space)

---

### Android Tests (No Safe Area Insets)

**Test on:** Android device without notch

**Check:**
1. Bottom buttons have minimum 16px padding + 70px space = 86px total
2. No awkward spacing at top/bottom
3. Padding formula fallback works: `Math.max(0, 16) + 70`

---

### Landscape Orientation Test

**Steps:**
1. Rotate device to landscape mode
2. Test all tabs: Enhance, Video, Gallery, Queue, Explore, Settings

**Expected Result:** ✅
- All screens remain usable in landscape
- Bottom buttons don't overlap content
- Safe area insets still respected

---

## 🐛 Known Issues to Watch For

### Issue 1: Haptic Feedback Not Working
**Symptom:** No vibration when tapping buttons
**Cause:** Haptic permissions not granted on device
**Solution:** Check device settings → Notifications → Expo Go → Allow haptics

### Issue 2: Image Picker Permissions Denied
**Symptom:** "Permission denied" error when selecting photos
**Cause:** First-time permission prompt declined
**Solution:** iOS Settings → Expo Go → Photos → Select "All Photos"

### Issue 3: Slow First Load
**Symptom:** App takes 10+ seconds to load initially
**Cause:** Metro bundler compiling JavaScript
**Solution:** Normal behavior, subsequent loads are instant

---

## ✅ Test Results Template

Copy this template to track your testing:

```
# CraveMode Mobile - Test Results
**Date:** [Fill in]
**Tester:** [Fill in]
**Device:** [iPhone 14 / Pixel 7 / etc.]
**OS Version:** [iOS 17.2 / Android 14 / etc.]

## Critical Tests
- [ ] Test 1: Enhance upload works (no crash)
- [ ] Test 2: Email validation on sign-in
- [ ] Test 3: Password min length on sign-in
- [ ] Test 4: Queue empty state CTA works
- [ ] Test 5: Video cancel confirmation appears

## UI Consistency Tests
- [ ] Test 6: Bottom buttons aligned
- [ ] Test 7: "Select Visible" label correct
- [ ] Test 8: Queue icon spins
- [ ] Test 9: Progress labels smooth

## Regression Tests
- [ ] Reg 1: Sign-up flow works
- [ ] Reg 2: Password change works
- [ ] Reg 3: Gallery filtering works
- [ ] Reg 4: Explore screen works

## Device-Specific
- [ ] Safe area insets respected (iPhone)
- [ ] Landscape orientation works
- [ ] No haptic/permission issues

## Issues Found
[List any bugs or unexpected behavior]

## Overall Assessment
- Stability: [1-10]
- UX Quality: [1-10]
- Ready for Production: [Yes/No]
```

---

## 🚀 Post-Testing Actions

### If All Tests Pass ✅
1. Mark app as "Ready for Production Testing"
2. Deploy to TestFlight (iOS) or Internal Testing (Android)
3. Gather user feedback from beta testers
4. Monitor crash analytics for 48 hours

### If Tests Fail ❌
1. Document exact failure scenario
2. Note device/OS where failure occurred
3. Check console logs for error messages
4. Create bug report with:
   - Steps to reproduce
   - Expected vs actual behavior
   - Screenshots/video if possible
5. Fix bug and re-test

---

## 📞 Support Contacts

**Technical Issues:**
- Claude Code (implemented all fixes)
- Check [MOBILE-UI-UX-FIXES-IMPLEMENTED.md](MOBILE-UI-UX-FIXES-IMPLEMENTED.md) for fix details

**Testing Questions:**
- Refer to [MOBILE-UI-UX-AUDIT.md](MOBILE-UI-UX-AUDIT.md) for original issue descriptions

---

**Happy Testing! 🎉**

Remember: The goal is to ensure users have a smooth, delightful experience with CraveMode AI on their devices. Report everything you see - no issue is too small!
