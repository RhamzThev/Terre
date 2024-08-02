import './style.css'

import * as THREE from 'three';

import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { UnrealBloomPass } from "/node_modules/three/examples/jsm/postprocessing/UnrealBloomPass.js";

const scene = new THREE.Scene();

const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1);

const renderer = new THREE.WebGLRenderer({
  canvas: document.getElementById("bg"),
  antialias: true
})

renderer.setPixelRatio(window.devicePixelRatio);
renderer.setSize(window.innerWidth, window.innerHeight);

camera.position.setZ(30);

const loader = new THREE.TextureLoader();

scene.background = loader.load("/milky_way.jpg");

const ADJACENT_LENGTH = 60
const OPPOSITE_LENGTH = ADJACENT_LENGTH * Math.tan(0.4101524)

const SUN_POSITION = new THREE.Vector3(0, OPPOSITE_LENGTH, ADJACENT_LENGTH);

//#region Earth
const earthGeometry = new THREE.SphereGeometry(15, 64, 32);

const earthMap = loader.load('/earth_day.jpg');
const earthNightMap = loader.load("/earth_night.jpg");

const earthVertexShader = `
out vec3 vPosition;
out vec3 vNormal;
out vec2 vUV;

void main() {
  vPosition = position;
  vNormal = normal;
  vUV = uv;
  gl_Position = projectionMatrix * modelViewMatrix * vec4( position, 1.0 );
}

`;

const earthFragmentShader = `
uniform sampler2D dayTexture;
uniform sampler2D nightTexture;
uniform vec3 lightPosition;

in vec3 vPosition;
in vec3 vNormal;
in vec2 vUV;

layout(location = 0) out vec4 FragColor;

void main() {

  vec3 lightDirection = normalize(lightPosition - vPosition);
  float dotProduct = max(dot(vNormal, lightDirection), 0.25);

  vec4 dayColor = texture2D(dayTexture, vUV);
  vec4 nightColor = texture2D(nightTexture, vUV);
  FragColor = mix(nightColor, dayColor, dotProduct);
}

`;

const earthMaterial = new THREE.ShaderMaterial({
  uniforms: {
    dayTexture: { value: earthMap },
    nightTexture: { value: earthNightMap },
    lightPosition: { value: SUN_POSITION }
  },
  vertexShader: earthVertexShader,
  fragmentShader: earthFragmentShader,
  glslVersion: THREE.GLSL3,
});

const earthMesh = new THREE.Mesh(earthGeometry, earthMaterial);
scene.add(earthMesh)



// Clouds
const earthCloudsMap = loader.load("/earth_clouds.jpg");

const earthCloudsMaterial = new THREE.MeshStandardMaterial({
  map: earthCloudsMap,
  blending: THREE.AdditiveBlending,
  alphaMap: earthCloudsMap,
})
const earthCloudsMesh = new THREE.Mesh(earthGeometry, earthCloudsMaterial);
earthCloudsMesh.scale.setScalar(1.005)
scene.add(earthCloudsMesh)

// Glow
const earthGlowVertexShader = `
out vec3 vPosition;
out vec3 vNormal;
out vec2 vUV;

void main() {
  vPosition = position;
  vNormal = normal;
  vUV = uv;
  gl_Position = projectionMatrix * modelViewMatrix * vec4( position, 1.0 );
}

`;

const earthGlowFragmentShader = `
in vec3 vPosition;
in vec3 vNormal;
in vec2 vUV;

layout(location = 0) out vec4 FragColor;

void main() {
  vec3 camera = normalize(cameraPosition);
  float intensity = 1.01 - dot(vNormal, camera);
  vec3 atmosphere = vec3(0,0.25,0.5) * pow(intensity, 1.1);

  FragColor = vec4(atmosphere, 1);
}

`;

const earthGlowMaterial = new THREE.ShaderMaterial({
  vertexShader: earthGlowVertexShader,
  fragmentShader: earthGlowFragmentShader,
  glslVersion: THREE.GLSL3,
  blending: THREE.AdditiveBlending,
});

const earthGlowMesh = new THREE.Mesh(earthGeometry, earthGlowMaterial);
earthGlowMesh.scale.setScalar(1.01);
scene.add(earthGlowMesh);

//#endregion
const ambientLight = new THREE.AmbientLight(0xffffff, 0.005); // soft white light 
scene.add(ambientLight);

// Sun
const pointLight = new THREE.PointLight(0xffffff, 1000);
pointLight.position.copy(SUN_POSITION);
scene.add(pointLight);

const sunMaterial = new THREE.ShaderMaterial({
  vertexShader: `
    out vec3 vPosition;
    out vec3 vNormal;
    out vec2 vUV;

    void main() {
      vPosition = position;
      vNormal = normal;
      vUV = uv;
      gl_Position = projectionMatrix * modelViewMatrix * vec4( position, 1.0 );
    }
  `,
  fragmentShader: `
    in vec3 vPosition;

    layout (location = 0) out vec4 FragColor;

    void main() {
      float dist = 1.0/length(vPosition);
      dist *= 0.1;
      dist = pow(dist, 0.8);
      vec3 col = dist * vec3(1,1,1);
      col = 1.0 - exp( -col );
      FragColor = vec4(col, 1.0);
    }
  `,
  glslVersion: THREE.GLSL3,
});

const sunMesh = new THREE.Mesh(
  new THREE.SphereGeometry(15, 64, 32),
  sunMaterial,
  // new THREE.MeshBasicMaterial({ color: 0xffffff })
)

// sunMesh.position.set(0, OPPOSITE_LENGTH * 25, ADJACENT_LENGTH * 25)
// sunMesh.position.set(0, 13, 30);
// scene.add(sunMesh);

// Stars
const controls = new OrbitControls(camera, renderer.domElement);

function animate() {

  // required if controls.enableDamping or controls.autoRotate are set to true
  controls.update();
  earthCloudsMesh.rotateY(0.00075)

  earthMaterial.uniforms.lightPosition.value.applyAxisAngle(new THREE.Vector3(0, 1, 0), -0.0005);


  earthMesh.rotateY(0.0005);

  renderer.render(scene, camera);
}

renderer.setAnimationLoop(animate);