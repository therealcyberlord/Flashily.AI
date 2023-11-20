<script>
	let files;
	export let flashcardCount;
	let prompt = "";

	async function handleFileChange() {
		if (files) {
			const formData = new FormData();
			for (const file of files) {
				formData.append("files", file);
			}
			console.log(flashcardCount);
			try {
				const uploadResponse = await fetch("http://localhost:8000/upload", {
					method: "POST",
					body: formData,
				});
				
				if (prompt === "") {
					prompt = "no specific instruction";
				}
				
				if (uploadResponse.ok) {
					const uploadResult = await uploadResponse.json();
					console.log(uploadResult);

					window.location.href = `/flashcard/${flashcardCount}&${prompt}`;
					// send flashcardCount to /flashcard
				} else {
					console.error("Error uploading files");
				}
			} catch (error) {
				console.error("Error:", error);
			}
		}
	}
</script>

<label for="fileInput" id="uploadButton"> Upload documents </label>

<input
	bind:files
	id="fileInput"
	multiple
	type="file"
	style="display: none"
	on:change={handleFileChange}
/>

{#if files}
	<h2>Selected files:</h2>
	{#each Array.from(files) as file}
		<p>{file.name} ({file.size} bytes)</p>
	{/each}
{/if}

<style>
	/* Add your styles here if needed */
	#fileInput {
		display: none;
	}

	#uploadButton {
		cursor: pointer;
		background: linear-gradient(to right, #ff6a7a, #ff9770);
		color: white;
		padding: 15px 20px; /* Adjust the padding values as needed */
		border-radius: 5px;
		border: none;
		text-align: center;
		text-decoration: none;
		display: inline-block;
		font-size: 18px;
		margin: 4px 2px;
		transition-duration: 0.4s;
		overflow: hidden;
	}

	#uploadButton:hover {
		background: linear-gradient(to right, #ff9770, #ff6a7a);
	}
</style>
