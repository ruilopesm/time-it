<script>
	import Modal from '$lib/Modal.svelte';
	import { openModal } from 'svelte-modals';

	let rock = 3;
	let pop = 3;
	let rap = 3;
	let eletronica = 3;
	let tradicional = 3;
	let jazz = 3;
	let metal = 3;

	function submit() {
		fetch('http://localhost:8000/', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				schedule: [
					{
						title: 'Abertura',
						date_start: '1641027600',
						date_end: '1641031200',
						tags: []
					},
					{
						title: 'Timmy Trumpet',
						date_start: '1641031200',
						date_end: '1641038400',
						tags: ['eletronica']
					},
					{
						title: 'Metallica',
						date_start: '1641031200',
						date_end: '1641038400',
						tags: ['rock']
					},
					{
						title: 'Almoço',
						date_start: '1641038400',
						date_end: '1641045600',
						tags: []
					},
					{
						title: 'Marshmello',
						date_start: '1641045600',
						date_end: '1641052800',
						tags: ['eletronica']
					},
					{
						title: 'Profjam',
						date_start: '1641045600',
						date_end: '1641052800',
						tags: ['rap']
					},
					{
						title: 'Tuna Académica',
						date_start: '1641052800',
						date_end: '1641060000',
						tags: ['traditional']
					},
					{
						title: 'Julinho KSD',
						date_start: '1641052800',
						date_end: '1641060000',
						tags: ['rap']
					},
					{
						title: 'JMF',
						date_start: '1641060000',
						date_end: '1641067200',
						tags: ['jazz']
					},
					{
						title: 'Miguel G',
						date_start: '1641060000',
						date_end: '1641067200',
						tags: ['pop']
					},
					{
						title: 'Artic Monkeys',
						date_start: '1641067200',
						date_end: '1641074400',
						tags: ['eletronica']
					}
				],
				interests: {
					tags: {
						rock: rock,
						metal: metal,
						eletronica: eletronica,
						pop: pop,
						rap: rap,
						jazz: jazz,
						tradicional: traditional
					}
				}
			})
		}).then((responseToJson) => {
			responseToJson.json().then((data) => {
				openModal(Modal, { title: 'Horário', data: data });
			});
		});
	}
</script>

<form id="musicForm" on:submit|preventDefault={submit}>
	<div class="inputs">
		<div class="rock input">
			<label for="rock">Rock: </label>
			<input type="range" id="rock" min="0" max="5" step="1" bind:value={rock} />
			<output for="rock" id="rock-output">{rock}</output>

			<br />
		</div>
		<div class="pop input">
			<label for="pop">Pop: </label>
			<input type="range" id="pop" min="0" max="5" step="1" bind:value={pop} />
			<output for="pop" id="pop-output">{pop}</output>

			<br />
		</div>
		<div class="rap input">
			<label for="rap">Rap: </label>
			<input type="range" id="rap" min="0" max="5" step="1" bind:value={rap} />
			<output for="rap" id="rap-output">{rap}</output>

			<br />
		</div>
		<div class="eletronica input">
			<label for="eletronica">Eletrónica: </label>
			<input type="range" id="eletronica" min="0" max="5" step="1" bind:value={eletronica} />
			<output for="eletronica" id="eletronica-output">{eletronica}</output>

			<br />
		</div>
		<div class="tradicional input">
			<label for="tradicional">Tradicional: </label>
			<input type="range" id="tradicional" min="0" max="5" step="1" bind:value={tradicional} />
			<output for="tradicional" id="tradicional-output">{tradicional}</output>

			<br />
		</div>
		<div class="jazz input">
			<label for="jazz">Jazz: </label>
			<input type="range" id="jazz" min="0" max="5" step="1" bind:value={jazz} />
			<output for="jazz" id="jazz-output">{jazz}</output>

			<br />
		</div>
		<div class="metal input">
			<label for="metal">Metal: </label>
			<input type="range" id="metal" min="0" max="5" step="1" bind:value={metal} />
			<output for="metal" id="metal-output">{metal}</output>
		</div>
		<br />
	</div>
	<input type="submit" value="Criar horário" class="btn btn-primary" />
</form>

<style>
	.inputs {
		display: grid;
		grid-template-columns: 1fr 1fr 1fr;
		grid-gap: 50px;
		text-align: center;
	}

	.input {
		display: flex;
		flex-direction: column;
	}
</style>
