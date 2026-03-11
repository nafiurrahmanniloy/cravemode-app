# Mobile App — Ultra-Comprehensive Test Plan
**Generated:** 2026-03-12
**Scope:** Every component, screen, hook, store, edge case
**Test Cases:** 150+ scenarios
**Difficulty:** Maximum (designed to break the app)

---

## 🎯 TEST METHODOLOGY

This test plan covers:
- ✅ All 6 screens (Enhance, Video, Gallery, Queue, Explore, Settings)
- ✅ All authentication flows
- ✅ All API hooks and mutations
- ✅ All Zustand stores
- ✅ All UI components
- ✅ All edge cases and race conditions
- ✅ Memory leaks and performance issues
- ✅ State synchronization bugs
- ✅ Platform-specific issues
- ✅ Accessibility and UX issues

---

## CATEGORY 1: AUTHENTICATION & SESSION MANAGEMENT (20 tests)

### Basic Auth Flows
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| A1 | Sign up with valid email/password | Account created, auto sign-in | CRITICAL |
| A2 | Sign up with existing email | Error: "Email already registered" | HIGH |
| A3 | Sign up with invalid email format | Client-side validation error | MEDIUM |
| A4 | Sign up with password < 6 chars | Error: "Password too short" | MEDIUM |
| A5 | Sign up with password > 128 chars | Error: "Password too long" | MEDIUM |
| A6 | Sign in with correct credentials | Successful auth, navigate to app | CRITICAL |
| A7 | Sign in with wrong password | Error: "Invalid credentials" | HIGH |
| A8 | Sign in with non-existent email | Error: "User not found" | HIGH |
| A9 | Sign out while logged in | Session cleared, redirect to auth | CRITICAL |
| A10 | Sign out while already signed out | No error, graceful handling | LOW |

### Session Edge Cases
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| A11 | Kill app mid-authentication | Resume auth on restart or reset | HIGH |
| A12 | Token expires while app is open | Auto-refresh or redirect to login | CRITICAL |
| A13 | Token expires during API call | Retry after refresh or prompt login | CRITICAL |
| A14 | Simultaneous logins on 2 devices | Both sessions remain valid | MEDIUM |
| A15 | Change password on device A, use device B | Device B session invalidated | HIGH |
| A16 | Revoke session from Supabase dashboard | App detects and redirects to login | HIGH |
| A17 | App in background for 7 days | Session persists or auto-refresh | MEDIUM |
| A18 | App in background, token expires, resume | Auto-refresh on resume | HIGH |
| A19 | Network drops during sign-up | Proper error, no partial account creation | HIGH |
| A20 | Rapid sign in/out 10 times | No race conditions, state stays consistent | HIGH |

---

## CATEGORY 2: ENHANCE SCREEN (25 tests)

### File Selection & Validation
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| E1 | Select 1 valid photo | Photo added to grid | CRITICAL |
| E2 | Select 10 valid photos | All 10 added to grid | HIGH |
| E3 | Select MAX_PHOTOS_PER_UPLOAD (10) | All added successfully | HIGH |
| E4 | Try to select 11+ photos | Either limit enforced or all accepted | MEDIUM |
| E5 | Select zero-byte corrupted file | Error: "Corrupted or empty" | HIGH |
| E6 | Select 1KB tiny valid image | Accepted (no minimum size) | LOW |
| E7 | Select exactly 10MB image | Accepted (at limit) | MEDIUM |
| E8 | Select 10.1MB image | Error: "Too large" | HIGH |
| E9 | Select 50MB image | Error: "Too large" | HIGH |
| E10 | Select non-image file (PDF, video) | Error: "Invalid type" | HIGH |
| E11 | Select image with no file extension | Validated by mime type, accepted if valid | MEDIUM |
| E12 | Select image with wrong extension (.txt renamed to .jpg) | Mime type validation catches it | MEDIUM |
| E13 | Select HEIC image (iOS native) | Convert or accept if supported | MEDIUM |
| E14 | Select WebP image | Accepted if mime type valid | LOW |
| E15 | Select 1px × 1px tiny resolution | Accepted (no min resolution check?) | LOW |

