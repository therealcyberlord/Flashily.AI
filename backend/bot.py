from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import DirectoryLoader
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
import json

load_dotenv()


class Bot:
    def __init__(self, temp: str):
        self.path = temp
        self.llm = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0)
        self.qa_chain = None

    def load(self):
        loader = DirectoryLoader(self.path)
        documents = loader.load()

        text_splitter = CharacterTextSplitter(chunk_size=1500, chunk_overlap=0)
        texts = text_splitter.split_documents(documents)

        embeddings = OpenAIEmbeddings()
        vectorstore = Chroma.from_documents(texts, embeddings)
        retriever = vectorstore.as_retriever()
        self.qa_chain = RetrievalQA.from_chain_type(self.llm, retriever=retriever)

    def generate(
        self,
        num_flash_cards: int = 5,
        max_attempts: int = 10,
        optional_instructions: str = "",
    ):
        if len(optional_instructions) > 0:
            query = f"""Based on the document, I want you to create exactly {num_flash_cards} question-answering pairs for me in the following format. In
                    particular, I want you to emphasis on the following instruction: {optional_instructions}
                            
                    if there are 3 questions-answering pairs, it would look like this:
                                
                    [
                        {{"question": "What is the capital of France", "answer": "The capital of France is Paris"}},
                        {{"question": "Did World War II end in 1945", "answer": "True"}},
                        {{"question": "What is an array in computer science", "answer": "An array is a collection of items of same data type stored at contiguous memory locations"}},
                    ],

                    do not include anything other than the json, should return just like the example provided
                    """
        else:
            query = f"""Based on the document, I want you to create exactly {num_flash_cards} question-answering pairs for me in the following format.
                            
                    if there are 3 questions-answering pairs, it would look like this:
                                
                    [
                        {{"question": "What is the capital of France", "answer": "The capital of France is Paris"}},
                         {{"question": "Did World War II end in 1945", "answer": "True"}},
                        {{"question": "What is an array in computer science", "answer": "An array is a collection of items of same data type stored at contiguous memory locations"}},
                    ],

                    do not include anything other than the json, should return just like the example provided
                    """

        for attempt in range(1, max_attempts + 1):
            try:
                res = self.qa_chain({"query": query})
                json_res = json.loads(res["result"].strip())
                return json_res
            except json.JSONDecodeError as e:
                print(
                    f"Failed to generate valid JSON on attempt {attempt}/{max_attempts}: {e}"
                )
        # if we can't generate valid JSON after max_attempts, return an error
        error_response = {
            "error": "Failed to generate valid JSON",
            "message": f"Max attempts ({max_attempts}) reached",
        }

        return error_response
