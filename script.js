/* ===== CYBER TELECOM & CONSTELLATION NETWORK MATRIX ===== */
(function initCyberTelecomMatrix() {
  const canvas = document.getElementById('starfield');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  let width = 0, height = 0;
  let stars = [];
  let nodes = [];
  let pulses = [];
  const mouse = { x: -1000, y: -1000, active: false };

  function resize() {
    width = canvas.width = window.innerWidth;
    height = canvas.height = window.innerHeight;
  }

  function initNodes() {
    stars = [];
    nodes = [];
    pulses = [];

    // 1. Background Twinkling Stars
    const starCount = Math.floor((width * height) / 10000);
    for (let i = 0; i < starCount; i++) {
      stars.push({
        x: Math.random() * width,
        y: Math.random() * height,
        size: Math.random() * 1.5 + 0.3,
        opacity: Math.random() * 0.7 + 0.3,
        twinkleSpeed: Math.random() * 0.02 + 0.005,
        twinklePhase: Math.random() * Math.PI * 2,
        color: Math.random() > 0.8 ? '#38bdf8' : (Math.random() > 0.9 ? '#f59e0b' : '#ffffff')
      });
    }

    // 2. Telecom & Circuit Nodes
    const nodeCount = Math.min(55, Math.floor(width / 26));
    for (let i = 0; i < nodeCount; i++) {
      nodes.push({
        x: Math.random() * width,
        y: Math.random() * height,
        vx: (Math.random() - 0.5) * 0.45,
        vy: (Math.random() - 0.5) * 0.45,
        radius: Math.random() * 2 + 1.2,
        pulsePhase: Math.random() * Math.PI * 2
      });
    }
  }

  // Generate periodic data pulses along connected links
  setInterval(() => {
    if (nodes.length < 2 || document.hidden) return;
    const fromIdx = Math.floor(Math.random() * nodes.length);
    const n1 = nodes[fromIdx];
    // Find closest connected node
    let closest = null, minD = 130;
    for (let j = 0; j < nodes.length; j++) {
      if (fromIdx === j) continue;
      const n2 = nodes[j];
      const d = Math.hypot(n1.x - n2.x, n1.y - n2.y);
      if (d < minD) {
        minD = d;
        closest = n2;
      }
    }
    if (closest && pulses.length < 15) {
      pulses.push({
        x1: n1.x, y1: n1.y,
        x2: closest.x, y2: closest.y,
        progress: 0,
        speed: 0.02 + Math.random() * 0.015,
        color: Math.random() > 0.4 ? '#38bdf8' : '#f59e0b'
      });
    }
  }, 400);

  function draw() {
    ctx.clearRect(0, 0, width, height);

    // 1. Draw Background Stars
    for (let i = 0; i < stars.length; i++) {
      const s = stars[i];
      s.twinklePhase += s.twinkleSpeed;
      const alpha = s.opacity * (Math.sin(s.twinklePhase) * 0.35 + 0.65);
      ctx.beginPath();
      ctx.arc(s.x, s.y, s.size, 0, Math.PI * 2);
      ctx.fillStyle = s.color === '#ffffff' ? `rgba(255, 255, 255, ${alpha})` : (s.color === '#38bdf8' ? `rgba(56, 189, 248, ${alpha})` : `rgba(245, 158, 11, ${alpha})`);
      ctx.fill();
    }

    // 2. Draw Connections between Nodes
    const maxDist = 125;
    for (let i = 0; i < nodes.length; i++) {
      const n1 = nodes[i];
      n1.x += n1.vx;
      n1.y += n1.vy;

      if (n1.x < -10) n1.x = width + 10;
      else if (n1.x > width + 10) n1.x = -10;
      if (n1.y < -10) n1.y = height + 10;
      else if (n1.y > height + 10) n1.y = -10;

      // Mouse interactive link
      if (mouse.active) {
        const md = Math.hypot(n1.x - mouse.x, n1.y - mouse.y);
        if (md < 140) {
          const mAlpha = (1 - md / 140) * 0.35;
          ctx.beginPath();
          ctx.moveTo(n1.x, n1.y);
          ctx.lineTo(mouse.x, mouse.y);
          ctx.strokeStyle = `rgba(56, 189, 248, ${mAlpha})`;
          ctx.lineWidth = 1;
          ctx.stroke();
        }
      }

      // Link with other nodes
      for (let j = i + 1; j < nodes.length; j++) {
        const n2 = nodes[j];
        const d = Math.hypot(n1.x - n2.x, n1.y - n2.y);
        if (d < maxDist) {
          const alpha = (1 - d / maxDist) * 0.16;
          ctx.beginPath();
          ctx.moveTo(n1.x, n1.y);
          ctx.lineTo(n2.x, n2.y);
          ctx.strokeStyle = `rgba(96, 165, 250, ${alpha})`;
          ctx.lineWidth = 0.8;
          ctx.stroke();
        }
      }

      // Node dot
      n1.pulsePhase += 0.04;
      const pulseSize = n1.radius + Math.sin(n1.pulsePhase) * 0.5;
      ctx.beginPath();
      ctx.arc(n1.x, n1.y, pulseSize, 0, Math.PI * 2);
      ctx.fillStyle = 'rgba(147, 197, 253, 0.7)';
      ctx.fill();
    }

    // 3. Draw Traveling Data Pulses (Fiber/Network Signals)
    for (let k = pulses.length - 1; k >= 0; k--) {
      const p = pulses[k];
      p.progress += p.speed;
      if (p.progress >= 1) {
        pulses.splice(k, 1);
        continue;
      }
      const curX = p.x1 + (p.x2 - p.x1) * p.progress;
      const curY = p.y1 + (p.y2 - p.y1) * p.progress;

      ctx.beginPath();
      ctx.arc(curX, curY, 2.4, 0, Math.PI * 2);
      ctx.fillStyle = p.color;
      ctx.shadowColor = p.color;
      ctx.shadowBlur = 8;
      ctx.fill();
      ctx.shadowBlur = 0; // reset
    }

    requestAnimationFrame(draw);
  }

  resize();
  initNodes();
  draw();

  window.addEventListener('resize', () => {
    resize();
    initNodes();
  });

  window.addEventListener('mousemove', (e) => {
    mouse.x = e.clientX;
    mouse.y = e.clientY;
    mouse.active = true;
  });
  window.addEventListener('mouseleave', () => {
    mouse.active = false;
  });
})();


/* ===== TYPING EFFECT ===== */
(function initTyping() {
  const el = document.getElementById('typingText');
  if (!el) return;

  const phrases = [
    'Electronics Engineering Student',
    'IoT & Embedded Systems Enthusiast',
    'Telecommunication Engineer',
    'Tahfidz Scholarship Awardee',
    'Fiber Optic & Network Specialist'
  ];

  let phraseIdx = 0;
  let charIdx = 0;
  let isDeleting = false;
  let typeDelay = 80;

  function type() {
    const current = phrases[phraseIdx];

    if (!isDeleting) {
      el.textContent = current.substring(0, charIdx + 1);
      charIdx++;
      if (charIdx === current.length) {
        isDeleting = true;
        typeDelay = 2000; // Pause before deleting
      } else {
        typeDelay = 70 + Math.random() * 40;
      }
    } else {
      el.textContent = current.substring(0, charIdx - 1);
      charIdx--;
      if (charIdx === 0) {
        isDeleting = false;
        phraseIdx = (phraseIdx + 1) % phrases.length;
        typeDelay = 400;
      } else {
        typeDelay = 35;
      }
    }

    setTimeout(type, typeDelay);
  }

  setTimeout(type, 800);
})();

