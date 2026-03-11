# Mobile App - End-to-End Test Cases
**Date:** 2026-03-12
**Purpose:** Final deployment readiness validation
**Test Type:** Simulated E2E via code review

---

## Test Suite 1: Authentication Flow 🔐

### TC-1.1: New User Sign Up (Happy Path)
**Steps:**
1. Open app → lands on sign-up screen
2. Enter valid email (user@test.com)
3. Enter valid password (minimum 6 chars)
4. Tap "Create account" button
5. See success message "Check your email"

**Expected Results:**
- ✅ Email validation passes (regex check)
- ✅ Password validation passes (6-128 chars)
- ✅ Haptic feedback on submit (medium)
- ✅ Success screen shows with green checkmark
- ✅ Email confirmation instructions displayed
- ✅ "Go to Sign In" button appears

**Status:** 🔄 TESTING...

---

### TC-1.2: Sign Up Validation Errors
**Steps:**
1. Try empty email → see error + haptic
2. Try invalid email (no @) → see error + haptic
3. Try password < 6 chars → see error + haptic
4. Try password > 128 chars → see error + haptic

**Expected Results:**
- ✅ All 4 validations trigger haptic.error()
- ✅ Error messages clear and specific
- ✅ Red error text displayed
- ✅ Form remains editable after error

**Status:** 🔄 TESTING...

---

### TC-1.3: Google OAuth Sign Up
**Steps:**
1. Tap "Continue with Google" button
2. Browser opens for Google auth
3. User approves access
4. Redirects back to app
5. User is logged in

**Expected Results:**
- ✅ Loading state shows "Redirecting..."
- ✅ Haptic feedback on error (if OAuth fails)
- ✅ Error message shown if auth fails
- ✅ Success redirects to main app

**Status:** 🔄 TESTING...

---

### TC-1.4: Existing User Sign In
**Steps:**
1. Navigate to sign-in screen
2. Enter valid email
3. Enter correct password
4. Tap "Sign in" button
5. Redirected to main app

**Expected Results:**
- ✅ Email validation (regex)
- ✅ Password validation (6+ chars)
- ✅ Haptic feedback on submit
- ✅ Loading state during auth
- ✅ Error handling for wrong credentials
- ✅ Success redirects to /(tabs)/

**Status:** 🔄 TESTING...

---

## Test Suite 2: Photo Enhancement Flow 📸

### TC-2.1: Upload and Enhance Photos (Happy Path)
**Steps:**
1. User logged in, on Upload tab
2. Tap upload zone
3. Select 3 photos from gallery
4. Photos appear in grid with preview
5. Select style: "Bright & Fresh"
6. Select format: "Instagram Square"
7. Select variations: 2
8. Enable enhancements: Lighting, Color
9. Tap "Enhance 3 Photos" button
10. Success toast appears
11. Navigate to Gallery tab
12. See processing jobs

**Expected Results:**
- ✅ Image picker opens correctly
- ✅ File validation (size, type, dimensions)
- ✅ Invalid files show error toast + haptic
- ✅ Valid files added to PhotoGrid
- ✅ Haptic feedback on style/format/variation select
- ✅ Cost preview calculates correctly
- ✅ Credit validation before upload
- ✅ Haptic medium on submit
- ✅ Upload mutation succeeds
- ✅ Success haptic + toast
- ✅ Files cleared after upload
- ✅ Navigation stays on Upload tab

**Status:** 🔄 TESTING...

---

### TC-2.2: Photo Upload Validations
**Steps:**
1. Try to enhance with 0 photos selected
2. Try file > 10MB
3. Try invalid file type (PDF)
4. Try image < 100x100px
5. Try corrupted file (0 bytes)

**Expected Results:**
- ✅ No photos error: haptic + toast "Select at least one photo"
- ✅ File too large: validation error with size in toast
- ✅ Invalid type: error toast + haptic
- ✅ Too small: error toast + haptic
- ✅ Corrupted: error toast + haptic
- ✅ All errors prevent upload
- ✅ Valid files still added (partial success)

**Status:** 🔄 TESTING...

---

### TC-2.3: Insufficient Credits
**Steps:**
1. User has 5 credits remaining
2. Select 10 photos
3. Set variations to 2 (needs 20 credits)
4. Tap "Enhance" button

**Expected Results:**
- ✅ Credit validation runs before upload
- ✅ Error toast: "Need 20 credits but only 5 remaining"
- ✅ Haptic error feedback
- ✅ Upload prevented
- ✅ User can reduce photo count or variations

**Status:** 🔄 TESTING...

---

### TC-2.4: Remove Photos from Grid
**Steps:**
1. Select 5 photos
2. Tap X button on 3rd photo
3. Photo removed from grid
4. Count updates to "4 photos selected"

