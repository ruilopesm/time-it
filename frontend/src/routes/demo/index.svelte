<script>
	import Form from './Form.svelte';
	import CreateIdFirstModal from './modals/CreateIdFirstModal.svelte';
	import { onMount } from 'svelte';

	let id = undefined;

	onMount(() => {
		id = localStorage.getItem('schedule_id');
	});
</script>

<svelte:head>
	<title>API Test</title>
</svelte:head>

{#if id === null}
	<div class="backdrop" />
	<CreateIdFirstModal />
{:else if id !== undefined}
	<Form />
{/if}