/* ===== NAVBAR & HUD ORBIT: Scroll + Active Link ===== */
const navbar = document.getElementById('navbar');
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.nav-link');
const scrollProgress = document.getElementById('scrollProgress');
const hudRailFill = document.getElementById('hudRailFill');
const hudNodes = document.querySelectorAll('.hud-node');

function updateNav() {
  const scrollY = window.scrollY;

  let current = 'home';
  sections.forEach(sec => {
    if (scrollY >= sec.offsetTop - 220) current = sec.getAttribute('id');
  });

  navLinks.forEach(link => {
    const section = link.getAttribute('data-section');
    link.classList.toggle('active', section === current);
  });

  hudNodes.forEach(node => {
    const target = node.getAttribute('data-target');
    node.classList.toggle('active', target === `#${current}`);
  });

  const docHeight = document.documentElement.scrollHeight - window.innerHeight;
  const pct = docHeight > 0 ? (scrollY / docHeight) * 100 : 0;
  if (hudRailFill) hudRailFill.style.height = `${Math.min(100, Math.max(0, pct))}%`;
}

let ticking = false;
window.addEventListener('scroll', () => {
  if (!ticking) {
    requestAnimationFrame(() => { updateNav(); updateBackToTop(); updateScrollProgress(); ticking = false; });
    ticking = true;
  }
}, { passive: true });

updateNav();

/* ===== MOBILE MENU ===== */
const menuBtn = document.getElementById('menuBtn');
const mobileMenu = document.getElementById('mobileMenu');

menuBtn.addEventListener('click', () => {
  const isOpen = mobileMenu.classList.toggle('open');
  menuBtn.setAttribute('aria-expanded', isOpen);
  menuBtn.textContent = isOpen ? '✕' : '☰';
});

document.querySelectorAll('.mobile-link').forEach(link => {
  link.addEventListener('click', () => {
    mobileMenu.classList.remove('open');
    menuBtn.textContent = '☰';
    menuBtn.setAttribute('aria-expanded', false);
  });
});

document.addEventListener('click', e => {
  if (!mobileMenu.contains(e.target) && e.target !== menuBtn) {
    mobileMenu.classList.remove('open');
    menuBtn.textContent = '☰';
  }
});

/* ===== SCROLL ANIMATIONS ===== */
const animObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry, i) => {
    if (entry.isIntersecting) {
      setTimeout(() => entry.target.classList.add('visible'), i * 90);
      animObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });

document.querySelectorAll('.animate-on-scroll').forEach(el => animObserver.observe(el));

/* ===== STAGGER DELAYS ===== */
document.querySelectorAll('.achievement-card').forEach((card, i) => {
  card.style.transitionDelay = `${i * 65}ms`;
});
document.querySelectorAll('.project-card').forEach((card, i) => {
  card.style.transitionDelay = `${i * 55}ms`;
});

/* ===== PORTFOLIO TABS ===== */
document.querySelectorAll('.ptab').forEach(btn => {
  btn.addEventListener('click', () => {
    const tab = btn.getAttribute('data-tab');

    // Toggle active tab button
    document.querySelectorAll('.ptab').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');

    // Toggle tab content
    document.querySelectorAll('.tab-content').forEach(tc => tc.classList.remove('active'));
    const target = document.getElementById(`tab-${tab}`);
    if (target) {
      target.classList.add('active');

      // Re-observe scroll animations for newly visible tab
      target.querySelectorAll('.animate-on-scroll').forEach(el => {
        el.classList.remove('visible');
        animObserver.observe(el);
      });
    }
  });
});

/* ===== STAT COUNTER ANIMATION ===== */
function animateCounter(el, target, suffix, duration = 1400) {
  const isFloat = String(target).includes('.');
  const decimals = isFloat ? 2 : 0;
  let start = null;
  const step = (ts) => {
    if (!start) start = ts;
    const progress = Math.min((ts - start) / duration, 1);
    const eased = 1 - Math.pow(1 - progress, 3);
    const value = eased * target;
    el.textContent = (isFloat ? value.toFixed(decimals) : Math.floor(value)) + suffix;
    if (progress < 1) requestAnimationFrame(step);
    else el.textContent = (isFloat ? target.toFixed(decimals) : target) + suffix;
  };
  requestAnimationFrame(step);
}

const statObserver = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const el = entry.target;
      const raw = el.getAttribute('data-count');
      const suffix = el.getAttribute('data-suffix') || '';
      if (raw) animateCounter(el, parseFloat(raw), suffix);
      statObserver.unobserve(el);
    }
  });
}, { threshold: 0.5 });

document.querySelectorAll('.mini-stat-number[data-count], .metric-number[data-count]').forEach(el => statObserver.observe(el));

/* ===== BACK TO TOP ===== */
const backToTopBtn = document.getElementById('backToTop');

function updateBackToTop() {
  if (backToTopBtn) {
    backToTopBtn.classList.toggle('show', window.scrollY > 400);
  }
}

if (backToTopBtn) {
  backToTopBtn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}

/* ===== SCROLL PROGRESS BAR ===== */
function updateScrollProgress() {
  if (scrollProgress) {
    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const scrollPercent = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
    scrollProgress.style.width = scrollPercent + '%';
  }
}

/* ===== SMOOTH SCROLL WITH CYBER WARP PORTAL TRANSITION ===== */
const warpPortal = document.getElementById('warpPortal');

function triggerSectionTransition(targetSelector) {
  const target = document.querySelector(targetSelector);
  if (!target) return;

  if (warpPortal) {
    warpPortal.classList.remove('active');
    void warpPortal.offsetWidth;
    warpPortal.classList.add('active');
    setTimeout(() => warpPortal.classList.remove('active'), 750);
  }

  if (typeof TechAudio !== 'undefined') {
    TechAudio.play('warp');
  }

  // Pre-scatter incoming section so it visibly converges into place
  target.classList.remove('converged');

  const offset = 80;
  window.scrollTo({ top: target.offsetTop - offset, behavior: 'smooth' });

  // Re-converge smoothly as user lands
  setTimeout(() => {
    target.classList.add('converged');
  }, 280);
}

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    const href = this.getAttribute('href');
    if (href && href !== '#' && document.querySelector(href)) {
      e.preventDefault();
      triggerSectionTransition(href);
    }
  });
});

document.querySelectorAll('.hud-node').forEach(node => {
  node.addEventListener('click', function () {
    const targetSel = this.getAttribute('data-target');
    if (targetSel) {
      triggerSectionTransition(targetSel);
    }
  });
});

/* ===== GALLERY MODAL ===== */
const modal = document.getElementById("imageModal");
const modalImg = document.getElementById("modalImg");
const captionText = document.getElementById("modalCaption");
const span = document.getElementsByClassName("modal-close")[0];

document.querySelectorAll('.gallery-item img').forEach(img => {
  img.addEventListener('click', function() {
    modal.style.display = "block";
    modalImg.src = this.src;
    captionText.innerHTML = this.nextElementSibling.querySelector('h4').innerHTML;
  });
});

if (span) {
  span.onclick = function() { 
    modal.style.display = "none";
  }
}

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

/* ===== SMOOTH SCROLL & INTERSECTION OBSERVER ===== */
const scrollElements = document.querySelectorAll('.animate-on-scroll, .animate-slide-up, .animate-fade-in');