### Upload State Management
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| E16 | Add 5 photos, remove 1, add 2 more | State updates correctly, 6 total | MEDIUM |
| E17 | Add 10 photos, remove all, add 5 | State reset and repopulated correctly | MEDIUM |
| E18 | Select style, change mind, select different | State updates, no lingering old value | LOW |
| E19 | Select format "all", then specific format | State updates correctly | LOW |
| E20 | Change variations from 1→2→3→4→1 | State tracks correctly | LOW |
| E21 | Toggle enhancement on/off rapidly 10 times | No race condition in state | MEDIUM |
| E22 | Toggle all 4 enhancements on | All 4 active in state | LOW |
| E23 | Toggle all 4 enhancements off | All 4 inactive in state | LOW |

### Credit & Cost Logic
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| E24 | Upload with sufficient credits | Success | CRITICAL |
| E25 | Upload when credits = exactly needed | Success, balance = 0 | HIGH |
| E26 | Upload when credits = needed - 1 | Error: "Insufficient credits" | CRITICAL |
| E27 | Upload when credits = 0 | Error: "Insufficient credits" | CRITICAL |
| E28 | Change variations, cost preview updates | Real-time cost calculation | HIGH |
| E29 | Add more photos, cost preview updates | Real-time cost calculation | HIGH |
| E30 | Cost preview shows correct tier pricing | Starter vs Growth vs Pro rates | HIGH |

### Upload Execution
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| E31 | Tap Enhance button once | Upload starts, loading state | CRITICAL |
| E32 | Double-tap Enhance rapidly (<100ms) | Only 1 upload (race guard works) | CRITICAL |
| E33 | Tap Enhance 5 times rapidly | Only 1 upload (race guard works) | CRITICAL |
| E34 | Network drops mid-upload | Error, no partial credit deduction | CRITICAL |
| E35 | Kill app mid-upload | Resume or cancel on restart | HIGH |
| E36 | Upload completes, files cleared | State reset, ready for next upload | HIGH |
| E37 | Upload fails, files remain | User can retry or remove files | HIGH |
| E38 | Upload succeeds, navigate away, come back | State reset (files cleared) | MEDIUM |
| E39 | Upload while another upload in progress | Second upload blocked or queued | HIGH |
| E40 | Start upload, immediately sign out | Upload cancelled, no orphaned jobs | HIGH |

---

## CATEGORY 3: VIDEO SCREEN (20 tests)

### Video Configuration
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| V1 | Select source photo for video | Photo selected | CRITICAL |
| V2 | Select 10MB photo as source | Accepted | MEDIUM |
| V3 | Select corrupted photo | Error caught | HIGH |
| V4 | Change duration 5s→10s→15s | State updates | LOW |
| V5 | Change aspect ratio 9:16→1:1→16:9 | State updates | LOW |
| V6 | Select motion preset "zoom" | State updates | LOW |
| V7 | Select multiple motion presets | All selected in state | LOW |
| V8 | Deselect all motion presets | State empty | LOW |
| V9 | Select camera direction "pan left" | State updates | LOW |
| V10 | Select all camera directions | All in state | LOW |

### Video Generation
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| V11 | Generate video with sufficient credits | Job created, polling starts | CRITICAL |
| V12 | Generate with insufficient credits | Error before API call | CRITICAL |
| V13 | Generate with credits = exactly needed | Success, balance = 0 | HIGH |
| V14 | Network drops mid-generation | Error, no partial credit deduction | CRITICAL |
| V15 | Generation job takes 5 minutes | Status polling every 5s, shows progress | HIGH |
| V16 | Generation fails on server | Error message shown, can retry | HIGH |
| V17 | Start generation, kill app | Job continues server-side, resume shows status | MEDIUM |
| V18 | Start generation, sign out | Job orphaned? Or visible after login? | HIGH |
| V19 | Generate 2 videos simultaneously | Both tracked independently | MEDIUM |
| V20 | Complete generation, auto-navigate to gallery | Navigation works, video visible | MEDIUM |

