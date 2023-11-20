<script>
	import { Input } from "flowbite-svelte";
	// import {Anchor} from './Anchor.svelte';

	let headerText = "Create an account";
	let usernameText = "Username";
	let passwordText = "Password";
	// let signUpLine = "Don't have an account?"
	let href;

	let uName = "";
	let pWord = "";
</script>

<div class="loginBackground">
	<div class="text-container">
		<p class="header-text">{headerText}</p>
		<!-- <p class="username-text">{usernameText}</p>
       <p class="password-text">{passwordText}</p> -->
	</div>

	<div class="uName-container">
		<!-- <label for="username">Username:</label> -->
		<Input
			type="text"
			bind:value={uName}
			placeholder={usernameText}
			id="username"
		/>
	</div>

	<div class="pWord-container">
		<!-- <label for="password">Username:</label> -->
		<Input
			type="password"
			bind:value={pWord}
			placeholder={passwordText}
			id="password"
		/>
	</div>

	<div class="createloginButton-container">
		<a href="http://localhost:3000/">
			<button type="button">Sign up</button>
		</a>
	</div>
	<!--     
    <div>
        <p class="signUpLine-container">{signUpLine}
    </div> -->
</div>

<style>
	html,
	body,
	h1,
	h2,
	h3 {
		width: 100%;
		height: 100%;
		margin: 0;
		padding: 0;
	}

	.text-container {
		margin-top: 0px;
		font-family: "Gill Sans", "Gill Sans MT", Calibri, "Trebuchet MS",
			sans-serif;
		text-align: center;
	}

	.header-text {
		font-size: 50px;
		background: linear-gradient(to right, #ff9770, #ff6a7a);
		-webkit-background-clip: text; /* WebKit/Blink browsers */
		background-clip: text;
		color: transparent; /* Hide the original text color */
		font-weight: 350;
	}

	/* .username-text { 
       font-size: 20px;
       margin-top: 120px;
       margin-right: 300px;
       color: black;
       font-weight: 200;  
     }     */

	.uName-container {
		margin-left: 435px;
		margin-top: 75px;
		display: flex;
		align-items: center;
		max-width: 500px;
	}

	/* 
     .password-text {
       font-size: 20px;
       margin-top: 50px;
       margin-right: 300px;
       color: black;
       font-weight: 200; 
     } */

	.pWord-container {
		margin-left: 435px;
		margin-top: 25px;
		display: flex;
		align-items: center;
		max-width: 500px;
	}

	.loginBackground {
		background: linear-gradient(250deg, rgb(25, 27, 126), rgb(45, 90, 125));
		height: 100vh;
		/* justify-content: center; */
		align-items: center;
	}

	button {
		padding: 10px 20px;
		font-size: 18px;
		background-color: #ff9770;
		color: white;
		border: none;
		border-radius: 5px;
		cursor: pointer;
		margin-top: 440px;
		margin-left: -280px;
	}

	.signUpLine-container {
		font-size: 30px;
		margin-top: 80px;
		margin-left: 475px;
		background: linear-gradient(to right, #ff9770, #ff6a7a);
		-webkit-background-clip: text; /* WebKit/Blink browsers */
		background-clip: text;
		color: transparent; /* Hide the original text color */
		font-weight: 350;
	}

	a {
		font-size: 30px;
		background: linear-gradient(to right, #ff9770, #ff6a7a);
		-webkit-background-clip: text; /* WebKit/Blink browsers */
		background-clip: text;
		color: transparent; /* Hide the original text color */
		text-decoration: none; /* Remove underline */
		margin-top: -325px; /* Adjust the margin-top as needed */
		margin-left: 300px;
		display: block; /* Make the link a block element to control its width and positioning */
		text-align: center; /* Center the text */
		text-decoration: underline;
		text-decoration-color: black;
	}
</style>
