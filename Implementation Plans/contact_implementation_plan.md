# Implementation Plan - The Wonderment Tour Contact Page (Updated)

We will create a stunning, responsive, and interactive contact page (`contact.html`) in the project workspace root. 

This page will be entirely frontend-based, featuring card components for social/email links, a pure frontend contact form, a prominent disclaimer section, and a personal portfolio link.

---

## User Review Required

> [!IMPORTANT]
> We will add a disclaimer box clearly stating that this site is NOT the official page for the Wonderment Tour and is not directly affiliated with AR Rahman. It is a web development template/project, and no actual financial transactions or ticketing costs are involved.

> [!TIP]
> The personal portfolio link (`https://spotlight-elangodilliraj.netlify.app/`) will be displayed as a featured badge/card, highlighting the author's work with an elegant, glowing button.

---

## Proposed Changes

### [Web Application Components]

#### [NEW] [contact.html](file:///c:/Users/ELANGO%20N%20D/OneDrive/Desktop/SUMMER/The%20Wonderment%20tour/contact.html)
A premium HTML page containing:
- **Design System Integration**: Google Fonts (Outfit/Inter) and a glassmorphic background consistent with the other pages.
- **Header**: "Get in Touch" styled with a gradient text effect.
- **Layout Structure**:
  - **Left Column: Direct Contacts & Creator**:
    - **Email Card**: Styled panel with an envelope icon, displaying `n.d.elango2007@gmail.com` and a quick `mailto:` CTA button.
    - **Instagram Card**: Styled panel with an Instagram logo, displaying `@elango._7` and redirecting to `https://www.instagram.com/elango._7/`.
    - **Portfolio Card**: Styled panel with a link icon, redirecting to the user's personal website: `https://spotlight-elangodilliraj.netlify.netlify.app` (or exactly `https://spotlight-elangodilliraj.netlify.app/`).
  - **Right Column: Contact Form**:
    - A form with inputs for **Your Name**, **Your Email**, **Subject**, and a textarea for **Message**.
    - Styled with semi-transparent input borders that glow on focus.
    - An action button "Send Message" that invokes a JavaScript handler to launch the pre-formatted `mailto:` client redirect.
- **Footer/Disclaimer Section**:
  - A prominent card at the bottom of the page containing the disclaimer text:
    > "Disclaimer: This website is an unofficial page. It does not have any direct affiliation or association with the Wonderment Tour or AR Rahman. This website is a template and simple project created for web development practice. No ticket purchases, costs, or actual financial transactions will be processed or affected through this site."

---

## Verification Plan

### Automated Tests
- Verify JavaScript code that escapes input text and constructs the `mailto:` URL.

### Manual Verification
- Open `contact.html` in a web browser.
- Verify the disclaimer text is displayed clearly at the bottom.
- Click the personal portfolio link to confirm it successfully opens `https://spotlight-elangodilliraj.netlify.app/` in a new tab.
- Click the Instagram link to confirm it successfully opens `https://www.instagram.com/elango._7/` in a new tab.
