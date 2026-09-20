def chunk_text(
    text: str,
    chunk_size: int = 500,
    overlap: int = 50
):
    if overlap >= chunk_size:
        raise ValueError(
            "overlap must be smaller than chunk_size"
        )

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)

        start = end - overlap

    return chunks

def chunk_by_paragraph(
    text: str,
    chunk_size: int = 500
):
    paragraphs = [
        paragraph.strip()
        for paragraph in text.split("\n\n")
        if paragraph.strip()
    ]

    chunks = []
    current_chunk = ""

    for paragraph in paragraphs:

        if not current_chunk:
            current_chunk = paragraph
            continue

        candidate = current_chunk + "\n\n" + paragraph

        if len(candidate) <= chunk_size:
            current_chunk = candidate

        else:
            chunks.append(current_chunk)
            current_chunk = paragraph

    if current_chunk:
        chunks.append(current_chunk)

    return chunks

if __name__ == "__main__":

    text = """
What is the fruit fly connectome, exactly?
The fruit fly connectome is a publicly released map of a Drosophila brain and nerve cord, produced by researchers connected to Google DeepMind. It documents roughly 166,000 neurons and more than 125 million connections between them, essentially a wiring diagram of a real biological brain. The dataset is downloadable, and because it’s structured like a network graph, it can be loaded into a simulation and treated much like any other neural network, including one you can train to perform tasks.

That last part is what turned a niche neuroscience release into an internet hobby project. Within days of it going public, people were running the simulated fly brain through video games, letting it trade stocks, and pointing it at coding tasks. None of these are things a fruit fly brain was built to do. They’re demonstrations of what happens when you take a real, mapped biological neural network and repurpose it the way you’d repurpose an artificial one.

TL;DR
The fruit fly connectome is a real map of a Drosophila brain, roughly 166,000 neurons and 125 million-plus connections, released as a public dataset by Google DeepMind researchers.
Hobbyists are running this connectome inside simulations and training it on new tasks, from email sorting to trading to playing games, using large language models to handle the data prep and training pipeline.
One creator trained the simulated fly brain as an email classifier by feeding it hundreds of labeled email examples across a handful of categories and mapping which “brain regions” activated for each label.
The system worked by pattern-matching character sequences in emails to pre-written template replies, not by generating original text, and topped out around 80% accuracy compared to a small conventional neural network.
The motor circuitry controlling the simulated fly’s movement was kept separate from the part trained on email data, because mixing the two risked breaking the brain’s basic navigation behavior.
Task complexity has a ceiling: attempts to scale past roughly five to ten categories saw performance break down, since a fly brain is orders of magnitude simpler than even a small purpose-built model.
The project raises real ethical questions about whether a simulated biological brain can sense or experience anything, questions nobody can currently answer with confidence.
"""

    chunks = chunk_by_paragraph(
        text,
        chunk_size=150
    )

    for index, chunk in enumerate(chunks):

        print("\n" + "=" * 50)
        print(f"CHUNK {index}")
        print(chunk)