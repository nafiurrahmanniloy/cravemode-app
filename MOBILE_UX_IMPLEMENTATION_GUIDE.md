# Mobile UX Implementation Guide — Quick Reference

Copy-paste ready code for implementing premium mobile UX patterns in CraveMode AI.

---

## 1. Touch Targets & Spacing

```css
/* Base sizing system */
:root {
  --touch-target-min: 48px;
  --touch-spacing-min: 12px;
  --touch-spacing-comfortable: 24px;
}

/* Expandable touch target */
.icon-button {
  width: 24px;
  height: 24px;
  padding: 12px; /* Total: 48x48px */
  cursor: pointer;
  background: transparent;
  border: none;
  -webkit-tap-highlight-color: transparent;
}

/* Or using pseudo-element */
.small-icon {
  width: 20px;
  height: 20px;
  position: relative;
}

.small-icon::before {
  content: '';
  position: absolute;
  inset: -14px; /* Creates 48x48px touch area */
}
```

---

## 2. Spring Animations

```javascript
// React Spring / Framer Motion config
export const springConfig = {
  type: 'spring',
  stiffness: 300,
  damping: 30,
  mass: 0.8
};

// Framer Motion example
<motion.div
  initial={{ scale: 0.8, opacity: 0 }}
  animate={{ scale: 1, opacity: 1 }}
  exit={{ scale: 0.8, opacity: 0 }}
  transition={springConfig}
/>
```

```css
/* CSS Spring (using linear() function) */
@keyframes spring-in {
  0% { transform: scale(0.9); }
  100% { transform: scale(1); }
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

---

## 3. Intersection Observer (Lazy Loading & Infinite Scroll)

```javascript
// Image lazy loading
const imageObserver = new IntersectionObserver(
  (entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const img = entry.target;
        img.src = img.dataset.src;
        img.classList.remove('lazy');
        observer.unobserve(img);
      }
    });
  },
  {
    root: null,
    rootMargin: '200% 0px', // Load 2 viewports ahead
    threshold: 0
  }
);

// Observe all lazy images
document.querySelectorAll('img.lazy').forEach(img => {
  imageObserver.observe(img);
});

// Infinite scroll sentinel
const sentinelObserver = new IntersectionObserver(
  (entries) => {
    if (entries[0].isIntersecting) {
      loadMoreImages();
    }
  },
  { rootMargin: '300px' }
);

sentinelObserver.observe(document.querySelector('.sentinel'));
```

```html
<!-- Lazy image markup -->
<img
  class="lazy"
  data-src="actual-image.jpg"
  src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg'/%3E"
  alt="Description"
/>

<!-- Or native lazy loading -->
<img src="image.jpg" loading="lazy" alt="Description" />
```

---

## 4. Bottom Sheet / Drawer

```tsx
// React + Framer Motion
import { motion, AnimatePresence } from 'framer-motion';

export function BottomSheet({ isOpen, onClose, children }) {
  return (
    <AnimatePresence>
      {isOpen && (
        <>
          <motion.div
            className="fixed inset-0 bg-black/50 z-50"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            onClick={onClose}
          />
          <motion.div
            className="fixed bottom-0 left-0 right-0 bg-white rounded-t-2xl z-50 max-h-[90vh] overflow-hidden"
            initial={{ y: '100%' }}
            animate={{ y: 0 }}
            exit={{ y: '100%' }}
            transition={{ type: 'spring', stiffness: 300, damping: 30 }}
            drag="y"
            dragConstraints={{ top: 0, bottom: 0 }}
            dragElastic={0.2}
            onDragEnd={(e, info) => {
              if (info.offset.y > 100) onClose();
            }}
          >
            <div className="w-10 h-1 bg-gray-300 rounded-full mx-auto my-3" />
            <div className="px-6 pb-6 overflow-y-auto max-h-[calc(90vh-40px)]">
              {children}
            </div>
          </motion.div>
        </>
      )}
    </AnimatePresence>
  );
}
```

---

## 5. Skeleton Loading

```css
@keyframes shimmer {
  0% { background-position: -200% 0; }
  100% { background-position: 200% 0; }
}

