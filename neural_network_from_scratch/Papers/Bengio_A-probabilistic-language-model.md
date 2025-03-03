##### A Neural Probabilistic Language Model.
----
How Does Bengio’s Model Improve Over N-Grams?

In the paper, Bengio proposes a Neural Probabilistic Language Model (NPLM) to address the limitations of *n-gram* models. The key improvements are:
- **Word Embeddings**: Instead of treating words as discrete tokens, Bengio’s model learns dense vector representations, capturing semantic similarities.
- **Generalization**: Neural networks generalize better by sharing parameters across words, unlike n-grams which treat every new sequence as separate.
- **Longer Contexts**: The neural model can capture dependencies beyond a fixed  n -gram window.
Bengio’s model still uses a fixed-size context window (similar to an *n-gram*) but encodes words into a **continuous space**, making probability estimation smoother.
---
A **vector-space representation** is a way of mapping objects (such as words, sentences, documents, or even images) into a multi-dimensional numerical space, where each object is represented as a vector. This representation allows for mathematical operations like similarity calculations, clustering, and transformations.

- Key Concepts:

	1. *Embedding* Objects in a Vector Space:
	    - Each object is mapped to a fixed-length vector of real numbers.
	    - Similar objects are placed closer in the space, while dissimilar ones are farther apart.
   	2. *Dimensionality*:
        - The number of dimensions (features) in the vector space depends on the application.
        - In word embeddings like Word2Vec, GloVe, or FastText, vectors are typically 100-1000 dimensions.
        - In TF-IDF document representation, the dimensionality is equal to the number of unique words (often in the tens or hundreds of thousands).
	3. Mathematical Operations:
        - Cosine similarity, Euclidean distance, dot product, etc., can be used to measure relationships between vectors.

---