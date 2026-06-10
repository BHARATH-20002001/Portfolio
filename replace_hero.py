import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Replace Hero CSS
css_old_start = r"    #hero \{"
css_old_end = r"    @keyframes scrollBob \{\n      0%, 100% \{ transform: translateX\(-50%\) translateY\(0\); opacity: 0\.4; \}\n      50%       \{ transform: translateX\(-50%\) translateY\(8px\); opacity: 1; \}\n    \}"

css_new = """    #hero {
      min-height: 100vh;
      background: var(--off-white);
      position: relative;
      overflow: hidden;
      display: flex;
      align-items: center;
      padding: 0 40px;
    }

    .hero-grid {
      display: grid;
      grid-template-columns: 60% 40%;
      width: 100%;
      max-width: 1200px;
      margin: 0 auto;
      align-items: center;
      z-index: 2;
      position: relative;
    }

    .hero-left {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      gap: 20px;
      padding-right: 40px;
      opacity: 0;
    }

    .hero-tagline {
      font-family: var(--mono);
      font-size: 12px;
      font-weight: 500;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: var(--accent);
    }
    .hero-tagline::before { content: '// '; }

    .hero-h1 {
      font-family: var(--font);
      font-size: clamp(48px, 6vw, 90px);
      font-weight: 700;
      color: var(--black);
      line-height: 0.95;
      letter-spacing: -0.04em;
    }

    .hero-sub {
      font-size: clamp(15px, 1.4vw, 18px);
      color: #555;
      line-height: 1.6;
      max-width: 500px;
    }
    .hero-sub strong {
      color: var(--black);
      font-weight: 700;
    }

    .hero-cta {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      padding: 14px 32px;
      background: var(--accent);
      color: #fff;
      font-family: var(--mono);
      font-size: 12px;
      font-weight: 600;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      transition: background 0.3s, transform 0.3s;
      border-radius: 999px;
      margin-top: 10px;
    }
    .hero-cta:hover {
      background: #ff5734;
      transform: translateY(-2px);
    }

    .hero-right {
      display: flex;
      align-items: center;
      justify-content: center;
      height: 70vh;
      width: 100%;
    }

    #media-frame {
      width: 100%;
      height: 100%;
      border-radius: 12px;
      overflow: hidden;
    }

    #media-overlay {
      position: absolute;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      z-index: 10;
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
      transform-origin: center center;
    }

    #media-overlay video {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }"""

content = re.sub(css_old_start + r".*?" + css_old_end, css_new, content, flags=re.DOTALL)

# 2. Replace Hero HTML
html_old_start = r"  <!-- ===== HERO ===== -->\n  <section id=\"hero\">"
html_old_end = r"  </section>\n\n  <!-- ===== INTRO — DARK STATEMENT ===== -->"

html_new = """  <!-- ===== HERO ===== -->
  <section id="hero">
    <div class="hero-grid">
      <!-- Left Column: 60% -->
      <div class="hero-left" id="hero-text-content">
        <span class="hero-tagline">WordPress & Frontend Developer</span>
        <h1 class="hero-h1">Bharath<br>Sarangan</h1>
        <p class="hero-sub">
          <strong>WordPress & Frontend Developer</strong> building high-performance websites.<br>
          Expertise in modern frameworks (React/Next.js/Shopify).<br>
          Pixel-perfect design through custom code and minimal plugin use.
        </p>
        <a href="#contact" class="hero-cta">Let's Talk</a>
      </div>

      <!-- Right Column: 40% -->
      <div class="hero-right">
        <div id="media-frame"></div>
      </div>
    </div>

    <!-- Full-screen absolute overlay containing the video -->
    <div id="media-overlay">
      <video id="hero-video" autoplay loop muted playsinline poster="./assets/seq/Frontview.png">
        <source src="./assets/Use_this_image_and_make_a_vide.mp4" type="video/mp4">
      </video>
    </div>
  </section>

  <!-- ===== INTRO — DARK STATEMENT ===== -->"""

content = re.sub(html_old_start + r".*?" + html_old_end, html_new, content, flags=re.DOTALL)

# 3. Replace Mobile CSS for Hero
# From "      /* ── Hero ── */" to "      /* ── Intro ── */"
mobile_css_old_start = r"      /\* ── Hero ── \*/"
mobile_css_old_end = r"      /\* ── Intro ── \*/"

mobile_css_new = """      /* ── Hero ── */
      .hero-grid { grid-template-columns: 1fr; gap: 30px; }
      .hero-left { padding-right: 0; margin-top: 100px; align-items: center; text-align: center; }
      .hero-right { height: 40vh; width: 100%; }
      .hero-h1 { font-size: clamp(42px, 12vw, 80px); }
      .hero-sub { text-align: center; }
      
      /* ── Intro ── */"""

content = re.sub(mobile_css_old_start + r".*?" + mobile_css_old_end, mobile_css_new, content, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(content)

print("Modifications applied successfully.")