---

## CATEGORY 4: GALLERY SCREEN (30 tests)

### Gallery Loading & Display
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| G1 | Load gallery with 0 items | Empty state shown | LOW |
| G2 | Load gallery with 1 item | Single item displayed | MEDIUM |
| G3 | Load gallery with 20 items (1 page) | All 20 visible | HIGH |
| G4 | Load gallery with 100 items (5 pages) | Pagination works | HIGH |
| G5 | Load gallery with 1000 items (50 pages) | Stops at 50 pages (safety limit) | CRITICAL |
| G6 | Load gallery with 1001+ items | Safety limit prevents infinite load | CRITICAL |
| G7 | Gallery images fail to load | Placeholder or error state | MEDIUM |
| G8 | Gallery videos fail to load | Placeholder or error state | MEDIUM |

### Filtering & Sorting
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| G9 | Filter: "all" | Shows all items | CRITICAL |
| G10 | Filter: "enhanced" | Only enhanced photos | HIGH |
| G11 | Filter: "videos" | Only videos | HIGH |
| G12 | Filter: "originals" | Only original uploads | HIGH |
| G13 | Sort: "newest" | Newest first | HIGH |
| G14 | Sort: "oldest" | Oldest first | HIGH |
| G15 | Change filter "all"→"videos" | Re-fetch, show only videos | HIGH |
| G16 | Change sort "newest"→"oldest" | Re-sort, oldest first | HIGH |
| G17 | Change filter + sort simultaneously | Both applied correctly | MEDIUM |
| G18 | Apply filter, scroll 3 pages, change filter | Reset to page 1 | MEDIUM |

### Item Actions
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| G19 | Tap item to view full-screen | Modal/detail view opens | HIGH |
| G20 | Download single item | File downloads, share sheet opens | CRITICAL |
| G21 | Delete single item | Confirmation, item removed | CRITICAL |
| G22 | Cancel delete confirmation | Item remains | MEDIUM |
| G23 | Delete item, then undo (if supported) | Item restored | LOW |
| G24 | Delete last item on page | Page updates or goes to prev page | MEDIUM |

### Select Mode & Bulk Actions
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| G25 | Enter select mode | Checkboxes appear | HIGH |
| G26 | Select 1 item | Checkbox marked | MEDIUM |
| G27 | Select 10 items | All 10 marked | HIGH |
| G28 | Select all items on current page | All marked | HIGH |
| G29 | Select all across multiple pages | Only current page? Or all loaded? | MEDIUM |
| G30 | Bulk delete 10 selected items | All 10 deleted after confirmation | CRITICAL |
| G31 | Bulk delete 100 items | All deleted (may take time) | HIGH |
| G32 | Cancel bulk delete | Items remain | MEDIUM |
| G33 | Bulk download 10 items | All 10 downloaded (share sheet?) | MEDIUM |
| G34 | Exit select mode | Checkboxes hidden, selection cleared | LOW |

### Pagination Edge Cases
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| G35 | Scroll to load page 2 | Loads seamlessly | CRITICAL |
| G36 | Scroll to load page 10 | All 10 pages loaded | HIGH |
| G37 | Scroll very fast to page 50 | Stops at 50 (safety limit) | CRITICAL |
| G38 | Scroll to bottom, API returns no nextPage | Stops loading, no infinite spinner | HIGH |

---

## CATEGORY 5: QUEUE SCREEN (20 tests)

