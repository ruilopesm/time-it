<script>
	import addEventModal from './modals/AddEventModal.svelte';
	import ShowIdModal from './modals/ShowIdModal.svelte';
	import { openModal, closeModals } from 'svelte-modals';
	import { onMount } from 'svelte';

	let events = [];

	function addEvent(event_title, event_date_start, event_date_end, event_tags) {
		events.push({
			local_id: events.length,
			title: event_title,
			date_start: event_date_start,
			date_end: event_date_end,
			tags: event_tags
		});

		//Trigger svelte DOM update
		events = events;

		closeModals();
	}

	let id = null;

	onMount(() => {
		id = localStorage.getItem('schedule_id');
	});

	function createSchedule() {
		let json = [];
		events.forEach((event) => {
			json.push({
				title: event.title,
				date_start: new Date(event.date_start).getTime(),
				date_end: new Date(event.date_end).getTime(),
				tags: event.tags.split(';')
			});
		});

		fetch('http://127.0.0.1:8000/api/create', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(json)
		}).then((data) => {
			data.json().then((json) => {
				id = json.id;
				localStorage.setItem('schedule_id', id);
			});
		});
	}
</script>

{#if id !== null}
	<div class="backdrop" />
	<ShowIdModal {id} />
{/if}

{#if events.length === 0}
	<div class="center">
		<h1>Looks so empty, click the button to start adding events.</h1>
	</div>
{:else}
	<h1 class="title">Your events:</h1>
{/if}

{#each events as { local_id, name, date_start, date_end, tags } (local_id)}
	<div class="event">
		<h1>{local_id + 1}# {name}</h1>
		<p>Date: (start-end): {date_start} - {date_end}</p>
		<p>Tags: {tags}</p>
	</div>
{/each}

{#if events.length !== 0}
	<div class="createschedule">
		<button class="btn btn-primary" on:click={() => createSchedule()}>Create schedule</button>
	</div>
{/if}

<button class="btn btn-primary addevent" on:click={() => openModal(addEventModal, { title: 'Create Event', addEvent: addEvent })}>Add Event</button>

<style>
	.center {
		width: 85vw;
		height: 100vh;
		margin: auto;
		display: flex;
		justify-content: center;
		align-items: center;
		text-align: center;
	}

	button.addevent {
		font-size: 20px;
		line-height: 0;
		height: 50px;
		border-radius: 15px;
		position: fixed;
		right: 0;
		bottom: 0;
		margin: 20px;
		padding-bottom: 8px;
	}

	.title {
		text-align: center;
		font-size: 40px;
		margin-bottom: 20px;
		margin-top: 20px;
	}

	.event {
		margin: 20px;
		padding: 20px;
		border: 1px solid #ccc;
		border-radius: 5px;
	}

	.createschedule {
		display: flex;
		justify-content: center;
		align-items: center;
		margin-top: 40px;
	}
</style>
