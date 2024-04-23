/**
 * Javascript used for index.html -> <script src="{% static 'home/index.js' %}"></script>
 * Primarily used for matrix effect and other smaller functions
 */

function HelloYou() {
    alert("Hello World!!!!11!11!");
}

let canvas = document.querySelector("canvas");

let ctx = canvas.getContext("2d");
let width = canvas.width = window.innerWidth;
let height = canvas.height = window.innerHeight;
let str = "A+jk js:2 @dfs 17 tr YY ufds M5r P87 #18 $!& ^dfs $Ew er JH # $ * . (! ;) ,: :";
let matrix = str.split("");
let font = 12;
let col = width / font;
let arr = [];

const grad = ctx.createLinearGradient(0, 0, 280, 0);
grad.addColorStop(0, '#A239CA');
grad.addColorStop(0, '#4717F6');

for(let i = 0; i < col; i++) {
    arr[i] = 1;
}

const draw = () => {
    ctx.fillStyle = "rgba(34,34,34,0.05)";
    ctx.fillRect(0, 0, width, height);
    ctx.fillStyle = grad;
    ctx.font = `${font}px system-ui`;

    for(let i = 0; i < arr.length; i++) {
        let txt = matrix[Math.floor(Math.random() * matrix.length)];
        ctx.fillText(txt, i * font, arr[i] * font);

        if(arr[i] * font > height && Math.random() > 0.975) {
            arr[i] = 0;
        }
        arr[i]++;
    }
}

setInterval(draw, 20);

window.addEventListener("resize", () => location.reload());