### Queue Display
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| Q1 | Load queue with 0 jobs | Empty state | LOW |
| Q2 | Load queue with 1 active job | Job shown with status | HIGH |
| Q3 | Load queue with 10 jobs (various states) | All displayed correctly | HIGH |
| Q4 | Load queue with 50+ jobs | Paginated or all shown | MEDIUM |
| Q5 | Job status: "queued" | Shows queued state | HIGH |
| Q6 | Job status: "processing" | Shows processing with progress | HIGH |
| Q7 | Job status: "completed" | Shows completed with result | HIGH |
| Q8 | Job status: "failed" | Shows error message | HIGH |
| Q9 | Job status: "cancelled" | Shows cancelled state | MEDIUM |

### Status Polling
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| Q10 | Active job polls every 5s | Status updates in real-time | CRITICAL |
| Q11 | Job completes while polling | Stops polling, shows result | CRITICAL |
| Q12 | Job fails while polling | Stops polling, shows error | HIGH |
| Q13 | Multiple active jobs | All poll independently | HIGH |
| Q14 | No active jobs | No polling (saves battery) | MEDIUM |
| Q15 | Navigate away, come back | Polling resumes if needed | MEDIUM |

### Job Actions
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| Q16 | Cancel queued job | Job cancelled immediately | HIGH |
| Q17 | Cancel processing job | Job cancelled (may take time) | HIGH |
| Q18 | Try to cancel completed job | Button disabled or no-op | LOW |
| Q19 | Retry failed job | New job created | HIGH |
| Q20 | Retry with insufficient credits | Error before retry | CRITICAL |

---

## CATEGORY 6: EXPLORE SCREEN (20 tests)

### Content Display
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| EX1 | Load explore screen | Featured videos load | CRITICAL |
| EX2 | Load with 0 showcase videos | Empty or placeholder | LOW |
| EX3 | Load with 10 showcase videos | All 10 displayed | HIGH |
| EX4 | Scroll through showcase carousel | Smooth scrolling | MEDIUM |
| EX5 | Before/after section loads | Images displayed side-by-side | HIGH |
| EX6 | Before/after images fail to load | Placeholder or error | LOW |

### Video Playback
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| EX7 | Tap to play showcase video | Video plays | CRITICAL |
| EX8 | Tap to pause video | Video pauses | HIGH |
| EX9 | Play video, scroll away | Video stops/unmounts | HIGH |
| EX10 | Play 3 videos in sequence | Each plays correctly, previous stops | HIGH |
| EX11 | Video fails to load | Error state or skip | MEDIUM |
| EX12 | Play video on slow network | Buffering indicator | MEDIUM |

### Category Filtering
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| EX13 | Filter by category "All" | Shows all videos | HIGH |
| EX14 | Filter by category "Food" | Only food videos | HIGH |
| EX15 | Filter by category "Drink" | Only drink videos | HIGH |
| EX16 | Filter by category "Dessert" | Only dessert videos | HIGH |
| EX17 | Switch categories rapidly | No race condition | MEDIUM |
| EX18 | Filter to empty category | Empty state or message | LOW |

### Memory Management
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| EX19 | Scroll through 50 videos | No memory leak, old videos unload | CRITICAL |
| EX20 | Play video, navigate away, come back | Video resets, no memory leak | HIGH |

---

## CATEGORY 7: SETTINGS SCREEN (25 tests)

### Profile Management
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| S1 | Load settings screen | Profile data loads | CRITICAL |
| S2 | Edit display name | Updates successfully | HIGH |
| S3 | Edit email | Updates or requires verification | HIGH |
| S4 | Edit restaurant name | Updates successfully | MEDIUM |
| S5 | Save profile with no changes | No API call or no-op | LOW |
| S6 | Save profile with network error | Error shown, changes not lost | HIGH |
| S7 | Edit profile, navigate away without saving | Changes discarded or prompt to save | MEDIUM |

