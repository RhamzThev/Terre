<script setup>
import { ref, onMounted, watch } from 'vue';
import { Scene, PerspectiveCamera, WebGLRenderer, TextureLoader, EquirectangularReflectionMapping, Vector3, PointLight, SphereGeometry, ShaderMaterial, GLSL3, Mesh, MeshStandardMaterial, AdditiveBlending, Group, MeshBasicMaterial, Raycaster, Vector2, Object3D } from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { CSS2DRenderer, CSS2DObject } from 'three/addons/renderers/CSS2DRenderer.js';

/***
 * HEY RHAMSEZ, THIS IS YOUR REMINDER
 * X = left and right
 * Y = up and down
 * Z = forward and back
 */

const earth = ref();

const radians = (degrees) => degrees * (Math.PI / 180)

const raycaster = new Raycaster();
const pointer = new Vector2();

// declarations
const scene = new Scene();

const camera = new PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1);
camera.position.setZ(30);

const renderer = new WebGLRenderer();
renderer.setPixelRatio(window.devicePixelRatio);
renderer.setSize(window.innerWidth, window.innerHeight);

// texture loader
const loader = new TextureLoader();

//#region Not Earth
// galaxy
const milkyWay = loader.load("/milky_way.jpg");
milkyWay.mapping = EquirectangularReflectionMapping;

scene.background = milkyWay

// sun
const ADJACENT_LENGTH = 60
const OPPOSITE_LENGTH = ADJACENT_LENGTH * Math.tan(0.4101524)
const SUN_POSITION = new Vector3(0, OPPOSITE_LENGTH, ADJACENT_LENGTH);

const sunLight = new PointLight(0xffffff, 1000);
sunLight.position.copy(SUN_POSITION);

scene.add(sunLight);
//#endregion

//#region Earth
const earthGroup = new Group();

const RADIUS = 15

const earthGeometry = new SphereGeometry(RADIUS, 64, 32);

// globe
const eartDayhMap = loader.load('/earth_day.jpg');
const earthNightMap = loader.load("/earth_night.jpg");

const earthVertexShader = `
out vec4 vPosition;
out vec2 vUV;

void main() {
  vPosition = modelMatrix * vec4(position, 1.0);
  vUV = uv;

  gl_Position = projectionMatrix * modelViewMatrix * vec4( position, 1.0 );
}
`;
const earthFragmentShader = `
uniform sampler2D dayTexture;
uniform sampler2D nightTexture;
uniform vec3 lightPosition;

in vec4 vPosition;
in vec2 vUV;

layout(location = 0) out vec4 FragColor;

void main() {
  vec3 light = normalize(lightPosition);
  vec4 position = normalize(vPosition);

  float intensity = max(dot(position, vec4(light, 1.0)),0.33);

  vec4 dayColor = texture2D(dayTexture, vUV);
  vec4 nightColor = texture2D(nightTexture, vUV);

  FragColor = mix(nightColor, dayColor, intensity);
}
`;

const earthMaterial = new ShaderMaterial({
  uniforms: {
    dayTexture: { value: eartDayhMap },
    nightTexture: { value: earthNightMap },
    lightPosition: { value: sunLight.position },
  },
  vertexShader: earthVertexShader,
  fragmentShader: earthFragmentShader,
  glslVersion: GLSL3,
});

const earthMesh = new Mesh(earthGeometry, earthMaterial);

earthGroup.add(earthMesh);

// clouds
const earthCloudsMap = loader.load("/earth_clouds.jpg");

const earthCloudsMaterial = new MeshStandardMaterial({
  map: earthCloudsMap,
  blending: AdditiveBlending,
  alphaMap: earthCloudsMap,
});

const earthCloudsMesh = new Mesh(earthGeometry, earthCloudsMaterial);
earthCloudsMesh.scale.setScalar(1.005);

earthGroup.add(earthCloudsMesh);

// coordinates
const coordGroup = new Group();

/**
 * 
 * @param latitude vertical coordinates
 * @param longitude horizontal coordinates
 */
function getCoordinateLocation (latitude, longitude) {
  const z = RADIUS * Math.cos(radians(latitude)) * Math.cos(radians(longitude + 90))
  const x = RADIUS * Math.cos(radians(latitude)) * Math.sin(radians(longitude + 90))
  const y = RADIUS * Math.sin(radians(latitude))

  return { x,y,z };
}

const COORD_RADIUS = 0.125
const coordGeometry = new SphereGeometry(COORD_RADIUS, 64, 32);

let coordContent = {};

