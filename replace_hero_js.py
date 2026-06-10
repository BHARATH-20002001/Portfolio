import re

with open('index.html', 'r') as f:
    content = f.read()

old_start = r"    // Hero video parallax \(fallback layer — WebGL canvas handles display when active\)"
old_end = r"      if \(document\.readyState === 'complete'\) \{\n        initFluid\(\);\n      \} else \{\n        window\.addEventListener\('load', initFluid\);\n      \}\n    \}\)\(\);"

new_js = """    // Trigger splash check for hero right away, since we no longer wait for Three JS
    window._readyFlags.hero = true;
    if(window._checkAllReady) window._checkAllReady();

    // GSAP Entrance Animation
    window.addEventListener('load', () => {
      const overlay = document.getElementById('media-overlay');
      const frame = document.getElementById('media-frame');
      const heroContent = document.getElementById('hero-text-content');
      const leftTextElements = document.querySelectorAll('#hero-text-content > *');
      const hero = document.getElementById('hero');

      // Ensure container is visible, children hidden
      gsap.set(heroContent, { opacity: 1 });
      gsap.set(leftTextElements, { opacity: 0, y: 30 });

      // Initial scale of 2
      gsap.set(overlay, { scale: 2 });

      const tl = gsap.timeline({
        delay: 0.2, // slight delay after load
        onComplete: () => {
          // Reparent the overlay to media-frame to finalize structure
          gsap.set(overlay, { clearProps: "all" });
          overlay.style.position = "relative";
          overlay.style.width = "100%";
          overlay.style.height = "100%";
          overlay.style.zIndex = "1";
          frame.appendChild(overlay);
        }
      });

      // Calculate relative bounds
      const frameRect = frame.getBoundingClientRect();
      const heroRect = hero.getBoundingClientRect();

      const targetTop = frameRect.top - heroRect.top;
      const targetLeft = frameRect.left - heroRect.left;

      tl.to(overlay, {
        scale: 1,
        top: targetTop,
        left: targetLeft,
        width: frameRect.width,
        height: frameRect.height,
        borderRadius: "12px", // match frame border radius
        duration: 1.8,
        ease: "expo.inOut"
      })
      .to(leftTextElements, {
        opacity: 1,
        y: 0,
        stagger: 0.15,
        duration: 1,
        ease: "power3.out"
      }, "-=0.8");
    });"""

new_content = re.sub(old_start + r".*?" + old_end, new_js, content, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(new_content)

print("JS Modifications applied successfully.")
