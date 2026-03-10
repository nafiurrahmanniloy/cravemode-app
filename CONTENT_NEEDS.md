# CraveMode AI — Content Production Brief

## Why We Need This Content

CraveMode AI is a done-for-you food photo and video enhancement service. Our website IS our portfolio — every section needs to overflow with stunning food visuals because that's literally what we sell. Visitors need to see our output everywhere they scroll so they think: "I want MY food to look like that."

Our competitors (Higgsfield AI, Kie AI) flood their websites with generated content. Every scroll reveals more output. That's the standard we're matching — and exceeding — for the food vertical.

### The Problem Right Now

We have 23 videos and 6 before/after photo pairs. Our website has 3 video sections and 5 photo sections. The same clips and images repeat across multiple sections — a visitor scrolling through sees the same burger video 3 times. This kills credibility. A premium service can't look like it only has 23 examples.

### What We're Building

The website has these content-heavy sections (in scroll order):

1. **Hero** — 30 floating food photos surrounding the headline (first impression)
2. **How It Works** — 1 before/after pair + 1 video showing the process
3. **Video Showcase Grid** — 8 of our best video clips in a cinematic layout
4. **Video Spotlight** — Auto-playing compilation reel (uses all videos, rapid rotation)
5. **Giant Text Reveal** — 10 food photos visible through giant "CRAVE MODE" letterforms
6. **Browse by Cuisine** — 48 videos organized into 12 food categories (users click tabs to explore)
7. **Before/After Slider** — 15 interactive drag-to-compare transformations
8. **Pricing Section** — 10 enhanced photos rotating behind the pricing cards

Every section has a different visual treatment, so the same photo/video feels fresh even if reused in 1-2 places. But we still need enough volume that no single asset carries too much weight.

---

## What We Currently Have

### Videos (23 total)
All stored in `/public/cravemode/videos/`. Portrait 9:16 format, 3-10 seconds each.

| File | Status |
|------|--------|
| video-1.mp4 | Working |
| video-2.mp4 | Working |
| video-3.mp4 | Working |
| video-4.mp4 | Working |
| video-5.mp4 | Working |
| video-6.mp4 | BROKEN — corrupted filename, excluded from site |
| video-7.mp4 | Working |
| video-8.mp4 | Working |
| video-9.mp4 | Working |
| video-10.mp4 | Working |
| video-12.mp4 | Working |
| video-13.mp4 | Working |
| video-14.mp4 | Working (missing thumbnail) |
| video-16.mp4 | Working |
| video-18.mp4 | Working |
| video-19.mp4 | Working |
| video-20.mp4 | Working |
| video-21.mp4 | Working |
| video-22.mp4 | Working |
| video-23.mp4 | Working |
| video-24.mp4 | Working |
| video-25.mp4 | Working |
| video-26.mp4 | Working |
| video-27.mp4 | Working |

**Missing numbers (gaps):** 6 (corrupted), 11, 15, 17 — these were never created or were deleted.

### Video Thumbnails (22 total)
Stored in `/public/cravemode/videos/thumbnails/`. PNG format, one per video.

| File | Status |
|------|--------|
| 1.png | Working (for video-1) |
| thumb-2png.png | Working but has typo in name (for video-2) |
| thumb-3.png through thumb-5.png | Working |
| thumb-6.png | Exists but video-6 is broken |
| thumb-7.png through thumb-10.png | Working |
| thumb-12.png, thumb-13.png | Working |
| thumb-14.png | MISSING — video-14 has no thumbnail |
| thumb-16.png | Working |
| thumb-18.png through thumb-27.png | Working |
| ` .png` (space in name) | GARBAGE FILE — should be deleted |

### Before/After Photo Pairs (6 pairs = 12 photos)
Stored in `/public/cravemode/`. JPG format.

| Pair | Before | After | Restaurant |
|------|--------|-------|-----------|
| 1 | before-1.jpg | after-1.jpg | Culinary Dropout |
| 2 | before-2.jpg | after-2.jpg | Tokyo Hana |
| 3 | before-3.jpg | after-3.jpg | El Jefe Restaurant |
| 4 | before-4.jpg | after-4.jpg | CAPO PIZZA |
| 5 | before-5.jpg | after-5.jpg | Mega Burgers |
| 6 | before-6.jpg | after-6.jpg | Roost |

### Hero Food Photos (20 total)
Stored in `/public/hero/`. JPG format. Used in the floating collage around the hero headline.

| Files | Count |
|-------|-------|
| food-02.jpg, food-03.jpg, food-04.jpg, food-05.jpg | 4 |
| food-07.jpg, food-08.jpg, food-09.jpg | 3 |
| food-13.jpg, food-14.jpg, food-15.jpg, food-16.jpg, food-17.jpg | 5 |
| food-18.jpg, food-19.jpg, food-20.jpg, food-21.jpg, food-22.jpg | 5 |
| food-23.jpg, food-24.jpg, food-25.jpg | 3 |

