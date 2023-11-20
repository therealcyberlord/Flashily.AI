<script>
	export let question;
	export let answer;
	export let showCardBack;

	// make a request to the backend to get the audio file
	const getAudio = async (text) => {
		try {
			const response = await fetch("http://localhost:8000/tts?text=" + text);

			if (!response.ok) {
				throw new Error(`HTTP error! Status: ${response.status}`);
			}

			const audioBlob = await response.blob();
			const audioUrl = URL.createObjectURL(audioBlob);

			const audioElement = new Audio(audioUrl);
			audioElement.play();
		} catch (error) {
			console.error("Error:", error);
		}
	};
</script>

<div class="flip-box-front">
	<div id="image-cont">
		<h2>{question}</h2>
		<button on:click={getAudio(question)}>🔉</button>
	</div>
</div>

<div class="flip-box-back" class:conceal-answer={showCardBack}>
	<h2>{answer}</h2>
	<button on:click={getAudio(answer)}>🔉</button>
</div>

<style>
	/* Position the front and back side */
	.flip-box-front,
	.flip-box-back {
		position: absolute;
		width: 100%;
		height: 100%;
		-webkit-backface-visibility: hidden; /* Safari */
		backface-visibility: hidden;
		box-shadow: -1px 1px 3px black;
		border-radius: 20px;
	}

	/* Style the front side */
	.flip-box-front {
		background-color: #ddd;
		color: black;
		display: flex;
		justify-content: center;
		border-radius: 20px;
	}

	@keyframes revealTextSlowly {
		to {
			color: white;
		}
	}

	.conceal-answer {
		animation: revealTextSlowly 0.3s forwards;
	}

	/* Style the back side */
	.flip-box-back {
		display: flex;
		justify-content: center;
		align-items: center;
		background-color: #2980b9;
		font-size: 1.3rem;
		transform: rotateY(180deg);
		border-radius: 20px;
	}

	#image-cont {
		max-width: 100%;
		display: flex;
		justify-content: center;
		align-items: center;
		font-size: 1.3rem;
	}
</style>
