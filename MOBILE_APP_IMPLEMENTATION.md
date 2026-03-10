# CraveMode Mobile App — Quick Implementation Guide

## Immediately Implementable Patterns

### 1. Tab Bar (iOS 26 Liquid Glass Style)

```tsx
// components/mobile/tab-bar.tsx
import { motion } from 'framer-motion';

const tabs = [
  { id: 'enhance', icon: 'camera.filters', label: 'Enhance' },
  { id: 'gallery', icon: 'photo.on.rectangle', label: 'Gallery' },
  { id: 'queue', icon: 'clock.arrow.circlepath', label: 'Queue' },
  { id: 'profile', icon: 'person.crop.circle', label: 'Profile' },
];

export function TabBar({ activeTab, onTabChange }) {
  return (
    <div className="fixed bottom-0 left-0 right-0 h-[83px] backdrop-blur-xl bg-black/90 border-t border-white/10">
      <div className="flex items-center justify-around h-full px-4 pb-safe">
        {tabs.map((tab) => (
          <button
            key={tab.id}
            onClick={() => onTabChange(tab.id)}
            className="flex flex-col items-center gap-1"
          >
            <motion.div
              className={`p-2 rounded-lg ${
                activeTab === tab.id
                  ? 'bg-amber-500/20'
                  : 'bg-transparent'
              }`}
              whileTap={{ scale: 0.96 }}
            >
              <Icon
                name={tab.icon}
                className={activeTab === tab.id ? 'text-amber-500' : 'text-gray-400'}
                size={24}
              />
            </motion.div>
            <span className="text-[10px] font-medium">
              {tab.label}
            </span>
          </button>
        ))}
      </div>
    </div>
  );
}
```

**Tailwind Config**:
```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      spacing: {
        'safe': 'env(safe-area-inset-bottom)',
      },
      backdropBlur: {
        'xl': '20px',
      },
    },
  },
};
```

---

### 2. Dark Glassmorphism Card

```tsx
// components/mobile/glass-card.tsx
export function GlassCard({ children, className = '' }) {
  return (
    <div
      className={`
        relative overflow-hidden rounded-2xl p-4
        bg-gradient-to-br from-amber-500/10 to-orange-500/10
        backdrop-blur-[20px]
        border border-white/10
        shadow-[0_8px_32px_rgba(0,0,0,0.3),inset_0_1px_0_rgba(255,255,255,0.1)]
        transition-all duration-300 ease-out
        hover:translate-y-[-4px]
        hover:shadow-[0_16px_48px_rgba(0,0,0,0.4),inset_0_1px_0_rgba(255,255,255,0.2)]
        ${className}
      `}
    >
      {children}
    </div>
  );
}
```

**CSS Alternative**:
```css
.glass-card {
  background: linear-gradient(135deg, rgba(255, 184, 0, 0.1) 0%, rgba(255, 87, 34, 0.1) 100%);
  backdrop-filter: blur(20px);
  border-radius: 16px;
  padding: 16px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow:
    0 8px 32px rgba(0, 0, 0, 0.3),
    inset 0 1px 0 rgba(255, 255, 255, 0.1);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.glass-card:hover {
  transform: translateY(-4px);
  box-shadow:
    0 16px 48px rgba(0, 0, 0, 0.4),
    inset 0 1px 0 rgba(255, 255, 255, 0.2);
}
```

---

### 3. Photo Grid with Multi-Select (Instagram Pattern)