.skeleton {
  background: linear-gradient(
    90deg,
    rgba(255, 255, 255, 0.1) 0%,
    rgba(255, 255, 255, 0.2) 50%,
    rgba(255, 255, 255, 0.1) 100%
  );
  background-size: 200% 100%;
  background-attachment: fixed; /* Sync all skeletons */
  animation: shimmer 1.5s infinite;
  border-radius: 4px;
}

.skeleton-text { height: 16px; margin-bottom: 8px; }
.skeleton-image { width: 100%; aspect-ratio: 16 / 9; }
.skeleton-circle { width: 48px; height: 48px; border-radius: 50%; }
.skeleton-button { height: 44px; border-radius: 8px; }
```

```tsx
// React component
export function SkeletonCard() {
  return (
    <div className="border border-white/10 rounded-lg p-4">
      <div className="skeleton skeleton-image mb-4" />
      <div className="skeleton skeleton-text" />
      <div className="skeleton skeleton-text" />
      <div className="skeleton skeleton-text w-3/5" />
    </div>
  );
}
```

---

## 6. Haptic Feedback

```typescript
// haptics.ts
export const haptics = {
  light: 10,
  medium: 20,
  heavy: 30,
  success: [10, 50, 10],
  error: [50, 100, 50],
};

export function triggerHaptic(type: keyof typeof haptics = 'light') {
  if ('vibrate' in navigator) {
    navigator.vibrate(haptics[type]);
  }
}
```

```tsx
// Usage in components
import { triggerHaptic } from '@/lib/haptics';

<button
  onClick={() => {
    triggerHaptic('medium');
    // ... handle click
  }}
>
  Submit
</button>
```

---

## 7. Before/After Comparison Slider

```tsx
'use client';

import { useState, useRef, useEffect } from 'react';

export function BeforeAfterSlider({ beforeSrc, afterSrc, alt }) {
  const [position, setPosition] = useState(50);
  const [isDragging, setIsDragging] = useState(false);
  const containerRef = useRef<HTMLDivElement>(null);

  const handleMove = (clientX: number) => {
    if (!containerRef.current) return;
    const rect = containerRef.current.getBoundingClientRect();
    const x = clientX - rect.left;
    const percentage = Math.max(0, Math.min(100, (x / rect.width) * 100));
    setPosition(percentage);
  };

  const handleMouseMove = (e: MouseEvent) => {
    if (isDragging) handleMove(e.clientX);
  };

  const handleTouchMove = (e: TouchEvent) => {
    if (isDragging) handleMove(e.touches[0].clientX);
  };

  useEffect(() => {
    if (isDragging) {
      document.addEventListener('mousemove', handleMouseMove);
      document.addEventListener('touchmove', handleTouchMove);
      document.addEventListener('mouseup', () => setIsDragging(false));
      document.addEventListener('touchend', () => setIsDragging(false));
    }

    return () => {
      document.removeEventListener('mousemove', handleMouseMove);
      document.removeEventListener('touchmove', handleTouchMove);
    };
  }, [isDragging]);

  return (
    <div
      ref={containerRef}
      className="relative w-full aspect-video overflow-hidden rounded-lg touch-none"
    >
      {/* Before Image */}
      <div className="absolute inset-0">
        <img src={beforeSrc} alt={`${alt} - Before`} className="w-full h-full object-cover" />
      </div>

      {/* After Image */}
      <div
        className="absolute inset-0"
        style={{ clipPath: `inset(0 0 0 ${position}%)` }}
      >
        <img src={afterSrc} alt={`${alt} - After`} className="w-full h-full object-cover" />
      </div>

      {/* Slider Handle */}
      <div
        className="absolute top-0 bottom-0 w-1 bg-white cursor-ew-resize z-10"
        style={{ left: `${position}%`, transform: 'translateX(-50%)' }}
        onMouseDown={() => setIsDragging(true)}
        onTouchStart={() => setIsDragging(true)}
      >
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-12 h-12 bg-white rounded-full flex items-center justify-center shadow-lg">
          <svg className="w-6 h-6 text-gray-800" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 9l4-4 4 4m0 6l-4 4-4-4" />
          </svg>
        </div>
      </div>

      {/* Labels */}
      <div className="absolute top-4 left-4 bg-black/60 text-white px-3 py-1 rounded-full text-sm">
        Before
      </div>
      <div className="absolute top-4 right-4 bg-black/60 text-white px-3 py-1 rounded-full text-sm">
        After
      </div>
    </div>
  );
}
```

---

## 8. Pinch Zoom & Pan Image Viewer

```tsx
'use client';