### Password Change
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| S8 | Change password with valid inputs | Success, password updated | CRITICAL |
| S9 | New password < 6 chars | Error: "Too short" | HIGH |
| S10 | New password > 128 chars | Error: "Too long" | HIGH |
| S11 | New password = confirm password | Validation passes | HIGH |
| S12 | New password ≠ confirm password | Error: "Passwords don't match" | HIGH |
| S13 | Leave new password empty | Validation error | MEDIUM |
| S14 | Leave confirm password empty | Validation error | MEDIUM |
| S15 | Change password, network drops | Error, password not changed | HIGH |
| S16 | Change password successfully | Form resets, success message | MEDIUM |
| S17 | Rapid password changes (3 in 10s) | All processed or rate limited | LOW |

### Plan & Usage Display
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| S18 | Display current plan (Starter/Growth/Pro) | Correct plan shown | HIGH |
| S19 | Display credit balance | Accurate balance | CRITICAL |
| S20 | Display credits used this month | Accurate count | HIGH |
| S21 | Display next renewal date | Correct date for subscriptions | MEDIUM |
| S22 | One-time pack: no renewal date | Shows "N/A" or hidden | LOW |
| S23 | Usage at 80% → warning indicator | Red/warning color | MEDIUM |
| S24 | Usage at 100% → indicator | Clearly shows limit reached | HIGH |

### External Links
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| S25 | Tap "Upgrade Plan" | Opens pricing URL in browser | HIGH |
| S26 | Tap "Billing Portal" | Opens Stripe portal | HIGH |
| S27 | Tap "Terms of Service" | Opens terms page | LOW |
| S28 | Tap "Privacy Policy" | Opens privacy page | LOW |
| S29 | Sign out button | Confirms, then signs out | CRITICAL |

---

## CATEGORY 8: STATE MANAGEMENT (20 tests)

### Auth Store (Zustand)
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| ST1 | Sign in updates authStore.session | Session stored | CRITICAL |
| ST2 | Sign in updates authStore.user | User data stored | CRITICAL |
| ST3 | Sign out clears authStore | Session and user null | CRITICAL |
| ST4 | Token refresh updates authStore | New token stored | HIGH |
| ST5 | Concurrent auth actions | State remains consistent | HIGH |

### Upload Store (Zustand)
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| ST6 | addFiles() adds to uploadStore.files | Files stored | CRITICAL |
| ST7 | removeFile() removes from uploadStore.files | File removed | HIGH |
| ST8 | clearFiles() empties uploadStore.files | All files cleared | HIGH |
| ST9 | setStyle() updates uploadStore.style | Style stored | MEDIUM |
| ST10 | setFormat() updates uploadStore.format | Format stored | MEDIUM |
| ST11 | setVariations() updates uploadStore.variations | Variations stored | MEDIUM |
| ST12 | toggleEnhancement() toggles in array | Enhancement toggled | MEDIUM |
| ST13 | Multiple rapid store updates | No race condition, final state correct | HIGH |

### UI Store (Zustand)
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| ST14 | setGalleryFilter() updates filter | Filter stored | HIGH |
| ST15 | setGallerySort() updates sort | Sort stored | HIGH |
| ST16 | Multiple rapid UI updates | State consistent | MEDIUM |

### React Query Cache
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| ST17 | Upload invalidates usage cache | Usage refetched | CRITICAL |
| ST18 | Delete item invalidates gallery cache | Gallery refetched | CRITICAL |
| ST19 | Profile update invalidates profile cache | Profile refetched | HIGH |
| ST20 | Concurrent mutations invalidate correctly | All caches updated properly | HIGH |

---

## CATEGORY 9: API INTEGRATION (25 tests)

### Network Conditions
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| API1 | All APIs work on good network | Success | CRITICAL |
| API2 | API call on slow 3G network | Completes or times out gracefully | HIGH |
| API3 | API call on 2G network | Times out with error | MEDIUM |
| API4 | API call with no internet | Offline error immediately | CRITICAL |
| API5 | Network drops mid-request | Request fails, error shown | HIGH |
| API6 | Network reconnects after drop | Auto-retry or user can retry | HIGH |

