<script>
	import { closeModal } from 'svelte-modals';
	import SveltyPicker from 'svelty-picker';

	export let isOpen;
	export let title;
	export let addEvent;

	let event_name;
	let event_date_end;
	let event_date_start;
	let event_tags;
</script>

{#if isOpen}
	<div role="dialog" class="modal">
		<div class="contents">
			<h1>{title}</h1>

			<form on:submit|preventDefault={addEvent(event_name, event_date_start, event_date_end, event_tags)}>
				<input type="text" name="name" class="form-control" placeholder="Event Name" id="event_name" bind:value={event_name} />
				<SveltyPicker inputClasses="form-control" format="yyyy-mm-dd hh:ii" bind:value={event_date_start} placeholder="Start Date" />
				<SveltyPicker inputClasses="form-control" format="yyyy-mm-dd hh:ii" bind:value={event_date_end} placeholder="End Date" />
				<input type="text" class="form-control" placeholder="Event Tags" name="tags" bind:value={event_tags} />
				<input class="btn btn-primary" type="submit" value="Add event" />
			</form>

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
		padding-top: 26px;
		padding-bottom: 26px;
		padding-left: 16px;
		padding-right: 16px;
		background: white;
		display: flex;
		flex-direction: column;
		justify-content: space-between;
		pointer-events: auto;
		max-height: 90vh;
		width: 60vw;
		text-align: center;
		overflow: auto;
	}

	.actions {
		position: absolute;
		right: 22%;
	}

	:global(.form-control) {
		width: 200px;
		margin-top: 10px;
	}
</style>