import { useState, useRef, useEffect } from 'react';

export function ZoomableImage({ src, alt }) {
  const [scale, setScale] = useState(1);
  const [translate, setTranslate] = useState({ x: 0, y: 0 });
  const imageRef = useRef<HTMLImageElement>(null);
  const initialDistance = useRef(0);
  const lastTapTime = useRef(0);

  const handleTouchStart = (e: React.TouchEvent) => {
    if (e.touches.length === 2) {
      initialDistance.current = getDistance(e.touches[0], e.touches[1]);
    }
  };

  const handleTouchMove = (e: React.TouchEvent) => {
    e.preventDefault();

    if (e.touches.length === 2) {
      // Pinch zoom
      const currentDistance = getDistance(e.touches[0], e.touches[1]);
      const newScale = Math.max(1, Math.min(5, (currentDistance / initialDistance.current) * scale));
      setScale(newScale);
    } else if (e.touches.length === 1 && scale > 1) {
      // Pan (only when zoomed)
      // Implementation similar to above
    }
  };

  const handleDoubleTap = (e: React.TouchEvent) => {
    const currentTime = Date.now();
    const tapGap = currentTime - lastTapTime.current;

    if (tapGap < 300 && tapGap > 0) {
      if (scale === 1) {
        setScale(2);
      } else {
        setScale(1);
        setTranslate({ x: 0, y: 0 });
      }
    }

    lastTapTime.current = currentTime;
  };

  const getDistance = (touch1: React.Touch, touch2: React.Touch) => {
    const dx = touch2.clientX - touch1.clientX;
    const dy = touch2.clientY - touch1.clientY;
    return Math.sqrt(dx * dx + dy * dy);
  };

  return (
    <div className="overflow-hidden touch-none">
      <img
        ref={imageRef}
        src={src}
        alt={alt}
        className="w-full h-full object-contain transition-transform duration-100"
        style={{
          transform: `translate(${translate.x}px, ${translate.y}px) scale(${scale})`,
          willChange: 'transform',
        }}
        onTouchStart={handleTouchStart}
        onTouchMove={handleTouchMove}
        onTouchEnd={handleDoubleTap}
      />
    </div>
  );
}
```

---

## 9. Upload Flow (Drag & Drop)

```tsx
'use client';

import { useState, useCallback } from 'react';

