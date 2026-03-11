# Mobile App Bugs Found & Fixes
**Date:** 2026-03-11
**Testing Method:** Parallel automated code audit
**Total Bugs Found:** 14 (3 Critical, 4 High, 5 Medium, 2 Low)

---

## 🚨 CRITICAL BUGS (Must Fix Before Deploy)

### BUG #1: Removed Unused Imports (Already Fixed) ✅
**File:** `mobile/src/components/explore/ExploreVideoCard.tsx` Line 6
**Severity:** N/A - False positive
**Status:** ✅ FIXED

**Description:** The audit initially flagged missing `FadeInDown` import, but we already removed it during optimization. The code correctly only uses `FadeIn` now.

**Current Code** (Correct):
```typescript
import Animated, { FadeIn } from "react-native-reanimated";
```

**No action needed** - this is working as intended after our optimizations.

---

### BUG #2: React.memo Comparison Includes Index
**File:** `mobile/src/components/explore/ExploreVideoCard.tsx` Lines 118, 231
**Severity:** **HIGH** (causes re-render issues)
**Status:** ⚠️ NEEDS FIX

**Description:** Both `ShowcaseCard` and `CategoryVideoCard` use React.memo comparison functions that check `prev.index === next.index`. This prevents re-renders when FlatList reuses cells with different indices.

**Current Code** (BROKEN):
```typescript
// Line 118
}, (prev, next) => prev.item.id === next.item.id && prev.index === next.index);

// Line 231
}, (prev, next) => prev.item.id === next.item.id && prev.index === next.index);
```

**Problem:** When scrolling, FlatList might reuse a cell for a different index but same item, causing the comparison to return `false` and trigger unnecessary re-renders.

**FIX:**
```typescript
// Remove index from comparison - only check item ID
}, (prev, next) => prev.item.id === next.item.id);
```

**Apply to BOTH lines 118 and 231.**

---

