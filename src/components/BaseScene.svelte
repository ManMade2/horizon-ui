<script lang="ts">
	import { T, useThrelte } from "@threlte/core";
	import { OrbitControls, interactivity } from "@threlte/extras";
	import SceneSettings from "./SceneSettings.svelte";
	import { onMount } from "svelte";
	import type { OrbitControlsSettings } from "../lib/types/orbitControlSettings";

	const { scene } = useThrelte();

	let settings: OrbitControlsSettings = {
		enableDamping: true,
		autoRotate: false,
		rotateSpeed: 1,
		zoomToCursor: false,
		zoomSpeed: 1,
		minPolarAngle: 0,
		maxPolarAngle: Math.PI,
		enableZoom: true,
		dampingFactor: 0.25,
	};

	var position: [number, number, number] = [10, 5, 10];

	const mouseButtons = {
		LEFT: null, // Left click to pan
		MIDDLE: 2, // Middle click to zoom (default)
		RIGHT: 0, // Right click to rotate
	};
</script>

<T.PerspectiveCamera makeDefault {position} lookAt.y={0.5}>
	<T.Mesh>
		<T.BoxGeometry />
		<T.MeshBasicMaterial color="red" />
	</T.Mesh>
	<OrbitControls
		{mouseButtons}
		enableDamping={settings.enableDamping}
		autoRotate={settings.autoRotate}
		rotateSpeed={settings.rotateSpeed}
		zoomToCursor={settings.zoomToCursor}
		zoomSpeed={settings.zoomSpeed}
		minPolarAngle={settings.minPolarAngle}
		maxPolarAngle={settings.maxPolarAngle}
		enableZoom={settings.enableZoom}
		dampingFactor={settings.dampingFactor}
	/>
</T.PerspectiveCamera>

<slot />

<T.AmbientLight intensity={0.8} />
<T.DirectionalLight position.y={10} position.z={10} />