export function UploadZone({ onFilesSelected }) {
  const [isDragOver, setIsDragOver] = useState(false);

  const handleFiles = useCallback((files: FileList) => {
    const validFiles = Array.from(files).filter(
      file => file.type.startsWith('image/') && file.size <= 10 * 1024 * 1024
    );
    onFilesSelected(validFiles);
  }, [onFilesSelected]);

  const handleDrop = useCallback((e: React.DragEvent) => {
    e.preventDefault();
    setIsDragOver(false);
    handleFiles(e.dataTransfer.files);
  }, [handleFiles]);

  const handleChange = useCallback((e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files) handleFiles(e.target.files);
  }, [handleFiles]);

  return (
    <div
      className={`
        border-2 border-dashed rounded-xl p-12 text-center cursor-pointer
        transition-all duration-200
        ${isDragOver
          ? 'border-amber-500 bg-amber-500/10 border-solid'
          : 'border-white/30 hover:border-white/60 hover:bg-white/5'
        }
      `}
      onDragOver={(e) => { e.preventDefault(); setIsDragOver(true); }}
      onDragLeave={() => setIsDragOver(false)}
      onDrop={handleDrop}
      onClick={() => document.getElementById('file-input')?.click()}
    >
      <input
        id="file-input"
        type="file"
        accept="image/*"
        multiple
        onChange={handleChange}
        className="hidden"
      />

      <svg className="w-12 h-12 mx-auto mb-4 opacity-60" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
      </svg>

      <p className="text-lg font-medium mb-2">
        {isDragOver ? 'Drop files here' : 'Tap to upload or drag files here'}
      </p>
      <p className="text-sm opacity-60">JPG, PNG up to 10MB</p>
    </div>
  );
}
```

---

## 10. Gallery Grid (Instagram-Style)

```tsx
export function GalleryGrid({ images }) {
  return (
    <div className="grid grid-cols-3 gap-px bg-black">
      {images.map((image, index) => (
        <div key={image.id} className="aspect-square relative overflow-hidden group">
          <img
            src={image.thumbnail}
            alt={image.alt}
            loading="lazy"
            className="w-full h-full object-cover transition-transform duration-200 group-active:scale-95"
          />

          {/* Overlay on tap */}
          <div className="absolute inset-0 bg-black/40 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center">
            <span className="text-white text-sm font-medium">View</span>
          </div>
        </div>
      ))}

      {/* Infinite scroll sentinel */}
      <div className="sentinel col-span-3 h-px" />
    </div>
  );
}
```

---

## 11. Gesture Detection System

```typescript
// gestures.ts
export class GestureDetector {
  private element: HTMLElement;
  private touches: Touch[] = [];
  private startTime = 0;
  private startX = 0;
  private startY = 0;
  private longPressTimer: NodeJS.Timeout | null = null;

  constructor(element: HTMLElement, handlers: GestureHandlers) {
    this.element = element;
    this.bind(handlers);
  }

  private bind(handlers: GestureHandlers) {
    this.element.addEventListener('touchstart', (e) => this.onTouchStart(e, handlers));
    this.element.addEventListener('touchmove', (e) => this.onTouchMove(e, handlers));
    this.element.addEventListener('touchend', (e) => this.onTouchEnd(e, handlers));
  }

  private onTouchStart(e: TouchEvent, handlers: GestureHandlers) {
    this.touches = Array.from(e.touches);
    this.startTime = Date.now();
    this.startX = this.touches[0].clientX;
    this.startY = this.touches[0].clientY;

    // Long-press detection
    this.longPressTimer = setTimeout(() => {
      handlers.onLongPress?.(this.touches[0]);
      if ('vibrate' in navigator) navigator.vibrate(20);
    }, 500);
  }

  private onTouchMove(e: TouchEvent, handlers: GestureHandlers) {
    if (this.longPressTimer) clearTimeout(this.longPressTimer);
    this.touches = Array.from(e.touches);

    if (this.touches.length === 2) {
      handlers.onPinch?.(this.touches);
    } else if (this.touches.length === 1) {
      const deltaX = this.touches[0].clientX - this.startX;
      const deltaY = this.touches[0].clientY - this.startY;
      const distance = Math.sqrt(deltaX ** 2 + deltaY ** 2);

      if (distance > 40) {
        const angle = Math.atan2(deltaY, deltaX) * (180 / Math.PI);

        if (Math.abs(angle) < 15) handlers.onSwipeRight?.();
        else if (Math.abs(angle - 180) < 15) handlers.onSwipeLeft?.();
        else if (angle > 75 && angle < 105) handlers.onSwipeDown?.();
        else if (angle > -105 && angle < -75) handlers.onSwipeUp?.();
      }
    }
  }

  private onTouchEnd(e: TouchEvent, handlers: GestureHandlers) {
    if (this.longPressTimer) clearTimeout(this.longPressTimer);
    const duration = Date.now() - this.startTime;

    if (duration < 300 && this.touches.length === 1) {
      handlers.onTap?.(this.touches[0]);
      if ('vibrate' in navigator) navigator.vibrate(10);
    }
  }
}