```tsx
// components/mobile/photo-grid.tsx
import { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';

export function PhotoGrid({ photos, onSelectionChange }) {
  const [selectedIds, setSelectedIds] = useState<string[]>([]);
  const [isMultiSelectMode, setIsMultiSelectMode] = useState(false);

  const handleLongPress = (photoId: string) => {
    // Enter multi-select mode
    setIsMultiSelectMode(true);
    setSelectedIds([photoId]);
    // Haptic feedback (iOS)
    if (window.navigator.vibrate) {
      window.navigator.vibrate(10);
    }
  };

  const handleTap = (photoId: string) => {
    if (isMultiSelectMode) {
      // Toggle selection
      setSelectedIds(prev =>
        prev.includes(photoId)
          ? prev.filter(id => id !== photoId)
          : [...prev, photoId]
      );
    }
  };

  return (
    <div className="grid grid-cols-3 gap-[2px]">
      {photos.map((photo) => (
        <motion.div
          key={photo.id}
          className="relative aspect-square"
          onTapStart={() => {
            const timer = setTimeout(() => handleLongPress(photo.id), 500);
            return () => clearTimeout(timer);
          }}
          onClick={() => handleTap(photo.id)}
        >
          <img
            src={photo.url}
            alt=""
            className="w-full h-full object-cover"
          />

          <AnimatePresence>
            {isMultiSelectMode && (
              <motion.div
                initial={{ opacity: 0, scale: 0.8 }}
                animate={{ opacity: 1, scale: 1 }}
                exit={{ opacity: 0, scale: 0.8 }}
                className="absolute top-2 right-2"
              >
                <div className={`
                  w-6 h-6 rounded-full flex items-center justify-center
                  ${selectedIds.includes(photo.id)
                    ? 'bg-amber-500'
                    : 'bg-white/20 backdrop-blur-sm border border-white/40'
                  }
                `}>
                  {selectedIds.includes(photo.id) && (
                    <CheckIcon className="w-4 h-4 text-white" />
                  )}
                </div>
              </motion.div>
            )}
          </AnimatePresence>
        </motion.div>
      ))}

      {isMultiSelectMode && (
        <div className="fixed bottom-20 left-0 right-0 p-4">
          <GlassCard>
            <div className="flex items-center justify-between">
              <span className="text-white font-medium">
                {selectedIds.length} selected
              </span>
              <button
                onClick={() => {
                  setIsMultiSelectMode(false);
                  setSelectedIds([]);
                }}
                className="text-amber-500 font-medium"
              >
                Deselect All
              </button>
            </div>
          </GlassCard>
        </div>
      )}
    </div>
  );
}
```

---

### 4. Skeleton Screen with Shimmer

```tsx
// components/mobile/skeleton.tsx
export function ImageSkeleton() {
  return (
    <div className="relative overflow-hidden rounded-xl bg-gray-800/50">
      <div className="aspect-video" />
      <div
        className="absolute inset-0 -translate-x-full animate-shimmer"
        style={{
          background: 'linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent)',
        }}
      />
    </div>
  );
}
```

**Tailwind Config**:
```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      keyframes: {
        shimmer: {
          '0%': { transform: 'translateX(-100%)' },
          '100%': { transform: 'translateX(100%)' },
        },
      },
      animation: {
        shimmer: 'shimmer 1.5s infinite',
      },
    },
  },
};
```

**Usage**:
```tsx
// In loading state
{isLoading ? (
  <div className="grid grid-cols-2 gap-4">
    {Array.from({ length: 6 }).map((_, i) => (
      <ImageSkeleton key={i} />
    ))}
  </div>
) : (
  <PhotoGrid photos={photos} />
)}
```

---

### 5. Progress Ring (Upload/Processing)

```tsx
// components/mobile/progress-ring.tsx
export function ProgressRing({ progress, size = 100 }) {
  const radius = 45;
  const circumference = 2 * Math.PI * radius;
  const offset = circumference - (progress / 100) * circumference;

  return (
    <svg width={size} height={size} className="transform -rotate-90">
      {/* Background circle */}
      <circle
        cx={size / 2}
        cy={size / 2}
        r={radius}
        stroke="#1C1C1E"
        strokeWidth="8"
        fill="none"
      />
      {/* Progress circle */}
      <circle
        cx={size / 2}
        cy={size / 2}
        r={radius}
        stroke="#FFB800"
        strokeWidth="8"
        fill="none"
        strokeDasharray={circumference}
        strokeDashoffset={offset}
        className="transition-all duration-300 ease-out"
      />
      {/* Percentage text */}
      <text
        x="50%"
        y="50%"
        textAnchor="middle"
        dy="0.3em"
        className="text-2xl font-bold fill-white transform rotate-90"
        style={{ transformOrigin: 'center' }}
      >
        {Math.round(progress)}%
      </text>
    </svg>
  );
}
```

