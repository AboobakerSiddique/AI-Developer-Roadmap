PROMPT_V1 = """
Classify the customer message as:

billing
technical_support
account
general

Return only the category.

Message:
{message}
"""

PROMPT_V2 = """
Classify the customer message into exactly one category.

Categories:

billing:
Payments, charges, invoices, refunds.

technical_support:
Software bugs, crashes, errors, technical problems.

account:
Login, password, profile, or account settings.

general:
Questions that do not fit the other categories.

Return only the category name.

Message:
{message}
"""

PROMPT_V3 = """
Classify the customer message into exactly one category.

Categories:

billing:
Payments, charges, invoices, refunds.

technical_support:
Software bugs, crashes, errors, technical problems.

account:
Login, password, profile, or account settings.

general:
Questions that do not fit the other categories.

Examples:

"I was charged twice."
→ billing

"The application crashes when I upload a file."
→ technical_support

"I cannot reset my password."
→ account

"What time does support close?"
→ general

Return only the category name.

Message:
{message}
"""