**Missing numbers (gaps):** 01, 06, 10, 11, 12

### Summary of Current Inventory

| Asset Type | Count | Location |
|-----------|-------|----------|
| Working videos | **23** | `/public/cravemode/videos/` |
| Video thumbnails | **22** (1 missing, 1 garbage) | `/public/cravemode/videos/thumbnails/` |
| Before/After pairs | **6 pairs** (12 photos) | `/public/cravemode/` |
| Hero food photos | **20** | `/public/hero/` |
| Pricing showcase photos | **0** (currently reuses B/A) | — |
| Artistic text photos | **0** (currently reuses B/A) | — |

---

## Total Content Needed

| Asset Type | Quantity | We Have | Need to Produce |
|-----------|----------|---------|-----------------|
| **Short food videos** (3-10s each) | **60** | 23 | **37 new videos** |
| **Video thumbnails** (first-frame stills) | **60** | 22 | **38 new thumbnails** |
| **Before/After photo pairs** | **15 pairs** (30 photos) | 6 pairs (12 photos) | **9 new pairs** (18 photos) |
| **Hero food photos** (enhanced, standalone) | **30** | 20 | **10 new hero shots** |
| **Pricing showcase photos** (enhanced, standalone) | **10** | 0 (shared) | **10 new photos** |
| **Artistic food photos** (for text reveal section) | **10** | 0 (shared) | **10 new photos** |

### Grand Total to Produce
- **37 new videos** + thumbnails
- **48 new photos** (18 before/after + 10 hero + 10 pricing + 10 artistic)

---

## Video Production List (37 New Videos)

All videos should be **portrait 9:16 aspect ratio, 1080x1920 resolution, 3-10 seconds long**. They should showcase the food in a cinematic, mouth-watering way — slow zooms, steam rising, sauce drizzling, cheese pulling, drinks pouring, plating in action. These are AI-generated food content clips that demonstrate what CraveMode delivers to restaurant clients.

### Videos by Food Category

Each category needs a specific number of videos. The videos will be displayed in a tabbed grid where users browse by cuisine type.

#### 1. Pizza & Italian (5 videos)
Generate 5 short clips showing:
- Cheese pull / pizza slice lift (the classic money shot)
- Wood-fired pizza with bubbling cheese close-up
- Fresh pasta being plated with sauce drizzle
- Margherita pizza overhead rotating shot
- Tiramisu or Italian dessert detail shot

#### 2. Burgers & American (5 videos)
Generate 5 short clips showing:
- Juicy burger with melting cheese close-up
- Fries being dipped in sauce
- Stacked burger assembly / ingredients falling in slow motion
- BBQ sauce drizzle on pulled pork
- Milkshake or American diner dessert

#### 3. Sushi & Japanese (5 videos)
Generate 5 short clips showing:
- Sushi roll being sliced with precision
- Ramen with steam rising, chopstick lift
- Sashimi plating on elegant Japanese dish
- Miso soup or matcha preparation
- Gyoza or tempura close-up with dipping sauce

#### 4. Coffee & Cafe (4 videos)
Generate 4 short clips showing:
- Latte art being poured (overhead or side angle)
- Croissant being torn open showing flaky layers
- Iced coffee with cream swirl
- Avocado toast or cafe brunch plating

#### 5. Desserts & Bakery (4 videos)
Generate 4 short clips showing:
- Chocolate lava cake breaking open with molten center
- Macaron or cupcake decorating detail
- Cake slice with fork cutting through layers
- Fresh pastry with powdered sugar dusting

#### 6. BBQ & Grill (4 videos)
Generate 4 short clips showing:
- Brisket being sliced showing smoke ring
- Ribs with BBQ glaze close-up
- Steak searing on grill with flames
- Grilled corn or sides plating

#### 7. Tacos & Mexican (3 videos)
Generate 3 short clips showing:
- Taco assembly with toppings falling
- Guacamole being made in molcajete
- Burrito being wrapped or cut in half showing filling

#### 8. Rice & Asian (3 videos)
Generate 3 short clips showing:
- Fried rice tossing in wok with flames
- Biryani or rice bowl with garnish being added
- Thai curry being poured over rice

#### 9. Seafood (2 videos)
Generate 2 short clips showing:
- Lobster or crab with butter drizzle
- Fish taco or poke bowl assembly

#### 10. Drinks & Cocktails (2 videos)
Generate 2 short clips showing:
- Cocktail being shaken and poured with garnish
- Smoothie or fresh juice blending

**Total new videos: 37**

