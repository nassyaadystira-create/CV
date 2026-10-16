import sys

with open('script.js', 'r', encoding='utf-8') as f:
    content = f.read()

bad_string = "const contactForm = document.getElementById('contactForm');"
idx = content.rfind(bad_string)

if idx != -1:
    good_content = content[:idx] + '''const contactForm = document.getElementById('contactForm');
if (contactForm) {
  contactForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const name = document.getElementById('cName').value;
    const email = document.getElementById('cEmail').value;
    const msg = document.getElementById('cMessage').value;
    
    const subject = encodeURIComponent("Let's Connect - Portfolio Inquiry from " + name);
    const body = encodeURIComponent("Hi Nassya,\\n\\nMy name is " + name + " (" + email + ").\\n\\n" + msg + "\\n\\nBest regards,\\n" + name);
    
    window.location.href = "mailto:nassyaadystira@gmail.com?subject=" + subject + "&body=" + body;
  });
}
'''
    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(good_content)
    print("Fixed script.js")
else:
    print("Not found")

