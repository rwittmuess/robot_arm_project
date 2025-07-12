/*****************************************************************
 * Rainbow sliders + joint dots + click‑lock while animating
 *****************************************************************/

// joint colours
const colours = ['red','orange','gold','green','dodgerblue','purple'];

const slidersDiv = document.getElementById('sliders');
const moveBtn    = document.getElementById('moveBtn');
const sliders    = [];
const linkLen    = 35;               // pixels per link
let animId       = null;
let animating    = false;            // prevents double‑click jump

/* ---------- build sliders ---------- */
for (let i = 0; i < 6; i++) {
  const row = document.createElement('div');

  const label = document.createElement('label');
  label.textContent = `Joint ${i+1}:`;

  const minCap = document.createElement('span');
  minCap.className = 'limit';
  minCap.textContent = '-180';

  const slider = document.createElement('input');
  slider.type  = 'range';
  slider.min   = -180;
  slider.max   =  180;
  slider.value = 0;
  slider.step  = 1;
  slider.style.accentColor = colours[i];
  sliders.push(slider);

  const maxCap = document.createElement('span');
  maxCap.className = 'limit';
  maxCap.textContent = '180';

  row.append(label,minCap,slider,maxCap);
  slidersDiv.appendChild(row);
}

/* ---------- send angles ---------- */
async function sendAngles(){
  if (animating) return;             // ignore double‑click
  animating = true;
  moveBtn.disabled = true;

  const angles = sliders.map(s => parseInt(s.value,10));

  const res  = await fetch('http://localhost:8000/api/move',{
    method:'POST',
    headers:{'Content-Type':'application/json'},
    body:JSON.stringify({target_angles:angles,speed:95})
  });
  const {frames,step_time} = await res.json();

  if (animId) clearInterval(animId);
  let i = 0;
  animId = setInterval(()=>{
    drawArm(frames[i]);
    if (++i >= frames.length){
      clearInterval(animId);
      animating = false;
      moveBtn.disabled = false;      // re‑enable button
    }
  }, step_time * 1500);
}

/* ---------- draw arm with dots ---------- */
function drawArm(angles) {
  const canvas = document.getElementById('robotCanvas');
  const ctx    = canvas.getContext('2d');
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  let x = canvas.width / 2;
  let y = canvas.height / 2;
  let acc = 0;
  const linkLen = 30;

  /* fixed support — little gray triangle */
  ctx.beginPath();
  ctx.moveTo(x - 15, y + 15);   // left base
  ctx.lineTo(x + 15, y + 15);   // right base
  ctx.lineTo(x,       y);       // tip at joint
  ctx.closePath();
  ctx.fillStyle = '#999';
  ctx.fill();

  /* links and joint dots (no dot at last tip) */
  angles.forEach((deg, idx) => {
    // dot at joint connecting to previous link (skip base)
    if (idx >= 0) {
      ctx.beginPath();
      ctx.arc(x, y, 6, 0, 2 * Math.PI);
      ctx.fillStyle = colours[idx];
      ctx.fill();
    }

    // draw link
    ctx.beginPath();
    ctx.moveTo(x, y);
    acc += deg * Math.PI / 180;
    const nx = x + linkLen * Math.cos(acc);
    const ny = y + linkLen * Math.sin(acc);
    ctx.lineTo(nx, ny);
    ctx.strokeStyle = colours[idx];
    ctx.lineWidth = 3;
    ctx.stroke();

    x = nx; y = ny; // advance head
  });
}

// draw initial pose
drawArm(new Array(6).fill(0));
