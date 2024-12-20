<script lang="ts">
    import { onMount } from "svelte";
    import { useThrelte } from "@threlte/core";
    const { scene } = useThrelte();

    export let sceneObjects: any[] = [];

    onMount(() => {
        const objects: any[] = [];
        scene.traverse((child) => {
            if (child.type === "Mesh") {
                objects.push(child);
                console.log(child);
            }
        });
        sceneObjects = objects;
    });
</script>