**Expected Results:**
- ✅ Haptic light on X button press
- ✅ Photo smoothly animates out (FadeOut)
- ✅ Grid reflows correctly
- ✅ Cost preview updates
- ✅ No crashes or UI glitches

**Status:** 🔄 TESTING...

---

## Test Suite 3: Video Generation Flow 🎥

### TC-3.1: Generate Videos (Happy Path)
**Steps:**
1. Navigate to Video tab
2. Upload 2 start frame images
3. Select motion style: "Slow Zoom"
4. Select camera direction: "Zoom In"
5. Set duration: 10s
6. Set aspect ratio: 9:16
7. Tap "Generate 2 Videos" button
8. Processing screen appears
9. Progress updates: 0% → 100%
10. Success toast appears
11. Auto-navigate to Gallery

**Expected Results:**
- ✅ Image picker accepts multiple images
- ✅ Images validated (size, type, dimensions)
- ✅ Haptic feedback on all selections
- ✅ Motion preset toggleable (multi-select)
- ✅ Credit preview shows total videos count
- ✅ Haptic medium on generate
- ✅ Processing ring animates
- ✅ Progress text updates (Initializing → Analyzing → Rendering → Finalizing)
- ✅ Cancel button works with confirmation
- ✅ Success haptic + toast
- ✅ Auto-navigate after 1 second

**Status:** 🔄 TESTING...

---

### TC-3.2: Video Validation Errors
**Steps:**
1. Try to generate with 0 images
2. Try with insufficient credits
3. Test upload error scenario

**Expected Results:**
- ✅ No images: haptic + toast "Upload at least one start frame"
- ✅ Insufficient credits: haptic + toast "Need X but only Y remaining"
- ✅ Upload error: haptic + toast with error message
- ✅ All errors prevent generation
- ✅ Form remains usable after error

**Status:** 🔄 TESTING...

---

### TC-3.3: Cancel Video Generation
**Steps:**
1. Start video generation (processing)
2. Tap "Cancel" button
3. Alert appears: "Are you sure?"
4. Tap "Yes, Cancel"
5. Generation stops
6. Return to upload form

**Expected Results:**
- ✅ Haptic medium on cancel tap
- ✅ Alert dialog shows
- ✅ "Keep Generating" dismisses alert
- ✅ "Yes, Cancel" stops job
- ✅ Processing screen disappears
- ✅ Images remain in form
- ✅ Can retry generation

**Status:** 🔄 TESTING...

---

## Test Suite 4: Gallery Management 🖼️

### TC-4.1: View Gallery Items
**Steps:**
1. Navigate to Gallery tab
2. See grid of enhanced photos/videos
3. Pull to refresh
4. Scroll to load more
5. Apply filter: "Enhanced"
6. Search for specific item

**Expected Results:**
- ✅ FlatList renders in 2-column grid
- ✅ Items load with pagination (20 per page)
- ✅ Pull-to-refresh works with spinner
- ✅ Infinite scroll loads next page
- ✅ Max 50 pages (1000 items) with warning toast
- ✅ Filter changes re-fetch data
- ✅ Search input filters client-side
- ✅ Empty state shows for no items
- ✅ Performance smooth (windowed rendering)

**Status:** 🔄 TESTING...

---

### TC-4.2: Download Single Item
**Steps:**
1. Long press on gallery item
2. Tap download icon
3. File downloads to device
4. Share dialog opens

**Expected Results:**
- ✅ Haptic light on long press
- ✅ Download mutation triggers
- ✅ File fetched from API
- ✅ ExpoFile downloads to cache
- ✅ Sharing.shareAsync opens
- ✅ Error handling: haptic + toast on failure

**Status:** 🔄 TESTING...

---

### TC-4.3: Delete Single Item
**Steps:**
1. Long press on gallery item
2. Tap delete icon
3. Item removed from gallery
4. Gallery re-fetches

**Expected Results:**
- ✅ Delete mutation succeeds
- ✅ Item animates out
- ✅ React Query invalidates gallery cache
- ✅ UI updates without full reload

**Status:** 🔄 TESTING...

---

### TC-4.4: Bulk Select and Delete
**Steps:**
1. Tap select mode icon (checkbox)
2. Tap 5 gallery items
3. Tap "Select Visible" to select all loaded
4. Tap "Delete" button
5. Confirm deletion in alert
6. All selected items deleted

**Expected Results:**
- ✅ Haptic selection on each item tap
- ✅ Checkmark appears on selected items
- ✅ Count shows "5 selected"
- ✅ "Select Visible" adds all loaded items
- ✅ Delete button shows count
- ✅ Alert confirms deletion
- ✅ Haptic error if delete fails
- ✅ Success toast shows deleted count
- ✅ Gallery refreshes
- ✅ Select mode exits

