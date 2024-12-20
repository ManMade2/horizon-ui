<script lang="ts">
	import DrawerNav from "./components/DrawerNav.svelte";
	import Sidebar from "./components/Sidebar.svelte";
	import Canvas from "./components/Canvas.svelte";
	import dracoLoader from "./lib/loaders/dracoLoader";
	let sceneObjects: any[] = [];

	const navItems = [
		{
			label: "Parent",
			href: "#",
			children: [
				{
					label: "Sub item",
					href: "#",
				},
				{
					label: "Sub item",
					href: "#",
					children: [
						{
							label: "Sub item",
							href: "#",
						},
						{
							label: "Sub item",
							href: "#",
						},
					],
				},
			],
		},
		{
			label: "Parent",
			href: "#",
			children: [
				{
					label: "Sub item",
					href: "#",
				},
				{
					label: "Sub item",
					href: "#",
				},
			],
		},
	];

	const uploadOptions = {
		url: "/api/upload",
		multiple: true,
		onBeforeSend: (e: any) => {
			console.info(e);
		},
		onProgress: (e: any) => {
			console.info(e);
		},
		onComplete: (e: any) => {
			console.info(e);
		},
		onError: (e: any) => {
			console.info(e);
		},
	};
</script>

<div class="app-shell">
	<Sidebar isOpen={true}>
		<DrawerNav items={navItems} />
		{#each sceneObjects as object}
			<div>
				<h1>{object.type}</h1>
			</div>
		{/each}
	</Sidebar>

	<main class="main-content">
		<Canvas bind:sceneObjects />
	</main>
</div>

<style lang="scss">
	:global(*) {
		margin: 0;
		padding: 0;
		box-sizing: border-box;
	}

	.app-shell {
		display: flex;
		height: 100vh;
		width: 100vw;
		overflow: hidden;
	}

	.main-content {
		flex: 1;
		padding: 2rem;
		overflow-y: auto;
	}
</style>
