<script>
	import Music from './forms/musica.svelte';
	let visibleForm = Music;
</script>

<svelte:head>
	<title>API Test</title>
</svelte:head>

<svelte:component this={visibleForm} />
