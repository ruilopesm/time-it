<script>
	import '../app.css';
	import { Modals, closeModal } from 'svelte-modals';
</script>

<Modals>
	<div slot="backdrop" class="backdrop" on:click={closeModal} />
</Modals>

<section class="title">
	<h1>Form</h1>
	<h2>Select from 0 to 5 according to your preferences:</h2>
</section>

<main>
	<slot />
</main>

<style>
	.backdrop {
		position: fixed;
		top: 0;
		bottom: 0;
		right: 0;
		left: 0;
		background: rgba(0, 0, 0, 0.5);
	}

	.title {
		text-align: center;
		margin-bottom: 2rem;
		margin-top: 2rem;
	}
</style>
