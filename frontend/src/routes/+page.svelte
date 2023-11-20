<script>
	import {
		Heading,
		P,
		A,
		Mark,
		Secondary,
		GradientButton,
		Modal,
		Label,
		Input,
		Button,
	} from "flowbite-svelte";
	import UploadButton from "./uploadButton.svelte";
	let flashcardCount = 0;
	let inputClass = "custom-input";

	function handleFlashcardCountSubmit() {
		// show upload button
		console.log(flashcardCount);
	}
</script>

<div class="background">
	<div class="min-h-screen" />
	<div class="text-center">
		<Heading
			tag="h1"
			class="mb-4 text-[#ff7f50]"
			customSize="text-4xl font-extrabold  md:text-5xl lg:text-6xl "
			>Learn lightning fast with <span class="text-[#87cefa]"
				>Flashily<span /></span
			></Heading
		>
		<center>
			<P class="mb-6 text-lg lg:text-xl sm:px-16 xl:px-48 text-[#87cefa]">
				Unlock the power of rapid learning. Get personalized flashcards in
				seconds and
				<strong>supercharge your knowledge journey</strong>.
			</P></center
		>
		<!-- Step 1: Ask users how many flashcards they want -->
		<div class="space-y-4">
			<Label>
				<span class="mb-6 text-lg lg:text-xl sm:px-16 xl:px-48 text-[#87cefa]"
					>How many flashcards do you want?</span
				>
				<Input
					type="number"
					bind:value={flashcardCount}
					min="1"
					required
					class="mx-auto block w-32 mt-2"
				/>
			</Label>
			<!-- <Button on:click={handleFlashcardCountSubmit}>Next</Button> -->
			<UploadButton {flashcardCount} />
		</div>

		<!-- <UploadButton /> -->
	</div>
</div>

<style>
	.background {
		background: linear-gradient(250deg, rgb(25, 27, 126), rgb(45, 90, 125));
		display: flex;
		height: 100%;
		justify-content: center;
		align-items: center;
	}
</style>
