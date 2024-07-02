import os
from typing import List, Dict, Any
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter


class VectorDB:
    def __init__(self, base_path: str):
        self.base_path = base_path
        self.db = None
        self.embeddings = HuggingFaceEmbeddings()
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        self.current_db_path = None

    def create_or_load_db(self, directory: str):
        """Create a new vector database or load an existing one."""
        db_path = os.path.join(self.base_path, directory, 'vector_db')
        os.makedirs(db_path, exist_ok=True)

        self.db = Chroma(persist_directory=db_path, embedding_function=self.embeddings)
        self.current_db_path = db_path

    def add_document(self, file_path: str, content: str):
        """Add a document to the vector database."""
        if self.db is None:
            raise ValueError("No database loaded. Use create_or_load_db() first.")

        # Split the content into chunks
        docs = self.text_splitter.create_documents([content], metadatas=[{"source": file_path}])

        # Add the documents to the vector store
        self.db.add_documents(docs)

    def search(self, query: str, k: int = 5) -> List[Dict[str, Any]]:
        """Search for similar documents in the vector database."""
        if self.db is None:
            raise ValueError("No database loaded. Use create_or_load_db() first.")

        results = self.db.similarity_search_with_score(query, k=k)

        return [
            {
                'content': doc.page_content,
                'metadata': doc.metadata,
                'score': score
            } for doc, score in results
        ]

    def save(self):
        """Save the current state of the vector database."""
        if self.db is None:
            raise ValueError("No database loaded. Use create_or_load_db() first.")

        self.db.persist()

    def close(self):
        """Close the database connection."""
        if self.db:
            self.save()
            self.db = None
        self.current_db_path = None

    def get_all_documents(self) -> List[Document]:
        """Retrieve all documents from the vector database."""
        if self.db is None:
            raise ValueError("No database loaded. Use create_or_load_db() first.")

        return self.db.get()

    def delete_document(self, document_id: str):
        """Delete a document from the vector database."""
        if self.db is None:
            raise ValueError("No database loaded. Use create_or_load_db() first.")

        self.db.delete([document_id])

    def update_document(self, document_id: str, content: str, metadata: Dict[str, Any]):
        """Update a document in the vector database."""
        if self.db is None:
            raise ValueError("No database loaded. Use create_or_load_db() first.")

        self.delete_document(document_id)
        doc = Document(page_content=content, metadata=metadata)
        self.db.add_documents([doc])