const elementInView = (el, dividend = 1) => {
  const elementTop = el.getBoundingClientRect().top;
  return (elementTop <= (window.innerHeight || document.documentElement.clientHeight) / dividend);
};

const displayScrollElement = (element) => {
  element.classList.add('visible');
};

const handleScrollAnimation = () => {
  scrollElements.forEach((el) => {
    if (elementInView(el, 1.15)) {
      displayScrollElement(el);
    }
  });
};

window.addEventListener('scroll', () => {
  handleScrollAnimation();
});
handleScrollAnimation(); // Trigger on load

/* ===== PROJECT MODAL LOGIC ===== */
const projectCards = document.querySelectorAll('.compact-card');
const pModal = document.getElementById('projectModal');
const pClose = document.querySelector('.project-modal-close');

const pmTitle = document.getElementById('pm-title');
const pmYear = document.getElementById('pm-year');
const pmRole = document.getElementById('pm-role');
const pmTags = document.getElementById('pm-tags');
const pmDesc = document.getElementById('pm-desc');
const pmFeatures = document.getElementById('pm-features');
const pmIcon = document.getElementById('pm-icon');

projectCards.forEach(card => {
  card.addEventListener('click', () => {
    pmTitle.textContent = card.dataset.title;
    pmYear.textContent = card.dataset.year;
    pmRole.textContent = card.dataset.role;
    pmIcon.textContent = card.dataset.icon;
    pmDesc.textContent = card.dataset.desc;
    
    // Process tags
    pmTags.innerHTML = '';
    const tags = (card.dataset.tags || '').split(',');
    tags.forEach(tag => {
      const span = document.createElement('span');
      span.textContent = tag.trim();
      pmTags.appendChild(span);
    });

    // Process features
    pmFeatures.innerHTML = '';
    const features = (card.dataset.features || '').split('|');
    features.forEach(feat => {
      const li = document.createElement('li');
      li.textContent = feat.trim();
      pmFeatures.appendChild(li);
    });

    pModal.classList.add('active');
    document.body.style.overflow = 'hidden'; // prevent background scrolling
  });
});

if (pClose) {
  pClose.addEventListener('click', () => {
    pModal.classList.remove('active');
    document.body.style.overflow = '';
  });
}
window.addEventListener('click', (e) => {
  if (e.target === pModal) {
    pModal.classList.remove('active');
    document.body.style.overflow = '';
  }
});

/* ===== CONTACT FORM LOGIC ===== */
// Form handled natively by FormSubmit.co

/* ===== THEME TOGGLE ===== */
const themeToggle = document.getElementById('themeToggle');
const sunIcon = document.querySelector('.sun-icon');
const moonIcon = document.querySelector('.moon-icon');

function setTheme(isLight) {
  if (isLight) {
    document.documentElement.setAttribute('data-theme', 'light');
    if(sunIcon) sunIcon.style.display = 'block';
    if(moonIcon) moonIcon.style.display = 'none';
  } else {
    document.documentElement.removeAttribute('data-theme');
    if(sunIcon) sunIcon.style.display = 'none';
    if(moonIcon) moonIcon.style.display = 'block';
  }
}

if (themeToggle) {
  let isLight = false;
  themeToggle.addEventListener('click', () => {
    isLight = !isLight;
    setTheme(isLight);
  });
}

/* ===== CUSTOM CURSOR ===== */
const cursor = document.getElementById('customCursor');
const cursorFollower = document.getElementById('cursorFollower');

if (cursor && cursorFollower && window.matchMedia('(min-width: 1024px)').matches) {
  let mouseX = 0, mouseY = 0;
  let followerX = 0, followerY = 0;

  document.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
    cursor.style.left = mouseX + 'px';
    cursor.style.top = mouseY + 'px';
  });

  function animateFollower() {
    followerX += (mouseX - followerX) * 0.15;
    followerY += (mouseY - followerY) * 0.15;
    cursorFollower.style.left = followerX + 'px';
    cursorFollower.style.top = followerY + 'px';
    requestAnimationFrame(animateFollower);
  }
  animateFollower();

  const interactables = document.querySelectorAll('a, button, input, textarea, .gallery-item, .project-card, .nav-link');
  interactables.forEach(el => {
    el.addEventListener('mouseenter', () => {
      cursor.classList.add('hover');
      cursorFollower.classList.add('hover');
    });
    el.addEventListener('mouseleave', () => {
      cursor.classList.remove('hover');
      cursorFollower.classList.remove('hover');
    });
  });
}


