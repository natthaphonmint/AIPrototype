particlesJS("particles-js", {
  "particles": {
    "number": { "value": 150, "density": { "enable": true, "value_area": 800 } },
    "color": { "value": "#ffc0cb" }, /* สีชมพูอ่อน */
    "shape": {
      "type": "circle", /* เป็นวงกลมเล็กๆ เหมือนกลีบดอกไม้ */
    },
    "opacity": {
      "value": 0.8,
      "random": true,
      "anim": { "enable": true, "speed": 1, "opacity_min": 0.3, "sync": false }
    },
    "size": {
      "value": 6,
      "random": true, /* ขนาดไม่เท่ากัน ให้ดูธรรมชาติ */
      "anim": { "enable": false }
    },
    "line_linked": { "enable": false }, /* ไม่มีเส้นเชื่อม */
    "move": {
      "enable": true,
      "speed": 3,
      "direction": "bottom-right", /* ร่วงเฉียงๆ เหมือนลมพัดมาจากภูเขา */
      "random": true,
      "straight": false,
      "out_mode": "out",
      "bounce": false,
    }
  },
  "interactivity": {
    "detect_on": "canvas",
    "events": { "onhover": { "enable": true, "mode": "repulse" }, "onclick": { "enable": true, "mode": "push" } },
    "modes": { "repulse": { "distance": 100, "duration": 0.4 } }
  },
  "retina_detect": true
});