Plus we keep the 23 existing videos = **60 total videos** across the website.

---

## Photo Production List (48 New Photos)

### Before/After Pairs (9 new pairs = 18 photos)

Each pair needs TWO versions of the same dish:
- **BEFORE**: Poorly lit, phone-quality, bad angle, washed out colors — the way a restaurant owner would snap a quick photo on their iPhone
- **AFTER**: Professionally enhanced — perfect lighting, rich colors, sharp focus, appetizing composition

Generate these 9 new B/A pairs:

| # | Dish / Category | Before Style | After Style |
|---|----------------|-------------|------------|
| 1 | **Pizza slice** (pepperoni or margherita) | Overhead phone shot, fluorescent lighting, paper plate | Warm golden lighting, wooden board, melted cheese glistening |
| 2 | **Ramen bowl** | Side angle, steam obscuring, cluttered background | Dramatic dark background, steam wisps, perfect noodle lift |
| 3 | **Steak dinner** | Flash photo, shiny/greasy look, messy plate | Moody restaurant lighting, herb butter melting, clean plating |
| 4 | **Smoothie bowl** | Flat overhead, dull colors, plastic container | Vibrant colors popping, artistic toppings arrangement, natural light |
| 5 | **Tacos** (street style) | Blurry, bad white balance, paper wrapper | Sharp detail, lime and cilantro vibrant, rustic presentation |
| 6 | **Croissant & latte** | Counter photo, harsh shadows, cluttered | Soft morning light, steam from coffee, bakery warmth |
| 7 | **Poke bowl** | Overhead phone, yellowish tint, styrofoam container | Fresh and bright, colorful fish, premium bowl |
| 8 | **BBQ ribs** | Dark photo, flash reflection on sauce, plastic tray | Rich smoke-ring visible, glistening glaze, dark wood board |
| 9 | **Chocolate cake** | Dim restaurant, blurry, plate edge visible | Dark moody, molten center visible, dusted cocoa powder |

### Hero Photos (10 new standalone enhanced food shots)

These are pure portfolio pieces — our absolute best work. They float around the hero section as the first thing visitors see. No "before" needed, just stunning food photography.

Generate 10 photos of different dishes, each with different lighting/mood:

| # | Dish | Mood / Style |
|---|------|-------------|
| 1 | Wagyu beef steak | Dark & moody, dramatic side lighting |
| 2 | Rainbow sushi platter | Bright & vibrant, overhead flat lay |
| 3 | Artisan pizza | Warm rustic, wood-fired oven glow |
| 4 | Lobster tail | Luxury fine dining, black background |
| 5 | Acai bowl | Fresh & bright, natural daylight |
| 6 | Tandoori chicken | Warm golden, smoky atmosphere |
| 7 | French macarons (assorted) | Pastel soft light, clean minimal |
| 8 | Pad Thai in wok | Action shot, flames visible, motion |
| 9 | Espresso martini | Dark bar ambiance, condensation drops |
| 10 | Gelato scoops (multiple flavors) | Bright, colorful, summer vibe |

### Pricing Section Photos (10 new enhanced shots)

These rotate behind the pricing cards — they need to look premium and diverse to reinforce "we work with all types of restaurants." Generate 10 different dishes:

1. Gourmet burger with truffle fries
2. Sashimi close-up on ice
3. Wood-fired Neapolitan pizza
4. Eggs Benedict brunch plate
5. Pho soup with herbs
6. Churros with chocolate sauce
7. Mediterranean mezze platter
8. Korean fried chicken
9. Matcha latte art
10. Cheesecake slice with berry compote

### Text Reveal Photos (10 new artistic food shots)

These are visible THROUGH giant text letterforms — they need to be colorful, high-contrast, and visually dense (lots of food filling the frame). Generate 10 photos that are:

- Tightly cropped (full frame, no empty space)
- Very colorful and varied textures
- Different color palettes so they look distinct through text

1. Overhead spread of Indian curry dishes (reds, yellows, greens)
2. Charcuterie board close-up (meats, cheeses, fruits)
3. Colorful poke bowls (salmon pink, tuna red, avocado green)
4. Breakfast spread (pancakes, berries, syrup, eggs)
5. Dim sum bamboo steamers (various dumplings)
6. Ice cream sundae with toppings overflowing
7. Taco bar spread (multiple tacos, salsas, limes)
8. Bakery display (croissants, danishes, muffins variety)
9. Seafood tower (oysters, shrimp, crab, lemon)
10. Mediterranean grilled vegetables (charred, colorful)

---

## Technical Specifications

### Video Requirements