/* ===== PRELOADER LOGIC ===== */
const lCanvas = document.getElementById('lightningCanvas');
if(lCanvas) {
  const lCtx = lCanvas.getContext('2d');
  
  function resizeLCanvas() {
    lCanvas.width = window.innerWidth;
    lCanvas.height = window.innerHeight;
  }
  window.addEventListener('resize', resizeLCanvas);
  resizeLCanvas();

  let bolts = [];
  let stars = [];
  let shootingStars = [];

  // Generate background stars
  for(let i=0; i<150; i++) {
    stars.push({
      x: Math.random() * lCanvas.width,
      y: Math.random() * lCanvas.height,
      radius: Math.random() * 1.5,
      alpha: Math.random(),
      blinkSpeed: Math.random() * 0.05
    });
  }

  class Bolt {
    constructor(isMain) {
      this.x = lCanvas.width / 2 + (Math.random() - 0.5) * 400;
      this.y = 0;
      this.path = [{x: this.x, y: this.y}];
      this.active = true;
      this.isMain = isMain;
      this.baseWidth = isMain ? Math.random() * 4 + 5 : Math.random() * 2 + 2;
    }
    
    update() {
      if(!this.active) return;
      
      let lastPoint = this.path[this.path.length - 1];
      let newX = lastPoint.x + (Math.random() - 0.5) * 60; // controlled zig-zag
      let newY = lastPoint.y + Math.random() * 15 + 8; // move down faster
      
      this.path.push({x: newX, y: newY});
      
      if(newY > lCanvas.height) {
        this.active = false;
      }
    }
    
    draw(ctx) {
      if(this.path.length < 2) return;
      
      // 1. Draw Outer Blue Glow
      ctx.beginPath();
      ctx.moveTo(this.path[0].x, this.path[0].y);
      for(let i=1; i<this.path.length; i++) {
        ctx.lineTo(this.path[i].x, this.path[i].y);
      }
      ctx.strokeStyle = `rgba(59, 130, 246, 0.8)`;
      ctx.lineWidth = this.baseWidth * 2;
      ctx.shadowBlur = 80;
      ctx.shadowColor = '#818cf8'; // bright blue
      ctx.stroke();

      // 2. Draw White Hot Core
      ctx.beginPath();
      ctx.moveTo(this.path[0].x, this.path[0].y);
      for(let i=1; i<this.path.length; i++) {
        ctx.lineTo(this.path[i].x, this.path[i].y);
      }
      ctx.strokeStyle = `rgba(255, 255, 255, 0.9)`;
      ctx.lineWidth = this.baseWidth * 0.5;
      ctx.shadowBlur = 25;
      ctx.shadowColor = '#ffffff';
      ctx.stroke();
    }
  }

  class ShootingStar {
    constructor() {
      this.x = lCanvas.width / 2 + (Math.random() - 0.5) * 400;
      this.y = 0;
      this.length = Math.random() * 80 + 20;
      this.speed = Math.random() * 10 + 15;
      this.active = true;
    }
    update() {
      this.x -= this.speed; // move left
      this.y += this.speed; // move down
      if(this.x < 0 || this.y > lCanvas.height) this.active = false;
    }
    draw(ctx) {
      ctx.beginPath();
      ctx.moveTo(this.x, this.y);
      ctx.lineTo(this.x + this.length, this.y - this.length);
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.8)';
      ctx.lineWidth = 2;
      ctx.shadowBlur = 25;
      ctx.shadowColor = 'white';
      ctx.stroke();
    }
  }

  function animateLightning() {
    if(!document.getElementById('preloader')) return;
    
    // Fade out for lightning trail, clear dark enough to maintain galaxy black
    lCtx.globalCompositeOperation = 'destination-out';
    lCtx.fillStyle = 'rgba(0, 0, 0, 0.15)';
    lCtx.fillRect(0, 0, lCanvas.width, lCanvas.height);
    lCtx.globalCompositeOperation = 'source-over';
    
    // Draw background stars
    stars.forEach(star => {
      star.alpha += star.blinkSpeed;
      if(star.alpha > 1 || star.alpha < 0) star.blinkSpeed *= -1;
      lCtx.beginPath();
      lCtx.arc(star.x, star.y, star.radius, 0, Math.PI * 2);
      lCtx.fillStyle = `rgba(255, 255, 255, ${Math.abs(star.alpha)})`;
      lCtx.shadowBlur = 0;
      lCtx.fill();
    });

    // Spawn shooting stars
    if(Math.random() < 0.03) {
      shootingStars.push(new ShootingStar());
    }

    shootingStars = shootingStars.filter(s => s.active);
    shootingStars.forEach(s => {
      s.update();
      s.draw(lCtx);
    });
    
    // Spawn lightning bolts
    if(Math.random() < 0.06 && bolts.filter(b => b.active).length < 2) {
      bolts.push(new Bolt(true));
      // spawn branch
      if(Math.random() < 0.5) bolts.push(new Bolt(false));
    }
    
    // Background lightning flash
    if(Math.random() < 0.02) {
      lCtx.fillStyle = 'rgba(60, 100, 255, 0.02)';
      lCtx.fillRect(0, 0, lCanvas.width, lCanvas.height);
    }
    
    bolts = bolts.filter(b => b.active || Math.random() < 0.90); // keep dead bolts shortly for glow trail
    bolts.forEach(bolt => {
      for(let i=0; i<2; i++) bolt.update(); // slower strike
      bolt.draw(lCtx);
    });
    
    requestAnimationFrame(animateLightning);
  }
  
  animateLightning();
  
  // Progress Bar Logic
  const lBar = document.getElementById('loadingBar');
  const lPercent = document.getElementById('loadingPercent');
  let progress = 0;
  
  const pInterval = setInterval(() => {
    progress += Math.random() * 8; 
    if(progress >= 100) progress = 100;
    
    lBar.style.width = progress + '%';
    lPercent.textContent = Math.floor(progress) + '%';
    
    if(progress === 100) {
      clearInterval(pInterval);
      setTimeout(() => {
        const preloader = document.getElementById('preloader');
        preloader.style.opacity = '0';
        setTimeout(() => {
          preloader.remove();
          document.body.classList.add('loaded');
        }, 800);
      }, 500);
    }
  }, 120);
}


/* ===== TYPEWRITER LOGIC ===== */
const typeText = document.getElementById('typewriter-text');
if (typeText) {
  const phrases = [
    "I'm an Electronics & Telecommunications Student.",
    "I'm an IoT Developer & Tech Enthusiast.",
    "I'm a Creative Problem Solver."
  ];
  let phraseIndex = 0;
  let charIndex = 0;
  let isDeleting = false;
  
  function typeEffect() {
    const currentPhrase = phrases[phraseIndex];
    if (isDeleting) {
      typeText.textContent = currentPhrase.substring(0, charIndex - 1);
      charIndex--;
    } else {
      typeText.textContent = currentPhrase.substring(0, charIndex + 1);
      charIndex++;
    }
    
    let typeSpeed = isDeleting ? 40 : 80;
    
    if (!isDeleting && charIndex === currentPhrase.length) {
      typeSpeed = 2000; // pause at end of word
      isDeleting = true;
    } else if (isDeleting && charIndex === 0) {
      isDeleting = false;
      phraseIndex = (phraseIndex + 1) % phrases.length;
      typeSpeed = 500; // pause before typing next
    }
    
    setTimeout(typeEffect, typeSpeed);
  }
  
  setTimeout(typeEffect, 1000);
}

/* ===== SUCCESS CONFETTI LOGIC ===== */
function fireConfetti() {
  const colors = ['#3b82f6', '#60a5fa', '#ffffff', '#f59e0b', '#ef4444'];
  for(let i=0; i<100; i++) {
    const conf = document.createElement('div');
    conf.style.position = 'fixed';
    conf.style.width = Math.random() * 8 + 4 + 'px';
    conf.style.height = Math.random() * 16 + 8 + 'px';
    conf.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
    conf.style.left = Math.random() * 100 + 'vw';
    conf.style.top = '-20px';
    conf.style.zIndex = '9999999';
    conf.style.pointerEvents = 'none';
    conf.style.borderRadius = Math.random() > 0.5 ? '50%' : '0';
    document.body.appendChild(conf);
    
    const animation = conf.animate([
      { transform: `translate3d(0, 0, 0) rotate(0deg)`, opacity: 1 },
      { transform: `translate3d(${(Math.random() - 0.5) * 300}px, ${window.innerHeight + 100}px, 0) rotate(${Math.random() * 720}deg)`, opacity: 0 }
    ], {
      duration: Math.random() * 2000 + 2000,
      easing: 'cubic-bezier(.37,0,.63,1)'
    });
    
    animation.onfinish = () => conf.remove();
  }
}

const contactForm = document.getElementById('contactForm');
if (contactForm) {
  contactForm.addEventListener('submit', function(e) {
    e.preventDefault(); // Stop page reload
    
    // FIRE CONFETTI!
    fireConfetti();
    playHoverSound(); // play a beep for success
    
    const btn = contactForm.querySelector('button');
    const originalText = btn.innerHTML;
    btn.innerHTML = '✨ Pesan Sedang Dikirim... ✨';
    btn.disabled = true;
    
    const formData = new FormData(contactForm);
    fetch(contactForm.action, {
      method: 'POST',
      body: formData,
      headers: {
        'Accept': 'application/json'
      }
    }).then(response => {
      contactForm.reset();
      btn.innerHTML = '✨ Pesan Berhasil Terkirim! ✨';
      setTimeout(() => {
        btn.innerHTML = originalText;
        btn.disabled = false;
      }, 5000);
    }).catch(error => {
      btn.innerHTML = '❌ Gagal Mengirim';
      setTimeout(() => {
        btn.innerHTML = originalText;
        btn.disabled = false;
      }, 3000);
    });
  });
}