**Usage**:
```tsx
// In upload component
<div className="flex flex-col items-center gap-4">
  <ProgressRing progress={uploadProgress} />
  <p className="text-gray-400 text-sm">Uploading photos...</p>
</div>
```

---

### 6. Before/After Slider with Haptic Feedback

```tsx
// components/mobile/before-after-slider.tsx
import { useState, useRef } from 'react';

export function BeforeAfterSlider({ beforeImage, afterImage }) {
  const [sliderPosition, setSliderPosition] = useState(50);
  const containerRef = useRef<HTMLDivElement>(null);
  const hasVibratedAt50 = useRef(false);

  const handleMove = (clientX: number) => {
    if (!containerRef.current) return;

    const rect = containerRef.current.getBoundingClientRect();
    const x = clientX - rect.left;
    const percentage = Math.max(0, Math.min(100, (x / rect.width) * 100));

    setSliderPosition(percentage);

    // Haptic feedback at 50%
    if (Math.abs(percentage - 50) < 2 && !hasVibratedAt50.current) {
      if (window.navigator.vibrate) {
        window.navigator.vibrate(20); // Rigid impact
      }
      hasVibratedAt50.current = true;
    } else if (Math.abs(percentage - 50) > 5) {
      hasVibratedAt50.current = false;
    }
  };

  return (
    <div
      ref={containerRef}
      className="relative w-full aspect-video overflow-hidden rounded-xl"
      onTouchMove={(e) => handleMove(e.touches[0].clientX)}
      onMouseMove={(e) => handleMove(e.clientX)}
    >
      {/* After image (full width) */}
      <img
        src={afterImage}
        alt="After"
        className="absolute inset-0 w-full h-full object-cover"
      />

      {/* Before image (clipped) */}
      <div
        className="absolute inset-0 overflow-hidden"
        style={{ clipPath: `inset(0 ${100 - sliderPosition}% 0 0)` }}
      >
        <img
          src={beforeImage}
          alt="Before"
          className="w-full h-full object-cover"
        />
      </div>

      {/* Slider handle */}
      <div
        className="absolute top-0 bottom-0 w-1 bg-white shadow-lg"
        style={{ left: `${sliderPosition}%` }}
      >
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-10 h-10 bg-white rounded-full shadow-xl flex items-center justify-center">
          <svg className="w-6 h-6 text-gray-900" viewBox="0 0 24 24" fill="none">
            <path d="M15 18l-6-6 6-6" stroke="currentColor" strokeWidth="2" />
            <path d="M9 18l6-6-6-6" stroke="currentColor" strokeWidth="2" />
          </svg>
        </div>
      </div>

      {/* Labels */}
      <div className="absolute top-4 left-4 px-3 py-1 bg-black/60 backdrop-blur-sm rounded-full text-xs text-white font-medium">
        Before
      </div>
      <div className="absolute top-4 right-4 px-3 py-1 bg-black/60 backdrop-blur-sm rounded-full text-xs text-white font-medium">
        After
      </div>
    </div>
  );
}
```

---

### 7. One-Tap Enhance Button

```tsx
// components/mobile/enhance-button.tsx
import { motion } from 'framer-motion';

export function EnhanceButton({ onClick, isLoading = false }) {
  return (
    <motion.button
      onClick={onClick}
      disabled={isLoading}
      whileTap={{ scale: 0.96 }}
      className={`
        w-full h-14 rounded-2xl font-semibold text-white text-lg
        bg-gradient-to-r from-amber-500 to-orange-500
        shadow-[0_8px_24px_rgba(255,184,0,0.3)]
        disabled:opacity-50 disabled:cursor-not-allowed
        transition-all duration-200
      `}
    >
      {isLoading ? (
        <div className="flex items-center justify-center gap-3">
          <div className="w-5 h-5 border-2 border-white/30 border-t-white rounded-full animate-spin" />
          <span>Enhancing...</span>
        </div>
      ) : (
        'Enhance Photo'
      )}
    </motion.button>
  );
}
```

---

### 8. Typography System

