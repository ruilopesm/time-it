<script>
	import { closeModal } from 'svelte-modals';

	export let isOpen;

	export let title;
	export let data;
</script>

{#if isOpen}
	<div role="dialog" class="modal">
		<div class="contents">
			<h1>{title}</h1>
			{#each data as { title, date_start, date_end }}
				<h3>{title}</h3>
				<h6>{new Date(parseInt(date_start) * 1000).toLocaleString('en-GB')}</h6>
				<h6>{new Date(parseInt(date_end) * 1000).toLocaleString('en-GB')}</h6>
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
		right: 12%;
	}
</style>
