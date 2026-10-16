import sys
import re

def update_html():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add Project Modal HTML before closing body
    modal_html = '''
  <!-- Project Detail Modal -->
  <div id="projectModal" class="project-modal">
    <div class="project-modal-content glass-card">
      <button class="project-modal-close" aria-label="Close">&times;</button>
      <div class="project-modal-layout">
        <div class="project-modal-image">
          <img id="pm-image" src="" alt="Project Image" onerror="this.style.display='none'; document.getElementById('pm-placeholder').style.display='flex';" />
          <div id="pm-placeholder" class="pm-placeholder">
            <span id="pm-icon">🚀</span>
          </div>
        </div>
        <div class="project-modal-info">
          <div class="pm-badge-wrap">
            <span id="pm-year" class="project-badge"></span>
            <span id="pm-role" class="project-role"></span>
          </div>
          <h3 id="pm-title">Project Title</h3>
          <div id="pm-tags" class="project-tags"></div>
          
          <div class="pm-section">
            <h4>Overview</h4>
            <p id="pm-desc">Project overview goes here.</p>
          </div>
          
          <div class="pm-section">
            <h4>Key Features / Impact</h4>
            <ul id="pm-features" class="pm-features-list"></ul>
          </div>
        </div>
      </div>
    </div>
  </div>
'''
    if '<!-- Project Detail Modal -->' not in content:
        content = content.replace('</body>', modal_html + '\n</body>')

    # 2. Rewrite Projects Section to use compact cards + data attributes
    start_tag = '<!-- TAB: Projects -->'
    end_tag = '<!-- TAB: Gallery (Dokumentasi) -->'
    start_idx = content.find(start_tag)
    end_idx = content.find(end_tag)

    if start_idx != -1 and end_idx != -1:
        new_projects = '''<!-- TAB: Projects -->
      <div class="tab-content active" id="tab-projects">
        <div class="projects-grid compact-grid">
          <!-- Project 1 -->
          <div class="project-card compact-card animate-slide-up" data-title="Real-Time Friday Prayer Congregation Counter" data-year="2026 – Ongoing" data-role="Lead Developer" data-icon="📷" data-tags="Python,YOLOv8,Computer Vision,Webcam" data-desc="A real-time system to count Friday prayer attendees utilizing a webcam feed and the YOLOv8 object detection algorithm for accurate crowd analysis." data-features="Developed real-time video processing pipeline|Integrated YOLOv8 for accurate human detection|Designed for deployment in mosque environments">
            <div class="compact-card-icon">📷</div>
            <div class="compact-card-info">
              <h3>Real-Time Friday Prayer Counter</h3>
              <p>YOLOv8 based crowd analysis system.</p>
              <button class="btn-view-details">View Details</button>
            </div>
          </div>

          <!-- Project 2 -->
          <div class="project-card compact-card animate-slide-up" data-title="WASMAN Attendance System" data-year="2026" data-role="Data Automation" data-icon="📊" data-tags="Spreadsheet,Automation,Data Management" data-desc="A spreadsheet-based attendance management system with automated formulas and filters to process monthly records and generate squad-based reports efficiently." data-features="Automated monthly attendance calculation|Squad-based filtering and reporting|Eliminated manual data entry errors">
            <div class="compact-card-icon">📊</div>
            <div class="compact-card-info">
              <h3>WASMAN Attendance System</h3>
              <p>Automated spreadsheet data management.</p>
              <button class="btn-view-details">View Details</button>
            </div>
          </div>

          <!-- Project 3 -->
          <div class="project-card compact-card animate-slide-up" data-title="Bidirectional PCM Simulation" data-year="2026" data-role="Simulation Engineer" data-icon="🔊" data-tags="MATLAB,Signal Processing,PCM" data-desc="A comprehensive bidirectional PCM communication simulation covering accurate signal transmission, encoding, and reception using MATLAB." data-features="Simulated end-to-end PCM communication|Implemented signal encoding and decoding|Visualized waveforms at each stage">
            <div class="compact-card-icon">🔊</div>
            <div class="compact-card-info">
              <h3>Bidirectional PCM Simulation</h3>
              <p>MATLAB-based communication simulation.</p>
              <button class="btn-view-details">View Details</button>
            </div>
          </div>

          <!-- Project 4 -->
          <div class="project-card compact-card animate-slide-up" data-title="Microstrip Antenna Design" data-year="2025" data-role="RF Designer" data-icon="📡" data-tags="CST Studio Suite,RF,Antenna" data-desc="Simulated a 2.4 GHz microstrip antenna and thoroughly analyzed VSWR, return loss, and gain parameters for optimal RF applications." data-features="Designed for 2.4 GHz ISM band|Optimized dimensions for high gain|Analyzed VSWR and Return Loss">
            <div class="compact-card-icon">📡</div>
            <div class="compact-card-info">
              <h3>Microstrip Antenna Design</h3>
              <p>2.4 GHz antenna simulation in CST.</p>
              <button class="btn-view-details">View Details</button>
            </div>
          </div>

          <!-- Project 5 -->
          <div class="project-card compact-card animate-slide-up" data-title="BTS Site Design & Bad Spot Analysis" data-year="2025" data-role="Field Analyst" data-icon="📶" data-tags="AutoCAD,CellMapper,G-NetTrack" data-desc="Conducted field measurements using G-NetTrack Lite and CellMapper to analyze weak signal areas and propose new BTS locations mapped in AutoCAD." data-features="Field data collection with G-NetTrack|Identified signal bad spots|Proposed new BTS topology in AutoCAD">
            <div class="compact-card-icon">📶</div>
            <div class="compact-card-info">
              <h3>BTS Site Design Analysis</h3>
              <p>Network optimization and mapping.</p>
              <button class="btn-view-details">View Details</button>
            </div>
          </div>

          <!-- Project 6 -->
          <div class="project-card compact-card animate-slide-up" data-title="FTTH Network Simulation" data-year="2025" data-role="Network Modeler" data-icon="🌐" data-tags="OptiSystem,Fiber Optic,FTTH" data-desc="Modeled an end-to-end FTTH network architecture from Telkom Pekanbaru to a local residential area utilizing OptiSystem." data-features="Designed FTTH topology|Calculated optical power budget|Analyzed BER and Q-Factor">
            <div class="compact-card-icon">🌐</div>
            <div class="compact-card-info">
              <h3>FTTH Network Simulation</h3>
              <p>Fiber optic network modeling in OptiSystem.</p>
              <button class="btn-view-details">View Details</button>
            </div>
          </div>

          <!-- Project 7 -->
          <div class="project-card compact-card animate-slide-up" data-title="IoT-Based Automatic Clothesline System" data-year="2024" data-role="Hardware Developer" data-icon="🌦️" data-tags="ESP32,IoT,Sensors" data-desc="Designed an IoT clothes-drying system using rain, temperature, and LDR sensors with real-time web monitoring via ESP32." data-features="Integrated multiple environmental sensors|Automated motorized clothesline retraction|Real-time data visualization via web dashboard">
            <div class="compact-card-icon">🌦️</div>
            <div class="compact-card-info">
              <h3>IoT Automatic Clothesline</h3>
              <p>Sensor-driven automated retraction system.</p>
              <button class="btn-view-details">View Details</button>
            </div>
          </div>

          <!-- Project 8 -->
          <div class="project-card compact-card animate-slide-up" data-title="Line Follower Robot" data-year="2024" data-role="Robotics Builder" data-icon="🤖" data-tags="Robotics,Infrared,Microcontroller" data-desc="Designed an autonomous robot using infrared sensors and microcontroller-based motion control." data-features="PID control for smooth line tracking|Custom PCB design|Fast response IR sensor array">
            <div class="compact-card-icon">🤖</div>
            <div class="compact-card-info">
              <h3>Line Follower Robot</h3>
              <p>Autonomous IR-guided robotics.</p>
              <button class="btn-view-details">View Details</button>
            </div>
          </div>

          <!-- Project 9 -->
          <div class="project-card compact-card animate-slide-up" data-title="Image Denoising GUI" data-year="2024" data-role="Developer" data-icon="🖼️" data-tags="MATLAB,GUI,Image Processing" data-desc="Developed an interactive GUI for image noise reduction using spatial filtering techniques in MATLAB." data-features="Implemented various spatial filters|Interactive parameter tuning|Real-time before/after comparison">
            <div class="compact-card-icon">🖼️</div>
            <div class="compact-card-info">
              <h3>Image Denoising GUI</h3>
              <p>MATLAB-based spatial filtering tool.</p>
              <button class="btn-view-details">View Details</button>
            </div>
          </div>

          <!-- Project 10 -->
          <div class="project-card compact-card animate-slide-up" data-title="Smartphone-Controlled RC Car" data-year="2024" data-role="Hardware Developer" data-icon="🚗" data-tags="IoT,Bluetooth,Embedded Systems" data-desc="Built a mini car controlled through a smartphone app using Bluetooth wireless communication." data-features="Bluetooth serial communication|Custom Android control interface|Motor driver integration">
            <div class="compact-card-icon">🚗</div>
            <div class="compact-card-info">
              <h3>Bluetooth RC Car</h3>
              <p>Smartphone-controlled mini vehicle.</p>
              <button class="btn-view-details">View Details</button>
            </div>
          </div>

          <!-- Project 11 -->
          <div class="project-card compact-card animate-slide-up" data-title="Bus Ticket Reservation App" data-year="2024" data-role="Developer" data-icon="🎫" data-tags="Python,GUI,Application" data-desc="Created a GUI-based bus ticketing system with passenger data input and payment validation features." data-features="User-friendly desktop interface|Ticket booking and seat selection|Basic data persistence">
            <div class="compact-card-icon">🎫</div>
            <div class="compact-card-info">
              <h3>Bus Ticketing App</h3>
              <p>Python GUI desktop application.</p>
              <button class="btn-view-details">View Details</button>
            </div>
          </div>
        </div>
      </div>

      '''
        content = content[:start_idx] + new_projects + content[end_idx:]

    # 3. Add Photo Strip section before Contact
    contact_start = content.find('<!-- ===== CONTACT SECTION ===== -->')
    if contact_start != -1 and '<!-- ===== PHOTO STRIP ===== -->' not in content:
        photo_strip = '''<!-- ===== PHOTO STRIP ===== -->
  <section class="section photo-strip-section">
    <div class="container" style="margin-bottom: 20px; text-align: center;">
      <h3 class="section-title animate-slide-up" style="font-size: 1.8rem;">Capturing <span class="gradient-text">Moments</span></h3>
    </div>
    <div class="coverflow-container animate-fade-in">
      <div class="coverflow-track">
        <!-- We use the gallery images for this visual transition -->
        <div class="coverflow-item"><img src="WhatsApp Image 2026-10-08 at 11.04.40.jpeg" alt="Moment" loading="lazy"></div>
        <div class="coverflow-item"><img src="WhatsApp Image 2026-10-08 at 11.04.43.jpeg" alt="Moment" loading="lazy"></div>
        <div class="coverflow-item"><img src="WhatsApp Image 2026-10-08 at 11.04.57 (2).jpeg" alt="Moment" loading="lazy"></div>
        <div class="coverflow-item"><img src="WhatsApp Image 2026-10-08 at 11.05.08.jpeg" alt="Moment" loading="lazy"></div>
        <div class="coverflow-item"><img src="WhatsApp Image 2026-10-08 at 11.05.11 (3).jpeg" alt="Moment" loading="lazy"></div>
      </div>
    </div>
  </section>

  '''
        content = content[:contact_start] + photo_strip + content[contact_start:]

    # 4. Rewrite Contact Section to match the screenshot form
    contact_tag = '<!-- ===== CONTACT SECTION ===== -->'
    footer_tag = '<!-- FOOTER -->'
    c_start = content.find(contact_tag)
    f_start = content.find(footer_tag)
    if c_start != -1 and f_start != -1:
        new_contact = '''<!-- ===== CONTACT SECTION ===== -->
  <section class="section" id="contact">
    <div class="container contact-container">
      <div class="contact-layout animate-slide-up">
        
        <!-- Left: Form -->
        <div class="contact-form-side glass-card">
          <h2 class="contact-form-title">Hubungi</h2>
          <p class="contact-form-desc">Ada yang mau didiskusikan? Langsung kirim pesan aja ya..!</p>
          
          <form id="contactForm" class="contact-form">
            <div class="input-group">
              <span class="input-icon">👤</span>
              <input type="text" id="cName" placeholder="Nama Anda" required />
            </div>
            <div class="input-group">
              <span class="input-icon">✉️</span>
              <input type="email" id="cEmail" placeholder="Email Anda" required />
            </div>
            <div class="input-group align-top">
              <span class="input-icon" style="margin-top: 14px;">💬</span>
              <textarea id="cMessage" rows="5" placeholder="Pesan Anda" required></textarea>
            </div>
            <button type="submit" class="btn-submit">
              <span class="btn-icon">✈️</span> Kirim Pesan
            </button>
          </form>
        </div>

        <!-- Right: Find Me -->
        <div class="contact-info-side">
          <h3 class="find-me-title">FIND ME</h3>
          <div class="social-cards">
            <a href="mailto:nassyaadystira@gmail.com" class="social-card glass-card">
              <div class="sc-icon" style="background:#ea4335;">✉️</div>
              <div class="sc-text">
                <h4>Email</h4>
                <p>nassyaadystira@gmail.com</p>
              </div>
            </a>
            <a href="https://www.linkedin.com/in/nassya-adystira-09b844319/" target="_blank" class="social-card glass-card">
              <div class="sc-icon" style="background:#0a66c2;">in</div>
              <div class="sc-text">
                <h4>Let's Connect</h4>
                <p>on LinkedIn</p>
              </div>
            </a>
            <a href="https://www.instagram.com/nassyaadystira" target="_blank" class="social-card glass-card">
              <div class="sc-icon" style="background:linear-gradient(45deg, #f09433, #e6683c, #dc2743, #cc2366, #bc1888);">📸</div>
              <div class="sc-text">
                <h4>Instagram</h4>
                <p>@nassyaadystira</p>
              </div>
            </a>
          </div>
        </div>

      </div>
    </div>
  </section>

  '''
        content = content[:c_start] + new_contact + content[f_start:]
        
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

update_html()