// on new input, add new coordinates
const updateEvents = (events) => {

  if (events) {
    coordGroup.clear();
    coordContent = {};

    events.map((e) => {
      const lat = parseInt(e["lat"]["value"])
      const lon = parseInt(e["lon"]["value"])
      const coordString = `${lat}-${lon}`

      const name = e["eventLabel"]["value"];

      if (!(coordString in coordContent)) {
        // create new point, add name to stuff
        coordContent[coordString] = [name]

        const coord = getCoordinateLocation(lat, lon);
        const coordMaterial = new MeshBasicMaterial( { color: 0xff0000 } );
        const coordMesh = new Mesh(coordGeometry, coordMaterial);

        coordMesh.name = coordString;

        const coordPosition = new Vector3(coord.x, coord.y, coord.z);
        coordMesh.position.copy(coordPosition);
        coordGroup.add(coordMesh);

        // create label
        const coordDiv = document.createElement('div');
        coordDiv.setAttribute("id", coordString);

        const coordLabel =  new CSS2DObject(coordDiv);
        coordLabel.position.set(0, 1.5 * COORD_RADIUS, 1.5 * COORD_RADIUS);
        coordLabel.center.set( 0, 0 );
				coordMesh.add(coordLabel);

      } else {
        coordContent[coordString].push(name);
      }
    })

  }
};

earthGroup.add(coordGroup);
scene.add(earthGroup);
//#endregion

//#region Three.js Events
document.addEventListener("mousemove", onPointerMove);

function onPointerMove( event ) {
  pointer.x = ( event.clientX / window.innerWidth ) * 2 - 1;
  pointer.y = - ( event.clientY / window.innerHeight ) * 2 + 1;
}

window.addEventListener('resize', onWindowResize, false);

function onWindowResize() {
  renderer.setSize(window.innerWidth, window.innerHeight);
  labelRenderer.setSize( window.innerWidth, window.innerHeight );

  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
}

const labelRenderer = new CSS2DRenderer();
labelRenderer.setSize( window.innerWidth, window.innerHeight );
labelRenderer.domElement.style.position = 'absolute';
labelRenderer.domElement.style.top = '0px';
labelRenderer.domElement.style.pointerEvents = 'none';
document.body.appendChild( labelRenderer.domElement );

// orbit controls
const controls = new OrbitControls(camera, renderer.domElement);
let rotationSpeed = 0.0005;
let currentRotationSpeed = rotationSpeed;
let targetRotationSpeed = rotationSpeed;
let interactionTimeout;

function onInteractionStart() {
  // Smoothly slow down the rotation when user starts interacting
  targetRotationSpeed = 0;
  clearTimeout(interactionTimeout);
}

function onInteractionEnd() {
  // Smoothly resume rotation after 2 seconds of no interaction
  interactionTimeout = setTimeout(() => {
    targetRotationSpeed = rotationSpeed;
  }, 10 * 1000);
}

controls.addEventListener('start', onInteractionStart);
controls.addEventListener('end', onInteractionEnd);
//#endregion

//#region Main loop
let INTERSECTED;

function animate() {
    setTimeout(() => requestAnimationFrame( animate ), 1000 / 30 );

  controls.update();

  currentRotationSpeed += (targetRotationSpeed - currentRotationSpeed) * 0.025;

  earthCloudsMesh.rotateY(currentRotationSpeed / 1.5);
  earthGroup.rotateY(currentRotationSpeed);

  raycaster.setFromCamera( pointer, camera );
  const intersects = raycaster.intersectObjects(coordGroup.children, false);

  if (intersects.length > 0) {

    if (!INTERSECTED) {
      INTERSECTED = intersects[0].object;
    } else {
      if (INTERSECTED != intersects[0].object) {
        INTERSECTED.material.color.setHex( 0xff0000 );
        INTERSECTED = intersects[0].object;
      }
    }
    
    INTERSECTED.children[0].element.textContent = coordContent[INTERSECTED.name].join(", ");
    INTERSECTED.material.color.setHex( 0xffffff );

  } else {
    if (INTERSECTED) {
      INTERSECTED.children[0].element.textContent = "";
      INTERSECTED.material.color.setHex( 0xff0000 );
    }
  }

  renderer.render(scene, camera);
  labelRenderer.render(scene, camera);
}
//#endregion

//#region Vue Stuff

// Watch for prop changes and update the scene accordingly
const props = defineProps(['scene-data'])

watch(() => props.sceneData, (newData) => {
  if (newData) {
    const jsonData = JSON.parse(JSON.stringify(newData));
    updateEvents(jsonData);
  }
});

onMounted(() => {
  earth.value.appendChild(renderer.domElement);
  animate();
})
//#endregion
</script>

<template>
  <div ref="earth"></div>
</template>

<style scoped></style>