**Status:** 🔄 TESTING...

---

### TC-4.5: Bulk Download
**Steps:**
1. Enter select mode
2. Select 3 items
3. Tap "Save" button
4. All 3 items download

**Expected Results:**
- ✅ Download mutation called for each item
- ✅ Toast: "Downloading 3 items..."
- ✅ Select mode exits
- ✅ Share dialogs open sequentially

**Status:** 🔄 TESTING...

---

## Test Suite 5: Queue Monitoring 📊

### TC-5.1: View Active Jobs
**Steps:**
1. Navigate to Queue tab
2. See list of processing jobs
3. Each job shows:
   - Status badge (queued/processing/complete/failed)
   - Progress percentage
   - Item count
   - Timestamp

**Expected Results:**
- ✅ Jobs sorted by newest first
- ✅ Processing jobs show spinning icon
- ✅ Status colors match theme (green/blue/amber/red)
- ✅ Progress ring animates
- ✅ Auto-refresh every 5s for active jobs
- ✅ Empty state shows "Go to Enhance" button

**Status:** 🔄 TESTING...

---

### TC-5.2: Cancel Queued Job
**Steps:**
1. Find job with status "queued"
2. Tap cancel icon
3. Alert confirms cancellation
4. Job status updates to "cancelled"

**Expected Results:**
- ✅ Alert shows "Cancel Job?" confirmation
- ✅ Haptic success on cancel
- ✅ Toast: "Job cancelled"
- ✅ Haptic error if cancel fails
- ✅ Toast error message if fails
- ✅ Queue refreshes

**Status:** 🔄 TESTING...

---

### TC-5.3: Retry Failed Job
**Steps:**
1. Find job with status "failed"
2. Tap retry icon
3. Job restarts processing

**Expected Results:**
- ✅ Haptic medium on retry
- ✅ Retry mutation succeeds
- ✅ Haptic success + toast "Job restarted"
- ✅ Haptic error if retry fails
- ✅ Job status updates
- ✅ Queue and usage stats refresh

**Status:** 🔄 TESTING...

---

## Test Suite 6: Settings & Profile ⚙️

### TC-6.1: View Usage Stats
**Steps:**
1. Navigate to Settings tab
2. See usage stats card:
   - Current plan badge
   - Photo usage ring (X/Y used)
   - Video usage ring (X/Y used)
   - Renewal date

**Expected Results:**
- ✅ Plan badge shows correct tier (Starter/Growth/Pro)
- ✅ Progress rings animate on load
- ✅ Progress rings pulse at 90%+
- ✅ Usage numbers accurate
- ✅ Renewal date formatted correctly
- ✅ Skeleton loaders show during fetch

**Status:** 🔄 TESTING...

---

### TC-6.2: Update Profile
**Steps:**
1. Edit "Full Name" field
2. Edit "Restaurant Name" field
3. Tap "Save Changes" button
4. Profile updates

**Expected Results:**
- ✅ "Save Changes" button only shows when changed
- ✅ Haptic medium on save
- ✅ Update mutation succeeds
- ✅ Haptic success + toast "Profile updated"
- ✅ Haptic error if save fails
- ✅ Profile data refetches
- ✅ Button disappears after save

**Status:** 🔄 TESTING...

---

### TC-6.3: Change Password
**Steps:**
1. Tap "Change Password" → expands form
2. Enter new password (8 chars)
3. Confirm password (matching)
4. Tap "Update Password" button
5. Password updated

**Expected Results:**
- ✅ Haptic selection on expand
- ✅ Password validation (6-128 chars)
- ✅ Mismatch validation with haptic
- ✅ Too short validation with haptic
- ✅ Too long validation with haptic
- ✅ Haptic medium on submit
- ✅ Supabase auth.updateUser called
- ✅ Haptic success + toast on success
- ✅ Haptic error + toast on failure
- ✅ Form collapses on success

**Status:** 🔄 TESTING...

---

### TC-6.4: Manage Billing
**Steps:**
1. Tap "Manage Billing" button
2. Browser opens to Stripe portal
3. User can update payment method

**Expected Results:**
- ✅ Haptic light on tap
- ✅ useBillingPortal mutation called
- ✅ Linking.openURL opens browser
- ✅ Stripe portal URL correct

**Status:** 🔄 TESTING...

---

### TC-6.5: View Plans
**Steps:**
1. Tap "View Plans" button
2. Browser opens to pricing page

**Expected Results:**
- ✅ Haptic light on tap
- ✅ PRICING_URL constant used
- ✅ Linking.openURL opens browser