```tsx
// styles/typography.tsx
export const typography = {
  h1: 'text-[34px] font-bold leading-tight text-white',
  h2: 'text-[28px] font-semibold leading-tight text-white',
  h3: 'text-[20px] font-semibold leading-snug text-white',
  body: 'text-[17px] font-normal leading-relaxed text-gray-200',
  caption: 'text-[13px] font-normal leading-normal text-gray-400',
  button: 'text-[17px] font-semibold text-white',
};

// Usage:
<h1 className={typography.h1}>Gallery</h1>
<p className={typography.body}>Select photos to enhance</p>
```

---

### 9. Color System (Tailwind Config)

```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        // Background levels
        'bg-0': '#0A0A0A',
        'bg-1': '#1C1C1E',
        'bg-2': '#2C2C2E',
        'bg-3': '#3A3A3C',

        // Primary
        'amber': {
          500: '#FFB800',
        },
        'orange': {
          500: '#FF8C00',
        },

        // Semantic
        'success': '#34C759',
        'error': '#FF3B30',
        'warning': '#FF9500',
        'info': '#007AFF',

        // Text
        'text-primary': '#FFFFFF',
        'text-secondary': '#E5E5E7',
        'text-tertiary': '#8E8E93',
        'text-disabled': '#48484A',
      },
    },
  },
};
```

---

### 10. Haptic Feedback Utility

```tsx
// utils/haptics.ts
export const haptics = {
  light: () => {
    if (window.navigator.vibrate) {
      window.navigator.vibrate(10);
    }
  },

  medium: () => {
    if (window.navigator.vibrate) {
      window.navigator.vibrate(20);
    }
  },

  rigid: () => {
    if (window.navigator.vibrate) {
      window.navigator.vibrate([20, 10, 20]);
    }
  },

  success: () => {
    if (window.navigator.vibrate) {
      window.navigator.vibrate([10, 50, 10]);
    }
  },

  error: () => {
    if (window.navigator.vibrate) {
      window.navigator.vibrate([30, 50, 30, 50, 30]);
    }
  },
};

// Usage:
import { haptics } from '@/utils/haptics';

<button onClick={() => {
  haptics.light();
  handleUpload();
}}>
  Upload
</button>
```

---

## Quick Start Checklist

### Foundation
- [ ] Install Framer Motion: `npm install framer-motion`
- [ ] Add Tailwind config with color system and animations
- [ ] Create `typography.tsx` with text styles
- [ ] Create `haptics.ts` utility

### Components (Priority Order)
1. [ ] `TabBar` — Bottom navigation with Liquid Glass
2. [ ] `GlassCard` — Glassmorphism container
3. [ ] `EnhanceButton` — Primary CTA with gradient
4. [ ] `ProgressRing` — Upload/processing indicator
5. [ ] `ImageSkeleton` — Loading state with shimmer
6. [ ] `PhotoGrid` — Multi-select gallery
7. [ ] `BeforeAfterSlider` — Comparison view

### Testing
- [ ] Test haptic feedback on iOS device (Safari)
- [ ] Test tab bar blur on scroll
- [ ] Test photo grid long-press on mobile
- [ ] Test slider at 50% haptic trigger
- [ ] Test skeleton → content transition

---

## Performance Tips

### Mobile Optimization
1. **Lazy Load Images**: Use `loading="lazy"` on all `<img>` tags
2. **Virtualize Long Lists**: Use `react-window` for galleries >50 images
3. **Debounce Slider**: Throttle slider position updates to 60fps
4. **Preload Critical Images**: Use `<link rel="preload">` for above-fold images
5. **WebP Format**: Serve WebP with JPEG fallback for 30% smaller files

### Glassmorphism Performance
- Modern iOS/Android GPUs handle `backdrop-filter: blur(20px)` efficiently
- Avoid blur on elements that animate (causes repaints)
- Use fixed blur values (not animated blur radius)

### Haptic Best Practices
- Only vibrate on intentional actions (not accidental taps)
- Test on physical devices (simulators don't vibrate)
- Respect user's accessibility settings (reduced motion)

---

## Resources

- **Full Research Report**: `/Users/nafiurrahman/Desktop/Foodshot/MOBILE_APP_RESEARCH.md`
- **Tailwind CSS**: https://tailwindcss.com/docs
- **Framer Motion**: https://www.framer.com/motion/
- **iOS Haptic Guidelines**: https://developer.apple.com/design/human-interface-guidelines/haptics

---

**Last Updated**: 2026-03-10
