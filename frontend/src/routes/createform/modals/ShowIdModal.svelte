<script>
	export let id;
</script>

<div role="dialog" class="modal">
	<div class="contents">
		<h1>Your schedule ID is: {id}</h1>
		<h4>Access the API with http://127.0.0.1:8000/api/{id}/schedule</h4>
		<h5>Read more at our <a href="https://github.com/RuiL1904/Hackathon">GitHub</a></h5>
	</div>
</div>

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
		width: 60vw;
		text-align: center;
		overflow: auto;
	}
</style>
