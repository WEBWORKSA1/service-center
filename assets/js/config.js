/* ============================================================
   Service.Center — site configuration
   Edit this ONE file to switch on monetization, forms and links.
   ============================================================ */
window.SC_CONFIG = {
  siteName: "Service.Center",
  // Canonical domain (used for share links / sitemap references)
  siteUrl: "https://service.center",

  /* ---- Contact routing ------------------------------------------------
     The contact address is stored encoded so it never appears as plain
     text anywhere on the site. It is decoded at runtime only when a user
     clicks a contact link or submits a form. Do NOT paste the address
     anywhere else in the codebase.                                       */
  contactKey: "d2Vid29ya3NhMUBnbWFpbC5jb20=",

  /* ---- Forms -----------------------------------------------------------
     Static hosting has no backend, so forms post to a form relay.
     Default: FormSubmit.co AJAX endpoint built from the encoded address.
     After the first submission, FormSubmit emails an activation link; you
     can then replace `formEndpoint` with your private hashed endpoint
     (https://formsubmit.co/ajax/<random-string>) so even the request URL
     carries no address. Alternatives: Formspree, Basin, Getform, Web3Forms
     (set formEndpoint to their URL).                                      */
  formEndpoint: "",            // leave empty to auto-build from contactKey
  formProvider: "formsubmit",  // "formsubmit" | "generic"
  formRedirect: "",            // optional thank-you URL

  /* ---- Google AdSense --------------------------------------------------
     Put your publisher id (ca-pub-XXXXXXXXXXXXXXXX) here. Ad slots render
     only when this is set. Also update /ads.txt with your publisher id.  */
  adsenseClient: "",
  adSlots: {
    header: "",     // responsive display slot id
    inArticle: "",  // in-article slot id
    sidebar: "",    // vertical slot id
    footer: ""
  },

  /* ---- YouTube ---------------------------------------------------------
     channelId: your channel (UC...). uploads playlist auto-derived.
     playlists / videoIds: curated content per category.                  */
  youtube: {
    channelId: "",
    handle: "",
    featured: [],           // ["VIDEO_ID", ...]
    byCategory: {           // category slug -> playlist id or [videoIds]
      phones: [], electronics: [], appliances: [], computers: [], auto: [], home: []
    }
  },

  /* ---- Donations / support ------------------------------------------ */
  support: {
    buyMeACoffee: "",       // e.g. "https://buymeacoffee.com/yourname"
    kofi: "",
    paypal: "",             // e.g. "https://paypal.me/yourname"
    githubSponsors: "",     // e.g. "https://github.com/sponsors/yourname"
    patreon: "",
    stripeLink: ""          // Stripe Payment Link
  },

  /* ---- Affiliate ------------------------------------------------------ */
  affiliate: {
    amazonTag: "",          // e.g. "servicecenter-20"
    ifixitRef: "",
    ebayCampaign: ""
  },

  /* ---- Analytics ------------------------------------------------------ */
  ga4: "",                  // "G-XXXXXXX"
  plausibleDomain: "",      // "service.center"

  /* ---- Social --------------------------------------------------------- */
  social: {
    youtube: "", x: "", instagram: "", facebook: "", linkedin: "", tiktok: ""
  },

  /* ---- Domain / sponsorship banner link (required on every page) ----- */
  ownerContactUrl: "https://web.works/contact"
};
