<script>
	import { onMount } from "svelte";
	import Flashcard from "../Flashcard.svelte";
	import { Spinner } from "flowbite-svelte";
	import { GradientButton } from "flowbite-svelte";
	import MagicModal from "../MagicModal.svelte";
	import { page } from "$app/stores";

	let flashcards = [];
	let flashcardIndex = 0;
	let question = "";
	let answer = "";
	let showCardBack = false;
	let isLoading = true; // Added loading state

	console.log(JSON.stringify($page, null, 2));
	let num_flash_cards = parseInt($page.params.num);
	let prompt = $page.params.prompt;
	console.log(num_flash_cards, prompt);
	const toggleShowBack = () => (showCardBack = !showCardBack);

	const prevCard = () => {
		showCardBack = false;
		flashcardIndex =
			flashcardIndex === 0 ? flashcards.length - 1 : flashcardIndex - 1;
		updateCard();
	};

	const nextCard = () => {
		showCardBack = false;
		flashcardIndex =
			flashcardIndex === flashcards.length - 1 ? 0 : flashcardIndex + 1;
		updateCard();
	};

	const updateCard = () => {
		question = flashcards[flashcardIndex].question;
		answer = flashcards[flashcardIndex].answer;
	};

	onMount(async () => {
		try {
			if (prompt.length > 0) {
				const response = await fetch(
					`http://localhost:8000/generate?num_flash_cards=${num_flash_cards}&optional_instructions=${prompt}`
				);
				flashcards = await response.json();
				updateCard();
			} else {
				const response = await fetch(
					`http://localhost:8000/generate?num_flash_cards=${num_flash_cards}`
				);
				flashcards = await response.json();
				updateCard();
			}
		} finally {
			isLoading = false; // Set loading state to false once data is fetched
		}
	});
</script>

{#if isLoading}
	<!-- Loading screen -->
	<div class="loading-screen">
		<p>Loading...</p>
		<Spinner class="blue" />
	</div>
{:else}
	<div class="background">
		<div class="min-h-screen" />
		<main>
			<!-- FLASHCARD -->
			<div class="flip-box">
				<div class="flip-box-inner" class:flip-it={showCardBack}>
					<Flashcard {question} {answer} {showCardBack} />
				</div>
			</div>

			<!-- BUTTONS -->
			<div id="btn-cont" class="space-x-4">
				<button class="arrow-btn" on:click={prevCard}>&#8592;</button>

				<GradientButton on:click={toggleShowBack} class="w-24">
					{showCardBack ? "Hide Answer" : "Show Answer"}
				</GradientButton>

				<button class="arrow-btn" on:click={nextCard}>&#8594;</button>
			</div>
			<MagicModal flashcardCount={num_flash_cards} />
		</main>
	</div>
{/if}

<style>
	main {
		display: flex;
		flex-direction: column;
		align-items: center;
		margin-top: 15%;
		height: 100vh;
	}
	.background {
		background: linear-gradient(250deg, rgb(25, 27, 126), rgb(45, 90, 125));
		display: flex;
		height: 100%;
		justify-content: center;
		align-items: center;
	}

	/* The flip box container - set the width and height to whatever you want. We have added the border property to demonstrate that the flip itself goes out of the box on hover (remove perspective if you don't want the 3D effect */
	.flip-box {
		background-color: transparent;
		width: 500px; /* Increase the width */
		height: 400px; /* Increase the height */
		border-radius: 15px; /* Add rounded corners */
		perspective: 1000px; /* Remove this if you don't want the 3D effect */
	}

	/* This container is needed to position the front and back side */
	.flip-box-inner {
		position: relative;
		width: 100%;
		height: 100%;
		text-align: center;
		transition: transform 0.4s;
		transform-style: preserve-3d;
		border-radius: 15px;
	}

	/* Do an horizontal flip on button click */
	.flip-it {
		transform: rotateY(180deg);
	}

	#btn-cont {
		width: 200px;
		padding: 10px 0;
		display: flex;
		justify-content: space-between;
	}

	button {
		background-color: hsl(65, 6%, 40%);
		padding: 10px 10px;
		color: white;
		cursor: pointer;
	}

	button:active {
		background-color: hsl(50, 65%, 25%);
	}

	.loading-screen {
		display: flex;
		justify-content: center;
		align-items: center;
		height: 100vh;
	}

	.loading-screen p {
		font-size: 20px;
	}
</style>