/* ===== CERTIFICATE MODAL LOGIC ===== */
(function initCertificateModal() {
  const certModal = document.getElementById('certModal');
  if (!certModal) return;

  const certModalBackdrop = document.getElementById('certModalBackdrop');
  const certModalCloseBtn = document.getElementById('certModalCloseBtn');
  const certModalTitle = document.getElementById('certModalTitle');
  const certModalSubtitle = document.getElementById('certModalSubtitle');
  const certModalBadge = document.getElementById('certModalBadge');
  const certModalOpenBtn = document.getElementById('certModalOpenBtn');
  const certModalDownloadBtn = document.getElementById('certModalDownloadBtn');
  const certImageWrap = document.getElementById('certImageWrap');
  const certModalImg = document.getElementById('certModalImg');
  const certPdfWrap = document.getElementById('certPdfWrap');
  const certModalIframe = document.getElementById('certModalIframe');
  const certPdfFallbackBtn = document.getElementById('certPdfFallbackBtn');

  function openCertificate(certUrl, title, subtitle, badge) {
    if (!certUrl) return;

    if (certModalTitle) certModalTitle.textContent = title || 'Sertifikat Penghargaan';
    if (certModalSubtitle) certModalSubtitle.textContent = subtitle || '';
    if (certModalBadge) certModalBadge.textContent = badge || '🏆 Official Certificate';

    const cleanName = certUrl.split('/').pop();
    if (certModalOpenBtn) certModalOpenBtn.href = certUrl;
    if (certModalDownloadBtn) {
      certModalDownloadBtn.href = certUrl;
      certModalDownloadBtn.setAttribute('download', cleanName);
    }
    if (certPdfFallbackBtn) certPdfFallbackBtn.href = certUrl;

    const isPdf = certUrl.toLowerCase().endsWith('.pdf');
    if (isPdf) {
      if (certImageWrap) certImageWrap.style.display = 'none';
      if (certModalImg) certModalImg.src = '';
      if (certPdfWrap) certPdfWrap.style.display = 'flex';
      if (certModalIframe) certModalIframe.src = certUrl;
    } else {
      if (certPdfWrap) certPdfWrap.style.display = 'none';
      if (certModalIframe) certModalIframe.src = '';
      if (certImageWrap) certImageWrap.style.display = 'flex';
      if (certModalImg) certModalImg.src = certUrl;
    }

    certModal.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeCertificate() {
    certModal.classList.remove('active');
    document.body.style.overflow = '';
    setTimeout(() => {
      if (certModalIframe) certModalIframe.src = '';
      if (certModalImg) certModalImg.src = '';
    }, 250);
  }

  if (certModalCloseBtn) certModalCloseBtn.addEventListener('click', closeCertificate);
  if (certModalBackdrop) certModalBackdrop.addEventListener('click', closeCertificate);

  window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && certModal.classList.contains('active')) {
      closeCertificate();
    }
  });

  // Attach click & enter/space keydown listener to each achievement card
  // Attach click & enter/space keydown listener to both achievement cards and certification cards
  document.querySelectorAll('.achievement-card[data-cert], .cert-card[data-cert]').forEach(card => {
    const handleTrigger = () => {
      const cert = card.getAttribute('data-cert');
      if (!cert) return;
      const titleEl = card.querySelector('h3') || card.querySelector('strong');
      const title = titleEl ? titleEl.textContent.trim() : 'Sertifikat';
      const p = card.querySelector('p') ? card.querySelector('p').textContent.trim() : '';
      const org = card.querySelector('.achieve-org') ? card.querySelector('.achieve-org').textContent.trim() : '';
      const iconEl = card.querySelector('.achieve-icon') || card.querySelector('.cert-icon');
      const icon = iconEl ? iconEl.textContent.trim() : '🏅';
      const subtitle = org ? `${p} • ${org}` : p;
      const customBadge = card.getAttribute('data-badge') || '🏅 Official Verified';
      openCertificate(cert, `${icon} ${title}`, subtitle, customBadge);
    };

    card.addEventListener('click', handleTrigger);
    card.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        handleTrigger();
      }
    });
  });
})();


/* ===== AWARDS CATEGORY FILTER ===== */
(function initAwardsFilter() {
  const filterBtns = document.querySelectorAll('.award-filter-btn');
  const cards = document.querySelectorAll('.achievement-card[data-category]');
  if (!filterBtns.length) return;

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const filter = btn.getAttribute('data-filter');

      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      cards.forEach(card => {
        const cat = card.getAttribute('data-category');
        if (filter === 'all' || cat === filter) {
          card.classList.remove('filter-hidden');
        } else {
          card.classList.add('filter-hidden');
        }
      });
    });
  });
})();

/* ===== SKILL PROFICIENCY BAR ANIMATION ===== */
(function initProficiencyBars() {
  const bars = document.querySelectorAll('.prof-bar-fill');
  if (!bars.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const bar = entry.target;
        const width = bar.getAttribute('data-width');
        bar.style.width = width + '%';
        observer.unobserve(bar);
      }
    });
  }, { threshold: 0.3 });

  bars.forEach(bar => observer.observe(bar));
})();

/* ===== REAL-TIME PEKANBARU WIB WORLD CLOCK ===== */
(function initLiveWIBClock() {
  const clockEl = document.getElementById('liveClockDisplay');
  if (!clockEl) return;

  function updateTime() {
    try {
      const now = new Date();
      const formatter = new Intl.DateTimeFormat('id-ID', {
        timeZone: 'Asia/Jakarta',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
        hour12: false
      });
      clockEl.textContent = formatter.format(now).replace(/\./g, ':') + ' WIB';
    } catch (e) {
      const now = new Date();
      clockEl.textContent = now.toTimeString().split(' ')[0] + ' WIB';
    }
  }
  updateTime();
  setInterval(updateTime, 1000);
})();

/* ===== 3D PERSPECTIVE TILT WITH DYNAMIC GLARE ===== */
(function init3DTiltEngine() {
  // Only apply on non-touch desktop devices for buttery smooth feel
  if (window.matchMedia('(pointer: coarse)').matches) return;

  const targetSelector = '.hero-status-card, .metric-card, .project-card, .cert-card, .achievement-card, .org-card, .skill-proficiency-section';
  const cards = document.querySelectorAll(targetSelector);

  cards.forEach(card => {
    let bounds;

    function onMouseEnter(e) {
      bounds = card.getBoundingClientRect();
      card.style.transition = 'transform 0.1s ease, box-shadow 0.25s ease';
    }

    function onMouseMove(e) {
      if (!bounds) bounds = card.getBoundingClientRect();
      const mouseX = e.clientX - bounds.left;
      const mouseY = e.clientY - bounds.top;

      const xPercent = (mouseX / bounds.width) - 0.5;
      const yPercent = (mouseY / bounds.height) - 0.5;

      const rotateX = -yPercent * 10;
      const rotateY = xPercent * 10;

      card.style.transform = `perspective(1000px) rotateX(${rotateX.toFixed(2)}deg) rotateY(${rotateY.toFixed(2)}deg) translateZ(6px) scale3d(1.015, 1.015, 1.015)`;
      card.style.setProperty('--glare-x', `${mouseX}px`);
      card.style.setProperty('--glare-y', `${mouseY}px`);
      card.style.setProperty('--glare-opacity', '1');
    }

    function onMouseLeave() {
      card.style.transition = 'transform 0.45s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.45s ease';
      card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) translateZ(0) scale3d(1, 1, 1)';
      card.style.setProperty('--glare-opacity', '0');
    }

    card.addEventListener('mouseenter', onMouseEnter);
    card.addEventListener('mousemove', onMouseMove);
    card.addEventListener('mouseleave', onMouseLeave);
  });
})();

