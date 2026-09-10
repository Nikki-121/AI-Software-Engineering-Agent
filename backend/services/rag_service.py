from typing import List


def retrieve_relevant_context(
    query: str,
    documents: List[str],
    top_k: int = 3
):
    """
    Retrieve the most relevant documents for a query.

    This is a lightweight baseline retrieval system.
    It will later be connected to ChromaDB for vector search.
    """

    if not query or not documents:
        return []

    query_words = set(
        query.lower().split()
    )

    scored_documents = []

    for document in documents:

        document_words = set(
            document.lower().split()
        )

        score = len(
            query_words.intersection(document_words)
        )

        scored_documents.append(
            (score, document)
        )

    scored_documents.sort(
        key=lambda item: item[0],
        reverse=True
    )

    return [
        document
        for score, document in scored_documents[:top_k]
        if score > 0
    ]
