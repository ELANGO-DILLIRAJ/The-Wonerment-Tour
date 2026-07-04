# Implementation Plan - The Wonderment Tour Venue Page (Updated)

We will create a stunning, responsive, and interactive venue details page (`venue.html`) in the project workspace root. 

The venue page will display individual detailed boxes (cards) for all 5 tour venues, incorporating stadium photographs (aerial views), seating block diagrams, and direct Google Maps location links.

## Image Analysis - Venue Folder

We analyzed the files in the [Venue](file:///c:/Users/ELANGO%20N%20D/OneDrive/Desktop/SUMMER/The%20Wonderment%20tour/Venue) folder. There are 2 images for each of the 5 stadiums:

1. **Chennai (Jawaharlal Nehru Stadium)**:
   - Aerial View: `Jawaharlal Nehru stadium aerial view.jpg` (JPEG, `597x335`)
   - Seating Block: `Jawaharlal Nehru stadium block diagram.jpg` (JPEG, `409x488`)
2. **Mumbai (D.Y. Patil Stadium)**:
   - Aerial View: `dy-patil-stadium-navi-mumbai aerial view.jpg` (JPEG, `800x400`)
   - Seating Block: `dy-patil-stadium-navi-mumbai block diagram.jpg` (JPEG, `1080x832`)
3. **Dubai (Coca-Cola Arena)**:
   - Aerial View: `Coco-Cola Arena aerial view.jpg` (JPEG, `2560x1483`)
   - Seating Block: `Coco-Cola Arena block diagram.jpg` (JPEG, `739x415`)
4. **London (The O2 Arena)**:
   - Aerial View: `The O2 arena aerial view.png` (PNG, `746x602`)
   - Seating Block: `The O2 arena block diagram.jpg` (JPEG, `400x460`)
5. **New York (Madison Square Garden)**:
   - Aerial View: `Madison Sqaure garden aerial view.png` (PNG, `1200x900` - Note spelling `Sqaure` in file name)
   - Seating Block: `Madison Sqaure garden block diagram.webp` (WEBP, `974x776` - Note spelling `Sqaure` in file name)

---

## User Review Required

> [!IMPORTANT]
> The Madison Square Garden files contain the typo `Sqaure` in their filenames (`Madison Sqaure garden...`). We must reference them exactly as `Venue/Madison Sqaure garden aerial view.png` and `Venue/Madison Sqaure garden block diagram.webp` in the HTML so they load correctly.

> [!TIP]
> We will implement a native, lightweight JavaScript-based Lightbox Modal. When a user clicks on any aerial view or seating block diagram, it will smoothly fade in as a high-resolution, full-screen overlay, allowing them to inspect details (especially seating charts) clearly.

---

## Proposed Changes

### [Web Application Components]

#### [NEW] [venue.html](file:///c:/Users/ELANGO%20N%20D/OneDrive/Desktop/SUMMER/The%20Wonderment%20tour/venue.html)
A premium HTML page containing:
- **Design System Integration**: A deep space dark mode background with clean glassmorphic panels, matching `events.html`.
- **5 Event Box Structures (Cards)**: Arranged in a beautiful grid/list containing:
  - **Header**: Venue Name (e.g. "Jawaharlal Nehru Stadium") and Location (e.g. "Chennai").
  - **Dates**: Show date and time.
  - **Availability Time Details**: Timing slots (e.g. Gates open, Show starts, Show ends).
  - **Contact Details**: Specific phone numbers and support emails for venue inquiries.
  - **Media Grid**: Side-by-side display of the **Aerial View** and the **Seating Block Diagram**.
  - **Interactive Lightbox**: Click handler on images to open them in a full-sized overlay.
  - **Google Maps Navigation**: A link button redirecting to the venue's Google Maps location:
    - **Chennai**: `https://www.google.com/maps/place/Jawaharlal+Nehru+Stadium/@13.0855653,80.2691533,17z/data=!3m1!4b1!4m6!3m5!1s0x3a5265fbe6a909ab:0x5a6046dfc9f0d784!8m2!3d13.0855653!4d80.2717282!16zL20vMDc4YzV5?entry=ttu&g_ep=EgoyMDI2MDYyMy4wIKXMDSoASAFQAw%3D%3D`
    - **Mumbai**: `https://www.google.com/maps/place/Dr+D.Y.Patil+Stadium/@19.0423934,73.0239322,17z/data=!3m1!4b1!4m6!3m5!1s0x3be7c3c53b1e255b:0x3fa8b73a42118233!8m2!3d19.0423934!4d73.0265071!16s%2Fm%2F0263rsl?entry=ttu&g_ep=EgoyMDI2MDYyMy4wIKXMDSoASAFQAw%3D%3D`
    - **Dubai**: `https://www.google.com/maps/place/Coca-Cola+Arena/@25.2037509,55.2635888,17z/data=!4m10!1m2!2m1!1scoca+cola+arena!3m6!1s0x3e5f43db141ff4fd:0xd3ce726c8458af4c!8m2!3d25.2043102!4d55.2653822!15sCg9jb2NhIGNvbGEgYXJlbmFaESIPY29jYSBjb2xhIGFyZW5hkgEFYXJlbmHgAQA!16s%2Fg%2F11fl7q5rsc?entry=ttu&g_ep=EgoyMDI2MDYyMy4wIKXMDSoASAFQAw%3D%3D`
    - **London**: `https://www.google.com/maps/place/The+O2/@51.5029456,0.0006511,17z/data=!3m1!5s0x47d8a81ce55fb6cf:0xd17024fbebc06a05!4m10!1m2!2m1!1sthe+o2+arena!3m6!1s0x47d8a81c5507b387:0x981ded0cf3b9dadf!8m2!3d51.503038!4d0.0031543!15sCgx0aGUgbzIgYXJlbmFaDiIMdGhlIG8yIGFyZW5hkgEQbGl2ZV9tdXNpY192ZW51ZeABAA!16s%2Fm%2F047t9qn?entry=ttu&g_ep=EgoyMDI2MDYyMy4wIKXMDSoASAFQAw%3D%3D`
    - **New York**: `https://www.google.com/maps/place/Madison+Square+Garden/@40.7505045,-73.9960136,17z/data=!3m1!4b1!4m6!3m5!1s0x89c25a21fb011c85:0x33df10e49762f8e4!8m2!3d40.7505045!4d-73.9934387!16zL20vMGpfNjY?entry=ttu&g_ep=EgoyMDI2MDYyMy4wIKXMDSoASAFQAw%3D%3D`
  - **CTA Button**: A stylized link redirecting to the local tickets page (`tickets.html?event=city_name`).

---

## Verification Plan

### Automated Tests
- Verify HTML links to ensure the Google Maps redirect URLs are correct and open in new tabs (`target="_blank" rel="noopener noreferrer"`).

### Manual Verification
- Load `venue.html` in a web browser.
- Verify that clicking the Google Maps link button redirects to the correct Google Maps coordinates.
