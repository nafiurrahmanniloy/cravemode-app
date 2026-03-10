---
name: figma
description: Figma design bridge. Browse files, extract components, download assets, and convert food-type designs to code for CraveMode AI.
---
# figma

Figma MCP skill for browsing designs, extracting components, downloading images/icons, and bridging Figma layouts into CraveMode website and mobile app code. Uses the `figma-developer-mcp` server.

## Prerequisites

Figma MCP must be configured in `.mcp.json` with a valid API key:

```json
{
  "mcpServers": {
    "figma": {
      "command": "npx",
      "args": ["-y", "figma-developer-mcp", "--stdio"],
      "env": {
        "FIGMA_API_KEY": "<your-figma-api-key>"
      }
    }
  }
}
```

After changing the key, run **"Developer: Reload Window"** in VS Code.

---

## How to Use This Skill

### Step 1: Get the Figma File Key

Extract the file key from any Figma URL:

```
https://www.figma.com/design/<FILE_KEY>/...
https://www.figma.com/file/<FILE_KEY>/...
```

The file key is the alphanumeric string between `/design/` (or `/file/`) and the next `/`.

### Step 2: Browse the Full File

Fetch the top-level structure to see all pages, frames, and components:

```
mcp__figma__get_figma_data(fileKey: "<FILE_KEY>")
```

This returns:
- Pages and their children (frames, groups, components)
- Layout info (position, size, auto-layout, constraints)
- Text content and styling (font, size, weight, color)
- Fill colors, strokes, effects (shadows, blur)
- Component instances and their overrides

### Step 3: Drill Into a Specific Node

When you find a frame or component you want to inspect deeper, use its node ID:

```
mcp__figma__get_figma_data(fileKey: "<FILE_KEY>", nodeId: "1234:5678")
```

Node IDs are formatted as `1234:5678` or `1234-5678`. For nested instances: `I5666:180910;1:10515`.

Use the optional `depth` parameter to control tree traversal (only if the user requests it).

### Step 4: Download Images and Icons

Export raster (PNG) or vector (SVG) assets from specific nodes:

```
mcp__figma__download_figma_images(
  fileKey: "<FILE_KEY>",
  localPath: "/absolute/path/to/save/",
  nodes: [
    { "nodeId": "1234:5678", "fileName": "hero-image.png" },
    { "nodeId": "2345:6789", "fileName": "logo-icon.svg" }
  ]
)
```

**Parameters:**
- `localPath` — Absolute path to the download directory (created if missing)
- `nodes[].nodeId` — The Figma node ID to export
- `nodes[].fileName` — Local filename with extension (`.png` or `.svg`)
- `nodes[].imageRef` — Required for image fills (raster photos); leave blank for vector SVGs
- `pngScale` — Export scale for PNGs (default: 2x for retina)

**Recommended save locations:**
| Asset Type | Path |
|------------|------|
| Website images | `site/public/images/` |
| Website icons | `site/public/icons/` |
| Brand assets | `site/public/brand/` |
| Mobile app assets | `mobile/assets/` |
| Reference screenshots | `references/figma/` |

---

## CraveMode Design Workflows

### Browse Food Photography Designs

1. Fetch the file to see all pages/frames
2. Look for frames tagged with food categories (burgers, sushi, pizza, desserts, etc.)
3. Extract color palettes, typography, and layout patterns
4. Download hero images, food photos, and icons

### Extract Dashboard Components

For the CraveMode client dashboard:

1. Browse the dashboard page/frame
2. Identify reusable components: cards, stats widgets, navigation, charts
3. Note auto-layout settings, spacing, border-radius, and color tokens
4. Map Figma tokens to existing CSS variables in `site/src/app/globals.css`

**Token mapping reference:**

| Figma Token | CSS Variable | Usage |
|-------------|-------------|-------|
| Background (dark) | `--background` | `hsl(20 10% 4%)` |
| Primary amber/gold | `--primary` | `hsl(35 65% 58%)` |
| Secondary orange | `--secondary` | `hsl(25 60% 52%)` |
| Surface | `--surface` | `hsl(20 8% 8%)` |
| Muted | `--muted` | `hsl(20 6% 12%)` |
| Border | `--border` | `hsl(20 8% 18%)` |
| Truffle brown | `--truffle-brown` | `hsl(30 15% 12%)` |
| Caramel | `--caramel` | `hsl(35 45% 45%)` |
| Cream | `--cream` | `hsl(40 30% 85%)` |

### Extract Mobile App Screens

For the CraveMode mobile app:

1. Browse mobile frames (look for 375x812 or 390x844 artboards)
2. Identify navigation patterns (tab bar, drawer, stack)
3. Extract component styles for React Native / Flutter implementation
4. Download @2x and @3x assets for mobile

### Convert Figma to Code

After extracting design data, translate to the CraveMode stack:

| Figma Property | Next.js / Tailwind Equivalent |
|---------------|------------------------------|
| Auto-layout horizontal | `flex flex-row` |
| Auto-layout vertical | `flex flex-col` |
| Gap: 16 | `gap-4` |
| Padding: 24 | `p-6` |
| Border-radius: 24 | `rounded-3xl` |
| Fill: linear gradient | `bg-gradient-to-r from-X to-Y` |
| Drop shadow | `shadow-xl` or Framer Motion `boxShadow` |
| Font: Inter 600 16px | `font-semibold text-base` (Inter is default) |
| Opacity: 50% | `opacity-50` or `/50` suffix |

---

## Quick Reference

| Task | Command |
|------|---------|
| Browse full file | `get_figma_data(fileKey)` |
| Inspect a frame | `get_figma_data(fileKey, nodeId)` |
| Download PNG | `download_figma_images(fileKey, nodes: [{nodeId, fileName: "x.png"}], localPath)` |
| Download SVG | `download_figma_images(fileKey, nodes: [{nodeId, fileName: "x.svg"}], localPath)` |
| Download at 3x | `download_figma_images(fileKey, nodes, localPath, pngScale: 3)` |

---

## Tips

1. **Always browse first** — Fetch the full file before diving into nodes to understand the structure
2. **Use node IDs from URLs** — When a user shares a Figma link with `?node-id=X:Y`, pass that as `nodeId`
3. **SVG for icons, PNG for photos** — Use `.svg` extension for vector graphics, `.png` for raster images
4. **Retina by default** — `pngScale: 2` is the default; use `3` for mobile @3x assets
5. **Match the brand** — Always map Figma colors to CraveMode CSS variables, don't introduce new colors
6. **Food categories** — When browsing food designs, tag them: appetizers, mains, desserts, drinks, ambiance
