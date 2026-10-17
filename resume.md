---
layout: page
title: "Resume"
permalink: /resume/
class: resume-page
---

{% include profile-contact.html %}

<div class="resume-intro">
  <p>Electrical Engineering dual-degree student at IIT Bombay, focused on digital design, embedded systems, FPGA acceleration, and applied AI.</p>
  <a class="resume-download" href="{{ '/assets/files/resume_core.pdf' | relative_url }}" target="_blank" rel="noopener">Download PDF</a>
</div>

## Education

<div class="resume-entry">
  <h3>IIT Bombay <span>2024–2029</span></h3>
  <p class="subtitle">Dual Degree (B.Tech. + M.Tech.) in Electrical Engineering · CPI 9.24</p>
  <p><strong>Minor:</strong> Artificial Intelligence and Data Science, C-MInDS. Earned a 9.42 SPI in the fourth semester and AA/AB grades in 11 of 14 core courses during second year.</p>
</div>

## Experience

<div class="resume-entry">
  <h3>Digital Design Trainee · Cadence Design Systems <span>May–July 2026</span></h3>
  <ul>
    <li><strong>Static timing analysis:</strong> Evaluated setup/hold violations, on-chip variations, path pessimism, transition rates, and load capacitances using Cadence Tempus.</li>
    <li><strong>Chip optimization:</strong> Explored propagation delay and interconnect/cell delay models, including NLDM and CSM.</li>
    <li><strong>AI tooling:</strong> Built a Python MCP client-server application to automate chip-design constraint validation with TimeVision.</li>
  </ul>
</div>

<div class="resume-entry">
  <h3>AI Intern · Shorthills AI <span>May–July 2025</span></h3>
  <ul>
    <li><strong>Sales automation:</strong> Built an MCP- and LLM-agent pipeline that reduced lead response time from days to under 30 seconds.</li>
    <li><strong>Pipeline architecture:</strong> Led design and implementation using Python, Apache NiFi, APIs, and integrated tools for low-latency execution.</li>
    <li><strong>Personalized engagement:</strong> Added interaction workflows to improve lead communication at scale.</li>
  </ul>
</div>

<div class="resume-entry">
  <h3>Electrical Subsystem · IIT Bombay Racing <span>Jan 2025–Apr 2026</span></h3>
  <ul>
    <li><strong>Battery state estimation:</strong> Developed an Embedded C extended Kalman filter to estimate state-of-charge for a 2RC cell model.</li>
    <li><strong>Battery monitoring:</strong> Implemented circular daisy-chain monitoring for 96 cells.</li>
    <li><strong>System integration:</strong> Worked with ISO-SPI, SPI, and CAN as part of a 100+ member team building an electric race car for Formula Student competitions.</li>
  </ul>
</div>

## Selected Projects

<div class="resume-entry">
  <h3>Real-Time Sobel Edge Detection Accelerator <span>May 2026–Present</span></h3>
  <p class="subtitle">Research project · Verilog · FPGA · PYNQ-Z2</p>
  <ul>
    <li><strong>Streaming image pipeline:</strong> Implementing circular line buffers for live 3×3 windows and a convolution engine for binary edge classification.</li>
    <li><strong>Verification:</strong> Validated pixel accuracy against a NumPy reference model using BMP images and a custom testbench.</li>
  </ul>
</div>

<div class="resume-entry">
  <h3>I2C Device Driver on 8051 <span>Mar–Apr 2026</span></h3>
  <p class="subtitle">Microprocessors Laboratory · C · Bare-metal firmware</p>
  <ul>
    <li><strong>Protocol driver:</strong> Wrote reusable Start, Stop, Read, Write, ACK, and NACK routines for an 8051-based PT-51 board.</li>
    <li><strong>Device integration:</strong> Connected a BMP280 pressure sensor and DS1307 RTC; decoded timestamps and streamed readings over UART.</li>
  </ul>
</div>

<div class="resume-entry">
  <h3>WashU-2 16-bit CPU <span>Mar–Apr 2026</span></h3>
  <p class="subtitle">Microprocessors course project · VHDL</p>
  <ul>
    <li><strong>CPU design:</strong> Enhanced a 17-state multi-cycle processor's fetch-decode-execute flow, instruction encoding, and ALU.</li>
    <li><strong>Verification:</strong> Implemented ADD and BRPOS control logic and authored testbenches for arithmetic and branch conditions.</li>
  </ul>
</div>

<div class="resume-entry">
  <h3>Additional digital and circuits projects</h3>
  <ul>
    <li><strong>VHDL RLE encoder/decoder:</strong> Designed an FSM and 1024-bit buffer for lossless 8×8 matrix compression; synthesized and deployed to FPGA.</li>
    <li><strong>Parallel ODE solver:</strong> Implemented Euler integration and parallel computational units in Verilog to solve Kuramoto oscillator equations on FPGA.</li>
    <li><strong>Phase-sensitive detector:</strong> Built and tested an op-amp lock-in amplifier using a CD4066 switch, phase shifter, and active low-pass filter.</li>
  </ul>
</div>

## Technical Skills

<ul>
  <li><strong>Programming and hardware:</strong> C, C++, Python, Verilog, VHDL, Tcl, 8051 and STM microcontrollers.</li>
  <li><strong>Design and analysis:</strong> Cadence Tempus, Vivado, Quartus, MATLAB, LTspice, Joules RTL Studio.</li>
  <li><strong>Relevant coursework:</strong> Digital Systems, Microprocessors, Analog Circuits, Signal Processing, Control Systems, Linear Algebra, Probability, and Programming for Data Science.</li>
</ul>

## Leadership and Activities

<ul>
  <li><strong>Career Guidance Cell:</strong> Served as Vice Captain at Shiv Nadar School, coordinating 20+ college and career fairs for 500+ students.</li>
  <li><strong>Basketball:</strong> IIT Bombay Freshiesta bronze medalist; fourth place in the IIT Bombay Basketball General Championship; selected for the Inter-IIT Pre-Camp top 20.</li>
  <li><strong>Winter in Data Science:</strong> Explored multi-agent reinforcement learning for geopolitical disruptions in global supply chains.</li>
  <li><strong>Swiss Innovation Camp:</strong> Represented school in Geneva and attended STEM workshops at CERN and other research centers.</li>
</ul>
