import sys

def append_css():
    css_content = '''
/* ===== NEW ANIMATIONS ===== */
.animate-slide-up {
  opacity: 0;
  transform: translateY(40px);
  transition: opacity 0.8s cubic-bezier(0.16, 1, 0.3, 1), transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
}
.animate-slide-up.visible { opacity: 1; transform: translateY(0); }

.animate-fade-in {
  opacity: 0;
  transition: opacity 1s ease;
}
.animate-fade-in.visible { opacity: 1; }

/* ===== COMPACT PROJECT CARDS ===== */
.compact-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 24px;
}
.compact-card {
  padding: 24px;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 16px;
  background: rgba(10,15,36,0.6);
  border: 1px solid rgba(96,165,250,0.15);
  border-radius: 16px;
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  cursor: pointer;
}
.compact-card:hover {
  transform: translateY(-5px) scale(1.02);
  border-color: rgba(96,165,250,0.4);
  box-shadow: 0 16px 40px rgba(59,130,246,0.15);
  background: rgba(15,25,50,0.8);
}
.compact-card-icon {
  width: 60px;
  height: 60px;
  flex-shrink: 0;
  background: linear-gradient(135deg, rgba(59,130,246,0.15), rgba(6,182,212,0.1));
  border-radius: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.8rem;
  border: 1px solid rgba(96,165,250,0.2);
}
.compact-card-info h3 {
  font-family: 'Space Grotesk', sans-serif;
  font-size: 1.05rem;
  font-weight: 700;
  color: #fff;
  margin-bottom: 6px;
  line-height: 1.3;
}
.compact-card-info p {
  color: var(--text-muted);
  font-size: 0.8rem;
  margin-bottom: 12px;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.btn-view-details {
  background: transparent;
  border: none;
  color: var(--primary-light);
  font-size: 0.8rem;
  font-weight: 700;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 4px;
  padding: 0;
  transition: color 0.3s;
}
.btn-view-details::after {
  content: '→';
  transition: transform 0.3s;
}
.compact-card:hover .btn-view-details { color: var(--accent); }
.compact-card:hover .btn-view-details::after { transform: translateX(4px); }

/* ===== PROJECT MODAL ===== */
.project-modal {
  display: none;
  position: fixed;
  z-index: 9999;
  inset: 0;
  background: rgba(5,5,16,0.85);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  padding: 20px;
  overflow-y: auto;
  align-items: center;
  justify-content: center;
}
.project-modal.active { display: flex; animation: modalFadeIn 0.4s ease; }
@keyframes modalFadeIn { from { opacity: 0; } to { opacity: 1; } }

.project-modal-content {
  background: var(--bg2);
  width: 100%;
  max-width: 850px;
  border-radius: 24px;
  position: relative;
  overflow: hidden;
  box-shadow: 0 30px 80px rgba(0,0,0,0.6);
  border: 1px solid rgba(96,165,250,0.2);
  transform: scale(0.95);
  opacity: 0;
  animation: modalPopUp 0.5s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
@keyframes modalPopUp { to { transform: scale(1); opacity: 1; } }

.project-modal-close {
  position: absolute;
  top: 20px;
  right: 24px;
  background: rgba(255,255,255,0.1);
  border: none;
  color: #fff;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  font-size: 1.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  z-index: 10;
  transition: background 0.3s, transform 0.3s;
}
.project-modal-close:hover { background: #ef4444; transform: rotate(90deg); }

.project-modal-layout {
  display: grid;
  grid-template-columns: 1fr;
  max-height: 85vh;
  overflow-y: auto;
}
@media (min-width: 768px) {
  .project-modal-layout { grid-template-columns: 350px 1fr; }
}
.project-modal-image {
  background: rgba(10,15,36,0.5);
  position: relative;
  min-height: 250px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-right: 1px solid rgba(96,165,250,0.1);
}
.project-modal-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  position: absolute;
  inset: 0;
}
.pm-placeholder {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, rgba(59,130,246,0.1), rgba(6,182,212,0.05));
}
.pm-placeholder span { font-size: 4rem; opacity: 0.8; }

.project-modal-info { padding: 40px 32px; }
.pm-badge-wrap { display: flex; gap: 12px; align-items: center; margin-bottom: 16px; }
.project-modal-info h3 {
  font-family: 'Space Grotesk', sans-serif;
  font-size: 1.8rem;
  font-weight: 800;
  margin-bottom: 20px;
  color: #fff;
}
.pm-section { margin-top: 32px; }
.pm-section h4 { font-size: 1rem; color: var(--text); margin-bottom: 12px; font-weight: 700; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 8px;}
.pm-section p, .pm-features-list li { color: var(--text-muted); font-size: 0.9rem; line-height: 1.7; }
.pm-features-list { padding-left: 20px; }
.pm-features-list li { margin-bottom: 8px; }

/* ===== PHOTO STRIP (COVER FLOW) ===== */
.photo-strip-section { padding: 60px 0; overflow: hidden; background: linear-gradient(to bottom, transparent, rgba(59,130,246,0.03), transparent); }
.coverflow-container {
  width: 100%;
  padding: 40px 0;
  display: flex;
  justify-content: center;
  perspective: 1000px;
}
.coverflow-track {
  display: flex;
  gap: 20px;
  align-items: center;
  width: max-content;
  animation: scrollMarquee 25s linear infinite;
}
.coverflow-container:hover .coverflow-track { animation-play-state: paused; }
@keyframes scrollMarquee {
  0% { transform: translateX(10%); }
  100% { transform: translateX(-50%); }
}
.coverflow-item {
  width: 280px;
  height: 200px;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 20px 40px rgba(0,0,0,0.5);
  border: 1px solid rgba(255,255,255,0.1);
  transition: transform 0.4s ease, filter 0.4s ease;
  filter: grayscale(40%) brightness(0.8);
}
.coverflow-item:hover {
  transform: scale(1.1) translateY(-10px);
  filter: grayscale(0%) brightness(1.1);
  z-index: 2;
  box-shadow: 0 30px 60px rgba(59,130,246,0.3);
}
.coverflow-item img { width: 100%; height: 100%; object-fit: cover; }

/* ===== CONTACT SECTION REDESIGN ===== */
.contact-container { max-width: 1000px; }
.contact-layout {
  display: grid;
  grid-template-columns: 1.2fr 1fr;
  gap: 40px;
  background: #101423; /* Dark bluish */
  border-radius: 24px;
  padding: 40px;
  box-shadow: 0 24px 60px rgba(0,0,0,0.4);
  border: 1px solid rgba(255,255,255,0.05);
}
@media (max-width: 800px) {
  .contact-layout { grid-template-columns: 1fr; padding: 24px; }
}

.contact-form-side {
  background: transparent;
  border: none;
  box-shadow: none;
  padding: 0;
}
.contact-form-title { font-family: 'Space Grotesk', sans-serif; font-size: 2rem; color: #3b82f6; margin-bottom: 8px; font-weight: 800; }
.contact-form-desc { color: #94a3b8; font-size: 0.9rem; margin-bottom: 32px; }

.contact-form { display: flex; flex-direction: column; gap: 16px; }
.input-group {
  position: relative;
  display: flex;
  align-items: center;
  background: #1e243b;
  border: 1px solid #2d3748;
  border-radius: 12px;
  overflow: hidden;
  transition: border-color 0.3s;
}
.input-group.align-top { align-items: flex-start; }
.input-group:focus-within { border-color: #3b82f6; }
.input-icon { padding: 14px 16px; color: #94a3b8; font-size: 1.1rem; }
.contact-form input, .contact-form textarea {
  width: 100%;
  background: transparent;
  border: none;
  padding: 14px 16px 14px 0;
  color: #fff;
  font-family: 'Inter', sans-serif;
  font-size: 0.95rem;
  outline: none;
}
.contact-form textarea { resize: vertical; }

.btn-submit {
  background: #3b82f6;
  color: white;
  border: none;
  padding: 16px;
  border-radius: 12px;
  font-weight: 700;
  font-size: 1rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  transition: background 0.3s, transform 0.2s;
  margin-top: 8px;
}
.btn-submit:hover { background: #2563eb; transform: translateY(-2px); }

.find-me-title { font-size: 0.85rem; color: #fff; letter-spacing: 0.1em; margin-bottom: 20px; font-weight: 800; text-transform: uppercase; border-top: 1px solid #2d3748; padding-top: 32px; }
.social-cards { display: flex; flex-direction: column; gap: 12px; }
.social-card {
  display: flex;
  align-items: center;
  gap: 16px;
  background: #1e243b;
  border: 1px solid #2d3748;
  padding: 12px 16px;
  border-radius: 12px;
  text-decoration: none;
  transition: transform 0.3s, border-color 0.3s;
}
.social-card:hover { transform: translateX(8px); border-color: #3b82f6; }
.sc-icon {
  width: 36px;
  height: 36px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 1.2rem;
  font-weight: 800;
  flex-shrink: 0;
}
.sc-text h4 { color: #fff; font-size: 0.9rem; font-weight: 700; }
.sc-text p { color: #94a3b8; font-size: 0.75rem; }
'''
    with open('style.css', 'a', encoding='utf-8') as f:
        f.write(css_content)
    print("CSS updated.")

def update_js():
    js_content = '''
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
    const tags = card.dataset.tags.split(',');
    tags.forEach(tag => {
      const span = document.createElement('span');
      span.textContent = tag.trim();
      pmTags.appendChild(span);
    });

    // Process features
    pmFeatures.innerHTML = '';
    const features = card.dataset.features.split('|');
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
const contactForm = document.getElementById('contactForm');
if (contactForm) {
  contactForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const name = document.getElementById('cName').value;
    const email = document.getElementById('cEmail').value;
    const msg = document.getElementById('cMessage').value;
    
    const subject = encodeURIComponent(Let's Connect - Portfolio Inquiry from );
    const body = encodeURIComponent(Hi Nassya,\n\nMy name is  ().\n\n\n\nBest regards,\n);
    
    window.location.href = mailto:nassyaadystira@gmail.com?subject=&body=;
  });
}
'''
    with open('script.js', 'a', encoding='utf-8') as f:
        f.write(js_content)
    print("JS updated.")

append_css()
update_js()