### HTTP Status Codes
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| API7 | 200 OK response | Success | CRITICAL |
| API8 | 201 Created response | Success | HIGH |
| API9 | 400 Bad Request | Error shown, no retry | HIGH |
| API10 | 401 Unauthorized | Redirect to login or refresh token | CRITICAL |
| API11 | 403 Forbidden | Error shown, no retry | HIGH |
| API12 | 404 Not Found | Error shown, no retry | HIGH |
| API13 | 422 Validation Error | Error shown, no retry | HIGH |
| API14 | 429 Rate Limited | Error shown or auto-retry after delay | HIGH |
| API15 | 500 Internal Server Error | Error shown, retry up to 3 times | HIGH |
| API16 | 502 Bad Gateway | Error shown, retry | MEDIUM |
| API17 | 503 Service Unavailable | Error shown, retry | MEDIUM |
| API18 | Network timeout (no response) | Timeout error, can retry | HIGH |

### Retry Logic
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| API19 | 500 error → retry 3 times | Retries, then fails | HIGH |
| API20 | 401 error → no retry | Immediate failure | CRITICAL |
| API21 | Network error → retry 3 times | Retries network errors | HIGH |
| API22 | Successful retry on 2nd attempt | Success after retry | HIGH |

### Concurrent API Calls
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| API23 | 5 API calls simultaneously | All complete independently | HIGH |
| API24 | Upload while fetching gallery | Both succeed | HIGH |
| API25 | Delete while polling queue | Both succeed, queue updates | HIGH |

---

## CATEGORY 10: PERFORMANCE & MEMORY (20 tests)

### App Performance
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| P1 | App launch time (cold start) | < 3 seconds | HIGH |
| P2 | App launch time (warm start) | < 1 second | MEDIUM |
| P3 | Screen transition time | < 300ms | MEDIUM |
| P4 | FlatList scroll performance (60fps) | Smooth scrolling, no jank | HIGH |
| P5 | Image rendering performance | No lag on high-res images | MEDIUM |

### Memory Management
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| P6 | Memory usage at idle | Baseline stable | MEDIUM |
| P7 | Memory after loading 100 gallery items | No excessive growth | HIGH |
| P8 | Memory after playing 10 videos | Videos unloaded properly | CRITICAL |
| P9 | Memory after 1 hour of use | No continuous growth (leak) | CRITICAL |
| P10 | Memory after uploading 50 photos | Photos released after upload | HIGH |

### Battery Usage
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| P11 | Battery drain at idle | Minimal drain | MEDIUM |
| P12 | Battery drain while polling queue | Acceptable drain | MEDIUM |
| P13 | Battery drain while playing videos | Expected high drain | LOW |
| P14 | Battery drain in background | Minimal to none | HIGH |

### Large Data Sets
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| P15 | Load gallery with 1000 items | Works, may be slow | HIGH |
| P16 | Scroll through 1000 gallery items | Smooth with windowing | HIGH |
| P17 | Queue with 100 jobs | All displayed efficiently | MEDIUM |
| P18 | Upload 10 photos simultaneously | All upload without crash | HIGH |

### Background Behavior
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| P19 | App to background during upload | Upload continues or pauses cleanly | HIGH |
| P20 | App to background for 10 minutes | State persists on resume | HIGH |

---

## CATEGORY 11: UI/UX & ACCESSIBILITY (20 tests)

### Visual Elements
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| UI1 | All screens render correctly | No visual bugs | HIGH |
| UI2 | Safe area insets on iPhone notch | Content not clipped | HIGH |
| UI3 | Safe area insets on Android hole-punch | Content not clipped | MEDIUM |
| UI4 | Status bar color matches theme | Consistent look | LOW |
| UI5 | Tab bar visible on all tabs | Always present | MEDIUM |
| UI6 | Tab bar highlight on active tab | Correct tab highlighted | LOW |

### Responsive Layout
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| UI7 | App on iPhone SE (small screen) | Layout adapts | HIGH |
| UI8 | App on iPhone 15 Pro Max (large screen) | Layout uses space well | MEDIUM |
| UI9 | App on iPad (tablet) | Layout adapts or shows phone layout | LOW |
| UI10 | Rotate to landscape | Layout adapts or locked to portrait | MEDIUM |