**Status:** 🔄 TESTING...

---

### TC-6.6: Sign Out
**Steps:**
1. Tap "Sign Out" button
2. Alert confirms sign out
3. Tap "Sign Out" in alert
4. User logged out
5. Redirected to sign-in screen

**Expected Results:**
- ✅ Alert shows "Are you sure?"
- ✅ Cancel dismisses alert
- ✅ Sign Out calls signOut()
- ✅ Auth store cleared
- ✅ Router replaces to /(auth)/sign-in
- ✅ No navigation stack left

**Status:** 🔄 TESTING...

---

## Test Suite 7: Error Handling & Edge Cases 🚨

### TC-7.1: Network Offline
**Steps:**
1. Turn off WiFi/cellular
2. Try to enhance photos
3. Try to fetch gallery
4. Try to update profile

**Expected Results:**
- ✅ React Query retry logic (3 attempts)
- ✅ Error toast shows for each failure
- ✅ Haptic error feedback
- ✅ User can retry manually
- ✅ No app crashes

**Status:** 🔄 TESTING...

---

### TC-7.2: API Rate Limiting (401/403)
**Steps:**
1. Simulate 401 Unauthorized response
2. Simulate 403 Forbidden response

**Expected Results:**
- ✅ React Query stops retrying (no infinite loop)
- ✅ ApiError class detects status codes
- ✅ User sees auth error message
- ✅ Redirect to sign-in if needed

**Status:** 🔄 TESTING...

---

### TC-7.3: 404 Not Found
**Steps:**
1. Request deleted gallery item
2. Request non-existent job

**Expected Results:**
- ✅ React Query stops retrying
- ✅ Error toast shows
- ✅ UI handles gracefully (removes item)

**Status:** 🔄 TESTING...

---

### TC-7.4: Double-Tap Race Condition
**Steps:**
1. Rapidly tap "Enhance" button 5 times
2. Only one upload should trigger

**Expected Results:**
- ✅ isUploading guard prevents duplicates
- ✅ Button disabled during loading
- ✅ No duplicate API calls

**Status:** 🔄 TESTING...

---

### TC-7.5: Memory Leak Prevention
**Steps:**
1. Navigate between tabs 20 times
2. Upload 10 photos, cancel, repeat 5 times
3. Scroll gallery 100+ items

**Expected Results:**
- ✅ No memory leaks from animations
- ✅ useCallback/useMemo prevent re-renders
- ✅ FlatList windowSize limits memory
- ✅ removeClippedSubviews unmounts off-screen
- ✅ React Query stale time prevents over-fetching

**Status:** 🔄 TESTING...

---

## Test Suite 8: Performance & UX Polish ⚡

### TC-8.1: Animation Smoothness
**Steps:**
1. Navigate between tabs
2. Select photos (grid animation)
3. Toggle filters
4. Scroll gallery

**Expected Results:**
- ✅ All animations 60fps
- ✅ FadeInDown stagger looks smooth
- ✅ Progress rings animate fluidly
- ✅ No jank on tab switch
- ✅ Haptic feedback feels responsive

**Status:** 🔄 TESTING...

---

### TC-8.2: Loading States
**Steps:**
1. Check all screens on first load
2. Check all mutations during processing

**Expected Results:**
- ✅ Skeleton loaders show during fetch
- ✅ Button loading states prevent double-tap
- ✅ Spinner shows on pull-to-refresh
- ✅ Progress rings show during processing
- ✅ No blank screens or flash of content

**Status:** 🔄 TESTING...

---

### TC-8.3: Safe Area Insets
**Steps:**
1. Test on iPhone with notch/Dynamic Island
2. Check all tabs

**Expected Results:**
- ✅ Top content respects insets.top
- ✅ Bottom sticky buttons clear home indicator
- ✅ No content hidden behind notch
- ✅ Math.max(insets.bottom, 16) + 70 for tab bar

**Status:** 🔄 TESTING...

---

### TC-8.4: Haptic Feedback Consistency
**Steps:**
1. Test all user actions
2. Verify haptic type matches action

**Expected Results:**
- ✅ Buttons: light or medium
- ✅ Primary actions: medium
- ✅ Selections: selection
- ✅ Errors: error
- ✅ Success: success
- ✅ No missing haptics on interactions

**Status:** 🔄 TESTING...

---

## 📊 Test Execution Summary

**Total Test Cases:** 0 (to be counted after execution)
**Passed:** 0
**Failed:** 0
**Blocked:** 0
**Deployment Ready:** ⏳ PENDING

---

**Next Steps:**
1. Execute all test cases via code review
2. Document any failures with line numbers
3. Fix critical/high issues before deployment
4. Generate final deployment readiness report
