<script lang="ts">
	import { onMount } from "svelte";
	import { NotificationPosition, NotificationStatus } from "../lib/types/notification";

	export let message: string;
	export let pos: NotificationPosition = NotificationPosition.TopCenter;
	export let status: NotificationStatus = NotificationStatus.Default;
	export let timeout: number = 5000;

	function showNotification() {
		// @ts-ignore
		UIkit.notification({
			message,
			pos: pos.toString(),
			status: status.toString(),
			timeout: timeout,
		});
	}
</script>

<button class="uk-button uk-button-default" type="button" on:click={showNotification}>
	Top Left
</button>
