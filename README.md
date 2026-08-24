# Meditation Timer (PWA)

A simple installable web app for interval-bell meditation sessions. Set a total
duration and a bell interval (e.g. 30 minutes total, ding every 1 minute), tap
Begin, and it rings a generated bell/singing-bowl tone on every interval and a
longer closing bell at the end.

Features:
- Total duration + interval bell, adjustable in the app (with quick presets)
- Bell tones generated with the Web Audio API — no sound files, works offline
- Screen Wake Lock so your iPhone doesn't lock mid-session (iOS 16.4+, Safari/PWA)
- 4-digit PIN lock screen (set on first launch) so a stumbled-on link can't be used
- Installable as a Home Screen app (PWA) with offline support via a service worker

## 1. One-time setup: accounts you'll need

1. **GitHub account** (free) — https://github.com/join. This is where the code
   will live; Vercel deploys straight from a GitHub repo.
2. **Vercel account** (free) — https://vercel.com/signup. Choose **"Continue
   with GitHub"** so the two are linked automatically — this makes deploys
   and future updates one click.

You don't need to know Git — the steps below use GitHub's web upload, no
command line required. Let me know once both accounts exist and I can help
you push the code and wire up the deploy (or walk you through the exact
clicks if you'd rather do it yourself).

## 2. Get the code into a GitHub repo

1. On github.com, click **New repository**. Name it `meditation-timer`,
   keep it **Private** (recommended, since this is for your personal use),
   and click **Create repository**.
2. On the empty repo page, click **uploading an existing file**.
3. Drag in every file from this folder (`index.html`, `manifest.webmanifest`,
   `sw.js`, `vercel.json`, and the whole `icons/` folder), then click
   **Commit changes**.

## 3. Deploy on Vercel

1. Go to https://vercel.com/new.
2. Under "Import Git Repository", select `meditation-timer` (Vercel will
   list your GitHub repos once the accounts are linked) and click **Import**.
3. Framework Preset: leave as **Other** (it's a static site, no build step).
   Leave the Build/Output settings at their defaults and click **Deploy**.
4. After ~30 seconds you'll get a live URL like
   `https://meditation-timer-yourname.vercel.app`. That's your app.

Every time you (or I) push a change to the GitHub repo, Vercel automatically
redeploys — no repeat setup needed.

## 4. Install it on your iPhone 15

1. Open the Vercel URL in **Safari** (must be Safari, not Chrome, for the
   install option to appear).
2. Tap the **Share** icon → **Add to Home Screen** → **Add**.
3. Launch it from the home screen icon like any app. The first time, it'll
   ask you to set a 4-digit PIN — that's the lock screen for the app.

## Notes on iOS limits (so expectations are set correctly)

- **Keep the app open and phone face-up during a session.** iOS suspends
  JavaScript timers in background/locked apps — this is a platform rule that
  applies to *all* web apps and most non-native timer apps, not something in
  this code. The app requests a **Screen Wake Lock** when you tap Begin, which
  keeps the screen on and the app active so bells fire on time. If you
  manually lock the phone or switch apps mid-session, dings can be delayed
  until you return.
- Bells are generated in-app (no audio files), so the very first tone after
  each fresh app load needs that first tap on "Begin Session" to unlock audio
  on iOS — this is already wired up, just noting why the button matters.
- The PIN is stored locally on your phone (hashed, never sent anywhere) — it
  protects against someone else opening the app on your device or guessing
  the URL, not a full authentication system. If you want something stronger
  (e.g., Vercel-level password on the whole site), let me know and I can add
  HTTP Basic Auth via Vercel Edge Middleware instead/in addition.

## Local files in this folder

```
meditation-timer/
├── index.html              # the entire app (UI + timer logic + audio)
├── manifest.webmanifest    # PWA metadata (name, icons, colors)
├── sw.js                   # service worker for offline caching
├── vercel.json             # security headers + no-cache for the service worker
├── gen_icons.py            # script that generated the icons (optional, not deployed)
└── icons/
    ├── icon-192.png
    ├── icon-512.png
    ├── icon-180.png          # apple-touch-icon
    ├── icon-192-maskable.png
    └── icon-512-maskable.png
```