/* ===== WEB-AUDIO TECH HAPTIC SOUND FX ===== */
const TechAudio = (function initTechAudio() {
  let ctx = null;
  let enabled = false;

  const toggleBtn = document.getElementById('soundToggle');
  const onIcon = toggleBtn ? toggleBtn.querySelector('.sound-on-icon') : null;
  const offIcon = toggleBtn ? toggleBtn.querySelector('.sound-off-icon') : null;

  function initCtx() {
    if (!ctx) {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      if (AudioCtx) ctx = new AudioCtx();
    }
    if (ctx && ctx.state === 'suspended') {
      ctx.resume();
    }
  }

  function play(type = 'click') {
    if (!enabled) return;
    initCtx();
    if (!ctx) return;

    try {
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.connect(gain);
      gain.connect(ctx.destination);

      const now = ctx.currentTime;
      if (type === 'click') {
        osc.type = 'sine';
        osc.frequency.setValueAtTime(1100, now);
        osc.frequency.exponentialRampToValueAtTime(500, now + 0.04);
        gain.gain.setValueAtTime(0.04, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.04);
        osc.start(now);
        osc.stop(now + 0.04);
      } else if (type === 'modal') {
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(450, now);
        osc.frequency.exponentialRampToValueAtTime(880, now + 0.08);
        gain.gain.setValueAtTime(0.05, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.08);
        osc.start(now);
        osc.stop(now + 0.08);
      } else if (type === 'tab') {
        osc.type = 'sine';
        osc.frequency.setValueAtTime(750, now);
        gain.gain.setValueAtTime(0.035, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.05);
        osc.start(now);
        osc.stop(now + 0.05);
      } else if (type === 'warp') {
        osc.type = 'sine';
        osc.frequency.setValueAtTime(320, now);
        osc.frequency.exponentialRampToValueAtTime(1400, now + 0.16);
        osc.frequency.exponentialRampToValueAtTime(400, now + 0.32);
        gain.gain.setValueAtTime(0.05, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.32);
        osc.start(now);
        osc.stop(now + 0.32);
      } else if (type === 'packet') {
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(950, now);
        osc.frequency.exponentialRampToValueAtTime(1750, now + 0.08);
        gain.gain.setValueAtTime(0.045, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.08);
        osc.start(now);
        osc.stop(now + 0.08);
      }
    } catch (e) {}
  }

  if (toggleBtn) {
    toggleBtn.addEventListener('click', () => {
      initCtx();
      enabled = !enabled;
      toggleBtn.classList.toggle('active', enabled);
      if (onIcon && offIcon) {
        onIcon.style.display = enabled ? 'block' : 'none';
        offIcon.style.display = enabled ? 'none' : 'block';
      }
      if (enabled) play('modal');
    });
  }

  // Attach soft clicks to buttons and tabs
  document.addEventListener('click', (e) => {
    if (e.target.closest('.ptab, .award-filter-btn, .project-filter-btn, .btn-primary, .btn-outline-hero, .cert-card, .achievement-card')) {
      play('click');
    }
  });

  return { play };
})();

/* ===== PROJECTS FILTER & REAL-TIME SEARCH ===== */
(function initProjectsFilterAndSearch() {
  const filterBtns = document.querySelectorAll('.project-filter-btn');
  const searchInput = document.getElementById('projectSearchInput');
  const clearBtn = document.getElementById('projectSearchClear');
  const cards = document.querySelectorAll('.project-card');
  const grid = document.querySelector('.projects-grid');
  if (!filterBtns.length || !cards.length) return;

  let currentFilter = 'all';
  let currentQuery = '';

  function applyFilter() {
    let visibleCount = 0;

    cards.forEach(card => {
      const cats = (card.getAttribute('data-category') || '').split(',');
      const title = (card.getAttribute('data-title') || '').toLowerCase();
      const desc = (card.getAttribute('data-desc') || '').toLowerCase();
      const tags = (card.getAttribute('data-tags') || '').toLowerCase();

      const matchesCategory = currentFilter === 'all' || cats.includes(currentFilter);
      const matchesSearch = !currentQuery || title.includes(currentQuery) || desc.includes(currentQuery) || tags.includes(currentQuery);

      if (matchesCategory && matchesSearch) {
        card.classList.remove('filter-hidden');
        visibleCount++;
      } else {
        card.classList.add('filter-hidden');
      }
    });

    // Handle Empty State
    let emptyMsg = grid.querySelector('.projects-empty-state');
    if (visibleCount === 0) {
      if (!emptyMsg) {
        emptyMsg = document.createElement('div');
        emptyMsg.className = 'projects-empty-state';
        emptyMsg.innerHTML = `
          <span>🔍</span>
          <h3>Tidak ada proyek yang sesuai</h3>
          <p>Coba kata kunci lain atau setel ulang filter pencarian.</p>
          <button class="btn-reset-filter" id="resetProjectFilterBtn">Reset Filter & Pencarian</button>
        `;
        grid.appendChild(emptyMsg);
        document.getElementById('resetProjectFilterBtn').addEventListener('click', () => {
          currentFilter = 'all';
          currentQuery = '';
          if (searchInput) searchInput.value = '';
          if (clearBtn) clearBtn.style.display = 'none';
          filterBtns.forEach(b => b.classList.toggle('active', b.getAttribute('data-filter') === 'all'));
          applyFilter();
        });
      }
    } else if (emptyMsg) {
      emptyMsg.remove();
    }
  }

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentFilter = btn.getAttribute('data-filter');
      applyFilter();
    });
  });

  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      currentQuery = e.target.value.trim().toLowerCase();
      if (clearBtn) clearBtn.style.display = currentQuery ? 'block' : 'none';
      applyFilter();
    });
  }

  if (clearBtn) {
    clearBtn.addEventListener('click', () => {
      searchInput.value = '';
      currentQuery = '';
      clearBtn.style.display = 'none';
      searchInput.focus();
      applyFilter();
    });
  }
})();

