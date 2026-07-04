# Implementation Plan - The Wonderment Tour of ARR

We will build a high-fidelity, visually stunning multi-page website for **"The Wonderment Tour of ARR" (AR Rahman Live Concert)**. The design will follow a premium, minimalist dark aesthetic utilizing vibrant neon elements (pink, orange, violet, red), custom-crafted SVG outline traces of musical instruments, smooth page transition animations, a custom loading screen, and a Web Audio API ambient BGM backdrop.

---

## Visual Design & Theme Guidelines

### Core Color Palette
We will implement CSS variables for a cohesive theme:
*   **Deep Dark Background**: `#050206` (A rich black with a subtle violet hue)
*   **Card/Section Background**: `rgba(15, 8, 20, 0.6)` with a glassmorphism blur (`backdrop-filter: blur(12px)`)
*   **Neon Pink**: `#ff007f` (representing high energy, vocals)
*   **Neon Orange**: `#ff7300` (representing percussion, rhythm)
*   **Neon Violet**: `#8b00ff` (representing classical fusion, strings)
*   **Neon Red**: `#ff073a` (representing intensity, brass)
*   **Neon Text Shadow**: `0 0 5px [color], 0 0 15px [color], 0 0 30px [color]`
*   **Neon Box Shadow**: `0 0 8px [color], inset 0 0 8px [color]`

### Typography
We will import Google Fonts:
*   **Handwritten Title**: `Caveat` or `Alex Brush` (for the handwritten style of "The Wonderment Tour of ARR")
*   **Interface/Content Font**: `Outfit` (a geometric, premium modern sans-serif that aligns with a high-end show layout)

