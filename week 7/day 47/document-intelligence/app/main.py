from app.loaders import load_document
from app.chains import (
    extraction_chain,
    summary_chain,
    topics_chain,
    actions_chain,
)


def main():
    text = load_document("documents/sample.pdf")

    extraction = extraction_chain.invoke({
        "document": text
    })

    summary = summary_chain.invoke({
        "document": text
    })

    topics = topics_chain.invoke({
        "document": text
    })

    actions = actions_chain.invoke({
        "document": text
    })

    print("\n===== INFORMATION EXTRACTION =====\n")
    print(extraction)

    print("\n===== SUMMARY =====\n")
    print(summary)

    print("\n===== KEY TOPICS =====\n")
    print(topics)

    print("\n===== ACTION ITEMS =====\n")
    print(actions)


if __name__ == "__main__":
    main()