/* ===== SILICON-VALLEY COMMAND PALETTE (CTRL + K) ===== */
(function initCommandPalette() {
  const modal = document.getElementById('cmdPaletteModal');
  const input = document.getElementById('cmdInput');
  const resultsEl = document.getElementById('cmdResults');
  const backdrop = document.getElementById('cmdBackdrop');
  const openBtn = document.getElementById('cmdBtn');
  if (!modal || !input || !resultsEl) return;

  const commands = [
    // Navigation
    { type: 'Navigasi', icon: '🏠', title: 'Home', subtitle: 'Kembali ke bagian utama', action: () => scrollTo('#home') },
    { type: 'Navigasi', icon: '👤', title: 'About Me', subtitle: 'Profil, latar belakang, dan riwayat singkat', action: () => scrollTo('#about') },
    { type: 'Navigasi', icon: '🚀', title: 'Portfolio Projects', subtitle: 'Lihat koleksi proyek teknologi & rekayasa', action: () => switchPortfolioTab('projects') },
    { type: 'Navigasi', icon: '⚙️', title: 'Tech Stack & Skills', subtitle: 'Instrumen, RF, sirkuit, dan keahlian teknis', action: () => switchPortfolioTab('skills') },
    { type: 'Navigasi', icon: '🏆', title: 'Awards & Honors', subtitle: 'Medali olimpiade sains, beasiswa tahfidz, IPK tertinggi', action: () => switchPortfolioTab('achievements') },
    { type: 'Navigasi', icon: '📸', title: 'Gallery & Dokumentasi', subtitle: 'Dokumentasi foto kegiatan dan momen berharga', action: () => switchPortfolioTab('gallery') },
    { type: 'Navigasi', icon: '🏛️', title: 'Organisasi & Kepemimpinan', subtitle: 'Pengalaman UKMI, AET PCR, dan kepengurusan', action: () => switchPortfolioTab('organizations') },
    { type: 'Navigasi', icon: '✉️', title: 'Hubungi Saya (Contact)', subtitle: 'Kirim pesan langsung ke email Nassya', action: () => scrollTo('#contact') },
    
    // Actions
    { type: 'Aksi', icon: '📄', title: 'Unduh CV Resmi (PDF)', subtitle: 'Download berkas CV Nassya Adystira', action: () => downloadCV() },
    { type: 'Aksi', icon: '🌓', title: 'Ganti Tema (Dark / Light)', subtitle: 'Beralih antara mode gelap dan mode terang', action: () => toggleTheme() },

    // Certifications
    { type: 'Sertifikasi', icon: '🏅', title: 'Cisco: Introduction to Networks', subtitle: 'Lihat Sertifikat Resmi CCNA Cisco Academy', action: () => openCert('CERTIFICATION INTRODUCTION.pdf', 'Introduction to Networks', 'Cisco Networking Academy · September 2025') },
    { type: 'Sertifikasi', icon: '🏅', title: 'Cisco: Switching, Routing, & Wireless', subtitle: 'Lihat Sertifikat Resmi CCNA Cisco Academy', action: () => openCert('CERTIFICATION SWITCHING ROUTING.pdf', 'Switching, Routing, and Wireless Essentials', 'Cisco Networking Academy · January 2026') },

    // Featured Projects
    { type: 'Proyek', icon: '📷', title: 'Real-Time Friday Prayer Counter', subtitle: 'Computer Vision & YOLOv8 crowd counter', action: () => openProject('Real-Time Friday Prayer Congregation Counter') },
    { type: 'Proyek', icon: '📡', title: 'Microstrip Antenna Design', subtitle: 'Simulasi antena 2.4 GHz di CST Studio Suite', action: () => openProject('Microstrip Antenna Design') },
    { type: 'Proyek', icon: '🌐', title: 'FTTH Network Simulation', subtitle: 'Pemodelan jaringan fiber optik di OptiSystem', action: () => openProject('FTTH Network Simulation') },
    { type: 'Proyek', icon: '🌦️', title: 'IoT Automatic Clothesline', subtitle: 'Sistem jemuran otomatis berbasis ESP32 & sensor', action: () => openProject('IoT-Based Automatic Clothesline System') },
    { type: 'Proyek', icon: '🤖', title: 'Line Follower Robot', subtitle: 'Robot navigasi garis otonom berbasis sensor IR', action: () => openProject('Line Follower Robot') },
    { type: 'Proyek', icon: '📶', title: 'BTS Site Design & Bad Spot', subtitle: 'Analisis jangkauan sinyal dengan CellMapper & AutoCAD', action: () => openProject('BTS Site Design & Bad Spot Analysis') },

    // Featured Awards
    { type: 'Penghargaan', icon: '🥇', title: 'Gold Medal – Physics (NYSO 2025)', subtitle: 'National Youth Science Olympiad 2.0', action: () => openAwardCert('sertifikat-nyso-physics-2025.pdf', 'Gold Medal – Physics', 'NYSO 2.0 (2025)') },
    { type: 'Penghargaan', icon: '📜', title: "Beasiswa Tahfidz Al-Qur'an", subtitle: 'Pemerintah Provinsi Riau (2023)', action: () => openAwardCert('sertifikat-beasiswa-tahfidz.png', 'Tahfidz Scholarship', 'Pemerintah Provinsi Riau (2023)') },
    { type: 'Penghargaan', icon: '🏆', title: 'Highest GPA (3.97 & 3.94)', subtitle: 'Mahasiswa Berprestasi Terbaik D-IV TET PCR', action: () => openAwardCert('sertifikat-highest-gpa-397.jpeg', 'Highest GPA (3.97)', 'Politeknik Caltex Riau') }
  ];

  let selectedIndex = 0;
  let filtered = [...commands];

  function openPalette() {
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
    input.value = '';
    renderResults('');
    setTimeout(() => input.focus(), 50);
    TechAudio.play('modal');
  }

  function closePalette() {
    modal.classList.remove('active');
    document.body.style.overflow = '';
  }

  function scrollTo(selector) {
    closePalette();
    const el = document.querySelector(selector);
    if (el) el.scrollIntoView({ behavior: 'smooth' });
  }

  function switchPortfolioTab(tabId) {
    closePalette();
    scrollTo('#portfolio');
    setTimeout(() => {
      const tabBtn = document.querySelector(`.ptab[data-tab="${tabId}"]`);
      if (tabBtn) tabBtn.click();
    }, 400);
  }

  function downloadCV() {
    closePalette();
    const a = document.createElement('a');
    a.href = 'CV_Nassya_Adystira.pdf';
    a.download = 'CV_Nassya_Adystira.pdf';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
  }

  function toggleTheme() {
    closePalette();
    const btn = document.getElementById('themeToggle');
    if (btn) btn.click();
  }

  function openCert(file, title, subtitle) {
    closePalette();
    const card = document.querySelector(`.cert-card[data-cert="${file}"]`);
    if (card) {
      card.click();
    }
  }

  function openAwardCert(file, title, subtitle) {
    closePalette();
    switchPortfolioTab('achievements');
    setTimeout(() => {
      const card = document.querySelector(`.achievement-card[data-cert="${file}"]`);
      if (card) card.click();
    }, 500);
  }

  function openProject(title) {
    closePalette();
    switchPortfolioTab('projects');
    setTimeout(() => {
      const card = document.querySelector(`.project-card[data-title="${title}"]`);
      if (card) {
        const btn = card.querySelector('.btn-view-details');
        if (btn) btn.click();
      }
    }, 500);
  }

  function renderResults(query) {
    const q = query.toLowerCase().trim();
    if (!q) {
      filtered = commands.slice(0, 10);
    } else {
      filtered = commands.filter(c =>
        c.title.toLowerCase().includes(q) ||
        c.subtitle.toLowerCase().includes(q) ||
        c.type.toLowerCase().includes(q)
      );
    }

    selectedIndex = 0;
    if (filtered.length === 0) {
      resultsEl.innerHTML = '<div style="text-align:center;padding:32px;color:#94a3b8;font-size:0.9rem;">Tidak ada perintah atau item yang cocok.</div>';
      return;
    }

    let html = '';
    let currentType = '';

    filtered.forEach((item, idx) => {
      if (item.type !== currentType) {
        currentType = item.type;
        html += `<div class="cmd-group-title">${currentType}</div>`;
      }
      const isSelected = idx === selectedIndex ? 'selected' : '';
      html += `
        <div class="cmd-item ${isSelected}" data-idx="${idx}">
          <div class="cmd-item-left">
            <span class="cmd-item-icon">${item.icon}</span>
            <div class="cmd-item-text">
              <strong>${item.title}</strong>
              <span>${item.subtitle}</span>
            </div>
          </div>
          <span class="cmd-item-badge">${item.type}</span>
        </div>
      `;
    });

    resultsEl.innerHTML = html;

    resultsEl.querySelectorAll('.cmd-item').forEach(el => {
      el.addEventListener('click', () => {
        const idx = parseInt(el.getAttribute('data-idx'));
        if (filtered[idx]) filtered[idx].action();
      });
      el.addEventListener('mouseenter', () => {
        resultsEl.querySelectorAll('.cmd-item').forEach(i => i.classList.remove('selected'));
        el.classList.add('selected');
        selectedIndex = parseInt(el.getAttribute('data-idx'));
      });
    });
  }

  input.addEventListener('input', (e) => {
    renderResults(e.target.value);
  });

  input.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowDown') {
      e.preventDefault();
      selectedIndex = (selectedIndex + 1) % filtered.length;
      updateSelectedVisual();
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      selectedIndex = (selectedIndex - 1 + filtered.length) % filtered.length;
      updateSelectedVisual();
    } else if (e.key === 'Enter') {
      e.preventDefault();
      if (filtered[selectedIndex]) filtered[selectedIndex].action();
    } else if (e.key === 'Escape') {
      closePalette();
    }
  });

  function updateSelectedVisual() {
    const items = resultsEl.querySelectorAll('.cmd-item');
    items.forEach((item, idx) => {
      item.classList.toggle('selected', idx === selectedIndex);
      if (idx === selectedIndex) {
        item.scrollIntoView({ block: 'nearest' });
      }
    });
  }

  // Keyboard shortcut Ctrl + K or Cmd + K
  window.addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
      e.preventDefault();
      if (modal.classList.contains('active')) closePalette();
      else openPalette();
    } else if (e.key === 'Escape' && modal.classList.contains('active')) {
      closePalette();
    }
  });

  if (openBtn) openBtn.addEventListener('click', openPalette);
  if (backdrop) backdrop.addEventListener('click', closePalette);
})();