### Musical Instrument Outlines
We will design clean, minimalist SVG outlines of instruments which will glow and trace:
1.  **Grand Piano / Keyboard** (representing ARR's signature instrument)
2.  **Violin / Bow** (representing orchestrations)
3.  **Acoustic/Electric Guitar** (representing rock/fusion items)
4.  **Drums/Tablas** (representing rhythms)
These will be positioned subtly in page headers, sections, and background elements, animating dynamically with CSS stroke-dashoffset transitions (simulating glowing electric pulses).

---

## Proposed File Structure

We will create the following files in the workspace directory:
*   `index.html` — Home Page
*   `events.html` — Events (Timeline)
*   `venue.html` — Venue Details & Availability Widget
*   `eligibility.html` — Ticket Eligibility, Rules & Disclaimer
*   `tickets.html` — Ticket Tier Pricing & Dynamic Calculator
*   `booking-success.html` — Mock Ticket Invoice & Glowing QR Code E-Ticket
*   `contact.html` — Contact form & Socials
*   `css/style.css` — Shared stylesheet (animations, layouts, neon variables, header/footer, custom loading screens)
*   `js/main.js` — Custom transitions, page loader logic, navigation routing helper, global styling checks
*   `js/audio.js` — Audio background controller, Web Audio API ambient pad synthesizer, visualizer helper
*   `js/booking.js` — Logic for tickets selection, mathematical calculation, verification check, success redirect

---

## Proposed Changes

### Component 1: Core Design System & Global Styles

#### [NEW] [style.css](file:///c:/Users/ELANGO%20N%20D/OneDrive/Desktop/SUMMER/The%20Wonderment%20tour/css/style.css)
*   Define global variables for colors, glows, blur, and timing.
*   Configure custom scrollbar: dark track with glowing neon slider.
*   Setup loading overlay styles: full screen, deep black, centering a pulsing neon instrument SVG and glowing progress bar.
*   Define keyframe animations:
    *   `neonGlow`: pulsing box and text shadows.
    *   `flicker`: rapid opacity shifts on text to mimic neon tubes.
    *   `pulseOutline`: SVG stroke-dashoffset tracing animation.
*   Setup typography hierarchy and navbar styles (glassmorphism overlay header, logo with glowing notes, active state indicator).
*   Create a responsive grid system and reusable cards with hover-expand glowing effects.

#### [NEW] [main.js](file:///c:/Users/ELANGO%20N%20D/OneDrive/Desktop/SUMMER/The%20Wonderment%20tour/js/main.js)
*   Intercept all standard anchor clicks (`a[href]`) to prevent abrupt page refreshes.
*   When a link is clicked, trigger the custom transition fade-out/slide overlay.
*   Wait for the fade-out to finish (~400ms), update `window.location.href`.
*   On page load (`window.onload`), fade out the loading screen and slide content in, creating a cohesive SPA feel.

#### [NEW] [audio.js](file:///c:/Users/ELANGO%20N%20D/OneDrive/Desktop/SUMMER/The%20Wonderment%20tour/js/audio.js)
*   Since standard BGM files may fail to load or get blocked, we will implement a dual-mode audio system:
    1.  **Synthesizer Mode (Web Audio API)**: Automatically builds an oscillator, low-pass filter, and gain node to programmatically generate a beautiful, ambient, slow-pulsing ARR-themed minor/major chord pad loop in D major/B minor. This requires no network traffic and sounds exceptionally immersive.
    2.  **MP3 Fallback Mode**: Supports loading a URL for background audio.
*   Build a glowing visualizer (using HTML5 canvas or simple CSS bands) that pulses in sync with the audio state when activated.
*   Audio button (floating or header integrated) with indicator showing whether BGM is playing (pulsing green/pink equalizer bars).

---

### Component 2: Page Implementation

#### [NEW] [index.html](file:///c:/Users/ELANGO%20N%20D/OneDrive/Desktop/SUMMER/The%20Wonderment%20tour/index.html) (Home)
*   **Header & Hero Section**:
    *   **Asset placement**: Display `home/title.webp` at the very top center.
    *   **Concert Title**: Under the image, reveal the title **"The Wonderment Tour: of ARR: 2026"** using a handwritten font (`Caveat`/`Alex Brush`) styled with a CSS typewriter typing reveal animation.
    *   **Highlights**: Integrate a golden logo highlight saying *"Grab your tickets"* and a link for *"Safety Eligibility"* near the header text.
*   **Scrolling Video Backdrop**:
    *   Below the initial hero fold, embed the local video `home/Video 1.mp4` using standard HTML5 tags (`autoplay`, `loop`, `muted`, `playsinline`). It will occupy the full width and height of its section, blending into the page as the user scrolls.
*   **Tour Explanation Section**:
    *   This section features the pre-generated background collage `home/collage.jpg` centered with a medium opacity layer (`0.3 - 0.4`) and dark overlays to preserve readability of the text displayed on top.
    *   **Split Layout**:
        *   **Left Column**: Display the background-removed photo `home/image_1_cropped.png` containing only the maestro. Apply entrance scroll animations (fade-in & slide-right) and a custom CSS hover scale/neon shadow effect.
        *   **Right Column**: Display the primary text: *"A Symphony of the Soul. For over three decades, the music of A.R. Rahman has crossed boundaries, shaped cinematic history, and served as the soundtrack to countless lives..."*
    *   **Centered Sub-Layout**:
        *   Below the columns, display the remaining narrative in the center:
            1.  *"From the Mozaic of Madras to the Global Stage..."*
            2.  *"Infinite Echoes Across Continents..."*
            3.  *"Rhythms of Reality: A Sonic Experience..."*
        *   Conclude the explanation with: *"Secure Your Journey. Spaces in each global city are strictly limited to preserve the premium nature of the arena layouts. Select your destination below to experience the Symphony of the Soul live."*
*   **Concert Timeline Grid**:
    *   A stylized timeline showcasing the 5 global tour dates next to or stacked adjacent to each other:
        1.  **Mozaic of Madras** — October 10, 2026 — Chennai
        2.  **Infinite Echoes** — October 24, 2026 — Mumbai
        3.  **Reality of Rhythm** — November 4, 2026 — Dubai
        4.  **Symphony of the Soul** — November 21, 2026 — London
        5.  **A Global Sonic Experience** — December 12, 2026 — New York
*   **Action Navigation & CTAs**:
    *   Positioned below the timeline block:
        *   **Primary CTA**: A large button with a shining gold gradient background/glow text showing **"Grab your tickets"** (linking to `tickets.html`).
        *   **Secondary CTA**: A button showing **"Check Eligibility"** (linking to `eligibility.html`).
        *   **Contact Info**: Two clean links for **"Contact Queries"** directing the user to `contact.html`.
*   **Footer**:
    *   Display the text **"The Roaming Rhythm"** as a brand tagline.
    *   Include organizational details: **"Organized by DEXTER AGENCIES. All Rights Reserved."** with customized neon indicators.

#### [NEW] [events.html](file:///c:/Users/ELANGO%20N%20D/OneDrive/Desktop/SUMMER/The%20Wonderment%20tour/events.html) (Events Timeline)
*   Configure the timeline page layout.
*   **Timeline Element**:
    *   A central glowing neon vertical track (alternating neon colors) that splits events.
    *   **Timeline Cards** positioned adjacent (left and right columns on desktop, stacking on mobile):
        1.  *Chennai (Home ground)*: Nehru Stadium - Oct 10, 2026.
        2.  *Mumbai*: DY Patil Stadium - Oct 24, 2026.
        3.  *Delhi*: Jawaharlal Nehru Stadium - Nov 07, 2026.
        4.  *London*: Wembley Arena - Nov 28, 2026.
    *   Each card features a high-fidelity image placeholder (glowing border), venue/date details, and a dedicated "Book your tickets" link mapping directly to that city in `tickets.html`.

#### [NEW] [venue.html](file:///c:/Users/ELANGO%20N%20D/OneDrive/Desktop/SUMMER/The%20Wonderment%20tour/venue.html) (Venue)
*   Provide detailed layouts of the stadia.
*   Include guidelines for entry, seat layout (VIP lounge vs Platinum vs Gold vs Silver).
*   **Availability Checker Widget**:
    *   Interactive drop-down where users select their preferred city.
    *   Clicking "Check Live Seats" runs a custom animated check (neon spinner, "Accessing seating grid...") and returns mock remaining seats and statuses (e.g., "Silver: SOLD OUT", "VIP: 14 seats left - Selling Fast!").
*   Detail gate entry timings, opening acts, and contact helpline details per stadium.

#### [NEW] [eligibility.html](file:///c:/Users/ELANGO%20N%20D/OneDrive/Desktop/SUMMER/The%20Wonderment%20tour/eligibility.html) (Eligibility & Guidelines)
*   Crucial safety information page.
*   Highlights:
    *   **Age Limit**: Strictly 18+ (verified at entry gates via ID proof).
    *   **Medical Warning**: High intensity strobe, lasers, sub-bass frequencies, smoke/fog effects.
    *   **Prohibited Items**: Flash cameras, lasers, spray paint, aerosols, liquids, external foods, weapons.
*   **Gate Acknowledge Component**: An interactive checklist with a "Proceed to Tickets" button. Once checked, it sets a variable in local storage so the ticket page knows they read the guidelines, bypassing the entry disclaimer.

#### [NEW] [tickets.html](file:///c:/Users/ELANGO%20N%20D/OneDrive/Desktop/SUMMER/The%20Wonderment%20tour/tickets.html) (Tickets)
*   **Disclaimer Banner**: Glowing neon orange border: "Web Development Project Disclaimer: This website is created solely for web development demonstration purposes and does not represent a real or actual event. No tickets are being sold, and no real transactions will occur."
*   **Event Card Selection Grid**: Carousel/flex row showing the upcoming concert dates.
*   **Interactive Booking Panel**:
    *   Dropdown for city selection.
    *   Drop-down for ticket class (VIP Lounge, Platinum, Gold, Silver) with prices.
    *   Quantity selection (1 to 5).
    *   Live price calculation dynamically rendering total with glowing text effect.
    *   **Purchase Button**: Redirects to `booking-success.html`.

#### [NEW] [booking-success.html](file:///c:/Users/ELANGO%20N%20D/OneDrive/Desktop/SUMMER/The%20Wonderment%20tour/booking-success.html) (Confirmation)
*   A page that mimics an e-ticket generator.
*   Displays a beautiful neon vector ticket showing:
    *   Concert: The Wonderment Tour
    *   Category: VIP / Platinum (based on URL queries)
    *   A simulated glowing neon QR Code.
    *   Print / Download instructions.

#### [NEW] [contact.html](file:///c:/Users/ELANGO%20N%20D/OneDrive/Desktop/SUMMER/The%20Wonderment%20tour/contact.html) (Contact)
*   Features query form styled with glowing input borders.
*   **Form Logic**: Submitting intercepts the form event, fetches values (Name, Message, Subject), constructs a `mailto:dexteragencies@example.com?subject=...&body=...` and opens it in the user's native mail client.
*   **Instagram Button**: Vibrant neon pink/orange gradient hover button leading to Instagram.
*   **Footer**: "Organized by DEXTER AGENCIES. All Rights Reserved."

---

## Verification Plan

### Manual Verification
1.  **Loading & Page Transition Test**: Click navigation links. Ensure the screen fades to black, displays the pulsing custom instrument spinner, and smoothly loads the target page with a slide-up entrance animation.
2.  **Audio Background Check**: Click the "Activate BGM" button. Listen to check if a synthesized electronic/ambient pad is successfully generated and if the neon audio-indicator animations start moving.
3.  **Responsive Layout Check**: Resize the browser to mobile viewport (375px), tablet viewport (768px), and monitor screen size. Check that cards stack properly and the timeline aligns in a single column on smaller viewports.
4.  **Tickets Calculator Check**: Select Mumbai, Platinum ticket, set quantity to 3. Verify total is calculated accurately (8000 * 3 = 24,000 INR) and clicking "Proceed to Book" redirects to the success ticket preview with matching parameters.
5.  **Contact Mailto Check**: Fill in the form and click Send. Confirm it launches the mail client with fields pre-filled.
