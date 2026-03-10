# Mobile Testing Setup Guide

Complete guide to test CraveMode AI PWA on your mobile device.

## ✅ What We Fixed

All `localhost:3000` references have been removed from:
- `/api/upload/route.ts` — Callback URL for n8n webhooks
- `/api/billing/checkout/route.ts` — Stripe checkout redirect
- `/api/billing/portal/route.ts` — Billing portal return URL

Created new utility: `src/lib/utils/site-url.ts` for consistent URL handling.

---

## 🚀 Step 1: Start Cloudflare Tunnel

### Option A: Use the Script (Recommended)
```bash
cd site
./start-tunnel.sh
```

### Option B: Manual Command
```bash
cd site
cloudflared tunnel --url http://localhost:3000
```

**Look for output like:**
```
2026-03-11T14:23:45Z INF +--------------------------------------------------------------------------------------------+
2026-03-11T14:23:45Z INF |  Your quick Tunnel has been created! Visit it at (it may take some time to be reachable):  |
2026-03-11T14:23:45Z INF |  https://practice-gratuit-musician-conventional.trycloudflare.com                          |
2026-03-11T14:23:45Z INF +--------------------------------------------------------------------------------------------+
```

**⚠️ IMPORTANT:** Copy this URL! You'll need it for the next steps.

---

## 🔧 Step 2: Update Environment Variables

1. Open `site/.env.local`
2. Update `NEXT_PUBLIC_SITE_URL` with your tunnel URL:

```bash
# Replace with YOUR tunnel URL from Step 1
NEXT_PUBLIC_SITE_URL=https://practice-gratuit-musician-conventional.trycloudflare.com
```

3. Save the file

---

## 🔐 Step 3: Configure Supabase Redirect URLs

1. **Open Supabase Dashboard:**
   Go to: https://supabase.com/dashboard/project/gvtpnuowqapzbjriksmn/auth/url-configuration

2. **Add Redirect URLs:**
   Click "Add URL" and add these (replace with YOUR tunnel URL):

   ```
   https://practice-gratuit-musician-conventional.trycloudflare.com/auth/callback
   https://practice-gratuit-musician-conventional.trycloudflare.com/reset-password
   ```

3. **Add Site URL:**
   Set **Site URL** to:
   ```
   https://practice-gratuit-musician-conventional.trycloudflare.com
   ```

4. **Click "Save"**

---

## 💻 Step 4: Start Development Server

**In a NEW terminal tab/window** (keep tunnel running):

```bash
cd site
npm run dev
```

Wait for:
```
✓ Ready in 1.5s
○ Local:        http://localhost:3000
✓ Ready in 1.5s
```

---

## 📱 Step 5: Test on Your Phone

### Access from Mobile
1. Open **Safari** (iOS) or **Chrome** (Android) on your phone
2. Visit your tunnel URL:
   ```
   https://practice-gratuit-musician-conventional.trycloudflare.com
   ```

### Install PWA
**iOS (Safari):**
1. Tap the **Share** button
2. Scroll down and tap **"Add to Home Screen"**
3. Tap **"Add"**

**Android (Chrome):**
1. Tap the **3-dot menu**
2. Tap **"Add to Home Screen"** or **"Install App"**
3. Tap **"Install"**

### Test Login
1. Open the CraveMode app from your home screen
2. Tap **"Sign In"**
3. Enter your credentials
4. **✅ You should now stay on your tunnel URL** (not redirect to localhost:3000)

---

## 🐛 Troubleshooting

### "Site can't be reached"
- Make sure both tunnel AND dev server are running
- Check that tunnel URL matches `.env.local`

### "Redirect URL not allowed"
- Double-check Supabase redirect URLs include your tunnel URL
- Make sure you clicked "Save" in Supabase dashboard

### "localhost:3000 not found"
- Restart the dev server: `npm run dev`
- Clear browser cache and service worker:
  - iOS: Settings → Safari → Clear History and Website Data
  - Android: Chrome → Settings → Privacy → Clear browsing data

### Tunnel URL changed
Cloudflare tunnels use random URLs. If your URL changes:
1. Update `.env.local` with new URL
2. Update Supabase redirect URLs
3. Restart dev server
4. Uninstall old PWA and reinstall

---

## 🎯 Pro Tips

### Keep the Same Tunnel URL
Use a **persistent tunnel** (requires free Cloudflare account):

```bash
# Login once
cloudflared login

# Create a persistent tunnel
cloudflared tunnel create cravemode

# Configure tunnel
cloudflared tunnel route dns cravemode cravemode.yourdomain.com

# Run with persistent tunnel
cloudflared tunnel run cravemode
```

### Use ngrok Instead
If you prefer ngrok:

```bash
ngrok http 3000
```

Then update `.env.local` with the ngrok URL.

---

## ✅ Verification Checklist

- [ ] Cloudflare tunnel is running
- [ ] Dev server is running (`npm run dev`)
- [ ] `.env.local` has correct tunnel URL
- [ ] Supabase redirect URLs configured
- [ ] Can access site on phone via tunnel URL
- [ ] PWA installs successfully
- [ ] Login works without redirecting to localhost

---

## 🎉 Next Steps

Once mobile testing works:

1. **Deploy to Production:**
   - Vercel: `vercel --prod`
   - Netlify: `netlify deploy --prod`

2. **Update Supabase URLs:**
   - Replace tunnel URLs with production URLs
   - Keep tunnel URLs for development

3. **Set up Custom Domain:**
   - `cravemode.ai` or your domain
   - Update all URLs to use custom domain

---

**Need Help?** Check that:
1. Both tunnel and dev server are running
2. URLs match between `.env.local` and Supabase
3. You're using HTTPS (tunnel URLs are always HTTPS)