/* ===== SECTION CONVERGE OBSERVER ("NYEBAR KE TENGAH") ===== */
(function initSectionConvergeSystem() {
  const convergeSections = document.querySelectorAll('.section-converge');
  if (!convergeSections.length) return;

  const convergeObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('converged');
      } else {
        const rect = entry.target.getBoundingClientRect();
        if (rect.top > window.innerHeight * 0.95 || rect.bottom < 0) {
          entry.target.classList.remove('converged');
        }
      }
    });
  }, { threshold: 0.12, rootMargin: '-40px 0px -60px 0px' });

  convergeSections.forEach(sec => convergeObserver.observe(sec));
})();

/* ===== INTERACTIVE TELECOM & IOT NETWORK SIMULATOR ===== */
(function initTelecomSimulator() {
  const txBtn = document.getElementById('simTxBtn');
  const packet = document.getElementById('simPacket');
  const carrierStatus = document.getElementById('simCarrierStatus');
  const logConsole = document.getElementById('simLogConsole');
  const protoBtns = document.querySelectorAll('.sim-proto-btn');
  const metricRssi = document.getElementById('simMetricRssi');
  const metricPing = document.getElementById('simMetricPing');
  const metricSnr = document.getElementById('simMetricSnr');
  const metricLoss = document.getElementById('simMetricLoss');

  if (!txBtn || !packet) return;

  const nodeEls = [
    document.getElementById('simNode1'),
    document.getElementById('simNode2'),
    document.getElementById('simNode3'),
    document.getElementById('simNode4')
  ];

  let activeProtocol = 'lora';
  let isTransmitting = false;
  let packetCounter = 101;

  const protoConfig = {
    lora: { freq: '915.00 MHz', carrier: 'LoRaWAN AU915', pingBase: 18, rssiBase: -65, snrBase: 9.5 },
    mqtt: { freq: '2.40 GHz WiFi', carrier: 'MQTT over TLS:8883', pingBase: 12, rssiBase: -54, snrBase: 14.0 },
    fiber: { freq: '1310/1490 nm', carrier: 'GPON FTTH Optical', pingBase: 4, rssiBase: -19, snrBase: 28.5 },
    '5g': { freq: '3.50 GHz (n78)', carrier: '5G NR Standalone', pingBase: 7, rssiBase: -58, snrBase: 18.2 }
  };

  protoBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      protoBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      activeProtocol = btn.getAttribute('data-proto');
      const cfg = protoConfig[activeProtocol] || protoConfig.lora;
      if (carrierStatus) carrierStatus.textContent = `CARRIER: LOCKED · ${cfg.carrier}`;
      addLog(`[CONFIG] Protocol switched to ${btn.textContent.trim()} [${cfg.freq}].`);
      if (typeof TechAudio !== 'undefined') TechAudio.play('tab');
    });
  });

  function addLog(text) {
    if (!logConsole) return;
    const now = new Date();
    const timeStr = `${String(now.getHours()).padStart(2, '0')}:${String(now.getMinutes()).padStart(2, '0')}:${String(now.getSeconds()).padStart(2, '0')}`;
    const row = document.createElement('div');
    row.innerHTML = `<span style="color:#64748b;">${timeStr}</span> ${text}`;
    logConsole.appendChild(row);
    logConsole.scrollTop = logConsole.scrollHeight;
  }

  txBtn.addEventListener('click', () => {
    if (isTransmitting) return;
    isTransmitting = true;
    txBtn.disabled = true;
    packetCounter++;

    if (typeof TechAudio !== 'undefined') TechAudio.play('packet');

    const cfg = protoConfig[activeProtocol] || protoConfig.lora;
    const jitterPing = Math.max(2, Math.round(cfg.pingBase + (Math.random() * 6 - 3)));
    const jitterRssi = Math.round(cfg.rssiBase + (Math.random() * 4 - 2));
    const jitterSnr = (cfg.snrBase + (Math.random() * 1.5 - 0.75)).toFixed(1);

    if (metricRssi) metricRssi.textContent = `${jitterRssi} dBm`;
    if (metricPing) metricPing.textContent = `${jitterPing} ms`;
    if (metricSnr) metricSnr.textContent = `+${jitterSnr} dB`;
    if (metricLoss) metricLoss.textContent = '0.0%';

    addLog(`<span class="log-hl">[TX]</span> Frame #${packetCounter} [${activeProtocol.toUpperCase()}] queued from ESP32.`);

    // Trigger visual packet animation
    packet.classList.remove('flying');
    void packet.offsetWidth;
    packet.classList.add('flying');

    // Sequential node highlight
    nodeEls.forEach(n => n && n.classList.remove('node-transmitting'));
    if (nodeEls[0]) nodeEls[0].classList.add('node-transmitting');

    setTimeout(() => {
      if (nodeEls[0]) nodeEls[0].classList.remove('node-transmitting');
      if (nodeEls[1]) nodeEls[1].classList.add('node-transmitting');
      addLog(`[RELAY] Gateway demodulated RF frame. RSSI: ${jitterRssi} dBm.`);
      if (typeof TechAudio !== 'undefined') TechAudio.play('click');
    }, 450);

    setTimeout(() => {
      if (nodeEls[1]) nodeEls[1].classList.remove('node-transmitting');
      if (nodeEls[2]) nodeEls[2].classList.add('node-transmitting');
      addLog(`[BROKER] MQTT broker published payload to /telecom/nassya/sensor.`);
      if (typeof TechAudio !== 'undefined') TechAudio.play('click');
    }, 950);

    setTimeout(() => {
      if (nodeEls[2]) nodeEls[2].classList.remove('node-transmitting');
      if (nodeEls[3]) nodeEls[3].classList.add('node-transmitting');
      addLog(`<span class="log-hl">[ACK]</span> Telemetry parsed! Temp: 25.${packetCounter % 9}°C | Status: NORMAL.`);
      if (typeof TechAudio !== 'undefined') TechAudio.play('modal');
    }, 1450);

    setTimeout(() => {
      if (nodeEls[3]) nodeEls[3].classList.remove('node-transmitting');
      packet.classList.remove('flying');
      isTransmitting = false;
      txBtn.disabled = false;
    }, 1850);
  });
})();