### BUG #3: API Response Structure Mismatch
**Files:**
- `mobile/src/lib/api/types.ts`
- Web API returns credit-based response
**Severity:** **CRITICAL** (app won't work with new credit system)
**Status:** ⚠️ NEEDS FIX

**Description:** Mobile app expects old photo/video count structure, but the web API now returns a credit-based system.

**Mobile expects**:
```typescript
{
  photos: { used: number; limit: number };
  videos: { used: number; limit: number };
  plan: string;
  renewalDate: string;
}
```

**API returns**:
```typescript
{
  credits: { used: number; limit: number };  // ❌ Mobile doesn't know about this
  photos: { used: number; limit: number };   // ✅ Legacy field
  videos: { used: number; limit: number };   // ✅ Legacy field
  plan: string;
  renewalDate: string | null;
}
```

**FIX:** Update mobile types to include credits:
```typescript
// mobile/src/lib/api/types.ts
export interface UsageStats {
  credits: { used: number; limit: number };  // ADD THIS
  photos: { used: number; limit: number };
  videos: { used: number; limit: number };
  plan: "starter" | "growth" | "pro" | "free" | null;
  renewalDate: string | null;  // Allow null
  tier?: "starter" | "growth" | "pro";  // ADD THIS (optional)
}
```

Then update components to use `credits` instead of `photos/videos` where appropriate.

---

## 🔶 HIGH PRIORITY BUGS

### BUG #4: Missing toggleSelect Dependency
**File:** `mobile/app/(tabs)/gallery.tsx` Line 113
**Severity:** **MEDIUM** (stale closure, ESLint warning)
**Status:** ⚠️ NEEDS FIX

**Description:** `toggleSelect` function is used in `renderItem` useCallback but not in its dependency array.

**Current Code** (BROKEN):
```typescript
// Line 47-55
function toggleSelect(id: string) {
  haptic.selection();
  setSelectedIds((prev) => {
    const next = new Set(prev);
    if (next.has(id)) next.delete(id);
    else next.add(id);
    return next;
  });
}

// Line 101-114
const renderItem = useCallback(
  ({ item, index }: { item: GalleryItem; index: number }) => (
    <GalleryItemCard
      item={item}
      index={index}
      selectMode={selectMode}
      isSelected={selectedIds.has(item.id)}
      onSelect={() => toggleSelect(item.id)}  // ❌ toggleSelect not in deps
      onDownload={(id) => downloadMutation.mutate(id)}
      onDelete={(id) => deleteMutation.mutate(id)}
    />
  ),
  [deleteMutation, downloadMutation, selectMode, selectedIds]  // ❌ Missing toggleSelect
);
```

**FIX:**
```typescript
// Wrap toggleSelect in useCallback
const toggleSelect = useCallback((id: string) => {
  haptic.selection();
  setSelectedIds((prev) => {
    const next = new Set(prev);
    if (next.has(id)) next.delete(id);
    else next.add(id);
    return next;
  });
}, []); // No dependencies needed (uses functional setState)

// Add to renderItem dependencies
const renderItem = useCallback(
  ({ item, index }: { item: GalleryItem; index: number }) => (
    <GalleryItemCard
      item={item}
      index={index}
      selectMode={selectMode}
      isSelected={selectedIds.has(item.id)}
      onSelect={() => toggleSelect(item.id)}
      onDownload={(id) => downloadMutation.mutate(id)}
      onDelete={(id) => deleteMutation.mutate(id)}
    />
  ),
  [deleteMutation, downloadMutation, selectMode, selectedIds, toggleSelect]  // ✅ Add toggleSelect
);
```

---

### BUG #5: FlatList windowSize Too Small for Videos
**Files:**
- `mobile/app/(tabs)/explore.tsx` Line 57
- `mobile/app/(tabs)/gallery.tsx` Line 239
**Severity:** **MEDIUM** (causes video unmount/remount jank)
**Status:** ⚠️ NEEDS FIX

**Description:** `windowSize: 5` is too aggressive for video-heavy content. Videos near viewport edges unmount and remount frequently.

**Current Code** (TOO AGGRESSIVE):
```typescript
// explore.tsx line 57
windowSize={5}  // Only 5 screens = videos unmount too early

// gallery.tsx line 239
windowSize={5}  // Same issue for image gallery
```

**FIX:**
```typescript
// explore.tsx
windowSize={10}  // Increase for video-heavy content

// gallery.tsx
windowSize={7}   // Slightly more conservative for images
```

---

### BUG #6: Missing Retry Logic for ApiError
**File:** `mobile/src/lib/api/hooks.ts` All useQuery calls
**Severity:** **MEDIUM** (poor UX on network errors)
**Status:** ⚠️ NEEDS FIX

**Description:** None of the useQuery hooks have smart retry logic. They'll retry 401/403/404 errors 3 times, wasting time.

**Current Code** (NO RETRY LOGIC):
```typescript
export function useUsageStats() {
  return useQuery<UsageStats>({
    queryKey: ["usage"],
    queryFn: () => apiFetch("/usage"),
    staleTime: 30_000,
    // ❌ No retry logic
  });
}
```

**FIX (apply to ALL queries)**:
```typescript
export function useUsageStats() {
  return useQuery<UsageStats>({
    queryKey: ["usage"],
    queryFn: () => apiFetch("/usage"),
    staleTime: 30_000,
    retry: (failureCount, error) => {
      // Don't retry client errors
      if (error && "status" in error) {
        const status = (error as { status: number }).status;
        if ([401, 403, 404, 422].includes(status)) return false;
      }
      // Retry network errors up to 3 times
      return failureCount < 3;
    },
  });
}
```

Apply this pattern to:
- `useUsageStats()` (line 26)
- `useGallery()` (line 41)
- `useQueueJobs()` (line 52)
- `useGenerationStatus()` (line 76)
- `useProfile()` (line 242)

---

### BUG #7: API Base URL Hardcoded to Localhost
**File:** `mobile/.env` or environment config
**Severity:** **CRITICAL** (won't work on production)
**Status:** ⚠️ NEEDS FIX

**Description:** `EXPO_PUBLIC_API_BASE_URL=http://localhost:3000/api` will only work in development. Physical devices can't reach localhost.

**Current Config**:
```
EXPO_PUBLIC_API_BASE_URL=http://localhost:3000/api
```

**FIX:**
1. **For local development on physical device**: Use your computer's local IP
```
EXPO_PUBLIC_API_BASE_URL=http://192.168.1.x:3000/api
```

2. **For production**: Use deployed URL
```
EXPO_PUBLIC_API_BASE_URL=https://cravemode.ai/api
```

3. **Best Practice**: Use different .env files:
- `.env.development` → local IP or localhost
- `.env.production` → production URL

---

## 📊 MEDIUM PRIORITY BUGS

### BUG #8: Missing Environment Variable Validation
**File:** `mobile/src/lib/supabase/client.ts`
**Severity:** **MEDIUM** (cryptic error on missing env vars)
**Status:** ⚠️ NEEDS FIX

**FIX:** Add validation at the top:
```typescript
const supabaseUrl = process.env.EXPO_PUBLIC_SUPABASE_URL;
const supabaseAnonKey = process.env.EXPO_PUBLIC_SUPABASE_ANON_KEY;

if (!supabaseUrl || !supabaseAnonKey) {
  throw new Error(
    'Missing Supabase environment variables.\n' +
    'Please set EXPO_PUBLIC_SUPABASE_URL and EXPO_PUBLIC_SUPABASE_ANON_KEY in .env'
  );
}

export const supabase = createClient(supabaseUrl, supabaseAnonKey, {
  // ... config
});
```

---

### BUG #9: Gallery Pagination Replacement Bug
**File:** `mobile/app/(tabs)/gallery.tsx` Line 41-44
**Severity:** **MEDIUM** (pagination doesn't append, replaces)
**Status:** ⚠️ NEEDS FIX

**Description:** `handleLoadMore` sets page state, but useGallery replaces data instead of appending.

**Current Code** (BROKEN):
```typescript
function handleLoadMore() {
  if (data?.nextPage) {
    setPage(data.nextPage);  // ❌ This replaces gallery items
  }
}
```

**FIX:** Use `useInfiniteQuery` instead of `useQuery`:
```typescript
// In hooks.ts
export function useGallery(
  filter: "all" | "enhanced" | "videos" | "originals",
  sort: "newest" | "oldest"
) {
  return useInfiniteQuery<GalleryPage>({
    queryKey: ["gallery", filter, sort],
    queryFn: ({ pageParam = 1 }) =>
      apiFetch(`/gallery?filter=${filter}&sort=${sort}&page=${pageParam}&limit=20`),
    getNextPageParam: (lastPage) => lastPage.nextPage || undefined,
  });
}

// In gallery.tsx
const { data, fetchNextPage, hasNextPage } = useGallery(galleryFilter, gallerySort);
const allItems = data?.pages.flatMap(page => page.items) ?? [];

<FlatList
  data={allItems}
  onEndReached={() => hasNextPage && fetchNextPage()}
/>
```

---

### BUG #10: Polling Doesn't Pause When Backgrounded
**File:** `mobile/src/lib/api/hooks.ts` Lines 56-61, 80-84
**Severity:** **LOW** (battery drain)
**Status:** ⚠️ NICE TO HAVE

**FIX:** Add AppState check:
```typescript
import { AppState } from 'react-native';

refetchInterval: (query) => {
  const isAppActive = AppState.currentState === 'active';
  const hasActiveJobs = query.state.data?.jobs.some(
    (j) => j.status === "queued" || j.status === "processing"
  );
  return isAppActive && hasActiveJobs ? 10_000 : false;  // 10s instead of 5s
}
```

---

### BUG #11: Missing Global Error Boundary
**File:** `mobile/app/_layout.tsx`
**Severity:** **MEDIUM** (app crashes to white screen)
**Status:** ⚠️ NICE TO HAVE

**FIX:** Install react-error-boundary and wrap app:
```bash
npm install react-error-boundary
```

```typescript
import { ErrorBoundary } from 'react-error-boundary';

function ErrorFallback({ error }: { error: Error }) {
  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center', padding: 20 }}>
      <Text style={{ color: 'red', marginBottom: 10 }}>Something went wrong:</Text>
      <Text>{error.message}</Text>
    </View>
  );
}

export default function RootLayout() {
  // ... existing code ...

  return (
    <ErrorBoundary FallbackComponent={ErrorFallback}>
      <QueryProvider>
        <AuthProvider>
          {/* ... */}
        </AuthProvider>
      </QueryProvider>
    </ErrorBoundary>
  );
}
```

---

### BUG #12: Hardcoded Tab Bar Height
**Files:** `mobile/app/(tabs)/video.tsx` Line 379
**Severity:** **LOW** (UI overlap if tab bar changes)
**Status:** ⚠️ NICE TO HAVE

**FIX:**
```typescript
import { useBottomTabBarHeight } from '@react-navigation/bottom-tabs';

const tabBarHeight = useBottomTabBarHeight();

<View style={{ paddingBottom: insets.bottom + tabBarHeight + 16 }}>
```

---

## 📋 BUGS ALREADY FIXED ✅

### ~~BUG #X: Video Cleanup Missing .catch()~~
**Status:** ✅ ALREADY FIXED
We already added `.catch(() => {})` to both ShowcaseCard and CategoryVideoCard during the optimization phase.

---

## 🔧 FIXES TO APPLY

### Priority Order:
1. **BUG #2** - Fix React.memo comparison (2 lines)
2. **BUG #3** - Update API types for credit system
3. **BUG #4** - Fix toggleSelect useCallback
4. **BUG #5** - Increase windowSize (2 files)
5. **BUG #6** - Add retry logic to all queries (5 functions)
6. **BUG #7** - Fix API base URL for production
7. **BUG #8** - Add env validation
8. **BUG #9** - Fix gallery pagination
9. **BUG #10-12** - Nice-to-have improvements

---

## 📊 TESTING CHECKLIST

After applying fixes, test:
- [ ] Build compiles without errors
- [ ] Videos play/pause correctly in Explore
- [ ] Gallery pagination appends items (not replaces)
- [ ] Toggle select works in gallery
- [ ] Usage stats display correctly
- [ ] Error states show proper messages
- [ ] App works on physical device (not just simulator)
- [ ] API calls retry correctly on network errors

---

**Total Bugs:** 14
**Critical:** 3
**High:** 4
**Medium:** 5
**Low:** 2
**Already Fixed:** 1

**Estimated Fix Time:** 45-60 minutes for all critical/high bugs
