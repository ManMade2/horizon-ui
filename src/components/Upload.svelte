<script lang="ts">
	import { onMount } from "svelte";
	import type { UploadProps } from "../lib/types/upload";

	export let options: UploadProps["options"];
	let progressBar: HTMLProgressElement;

	onMount(() => {
		if (!progressBar) return;

		// @ts-ignore
		UIkit.upload(".js-upload", {
			url: options.url,
			multiple: options.multiple,
			name: options.name,
			params: options.params,
			allow: options.allow,
			mime: options.mime,
			onBeforeSend: options.onBeforeSend,
			onProgress: options.onProgress,
			onComplete: options.onComplete,
			onError: options.onError,

			beforeAll: function (environment: any) {
				options.onBeforeSend?.(environment);
			},
			load: function () {},
			error: function () {
				options.onError?.(arguments);
			},
			complete: function () {
				options.onComplete?.(arguments);
			},

			loadStart: function (e: ProgressEvent) {
				progressBar.removeAttribute("hidden");
				progressBar.max = e.total;
				progressBar.value = e.loaded;
			},

			progress: function (e: ProgressEvent) {
				progressBar.max = e.total;
				progressBar.value = e.loaded;
			},

			loadEnd: function (e: ProgressEvent) {
				progressBar.max = e.total;
				progressBar.value = e.loaded;
			},

			completeAll: function () {
				setTimeout(function () {
					progressBar.setAttribute("hidden", "hidden");
				}, 1000);

				options.onComplete?.(arguments);
			},
		});
	});
</script>

<div class="js-upload uk-placeholder uk-text-center">
	<span class="uk-text-middle">Drop file here or</span>
	<div data-uk-form-custom>
		<input type="file" multiple />
		<span class="uk-link">select one</span>
	</div>
</div>

<progress bind:this={progressBar} class="uk-progress" value="0" max="100" hidden></progress>
