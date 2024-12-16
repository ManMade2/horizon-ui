<script lang="ts">
	import { Canvas } from "@threlte/core";
	import BaseScene from "./BaseScene.svelte";
</script>

<Canvas>
	<BaseScene>
		<slot />
	</BaseScene>
</Canvas>