| Spec | Value |
|------|-------|
| **Aspect ratio** | 9:16 (portrait / vertical) |
| **Resolution** | 1080 x 1920 pixels |
| **Duration** | 3-10 seconds per clip |
| **Format** | MP4 (H.264 codec) |
| **File size** | Under 10MB per clip ideally |
| **Style** | Cinematic food content — slow motion zooms, close-ups, steam, sauce drizzle |
| **Audio** | No audio needed (website plays muted) |
| **Background** | Variety — some dark/moody, some bright/airy, some rustic |

### Photo Requirements

| Spec | Before Photos | After Photos / Hero / Showcase |
|------|--------------|-------------------------------|
| **Resolution** | 1200 x 1200px minimum | 1200 x 1200px minimum |
| **Format** | JPG | JPG |
| **Quality** | 80% (intentionally imperfect) | 90-95% (crisp and premium) |
| **Lighting** | Bad — fluorescent, flash, dim | Perfect — golden hour, studio, moody |
| **Composition** | Messy — cluttered bg, bad angle | Clean — styled, focused, appetizing |
| **Color** | Washed out, yellow/blue tint | Rich, warm, saturated but natural |

### Thumbnail Requirements
- Extract from first frame of each video
- 540 x 960px (half of video resolution)
- PNG format
- One thumbnail per video

---

## File Naming & Delivery

Please deliver files using these exact naming conventions:

### Videos
```
video-28.mp4, video-29.mp4, video-30.mp4 ... video-60.mp4
```
(Continue from our existing numbering. We have up to video-27, so new ones start at 28.)

### Video Thumbnails
```
thumb-28.png, thumb-29.png, thumb-30.png ... thumb-60.png
```
(One thumbnail per video, matching number.)

### Before/After Pairs
```
before-7.jpg + after-7.jpg
before-8.jpg + after-8.jpg
...
before-15.jpg + after-15.jpg
```
(We have pairs 1-6. New ones start at 7.)

### Hero Photos
```
food-26.jpg, food-27.jpg ... food-35.jpg
```
(We have food-02 through food-25. New ones start at 26.)

### Pricing Showcase Photos
```
showcase-1.jpg, showcase-2.jpg ... showcase-10.jpg
```
(New naming — these go in `/public/cravemode/showcase/`)

### Text Reveal Photos
```
artistic-1.jpg, artistic-2.jpg ... artistic-10.jpg
```
(New naming — these go in `/public/cravemode/artistic/`)

---

## Category Assignment (How Videos Map to Website)

Once all 60 videos are ready, they'll be assigned to website sections like this:

### Video Showcase Grid (Top 8 — our absolute best)
These are the first videos visitors see. Pick the 8 most visually stunning clips regardless of category.

### Browse by Cuisine (48 videos across 12 categories)
Each tab shows a grid of videos for that food type:

| Category | Videos Needed | Notes |
|----------|:------------:|-------|
| Pizza & Italian | 5 | Include pasta, not just pizza |
| Burgers & American | 5 | Burgers, fries, BBQ, shakes |
| Sushi & Japanese | 5 | Sushi, ramen, tempura, matcha |
| Coffee & Cafe | 4 | Latte art, pastries, brunch |
| Desserts & Bakery | 4 | Cakes, pastries, ice cream |
| BBQ & Grill | 4 | Brisket, ribs, steaks, grilled |
| Tacos & Mexican | 3 | Tacos, burritos, guac |
| Rice & Asian | 3 | Fried rice, curry, biryani |
| Seafood | 3 | Lobster, fish, poke, shrimp |
| Drinks & Cocktails | 3 | Cocktails, smoothies, juices |
| Brunch & Breakfast | 3 | Eggs, pancakes, waffles, avocado toast |
| Fine Dining | 3 | Plated courses, molecular, artistic |
| **Total** | **45** | Plus 8 for showcase + 7 for spotlight overlap buffer |

### Video Spotlight (Compilation Reel)
Auto-plays ALL videos in a rapid 3-second rotation. Uses the full library. No exclusive content needed.

---

## Summary for Quick Reference

**Produce 37 new videos:**
- 5 Pizza/Italian + 5 Burgers/American + 5 Sushi/Japanese + 4 Coffee/Cafe + 4 Desserts + 4 BBQ + 3 Tacos/Mexican + 3 Rice/Asian + 2 Seafood + 2 Drinks

**Produce 48 new photos:**
- 9 before/after pairs (18 photos) — specific dishes listed above
- 10 hero shots — premium portfolio pieces
- 10 pricing showcase shots — diverse cuisine variety
- 10 artistic shots — colorful, full-frame, high-contrast

**All videos:** Portrait 9:16, 1080x1920, 3-10 seconds, MP4, no audio
**All photos:** 1200x1200px minimum, JPG, high quality

**File naming:** Continue existing numbering (videos start at 28, B/A pairs start at 7, hero shots start at 26)