interface GestureHandlers {
  onTap?: (touch: Touch) => void;
  onLongPress?: (touch: Touch) => void;
  onSwipeLeft?: () => void;
  onSwipeRight?: () => void;
  onSwipeUp?: () => void;
  onSwipeDown?: () => void;
  onPinch?: (touches: Touch[]) => void;
}
```

---

## 12. Card Swipe (Tinder-Style)

```tsx
'use client';

import { motion, useMotionValue, useTransform } from 'framer-motion';

export function SwipeCard({ image, onSwipe }) {
  const x = useMotionValue(0);
  const rotate = useTransform(x, [-200, 200], [-15, 15]);
  const opacity = useTransform(x, [-200, 0, 200], [0.5, 1, 0.5]);

  const handleDragEnd = (event, info) => {
    const threshold = 100;

    if (Math.abs(info.offset.x) > threshold) {
      onSwipe(info.offset.x > 0 ? 'right' : 'left');
    }
  };

  return (
    <motion.div
      className="absolute inset-0 bg-white rounded-2xl shadow-xl cursor-grab active:cursor-grabbing"
      style={{ x, rotate, opacity }}
      drag="x"
      dragConstraints={{ left: 0, right: 0 }}
      onDragEnd={handleDragEnd}
      whileTap={{ cursor: 'grabbing' }}
    >
      <img src={image} alt="Food" className="w-full h-full object-cover rounded-2xl" />
    </motion.div>
  );
}
```

---

## 13. Utility: Safe Area Insets

```css
/* Respect notch and home indicator */
.safe-container {
  padding-top: env(safe-area-inset-top);
  padding-bottom: env(safe-area-inset-bottom);
  padding-left: env(safe-area-inset-left);
  padding-right: env(safe-area-inset-right);
}

/* Bottom fixed navigation */
.bottom-nav {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  padding-bottom: max(16px, env(safe-area-inset-bottom));
}
```

---

## 14. PWA Meta Tags (Add to layout.tsx)

```tsx
export const metadata = {
  themeColor: '#000000',
  viewport: {
    width: 'device-width',
    initialScale: 1,
    maximumScale: 5,
    userScalable: true,
    viewportFit: 'cover', // Respect safe areas
  },
  appleWebApp: {
    capable: true,
    statusBarStyle: 'black-translucent',
    title: 'CraveMode AI',
  },
};
```

---

## 15. Performance Optimizations

```typescript
// Debounce for search/filter
export function debounce<T extends (...args: any[]) => any>(
  func: T,
  wait: number
): (...args: Parameters<T>) => void {
  let timeout: NodeJS.Timeout;
  return (...args: Parameters<T>) => {
    clearTimeout(timeout);
    timeout = setTimeout(() => func(...args), wait);
  };
}

// Throttle for scroll events
export function throttle<T extends (...args: any[]) => any>(
  func: T,
  limit: number
): (...args: Parameters<T>) => void {
  let inThrottle: boolean;
  return (...args: Parameters<T>) => {
    if (!inThrottle) {
      func(...args);
      inThrottle = true;
      setTimeout(() => (inThrottle = false), limit);
    }
  };
}

// Usage
const handleSearch = debounce((query: string) => {
  // Search logic
}, 300);

const handleScroll = throttle(() => {
  // Scroll logic
}, 16); // 60fps
```

---

## Implementation Priority

### Phase 1: Foundation (Week 1)
1. Touch targets (48px minimum)
2. Spring animations
3. Skeleton loading
4. Haptic feedback
5. Remove webkit tap highlights

### Phase 2: Core Interactions (Week 2)
1. Bottom sheet
2. Upload flow
3. Gallery grid + infinite scroll
4. Before/after slider
5. Image viewer (pinch zoom)

### Phase 3: Polish (Week 3)
1. Gesture system
2. Card swipe
3. Lazy loading optimization
4. Performance audit
5. Real device testing

---

*Copy these snippets directly into your CraveMode AI project.*
