import sys

def update_html():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    start_tag = '<!-- TAB: Projects -->'
    end_tag = '<!-- TAB: Gallery (Dokumentasi) -->'

    start_idx = content.find(start_tag)
    end_idx = content.find(end_tag)

    if start_idx != -1 and end_idx != -1:
        new_projects = '''<!-- TAB: Projects -->
      <div class="tab-content active" id="tab-projects">
        <div class="projects-grid">

          <div class="project-card animate-on-scroll">
            <div class="project-image-placeholder">📷</div>
            <div class="project-content">
              <div class="project-badge-wrap">
                <span class="project-badge">2026 – Ongoing</span>
                <span class="project-role">Lead Developer</span>
              </div>
              <h3>Real-Time Friday Prayer Congregation Counter</h3>
              <p>Developing a real-time system to count Friday prayer attendees utilizing a webcam feed and the YOLOv8 object detection algorithm for accurate crowd analysis.</p>
              <div class="project-tags">
                <span>Python</span><span>YOLOv8</span><span>Computer Vision</span><span>Webcam</span>
              </div>
              <div class="project-links">
                <a href="#" class="project-link" onclick="event.preventDefault()">🔗 View Details</a>
              </div>
            </div>
          </div>

          <div class="project-card animate-on-scroll">
            <div class="project-image-placeholder">📊</div>
            <div class="project-content">
              <div class="project-badge-wrap">
                <span class="project-badge">2026</span>
                <span class="project-role">Data Automation</span>
              </div>
              <h3>WASMAN Attendance System</h3>
              <p>Developed a spreadsheet-based attendance management system with automated formulas and filters to process monthly records and generate squad-based reports efficiently.</p>
              <div class="project-tags">
                <span>Spreadsheet</span><span>Automation</span><span>Data Management</span>
              </div>
              <div class="project-links">
                <a href="#" class="project-link" onclick="event.preventDefault()">🔗 View Details</a>
              </div>
            </div>
          </div>

          <div class="project-card animate-on-scroll">
            <div class="project-image-placeholder">🔊</div>
            <div class="project-content">
              <div class="project-badge-wrap">
                <span class="project-badge">2026</span>
                <span class="project-role">Simulation Engineer</span>
              </div>
              <h3>Bidirectional PCM Simulation</h3>
              <p>Developed a comprehensive bidirectional PCM communication simulation covering accurate signal transmission, encoding, and reception using MATLAB.</p>
              <div class="project-tags">
                <span>MATLAB</span><span>Signal Processing</span><span>PCM</span>
              </div>
              <div class="project-links">
                <a href="#" class="project-link" onclick="event.preventDefault()">🔗 View Details</a>
              </div>
            </div>
          </div>

          <div class="project-card animate-on-scroll">
            <div class="project-image-placeholder">📡</div>
            <div class="project-content">
              <div class="project-badge-wrap">
                <span class="project-badge">2025</span>
                <span class="project-role">RF Designer</span>
              </div>
              <h3>Microstrip Antenna Design</h3>
              <p>Simulated a 2.4 GHz microstrip antenna and thoroughly analyzed VSWR, return loss, and gain parameters for optimal RF applications.</p>
              <div class="project-tags">
                <span>CST Studio Suite</span><span>RF</span><span>Antenna</span>
              </div>
              <div class="project-links">
                <a href="#" class="project-link" onclick="event.preventDefault()">🔗 View Details</a>
              </div>
            </div>
          </div>

          <div class="project-card animate-on-scroll">
            <div class="project-image-placeholder">📶</div>
            <div class="project-content">
              <div class="project-badge-wrap">
                <span class="project-badge">2025</span>
                <span class="project-role">Field Analyst</span>
              </div>
              <h3>BTS Site Design & Bad Spot Analysis</h3>
              <p>Conducted field measurements using G-NetTrack Lite and CellMapper to analyze weak signal areas and propose new BTS locations mapped in AutoCAD.</p>
              <div class="project-tags">
                <span>AutoCAD</span><span>CellMapper</span><span>G-NetTrack</span>
              </div>
              <div class="project-links">
                <a href="#" class="project-link" onclick="event.preventDefault()">🔗 View Details</a>
              </div>
            </div>
          </div>

          <div class="project-card animate-on-scroll">
            <div class="project-image-placeholder">🌐</div>
            <div class="project-content">
              <div class="project-badge-wrap">
                <span class="project-badge">2025</span>
                <span class="project-role">Network Modeler</span>
              </div>
              <h3>FTTH Network Simulation</h3>
              <p>Modeled an end-to-end FTTH network architecture from Telkom Pekanbaru to a local residential area utilizing OptiSystem.</p>
              <div class="project-tags">
                <span>OptiSystem</span><span>Fiber Optic</span><span>FTTH</span>
              </div>
              <div class="project-links">
                <a href="#" class="project-link" onclick="event.preventDefault()">🔗 View Details</a>
              </div>
            </div>
          </div>

          <div class="project-card animate-on-scroll">
            <div class="project-image-placeholder">🌦️</div>
            <div class="project-content">
              <div class="project-badge-wrap">
                <span class="project-badge">2024</span>
                <span class="project-role">Hardware Developer</span>
              </div>
              <h3>IoT-Based Automatic Clothesline System</h3>
              <p>Designed an IoT clothes-drying system using rain, temperature, and LDR sensors with real-time web monitoring via ESP32.</p>
              <div class="project-tags">
                <span>ESP32</span><span>IoT</span><span>Sensors</span>
              </div>
              <div class="project-links">
                <a href="#" class="project-link" onclick="event.preventDefault()">🔗 View Details</a>
              </div>
            </div>
          </div>

          <div class="project-card animate-on-scroll">
            <div class="project-image-placeholder">🤖</div>
            <div class="project-content">
              <div class="project-badge-wrap">
                <span class="project-badge">2024</span>
                <span class="project-role">Robotics Builder</span>
              </div>
              <h3>Line Follower Robot</h3>
              <p>Designed an autonomous robot using infrared sensors and microcontroller-based motion control.</p>
              <div class="project-tags">
                <span>Robotics</span><span>Infrared</span><span>Microcontroller</span>
              </div>
              <div class="project-links">
                <a href="#" class="project-link" onclick="event.preventDefault()">🔗 View Details</a>
              </div>
            </div>
          </div>

        </div>
      </div>

      '''
        content = content[:start_idx] + new_projects + content[end_idx:]
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Success")
    else:
        print("Tags not found")

update_html()
