<script>
	import { closeModal } from 'svelte-modals';

	export let isOpen;

	export let data;
	console.log(data);
</script>

{#if isOpen}
	<div role="dialog" class="modal">
		<div class="contents">
			<h1>Schedule</h1>
			{#each data as { title, date_start, date_end }}
				<h3>{title}</h3>
				<h6>{new Date(parseInt(date_start)).toLocaleString('en-GB')}</h6>
				<h6>{new Date(parseInt(date_end)).toLocaleString('en-GB')}</h6>
			{/each}
			<div class="actions">
				<button class="btn-close" on:click={closeModal} />
			</div>
		</div>
	</div>
{/if}

<style>
	.modal {
		position: fixed;
		top: 0;
		bottom: 0;
		right: 0;
		left: 0;
		display: flex;
		justify-content: center;
		align-items: center;
		pointer-events: none;
		width: 60%;
		margin: auto;
	}

	.contents {
		min-width: 240px;
		border-radius: 6px;
		padding: 16px;
		background: white;
		display: flex;
		flex-direction: column;
		justify-content: space-between;
		pointer-events: auto;
		max-height: 90vh;
		width: 80vw;
		text-align: center;
		overflow: auto;
	}

	h3 {
		margin-top: 10px;
	}

	.actions {
		position: absolute;
		right: 3%;
	}
</style>
