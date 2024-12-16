<script lang="ts">
	import { Checkbox, Pane, ThemeUtils, Slider } from "svelte-tweakpane-ui";
	import type { OrbitControlsSettings } from "../lib/types/orbitControlSettings";

	export let settings: OrbitControlsSettings;
</script>

<Pane theme={ThemeUtils.presets.standard} position="fixed" title="OrbitControls">
	<Checkbox bind:value={settings.autoRotate} label="autoRotate" />
	<Checkbox bind:value={settings.enableDamping} label="enableDamping" />
	<Checkbox bind:value={settings.enableZoom} label="enableZoom" />
	<Checkbox bind:value={settings.zoomToCursor} label="zoomToCursor" />
	<Slider label="rotateSpeed" bind:value={settings.rotateSpeed} min={0.5} max={1} step={0.1} />
	<Slider
		label="dampingFactor"
		bind:value={settings.dampingFactor}
		min={0.05}
		max={0.5}
		step={0.05}
	/>
	<Slider label="zoomSpeed" bind:value={settings.zoomSpeed} min={0.1} max={2} step={0.1} />
	<Slider
		label="minPolarAngle"
		bind:value={settings.minPolarAngle}
		min={0}
		max={Math.PI}
		step={0.1}
	/>
	<Slider
		label="maxPolarAngle"
		bind:value={settings.maxPolarAngle}
		min={0}
		max={Math.PI}
		step={0.1}
	/>
</Pane>
