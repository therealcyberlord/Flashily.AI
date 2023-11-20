import { writable } from "svelte/store";

export const flashcardStore = writable({
  flashcards: [],
});
