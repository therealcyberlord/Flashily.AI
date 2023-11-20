<script>
	import {
		GradientButton,
		Button,
		Modal,
		Label,
		Input,
		Checkbox,
	} from "flowbite-svelte";
	let formModal = false;
	let prompt = "";
	export let flashcardCount;

	// on submit send the changes to the backend endpoint
	// Function to handle form submission
	async function handleSubmit() {
		// Prevent default behavior
		console.log(flashcardCount);
		event.preventDefault();

		// Perform any actions you need with the form data
		console.log("Form submitted with prompt:", prompt);
		if (prompt.length > 0) {
			// const response = await fetch(
			// `http://localhost:8000/magic?num_flash_cards=${flashcardCount}&optional_instructions=${prompt}`)
			window.location.href = `/flashcard/${flashcardCount}&${prompt}`;
		} else {
			window.location.href = `/flashcard/${flashcardCount}&default`;
		}
	}

	//window.location.href = "/flashcard";
</script>

<GradientButton on:click={() => (formModal = true)}>Magic</GradientButton>

<Modal bind:open={formModal} size="xs" autoclose={true} class="w-full">
	<form on:submit={handleSubmit} class="flex flex-col space-y-6">
		<h3 class="mb-4 text-xl font-medium text-gray-900 dark:text-white">
			How do you want to modify your flashcards?
		</h3>
		<Label class="space-y-2">
			<span>Your prompt</span>
			<Input
				type="text"
				name="prompt"
				placeholder="Make the questions true or false"
				bind:value={prompt}
				required
			/>
		</Label>

		<Button type="submit" class="w-full1" on:click={handleSubmit}
			>Change flashcards</Button
		>
	</form>
</Modal>
