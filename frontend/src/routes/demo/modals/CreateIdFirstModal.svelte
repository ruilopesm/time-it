<div role="dialog" class="modal">
	<div class="contents">
		<h1>You need to get an ID first!</h1>
		<p>You can get an ID by clicking the below button</p>
		<button class="btn btn-primary"><a href="http://localhost:3000/createform">Get ID</a></button>
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
		width: 80vw;
		text-align: center;
		overflow: auto;
	}

	button {
		margin-top: 20px;
	}

	a {
		text-decoration: none;
		color: white;
	}
</style>
