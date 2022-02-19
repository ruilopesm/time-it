<script>
	import Modal from 'src/routes/demo/modals/ScheduleModal.svelte';
	import { openModal } from 'svelte-modals';

	let tags = [];
	let schedule = {};
	let id = localStorage.getItem('schedule_id');

	function getTags() {
		fetch(`http://localhost:8000/api/${id}/tags`, {
			method: 'GET',
			headers: {
				'Content-Type': 'application/json'
			}
		})
			.then((response) => response.json())
			.then((data) => {
				tags = data;
				populateScheduleWithDefaultValues();
			});
	}

	// Populate the schedule with default value (3)
	function populateScheduleWithDefaultValues() {
		tags.forEach((tag) => {
			schedule[tag] = 3;
		});
	}

	function getSchedule() {
		fetch(`http://localhost:8000/api/${id}/schedule`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(schedule)
		})
			.then((response) => response.json())
			.then((data) => {
				openModal(Modal, { data: data });
			});
	}

	getTags();
</script>

<section class="title">
	<h1>Form</h1>
	<h2>Select from 0 to 5 according to your preferences:</h2>
</section>
<form id="musicForm" on:submit|preventDefault={getSchedule}>
	<div class="inputs" style="grid-template-columns: repeat({Math.min(3, tags.length)}, 1fr);">
		{#each tags as tag, i}
			<div class="{tag} input">
				<label for={tag}>{tag}: </label>
				<input
					type="range"
					id={tag}
					min="0"
					max="5"
					step="1"
					value="3"
					on:input={(event) => {
						schedule[tag] = parseInt(event.target.value) === undefined ? 3 : parseInt(event.target.value);
					}}
				/>
				<output for={tag} id="{tag}-output">{schedule[tag]}</output>
				<br />
			</div>
		{/each}
	</div>
	<input type="submit" value="Create shedule" class="btn btn-primary" />
</form>

<style>
	.title {
		text-align: center;
		margin-bottom: 2rem;
		margin-top: 2rem;
	}

	.inputs {
		margin-top: 30px;
		display: grid;
		grid-gap: 50px;
		text-align: center;
	}

	.input {
		display: flex;
		flex-direction: column;
	}
</style>
