<script lang="ts">
	import Button from "./components/Button.svelte";
	import DrawerNav from "./components/DrawerNav.svelte";
	import Sidebar from "./components/Sidebar.svelte";
	import { ButtonSize, ButtonVariant } from "./lib/types/button";
	import Notification from "./components/Notification.svelte";
	import { NotificationPosition, NotificationStatus } from "./lib/types/notification";
	import Upload from "./components/Upload.svelte";
	import Canvas from "./components/Canvas.svelte";

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
	</Sidebar>

	<main class="main-content">
		<!--<Button variant={ButtonVariant.Link} size={ButtonSize.Small}>Link</Button>
		<Button variant={ButtonVariant.Default}>Default</Button>
		<Button variant={ButtonVariant.Primary}>Primary</Button>
		<Button variant={ButtonVariant.Secondary}>Secondary</Button>
		<Button variant={ButtonVariant.Danger}>Danger</Button>
		<Button variant={ButtonVariant.Text}>Text</Button>
		<Notification
			message="Top Center"
			pos={NotificationPosition.TopCenter}
			status={NotificationStatus.Danger}
			timeout={1000}
		/>
		<Upload options={uploadOptions} />-->
		<Canvas />
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
