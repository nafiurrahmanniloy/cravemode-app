# Mobile UX Research Findings — Food Photography & Photo Editing Apps

## Executive Summary

This research analyzes the mobile UX patterns from industry-leading photo editing, food photography, and gallery apps to identify concrete, implementable patterns for a 10/10 mobile experience. All patterns include specific CSS/JS values and technical implementation details.

---

## 1. VSCO — Minimalist Editing Flow

### Key UX Characteristics

**Minimalist Interface Philosophy:**
- Static translucent bottom tab bar (rgba opacity ~0.85-0.95)
- Black highlighting on active tab (#000), lighter gray on inactive tabs (#666-#888)
- Maximum screen real estate dedicated to image preview
- All editing controls hidden until tapped

**Gesture-Based Editing:**
- Vertical swipe: Switch between different adjustment types (exposure, contrast, saturation)
- Horizontal swipe: Adjust selected parameter value (-100 to +100 range)
- Double-tap: Reset individual adjustment to 0
- Pinch: Zoom into image for detail inspection

**Animation Specifications:**
- Fade animations: `transition: opacity 200ms ease-out`
- Slide animations: `transition: transform 300ms cubic-bezier(0.4, 0.0, 0.2, 1)`
- Tab switching: 150ms fade with 50ms stagger between elements

**Filter Application:**
- Live preview as you swipe through filters (no "apply" needed)
- Filter strength slider appears on long-press
- "Recipe" saves: One-tap to apply saved preset combinations
- Smooth crossfade between filters: 180ms duration

### Implementation Values

```css
/* VSCO-style bottom tab bar */
.tab-bar {
  position: fixed;
  bottom: 0;
  width: 100%;
  height: 64px;
  background: rgba(0, 0, 0, 0.9);
  backdrop-filter: blur(20px);
  display: flex;
  justify-content: space-around;
  padding: 0 env(safe-area-inset-right) env(safe-area-inset-bottom) env(safe-area-inset-left);
}

/* Active tab indicator */
.tab-item.active {
  color: #fff;
  border-bottom: 2px solid #fff;
}

.tab-item {
  color: rgba(255, 255, 255, 0.6);
  transition: color 150ms ease-out, border-color 150ms ease-out;
}
```

**Sources:**
- [VSCO: a UX and Usability Case Study](https://medium.com/@tylerameylegault/vsco-a-ux-and-usability-case-study-45244fad7027)
- [A Critique of the User Interface and Experience of VSCO](https://medium.com/nyc-design/a-critique-of-the-user-interface-and-experience-of-vsco-204880e00035)
- [VSCO Features: Editing Photos & Videos](https://www.vsco.co/features)

---

## 2. Foodie (LINE) — Premium Food Photography

### Core Features

**Live Filter System:**
- 30+ professional filters optimized specifically for food
- Real-time preview (60fps camera feed with filter applied)
- Filter thumbnails show actual preview of current frame (not generic samples)
- Horizontal carousel with momentum scrolling

**Smart Angle Guide:**
- Overhead mode: Digital level indicator (green when level)
- 45-degree mode: Angle guide overlay appears at optimal dish angle
- Haptic feedback when reaching optimal angle (if supported)

**Photography Effects:**
- Auto background blur (depth-of-field simulation)
- Brightness adjustment: Vertical swipe on screen (up = brighter, down = darker)
- Flash control: Toggle in top-right corner with subtle glow animation

**Custom "Recipe" System:**
- Save complete editing formulas (filter + all adjustments)
- Share recipes as codes with other users
- Apply recipes with single tap

### Animation Specifications

```css
/* Foodie-style filter carousel */
.filter-carousel {
  display: flex;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  -webkit-overflow-scrolling: touch;
  gap: 12px;
  padding: 16px;
}

.filter-item {
  scroll-snap-align: center;
  min-width: 72px;
  height: 72px;
  border-radius: 8px;
  border: 2px solid transparent;
  transition: border-color 200ms ease, transform 150ms ease;
}

.filter-item.active {
  border-color: #FF6B6B; /* Foodie brand color */
  transform: scale(1.1);
}
```

**Touch Target Sizing:**
- Filter thumbnails: 72x72px visible, 88x88px tap target (padding)
- Camera shutter button: 80px diameter, 96px tap target
- Mode toggles: 44x44px minimum

**Sources:**
- [10 Best Food Photography Apps for Stunning Results](https://foodshot.ai/blog/best-food-photography-apps)
- [Foodie - Filter & Film Camera - Google Play](https://play.google.com/store/apps/details?id=com.linecorp.foodcam.android&hl=en_US)
- [Introducing "Foodie" Dedicated Camera App for Food Photos](https://www.linecorp.com/en/pr/news/en/2016/1236)

---

## 3. Snapseed — Gesture-Based Editing

### Revolutionary Gesture System

**Core Gestures:**
1. **Vertical swipe:** Cycle through adjustment types (Brightness → Contrast → Saturation → etc.)
2. **Horizontal swipe:** Adjust selected parameter value
3. **Pinch:** Zoom for detail inspection
4. **Two-finger swipe up/down:** Show/hide before-after comparison
5. **Long-press:** Show original (release to return to edit)

**Selective Editing:**
- Tap object/area to select (U Point technology)
- AI detects and selects complete object in <20ms
- Object Brush: Draw stroke on object, then adjust independently
- Multiple control points: Each with independent adjustments

**Performance:**
- Object detection: <20ms response time
- Gesture recognition: <16ms (60fps requirement)
- Parameter adjustment: Real-time preview (no lag)

### Implementation Details

```javascript
// Snapseed-style gesture handling
let currentTool = 'brightness';
let toolValue = 0;
let startY = 0;
let startX = 0;

element.addEventListener('touchstart', (e) => {
  startY = e.touches[0].clientY;
  startX = e.touches[0].clientX;
});

element.addEventListener('touchmove', (e) => {
  const deltaY = e.touches[0].clientY - startY;
  const deltaX = e.touches[0].clientX - startX;

  // Vertical: Change tool (minimum 40px movement to switch)
  if (Math.abs(deltaY) > 40 && Math.abs(deltaY) > Math.abs(deltaX)) {
    const toolIndex = Math.floor(deltaY / 60);
    cycleTool(toolIndex);
    startY = e.touches[0].clientY; // Reset for next tool switch
  }

  // Horizontal: Adjust value
  if (Math.abs(deltaX) > Math.abs(deltaY)) {
    toolValue = Math.max(-100, Math.min(100, deltaX / 3));
    applyAdjustment(currentTool, toolValue);
  }
});

// Before/After comparison (two-finger swipe)
let touchCount = 0;
element.addEventListener('touchstart', (e) => {
  touchCount = e.touches.length;
  if (touchCount === 2) {
    showOriginal();
  }
});

element.addEventListener('touchend', () => {
  if (touchCount === 2) {
    showEdited();
  }
});
```

**Visual Feedback:**
- Tool indicator appears at top: `transition: opacity 200ms, transform 200ms`
- Value bar appears at bottom: slides in from bottom with `transform: translateY(0)`
- Haptic feedback on tool switch (if supported): `navigator.vibrate(10)`

**Sources:**
- [UX Case Study: Snapseed — Photography App](https://medium.com/@tkxinggg/ux-case-study-snapseed-photography-app-473edf02be34)
- [Analysing Snapseed from a Mobile Design perspective](https://danielleklaasen.medium.com/analysing-snapseed-from-a-mobile-design-perspective-47f76adb3c1b)
- [Introducing interactive on-device segmentation in Snapseed](https://research.google/blog/introducing-interactive-on-device-segmentation-in-snapseed/)

---

## 4. Instagram — Gallery Grid & Image Viewer

### Gallery Grid Pattern

**Grid Specifications:**
- 3-column grid (mobile portrait)
- 1px gap between images (or 2px for higher density)
- Square aspect ratio (1:1) forced on all images
- Infinite scroll with Intersection Observer

**Grid Implementation:**

```css
/* Instagram-style gallery grid */
.gallery-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1px;
  background: #000; /* Gap color */
}

.gallery-item {
  aspect-ratio: 1 / 1;
  overflow: hidden;
  position: relative;
}

.gallery-item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

/* Loading shimmer */
.gallery-item.loading {
  background: linear-gradient(
    90deg,
    #262626 0%,
    #3a3a3a 50%,
    #262626 100%
  );
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
}

@keyframes shimmer {
  0% { background-position: -200% 0; }
  100% { background-position: 200% 0; }
}
```

**Infinite Scroll Pattern:**

```javascript
// Intersection Observer for lazy loading
const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        loadMoreImages();
        // Load next batch when within 2 viewports of bottom
      }
    });
  },
  {
    rootMargin: '200% 0px', // Load early (2 viewports ahead)
    threshold: 0
  }
);

// Observe sentinel element at end of grid
observer.observe(document.querySelector('.load-more-sentinel'));
```

### Full-Screen Image Viewer

**Entry/Exit Animations:**
- Tap image: Scale from grid position to full-screen (300ms spring animation)
- Exit: Scale back to grid position OR swipe down to dismiss
- Background fades from transparent to black: `transition: background 300ms ease`

**Viewer Gestures:**
- Horizontal swipe: Navigate between images (card-stack pattern)
- Pinch: Zoom into image (2x to 5x range)
- Double-tap: Quick zoom to 2x at tap point
- Swipe down: Dismiss viewer (with elastic resistance)

**Spring Animation Values:**

```javascript
// Instagram-style spring animation for image viewer
const spring = {
  type: 'spring',
  stiffness: 300,
  damping: 30,
  mass: 0.8
};

// In Framer Motion:
<motion.div
  initial={{ scale: 0.8, opacity: 0 }}
  animate={{ scale: 1, opacity: 1 }}
  exit={{ scale: 0.8, opacity: 0 }}
  transition={spring}
/>
```

**Sources:**
- [Progressive Web App Examples: 50 PWAs Across Every Industry](https://www.mobiloud.com/blog/progressive-web-app-examples)
- [9 Mobile App Design Trends for 2026](https://uxpilot.ai/blogs/mobile-app-design-trends)

---

## 5. Pinterest — PWA Excellence

### Performance Optimizations

**Bundle Size Reduction:**
- Core bundle: 150KB (down from 650KB)
- Code splitting by route
- Tree-shaking unused code
- Lazy-load images and components

**Loading Performance:**
- First paint: 1.8s (down from 4.2s)
- Time to Interactive: <6s
- App shell loads first, then dynamic content

**App Shell Pattern:**

```javascript
// Service worker caching strategy
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open('app-shell-v1').then((cache) => {
      return cache.addAll([
        '/',
        '/styles/main.css',
        '/scripts/app.js',
        '/images/logo.svg'
      ]);
    })
  );
});

// Cache-first strategy for shell, network-first for content
self.addEventListener('fetch', (event) => {
  if (event.request.url.includes('/api/')) {
    // Network first for dynamic content
    event.respondWith(
      fetch(event.request)
        .catch(() => caches.match(event.request))
    );
  } else {
    // Cache first for shell
    event.respondWith(
      caches.match(event.request)
        .then((response) => response || fetch(event.request))
    );
  }
});
```

### Micro-Interactions

**CSS Grid Masonry Layout:**
- Uses CSS Grid with auto-flow: dense
- Dynamic heights based on image aspect ratio
- Smooth repositioning on window resize

**Heart Animation (Like Button):**

```css
/* Pinterest-style heart explosion */
@keyframes heart-pop {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.3);
  }
  100% {
    transform: scale(1);
  }
}

.like-button.liked .heart {
  animation: heart-pop 300ms cubic-bezier(0.4, 0.0, 0.2, 1);
  color: #E60023; /* Pinterest red */
}

/* Particle burst effect */
@keyframes particle-burst {
  0% {
    transform: translate(0, 0) scale(1);
    opacity: 1;
  }
  100% {
    transform: translate(var(--tx), var(--ty)) scale(0);
    opacity: 0;
  }
}
```

**Smooth Scroll Transitions:**
- Page transitions: 250ms ease-out
- Scroll-triggered animations use Intersection Observer (not scroll events)
- 60fps maintained during scroll

**Sources:**
- [Pinterest PWA: Boosting Mobile Performance](https://www.tigren.com/blog/pinterest-pwa/)
- [A Pinterest Progressive Web App Performance Case Study](https://medium.com/dev-channel/a-pinterest-progressive-web-app-performance-case-study-3bd6ed2e6154)
- [The comprehensive guide to making your web app feel native](https://www.gfor.rest/blog/making-pwas-feel-native)

---

## 6. Adobe Lightroom Mobile — Professional Editing Controls

### Interface Layout

**Bottom-Anchored Controls:**
- Editing tools docked at bottom (above safe area)
- Can be dragged left/right to reposition without covering image
- Auto-hide after 3 seconds of inactivity (fade out 300ms)
- Single-finger drag to move entire menu panel

**Tool Organization:**
- Primary tools: Light, Color, Effects, Detail, Optics
- Each expands to show sub-controls (slide up animation 250ms)
- Scroll horizontally within expanded tool (momentum scrolling)

**Before/After Comparison:**

```javascript
// Lightroom-style before/after
const comparisonModes = {
  split: 'vertical-split',    // Draggable divider
  sideBySide: 'side-by-side', // Left = before, right = after
  tap: 'tap-to-toggle'        // Tap and hold to show before
};

// Long-press to show original
let longPressTimer;
imageElement.addEventListener('touchstart', () => {
  longPressTimer = setTimeout(() => {
    showOriginal();
    navigator.vibrate(20); // Haptic feedback
  }, 500);
});

imageElement.addEventListener('touchend', () => {
  clearTimeout(longPressTimer);
  showEdited();
});
```

### Slider Controls

**Precision Slider Pattern:**
- Horizontal drag: Normal adjustment (-100 to +100)
- Vertical drag while holding: Fine-tune mode (1/10th speed)
- Double-tap slider: Reset to 0
- Visual feedback: Value appears above thumb

```css
/* Lightroom-style precision slider */
.slider-container {
  position: relative;
  height: 44px; /* Touch target */
  padding: 12px 0;
}

.slider-track {
  height: 4px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 2px;
}

.slider-fill {
  height: 4px;
  background: #2680EB; /* Adobe blue */
  border-radius: 2px;
  transition: width 50ms linear;
}

.slider-thumb {
  width: 24px;
  height: 24px;
  border-radius: 12px;
  background: white;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
  position: absolute;
  top: 50%;
  transform: translate(-50%, -50%);
}

.slider-value {
  position: absolute;
  top: -30px;
  left: 50%;
  transform: translateX(-50%);
  background: rgba(0, 0, 0, 0.8);
  color: white;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
  opacity: 0;
  transition: opacity 200ms;
}

.slider-container.dragging .slider-value {
  opacity: 1;
}
```

### Export Flow

**Export Options:**
- Tap share icon → Bottom sheet slides up (300ms ease-out)
- Format selection: JPG, PNG, TIFF, DNG (radio buttons, 48px tall)
- Quality slider: 0-100% (JPG only)
- Dimension presets: Original, Large, Medium, Small (chips, 36px tall)
- Export button: Fixed at bottom, 56px tall, full-width

**Sources:**
- [4 Awesome Lightroom mobile Tips and Tricks](https://www.peachpit.com/articles/article.aspx?p=2246343)
- [Edit photos with Quick Actions in Lightroom on mobile](https://helpx.adobe.com/lightroom-cc/using/actions-lightroom-android.html)

---

## 7. DoorDash & Uber Eats — Food Photo Display

### Visual-First Design

**Photo Display Priorities:**
- Hero image: Full-width, 9:16 aspect ratio (fills mobile screen)
- Restaurant carousel: 16:9 thumbnails, horizontal scroll
- Menu items: 1:1 square thumbnails (consistency)
- All images use lazy loading (Intersection Observer)

**Engagement Statistics:**
- Restaurants with professional photos: +20-35% order volume
- Average order value increase: +15-25%
- 73% of customers want photos before ordering

### Card-Based Layout

**Restaurant Card Pattern:**

```css
/* DoorDash/Uber Eats restaurant card */
.restaurant-card {
  border-radius: 12px;
  overflow: hidden;
  background: white;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  transition: box-shadow 200ms, transform 200ms;
}

.restaurant-card:active {
  transform: scale(0.98);
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.12);
}

.restaurant-image {
  width: 100%;
  aspect-ratio: 16 / 9;
  object-fit: cover;
}

.restaurant-info {
  padding: 12px;
}

/* Skeleton loading for images */
.restaurant-image.loading {
  background: linear-gradient(
    90deg,
    #f0f0f0 0%,
    #f8f8f8 50%,
    #f0f0f0 100%
  );
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
}
```

### AI-Powered Personalization

**Dynamic Reordering:**
- User dietary preferences (vegetarian, gluten-free, etc.)
- Time of day (breakfast items in morning)
- Seasonal dishes (pumpkin in fall)
- Trending items in area
- Weather-based suggestions (soup on rainy days)

**Menu Photo Requirements (Uber Eats):**
- Minimum resolution: 1200x800px
- Aspect ratio: 3:2 or 16:9 preferred
- File size: <5MB
- Format: JPG or PNG
- Professional lighting required

**Sources:**
- [Top Food Delivery App Development Design Trends for 2025](https://beadaptify.com/blog/future-trends-in-food-delivery-app-development/)
- [Uber Eats US Photo Requirements 2026](https://www.menuphotoai.com/guides/uber-eats-us-photography)
- [Case Study: Enhance UX of food delivery app DoorDash](https://medium.com/design-bootcamp/case-study-enhance-ux-of-food-delivery-app-doordash-1824a5b46fd3)

---

## 8. Universal Mobile UX Patterns

### Touch Targets & Spacing

**Minimum Sizes (WCAG AAA + Platform Guidelines):**
- iOS: 44x44pt minimum for all controls
- Android: 48x48dp minimum (Material Design)
- Web (WCAG 2.1 AAA): 44x44px minimum
- Recommended: 48x48px for consistency across platforms

**Position-Based Variations:**
- Top of screen: 42px minimum (11mm physical)
- Bottom of screen: 46px minimum (12mm physical)
- Reason: Thumb reach and accidental tap prevention

**Spacing Between Targets:**
- Minimum: 8dp/px between interactive elements
- Recommended: 12-48px to prevent accidental taps
- Critical actions (delete, confirm): 48px spacing

**Visual vs. Touch Target:**
- Icon can be 24x24px visually
- Use padding to expand touch target to 44x44px
- All of the padded area should be tappable

```css
/* Proper touch target implementation */
.icon-button {
  width: 24px;
  height: 24px;
  padding: 10px; /* Expands to 44x44px total */
  cursor: pointer;
  background: transparent;
  border: none;
}

/* Alternative: Invisible pseudo-element */
.small-icon {
  width: 20px;
  height: 20px;
  position: relative;
}

.small-icon::before {
  content: '';
  position: absolute;
  top: -12px;
  left: -12px;
  right: -12px;
  bottom: -12px; /* Creates 44x44px touch area */
}
```

**Sources:**
- [Touch target size - Android Accessibility](https://support.google.com/accessibility/android/answer/7101858)
- [Mobile Accessibility Target Sizes Cheatsheet](https://smart-interface-design-patterns.com/articles/accessible-tap-target-sizes/)
- [Accessible Target Sizes Cheatsheet — Smashing Magazine](https://www.smashingmagazine.com/2023/04/accessible-tap-target-sizes-rage-taps-clicks/)

---

### Gesture Patterns

**Standard Gestures:**

1. **Tap:** Primary action (select, open)
   - Response time: <100ms
   - Visual feedback: Instant highlight/scale
   - Haptic: Optional 10ms vibration

2. **Double-Tap:** Secondary action (zoom, like)
   - Detection window: <300ms between taps
   - Cancel single-tap action if double-tap detected

3. **Long-Press:** Contextual menu or preview
   - Trigger time: 500ms
   - Haptic feedback: 20ms vibration at trigger
   - Visual: Subtle scale or glow at 250ms (halfway)

4. **Swipe:** Navigation or dismiss
   - Minimum velocity: 300px/s
   - Minimum distance: 40px
   - Direction lock: 15-degree threshold

5. **Pinch:** Zoom
   - Scale range: 0.5x to 5x typically
   - Smooth interpolation: Use transform, not width/height
   - Center point: Midpoint between fingers

**Gesture Implementation:**

```javascript
// Comprehensive gesture detection
class GestureDetector {
  constructor(element) {
    this.element = element;
    this.touches = [];
    this.startTime = 0;
    this.longPressTimer = null;

    this.bind();
  }

  bind() {
    this.element.addEventListener('touchstart', this.onTouchStart.bind(this));
    this.element.addEventListener('touchmove', this.onTouchMove.bind(this));
    this.element.addEventListener('touchend', this.onTouchEnd.bind(this));
  }

  onTouchStart(e) {
    this.touches = Array.from(e.touches);
    this.startTime = Date.now();
    this.startX = this.touches[0].clientX;
    this.startY = this.touches[0].clientY;

    // Long-press detection
    this.longPressTimer = setTimeout(() => {
      this.onLongPress(this.touches[0]);
      navigator.vibrate(20); // Haptic feedback
    }, 500);
  }

  onTouchMove(e) {
    clearTimeout(this.longPressTimer); // Cancel long-press
    this.touches = Array.from(e.touches);

    if (this.touches.length === 2) {
      this.onPinch(this.touches);
    } else if (this.touches.length === 1) {
      const deltaX = this.touches[0].clientX - this.startX;
      const deltaY = this.touches[0].clientY - this.startY;
      const distance = Math.sqrt(deltaX ** 2 + deltaY ** 2);

      if (distance > 40) {
        this.onSwipe(deltaX, deltaY);
      }
    }
  }

  onTouchEnd(e) {
    clearTimeout(this.longPressTimer);
    const duration = Date.now() - this.startTime;

    if (duration < 300 && this.touches.length === 1) {
      this.onTap(this.touches[0]);
    }
  }

  onTap(touch) {
    // Implement tap handler
    navigator.vibrate(10); // Light haptic
  }

  onLongPress(touch) {
    // Implement long-press handler
  }

  onSwipe(deltaX, deltaY) {
    const angle = Math.atan2(deltaY, deltaX) * (180 / Math.PI);

    if (Math.abs(angle) < 15) {
      this.onSwipeRight();
    } else if (Math.abs(angle - 180) < 15) {
      this.onSwipeLeft();
    } else if (angle > 75 && angle < 105) {
      this.onSwipeDown();
    } else if (angle > -105 && angle < -75) {
      this.onSwipeUp();
    }
  }

  onPinch(touches) {
    const distance = Math.sqrt(
      (touches[1].clientX - touches[0].clientX) ** 2 +
      (touches[1].clientY - touches[0].clientY) ** 2
    );

    if (!this.initialPinchDistance) {
      this.initialPinchDistance = distance;
    }

    const scale = distance / this.initialPinchDistance;
    this.element.style.transform = `scale(${scale})`;
  }
}
```

**Sources:**
- [The Role of Gestures in Mobile UX Design](https://sennalabs.com/blog/the-role-of-gestures-in-mobile-ux-design-simplifying-user-interaction)
- [In-App Gestures And Mobile App User Experience](https://www.smashingmagazine.com/2016/10/in-app-gestures-and-mobile-app-user-experience/)
- [Gestures - Patterns - Material Design](https://m1.material.io/patterns/gestures.html)

---

### Spring Animations

**Why Springs Over Easing:**
- More natural, physics-based motion
- Can accept initial velocity (from drag/swipe)
- Default in iOS/SwiftUI
- Better for interrupted animations (can reverse mid-motion)

**Spring Configuration:**

```javascript
// React Spring configuration
const springConfig = {
  tension: 300,    // Stiffness (higher = snappier)
  friction: 30,    // Damping (higher = less bouncy)
  mass: 0.8,       // Weight (higher = slower)
  velocity: 0      // Initial velocity from gesture
};

// CSS Spring Animation (using linear() function)
@keyframes spring-in {
  0% {
    transform: scale(0.8);
  }
  100% {
    transform: scale(1);
  }
}

.spring-element {
  animation: spring-in 400ms linear(
    0, 0.002, 0.01 0.9%, 0.038 1.8%, 0.156, 0.312 5.8%, 0.789 11.1%,
    1.015 14.2%, 1.096, 1.157, 1.199, 1.224 20.3%, 1.231, 1.231, 1.226,
    1.214 24.6%, 1.176 26.9%, 1.057 32.6%, 1.007 35.5%, 0.984, 0.968,
    0.956, 0.949 42%, 0.946 44.1%, 0.95 48.3%, 0.985 57.8%,
    0.996 60.7%, 1.001, 1.003 68.1%, 1.001 72.2%, 0.998 86.7%, 1
  );
}
```

**Platform-Specific Values:**

| Platform | Tension | Friction | Mass |
|----------|---------|----------|------|
| iOS Default | 157 | 20 | 1 |
| Android Default | 200 | 15 | 1 |
| Facebook Spring | 40 | 7 | 1 |
| Snappy (buttons) | 300 | 30 | 0.8 |
| Smooth (modals) | 170 | 26 | 1 |
| Bouncy (likes) | 180 | 12 | 1 |

**Sources:**
- [Spring Animation in CSS](https://medium.com/@dtinth/spring-animation-in-css-2039de6e1a03)
- [Springs and Bounces in Native CSS](https://www.joshwcomeau.com/animation/linear-timing-function/)
- [How I Transitioned from Ease to Spring Animations](https://medium.com/kaliberinteractive/how-i-transitioned-from-ease-to-spring-animations-5a09eeca0325)

---

### Infinite Scroll & Lazy Loading

**Intersection Observer Pattern:**

```javascript
// High-performance infinite scroll
const imageObserver = new IntersectionObserver(
  (entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const img = entry.target;

        // Load image
        img.src = img.dataset.src;
        img.classList.remove('lazy');

        // Stop observing this image
        observer.unobserve(img);
      }
    });
  },
  {
    root: null, // Viewport
    rootMargin: '200% 0px', // Load 2 viewports ahead
    threshold: 0
  }
);

// Observe all lazy images
document.querySelectorAll('img.lazy').forEach(img => {
  imageObserver.observe(img);
});

// Infinite scroll trigger
const sentinelObserver = new IntersectionObserver(
  (entries) => {
    if (entries[0].isIntersecting) {
      loadMoreImages();
    }
  },
  { rootMargin: '300px' } // Trigger 300px before reaching sentinel
);

sentinelObserver.observe(document.querySelector('.sentinel'));
```

**Performance Benefits:**
- 10x more efficient than scroll events (no main thread blocking)
- Improves Largest Contentful Paint (LCP) by 30-50%
- Reduces initial page weight by 60-80%

**Native Lazy Loading:**

```html
<!-- Modern browsers support native lazy loading -->
<img
  src="image.jpg"
  loading="lazy"
  alt="Food photo"
  width="400"
  height="300"
/>
```

**Browser Support (Feb 2026):**
- Chrome 115+: Full support
- Safari 26+: Full support
- Firefox: Full support
- Edge 115+: Full support

**Sources:**
- [Mastering the Intersection Observer API 2026](https://future.forem.com/sherry_walker_bba406fb339/mastering-the-intersection-observer-api-2026-a-complete-guide-561k)
- [Implementing Infinite Scroll And Image Lazy Loading In React](https://www.smashingmagazine.com/2020/03/infinite-scroll-lazy-image-loading-react/)
- [What is Lazy Loading? Boost Page Performance in 2026](https://elementor.com/blog/what-is-lazy-loading/)

---

### Image Viewer (Pinch Zoom & Pan)

**Transform-Based Approach:**

```javascript
// Performant pinch-zoom implementation
class ImageZoomPan {
  constructor(imageElement) {
    this.image = imageElement;
    this.scale = 1;
    this.translateX = 0;
    this.translateY = 0;
    this.initialDistance = 0;

    this.bind();
  }

  bind() {
    this.image.addEventListener('touchstart', this.handleTouchStart.bind(this));
    this.image.addEventListener('touchmove', this.handleTouchMove.bind(this));
    this.image.addEventListener('touchend', this.handleTouchEnd.bind(this));
  }

  handleTouchStart(e) {
    if (e.touches.length === 2) {
      this.initialDistance = this.getDistance(e.touches[0], e.touches[1]);
      this.initialScale = this.scale;
    }
  }

  handleTouchMove(e) {
    e.preventDefault();

    if (e.touches.length === 2) {
      // Pinch zoom
      const currentDistance = this.getDistance(e.touches[0], e.touches[1]);
      const scaleChange = currentDistance / this.initialDistance;
      this.scale = Math.max(1, Math.min(5, this.initialScale * scaleChange));

      this.updateTransform();
    } else if (e.touches.length === 1 && this.scale > 1) {
      // Pan (only when zoomed)
      const deltaX = e.touches[0].clientX - this.lastX;
      const deltaY = e.touches[0].clientY - this.lastY;

      this.translateX += deltaX;
      this.translateY += deltaY;

      this.clampTranslation();
      this.updateTransform();

      this.lastX = e.touches[0].clientX;
      this.lastY = e.touches[0].clientY;
    }
  }

  handleTouchEnd(e) {
    if (e.touches.length < 2) {
      this.initialDistance = 0;
    }
  }

  getDistance(touch1, touch2) {
    const dx = touch2.clientX - touch1.clientX;
    const dy = touch2.clientY - touch1.clientY;
    return Math.sqrt(dx * dx + dy * dy);
  }

  clampTranslation() {
    const maxTranslate = (this.image.offsetWidth * (this.scale - 1)) / 2;
    this.translateX = Math.max(-maxTranslate, Math.min(maxTranslate, this.translateX));
    this.translateY = Math.max(-maxTranslate, Math.min(maxTranslate, this.translateY));
  }

  updateTransform() {
    this.image.style.transform = `
      translate(${this.translateX}px, ${this.translateY}px)
      scale(${this.scale})
    `;
  }
}
```

**CSS Optimization:**

```css
.zoomable-image {
  width: 100%;
  height: 100%;
  object-fit: contain;
  touch-action: none; /* Disable browser zoom */
  transform-origin: center center;
  transition: transform 100ms linear; /* Smooth updates */
  will-change: transform; /* GPU acceleration hint */
}
```

**Double-Tap Zoom:**

```javascript
let lastTapTime = 0;

image.addEventListener('touchend', (e) => {
  const currentTime = Date.now();
  const tapGap = currentTime - lastTapTime;

  if (tapGap < 300 && tapGap > 0) {
    // Double-tap detected
    const rect = image.getBoundingClientRect();
    const x = e.changedTouches[0].clientX - rect.left;
    const y = e.changedTouches[0].clientY - rect.top;

    if (scale === 1) {
      // Zoom in to tap point
      scale = 2;
      translateX = (rect.width / 2 - x) * scale;
      translateY = (rect.height / 2 - y) * scale;
    } else {
      // Zoom out
      scale = 1;
      translateX = 0;
      translateY = 0;
    }

    image.style.transition = 'transform 250ms ease-out';
    updateTransform();

    setTimeout(() => {
      image.style.transition = 'transform 100ms linear';
    }, 250);
  }

  lastTapTime = currentTime;
});
```

**Sources:**
- [Zoom + Pan + Clamp image preview with vanilla javascript](https://mykolas-mankevicius.medium.com/zoom-pan-clamp-image-preview-with-vanilla-javascript-090215211fc9)
- [GitHub - timmywil/panzoom](https://github.com/timmywil/panzoom)
- [react-zoom-pan-pinch](https://github.com/BetterTyped/react-zoom-pan-pinch)

---

### Before/After Comparison Slider

**Drag & Swipe Implementation:**

```html
<div class="comparison-slider">
  <div class="before-image">
    <img src="before.jpg" alt="Before">
  </div>
  <div class="after-image">
    <img src="after.jpg" alt="After">
  </div>
  <div class="slider-handle">
    <div class="handle-icon">⟷</div>
  </div>
</div>
```

```css
.comparison-slider {
  position: relative;
  width: 100%;
  aspect-ratio: 4 / 3;
  overflow: hidden;
  touch-action: none;
}

.before-image,
.after-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.before-image {
  clip-path: inset(0 50% 0 0); /* Show left 50% */
}

.after-image {
  clip-path: inset(0 0 0 50%); /* Show right 50% */
}

.slider-handle {
  position: absolute;
  top: 0;
  left: 50%;
  width: 4px;
  height: 100%;
  background: white;
  transform: translateX(-50%);
  cursor: ew-resize;
  z-index: 10;
}

.handle-icon {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 48px;
  height: 48px;
  background: white;
  border-radius: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
  font-size: 20px;
  color: #333;
}
```

```javascript
// Comparison slider logic
const slider = document.querySelector('.comparison-slider');
const handle = slider.querySelector('.slider-handle');
const beforeImage = slider.querySelector('.before-image');
const afterImage = slider.querySelector('.after-image');

let isDragging = false;

handle.addEventListener('touchstart', () => {
  isDragging = true;
  handle.style.transition = 'none';
});

slider.addEventListener('touchmove', (e) => {
  if (!isDragging) return;

  const rect = slider.getBoundingClientRect();
  const x = e.touches[0].clientX - rect.left;
  const percentage = Math.max(0, Math.min(100, (x / rect.width) * 100));

  updateSlider(percentage);
});

slider.addEventListener('touchend', () => {
  isDragging = false;
  handle.style.transition = 'left 200ms ease-out';
});

function updateSlider(percentage) {
  handle.style.left = `${percentage}%`;
  beforeImage.style.clipPath = `inset(0 ${100 - percentage}% 0 0)`;
  afterImage.style.clipPath = `inset(0 0 0 ${percentage}%)`;
}

// Optional: Tap to toggle
slider.addEventListener('click', (e) => {
  if (isDragging) return;

  const rect = slider.getBoundingClientRect();
  const x = e.clientX - rect.left;
  const percentage = (x / rect.width) * 100;

  updateSlider(percentage);
});
```

**Alternative: Long-Press to Show Before:**

```javascript
let longPressTimer;

image.addEventListener('touchstart', () => {
  longPressTimer = setTimeout(() => {
    image.src = beforeImage;
    navigator.vibrate(20);
  }, 500);
});

image.addEventListener('touchend', () => {
  clearTimeout(longPressTimer);
  image.src = afterImage;
});
```

**Sources:**
- [Minimal Mobile-compatible Image Comparison Slider](https://www.cssscript.com/image-comparison-slider-before-after/)
- [GitHub - indaneey/iMatch](https://github.com/indaneey/iMatch)
- [Before/After comparison slider + mobile touch swipe](https://github.com/amirhosseinrahmati/before-after-comparison-slider)

---

### Upload Flow (Drag & Drop)

**Progressive Enhancement Pattern:**

```html
<div class="upload-zone" tabindex="0" role="button" aria-label="Upload images">
  <input
    type="file"
    id="file-input"
    accept="image/*"
    multiple
    style="display: none;"
  />
  <div class="upload-prompt">
    <svg class="upload-icon" width="48" height="48">
      <!-- Upload icon SVG -->
    </svg>
    <p class="upload-text">Tap to upload or drag files here</p>
    <p class="upload-subtext">JPG, PNG up to 10MB</p>
  </div>
</div>
```

```css
.upload-zone {
  border: 2px dashed rgba(255, 255, 255, 0.3);
  border-radius: 12px;
  padding: 48px 24px;
  text-align: center;
  cursor: pointer;
  transition: all 200ms ease;
}

.upload-zone:hover,
.upload-zone:focus {
  border-color: rgba(255, 255, 255, 0.6);
  background: rgba(255, 255, 255, 0.05);
}

.upload-zone.drag-over {
  border-color: #FF6B6B;
  background: rgba(255, 107, 107, 0.1);
  border-style: solid;
}

.upload-icon {
  margin: 0 auto 16px;
  opacity: 0.6;
}

.upload-text {
  font-size: 16px;
  font-weight: 500;
  margin-bottom: 8px;
}

.upload-subtext {
  font-size: 14px;
  opacity: 0.6;
}
```

```javascript
const uploadZone = document.querySelector('.upload-zone');
const fileInput = document.getElementById('file-input');

// Click to upload (fallback)
uploadZone.addEventListener('click', () => {
  fileInput.click();
});

// Keyboard accessibility
uploadZone.addEventListener('keydown', (e) => {
  if (e.key === 'Enter' || e.key === ' ') {
    fileInput.click();
  }
});

// Drag and drop
uploadZone.addEventListener('dragover', (e) => {
  e.preventDefault();
  uploadZone.classList.add('drag-over');
});

uploadZone.addEventListener('dragleave', () => {
  uploadZone.classList.remove('drag-over');
});

uploadZone.addEventListener('drop', (e) => {
  e.preventDefault();
  uploadZone.classList.remove('drag-over');

  const files = Array.from(e.dataTransfer.files).filter(file =>
    file.type.startsWith('image/')
  );

  handleFiles(files);
});

// File input change
fileInput.addEventListener('change', (e) => {
  const files = Array.from(e.target.files);
  handleFiles(files);
});

function handleFiles(files) {
  files.forEach(file => {
    // Validate size
    if (file.size > 10 * 1024 * 1024) {
      showError(`${file.name} is too large (max 10MB)`);
      return;
    }

    // Show preview
    const reader = new FileReader();
    reader.onload = (e) => {
      showPreview(e.target.result, file.name);
    };
    reader.readAsDataURL(file);

    // Upload
    uploadFile(file);
  });
}
```

**Upload Progress Indicator:**

```html
<div class="upload-item">
  <img class="upload-thumbnail" src="preview.jpg" alt="Upload preview">
  <div class="upload-info">
    <p class="upload-filename">photo.jpg</p>
    <div class="upload-progress">
      <div class="upload-progress-bar" style="width: 45%;"></div>
    </div>
    <p class="upload-status">Uploading... 45%</p>
  </div>
  <button class="upload-cancel" aria-label="Cancel upload">✕</button>
</div>
```

```css
.upload-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 8px;
  margin-bottom: 8px;
}

.upload-thumbnail {
  width: 56px;
  height: 56px;
  border-radius: 6px;
  object-fit: cover;
}

.upload-info {
  flex: 1;
}

.upload-filename {
  font-size: 14px;
  font-weight: 500;
  margin-bottom: 6px;
}

.upload-progress {
  height: 4px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 2px;
  overflow: hidden;
  margin-bottom: 4px;
}

.upload-progress-bar {
  height: 100%;
  background: linear-gradient(90deg, #FF6B6B, #FF8E53);
  transition: width 300ms ease;
}

.upload-status {
  font-size: 12px;
  opacity: 0.6;
}

.upload-cancel {
  width: 32px;
  height: 32px;
  border-radius: 16px;
  border: none;
  background: rgba(255, 255, 255, 0.1);
  color: white;
  cursor: pointer;
}
```

**Sources:**
- [File upload UI tips for designers](https://www.eleken.co/blog-posts/file-upload-ui)
- [UX best practices for designing a file uploader](https://uploadcare.com/blog/file-uploader-ux-best-practices/)
- [Building a Modern Drag-and-Drop Upload UI in 2025](https://blog.filestack.com/building-modern-drag-and-drop-upload-ui/)

---

### Bottom Sheet / Drawer

**Slide-Up Animation:**

```html
<div class="bottom-sheet-overlay">
  <div class="bottom-sheet">
    <div class="bottom-sheet-handle"></div>
    <div class="bottom-sheet-content">
      <!-- Content here -->
    </div>
  </div>
</div>
```

```css
.bottom-sheet-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0);
  pointer-events: none;
  transition: background 300ms ease;
  z-index: 1000;
}

.bottom-sheet-overlay.open {
  background: rgba(0, 0, 0, 0.5);
  pointer-events: auto;
}

.bottom-sheet {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  max-height: 90vh;
  background: white;
  border-radius: 16px 16px 0 0;
  transform: translateY(100%);
  transition: transform 300ms cubic-bezier(0.4, 0.0, 0.2, 1);
  overflow: hidden;
}

.bottom-sheet-overlay.open .bottom-sheet {
  transform: translateY(0);
}

.bottom-sheet-handle {
  width: 40px;
  height: 4px;
  background: rgba(0, 0, 0, 0.2);
  border-radius: 2px;
  margin: 12px auto;
}

.bottom-sheet-content {
  padding: 0 24px 24px;
  overflow-y: auto;
  max-height: calc(90vh - 40px);
}
```

```javascript
// Bottom sheet controller
class BottomSheet {
  constructor(element) {
    this.overlay = element;
    this.sheet = element.querySelector('.bottom-sheet');
    this.handle = element.querySelector('.bottom-sheet-handle');
    this.startY = 0;
    this.currentY = 0;
    this.isDragging = false;

    this.bind();
  }

  bind() {
    this.handle.addEventListener('touchstart', this.onDragStart.bind(this));
    this.handle.addEventListener('touchmove', this.onDragMove.bind(this));
    this.handle.addEventListener('touchend', this.onDragEnd.bind(this));
    this.overlay.addEventListener('click', this.onOverlayClick.bind(this));
  }

  open() {
    this.overlay.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  close() {
    this.overlay.classList.remove('open');
    document.body.style.overflow = '';
  }

  onDragStart(e) {
    this.isDragging = true;
    this.startY = e.touches[0].clientY;
    this.sheet.style.transition = 'none';
  }

  onDragMove(e) {
    if (!this.isDragging) return;

    this.currentY = e.touches[0].clientY;
    const deltaY = Math.max(0, this.currentY - this.startY); // Only allow downward drag

    this.sheet.style.transform = `translateY(${deltaY}px)`;
  }

  onDragEnd() {
    if (!this.isDragging) return;

    this.isDragging = false;
    this.sheet.style.transition = 'transform 300ms cubic-bezier(0.4, 0.0, 0.2, 1)';

    const deltaY = this.currentY - this.startY;

    if (deltaY > 100) {
      // Swipe down to close
      this.close();
    } else {
      // Snap back
      this.sheet.style.transform = 'translateY(0)';
    }
  }

  onOverlayClick(e) {
    if (e.target === this.overlay) {
      this.close();
    }
  }
}
```

**Sources:**
- [iOS & Android Style Bottom Sheet In JavaScript](https://www.cssscript.com/ios-android-bottom-sheet/)
- [Pure CSS slidedown / slideup animation using transform translateY](https://gist.github.com/webarthur/0fb22721264562c7aa74b07c7fe0f227)

---

### Skeleton Loading

**Shimmer Effect:**

```css
/* Unified shimmer effect across all elements */
@keyframes shimmer {
  0% {
    background-position: -200% 0;
  }
  100% {
    background-position: 200% 0;
  }
}

.skeleton {
  background: linear-gradient(
    90deg,
    rgba(255, 255, 255, 0.1) 0%,
    rgba(255, 255, 255, 0.2) 50%,
    rgba(255, 255, 255, 0.1) 100%
  );
  background-size: 200% 100%;
  background-attachment: fixed; /* Keeps all skeletons in sync */
  animation: shimmer 1.5s infinite;
  border-radius: 4px;
}

/* Skeleton shapes */
.skeleton-text {
  height: 16px;
  margin-bottom: 8px;
}

.skeleton-text:last-child {
  width: 60%; /* Partial line */
}

.skeleton-image {
  width: 100%;
  aspect-ratio: 16 / 9;
}

.skeleton-circle {
  width: 48px;
  height: 48px;
  border-radius: 50%;
}

.skeleton-button {
  height: 44px;
  border-radius: 8px;
}
```

**Complete Skeleton Card:**

```html
<div class="skeleton-card">
  <div class="skeleton skeleton-image"></div>
  <div class="skeleton-card-content">
    <div class="skeleton skeleton-circle"></div>
    <div class="skeleton-card-text">
      <div class="skeleton skeleton-text"></div>
      <div class="skeleton skeleton-text"></div>
      <div class="skeleton skeleton-text"></div>
    </div>
  </div>
</div>
```

**Performance Optimization:**

```css
/* Prevent main thread blocking */
.skeleton {
  /* Use transform instead of position for 60fps */
  will-change: background-position;

  /* Reduce repaints */
  contain: layout style paint;
}

/* Hide text while loading */
.skeleton-text:empty::before {
  content: '\00a0'; /* Non-breaking space */
}
```

**Layout Shift Prevention:**

```css
/* Reserve space with explicit dimensions */
.gallery-item {
  aspect-ratio: 1 / 1;
  min-height: 200px; /* Prevents CLS */
}

.gallery-item.loading {
  /* Skeleton shows in reserved space */
}

.gallery-item img {
  /* Image fills reserved space when loaded */
  width: 100%;
  height: 100%;
  object-fit: cover;
}
```

**Sources:**
- [Pure CSS Skeleton Loading Animation With Shimmer](https://codepen.io/maoberlehner/pen/bQGZYB)
- [Pure CSS Animated Skeleton Loaders](https://tarkan.dev/blog/pure-css-animated-skeleton-loaders)
- [Skeleton screens, but fast](https://dev.to/tigt/skeleton-screens-but-fast-48f1)

---

### Haptic Feedback

**Vibration API:**

```javascript
// Check for support
if ('vibrate' in navigator) {
  // Device supports vibration
}

// Vibration patterns (milliseconds)
const haptics = {
  light: 10,         // Light tap (button press)
  medium: 20,        // Medium tap (toggle, select)
  heavy: 30,         // Heavy tap (error, important action)
  success: [10, 50, 10], // Success pattern (double-pulse)
  error: [50, 100, 50],  // Error pattern (long-short-long)
};

// Use cases
function triggerHaptic(type = 'light') {
  if ('vibrate' in navigator) {
    navigator.vibrate(haptics[type]);
  }
}

// Examples
button.addEventListener('click', () => {
  triggerHaptic('light');
});

likeButton.addEventListener('click', () => {
  triggerHaptic('success');
});

form.addEventListener('submit', (e) => {
  if (!isValid) {
    e.preventDefault();
    triggerHaptic('error');
  }
});
```

**Best Practices:**
- Keep vibrations under 300ms total duration
- Only vibrate for meaningful interactions (success, error, confirmation)
- Don't vibrate on every tap (causes fatigue)
- Provide settings to disable haptics (accessibility)

**Platform Support:**
- Android: Full support
- iOS: Limited (only works in Safari for specific actions)
- Desktop: Generally no support

**Removing Webkit Tap Highlight:**

```css
/* Remove default tap highlight (add custom feedback instead) */
* {
  -webkit-tap-highlight-color: transparent;
  -webkit-touch-callout: none;
}

/* Custom tap feedback */
button:active {
  transform: scale(0.96);
  transition: transform 100ms ease;
}
```

**Sources:**
- [Web Haptics: The NPM Package Everyone's Adding](https://medium.com/@springmusk/web-haptics-the-npm-package-everyones-adding-for-haptic-feedback-4c774f10caaa)
- [Haptic Feedback in Web Design: UX You Can Feel](https://medium.com/@officialsafamarva/haptic-feedback-in-web-design-ux-you-can-feel-10e1a5095cee)
- [Vibration API - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Vibration_API)

---

### Card Swipe (Tinder-Style)

**Swipe Gesture Implementation:**

```html
<div class="card-stack">
  <div class="card" data-card="1">
    <img src="image1.jpg" alt="Image 1">
  </div>
  <div class="card" data-card="2">
    <img src="image2.jpg" alt="Image 2">
  </div>
  <div class="card" data-card="3">
    <img src="image3.jpg" alt="Image 3">
  </div>
</div>
```

```css
.card-stack {
  position: relative;
  width: 100%;
  max-width: 400px;
  aspect-ratio: 3 / 4;
  margin: 0 auto;
}

.card {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  cursor: grab;
  touch-action: none;
  transform-origin: bottom center;
}

.card:active {
  cursor: grabbing;
}

.card img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* Stack effect */
.card:nth-child(2) {
  transform: scale(0.95) translateY(10px);
  opacity: 0.8;
}

.card:nth-child(3) {
  transform: scale(0.9) translateY(20px);
  opacity: 0.6;
}

/* Swipe animations */
@keyframes swipe-right {
  to {
    transform: translateX(150%) rotate(20deg);
    opacity: 0;
  }
}

@keyframes swipe-left {
  to {
    transform: translateX(-150%) rotate(-20deg);
    opacity: 0;
  }
}

@keyframes swipe-up {
  to {
    transform: translateY(-150%) scale(0.8);
    opacity: 0;
  }
}
```

```javascript
class CardSwipe {
  constructor(card) {
    this.card = card;
    this.startX = 0;
    this.startY = 0;
    this.currentX = 0;
    this.currentY = 0;
    this.isDragging = false;

    this.bind();
  }

  bind() {
    this.card.addEventListener('touchstart', this.onDragStart.bind(this));
    this.card.addEventListener('touchmove', this.onDragMove.bind(this));
    this.card.addEventListener('touchend', this.onDragEnd.bind(this));
  }

  onDragStart(e) {
    this.isDragging = true;
    this.startX = e.touches[0].clientX;
    this.startY = e.touches[0].clientY;
    this.card.style.transition = 'none';
  }

  onDragMove(e) {
    if (!this.isDragging) return;

    this.currentX = e.touches[0].clientX;
    this.currentY = e.touches[0].clientY;

    const deltaX = this.currentX - this.startX;
    const deltaY = this.currentY - this.startY;

    // Calculate rotation (up to 15 degrees)
    const rotation = (deltaX / window.innerWidth) * 15;

    // Calculate opacity (fades as swiped)
    const opacity = 1 - Math.abs(deltaX) / window.innerWidth;

    this.card.style.transform = `
      translate(${deltaX}px, ${deltaY}px)
      rotate(${rotation}deg)
    `;
    this.card.style.opacity = opacity;
  }

  onDragEnd() {
    if (!this.isDragging) return;

    this.isDragging = false;
    this.card.style.transition = 'transform 300ms ease, opacity 300ms ease';

    const deltaX = this.currentX - this.startX;
    const deltaY = this.currentY - this.startY;
    const threshold = window.innerWidth * 0.3; // 30% of screen width

    if (Math.abs(deltaX) > threshold) {
      // Swipe threshold exceeded
      if (deltaX > 0) {
        this.swipeRight();
      } else {
        this.swipeLeft();
      }
    } else if (deltaY < -threshold) {
      this.swipeUp();
    } else {
      // Snap back to center
      this.card.style.transform = 'translate(0, 0) rotate(0deg)';
      this.card.style.opacity = 1;
    }
  }

  swipeRight() {
    this.card.style.animation = 'swipe-right 300ms ease-out forwards';
    this.card.addEventListener('animationend', () => {
      this.onSwipeComplete('right');
    }, { once: true });
  }

  swipeLeft() {
    this.card.style.animation = 'swipe-left 300ms ease-out forwards';
    this.card.addEventListener('animationend', () => {
      this.onSwipeComplete('left');
    }, { once: true });
  }

  swipeUp() {
    this.card.style.animation = 'swipe-up 300ms ease-out forwards';
    this.card.addEventListener('animationend', () => {
      this.onSwipeComplete('up');
    }, { once: true });
  }

  onSwipeComplete(direction) {
    console.log(`Swiped ${direction}`);
    this.card.remove(); // Remove card from DOM

    // Initialize next card
    const nextCard = document.querySelector('.card');
    if (nextCard) {
      new CardSwipe(nextCard);
    }
  }
}

// Initialize first card
const firstCard = document.querySelector('.card');
if (firstCard) {
  new CardSwipe(firstCard);
}
```

**Sources:**
- [Creating a Tinder-Style Swipe Card UI](https://codingartistweb.com/2025/06/creating-a-tinder-style-swipe-card-ui-with-html-css-and-javascript/)
- [Create Tinder-like card swipe gesture using React and framer-motion](https://www.geeksforgeeks.org/how-to-create-tinder-card-swipe-gesture-using-react-and-framer-motion/)
- [Tinderesque – building a Tinder-like interface](https://christianheilmann.com/2015/09/06/tinderesque-building-a-tinder-like-interface-with-css-animations-and-vanilla-js-justcode/)

---

## 9. Key Takeaways & Implementation Priorities

### Must-Have Patterns (High Impact)

1. **Touch Targets:** 48x48px minimum, 12-48px spacing
2. **Spring Animations:** tension: 300, friction: 30, mass: 0.8
3. **Lazy Loading:** Intersection Observer with 200% rootMargin
4. **Bottom Sheet:** 300ms cubic-bezier(0.4, 0.0, 0.2, 1) slide-up
5. **Skeleton Loading:** Unified shimmer with background-attachment: fixed
6. **Haptic Feedback:** 10ms light, 20ms medium, 30ms heavy
7. **Before/After:** Draggable clip-path slider

### Nice-to-Have Patterns (Polish)

1. **Pinch Zoom:** Transform-based, 1x-5x range
2. **Card Swipe:** Tinder-style dismiss gesture
3. **Double-Tap Zoom:** 250ms spring to 2x at tap point
4. **Long-Press Preview:** 500ms trigger, 20ms haptic
5. **Gesture-Based Editing:** Vertical = tool, horizontal = value

### Performance Requirements

- First Paint: <2s
- Time to Interactive: <6s
- Animation: 60fps (16.67ms per frame)
- Touch Response: <100ms
- Gesture Recognition: <16ms

### Accessibility Requirements

- Touch targets: 44x44px minimum (WCAG AAA)
- Keyboard navigation: Tab, Enter, Space
- Screen reader: ARIA labels, roles, live regions
- High contrast: Maintain 4.5:1 ratio
- Reduce motion: Respect prefers-reduced-motion

---

## Implementation Checklist

### Phase 1: Foundation
- [ ] Set up touch target sizing system (48px base)
- [ ] Implement spring animation utility (React Spring or CSS linear())
- [ ] Add Intersection Observer for lazy loading
- [ ] Create skeleton loading components
- [ ] Remove webkit tap highlights, add custom feedback

### Phase 2: Core Interactions
- [ ] Bottom sheet/drawer component
- [ ] Before/after comparison slider
- [ ] Upload flow with drag & drop
- [ ] Gallery grid with infinite scroll
- [ ] Image viewer with pinch zoom & pan

### Phase 3: Polish
- [ ] Haptic feedback integration
- [ ] Gesture-based editing controls
- [ ] Card swipe animations
- [ ] Double-tap zoom
- [ ] Long-press previews

### Phase 4: Optimization
- [ ] Reduce JavaScript bundle (<150KB core)
- [ ] Optimize images (WebP, lazy load)
- [ ] Implement service worker caching
- [ ] Add loading="lazy" to all images
- [ ] Test on real devices (iOS Safari, Android Chrome)

---

*Last Updated: March 10, 2026*
