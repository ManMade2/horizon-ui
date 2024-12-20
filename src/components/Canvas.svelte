<script lang="ts">
	import { Canvas } from "@threlte/core";
	import BaseScene from "./BaseScene.svelte";
	import SceneHook from "./SceneHook.svelte";

	export let sceneObjects: any[] = [];
</script>

<Canvas>
	<BaseScene>
		<slot />
	</BaseScene>
	<SceneHook bind:sceneObjects />
	{#each sceneObjects as object}
		<div>
			<h1>{object.type}</h1>
		</div>
	{/each}
</Canvas>
