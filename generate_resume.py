"""
Generate a professional PDF resume for Saif Ali Khan using WeasyPrint.
"""
from weasyprint import HTML

resume_html = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
    @page {
        size: A4;
        margin: 0;
    }
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    body {
        font-family: 'Helvetica Neue', Arial, sans-serif;
        color: #333;
        line-height: 1.5;
    }
    .resume {
        display: flex;
        min-height: 297mm;
    }
    .sidebar {
        width: 35%;
        background: linear-gradient(180deg, #1a1a2e 0%, #16213e 100%);
        color: #fff;
        padding: 40px 25px;
    }
    .main {
        width: 65%;
        padding: 40px 35px;
        background: #fff;
    }
    .profile-section {
        text-align: center;
        margin-bottom: 30px;
        padding-bottom: 25px;
        border-bottom: 1px solid rgba(255,255,255,0.2);
    }
    .profile-img {
        width: 120px;
        height: 120px;
        border-radius: 50%;
        border: 3px solid #6c63ff;
        margin-bottom: 15px;
        object-fit: cover;
    }
    .profile-name {
        font-size: 22px;
        font-weight: 700;
        margin-bottom: 5px;
        color: #fff;
    }
    .profile-title {
        font-size: 12px;
        color: #a8a8ff;
        letter-spacing: 1px;
        text-transform: uppercase;
    }
    .sidebar-section {
        margin-bottom: 25px;
    }
    .sidebar-section h3 {
        font-size: 13px;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        color: #6c63ff;
        margin-bottom: 12px;
        padding-bottom: 8px;
        border-bottom: 2px solid #6c63ff;
    }
    .sidebar-section p, .sidebar-section li {
        font-size: 11px;
        color: rgba(255,255,255,0.85);
        line-height: 1.7;
    }
    .sidebar-section ul {
        list-style: none;
        padding: 0;
    }
    .sidebar-section ul li {
        padding: 4px 0;
        padding-left: 15px;
        position: relative;
    }
    .sidebar-section ul li::before {
        content: "▸";
        position: absolute;
        left: 0;
        color: #6c63ff;
    }
    .contact-item {
        display: flex;
        align-items: flex-start;
        margin-bottom: 8px;
        font-size: 10px;
        color: rgba(255,255,255,0.85);
    }
    .contact-item .label {
        font-weight: 600;
        min-width: 55px;
        color: #a8a8ff;
    }
    .main h1 {
        font-size: 28px;
        color: #1a1a2e;
        margin-bottom: 5px;
    }
    .main .subtitle {
        font-size: 14px;
        color: #6c63ff;
        margin-bottom: 25px;
        font-weight: 500;
    }
    .main-section {
        margin-bottom: 22px;
    }
    .main-section h2 {
        font-size: 14px;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        color: #1a1a2e;
        margin-bottom: 12px;
        padding-bottom: 8px;
        border-bottom: 2px solid #6c63ff;
    }
    .main-section p {
        font-size: 11px;
        color: #555;
        line-height: 1.8;
    }
    .experience-item, .education-item {
        margin-bottom: 15px;
    }
    .experience-item h3, .education-item h3 {
        font-size: 13px;
        color: #1a1a2e;
        font-weight: 600;
    }
    .experience-item .company, .education-item .institution {
        font-size: 11px;
        color: #6c63ff;
        font-weight: 500;
    }
    .experience-item .date, .education-item .date {
        font-size: 10px;
        color: #999;
        margin-bottom: 5px;
    }
    .experience-item p, .education-item p {
        font-size: 11px;
        color: #555;
    }
    .skills-grid {
        display: flex;
        flex-wrap: wrap;
        gap: 6px;
    }
    .skill-tag {
        background: #f0efff;
        color: #6c63ff;
        padding: 4px 12px;
        border-radius: 15px;
        font-size: 10px;
        font-weight: 500;
    }
    .project-item {
        margin-bottom: 12px;
    }
    .project-item h3 {
        font-size: 12px;
        color: #1a1a2e;
        font-weight: 600;
    }
    .project-item p {
        font-size: 10px;
        color: #555;
    }
    .project-item .tech {
        font-size: 10px;
        color: #6c63ff;
        font-style: italic;
    }
</style>
</head>
<body>
<div class="resume">
    <div class="sidebar">
        <div class="profile-section">
            <div class="profile-name">SAIF ALI KHAN</div>
            <div class="profile-title">Software Developer</div>
        </div>

        <div class="sidebar-section">
            <h3>Contact</h3>
            <div class="contact-item">
                <span class="label">Email:</span>
                <span>sk3598547@gmail.com</span>
            </div>
            <div class="contact-item">
                <span class="label">Phone:</span>
                <span>+91 7849862005</span>
            </div>
            <div class="contact-item">
                <span class="label">Location:</span>
                <span>Sikar, Rajasthan, India</span>
            </div>
            <div class="contact-item">
                <span class="label">GitHub:</span>
                <span>github.com/saifkhandoodwa</span>
            </div>
            <div class="contact-item">
                <span class="label">LinkedIn:</span>
                <span>linkedin.com/in/saifkhandeveloper</span>
            </div>
        </div>

        <div class="sidebar-section">
            <h3>Technical Skills</h3>
            <ul>
                <li>HTML5 & CSS3</li>
                <li>JavaScript</li>
                <li>Python</li>
                <li>Kotlin</li>
                <li>C & C++</li>
                <li>Java</li>
                <li>Firebase & AWS</li>
                <li>Git & GitHub</li>
                <li>Responsive Design</li>
                <li>UI/UX Design</li>
            </ul>
        </div>

        <div class="sidebar-section">
            <h3>Areas of Interest</h3>
            <ul>
                <li>Web Development</li>
                <li>Android Development</li>
                <li>Artificial Intelligence</li>
                <li>Cybersecurity</li>
                <li>Computer Architecture</li>
                <li>Operating Systems</li>
            </ul>
        </div>

        <div class="sidebar-section">
            <h3>Languages</h3>
            <ul>
                <li>Hindi (Native)</li>
                <li>English (Professional)</li>
            </ul>
        </div>
    </div>

    <div class="main">
        <h1>SAIF ALI KHAN</h1>
        <p class="subtitle">Web Developer | Software Developer | AI Enthusiast</p>

        <div class="main-section">
            <h2>Professional Summary</h2>
            <p>
                Passionate and dedicated software developer with hands-on experience in web development,
                mobile app development, and artificial intelligence. Currently pursuing Bachelor of Computer
                Application (B.C.A.) with strong foundation in multiple programming languages and modern
                development frameworks. Committed to building innovative, user-friendly applications and
                continuously expanding technical expertise.
            </p>
        </div>

        <div class="main-section">
            <h2>Education</h2>
            <div class="education-item">
                <h3>Bachelor of Computer Application (B.C.A.)</h3>
                <div class="institution">4th Semester</div>
                <div class="date">2024 - 2027 (Expected)</div>
                <p>Studying core computer science subjects including data structures, algorithms,
                   database management, and software engineering.</p>
            </div>
        </div>

        <div class="main-section">
            <h2>Experience</h2>
            <div class="experience-item">
                <h3>AI Intern</h3>
                <div class="company">IBM</div>
                <div class="date">Artificial Intelligence Division</div>
                <p>Gained practical experience in artificial intelligence technologies,
                   machine learning concepts, and AI application development.</p>
            </div>
        </div>

        <div class="main-section">
            <h2>Projects</h2>
            <div class="project-item">
                <h3>Multiplayer Android Game</h3>
                <p>Developed a real-time multiplayer game application with online gameplay features.</p>
                <div class="tech">Kotlin, Python, Firebase, AWS, Java, XML</div>
            </div>
            <div class="project-item">
                <h3>AI Agentic Research Assistant</h3>
                <p>Built an AI-powered agent for email writing automation, developed during Kaggle participation.</p>
                <div class="tech">Python, AI/ML, NLP</div>
            </div>
            <div class="project-item">
                <h3>E-Commerce Shopping Website</h3>
                <p>Created a responsive e-commerce website with modern design and layout.</p>
                <div class="tech">HTML, CSS, Responsive Design</div>
            </div>
            <div class="project-item">
                <h3>ChatBot Testing Platform</h3>
                <p>Developed an interactive chatbot interface for testing conversational AI patterns.</p>
                <div class="tech">HTML, CSS, JavaScript</div>
            </div>
        </div>

        <div class="main-section">
            <h2>Core Competencies</h2>
            <div class="skills-grid">
                <span class="skill-tag">Problem Solving</span>
                <span class="skill-tag">Team Collaboration</span>
                <span class="skill-tag">Agile Development</span>
                <span class="skill-tag">Version Control</span>
                <span class="skill-tag">API Integration</span>
                <span class="skill-tag">Database Design</span>
                <span class="skill-tag">Mobile Development</span>
                <span class="skill-tag">Cloud Services</span>
            </div>
        </div>
    </div>
</div>
</body>
</html>
"""

if __name__ == "__main__":
    output_path = "/projects/sandbox/My-Profile/Resume.pdf"
    html = HTML(string=resume_html)
    html.write_pdf(output_path)
    print(f"Resume PDF generated successfully: {output_path}")
