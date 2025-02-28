let scene, camera, renderer, controls, jersey;

function init() {
    scene = new THREE.Scene();
    camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(document.getElementById('canvas-container').clientWidth, document.getElementById('canvas-container').clientHeight);
    document.getElementById('canvas-container').appendChild(renderer.domElement);

    controls = new THREE.OrbitControls(camera, renderer.domElement);

    const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
    scene.add(ambientLight);

    const pointLight = new THREE.PointLight(0xffffff, 1);
    pointLight.position.set(5, 5, 5);
    scene.add(pointLight);

    camera.position.z = 5;

    createJersey('tshirt');

    animate();
}

// ... (rest of the functions remain the same)

window.addEventListener('resize', function() {
    camera.aspect = document.getElementById('canvas-container').clientWidth / document.getElementById('canvas-container').clientHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(document.getElementById('canvas-container').clientWidth, document.getElementById('canvas-container').clientHeight);
});

document.addEventListener('DOMContentLoaded', function() {
    init();

    document.getElementById('jerseyType').addEventListener('change', function(e) {
        createJersey(e.target.value);
    });

    document.getElementById('jerseyColor').addEventListener('input', function(e) {
        updateJerseyColor(e.target.value);
    });

    document.getElementById('playerName').addEventListener('input', function(e) {
        updatePlayerName(e.target.value);
    });

    document.getElementById('playerNumber').addEventListener('input', function(e) {
        updatePlayerNumber(e.target.value);
    });

    document.getElementById('downloadBtn').addEventListener('click', function() {
        const dataURL = renderer.domElement.toDataURL('image/png');
        const link = document.createElement('a');
        link.download = 'custom_jersey.png';
        link.href = dataURL;
        link.click();
    });
});