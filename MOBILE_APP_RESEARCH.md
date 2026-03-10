# CraveMode AI — Mobile App UI/UX Research Report
*Premium Food Photography Enhancement App — 2026 Design Standards*

---

## Executive Summary

This research identifies specific, implementable UI/UX patterns from leading food photography apps, AI enhancement tools, and creative platforms to make CraveMode AI feel premium on mobile. The report focuses on dark theme implementations, animation patterns, and micro-interactions that define best-in-class mobile experiences in 2026.

**Key Insight**: Premium mobile apps in 2026 combine **Dark Glassmorphism** (translucent cards over vibrant gradients), **Liquid Glass UI** (Apple's iOS 26 blur aesthetic), and **subtle haptic micro-interactions** to create sophisticated, tactile experiences.

---

## 1. Food Photography Apps — UI Patterns

### Foodie (LINE Corp) — Market Leader
**Downloads**: 100M+ on Play Store
**Core Strength**: Live filter application with instant preview

#### Specific UI Patterns
- **Filter Gallery**: Horizontal scrollable strip at bottom, 30+ filters with thumbnail previews showing the effect on current image
- **Smart Guide Overlay**: Geometric grid overlay for top-down food shots (circle/square guides for plate alignment)
- **Before/After Paywall**: Carousel showcasing before-and-after examples as value proposition before showing premium filters
- **Recipe System**: Users can save custom editing formulas and share them (social proof + engagement loop)
- **Live Filter Toggle**: Real-time camera preview with filter applied (no need to shoot first, then edit)

#### Color & Typography
- Bright interface with selective dark mode support
- High contrast filter names (bold sans-serif) against blurred image backgrounds
- Filter names use food-related terms: "Yum", "Crispy", "Chewy", "Fresh"

**Source**: [Foodie - Filter & Film Camera App Showcase](https://screensdesign.com/showcase/foodie-filter-film-camera)

---

### FoodieLens — Simplified Editor
**Downloads**: 440K+
**Core Strength**: One-tap enhancement for non-photographers

#### Specific UI Patterns
- **One-Tap Enhance**: Single primary CTA labeled "Enhance" (no sliders for casual users)
- **Progressive Disclosure**: Advanced editing tools hidden behind "More" menu
- **Export Presets**: Quick export buttons for Instagram (1:1), Stories (9:16), Facebook (1200x630)

**Source**: [FoodieLens - Food Photo Editor App](https://apps.apple.com/us/app/foodielens-food-photo-editor/id1002182411)

---

### Before/After Slider Pattern
Multiple apps use interactive comparison sliders:

#### Implementation Details
- **Drag Modes**: Horizontal, vertical, oblique, or reversed oblique slider orientation
- **Manual Control**: User drags slider handle to reveal before/after
- **Auto-Play Option**: Slider animates back-and-forth on first view (3-second loop)
- **Lock/Unlock Toggle**: Lock slider at 50% for side-by-side comparison

**Premium Pattern**: Add haptic feedback at 50% slider position (midpoint vibration)

**Source**: [Before and After Pro Slider App](https://apps.apple.com/us/app/before-and-after-pro-slider/id680502514)

---

## 2. AI Photo Enhancement Apps — Premium UX Patterns

### Remini — AI Enhancer (100M+ Downloads)
**Business Model**: Freemium with watermarked previews

#### Specific UI Patterns
- **Batch Processing Queue**: Upload multiple photos, process in background, notify when ready
- **HD/4K Toggle**: Clear pricing tier indicator on export screen (Free: 720p, Pro: 4K)
- **Watermark Preview**: Show full enhanced result with watermark, remove on upgrade (drives conversions)
- **Progress Rings**: Circular progress indicator with percentage during AI processing (2-4 min typical)

#### Loading State
- **Skeleton Screen**: Blurred placeholder image with shimmer gradient overlay
- **AI Processing Message**: "Enhancing details..." / "Removing blur..." / "Upscaling to 4K..." (rotating messages)

**Source**: [Remini - AI Photo Enhancer](https://remini.ai/)

---

### Lensa — Artistic Filters (Prisma Labs)
**Famous For**: Magic Avatars (AI-generated portraits)

#### Specific UI Patterns
- **Multi-Upload Flow**: Select 10-20 selfies → AI generates 50+ avatar variations
- **Style Grid**: 3-column masonry grid showing different artistic styles (watercolor, cyberpunk, anime)
- **Pack System**: Sell avatar packs (e.g., "Cyber Punk Pack" — 10 variations for $3.99)
- **Social Sharing Loop**: One-tap share to Instagram Stories with branding overlay

#### Premium Feel
- **Gradient Cards**: Each style card has subtle gradient overlay (blue-purple, pink-orange)
- **Soft Shadows**: Cards have 8px blur, 2px offset shadow for depth
- **Haptic on Select**: Light haptic tap when selecting a style

**Source**: [Lensa App](https://lensa.app/)

---

### Prisma — Artistic AI Photo Editor
**Core Strength**: Turn photos into artwork (Picasso, Van Gogh styles)

#### Specific UI Patterns
- **Filter Intensity Slider**: After selecting style, adjust intensity (0-100%) with live preview
- **Masking Tool**: Apply filters to specific areas (e.g., keep face realistic, stylize background)
- **Export Crop Presets**: Quick crop buttons for Instagram (1:1), Story (9:16), Wide (16:9)

**Source**: [Prisma v4.6.8 Mod APK](https://getmodpc.net/prisma/)

---

### PhotoRoom — Background Removal
**Use Case**: Product photography, e-commerce

#### Specific UI Patterns
- **Instant Background Removal**: Upload → automatic cutout in <2 seconds
- **Background Library**: Horizontal scrollable backgrounds (solid colors, gradients, studio scenes)
- **Shadow Toggle**: Add realistic drop shadow to cutout object (adjustable opacity)

**Premium Mobile Pattern**: Use this for CraveMode's "Remove Background" feature (isolate dish from messy restaurant context)

**Source**: [PhotoRoom Background Removal](https://autogpt.net/top-mobile-ai-photo-enhancers-editors/)

---

### VSCO — Premium Photo Editor
**Subscription Model**: $29.99/year for 200+ presets

#### Specific UI Patterns
- **Studio Tab**: Camera roll auto-syncs, no import needed (seamless workflow)
- **Drafts Tab**: In-progress edits auto-save, return later
- **Preset Thumbnails**: Each preset shows thumbnail of current image with filter applied
- **Blur Tool (Premium)**: Circular and linear blur with adjustable size, direction, angle

#### Dark Mode Implementation
- **Background**: #0F0F0F (true black for OLED battery savings)
- **Cards**: #1C1C1E with 4px rounded corners
- **Text**: #FFFFFF primary, #8E8E93 secondary (iOS gray-5)
- **Accent**: #FFA500 (orange) for premium features

**Source**: [VSCO Dark Mode Guide](https://support.vsco.co/hc/en-us/articles/360059844211-How-to-enable-Dark-Mode)

---

## 3. Creative AI Apps — Upload → Generate → Gallery Flow

### Runway — Professional AI Video Platform
**Target Audience**: Filmmakers, content creators

#### Specific UI Patterns
- **Project-Based Workflow**: Create "Project" → upload assets → generate variations → export
- **Canvas Mode**: Visual timeline for sequencing multiple AI-generated clips
- **Model Selector**: Dropdown to choose AI model (Gen-3 Alpha Turbo vs. Gen-4 — speed vs. quality)
- **Credit Display**: Persistent top-right indicator showing remaining credits (e.g., "120 credits")

#### Generation Flow
1. Upload reference image/video
2. Write text prompt (optional)
3. Select duration (5s, 10s, 15s)
4. Click "Generate" → queue (2-4 min processing)
5. Thumbnail appears in gallery with play icon
6. Click to preview → export options

**Premium Pattern**: Show cost estimate BEFORE generating (e.g., "This will use 10 credits. Continue?")

**Source**: [Runway AI Review 2026](https://max-productive.ai/ai-tools/runwayml/)

---

### Pika — Fast AI Video Generation
**Key Differentiator**: Fastest generation speed (<2 min)

#### Specific UI Patterns
- **Pikaffects**: Fun creative effects (Squish It, Melt It, Explode It) as one-tap modifiers
- **Speed Slider**: Choose Fast (1 min, lower quality) vs. Slow (4 min, higher quality)
- **Aspect Ratio Toggle**: 1:1, 9:16, 16:9 quick-select buttons (no manual crop)

#### Mobile App (iOS)
- **Bottom Sheet Upload**: Tap "+" → bottom sheet slides up with "Camera", "Photo Library", "Paste Link"
- **Processing Queue**: Horizontal scrollable queue at bottom showing in-progress generations

**Source**: [Pika AI Comparison 2026](https://pikaais.com/comparison/)

---

### Kaiber — Music-Synced AI Videos
**Niche**: Music videos, beat-synced animations

#### Specific UI Patterns
- **Audio Upload First**: Workflow starts with uploading audio track (MP3, WAV)
- **Beat Detection**: AI analyzes beats-per-minute (BPM) and suggests animation speed
- **Style Transfer**: Upload reference image (e.g., food photo) → AI animates it to music beat
- **Timeline Scrubber**: Waveform visualization with playhead (preview how visuals sync to audio)

**Premium Pattern for CraveMode**: Sync food reveal animations to trending audio clips (TikTok sounds)

**Source**: [Kaiber AI Superstudio](https://www.kaiber.ai/superstudio/)

---

## 4. Marvie iOS UI Kit — Signature Design Patterns

### Overview
**Created By**: Blacklead Studio
**Availability**: Free for Sketch & Figma
**Screens**: 60+ ready-to-use mobile screens
**Components**: 50+ with Light & Dark Mode support

### Key Characteristics
- **Color Palette**: Bright and friendly (blue primary, orange accent)
- **Typography**: SF Pro (system font) for consistency
- **Spacing**: 8px grid system (multiples of 8: 8, 16, 24, 32, 40)
- **Rounded Corners**: 12px for cards, 8px for buttons, 4px for inputs

### Signature Patterns

#### 1. Card Design
- **Background**: #FFFFFF (light), #1C1C1E (dark)
- **Padding**: 16px all sides
- **Shadow**: 0px 4px 12px rgba(0,0,0,0.08)
- **Border**: None (shadow creates separation)

#### 2. Bottom Navigation (Tab Bar)
- **Height**: 83px (includes safe area)
- **Background**: Blurred with 90% opacity (glassmorphism)
- **Active Icon**: Primary color with 8px rounded background
- **Inactive Icon**: Gray (#8E8E93)
- **Label**: 10pt SF Pro Text (below icon)

#### 3. Upload Button
- **Style**: Large rounded rectangle (327x56px on 375px screen width)
- **Icon**: Plus icon or upload icon (24x24px)
- **Gradient Background**: Linear gradient (blue to purple)
- **Haptic**: Medium impact feedback on tap

#### 4. Image Grid (Gallery)
- **Layout**: 3-column grid
- **Spacing**: 2px gap between images (tight grid)
- **Aspect Ratio**: 1:1 (square thumbnails)
- **Selection Indicator**: Checkmark in top-right corner with blue circle background

**Source**: [Marvie iOS UI Kit on UI8](https://www.ui8.net/blacklead-studio/products/marvie-ios-app-ui-kit)

---

## 5. Mobile App UI Trends 2025-2026 — Dark Theme & Premium Design

### Dark Glassmorphism — The Dominant Trend

**Definition**: Translucent, frosted-glass UI elements over vibrant gradient backgrounds in dark mode.

#### Core Techniques
1. **Ambient Gradients**: Vibrant color orbs (deep purples, neon blues, hot pinks) floating behind UI
2. **Translucent Cards**: 10-20% opacity white cards with backdrop blur (20-40px)
3. **Refined Borders**: 1px borders (rgba(255,255,255,0.1)) for crisp separation
4. **Soft Shadows**: Subtle inner/outer shadows for depth without overwhelming

#### Code Example (CSS)
```css
.glassmorphic-card {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(30px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow:
    0 8px 32px rgba(0, 0, 0, 0.2),
    inset 0 1px 0 rgba(255, 255, 255, 0.1);
  border-radius: 16px;
}
```

**Mobile Performance**: Modern GPUs (A17 Pro, Snapdragon 8 Gen 3) handle blur/shadow efficiently — no FPS drop.

**Source**: [Dark Glassmorphism: The Aesthetic That Will Define UI in 2026](https://medium.com/@developer_89726/dark-glassmorphism-the-aesthetic-that-will-define-ui-in-2026-93aa4153088f)

---

### iOS 26 Liquid Glass — Apple's Tab Bar Evolution

#### What Changed in iOS 26 (WWDC 2025)
- **Old**: Opaque white/black tab bars with flat icons
- **New**: Translucent tab bars with blur + gradient + subtle layering

#### Design Characteristics
- **Blur Effect**: System material blur (automatically adjusts based on content behind)
- **Layering**: Tab bar feels like it's floating above content (not sitting on top)
- **Edge Fading**: Soft gradient fade at top edge (smooth transition from content to tab bar)
- **Light Bending**: Realistic refraction effect (not just opacity — actual light distortion)

#### Implementation in SwiftUI
```swift
TabView {
  ContentView()
    .tabItem {
      Label("Home", systemImage: "house")
    }
}
.tabBarMinimizeBehavior(.onScrollDown) // Auto-hide on scroll
```

**Key for CraveMode**: Use Liquid Glass for bottom tab bar to match iOS 26 system aesthetics.

**Source**: [Exploring tab bars on iOS 26 with Liquid Glass](https://www.donnywals.com/exploring-tab-bars-on-ios-26-with-liquid-glass/)

---

### Eye-Friendly Design (Beyond Basic Dark Mode)

#### Advanced Features in 2026
- **Warm Color Shifting**: Reduce blue light after sunset (adaptive color temperature)
- **Softer Color Schemes**: Replace pure black (#000000) with dark gray (#0F0F0F) to reduce eye strain
- **Configurable Text Size**: User-adjustable font scaling (100%-200%)
- **Material You Integration (Android)**: App colors adapt to user's wallpaper

#### Statistics
- **81.9%** of Android users use dark mode on their phones
- Apps with dark mode see **longer browsing sessions** (study cited in Envato research)

**Source**: [12 Mobile App UI/UX Design Trends for 2026](https://www.designstudiouiux.com/blog/mobile-app-ui-ux-design-trends/)

---

### Neumorphism 2.0 — Tactile Feel with Better Accessibility

**Original Neumorphism Problem**: Low contrast (unreadable for visually impaired users)

**2026 Solution**: Soft surfaces + stronger contrast + larger typography

#### Design Pattern
- **Raised Elements**: Light shadow on top-left, dark shadow on bottom-right (simulates depth)
- **Pressed Elements**: Inset shadows (element looks pushed into surface)
- **Background**: Single-color background (light gray or dark gray) for all surfaces
- **Contrast**: WCAG AA compliant (4.5:1 ratio for text)

**Use Case for CraveMode**: Apply neumorphism to buttons (Upload, Generate) for tactile feel.

**Source**: [9 Mobile App Design Trends for 2026](https://uxpilot.ai/blogs/mobile-app-design-trends)

---

## 6. Specific Design Elements — Implementation Guide

### Tab Bar Design (Bottom Navigation)

#### Best Practices 2026
- **Blur Background**: 95% opacity + backdrop-filter blur (15-20px)
- **Active Indicator**: Filled background behind icon (8px rounded rectangle)
- **Inactive State**: Icon-only with 60% opacity
- **Icon Size**: 24x24px (consistent across all tabs)
- **Label**: 10-12pt below icon (optional — hide on small screens)
- **Spacing**: Evenly distribute tabs (no clustering)

#### CraveMode Tab Bar Structure
| Tab | Icon | Active Color | Screen |
|-----|------|--------------|--------|
| Enhance | camera.filters | Amber (#FFB800) | Upload/Edit |
| Gallery | photo.on.rectangle | Amber (#FFB800) | Results Grid |
| Queue | clock.arrow.circlepath | Amber (#FFB800) | Processing Status |
| Profile | person.crop.circle | Amber (#FFB800) | Account/Settings |

**Source**: [iOS Tab Bar Liquid Glass](https://www.donnywals.com/exploring-tab-bars-on-ios-26-with-liquid-glass/)

---

### Card Design — Gradients, Glassmorphism, Shadows

#### Premium Card Pattern (2026)
```css
.premium-food-card {
  /* Base */
  background: linear-gradient(
    135deg,
    rgba(255, 184, 0, 0.1) 0%,
    rgba(255, 87, 34, 0.1) 100%
  );
  backdrop-filter: blur(20px);
  border-radius: 16px;
  padding: 16px;

  /* Border */
  border: 1px solid rgba(255, 255, 255, 0.1);

  /* Shadow */
  box-shadow:
    0 8px 32px rgba(0, 0, 0, 0.3),
    inset 0 1px 0 rgba(255, 255, 255, 0.1);

  /* Interaction */
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.premium-food-card:hover {
  transform: translateY(-4px);
  box-shadow:
    0 16px 48px rgba(0, 0, 0, 0.4),
    inset 0 1px 0 rgba(255, 255, 255, 0.2);
}
```

**Gradient Direction**: 135deg (diagonal top-left to bottom-right) creates depth.

**Source**: [Glassmorphism: What It Is and How to Use It in 2026](https://invernessdesignstudio.com/glassmorphism-what-it-is-and-how-to-use-it-in-2026)

---

### Upload Experience — Drag Gestures, Photo Grid, Selection Feedback

#### Mobile Upload Best Practices

**Key Insight**: Traditional drag-and-drop doesn't work on mobile (no mouse). Use touch gestures instead.

#### Touch Gesture Patterns
1. **Tap to Upload**: Primary button opens native file picker (iOS: PHPickerViewController, Android: Intent.ACTION_GET_CONTENT)
2. **Long-Press to Multi-Select**: Instagram pattern — long-press first image → swipe right to select more
3. **Drag to Reorder**: After selection, long-press + drag to reorder upload queue

#### Visual Feedback
- **Drop Zone**: Dashed border (2px) with pulsing animation (scale 1.0 → 1.02 → 1.0)
- **File Hover**: Drop zone background changes color when dragging file over it
- **Loading Spinner**: Circular progress indicator during upload
- **Success Message**: Checkmark animation + haptic feedback + green toast

#### Photo Grid Selection
- **Layout**: 3-column grid (tight 2px gaps)
- **Selection Indicator**: Blue checkmark circle in top-right corner
- **Multi-Select Mode**: Tap-and-hold first image → grid enters multi-select (checkboxes appear on all images)
- **Counter Badge**: Bottom bar shows "3 selected" with deselect all button

**Source**: [File upload UI tips for designers](https://www.eleken.co/blog-posts/file-upload-ui)

---

### Processing / Loading States — Skeleton, Shimmer, Progress

#### Skeleton Screen Best Practices

**When to Use**:
- **2-10 seconds**: Use skeleton screen
- **<2 seconds**: Use spinner
- **>10 seconds**: Use progress bar with percentage

#### Design Pattern
```css
.skeleton-image {
  background: linear-gradient(
    90deg,
    #1C1C1E 0%,
    #2C2C2E 50%,
    #1C1C1E 100%
  );
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
  border-radius: 12px;
}

@keyframes shimmer {
  0% { background-position: -200% 0; }
  100% { background-position: 200% 0; }
}
```

#### Shimmer Direction
- **Left to Right**: Matches reading direction (Western audiences)
- **Wave Speed**: 1.5s (not too fast to be distracting)
- **Gradient Width**: 200% (smooth gradient transition)

#### Skeleton Layout Accuracy
**Critical Rule**: Skeleton MUST match actual content layout. If content appears in different position, user trust breaks.

**CraveMode Example**:
```
[  Image Skeleton (16:9)  ]
[Title—————————————]
[Subtitle——————]
[Button———]
```

**Source**: [Skeleton Screens 101 - Nielsen Norman Group](https://www.nngroup.com/articles/skeleton-screens/)

---

### Gallery Presentation — Masonry vs. Grid

#### Masonry Layout (Pinterest-style)

**Pros**:
- No wasted space (images of different aspect ratios fit naturally)
- Visually interesting (varied heights)
- Good for mixed content (photos + videos)

**Cons**:
- Harder to scan (no predictable rows)
- Slower rendering (complex layout calculations)
- Not ideal for uniform content

**When to Use**: Mixed aspect ratios (9:16 + 1:1 + 16:9 outputs)

#### Grid Layout (Instagram-style)

**Pros**:
- Fast rendering (simple CSS Grid)
- Predictable scanning pattern
- Works well on all screen sizes
- Easy to implement infinite scroll

**Cons**:
- Crops images to fit grid (1:1 aspect ratio)
- Less dynamic visually

**When to Use**: Uniform aspect ratios (all 1:1 outputs)

#### CraveMode Recommendation
**Use Adaptive Grid**:
- **Gallery View**: 2-column masonry (preserves aspect ratios, shows full images)
- **Thumbnail View**: 3-column grid (1:1 crops for faster scanning)
- **Toggle**: Switch between views with icon button (grid icon ⇔ masonry icon)

**Source**: [Masonry Layout Options](https://masonry.desandro.com/layout)

---

### Typography Hierarchy

#### 2026 Standard: SF Pro (iOS) + Inter (Web/Android)

**Why SF Pro**:
- Optimized for Apple hardware (Retina displays)
- Variable font (supports Dynamic Type for accessibility)
- Consistent with iOS system fonts

**Why Inter**:
- Free and open-source
- Excellent legibility at small sizes (designed for screens)
- Wide range of weights (Thin → Black)

#### Typography Scale (CraveMode)

| Element | Font | Size | Weight | Color (Dark) |
|---------|------|------|--------|--------------|
| H1 (Screen Title) | SF Pro Display / Inter | 34pt | Bold (700) | #FFFFFF |
| H2 (Section Header) | SF Pro Display / Inter | 28pt | Semibold (600) | #FFFFFF |
| H3 (Card Title) | SF Pro Text / Inter | 20pt | Semibold (600) | #FFFFFF |
| Body | SF Pro Text / Inter | 17pt | Regular (400) | #E5E5E7 |
| Caption | SF Pro Text / Inter | 13pt | Regular (400) | #8E8E93 |
| Button | SF Pro Text / Inter | 17pt | Semibold (600) | #FFFFFF |

**Line Height**: 1.3x for headlines, 1.5x for body text

**Source**: [Mobile App Typography: Best Practices & Pro Tips](https://www.zignuts.com/blog/mastering-mobile-app-typography-best-practices-pro-tips)

---

### Micro-Interactions and Haptic Patterns

#### Haptic Feedback Types (iOS)

| Event | Haptic Type | When to Use |
|-------|-------------|-------------|
| Button Tap | Light Impact | All tappable elements |
| Toggle Switch | Selection | On/off states |
| Success Action | Notification Success | Upload complete, generation done |
| Error Action | Notification Error | Upload failed, invalid input |
| Slider at 50% | Rigid Impact | Before/after slider at midpoint |
| Photo Selected | Light Impact | Multi-select in gallery |
| Swipe to Delete | Rigid Impact | Destructive action confirmation |

#### Micro-Interaction Patterns

**1. Button Press**
```css
.button {
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
}

.button:active {
  transform: scale(0.96);
}
```

**2. Card Hover (Web) / Long-Press (Mobile)**
```css
.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 16px 48px rgba(0, 0, 0, 0.4);
}
```

**3. Checkbox Selection**
```css
.checkbox {
  transition: all 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55);
}

.checkbox:checked {
  transform: scale(1.1) rotate(360deg);
}
```

**4. Progress Ring** (for upload/processing)
```jsx
<svg width="100" height="100">
  <circle
    cx="50" cy="50" r="45"
    stroke="#1C1C1E"
    strokeWidth="8"
    fill="none"
  />
  <circle
    cx="50" cy="50" r="45"
    stroke="#FFB800"
    strokeWidth="8"
    fill="none"
    strokeDasharray={`${progress * 2.827} 282.7`}
    transform="rotate(-90 50 50)"
  />
</svg>
```

**Source**: [Mastering Haptic Micro-Interactions](https://earlams.co.uk/mastering-haptic-micro-interactions-deep-technical-strategies-for-enhanced-mobile-engagement/)

---

### Color Usage in Dark Themes

#### CraveMode Color Palette (Dark Theme)

**Background Colors**:
- **Level 0 (Background)**: #0A0A0A (true black with warm undertone)
- **Level 1 (Surface)**: #1C1C1E (iOS dark gray)
- **Level 2 (Elevated Surface)**: #2C2C2E (cards, modals)
- **Level 3 (Overlay)**: #3A3A3C (dropdowns, popovers)

**Primary Colors**:
- **Amber (Primary CTA)**: #FFB800 (warm gold)
- **Orange (Accent)**: #FF8C00 (vibrant tangerine)
- **Gradient**: Linear from Amber → Orange (135deg)

**Semantic Colors**:
- **Success**: #34C759 (iOS green)
- **Error**: #FF3B30 (iOS red)
- **Warning**: #FF9500 (iOS orange)
- **Info**: #007AFF (iOS blue)

**Text Colors**:
- **Primary Text**: #FFFFFF (100% white)
- **Secondary Text**: #E5E5E7 (90% white)
- **Tertiary Text**: #8E8E93 (iOS gray-5)
- **Disabled Text**: #48484A (iOS gray-6)

#### Gradient Best Practices
- **Direction**: 135deg (diagonal) creates depth
- **Warm Tones**: Use amber/gold/orange for food (appetite appeal)
- **Avoid**: Cool blues/greens for food content (unappetizing)

**Source**: [Mobile App Color Palette Dark Theme Trends](https://elements.envato.com/learn/color-scheme-trends-in-mobile-app-design)

---

## 7. Implementation Roadmap for CraveMode Mobile

### Phase 1: Foundation (Week 1-2)
- [ ] Implement Liquid Glass tab bar with blur + gradients
- [ ] Set up dark glassmorphism card system
- [ ] Define typography scale (SF Pro / Inter)
- [ ] Implement haptic feedback for all tappable elements
- [ ] Create amber/gold gradient system

### Phase 2: Upload Flow (Week 3-4)
- [ ] Build photo grid multi-select (Instagram pattern)
- [ ] Add long-press + swipe-right selection
- [ ] Implement drag-to-reorder in upload queue
- [ ] Add upload progress rings with shimmer
- [ ] Create skeleton screens for loading states

### Phase 3: Enhancement UI (Week 5-6)
- [ ] Build before/after slider with haptic at 50%
- [ ] Add live filter preview (no need to apply first)
- [ ] Implement "One-Tap Enhance" primary CTA
- [ ] Create advanced editing tools (progressive disclosure)
- [ ] Add export format quick-select buttons (1:1, 9:16, 16:9)

### Phase 4: Gallery & Results (Week 7-8)
- [ ] Build 2-column masonry layout (preserves aspect ratios)
- [ ] Add toggle to 3-column grid (1:1 crops)
- [ ] Implement infinite scroll with skeleton placeholders
- [ ] Add filter/sort options (date, type, status)
- [ ] Create swipe-to-delete with haptic confirmation

### Phase 5: Micro-Interactions (Week 9-10)
- [ ] Add button press scale animations (0.96)
- [ ] Implement card lift on hover/long-press
- [ ] Add success/error haptic notifications
- [ ] Create loading spinner with ambient gradient
- [ ] Add progress ring animations for AI processing

---

## 8. Key Takeaways — Premium vs. Basic Feel

### What Makes Mobile Apps Feel "Premium" in 2026

#### Premium Apps Have:
✅ **Dark Glassmorphism**: Translucent cards over vibrant gradients (not flat colors)
✅ **Liquid Glass Effects**: Blurred tab bars with layering (not opaque solid bars)
✅ **Haptic Feedback**: Tactile confirmation for every interaction (not just visual)
✅ **Skeleton Screens**: Shimmer placeholders during loading (not spinners)
✅ **Micro-Animations**: Subtle scale/lift on interactions (not static)
✅ **Consistent Typography**: System fonts with clear hierarchy (not random sizes)
✅ **Warm Dark Theme**: #0F0F0F backgrounds with amber accents (not pure black)
✅ **Progressive Disclosure**: Hide advanced features, show on demand (not overwhelming)
✅ **Cost Transparency**: Show pricing before actions (not surprise charges)

#### Basic Apps Have:
❌ Flat white/black cards with no depth
❌ Opaque solid tab bars
❌ No haptic feedback
❌ Generic loading spinners
❌ No animation on interactions
❌ Inconsistent font sizes
❌ Pure black backgrounds (#000000)
❌ All options visible at once (cluttered)
❌ Hidden pricing until checkout

---

## 9. Competitive Analysis Summary

| App | Strength | Weakness | CraveMode Can Learn |
|-----|----------|----------|---------------------|
| **Foodie** | Live filter preview, smart guides | Too many filters (overwhelming) | Use live preview, limit to 5-10 presets |
| **Remini** | AI enhancement quality, batch processing | Watermarked previews (frustrating) | Show full preview, lock export |
| **Lensa** | Social sharing loop, avatar packs | Long processing (10+ min) | Keep processing under 2 min |
| **VSCO** | Premium presets, seamless workflow | Expensive ($29.99/year) | Compete on price ($297/year = $24.75/mo) |
| **Runway** | Professional-grade results | Complex UI (steep learning curve) | Simplify to one-tap enhance |
| **Pika** | Fastest generation (<2 min) | Limited customization | Balance speed + control |
| **PhotoRoom** | Instant background removal | Limited to product shots | Apply to food photography |

---

## 10. Sources & References

### Food Photography Apps
- [Foodie - Filter & Film Camera App Showcase](https://screensdesign.com/showcase/foodie-filter-film-camera)
- [FoodieLens - Food Photo Editor App](https://apps.apple.com/us/app/foodielens-food-photo-editor/id1002182411)
- [Before and After Pro Slider App](https://apps.apple.com/us/app/before-and-after-pro-slider/id680502514)

### AI Photo Enhancement Apps
- [Remini - AI Photo Enhancer](https://remini.ai/)
- [Lensa App](https://lensa.app/)
- [Prisma v4.6.8 Mod APK](https://getmodpc.net/prisma/)
- [Top Mobile AI Photo Enhancers/Editors](https://autogpt.net/top-mobile-ai-photo-enhancers-editors/)
- [VSCO Dark Mode Guide](https://support.vsco.co/hc/en-us/articles/360059844211-How-to-enable-Dark-Mode)

### Creative AI Apps
- [Runway AI Review 2026](https://max-productive.ai/ai-tools/runwayml/)
- [Pika AI Comparison 2026](https://pikaais.com/comparison/)
- [Kaiber AI Superstudio](https://www.kaiber.ai/superstudio/)

### Marvie iOS UI Kit
- [Marvie iOS UI Kit on UI8](https://www.ui8.net/blacklead-studio/products/marvie-ios-app-ui-kit)
- [Marvie - Free iOS UI Kit for Sketch and Figma](https://www.uistore.design/items/marvie-ios-ui-kit-for-sketch-and-figma/)

### Mobile App UI Trends
- [Dark Glassmorphism: The Aesthetic That Will Define UI in 2026](https://medium.com/@developer_89726/dark-glassmorphism-the-aesthetic-that-will-define-ui-in-2026-93aa4153088f)
- [Exploring tab bars on iOS 26 with Liquid Glass](https://www.donnywals.com/exploring-tab-bars-on-ios-26-with-liquid-glass/)
- [12 Mobile App UI/UX Design Trends for 2026](https://www.designstudiouiux.com/blog/mobile-app-ui-ux-design-trends/)
- [9 Mobile App Design Trends for 2026](https://uxpilot.ai/blogs/mobile-app-design-trends)
- [Glassmorphism: What It Is and How to Use It in 2026](https://invernessdesignstudio.com/glassmorphism-what-it-is-and-how-to-use-it-in-2026)

### Design Patterns
- [Skeleton Screens 101 - Nielsen Norman Group](https://www.nngroup.com/articles/skeleton-screens/)
- [Mastering Haptic Micro-Interactions](https://earlams.co.uk/mastering-haptic-micro-interactions-deep-technical-strategies-for-enhanced-mobile-engagement/)
- [File upload UI tips for designers](https://www.eleken.co/blog-posts/file-upload-ui)
- [Masonry Layout Options](https://masonry.desandro.com/layout)
- [Mobile App Typography: Best Practices & Pro Tips](https://www.zignuts.com/blog/mastering-mobile-app-typography-best-practices-pro-tips)
- [Mobile App Color Palette Dark Theme Trends](https://elements.envato.com/learn/color-scheme-trends-in-mobile-app-design)

---

**Report Generated**: 2026-03-10
**Research Focus**: Premium mobile UI/UX for food photography enhancement apps
**Target Platform**: iOS (primary), Android (secondary)
**Design System**: Dark Glassmorphism + Liquid Glass + Haptic Micro-Interactions