### Touch Targets
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| UI11 | All buttons have min 44×44pt touch area | Easy to tap | MEDIUM |
| UI12 | Buttons don't overlap or too close | No accidental taps | MEDIUM |

### Loading & Empty States
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| UI13 | Loading state shows spinner | User knows something is happening | HIGH |
| UI14 | Empty state shows helpful message | User knows what to do | MEDIUM |
| UI15 | Error state shows retry button | User can recover | HIGH |
| UI16 | Skeleton loaders (if implemented) | Smooth loading experience | LOW |

### Animations
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| UI17 | Screen transitions are smooth | No jank | MEDIUM |
| UI18 | Button press animations work | Haptic + visual feedback | LOW |
| UI19 | Scroll animations don't stutter | 60fps | MEDIUM |
| UI20 | Long-running animations can be interrupted | No stuck states | LOW |

---

## CATEGORY 12: PLATFORM-SPECIFIC (15 tests)

### iOS-Specific
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| PL1 | Test on iOS 16 | App works | HIGH |
| PL2 | Test on iOS 17 | App works | HIGH |
| PL3 | Test on iOS 18 | App works | CRITICAL |
| PL4 | Image picker permissions on iOS | Permission prompt shown | HIGH |
| PL5 | Camera permissions on iOS | Permission prompt shown | MEDIUM |
| PL6 | HEIC image format (iOS native) | Converted or handled | MEDIUM |
| PL7 | Haptic feedback on iOS | Works correctly | LOW |
| PL8 | Safe area on iPhone notch models | Content not clipped | HIGH |

### Android-Specific
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| PL9 | Test on Android 12 | App works | HIGH |
| PL10 | Test on Android 13 | App works | HIGH |
| PL11 | Test on Android 14 | App works | CRITICAL |
| PL12 | Image picker permissions on Android | Permission prompt shown | HIGH |
| PL13 | Back button behavior | Navigates or exits app | MEDIUM |
| PL14 | Haptic feedback on Android | Works correctly | LOW |
| PL15 | Safe area on hole-punch displays | Content not clipped | MEDIUM |

---

## CATEGORY 13: EDGE CASES & WEIRD SCENARIOS (25 tests)

### Timing & Concurrency
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| EC1 | Upload photo, delete it from gallery before completion | Handles gracefully | HIGH |
| EC2 | Cancel job while it's completing | Completion wins or cancel wins, no stuck state | HIGH |
| EC3 | Sign out while upload in progress | Upload cancelled cleanly | HIGH |
| EC4 | Sign out while polling queue | Polling stops | MEDIUM |
| EC5 | Change plan tier mid-upload | Credit calculation uses correct tier | CRITICAL |
| EC6 | Credits refunded while upload pending | Balance updates, upload still succeeds | HIGH |
| EC7 | Delete account while jobs in queue | Jobs cancelled or orphaned | MEDIUM |

### Data Corruption
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| EC8 | Corrupt AsyncStorage auth data | App resets auth, prompts login | HIGH |
| EC9 | Corrupt React Query cache | Cache invalidated, refetches | MEDIUM |
| EC10 | Invalid JSON in API response | Error handled, no crash | HIGH |
| EC11 | Missing required fields in API response | Default values or error | HIGH |

### Extreme User Behavior
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| EC12 | Tap same button 100 times rapidly | Debounced or guarded | HIGH |
| EC13 | Swipe gestures at extreme speed | Handled smoothly | MEDIUM |
| EC14 | Scroll FlatList at max speed | No crash, smooth windowing | MEDIUM |
| EC15 | Switch tabs 50 times in 10 seconds | No memory leak or crash | MEDIUM |

### Long-Running Operations
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| EC16 | Leave app open for 24 hours | No crash, no memory leak | HIGH |
| EC17 | Poll queue for 2 hours straight | No crash, no excessive battery drain | MEDIUM |
| EC18 | Video generation takes 30 minutes | Polling continues, status updates | MEDIUM |

