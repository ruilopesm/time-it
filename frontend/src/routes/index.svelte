<script>
	import Music from './forms/musicForm.svelte';
	let visibleForm = Music;
</script>

<svelte:head>
	<title>API Test</title>
</svelte:head>

<svelte:component this={visibleForm} />