### Boundary Values
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| EC19 | Upload exactly 0 files | Error or disabled button | HIGH |
| EC20 | Upload exactly MAX files | Success | HIGH |
| EC21 | Upload exactly MAX + 1 files | Error or silent ignore | HIGH |
| EC22 | Password exactly 6 chars | Success (minimum) | MEDIUM |
| EC23 | Password exactly 128 chars | Success (maximum) | MEDIUM |
| EC24 | Credits exactly 0 | Can't upload | CRITICAL |
| EC25 | Credits exactly INT_MAX | Displays correctly, no overflow | LOW |

---

## CATEGORY 14: OFFLINE BEHAVIOR (15 tests)

### Offline Detection
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| OFF1 | Go offline, banner appears | Red "You're offline" banner | CRITICAL |
| OFF2 | Come back online, banner updates | Green "Back online" for 3s | HIGH |
| OFF3 | Already offline on app launch | Banner shows immediately | HIGH |
| OFF4 | Offline banner doesn't block UI | UI still usable (cached data) | MEDIUM |

### Cached Data Access
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| OFF5 | View cached gallery items offline | Items visible | HIGH |
| OFF6 | View cached usage stats offline | Stats visible | MEDIUM |
| OFF7 | View cached profile offline | Profile visible | MEDIUM |

### Offline Actions
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| OFF8 | Try to upload photo offline | Error: "No internet connection" | CRITICAL |
| OFF9 | Try to delete gallery item offline | Error or queued for when online | HIGH |
| OFF10 | Try to refresh data offline | Error or silent fail | MEDIUM |
| OFF11 | Try to change password offline | Error: "No internet connection" | HIGH |

### Reconnection Behavior
| ID | Test Case | Expected Result | Severity |
|----|-----------|----------------|----------|
| OFF12 | Offline, then online → auto-retry failed request | Request retries automatically | HIGH |
| OFF13 | Offline, then online → refresh stale data | Data refetches | MEDIUM |
| OFF14 | Offline for 1 hour, then online | Session still valid or refreshes | HIGH |
| OFF15 | Offline, upload queued, then online | Upload starts automatically | MEDIUM |

---

## 🎯 SUMMARY

### Total Test Cases: **150+**

| Category | Tests |
|----------|-------|
| Authentication & Session | 20 |
| Enhance Screen | 40 |
| Video Screen | 20 |
| Gallery Screen | 38 |
| Queue Screen | 20 |
| Explore Screen | 20 |
| Settings Screen | 29 |
| State Management | 20 |
| API Integration | 25 |
| Performance & Memory | 20 |
| UI/UX & Accessibility | 20 |
| Platform-Specific | 15 |
| Edge Cases | 25 |
| Offline Behavior | 15 |
| **TOTAL** | **327** |

### Severity Breakdown
- 🔴 **CRITICAL:** 50+ tests
- 🟡 **HIGH:** 100+ tests
- 🟠 **MEDIUM:** 100+ tests
- 🟢 **LOW:** 77+ tests

---

## 📊 EXECUTION STRATEGY

### Phase 1: Critical Path (Day 1)
Focus on CRITICAL severity tests that would prevent app from functioning.

### Phase 2: High Priority (Day 2-3)
Execute HIGH severity tests that affect core features.

### Phase 3: Medium Priority (Day 4-5)
Execute MEDIUM severity tests for edge cases and UX issues.

### Phase 4: Low Priority (Day 6)
Execute LOW priority tests for polish and minor issues.

### Phase 5: Regression (Day 7)
Re-run all CRITICAL and HIGH tests to ensure fixes didn't break anything.

---

**Test Plan Status:** Ready for Execution
**Estimated Execution Time:** 7-10 days with automated tooling, 2-3 weeks manual
**Next Step:** Begin systematic execution starting with CRITICAL tests
